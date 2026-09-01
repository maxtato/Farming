# -*- coding: utf-8 -*-
"""
LA CHAINE DES PORTRAITS. Une image de personnage entre, un portrait de jeu sort.
Cinq etapes, chacune verifiable a l oeil sur une planche de controle :

  1. DETOURAGE      le fond blanc part, le sujet reste, les blancs INTERIEURS restent
                    (les dents, le col) : on inonde depuis les bords, on ne seuille pas.
  2. CADRAGE        toutes les images n ont pas la meme taille ni le meme cadrage. On
                    mesure la TETE — pas la boite englobante, qui depend des epaules et
                    des bras tendus — et on met toutes les tetes a la meme hauteur, au
                    meme endroit. C est ce qui fait qu ils se ressemblent d un commerce
                    a l autre.
  3. COUPE          le buste se termine sur une ligne brisee, dans le style facette du
                    jeu. La meme pour tous : c est la mise en page qui doit etre
                    identique, pas seulement la taille.
  4. PIXELS         LA SUITE EST DANS `pixels.py`. L etape tenait ici en deux lignes —
                    `resize(LANCZOS)` puis `quantize(32)` — et ces deux lignes rendaient
                    une image reduite, pas un pixel art : 15,9 % des pixels livres
                    n avaient aucun voisin de leur couleur. Le module voisin fait le
                    travail pour de bon — palette partagee rangee en gammes, reduction
                    par moyenne d aire ponderee par l alpha, aplats, cerne — et il MESURE
                    ce taux d orphelins, qui est le chiffre qui distingue les deux.
                    `pixeliser` ci-dessous reste pour `rendre.py`, qui balaie un lot pour
                    voir ce qu il contient et n a pas besoin d une palette de casting.
  5. POIDS          on encode et on mesure. Rien ne rentre dans le jeu sans son chiffre.
"""
import io, os, sys, json
from collections import deque
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

def charger(chemin, cote=900):
    """ON TRAVAILLE SUR UNE REDUCTION, ET C EST SANS PERTE POUR LE RESULTAT. Les sources
       font trois millions de pixels ; le portrait final en fait trente mille. Detourer
       et mesurer sur la pleine resolution coute cent fois la memoire pour un masque
       qu on va reduire de toute facon — et ce sont ces cent fois qui font tuer le
       processus quand on enchaine les images."""
    im = Image.open(chemin).convert('RGB')
    k = cote / float(max(im.size))
    if k < 1.0:
        im = im.resize((max(1,int(round(im.width*k))), max(1,int(round(im.height*k)))), Image.LANCZOS)
    return im

# ---------- 1. DETOURAGE ------------------------------------------------------
def detourer(im, tol=26, marge=2):
    """Rend un masque alpha (H,W) uint8. Le fond est ce qui RESSEMBLE AUX COINS *et* qui
       est relie au bord : les dents blanches d un rire ressemblent au fond mais sont
       enfermees, elles restent.
       ON NE SEUILLE PLUS SUR LE BLANC. La moitie des planches livrees a un fond blanc
       casse — 242, 239, 237 — et un seuil a 238 ne le voyait pas : le detourage rendait
       le personnage entier, la mesure de tete donnait un pixel, et le cadrage demandait
       une image de quatre-vingt-dix mille pixels de large. On lit donc la couleur du fond
       sur l image meme, et l on appelle fond ce qui s en approche.
       ET ON LA LIT SUR TOUT LE POURTOUR, PAS SUR LES QUATRE COINS. Trois planches du lot
       ont le buste qui DEBORDE PAR LE BAS : leurs deux coins inferieurs sont dans la
       veste, la mediane de quatre coins tombe a mi-chemin entre le beige du fond et le
       brun du vetement, et plus rien ne ressemble au fond. La mediane du pourtour entier
       resiste : il faudrait que le sujet occupe plus de la moitie du tour du cadre."""
    a = np.asarray(im.convert('RGB')).astype(np.int16)
    H0, W0, _ = a.shape
    tour = np.concatenate([a[0], a[-1], a[:, 0], a[:, -1]])
    ref = np.median(tour, axis=0).astype(np.int16)
    clair = (np.abs(a - ref).max(axis=2) <= tol)
    H, W = clair.shape
    # inondation depuis les bords, sur une grille reduite : la BFS python ne tient pas
    # 1,5 million de pixels, elle en tient cent mille sans qu on la sente.
    ech = max(1, int(round(max(H, W) / 420.0)))
    pet = clair[::ech, ::ech]
    ph, pw = pet.shape
    vu = np.zeros((ph, pw), bool)
    f = deque()
    for x in range(pw):
        for y in (0, ph-1):
            if pet[y, x] and not vu[y, x]: vu[y, x] = True; f.append((y, x))
    for y in range(ph):
        for x in (0, pw-1):
            if pet[y, x] and not vu[y, x]: vu[y, x] = True; f.append((y, x))
    while f:
        y, x = f.popleft()
        for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
            b, c = y+dy, x+dx
            if 0 <= b < ph and 0 <= c < pw and pet[b, c] and not vu[b, c]:
                vu[b, c] = True; f.append((b, c))
    # on remonte le masque a la taille reelle, puis on le recale sur le vrai seuil
    gros = np.asarray(Image.fromarray((vu*255).astype(np.uint8)).resize((W, H), Image.BILINEAR))
    fond = (gros > 96) & clair
    # les bords restent du fond quoi qu il arrive : une bordure claire non reliee serait
    # un artefact de l echantillonnage, pas un morceau de personnage.
    fond[:marge, :] = clair[:marge, :]; fond[-marge:, :] = clair[-marge:, :]
    fond[:, :marge] = clair[:, :marge]; fond[:, -marge:] = clair[:, -marge:]
    alpha = np.where(fond, 0, 255).astype(np.uint8)
    # un point d adoucissement pour ne pas garder l escalier du fond d origine
    alpha = np.asarray(Image.fromarray(alpha).filter(ImageFilter.MedianFilter(3)))
    return alpha

# ---------- 2. CADRAGE : mesurer la tete --------------------------------------
def mesurer(alpha):
    """Rend (x0,y0,x1,y1) du sujet, le milieu de la tete et sa hauteur.
       LA TETE, ET NON LA BOITE. Un personnage qui tend le bras a une boite deux fois
       plus large qu un autre : cadrer dessus les mettrait a deux echelles. On lit les
       largeurs ligne a ligne depuis le haut ; la tete est la zone etroite du sommet, et
       les epaules commencent la ou la largeur fait un bond."""
    m = alpha > 127
    ys, xs = np.where(m)
    if len(ys) == 0: raise ValueError('image vide')
    y0, y1, x0, x1 = ys.min(), ys.max(), xs.min(), xs.max()
    larg = m.sum(axis=1).astype(float)
    lmax = larg[y0:y1+1].max()
    # premiere ligne, en descendant, ou la largeur depasse 62 % du maximum : les epaules
    seuil = 0.62 * lmax
    epaules = y1
    for y in range(y0, y1+1):
        if larg[y] > seuil: epaules = y; break
    hTete = max(1, epaules - y0)
    # le milieu de la tete se lit au TIERS de sa hauteur : au front, la ou le crane est
    # centre, et non a la machoire que la barbe ou une echarpe tire de cote.
    yr = min(y1, y0 + hTete // 3)
    ligne = np.where(m[yr])[0]
    cx = float((ligne.min() + ligne.max()) / 2) if len(ligne) else float((x0+x1)/2)
    hSujet = max(1, y1 - y0)
    return dict(x0=int(x0), y0=int(y0), x1=int(x1), y1=int(y1),
                epaules=int(epaules), hTete=int(hTete), cx=cx, lmax=float(lmax),
                hSujet=int(hSujet), part=hTete/float(hSujet),
                colle=bool(y0 <= 1 or x0 <= 1 or x1 >= m.shape[1]-2))

_CASC = None
def _cascades():
    global _CASC
    if _CASC is None:
        import cv2
        d = cv2.data.haarcascades
        _CASC = [cv2.CascadeClassifier(d + n) for n in
                 ('haarcascade_frontalface_default.xml',
                  'haarcascade_frontalface_alt2.xml',
                  'haarcascade_profileface.xml')]
    return _CASC

def visage(im, alpha=None):
    """LE VISAGE EST LE SEUL REPERE QUI VEUILLE DIRE LA MEME CHOSE D UN DESSIN A L AUTRE.
       Mesurer la « tete » par les largeurs echouait sur trois cas qui reviennent tous :
       une casquette plate qui rallonge le crane, une coiffure volumineuse qui le double,
       un cadrage serre ou les epaules commencent tout de suite. Le visage, lui, fait la
       meme fraction du personnage chez tout le monde.
       Rend (x, y, l, h) en pixels de `im`, ou None si aucun detecteur ne mord."""
    import cv2
    g = cv2.cvtColor(np.asarray(im.convert('RGB')), cv2.COLOR_RGB2GRAY)
    g = cv2.equalizeHist(g)
    H, W = g.shape
    best = None
    for c in _cascades():
        for ech in (1.05, 1.12):
            for v in c.detectMultiScale(g, ech, 4, minSize=(int(W*0.10), int(W*0.10))):
                x, y, w, h = [int(t) for t in v]
                if y + h/2 > 0.78*H: continue        # un « visage » dans le buste : non
                if best is None or w*h > best[2]*best[3]: best = (x, y, w, h)
        if best is not None: break                   # le premier detecteur qui mord suffit
    return best

# L ECART INTER-OCULAIRE ETALONNE SUR LA BOITE DE VISAGE.
# Sur les dix-sept planches ou les DEUX detecteurs mordent, le rapport entre l ecart des
# yeux et la largeur de la boite de visage tient dans une fourchette etroite : 0,38 a 0,45,
# mediane 0,41. C est ce qui autorise le deuxieme etage — quand on a la boite mais pas les
# yeux, on DEDUIT l ecart, a huit pour cent pres, ce qui ne se voit pas sur un portrait.
ECART_SUR_VISAGE = 0.41

def ancrer(im, alpha, oeilFn=None):
    """Rend (ecart, cx, cy, origine). Trois etages, du plus sur au plus grossier :
       1. LES YEUX, mesures dans la boite de visage : l echelle vraie.
       2. LA BOITE DE VISAGE seule, multipliee par le rapport etalonne ci-dessus.
       3. LA MESURE DE LARGEURS, quand aucun detecteur ne mord : approximatif, et signale
          comme tel pour qu on le corrige a la main.
       `origine` sert a savoir lesquels relire : c est la seule chose qui distingue un
       portrait mesure d un portrait devine."""
    v = visage(im, alpha)
    if v is not None and oeilFn is not None:
        R = oeilFn(im, v)
        if R: return R['ecart'], R['cx'], R['cy'], 'yeux'
    if v is not None:
        x, y, w, h = v
        return ECART_SUR_VISAGE*w, x + w/2.0, y + 0.46*h, 'visage'
    M = mesurer(alpha)
    return 0.42*M['hTete'], M['cx'], M['y0'] + 0.52*M['hTete'], 'largeur'

def cadrerAncre(im, alpha, W, H, ecartCible=0.150, yYeux=0.318, dx=0.0, dy=0.0, ech=1.0,
                oeilFn=None, ancre=None):
    """Pose le personnage sur l ecart des yeux : meme ecart, meme ligne d yeux, meme axe.
       `ancre` = (ecart, cx, cy) impose a la main quand les detecteurs se trompent."""
    if ancre is not None:
        ecart, cx, cy = ancre[:3]; org = 'main'
    else:
        ecart, cx, cy, org = ancrer(im, alpha, oeilFn)
    k = (ecartCible * W) / float(ecart) * ech
    src = im.convert('RGB')
    nW, nH = max(1,int(round(src.width*k))), max(1,int(round(src.height*k)))
    src = src.resize((nW, nH), Image.LANCZOS)
    al = Image.fromarray(alpha).resize((nW, nH), Image.LANCZOS)
    ox = int(round(W/2.0 - cx*k + dx*W))
    oy = int(round(yYeux*H - cy*k + dy*H))
    fond = Image.new('RGB', (W, H), (255, 255, 255)); aF = Image.new('L', (W, H), 0)
    fond.paste(src, (ox, oy)); aF.paste(al, (ox, oy))
    aF = Image.fromarray(np.minimum(np.asarray(aF), np.asarray(masqueCadre(W, H))))
    out = fond.copy(); out.putalpha(aF)
    return out, dict(ecart=ecart, cx=cx, cy=cy, source=org, k=k)

# ---------- 3. LA COUPE ANGULAIRE ---------------------------------------------
# LA LIGNE DU BAS EST CONVEXE, ET ELLE NE REVIENT JAMAIS SUR ELLE-MEME.
# Premiere version : cinq points qui montaient et redescendaient tour a tour, 0,906 puis
# 0,858 puis 0,947. Le joueur : « fait un arrondi legerement octogonal, pas des dents de
# scie. » Il a raison, et la raison est geometrique : une ligne brisee qui alterne les deux
# sens EST une denture, quelle que soit la longueur des dents. Ce qui fait la coupe de
# l image de reference, c est qu elle est CONVEXE de bout en bout — elle descend, elle
# court a plat, elle remonte, et pas une fois elle ne rebrousse.
# Six points, cinq cordes : deux biseaux courts aux angles, un fond presque plat au milieu,
# deux montees vers les bords. C est le bas d un octogone dont on aurait adouci les angles
# — assez droit pour rester dans le style facette du jeu, assez ouvert pour ne pas mordre.
# Le fond n est pas horizontal et les deux biseaux n ont pas la meme largeur : une symetrie
# parfaite se lirait comme un gabarit, pas comme une coupe.
# ELLE N EST VUE QUE SUR [0,15 ; 0,85]. Aux bords du cadre le buste est deja fini : les deux
# points extremes ne servent qu a fermer le polygone, et leur hauteur ne se voit pas.
COUPE = [(0.000, 0.836), (0.122, 0.902), (0.345, 0.945), (0.630, 0.951),
         (0.868, 0.914), (1.000, 0.843)]

def masqueCadre(W, H, coupe=COUPE):
    """Le masque garde TOUT ce qui est au-dessus de la ligne : on ferme le polygone par
       les deux coins du haut, et la ligne se parcourt de droite a gauche pour que le
       contour tourne dans un seul sens."""
    m = Image.new('L', (W, H), 0)
    ImageDraw.Draw(m).polygon([(0, 0), (W, 0)] + [(x*W, y*H) for x, y in reversed(coupe)],
                              fill=255)
    return m

def coupeConvexe(coupe=COUPE):
    """Le controle qui empeche la denture de revenir : la ligne descend jusqu a son point
       bas puis remonte, sans jamais changer de sens deux fois."""
    y = [p[1] for p in coupe]
    bas = y.index(max(y))
    return (all(y[i] <= y[i+1] for i in range(bas)) and
            all(y[i] >= y[i+1] for i in range(bas, len(y)-1)))

def cadrer(im, alpha, W, H, hVisage=0.255, yVisage=0.300, dx=0.0, dy=0.0, ech=1.0,
           boite=None):
    """Pose le personnage dans un cadre W x H : meme taille de VISAGE, meme hauteur d yeux,
       meme axe. `dx`/`dy`/`ech` laissent corriger un cas particulier a la main, et
       `boite` impose le visage quand le detecteur s est trompe.
       `hVisage` : la hauteur du visage en fraction du cadre.
       `yVisage` : ou tombe le CENTRE du visage, en fraction du cadre."""
    v = boite or visage(im, alpha)
    if v is not None:
        vx, vy, vw, vh = v
        k = (hVisage * H) / float(vh) * ech
        cxs, cys = vx + vw/2.0, vy + vh/2.0
        src = im.convert('RGB')
        nW, nH = max(1,int(round(src.width*k))), max(1,int(round(src.height*k)))
        src = src.resize((nW, nH), Image.LANCZOS)
        al = Image.fromarray(alpha).resize((nW, nH), Image.LANCZOS)
        ox = int(round(W/2.0 - cxs*k + dx*W))
        oy = int(round(yVisage*H - cys*k + dy*H))
        fond = Image.new('RGB', (W, H), (255, 255, 255))
        aFond = Image.new('L', (W, H), 0)
        fond.paste(src, (ox, oy)); aFond.paste(al, (ox, oy))
        aFond = Image.fromarray(np.minimum(np.asarray(aFond), np.asarray(masqueCadre(W, H))))
        out = fond.copy(); out.putalpha(aFond)
        return out, dict(visage=v, k=k, source='visage')
    return cadrerParLargeur(im, alpha, W, H, dx=dx, dy=dy, ech=ech)

def cadrerParLargeur(im, alpha, W, H, hauteurTete=0.430, hautTete=0.045, dx=0.0, dy=0.0, ech=1.0):
    """Le repli, quand aucun detecteur ne mord : on retombe sur la mesure de largeurs."""
    M = mesurer(alpha)
    # LA MESURE DE TETE PEUT ECHOUER, ET IL FAUT QUE CA SE VOIE. Une image dont le sujet
    # touche le haut du cadre donne une tete d un pixel, donc un agrandissement de cent :
    # de quoi demander une image de quatre-vingt-dix mille pixels de large et faire tuer le
    # processus. On refuse plutot que d essayer.
    if M['part'] < 0.12 or M['part'] > 0.90:
        raise ValueError('tete invraisemblable (%.0f %% du sujet) : image de travers, '
                         'sujet colle au bord, ou ce n est pas un portrait' % (100*M['part']))
    k = (hauteurTete * H) / M['hTete'] * ech
    src = im.convert('RGB')
    nW, nH = max(1, int(round(src.width*k))), max(1, int(round(src.height*k)))
    src = src.resize((nW, nH), Image.LANCZOS)
    al = Image.fromarray(alpha).resize((nW, nH), Image.LANCZOS)
    # le sommet du crane a `hautTete`, l axe de la tete au milieu
    ox = int(round(W/2 - M['cx']*k + dx*W))
    oy = int(round(hautTete*H - M['y0']*k + dy*H))
    fond = Image.new('RGB', (W, H), (255, 255, 255))
    aFond = Image.new('L', (W, H), 0)
    fond.paste(src, (ox, oy)); aFond.paste(al, (ox, oy))
    aFond = Image.fromarray(np.minimum(np.asarray(aFond), np.asarray(masqueCadre(W, H))))
    out = fond.copy(); out.putalpha(aFond)
    return out, M

# ---------- 4. PIXELS ----------------------------------------------------------
def pixeliser(rgba, larg, couleurs=48, palette=None):
    """Reduit a `larg` pixels de large et met en aplats. Aucun tramage : le tramage
       double le nombre de motifs et ruine le codage par plages."""
    W, H = rgba.size
    haut = int(round(larg * H / W))
    pet = rgba.resize((larg, haut), Image.LANCZOS)
    a = np.asarray(pet)[:, :, 3]
    rgb = Image.fromarray(np.asarray(pet)[:, :, :3])
    if palette is None:
        q = rgb.quantize(colors=couleurs, method=Image.MEDIANCUT, dither=Image.NONE)
        pal = np.asarray(q.getpalette()[:couleurs*3], np.uint8).reshape(-1, 3)
        idx = np.asarray(q)
    else:
        pal = np.asarray(palette, np.uint8)
        idx = plusProche(np.asarray(rgb), pal)
    idx = idx.astype(np.uint8)
    opaque = (a > 127)
    return idx, pal, opaque

def plusProche(img, pal):
    h, w, _ = img.shape
    p = pal.astype(np.int32)
    d = img.reshape(-1, 1, 3).astype(np.int32) - p.reshape(1, -1, 3)
    return np.argmin((d*d).sum(axis=2), axis=1).reshape(h, w)

def rendre(idx, pal, opaque, zoom=1):
    h, w = idx.shape
    rgb = pal[idx]
    im = Image.fromarray(rgb.astype(np.uint8), 'RGB')
    im.putalpha(Image.fromarray((opaque*255).astype(np.uint8)))
    return im.resize((w*zoom, h*zoom), Image.NEAREST) if zoom > 1 else im

# ---------- 5. POIDS : codage par plages --------------------------------------
def coder(idx, opaque, nPal):
    """Un octet de transparence en plus de la palette, puis des plages (valeur, longueur)
       en base 64 maison. On code LIGNE A LIGNE : un portrait a de longues plages
       horizontales, et couper aux lignes evite de coder des sauts de 200."""
    VIDE = nPal                      # l indice juste apres la palette dit « rien »
    plat = np.where(opaque, idx, VIDE).ravel()
    plages = []
    v = plat[0]; n = 1
    for x in plat[1:]:
        if x == v and n < 4095: n += 1
        else: plages.append((int(v), n)); v = x; n = 1
    plages.append((int(v), n))
    return plages

def enBase64(plages, nPal):
    """(valeur, longueur) -> deux a quatre caracteres. Longueur 1..63 sur un caractere,
       au-dela deux. C est un format du jeu, pas un standard : il n a qu a etre lu par
       les dix lignes de decodeur qui l accompagnent."""
    A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    out = []
    for v, n in plages:
        out.append(A[v])
        if n <= 63: out.append(A[n])
        else: out.append(A[63]); out.append(A[n >> 6]); out.append(A[n & 63])
    return ''.join(out)
