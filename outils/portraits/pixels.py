# -*- coding: utf-8 -*-
"""
DU PIXEL ART, ET NON UNE IMAGE REDUITE.

La premiere livraison faisait ceci : `resize(LANCZOS)` puis `quantize(32)`. Le joueur :
« attention, les fichiers pixel art doivent etre des vrais pixel art, pas juste un
retravail en png. » Il a raison, et cela se MESURE. Sur `restaurant-neutre`, 15,9 % des
pixels opaques n avaient AUCUN de leurs quatre voisins de leur propre couleur. Un pixel
isole, c est la signature d un reechantillonnage : personne ne pose un pixel seul a la
main. Du vrai pixel art tient sous les 4 %.

Trois choses distinguent un dessin en pixels d une photo reduite, et la chaine les fait
toutes les trois :

  A. LA PALETTE EST DECIDEE, PARTAGEE, ET RANGEE EN GAMMES.
     Trente-deux couleurs trouvees par statistique DANS CHAQUE IMAGE laissent chaque
     facette du rendu low-poly garder sa nuance : on obtient un degrade en trente-deux
     marches, pas des aplats. Ici la palette est UNE pour tout le casting, elle est batie
     en gammes — une famille de teinte, cinq marches de clarte —, et les marches sont
     REGULARISEES : clarte a pas constant, saturation qui se tient dans l ombre, teinte
     qui bascule vers le froid en bas et vers le chaud en haut. C est la facon dont on
     remplit un pixel art a la main, et c est ce que « avec tes propres couleurs » veut
     dire. Un commerce n en touche qu une vingtaine : le reste devient de l aplat tout
     seul, parce que deux facettes voisines tombent sur la meme marche.

  B. LA REDUCTION EST UNE MOYENNE D AIRE, PONDEREE PAR L ALPHA.
     LANCZOS sonne — il invente des pixels plus clairs que tout ce qui l entoure au bord
     d un contraste — et il moyenne le sujet AVEC LE FOND BLANC sur tout le pourtour, ce
     qui pose un liseré pale autour du personnage. Une moyenne de bloc ne sonne pas, et
     ponderee par l alpha elle ne regarde que le sujet. Le cadre fait exactement trois
     fois la fiche : chaque pixel livre est la moyenne honnete de neuf.

  C. LE DESSIN EST NETTOYE, PUIS CERNE.
     On efface les pixels orphelins — ceux dont aucun voisin n a la couleur —, on bouche
     les trous d un pixel dans la silhouette, et l on assombrit d UNE MARCHE DE SA PROPRE
     GAMME le liseré exterieur. Ce cerne-la n est pas un noir plaque : il garde la teinte
     de ce qu il borde, et c est lui qui fait tenir une figure a cette taille.
"""
import json, os
import numpy as np
from PIL import Image

# ---------- Oklab : la seule facon de comparer deux couleurs sans se tromper ----
# Un ecart euclidien en RVB dit que le bleu marine est plus proche du noir que le brun
# clair ne l est du beige. Oklab est fait pour que la distance corresponde a ce que l oeil
# voit, et toute la chaine — le regroupement en familles, l accrochage a la palette, le
# choix du voisin de remplacement — s y fait.
def _lin(c):
    return np.where(c <= 0.04045, c/12.92, ((c + 0.055)/1.055)**2.4)

def _delin(c):
    return np.where(c <= 0.0031308, c*12.92, 1.055*np.maximum(c, 0)**(1/2.4) - 0.055)

def oklab(rgb):
    c = _lin(np.asarray(rgb, np.float64)/255.0)
    r, g, b = c[..., 0], c[..., 1], c[..., 2]
    l = np.cbrt(0.4122214708*r + 0.5363325363*g + 0.0514459929*b)
    m = np.cbrt(0.2119034982*r + 0.6806995451*g + 0.1073969566*b)
    s = np.cbrt(0.0883024619*r + 0.2817188376*g + 0.6299787005*b)
    return np.stack([0.2104542553*l + 0.7936177850*m - 0.0040720468*s,
                     1.9779984951*l - 2.4285922050*m + 0.4505937099*s,
                     0.0259040371*l + 0.7827717662*m - 0.8086757660*s], -1)

def _deOklabBrut(lab):
    """Rend le RVB en 0..1 SANS le borner : c est ce qui permet de savoir si une couleur
       tient dans le gamut, ce que la version bornee ne peut plus dire."""
    L, A, B = lab[..., 0], lab[..., 1], lab[..., 2]
    l = (L + 0.3963377774*A + 0.2158037573*B)**3
    m = (L - 0.1055613458*A - 0.0638541728*B)**3
    s = (L - 0.0894841775*A - 1.2914855480*B)**3
    r = +4.0767416621*l - 3.3077115913*m + 0.2309699292*s
    g = -1.2684380046*l + 2.6097574011*m - 0.3413193965*s
    b = -0.0041960863*l - 0.7034186147*m + 1.7076147010*s
    return _delin(np.stack([r, g, b], -1))

def deOklab(lab):
    return np.clip(np.round(_deOklabBrut(lab)*255.0), 0, 255).astype(np.uint8)

def enGamut(L, teinte, C, marge=1e-4):
    """LA PLUS FORTE CHROMA QUI TIENNE ENCORE DANS LE sRGB, a clarte et teinte figees.

       Monter la chroma sans regarder le gamut ne rend pas la couleur plus vive : elle
       sort de l ecran, le bornage ecrase une composante sur 255 ou sur 0, et ce qui
       revient a une teinte DIFFERENTE et une clarte fausse. Un jaune pousse devient vert,
       un bleu sombre devient violet. On dichotomise donc sur la chroma — la teinte et la
       clarte, elles, ne bougent pas d un iota : c est la definition meme d un repli dans
       le gamut, et c est pour cela que le nuancier reste range en gammes apres coup."""
    v = np.array([L, C*np.cos(teinte), C*np.sin(teinte)])
    rgb = _deOklabBrut(v)
    if rgb.min() >= -marge and rgb.max() <= 1 + marge: return float(C)
    lo, hi = 0.0, float(C)
    for _ in range(24):
        m = (lo + hi)/2
        rgb = _deOklabBrut(np.array([L, m*np.cos(teinte), m*np.sin(teinte)]))
        if rgb.min() >= -marge and rgb.max() <= 1 + marge: lo = m
        else: hi = m
    return lo

# ---------- A. LA PALETTE ------------------------------------------------------
NFAM, NMARCHE, NGRIS = 10, 6, 7
SEUIL_GRIS = 0.035            # en dessous de cette chroma, c est un neutre
# L ECHELLE DE CLARTE EST A MOITIE MESUREE, A MOITIE REGULIERE, ET C EST LE COEUR DE
# L AFFAIRE. Premiere tentative : six quantiles des clartes de la famille. Resultat, un
# nuancier ou toutes les gammes avaient trois marches quasi noires — parce qu un rendu
# facette passe l essentiel de sa surface dans l ombre, et que les quantiles suivent la
# masse. Une gamme peinte a la main ne suit pas la masse : elle ECHELONNE. Deuxieme
# tentative, l inverse : six marches a pas constant entre le plus sombre et le plus clair.
# Le teint y perdait — la peau vit entre 0,65 et 0,82 de clarte, elle n avait plus que deux
# marches pour tout un visage.
# On prend la moyenne des deux : les marches se serrent la ou la couleur existe vraiment,
# sans jamais laisser un bout de la gamme sans marche.
MELANGE    = 0.5              # 0 = tout mesure, 1 = tout regulier
# ET AUCUNE GAMME DE COULEUR NE DESCEND AU NOIR. Avec un plancher a 0,17, les dix familles
# posaient chacune une marche presque noire : dix cases de palette pour dix noirs que l oeil
# ne distingue pas. Un dessinateur n en peint qu un et le partage. Le plancher est donc a
# 0,27 — une ombre encore coloree —, et ce qui est plus sombre que ca tombe sur la gamme des
# neutres, qui est la pour ca.
L_MIN, L_MAX = 0.27, 0.94
# La marche du bas bascule vers le froid, celle du haut vers le chaud : c est ce que fait
# la lumiere du jour, et c est la convention qui rend une gamme peinte a la main lisible.
VIRAGE     = (-0.14, -0.08, -0.03, +0.02, +0.06, +0.10)   # radians de teinte, par marche
# Une ombre desaturee est morte. On tient la chroma dans le bas de la gamme et on la lache
# dans les tres hautes lumieres, ou elle vire au blanc.
CHROMA     = (1.02, 1.12, 1.08, 0.98, 0.84, 0.58)
# LE PUNCH, ET IL SE MESURE. Le joueur : « change le ton des couleurs pour avoir des
# couleurs un peu plus punchy, dans le style de couleur du reste du jeu. » Le jeu donne le
# barème : ses trois boutons — l or #E8B33A, le vert #5C8C3F, le rouge #C2503E — tiennent
# a 0,138 de chroma en Oklab, quand les gammes des portraits tenaient a 0,083. Il manquait
# donc les deux tiers du chemin, et « un peu plus punchy » se chiffre : x 1,55, ce qui
# porte la moyenne des gammes a 0,128 — le voisinage des boutons, sans les depasser.
# CE N EST PAS UN MULTIPLICATEUR SEC : chaque marche repasse par `enGamut`, qui rend la
# plus forte chroma tenant dans le sRGB a SA clarte et SA teinte. Sans ce repli, les
# marches claires et les marches sombres sortent de l ecran, le bornage ecrase une
# composante, et la gamme se tord — un jaune pousse vire au vert.
# ET LE GAIN DEPEND DE LA CHROMA DEJA PRESENTE, sans quoi il cuit les visages. Un gain sec
# de 1,55 reveille bien la chemise rouge du Restaurant — c est ce qu on demandait — mais il
# porte AUSSI le teint a la meme enseigne, et une peau a 1,55 vire a l orange fluorescent.
# La regle du dessinateur est l inverse : ce qui est deja colore devient franc, ce qui est
# naturellement sourd — la peau, la pierre, le lin — le reste. Le gain court donc de 1,10
# pour une famille presque grise a 2,00 pour une famille pleinement coloree, la bascule se
# faisant a CREF, la chroma d une etoffe teinte.
PUNCH_MIN, PUNCH_MAX, CREF = 1.10, 2.00, 0.115

def punch(C):
    return PUNCH_MIN + (PUNCH_MAX - PUNCH_MIN)*min(1.0, C/CREF)
# ET LES NEUTRES SE RECHAUFFENT AVEC. Le jeu n a pas un seul gris pur : son papier est
# creme (#CFC3A4, chroma 0,044) et son voile tire au bleu. Des neutres a 0,005 de chroma
# a cote de gammes a 0,128 se lisent comme du carton photocopie.
NEUTRE     = 3.2
# LES NEUTRES NE SE MESURENT PAS, ILS SE POSENT. Mesures, ils suivaient eux aussi la masse :
# le tableau d ardoise du Restaurant et les vestes sombres donnaient cinq gris presque noirs
# et un blanc, sans rien entre les deux — donc pas de quoi peindre une blouse blanche ni un
# reflet de peau. Sept marches a pas constant du presque-noir au blanc, et le probleme
# n existe plus.
GRIS_L     = (0.16, 0.31, 0.45, 0.59, 0.72, 0.85, 0.98)

def _familles(lab, poids, n=NFAM, tours=40):
    """Regroupe les TEINTES, pas les couleurs : on travaille sur l angle, pondere par la
       chroma pour qu un beige presque gris ne tire pas le centre d une famille."""
    h = np.arctan2(lab[:, 2], lab[:, 1])
    c = np.hypot(lab[:, 1], lab[:, 2])
    ctr = np.linspace(-np.pi, np.pi, n, endpoint=False) + np.pi/n
    for _ in range(tours):
        d = np.abs(np.angle(np.exp(1j*(h[:, None] - ctr[None, :]))))
        a = np.argmin(d, axis=1)
        for k in range(n):
            s = (a == k)
            if s.sum() > 20:
                w = poids[s]*c[s]
                v = (np.exp(1j*h[s])*w).sum()
                if abs(v) > 1e-9: ctr[k] = np.angle(v)
    return ctr, a

def batir(echantillons, poids=None):
    """`echantillons` : un tableau (N,3) de pixels RVB pris sur TOUT le casting.
       Rend la palette (M,3) uint8 et la table des gammes."""
    lab = oklab(echantillons.astype(np.float64))
    if poids is None: poids = np.ones(len(lab))
    chroma = np.hypot(lab[:, 1], lab[:, 2])
    gris = chroma < SEUIL_GRIS
    pal, gammes = [], []

    # les neutres : une seule gamme, du presque-noir au blanc, tres legerement viree
    for i, L in enumerate(GRIS_L):
        t = i/(NGRIS - 1.0)
        # le noir tire au bleu, le blanc a la creme : un gris pur a l ecran fait du carton
        a_, b_ = 0.005*(t - 0.35)*NEUTRE, 0.014*(t - 0.30)*NEUTRE
        h = np.arctan2(b_, a_)
        C = enGamut(L, h, float(np.hypot(a_, b_)))
        pal.append(deOklab(np.array([L, C*np.cos(h), C*np.sin(h)])))
    gammes.append(list(range(len(pal))))

    ch = lab[~gris]; pch = poids[~gris]
    ctr, aff = _familles(ch, pch)
    for k in range(NFAM):
        s = (aff == k)
        if s.sum() < 60:                       # famille vide : on la saute proprement
            gammes.append([]); continue
        Ls = ch[s, 0]; Cs = np.hypot(ch[s, 1], ch[s, 2])
        base = float(np.quantile(Cs, 0.62))
        lo = max(float(np.quantile(Ls, 0.04)), L_MIN)
        hi = min(float(np.quantile(Ls, 0.97)), L_MAX)
        if hi - lo < 0.10: lo, hi = max(L_MIN, lo - 0.05), min(L_MAX, hi + 0.05)
        qs = np.linspace(0.05, 0.95, NMARCHE)
        idx = []
        for i in range(NMARCHE):
            mesuree = float(np.quantile(Ls, qs[i]))
            reguliere = lo + (hi - lo)*i/(NMARCHE - 1.0)
            L = (1 - MELANGE)*mesuree + MELANGE*reguliere
            hue = ctr[k] + VIRAGE[i]
            C = enGamut(L, hue, base*CHROMA[i]*punch(base))
            idx.append(len(pal))
            pal.append(deOklab(np.array([L, C*np.cos(hue), C*np.sin(hue)])))
        gammes.append(idx)
    P = np.asarray(pal, np.uint8)
    # deux couleurs identiques dans la palette ne servent a rien : on les fond
    P, gammes = _dedoubler(P, gammes)
    return P, gammes

def _dedoubler(P, gammes):
    vus, ren, garde = {}, {}, []
    for i, c in enumerate(map(tuple, P)):
        if c in vus: ren[i] = vus[c]
        else: vus[c] = len(garde); ren[i] = len(garde); garde.append(P[i])
    return np.asarray(garde, np.uint8), [[ren[i] for i in g] for g in gammes]

# ---------- B. LA REDUCTION PAR MOYENNE D AIRE ---------------------------------
def reduire(rgba, larg):
    """Cadre -> grille de la fiche. Le cadre fait un multiple entier de la fiche : chaque
       pixel rendu est la moyenne d un bloc, ponderee par l alpha, ce qui interdit au fond
       de deteindre sur le contour."""
    W, H = rgba.size
    k = W // larg
    if k < 1 or W % larg: raise ValueError('le cadre doit faire un multiple entier de la fiche')
    haut = H // k
    a = np.asarray(rgba).astype(np.float64)[:haut*k, :larg*k]
    rgb, al = a[:, :, :3], a[:, :, 3]/255.0
    bloc = lambda x: x.reshape(haut, k, larg, k, -1).sum(axis=(1, 3))
    poids = bloc(al[:, :, None])[:, :, 0]
    somme = bloc(rgb*al[:, :, None])
    couv = poids/float(k*k)
    moy = np.where(poids[:, :, None] > 1e-6, somme/np.maximum(poids, 1e-6)[:, :, None], 255.0)
    return moy, couv

# ---------- accrochage ---------------------------------------------------------
def accrocher(rgb, pal, masque=None):
    """Chaque pixel prend la couleur de palette la plus proche EN OKLAB."""
    lab = oklab(rgb).reshape(-1, 3)
    pl = oklab(pal.astype(np.float64))
    d = lab[:, None, :] - pl[None, :, :]
    return np.argmin((d*d).sum(axis=2), axis=1).reshape(rgb.shape[:2]).astype(np.int16)

def _boite(m, r):
    """Somme sur une fenetre carree, par sommes cumulees : le comptage de familles se fait
       sur toute l image d un coup au lieu de boucler sur chaque pixel."""
    p = np.pad(m, r)
    c = np.cumsum(np.cumsum(p, 0), 1)
    c = np.pad(c, ((1, 0), (1, 0)))
    n = 2*r + 1
    return c[n:, n:] - c[:-n, n:] - c[n:, :-n] + c[:-n, :-n]

def unifier(rgb, idx, op, pal, gammes, rayon=2, tol=0.060, tours=3):
    """UNE ETOFFE, UNE GAMME. Le rendu low-poly d origine peint une chemise rouge en
       cinquante facettes dont la teinte oscille ; accrochee pixel par pixel, une facette
       sur deux tombait dans la famille orange et l autre dans la rouge, et l on obtenait
       un damier de deux couleurs franches la ou il n y a qu un tissu. C est exactement le
       defaut que le pixel art ne fait pas : un dessinateur choisit UNE gamme pour un
       vetement et n en joue que les marches.
       On regarde donc, autour de chaque pixel, quelle FAMILLE domine ; si la meilleure
       marche de cette famille-la n est pas plus loin que `tol` de la couleur d origine, le
       pixel la prend. La marche de clarte, elle, reste libre : c est le modele qui doit
       survivre, pas la teinte accidentelle."""
    fam = np.full(len(pal), -1, np.int64)
    for f, g in enumerate(gammes):
        for c in g: fam[c] = f
    lab = oklab(rgb)
    pl = oklab(pal.astype(np.float64))
    d = np.sqrt(np.maximum(((lab[:, :, None, :] - pl[None, None, :, :])**2).sum(-1), 0))
    nf = len(gammes)
    idx = idx.astype(np.int64)
    for _ in range(tours):
        fp = fam[idx]
        cnt = np.stack([_boite(((fp == f) & op).astype(np.float32), rayon)
                        for f in range(nf)], -1)
        dom = np.argmax(cnt, axis=2)
        actuel = np.take_along_axis(d, idx[:, :, None], 2)[:, :, 0]
        bouge = 0
        for f in range(nf):
            if not gammes[f]: continue
            sel = op & (dom == f) & (fp != f)
            if not sel.any(): continue
            cols = np.asarray(gammes[f], np.int64)
            sub = d[:, :, cols]
            j = np.argmin(sub, axis=2)
            mieux = cols[j]
            ecart = np.take_along_axis(sub, j[:, :, None], 2)[:, :, 0] - actuel
            ok = sel & (ecart <= tol)
            idx = np.where(ok, mieux, idx)
            bouge += int(ok.sum())
        if not bouge: break
    return idx.astype(np.int16)

# ---------- C. LE NETTOYAGE ET LE CERNE ----------------------------------------
def nettoyerAlpha(op, tours=2):
    """Un pixel opaque seul au milieu du vide n est pas un dessin, c est un reste
       d echantillonnage ; un trou d un pixel dans une veste non plus."""
    for _ in range(tours):
        v = _voisins4(op.astype(np.int8))
        op = np.where(v <= 1, False, np.where(v >= 4, True, op))
    return op

def _voisins4(x):
    p = np.pad(x, 1)
    return p[:-2, 1:-1] + p[2:, 1:-1] + p[1:-1, :-2] + p[1:-1, 2:]

def deparasiter(idx, op, pal, tours=2):
    """LE PIXEL ORPHELIN. Aucun de ses quatre voisins n a sa couleur : il ne peut pas
       avoir ete pose a la main. On lui donne celle de ses voisins qui domine, et a
       egalite la plus proche de lui — ce qui garde les degrades dans le bon sens."""
    lab = oklab(pal.astype(np.float64))
    H, W = idx.shape
    out = idx.copy()
    for _ in range(tours):
        cur = out.copy()
        pi = np.pad(cur, 1, constant_values=-1)
        po = np.pad(op, 1, constant_values=False)
        vois = [(pi[:-2, 1:-1], po[:-2, 1:-1]), (pi[2:, 1:-1], po[2:, 1:-1]),
                (pi[1:-1, :-2], po[1:-1, :-2]), (pi[1:-1, 2:], po[1:-1, 2:])]
        pareil = np.zeros((H, W), np.int8)
        for v, m in vois: pareil += ((v == cur) & m).astype(np.int8)
        seuls = op & (pareil == 0)
        ys, xs = np.where(seuls)
        for y, x in zip(ys, xs):
            cand = {}
            for v, m in vois:
                if m[y, x]: cand[int(v[y, x])] = cand.get(int(v[y, x]), 0) + 1
            if not cand: continue
            top = max(cand.values())
            ex = [c for c, n in cand.items() if n == top]
            if len(ex) > 1:
                d = [((lab[c] - lab[cur[y, x]])**2).sum() for c in ex]
                ex = [ex[int(np.argmin(d))]]
            out[y, x] = ex[0]
    return out

def cerner(idx, op, gammes, force=1):
    """LE CERNE PREND LA TEINTE DE CE QU IL BORDE. Le liseré exterieur descend d une
       marche DANS SA PROPRE GAMME : la manche bleue est cernee de bleu sombre, la joue
       de brun. Un noir plaque tout autour ferait un autocollant."""
    bas = {}
    for g in gammes:
        for i, c in enumerate(g): bas[c] = g[max(0, i - force)]
    po = np.pad(op, 1, constant_values=False)
    bord = op & ~(po[:-2, 1:-1] & po[2:, 1:-1] & po[1:-1, :-2] & po[1:-1, 2:])
    out = idx.copy()
    ys, xs = np.where(bord)
    for y, x in zip(ys, xs): out[y, x] = bas.get(int(idx[y, x]), int(idx[y, x]))
    return out

# ---------- mesure -------------------------------------------------------------
def orphelins(idx, op):
    """Le chiffre qui dit si c est du pixel art : la part de pixels dont aucun des quatre
       voisins n a la couleur."""
    pi = np.pad(idx, 1, constant_values=-1); po = np.pad(op, 1, constant_values=False)
    pareil = (((pi[:-2, 1:-1] == idx) & po[:-2, 1:-1]).astype(np.int8) +
              ((pi[2:, 1:-1] == idx) & po[2:, 1:-1]) +
              ((pi[1:-1, :-2] == idx) & po[1:-1, :-2]) +
              ((pi[1:-1, 2:] == idx) & po[1:-1, 2:]))
    n = int(op.sum())
    return (int((op & (pareil == 0)).sum())/max(n, 1), n)

def dessiner(idx, op, pal, zoom=1):
    im = Image.fromarray(pal[np.clip(idx, 0, len(pal)-1)].astype(np.uint8), 'RGB')
    im.putalpha(Image.fromarray((op*255).astype(np.uint8)))
    return im.resize((im.width*zoom, im.height*zoom), Image.NEAREST) if zoom > 1 else im

def png8(idx, op, pal):
    m = len(pal)
    q = Image.fromarray(np.where(op, idx, m).astype(np.uint8), 'P')
    q.putpalette((list(np.asarray(pal, np.uint8).ravel()) + [0, 0, 0] + [0]*768)[:768])
    return q, m
