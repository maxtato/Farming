# -*- coding: utf-8 -*-
"""LE RENDU DE TOUS LES PORTRAITS, ET SA TABLE DE CORRECTION.
   Le cadrage automatique donne un point de depart, pas un resultat : sur un dessin
   stylise, aucun detecteur ne dit ou est le visage avec la constance qu il faudrait.
   On garde donc l automatique, ET une table `reglages.json` ou chaque planche peut
   corriger son echelle et son centrage. Trois nombres par image, relus a l oeil sur la
   planche de controle : c est ce qui fait que les quarante-cinq fiches se ressemblent.
"""
import portrait as P, os, glob, json, sys
from PIL import Image, ImageDraw

U='/root/.claude/uploads/3c255efa-fd9f-5aab-a574-54544179bd6d/'
W, H, LARG, COUL = 288, 360, 192, 32          # cadre de travail, largeur d art, couleurs
YEUX_Y, ECART = 0.318, 0.150                  # hauteur de la ligne d yeux, ecart inter-oculaire

def lot():
    c=[]
    for f in glob.glob(U+'*.png'):
        try: w,h=Image.open(f).size
        except: continue
        if h > w*1.05 or (w==h and w>1200): c.append((os.path.getmtime(f), f))
    return [f for _,f in sorted(c)]

def reglages():
    try: return json.load(open('reglages.json'))
    except Exception: return {}

def un(f, R):
    b = os.path.basename(f)[:8]
    r = R.get(b, {})
    im = P.charger(f); al = P.detourer(im)
    import oeil as O
    c, inf = P.cadrerAncre(im, al, W, H, ecartCible=ECART, yYeux=YEUX_Y,
                           ech=r.get('ech', 1.0), dx=r.get('dx', 0.0), dy=r.get('dy', 0.0),
                           oeilFn=O.reperes, ancre=r.get('ancre'))
    return b, c, inf

def planche(sortie, cols=6, zoom=1):
    R = reglages(); fs = lot(); vign=[]
    for f in fs:
        try:
            b, c, inf = un(f, R)
            idx,pal,op = P.pixeliser(c, LARG, couleurs=COUL)
            vign.append((b, P.rendre(idx,pal,op,zoom), inf.get('source','largeur')))
        except Exception as e:
            vign.append((os.path.basename(f)[:8], None, 'ECHEC '+str(e)[:30]))
        sys.stdout.flush()
    cw, ch = LARG*zoom, int(round(LARG*zoom*H/W))
    rows=(len(vign)+cols-1)//cols
    pl=Image.new('RGB',(cols*(cw+18)+18, rows*(ch+30)+18),(243,238,228)); d=ImageDraw.Draw(pl)
    for i,(b,v,src) in enumerate(vign):
        x=18+(i%cols)*(cw+18); y=18+(i//cols)*(ch+30)
        d.rectangle([x-1,y-1,x+cw,y+ch], outline=(214,204,186))
        if v is not None: pl.paste(v,(x,y),v)
        # les deux traits attendus : haut et bas du visage
        d.line([x,y+int(YEUX_Y*ch),x+cw,y+int(YEUX_Y*ch)], fill=(208,116,86))
        for s2 in (-1, 1):
            xe = x+cw//2 + int(s2*ECART*cw/2)
            d.line([xe, y+int(YEUX_Y*ch)-5, xe, y+int(YEUX_Y*ch)+5], fill=(208,116,86))
        d.line([x+cw//2, y, x+cw//2, y+ch], fill=(226,196,178))
        d.text((x, y+ch+8), b + ('' if src=='visage' else ' ['+src+']'), fill=(92,78,62))
    pl.save(sortie); print('->', sortie, pl.size)

if __name__ == '__main__':
    planche(sys.argv[1] if len(sys.argv)>1 else '10_controle.png')

def sortir(dossier='sortie'):
    """LES FICHIERS. Un PNG indexe par planche, 192 px de large, palette de 32 couleurs.
       Le nom reste celui de la source tant qu on ne sait pas a quel commerce elle va :
       le renommage se fera quand le groupement par metier sera connu."""
    import numpy as np, io as _io
    os.makedirs(dossier, exist_ok=True)
    R = reglages(); tot = 0; n = 0
    for f in lot():
        b, c, inf = un(f, R)
        idx, pal, op = P.pixeliser(c, LARG, couleurs=COUL)
        m = len(pal)
        plat = np.where(op, idx, m).astype(np.uint8)
        q = Image.fromarray(plat, 'P')
        q.putpalette((list(np.asarray(pal, np.uint8).ravel()) + [0,0,0] + [0]*768)[:768])
        chemin = os.path.join(dossier, b + '.png')
        q.save(chemin, 'PNG', optimize=True, transparency=m)
        t = os.path.getsize(chemin); tot += t; n += 1
        print('%-10s %s  %5.1f Ko  [%s]' % (b, '%dx%d'%q.size, t/1024, inf['source']))
    print('%d fichiers, %.0f Ko au total, %.1f Ko en moyenne' % (n, tot/1024, tot/1024/n))
