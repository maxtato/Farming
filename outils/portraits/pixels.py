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
# PLUS DE NUANCES, ET PLUS DE FAMILLES. Le joueur : « fais plus de nuances de couleurs. »
# On passe de dix familles a douze — le rouge et l orange n avaient qu une frontiere pour
# eux deux, le vert de l atelier et celui du marche partageaient une gamme — et de six
# marches de clarte a huit, ce qui reduit le pas d un huitieme a un onzieme de la plage :
# un modele de joue ou de manche a trois valeurs la ou il en avait deux.
# 12 x 8 + 9 = 105 couleurs, la ou il y en avait 67. Une palette indexee en tient 256.
NFAM, NMARCHE, NGRIS = 12, 8, 9
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
VIRAGE     = (-0.14, -0.11, -0.08, -0.04, -0.01, +0.03, +0.07, +0.10)  # radians, par marche
# Une ombre desaturee est morte. On tient la chroma dans le bas de la gamme et on la lache
# dans les tres hautes lumieres, ou elle vire au blanc.
CHROMA     = (1.00, 1.08, 1.13, 1.11, 1.04, 0.94, 0.80, 0.55)
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
PUNCH_MIN, PUNCH_MAX, CREF = 1.10, 1.55, 0.115
# ET L ON NE COLLE JAMAIS A LA FRONTIERE DU GAMUT. `enGamut` rend la plus forte chroma
# tenant dans le sRGB ; demander plus que cela revient donc a poser la couleur EXACTEMENT
# sur la frontiere — et la frontiere, aux clartes basses, c est l encre pure. Avec douze
# familles au lieu de dix, chaque famille est plus serree, sa chroma mesuree monte, le gain
# la porte au-dela du possible, et toutes les marches sombres se retrouvaient plaquees au
# meme endroit : #06006C, #4C0007, #480026 — des primaires, pas des ombres. On plafonne
# donc a 85 % de ce que la clarte autorise : il reste de l air sous la frontiere, et une
# ombre redevient une couleur choisie au lieu d une couleur saturee par accident.
PLAFOND_GAMUT = 0.85

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
GRIS_L     = (0.14, 0.25, 0.36, 0.47, 0.58, 0.69, 0.79, 0.89, 0.98)

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
            plafond = PLAFOND_GAMUT*enGamut(L, hue, 0.5)
            C = enGamut(L, hue, min(base*CHROMA[i]*punch(base), plafond))
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
def reduire(rgba, larg, encre=0.0, seuilEncre=34.0):
    """Cadre -> grille de la fiche. Le cadre fait un multiple entier de la fiche : chaque
       pixel rendu est la moyenne d un bloc, ponderee par l alpha, ce qui interdit au fond
       de deteindre sur le contour.

       `encre` : LE TRAIT EST PRIORITAIRE DANS LE VOTE DE BLOC. Une moyenne d aire efface
       les traits fins — un cordon de tablier sombre large d un pixel source, noye dans un
       bloc de trois par trois clairs, ressort a un neuvieme de sa force et disparait au
       premier accrochage. Un dessinateur de pixel art fait l inverse : le trait gagne le
       bloc. On tire donc la moyenne vers le pixel LE PLUS SOMBRE du bloc, d autant plus
       fort que l ecart entre les deux est grand — au-dela de `seuilEncre` niveaux, c est
       qu il y a un trait la-dedans et pas seulement un degrade. Sur une etoffe unie
       l ecart est nul et rien ne bouge : la regle ne touche que ce qu elle doit toucher.
       A `encre = 0`, la fonction rend exactement ce qu elle rendait avant."""
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
    if encre > 0:
        # La luminance du bloc, et le pixel le plus sombre qu il contient. Les pixels
        # transparents sont ecartes en les poussant au blanc : un trou dans la silhouette
        # ne doit pas se faire elire trait le plus sombre.
        lum = rgb @ np.array([0.299, 0.587, 0.114])
        lum = np.where(al > 0.5, lum, 255.0)
        cel = lum.reshape(haut, k, larg, k)
        iMin = cel.min(axis=(1, 3))
        # On remet les k x k pixels d un bloc a plat pour aller chercher la COULEUR du plus
        # sombre, et pas seulement sa luminance : un trait brun doit rester brun.
        plat = cel.transpose(0, 2, 1, 3).reshape(haut, larg, k*k)
        pp = rgb.reshape(haut, k, larg, k, 3).transpose(0, 2, 1, 3, 4).reshape(haut, larg, k*k, 3)
        arg = np.argmin(plat, axis=2)
        sombre = np.take_along_axis(pp, arg[:, :, None, None], axis=2)[:, :, 0, :]
        moyL = (moy @ np.array([0.299, 0.587, 0.114]))
        w = np.clip((moyL - iMin)/float(seuilEncre), 0.0, 1.0)*float(encre)
        w = np.where(couv > 0.5, w, 0.0)[:, :, None]
        moy = (1.0 - w)*moy + w*sombre
    return moy, couv

# ---------- accrochage ---------------------------------------------------------
def accrocher(rgb, pal, bloc=48):
    """Chaque pixel prend la couleur de palette la plus proche EN OKLAB.
       ON DECOUPE EN BANDES DE LIGNES, et ce n est pas de la coquetterie : le tableau des
       distances fait hauteur x largeur x couleurs. A 192 x 240 sur 67 couleurs il pesait
       74 Mo, ce qui passait ; a 384 x 480 sur 105 couleurs il en pese 464, ce qui ne passe
       pas. Quarante-huit lignes a la fois en demandent quarante-six."""
    lab = oklab(rgb)
    pl = oklab(pal.astype(np.float64))
    H, W, _ = lab.shape
    out = np.empty((H, W), np.int16)
    for y0 in range(0, H, bloc):
        y1 = min(H, y0 + bloc)
        d = lab[y0:y1, :, None, :] - pl[None, None, :, :]
        out[y0:y1] = np.argmin((d*d).sum(axis=3), axis=2)
    return out

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
    # Meme decoupe que dans `accrocher`, et le tableau est garde en simple precision :
    # on compare des distances entre elles, pas des millionniemes.
    H, W, _ = lab.shape
    d = np.empty((H, W, len(pal)), np.float32)
    for y0 in range(0, H, 48):
        y1 = min(H, y0 + 48)
        dd = lab[y0:y1, :, None, :] - pl[None, None, :, :]
        d[y0:y1] = np.sqrt(np.maximum((dd*dd).sum(-1), 0)).astype(np.float32)
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


# ---------- LA PALETTE RELEVEE SUR CHAQUE IMAGE ---------------------------------
# LE JOUEUR : « palette relevee sur chaque image (pas choisie) : environ 14 teintes, fusion
# des quasi-doublons sous 22 unites RVB, mais jamais un ton colore avec un neutre, et
# jusqu a trois places reservees aux couleurs rares mais lointaines. »
#
# C EST L EXACT CONTRAIRE DE LA PALETTE PARTAGEE, ET LES DEUX SE DEFENDENT.
# La palette commune de 105 couleurs fait tenir les quinze personnages ensemble : une peau
# y est la meme peau d un bout a l autre du casting, et c est ce qui donne l impression
# d une seule main. Une palette relevee PAR IMAGE fait l inverse — chaque fiche recoit les
# quatorze couleurs qui la servent le mieux, elle, et le casting cesse d etre un casting.
# En echange, chaque fiche est plus juste avec quatre fois moins de couleurs.
# On ne tranche pas ici : les deux jeux de fiches sont fabriques, et c est un interrupteur
# du jeu qui decide. Voir « Visages » dans les reglages.
NB_TEINTES   = 14      # la cible
FUSION_RVB   = 22.0    # deux couleurs plus proches que ca n en font qu une
SPREAD_NEUTRE= 18.0    # ecart max-min entre canaux : en dessous, c est un neutre
RESERVE      = 3       # places gardees pour les couleurs rares mais lointaines
PART_RARE    = 0.0008  # 0,08 % des pixels suffit a meriter une place
LOIN_RVB     = 88.0    # ... si son remplacant est a plus de 88 unites

def _neutre(c):
    """Un neutre est une couleur dont les trois canaux se tiennent : ni bleu, ni brun,
       du gris. La regle est en RVB parce que c est en RVB que le joueur l a posee."""
    c = np.asarray(c, np.float64)
    return (c.max(axis=-1) - c.min(axis=-1)) < SPREAD_NEUTRE

def _kmoyennes(pts, poids, k, tours=24):
    """K-moyennes EN OKLAB, deterministe de bout en bout — aucun tirage au sort.
       Une palette qui change d une fabrication a l autre n est pas une decision, c est un
       accident : deux passes de suite doivent rendre les memes octets. Le premier centre
       est donc la couleur LA PLUS FREQUENTE, et chacun des suivants le point le plus loin
       de ce qui est deja pris (ponderes par la frequence, pour qu un pixel isole ne fonde
       pas une famille a lui tout seul)."""
    lab = oklab(pts.reshape(1, -1, 3))[0]
    n = len(lab)
    k = min(k, n)
    cen = [int(np.argmax(poids))]
    d2 = ((lab - lab[cen[0]])**2).sum(1)
    for _ in range(k - 1):
        score = d2*poids
        j = int(np.argmax(score))
        if score[j] <= 0: break
        cen.append(j)
        d2 = np.minimum(d2, ((lab - lab[j])**2).sum(1))
    C = lab[cen].copy()
    for _ in range(tours):
        d = lab[:, None, :] - C[None, :, :]
        a = np.argmin((d*d).sum(2), 1)
        neuf = C.copy()
        for i in range(len(C)):
            m = a == i
            w = poids[m].sum()
            if w > 0: neuf[i] = (lab[m]*poids[m][:, None]).sum(0)/w
        if np.allclose(neuf, C, atol=1e-6): C = neuf; break
        C = neuf
    return np.clip(np.round(deOklab(C)), 0, 255).astype(np.uint8), C

def paletteImage(rgb, couv, cible=NB_TEINTES):
    """LES QUATORZE COULEURS DE CETTE IMAGE-LA, mesurees et non choisies.
       Rend un tableau (n, 3) d octets. n vaut au plus `cible` + RESERVE."""
    op = couv > 0.5
    pix = np.clip(np.round(rgb[op]), 0, 255).astype(np.uint8)
    if not len(pix): return np.zeros((1, 3), np.uint8)
    # On travaille sur les couleurs DISTINCTES ponderees par leur frequence : une fiche de
    # 576 x 720 porte quatre cent mille pixels pour quelques milliers de couleurs.
    uni, cpt = np.unique(pix.reshape(-1, 3), axis=0, return_counts=True)
    pal, _ = _kmoyennes(uni.astype(np.float64), cpt.astype(np.float64), cible)

    # 1. FUSION DES QUASI-DOUBLONS — MAIS JAMAIS UN COLORE AVEC UN NEUTRE.
    #    Deux gris a dix-huit unites l un de l autre sont le meme gris ; un gris et un
    #    bleu-gris a dix-huit unites sont deux decisions differentes, et les fondre est ce
    #    qui fait virer une chemise blanche au bleu sur toute sa surface.
    garde = list(range(len(pal)))
    fusionne = True
    while fusionne and len(garde) > 1:
        fusionne = False
        for i in range(len(garde)):
            for j in range(i + 1, len(garde)):
                a, b = pal[garde[i]].astype(np.float64), pal[garde[j]].astype(np.float64)
                if np.linalg.norm(a - b) >= FUSION_RVB: continue
                if _neutre(a) != _neutre(b): continue      # colore + neutre : on ne fond pas
                del garde[j]; fusionne = True; break
            if fusionne: break
    pal = pal[garde]

    # 2. LES PLACES RESERVEES. Une couleur peut ne peser que quelques centiemes de pour
    #    cent et etre pourtant ce qu on regarde en premier : le rouge d un tampon, le vert
    #    d une bouteille, l or d un bouton. La moyenne la noie ; on lui garde trois places,
    #    a la double condition qu elle soit assez presente pour ne pas etre du bruit et
    #    assez loin de son remplacant pour que la difference se VOIE.
    tot = float(cpt.sum())
    d = uni.astype(np.float64)[:, None, :] - pal.astype(np.float64)[None, :, :]
    dist = np.sqrt((d*d).sum(2)).min(1)
    cand = [(int(c), tuple(u)) for u, c, q in zip(uni, cpt, dist)
            if c/tot >= PART_RARE and q > LOIN_RVB]
    cand.sort(reverse=True)
    for _, u in cand[:RESERVE]:
        c = np.asarray(u, np.uint8)
        if np.min(np.linalg.norm(pal.astype(np.float64) - c.astype(np.float64), axis=1)) <= LOIN_RVB:
            continue
        pal = np.vstack([pal, c[None, :]])
    return pal


def gammesImage(pal, ecart=0.55):
    """RANGER UNE PALETTE RELEVEE EN GAMMES, parce que deux passes en ont besoin.
       `cerner` fait descendre le liseré d une marche DANS SA PROPRE gamme, et `unifier`
       demande quelle famille domine autour d un pixel : les deux veulent des groupes de
       teinte, pas une liste plate. La palette partagee les recoit de sa construction ; une
       palette relevee sur l image, elle, arrive en vrac et il faut les retrouver.
       On groupe par ANGLE DE TEINTE en Oklab — deux couleurs a moins de `ecart` radians
       l une de l autre sont la meme etoffe vue a deux clartes — et l on met tous les
       neutres ensemble, quel que soit leur angle : sur un gris, l angle ne veut rien dire,
       il tourne au hasard d une unite de bruit."""
    lab = oklab(pal.astype(np.float64).reshape(1, -1, 3))[0]
    neu = _neutre(pal.astype(np.float64))
    ang = np.arctan2(lab[:, 2], lab[:, 1])
    groupes = []
    for i in range(len(pal)):
        if neu[i]: continue
        pose = False
        for g in groupes:
            # Distance CIRCULAIRE au chef de file : a cheval sur pi, une difference brute
            # dirait six radians la ou il y en a un dixieme.
            d = abs((ang[i] - ang[g[0]] + np.pi) % (2*np.pi) - np.pi)
            if d <= ecart: g.append(i); pose = True; break
        if not pose: groupes.append([i])
    gris = [i for i in range(len(pal)) if neu[i]]
    if gris: groupes.append(gris)
    # Chaque gamme se lit du plus sombre au plus clair : c est ce que `cerner` attend.
    return [sorted(g, key=lambda c: lab[c][0]) for g in groupes]
