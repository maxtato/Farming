# -*- coding: utf-8 -*-
"""LE CONTROLE DES PROPORTIONS, SUR LES FICHIERS LIVRES ET SUR RIEN D AUTRE.

    python3 controle.py            # les chiffres, et la planche des silhouettes

`aligner.py --verifier` recadre depuis les sources, `preuve.py` lisait le cache : les deux
ont donne des chiffres differents sur la Laiterie et il a fallu un troisieme juge. Celui-ci
ne connait ni cache ni chaine de cadrage — il ouvre les PNG de `portraits/`, ceux que le jeu
charge. Un controle qui partage du code avec ce qu il controle ne controle pas grand-chose.

IL REND DEUX CHOSES, ET LA DEUXIEME N EST PAS UN ORNEMENT.

  1. UN CHIFFRE, avec sa confiance. Les trois rapports forment un triangle dont le produit
     doit valoir un ; quand il ne le vaut pas, l ecart calcule ne veut rien dire et le
     controle le DIT au lieu de faire semblant. C est arrive : sur la Laiterie, le produit
     des trois rapports valait 1,57. Deux mesures sur trois etaient fausses — son bravo rit
     a pleines joues, ce qui deforme vraiment le visage, et son refus tend une paume qui
     entre dans la fenetre. Annoncer « 4,9 % d ecart » aurait ete annoncer du bruit.

  2. UNE PLANCHE DE SILHOUETTES, ou les trois contours d un personnage sont tires l un sur
     l autre — neutre en cyan, bravo en magenta, refus en jaune. Trois traits confondus :
     c est bon. Un trait qui s ecarte : c est cette humeur-la qui est a la mauvaise echelle,
     et l on voit LAQUELLE, ce qu aucun chiffre agrege ne dit. C est cette planche qui a
     tranche la Laiterie quand la correlation n y arrivait plus.
"""
import os, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import aligner as A, fabriquer as F, portrait as P

SEUIL_ECART   = 0.04     # au-dela, les humeurs ne sont plus a la meme echelle
SEUIL_CONFIANCE = 0.04   # au-dela, le triangle ne ferme pas : la mesure ne conclut pas

def _fiches(rad):
    """Les fiches livrees, RAMENEES A LA MEME GRILLE. Depuis que la planche se calcule sur
       la boite ou le jeu la pose, les humeurs n ont plus la meme taille de fichier — 288
       pour la fenetre de contrat, 576 pour l ecran de gain. Ce controle-ci ne parle pas de
       taille a l ecran, il parle de CADRAGE : le personnage occupe-t-il la meme part de son
       cadre dans ses trois humeurs. On remonte donc tout a 576, au plus proche voisin —
       576 vaut exactement deux fois 288, l agrandissement ne fabrique donc aucun pixel
       intermediaire et la silhouette est rendue au pixel pres."""
    dos = F.DEST if F.table()[rad].get('site') else F.ATTENTE
    out = {}
    for h in F.HUMEURS:
        f = os.path.join(dos, rad + '-' + h + '.png')
        if not os.path.exists(f): continue
        im = Image.open(f).convert('RGBA')
        if im.width != F.LARG_MAX:
            k = F.LARG_MAX//im.width
            im = im.resize((im.width*k, im.height*k), Image.NEAREST)
        out[h] = im
    return out

def _bord(a):
    p = np.pad(a, 1)
    return a & ~(p[:-2, 1:-1] & p[2:, 1:-1] & p[1:-1, :-2] & p[1:-1, 2:])

def silhouettes(rads, sortie='40_silhouettes.png', zoom=2, cols=4):
    """Les trois contours l un sur l autre. Cyan = neutre, magenta = bravo, jaune = refus."""
    vig = []
    for rad in rads:
        im = _fiches(rad)
        hs = [h for h in F.HUMEURS if h in im]
        if len(hs) < 2: continue
        A0 = [np.asarray(im[h])[:, :, 3] > 127 for h in hs]
        Ht, W = A0[0].shape
        out = np.full((Ht, W, 3), 252, np.uint8)
        for k, a in enumerate(A0):
            b = _bord(a)
            for c in range(3): out[:, :, c][b] = 40 if c == F.HUMEURS.index(hs[k]) else 245
        v = Image.fromarray(out).resize((W*zoom, Ht*zoom), Image.NEAREST)
        ImageDraw.Draw(v).line([0, int(0.318*Ht*zoom), v.width, int(0.318*Ht*zoom)],
                               fill=(226, 168, 148))
        vig.append((rad, v))
    if not vig: return
    cw, ch = vig[0][1].size
    lignes = (len(vig) + cols - 1)//cols
    pl = Image.new('RGB', (cols*(cw+10)+10, lignes*(ch+24)+10), (250, 248, 244))
    d = ImageDraw.Draw(pl)
    try: pol = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 12)
    except Exception: pol = ImageFont.load_default()
    for i, (rad, v) in enumerate(vig):
        x = 10 + (i % cols)*(cw+10); y = 10 + (i//cols)*(ch+24)
        d.text((x, y), rad.upper(), fill=(96, 80, 64), font=pol)
        pl.paste(v, (x, y+18))
    pl.save(sortie); print('->', sortie, pl.size)

def poches():
    """AUCUNE POCHE DE FOND NE DOIT SUBSISTER, ET C EST UN CONTROLE, PAS UNE ESPERANCE.
       Le joueur : « il reste du blanc dans certains. » Vingt-deux poches sur douze
       fiches — le fond vu a travers le verre des lunettes, le fond entre le pouce et la
       manche. Une inondation depuis le bord ne peut pas les atteindre par construction,
       et la regle « ce qui est enferme reste » existe pour proteger les dents : c est
       donc un equilibre, et un equilibre se verifie. On refait le detourage et l on
       compte ce qui reste enferme, a la couleur du fond, au-dessus du seuil d aire.
       Le compte doit etre ZERO."""
    import cv2
    T = F.table(); reste = []
    for rad in sorted(T):
        for h in F.HUMEURS:
            reg = T[rad].get(h)
            if not reg: continue
            im, al, _ = F.plaque(reg)
            a = np.asarray(im.convert('RGB')).astype(np.int16)
            H, W, _ = a.shape
            tour = np.concatenate([a[0], a[-1], a[:, 0], a[:, -1]])
            ref = np.median(tour, axis=0).astype(np.int16)
            clair = (np.abs(a - ref).max(axis=2) <= 26)
            n, lab = cv2.connectedComponents(clair.astype(np.uint8), 4)
            b = np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))
            fond = np.isin(lab, b[b != 0])
            nn, ll, st, _ = cv2.connectedComponentsWithStats(
                (clair & ~fond & (al > 127)).astype(np.uint8), 4)
            seuil = P.AIRE_POCHE*H*W
            for i in range(1, nn):
                ar = int(st[i, cv2.CC_STAT_AREA])
                if ar < seuil: continue
                m = ll == i
                d = float(np.abs(a[m].mean(0) - ref).max())
                if d <= P.TOL_POCHE:
                    reste.append((rad + '-' + h, ar, d, int(st[i, 0]), int(st[i, 1])))
    for n, ar, d, x, y in sorted(reste, key=lambda t: -t[1]):
        print('  POCHE  %-22s %6d px  a %.1f unite(s) du fond, en (%d,%d)' % (n, ar, d, x, y))
    print('poches de fond restantes : %d   (seuil %.0f px sur une planche de 1 122 x 1 402, '
          'tolerance %d unites)' % (len(reste), P.AIRE_POCHE*1122*1402, P.TOL_POCHE))
    return 1 if reste else 0

def controler():
    T = F.table()
    lignes, pires, douteux = [], [], []
    for rad in sorted(T):
        im = _fiches(rad)
        hs = [h for h in F.HUMEURS if h in im]
        if len(hs) < 2: continue
        tail, res = A.tailles({h: im[h] for h in hs}, hs)
        med = sorted(tail.values())[len(hs)//2]
        e = max(tail.values())/min(tail.values()) - 1.0
        sur = res <= SEUIL_CONFIANCE
        (pires if sur else douteux).append((e, rad))
        lignes.append((e, '%-16s ecart %5.1f %%  %s   %s'
                          % (rad, 100*e,
                             '(sur)          ' if sur
                             else '(NON CONCLUANT, triangle %4.1f %%)' % (100*res),
                             '  '.join('%s %+.1f %%' % (h[:3], 100*(tail[h]/med - 1))
                                       for h in hs))))
    for _, l in sorted(lignes, reverse=True): print(l)
    silhouettes(sorted(T))
    trop = [r for e, r in pires if e > SEUIL_ECART]
    print('%d personnages mesures sûrement · ecart moyen %.1f %% · pire cas %.1f %%'
          % (len(pires), 100*np.mean([e for e, _ in pires]), 100*max(e for e, _ in pires)))
    if douteux:
        print('%d non concluant(s) — a juger sur la planche des silhouettes : %s'
              % (len(douteux), ', '.join(r for _, r in douteux)))
    print('ECHEC : %s' % ', '.join(trop) if trop else
          'LES TROIS HUMEURS SONT A LA MEME ECHELLE')
    return 1 if trop else 0

if __name__ == '__main__':
    if '--poches' in sys.argv: sys.exit(poches())
    sys.exit(controler() or poches())
