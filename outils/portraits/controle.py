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
import aligner as A, fabriquer as F

SEUIL_ECART   = 0.04     # au-dela, les humeurs ne sont plus a la meme echelle
SEUIL_CONFIANCE = 0.04   # au-dela, le triangle ne ferme pas : la mesure ne conclut pas

def _fiches(rad):
    dos = F.DEST if F.table()[rad].get('site') else F.ATTENTE
    return {h: Image.open(os.path.join(dos, rad + '-' + h + '.png')).convert('RGBA')
            for h in F.HUMEURS
            if os.path.exists(os.path.join(dos, rad + '-' + h + '.png'))}

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
    sys.exit(controler())
