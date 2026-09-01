# -*- coding: utf-8 -*-
"""LES VIGNETTES DE PRODUIT. Un rendu sur fond magenta entre, une vignette de menu sort :
   78 x 78 pixels, fond transparent, palette de 64 couleurs relevee sur l image.

       python3 fabriquer.py             # fabrique, et dit le poids
       python3 fabriquer.py --planche   # la planche de controle, pour juger la taille

   POURQUOI 78. La regle de la maison est celle des portraits : PX_JEU = 1/3, un pixel
   d art mesure un tiers de pixel CSS. Le jeu pose la vignette dans une boite de 26 CSS —
   la hauteur exacte du filet de couleur qu elle remplace, pour qu aucune ligne de menu ne
   bouge d un pixel — et la planche fait donc trois fois cela. Sur un telephone a trois
   points d ecran par pixel CSS, un pixel d art tombe sur un point.

   POURQUOI UNE TABLE ET PAS UN DOSSIER. Comme pour les portraits : `produits.json` dit
   quelle source va a quelle cle de `PRODUITS`, et c est la seule facon d etre sur qu on ne
   livre pas l orge a la place de l avoine — les deux sont des gerbes jaunes, et leurs noms
   de fichier sont des empreintes.
"""
import json, os, sys
import numpy as np, cv2
from PIL import Image

U     = '/root/.claude/uploads/3c255efa-fd9f-5aab-a574-54544179bd6d/'
ICI   = os.path.dirname(os.path.abspath(__file__))
DEST  = os.path.abspath(os.path.join(ICI, '..', '..', 'produits'))
TABLE = os.path.join(ICI, 'produits.json')

PX_JEU     = 1/3      # taille d un pixel d art, en pixels CSS — la meme que les portraits
BOITE      = 26       # la boite ou le jeu pose la vignette, en pixels CSS
COTE       = round(BOITE/PX_JEU)
MARGE      = 2        # en pixels d art : le sujet ne touche jamais le bord de la boite
COULEURS   = 64
SEUIL_TEINTE = 0.55   # au-dessus de cette teinte normalisee, un pixel EST du fond
LUM_MIN      = 40     # ... a condition d etre eclaire : un noir presque pur n a pas de teinte
BANDE        = 8      # largeur, en pixels source, de la frange ou l alpha se calcule


def cleTeinte(a):
    """CE QUI DISTINGUE LE MAGENTA DU RESTE : min(R,B) - G. Le fond est a +244, un jaune de
       ble a -134, un vert de feuille a -100. Et surtout, la grandeur est LINEAIRE dans le
       melange : un pixel a moitie fond, a moitie ble tombe pile au milieu. C est ce qui
       permet de lire l alpha dessus.

       LA DISTANCE AU FOND, ELLE, NE L EST PAS — et c est l erreur qu on a faite d abord.
       `max|P - fond|` vaut `a x max|C - fond|`, ou le second facteur depend de la couleur
       du sujet : le meme seuil rendait opaque un pixel a moitie magenta, et les barbes de
       l orge sortaient roses."""
    return np.minimum(a[:, :, 0], a[:, :, 2]) - a[:, :, 1]


def teinteNormee(a):
    """LA MEME CHOSE, DIVISEE PAR LA CLARTE — et c est ce qui voit les OMBRES PORTEES.
       Les deux bidons de lait en ont une, et la regle precedente les gardait : une ombre
       est le meme magenta MULTIPLIE par 0,6, elle est donc loin de la couleur du fond, et
       tout ce qui en est loin etait du sujet. Un gros pate rose restait au pied du bidon.

       Diviser par `max(R,G,B)` enleve ce facteur : le fond plein et son ombre tombent a la
       MEME valeur — 0,97 pour les huit planches PNG, 0,73 pour la photo JPEG dont le
       magenta est plus pale —, tandis que le sujet reste sous 0,55. Mesure sur les dix
       sources : PAS UN pixel de sujet plein n atteint 0,55, et l ombre la plus sombre
       reste a 91 de clarte, loin du plancher.

       LE PLANCHER DE CLARTE EST NECESSAIRE, et c est de l arithmetique : a (3, 0, 4) la
       division rend 0,75 et un noir presque pur passerait pour du magenta. En dessous de
       LUM_MIN un pixel n a pas de teinte, il a du bruit."""
    mx = a.max(axis=2)
    return np.where(mx >= LUM_MIN,
                    (np.minimum(a[:, :, 0], a[:, :, 2]) - a[:, :, 1])/np.maximum(mx, 1), -1)


def fondLocal(a, fond, sigma):
    """LA COULEUR DU FOND DERRIERE CHAQUE PIXEL, et non une couleur pour toute l image.
       Sous une ombre portee, le fond est le meme magenta en plus sombre : demeler la
       frange de cette zone avec le magenta PLEIN reviendrait a retirer plus de fond qu il
       n y en a, et le pied du bidon sortirait verdatre.
       Une moyenne gaussienne des pixels de fond, ponderee par eux seuls, donne cette
       couleur-la de proche en proche — et rend le fond plein partout ou il n y a pas
       d ombre, puisque tous les voisins y sont identiques."""
    m = fond.astype(np.float32)
    num = cv2.GaussianBlur(a*m[..., None], (0, 0), sigma)
    den = cv2.GaussianBlur(m, (0, 0), sigma)
    return num/np.maximum(den, 1e-6)[..., None], den


def detourer(chemin):
    """Rend (couleur H,W,3 demelangee ; alpha H,W dans [0,1])."""
    a = np.asarray(Image.open(chemin).convert('RGB')).astype(np.float32)
    tour = np.concatenate([a[0], a[-1], a[:, 0], a[:, -1]])
    ref = np.median(tour, axis=0)
    # 1. LE FOND ET SON OMBRE, ENFERMES OU NON. On n inonde pas depuis le bord,
    #    contrairement aux portraits : le magenta ne se trouve NULLE PART dans le sujet,
    #    tandis que l avoine et le colza ont des poches de fond ENFERMEES entre deux tiges.
    #    Une regle de connexite les aurait gardees opaques, et elles sortaient roses.
    fond = teinteNormee(a) >= SEUIL_TEINTE
    # 2. LA FRANGE : ce qui est a moins de BANDE pixels du fond. Au-dela, c est du sujet
    #    plein, et rien ne doit pouvoir l entamer — la ficelle brune d une gerbe est a
    #    quarante unites du magenta et se serait retrouvee a demi transparente.
    dist = cv2.distanceTransform((~fond).astype(np.uint8), cv2.DIST_L2, 3)
    frange = (~fond) & (dist <= BANDE)
    # 3. L ALPHA DE LA FRANGE se lit sur la teinte LINEAIRE, contre le fond QUI EST DERRIERE
    #    ce pixel-la. La reference du sujet est la MEDIANE du plein : elle vaut ce que vaut
    #    la matiere, et ne se devine pas.
    loc, den = fondLocal(a, fond, BANDE)
    loc = np.where((den > 1e-3)[..., None], loc, ref)
    k = cleTeinte(a)
    kf = float(np.median(k[(~fond) & (dist > BANDE)]))
    kb = cleTeinte(loc)
    al = np.where(fond, 0.0, 1.0)
    al[frange] = np.clip(((kb - k)/np.maximum(kb - kf, 1))[frange], 0, 1)
    # 4. LE DEMELANGE. Un pixel de frange vaut a.C + (1-a).fond ; on rend C, sans quoi la
    #    silhouette garderait un lisere magenta une fois posee sur le papier du menu.
    A = al[..., None]
    C = np.where(A > 0.02, (a - (1 - A)*loc)/np.maximum(A, 0.02), a)
    return np.clip(C, 0, 255), al


def vignette(chemin):
    """Detoure, recadre sur le sujet, met a l echelle par le PLUS GRAND COTE et centre.
       Le plus grand cote, et non la hauteur : les recoltes sont toutes debout, mais un
       fromage ou une vache seront couches, et une regle par hauteur les ferait deborder."""
    C, al = detourer(chemin)
    ys, xs = np.where(al > 0.02)
    C = C[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
    al = al[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
    h, w = al.shape
    s = (COTE - 2*MARGE)/max(h, w)
    nw, nh = max(1, round(w*s)), max(1, round(h*s))
    # LA REDUCTION SE FAIT SUR LA COULEUR PREMULTIPLIEE. Sans cela, la moyenne d un pixel
    # de bord melange la couleur du sujet a celle du vide — qui n est rien — et la
    # silhouette s eclaircit d un liseré sur tout son tour.
    pm = np.dstack([C*al[..., None], al*255]).astype(np.float32)
    r = cv2.resize(pm, (nw, nh), interpolation=cv2.INTER_AREA)
    a2 = np.clip(r[:, :, 3]/255.0, 0, 1)
    c2 = np.where(a2[..., None] > 0.004, r[:, :, :3]/np.maximum(a2[..., None], 0.004), 0)
    out = np.zeros((COTE, COTE, 4), np.uint8)
    oy, ox = (COTE - nh)//2, (COTE - nw)//2
    out[oy:oy + nh, ox:ox + nw, :3] = np.clip(c2, 0, 255).astype(np.uint8)
    out[oy:oy + nh, ox:ox + nw, 3] = np.clip(a2*255, 0, 255).astype(np.uint8)
    return Image.fromarray(out, 'RGBA'), (nw, nh)


def main():
    table = json.load(open(TABLE, encoding='utf-8'))
    os.makedirs(DEST, exist_ok=True)
    faits, poids = [], 0
    for cle, e in sorted(table.items()):
        src = os.path.join(U, e['src'])
        if not os.path.exists(src):
            print('  %-8s source absente : %s' % (cle, e['src']))
            continue
        im, (nw, nh) = vignette(src)
        # LA PALETTE EST RELEVEE SUR L IMAGE, comme celle de `portraits14/`. Un rendu de
        # recolte tient dans soixante-quatre couleurs — mesure : le passage de RGBA a la
        # palette ne se voit pas a 26 pixels CSS, et divise le poids par trois et demi.
        q = im.quantize(colors=COULEURS, method=Image.FASTOCTREE)
        f = os.path.join(DEST, cle + '.png')
        q.save(f, optimize=True)
        poids += os.path.getsize(f)
        faits.append((cle, nw, nh, os.path.getsize(f)))
    for cle, nw, nh, o in faits:
        print('  %-8s %2d x %2d dans %d  %5d o' % (cle, nw, nh, COTE, o))
    print('  %d vignettes, %.1f Ko' % (len(faits), poids/1024))
    if '--planche' in sys.argv:
        planche(faits)


def planche(faits):
    """Les vignettes a leur taille de jeu, et grossies huit fois, sur le papier du menu."""
    Z, N = 8, len(faits)
    im = Image.new('RGB', (COTE*Z*N, COTE*Z + COTE + 12), (232, 224, 202))
    for i, (cle, _, _, _) in enumerate(faits):
        v = Image.open(os.path.join(DEST, cle + '.png')).convert('RGBA')
        g = v.resize((COTE*Z, COTE*Z), Image.NEAREST)
        im.paste(g, (i*COTE*Z, 0), g)
        im.paste(v, (i*COTE*Z + 12, COTE*Z + 6), v)
    f = os.path.join(ICI, 'controle.png')
    im.save(f)
    print('  planche : ' + f)


if __name__ == '__main__':
    main()
