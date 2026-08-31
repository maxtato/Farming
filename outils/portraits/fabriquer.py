# -*- coding: utf-8 -*-
"""LA TABLE DE PRODUCTION, ET RIEN D AUTRE.
   `rendre.py` balaie un lot non trie pour voir ce qu il contient ; celui-ci fabrique les
   fiches du JEU, et il part d une table explicite — un commerce, trois humeurs, un fichier
   source par humeur. C est la seule facon d etre sur qu on ne livre pas le pouce leve d un
   metier a la place du refus d un autre, et c est aussi ce qui rend le travail
   REPRODUCTIBLE : les seize reglages a la main sont dans le fichier, pas dans une seance.

   Trois reglages facultatifs par humeur, dans l ordre ou l on y a recours :
     ech / dx / dy   corrigent ce que les detecteurs ont trouve
     ancre           [ecart, x, y] impose les yeux quand aucun detecteur ne mord

       python3 fabriquer.py                 # fabrique, et dit le poids
       python3 fabriquer.py --planche       # la planche de controle, pour juger
"""
import portrait as P, oeil as O, os, sys, json
import numpy as np
from PIL import Image, ImageDraw

U       = '/root/.claude/uploads/3c255efa-fd9f-5aab-a574-54544179bd6d/'
DEST    = '/home/user/Farming/portraits'
ATTENTE = '/home/user/Farming/outils/portraits/attente'
W, H, LARG, COUL = 288, 360, 192, 32
YEUX_Y, ECART = 0.318, 0.150
HUMEURS = ['neutre', 'bravo', 'refus']

def table(): return json.load(open(os.path.join(os.path.dirname(__file__) or '.', 'commerces.json')))

def une(reg):
    im = P.charger(U + reg['src'])
    al = P.detourer(im)
    c, inf = P.cadrerAncre(im, al, W, H, ecartCible=ECART, yYeux=YEUX_Y,
                           ech=reg.get('ech', 1.0), dx=reg.get('dx', 0.0),
                           dy=reg.get('dy', 0.0), oeilFn=O.reperes,
                           ancre=reg.get('ancre'))
    return c, inf

def png8(cadre):
    idx, pal, op = P.pixeliser(cadre, LARG, couleurs=COUL)
    m = len(pal)
    q = Image.fromarray(np.where(op, idx, m).astype(np.uint8), 'P')
    q.putpalette((list(np.asarray(pal, np.uint8).ravel()) + [0,0,0] + [0]*768)[:768])
    return q, m

def fabriquer():
    """UN PERSONNAGE SANS COMMERCE N EST PAS UN PERSONNAGE PERDU. Le premier groupe recu a
       ete attribue au Restaurant par ressemblance — une veste blanche, un foulard, un
       cuisinier — et c etait faux : le Restaurant, c est la femme au tableau d ardoise.
       Le chef, lui, n a rien perdu. Ses trois planches vont ensemble, on sait laquelle est
       le pouce leve et laquelle est le refus, on ne sait que son METIER.
       Une entree dont le champ `site` est vide part donc EN ATTENTE au lieu de partir dans
       le jeu : elle garde son groupement, son cadrage et ses reglages, et le jour ou l on
       apprend son commerce il n y a qu un mot a ecrire. C est aussi ce qui garantit que
       portraits/ ne contienne QUE ce que le jeu charge — un fichier de plus y serait un
       fichier que rien n affiche."""
    T = table()
    os.makedirs(DEST, exist_ok=True); os.makedirs(ATTENTE, exist_ok=True)
    tot = 0; n = 0; parkes = 0
    for rad in sorted(T):
        jeu = bool(T[rad].get('site'))
        for h in HUMEURS:
            reg = T[rad].get(h)
            if not reg: print('%-12s %-7s MANQUE' % (rad, h)); continue
            c, inf = une(reg)
            q, m = png8(c)
            f = os.path.join(DEST if jeu else ATTENTE, rad + '-' + h + '.png')
            q.save(f, 'PNG', optimize=True, transparency=m)
            t = os.path.getsize(f)
            if jeu: tot += t; n += 1
            else: parkes += 1
            print('%-12s %-7s %-22s %5.1f Ko  [%s]%s'
                  % (rad, h, reg['src'], t/1024, inf['source'], '' if jeu else '  EN ATTENTE'))
    print('%d fiches dans le jeu, %.0f Ko, %.1f Ko en moyenne%s'
          % (n, tot/1024, tot/1024/max(n,1),
             ('  ·  %d planches en attente de commerce' % parkes) if parkes else ''))

def planche(sortie='30_production.png'):
    T = table(); rads = sorted(T)
    cw, ch = LARG, int(round(LARG*H/W))
    pl = Image.new('RGB', (3*(cw+20)+20, len(rads)*(ch+32)+20), (244,239,229))
    d = ImageDraw.Draw(pl)
    for r, rad in enumerate(rads):
        for cI, h in enumerate(HUMEURS):
            reg = T[rad].get(h)
            x = 20+cI*(cw+20); y = 20+r*(ch+32)
            d.rectangle([x-1,y-1,x+cw,y+ch], outline=(216,206,188))
            if reg:
                c, inf = une(reg)
                idx, pal, op = P.pixeliser(c, LARG, couleurs=COUL)
                v = P.rendre(idx, pal, op, 1)
                pl.paste(v, (x, y), v)
                d.text((x, y+ch+6), '%s — %s  [%s]'
                       % (T[rad].get('site') or (rad + ' (en attente)'), h, inf['source']),
                       fill=(88,74,58) if T[rad].get('site') else (150,120,96))
            else:
                d.text((x+8, y+ch//2), 'manque', fill=(170,120,100))
        d.line([12, 20+r*(ch+32)+int(YEUX_Y*ch), pl.width-12, 20+r*(ch+32)+int(YEUX_Y*ch)],
               fill=(206,116,86))
    pl.save(sortie); print('->', sortie, pl.size)

if __name__ == '__main__':
    if '--planche' in sys.argv: planche()
    else: fabriquer()
