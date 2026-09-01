# -*- coding: utf-8 -*-
"""
LES TROIS HUMEURS D UN MEME PERSONNAGE DOIVENT ETRE A LA MEME ECHELLE.

Le joueur, planche annotee a l appui : « pour les personnages avec plusieurs images,
assure-toi que les proportions soient identiques sur les 3 images. » Il a raison, et le
defaut est structurel : `cadrerAncre` mesure CHAQUE PLANCHE ISOLEMENT. Les yeux, la boite
de visage, le profil des largeurs — trois estimateurs qui se trompent chacun de quelques
pour cent, et rien dans la chaine ne compare la planche du pouce leve a celle du refus.
Deux moitie-erreurs de sens contraire font un ecart de dix pour cent, et dix pour cent sur
une tete, ca se voit du premier coup d oeil quand les deux images se succedent a l ecran.

CE QU ON MESURE ICI, c est le rapport d echelle ENTRE DEUX CADRES DU MEME PERSONNAGE. Pas
une taille absolue — aucun estimateur ne la donne assez juste — mais un RAPPORT, et un
rapport se mesure bien : les deux planches montrent la meme tete, la meme coiffure, le meme
couvre-chef, dessines par la meme main. On cherche l agrandissement et le decalage qui font
coincider l une sur l autre, par correlation croisee normalisee.

TROIS PRECAUTIONS, chacune contre un piege du lot :

  1. ON NE REGARDE QUE LA BANDE DE LA TETE. Les bras changent d une humeur a l autre — un
     pouce leve, une paume tendue, une bouteille — et un recalage qui les prend en compte
     irait chercher un compromis entre deux poses differentes. La tete, elle, est le meme
     objet dans les trois.
  2. ON PONDERE PAR L ALPHA DU MODELE. Ce qui est transparent chez la reference ne compte
     pas : un objet en plus chez l autre humeur ne penalise rien.
  3. LA REFERENCE EST LA MEDIANE DES TROIS, pas la premiere ni la « mieux ancree ». Si deux
     humeurs s accordent et que la troisieme derape, la mediane est du bon cote. Choisir la
     premiere reviendrait a corriger deux planches justes pour en suivre une fausse.

Et la sortie n est pas une image, c est un NOMBRE PAR PLANCHE, ecrit dans `commerces.json`
comme n importe quel autre reglage a la main. La chaine reste reproductible, et le controle
qui va avec est evident : apres correction, une deuxieme passe doit retrouver 1,000.
"""
import numpy as np
from PIL import Image

# La bande de la tete, en fractions du cadre. La ligne des yeux tombe a 0,318 ; le menton
# vers 0,45. On prend d un peu au-dessus du crane a un peu sous le menton, et l on serre
# lateralement pour que l epaule et le bras n entrent pas dans la mesure.
BANDE = (0.030, 0.430, 0.200, 0.800)
# ET LA BANDE EST PONDEREE VERS SON MILIEU. Un pouce leve, une paume tendue, une bouteille
# montent parfois jusqu au menton et entrent par le cote dans la fenetre de mesure. Sur la
# Laiterie, cela suffisait a faire mentir une des trois paires : le triangle des rapports ne
# se fermait qu a onze pour cent pres, donc aucune des trois mesures n etait fiable. Un
# cosinus sureleve qui vaut 1 au milieu et 0,15 aux bords laisse la tete decider et reduit
# les intrus au bruit — sans les exclure franchement, ce qui ferait dependre le resultat
# d une frontiere arbitraire.
GRILLE = 192                    # on mesure sur une reduction : c est la forme qui compte

def _gris(cadre, larg=GRILLE):
    haut = int(round(larg*cadre.height/cadre.width))
    p = cadre.resize((larg, haut), Image.LANCZOS)
    a = np.asarray(p).astype(np.float64)
    g = 0.299*a[:, :, 0] + 0.587*a[:, :, 1] + 0.114*a[:, :, 2]
    return g, a[:, :, 3]/255.0

def _echantillonner(g, al, s, P):
    """Agrandit de `s` AUTOUR DU POINT D ANCRAGE, et non du centre du cadre : c est
       exactement ce que fait `ech` dans la chaine, donc la correction trouvee ici
       s y reporte telle quelle."""
    H, W = g.shape
    ys, xs = np.mgrid[0:H, 0:W].astype(np.float64)
    xc = P[0] + (xs - P[0])/s
    yc = P[1] + (ys - P[1])/s
    # L INTERPOLATION EST BILINEAIRE, ET CE N EST PAS UN DETAIL. Au plus proche voisin,
    # deux echelles distantes d un pour cent rendent souvent EXACTEMENT la meme image — les
    # arrondis tombent au meme endroit —, le score ne varie plus continument avec l echelle,
    # et la mesure plafonne a un pour cent pres. C est ce qui laissait deux a trois pour cent
    # d ecart entre humeurs apres correction.
    x0 = np.floor(xc); y0 = np.floor(yc)
    fx = xc - x0; fy = yc - y0
    xi0 = np.clip(x0.astype(int), 0, W-1); xi1 = np.clip(xi0 + 1, 0, W-1)
    yi0 = np.clip(y0.astype(int), 0, H-1); yi1 = np.clip(yi0 + 1, 0, H-1)
    bil = lambda A: (A[yi0, xi0]*(1-fx)*(1-fy) + A[yi0, xi1]*fx*(1-fy) +
                     A[yi1, xi0]*(1-fx)*fy     + A[yi1, xi1]*fx*fy)
    dedans = (xc >= 0) & (xc <= W-1) & (yc >= 0) & (yc <= H-1)
    return bil(g), bil(al)*dedans

def _poids(h, w):
    """Le cosinus sureleve qui donne le milieu de la bande pour la tete et les bords pour
       le bruit. Memorise : la bande a la meme forme d un appel a l autre."""
    cle = (h, w)
    if cle not in _POIDS:
        x = (np.arange(w) + 0.5)/w*2 - 1                  # -1 .. +1
        _POIDS[cle] = np.tile(0.15 + 0.85*np.cos(x*np.pi/2)**2, (h, 1))
    return _POIDS[cle]
_POIDS = {}

def _score(Rg, Ral, Cg, Cal, b):
    y0, y1, x0, x1 = b
    m = Ral[y0:y1, x0:x1] > 0.5
    n = int(m.sum())
    if n < 200: return -1.0
    w = _poids(y1-y0, x1-x0)[m]
    sw = w.sum()
    a = Rg[y0:y1, x0:x1][m]; c = Cg[y0:y1, x0:x1][m]
    ca = (Cal[y0:y1, x0:x1][m] > 0.5).astype(np.float64)
    a = a - (w*a).sum()/sw; c = c - (w*c).sum()/sw
    d = np.sqrt((w*a*a).sum()*(w*c*c).sum())
    ncc = float((w*a*c).sum()/d) if d > 1e-9 else 0.0
    # ET L ACCORD DES SILHOUETTES. La correlation seule se laisse prendre par un aplat :
    # deux joues unies correlent bien a n importe quelle echelle. La part du modele que
    # l autre humeur couvre vraiment, elle, ne se laisse pas prendre.
    return 0.55*ncc + 0.45*float((w*ca).sum()/sw)

def rapport(refCadre, autreCadre, yYeux=0.318, echs=None, dmax=16, pas=2, grille=GRILLE):
    """Rend (s, dx, dy, score) : l agrandissement et le decalage — EN FRACTIONS DU CADRE —
       a appliquer a `autreCadre` pour qu il vienne sur `refCadre`.
       `grille` : la largeur a laquelle on mesure. 192 pour degrossir, ou le bon maximum est
       large et la recherche entiere coute quatre dixiemes de seconde ; 288 pour finir, ou
       le pas de translation vaut trois millimes de cadre au lieu de cinq."""
    Rg, Ral = _gris(refCadre, grille); Cg, Cal = _gris(autreCadre, grille)
    H, W = Rg.shape
    P = (W/2.0, yYeux*H)
    y0, y1 = int(BANDE[0]*H), int(BANDE[1]*H)
    x0, x1 = int(BANDE[2]*W), int(BANDE[3]*W)
    if echs is None: echs = np.linspace(0.80, 1.26, 24)
    best = (1.0, 0, 0, -2.0)
    for s in echs:
        Cs, As = _echantillonner(Cg, Cal, s, P)
        for ty in range(-dmax, dmax+1, pas):
            for tx in range(-dmax, dmax+1, pas):
                # decaler = glisser la fenetre de lecture, sans recopier le tableau
                b = (y0 - ty, y1 - ty, x0 - tx, x1 - tx)
                if b[0] < 0 or b[2] < 0 or b[1] > H or b[3] > W: continue
                v = _score(Rg[y0:y1, x0:x1], Ral[y0:y1, x0:x1],
                           Cs[b[0]:b[1], b[2]:b[3]], As[b[0]:b[1], b[2]:b[3]],
                           (0, y1-y0, 0, x1-x0))
                if v > best[3]: best = (float(s), tx, ty, v)
    # deuxieme passe, serree autour du vainqueur : le pas de 2 pixels et de 2 % laisse
    # assez d incertitude pour que la correction se voie encore.
    s0 = best[0]
    fins = np.linspace(max(0.70, s0 - 0.024), min(1.40, s0 + 0.024), 25)
    for s in fins:
        Cs, As = _echantillonner(Cg, Cal, s, P)
        for ty in range(best[2]-2, best[2]+3):
            for tx in range(best[1]-2, best[1]+3):
                b = (y0 - ty, y1 - ty, x0 - tx, x1 - tx)
                if b[0] < 0 or b[2] < 0 or b[1] > H or b[3] > W: continue
                v = _score(Rg[y0:y1, x0:x1], Ral[y0:y1, x0:x1],
                           Cs[b[0]:b[1], b[2]:b[3]], As[b[0]:b[1], b[2]:b[3]],
                           (0, y1-y0, 0, x1-x0))
                if v > best[3]: best = (float(s), tx, ty, v)
    return best[0], best[1]/float(W), best[2]/float(H), best[3]
