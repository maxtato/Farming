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
TOL_FOND   = 40       # ecart au fond en dessous duquel un pixel EST le fond
BANDE      = 8        # largeur, en pixels source, de la frange ou l alpha se calcule


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


def detourer(chemin):
    """Rend (couleur H,W,3 demelangee ; alpha H,W dans [0,1])."""
    a = np.asarray(Image.open(chemin).convert('RGB')).astype(np.float32)
    tour = np.concatenate([a[0], a[-1], a[:, 0], a[:, -1]])
    ref = np.median(tour, axis=0)
    d = np.abs(a - ref).max(axis=2)
    # 1. LE FOND, ENFERME OU NON. On n inonde pas depuis le bord, contrairement aux
    #    portraits : le magenta ne se trouve NULLE PART dans le sujet — ni un ble, ni un
    #    colza, ni le raisin a venir n en approchent a moins de 128 unites — tandis que
    #    l avoine et le colza ont des poches de fond ENFERMEES entre deux tiges. Une regle
    #    de connexite les aurait gardees opaques, et elles sortaient roses.
    fond = d <= TOL_FOND
    # 2. LA FRANGE : ce qui est a moins de BANDE pixels du fond. Au-dela, c est du sujet
    #    plein, et rien ne doit pouvoir l entamer — la ficelle brune d une gerbe est a
    #    quarante unites du magenta et se serait retrouvee a demi transparente.
    dist = cv2.distanceTransform((~fond).astype(np.uint8), cv2.DIST_L2, 3)
    frange = (~fond) & (dist <= BANDE)
    # 3. L ALPHA DE LA FRANGE se lit sur la teinte. La reference du sujet est la MEDIANE du
    #    plein : elle vaut ce que vaut la matiere, et ne se devine pas.
    k = cleTeinte(a)
    kf = float(np.median(k[(~fond) & (dist > BANDE)]))
    kb = float(cleTeinte(ref.reshape(1, 1, 3))[0, 0])
    al = np.where(fond, 0.0, 1.0)
    al[frange] = np.clip((kb - k[frange])/(kb - kf), 0, 1)
    # 4. LE DEMELANGE. Un pixel de frange vaut a.C + (1-a).fond ; on rend C, sans quoi la
    #    silhouette garderait un lisere magenta une fois posee sur le papier du menu.
    A = al[..., None]
    C = np.where(A > 0.02, (a - (1 - A)*ref)/np.maximum(A, 0.02), a)
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
