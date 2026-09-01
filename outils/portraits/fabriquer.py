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

       python3 fabriquer.py --palette       # (re)bat la palette du casting entier
       python3 fabriquer.py                 # fabrique, et dit le poids
       python3 fabriquer.py --planche       # la planche de controle, pour juger

   LA PALETTE EST UN FICHIER, PAS UN CALCUL. `palette.json` est versionne : c est la
   decision de couleur du jeu, et refabriquer les fiches deux fois de suite doit rendre
   les memes octets. On ne la rebat qu en le demandant, et l on regarde le nuancier avant
   de la garder.
"""
import portrait as P, oeil as O, pixels as X, os, sys, json
import numpy as np
from PIL import Image, ImageDraw

U       = '/root/.claude/uploads/3c255efa-fd9f-5aab-a574-54544179bd6d/'
DEST    = '/home/user/Farming/portraits'
ATTENTE = '/home/user/Farming/outils/portraits/attente'
ICI     = os.path.dirname(os.path.abspath(__file__))
PALETTE = os.path.join(ICI, 'palette.json')
# LE CACHE NE VA PAS DANS LE DEPOT. Il pese quarante megaoctets et se refabrique en deux
# minutes ; ce qui doit etre versionne, c est la table des sources et la palette.
CACHE   = os.environ.get('PORTRAITS_CACHE', '/tmp/portraits-cadres.npz')

# LE CADRE FAIT EXACTEMENT TROIS FOIS LA FICHE. C est la condition de la reduction par
# moyenne d aire : 576 = 3 x 192, 720 = 3 x 240. Chaque pixel livre est la moyenne de neuf
# pixels du cadre, ponderee par leur alpha. Les cotes en fraction — l ecart des yeux, la
# ligne des yeux, les corrections dx/dy — ne changent pas d un poil : elles sont toutes
# relatives au cadre.
LARG, HAUT = 192, 240
GRAIN      = 3
W, H       = LARG*GRAIN, HAUT*GRAIN
YEUX_Y, ECART = 0.318, 0.150
HUMEURS = ['neutre', 'bravo', 'refus']

def table(): return json.load(open(os.path.join(ICI, 'commerces.json')))

# DETOURER ET CADRER SONT SEPARES, ET C EST LE RECALAGE QUI L A EXIGE. Detourer une
# planche coute deux secondes ; la cadrer, deux centiemes. Aligner les trois humeurs d un
# personnage demande de la recadrer une dizaine de fois avec des reglages qui bougent — on
# detoure UNE fois et l on recadre autant qu il faut.
def plaque(reg):
    im = P.charger(U + reg['src'])
    return im, P.detourer(im)

def cadrer(im, al, reg):
    return P.cadrerAncre(im, al, W, H, ecartCible=ECART, yYeux=YEUX_Y,
                         ech=reg.get('ech', 1.0), dx=reg.get('dx', 0.0),
                         dy=reg.get('dy', 0.0), oeilFn=O.reperes,
                         ancre=reg.get('ancre'))

def une(reg):
    im, al = plaque(reg)
    return cadrer(im, al, reg)

# ---------------------------------------------------------------------------
# LE CORPUS. Batir la palette demande de voir TOUT le casting d un coup : c est le seul
# moyen qu une gamme de peau serve a quatorze visages au lieu d etre refaite quatorze fois.
# Detourer et cadrer trente-huit planches coute deux minutes ; on ne le refait pas a chaque
# essai de palette, on le garde.
def cadres(refaire=False):
    """Rend {cle: (rgb (240,192,3) float, couverture (240,192) float)} pour tout le lot."""
    if not refaire and os.path.exists(CACHE):
        z = np.load(CACHE)
        return {k[2:]: (z[k], z['c_' + k[2:]]) for k in z.files if k.startswith('r_')}
    T = table(); out = {}
    for rad in sorted(T):
        for h in HUMEURS:
            reg = T[rad].get(h)
            if not reg: continue
            c, inf = une(reg)
            rgb, couv = X.reduire(c, LARG)
            out[rad + '-' + h] = (rgb, couv)
            print('  cadre %-22s [%s]' % (rad + '-' + h, inf['source']))
    np.savez_compressed(CACHE, **{('r_' + k): v[0].astype(np.float32) for k, v in out.items()},
                        **{('c_' + k): v[1].astype(np.float32) for k, v in out.items()})
    return out

def batirPalette(refaire=False):
    """UNE palette pour tout le monde, rangee en gammes, ecrite sur le disque.
       On l ecrit parce qu elle doit pouvoir se relire, se juger et se retoucher : une
       palette trouvee a la volee a chaque fabrication ne serait pas une decision."""
    C = cadres(refaire)
    ech = []
    for k in sorted(C):
        rgb, couv = C[k]
        pix = rgb[couv > 0.5]
        ech.append(pix[::3])                      # un pixel sur trois suffit largement
    ech = np.concatenate(ech, 0)
    pal, gammes = X.batir(ech)
    json.dump({'couleurs': pal.tolist(), 'gammes': gammes,
               'echantillons': int(len(ech))}, open(PALETTE, 'w'), indent=1)
    print('palette : %d couleurs, %d gammes, sur %d pixels du casting entier'
          % (len(pal), sum(1 for g in gammes if g), len(ech)))
    return pal, gammes

def palette():
    d = json.load(open(PALETTE))
    return np.asarray(d['couleurs'], np.uint8), d['gammes']

def fiche(rgb, couv, pal, gammes):
    """La fiche livree, de la moyenne d aire au fichier : accrochage a la palette,
       silhouette nettoyee, orphelins effaces, cerne d une marche."""
    op = X.nettoyerAlpha(couv >= 0.5)
    idx = X.accrocher(rgb, pal)
    idx = X.unifier(rgb, idx, op, pal, gammes, rayon=3, tol=0.075)
    idx = X.deparasiter(idx, op, pal)
    idx = X.cerner(idx, op, gammes)
    idx = X.deparasiter(idx, op, pal, tours=1)
    return idx, op

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
    # LA COUPE NE DOIT PAS REDEVENIR UNE DENTURE. C est la seule propriete du gabarit qu on
    # ne peut pas juger sur la planche sans se tromper — une dent de deux pour cent de
    # hauteur ne se voit pas sur une vignette et saute aux yeux sur la fiche a taille reelle.
    if not P.coupeConvexe():
        raise ValueError('la coupe du buste n est pas convexe : elle rebrousse, donc elle denture')
    C = cadres(); pal, gammes = palette()
    os.makedirs(DEST, exist_ok=True); os.makedirs(ATTENTE, exist_ok=True)
    tot = 0; n = 0; parkes = 0; orphTot = []
    for rad in sorted(T):
        jeu = bool(T[rad].get('site'))
        # UN COMMERCE PEUT N AVOIR QU UNE HUMEUR, ET CE N EST PAS UN OUBLI. Le comptoir
        # agricole ne donne pas de mission et ne refuse jamais un achat : il n a ni pouce
        # leve ni refus a montrer. `humeurs` dit lesquelles il DOIT avoir, pour qu une
        # absence voulue ne se lise pas comme un fichier perdu.
        voulues = T[rad].get('humeurs') or HUMEURS
        for h in HUMEURS:
            reg = T[rad].get(h)
            if not reg:
                if h in voulues: print('%-12s %-7s MANQUE' % (rad, h))
                continue
            rgb, couv = C[rad + '-' + h]
            idx, op = fiche(rgb, couv, pal, gammes)
            q, m = X.png8(idx, op, pal)
            f = os.path.join(DEST if jeu else ATTENTE, rad + '-' + h + '.png')
            q.save(f, 'PNG', optimize=True, transparency=m)
            t = os.path.getsize(f)
            orph, opq = X.orphelins(idx, op)
            teintes = len(set(idx[op].tolist()))
            if jeu: tot += t; n += 1; orphTot.append(orph)
            else: parkes += 1
            print('%-12s %-7s %-22s %5.1f Ko  %2d teintes  %4.1f %% orphelins%s'
                  % (rad, h, reg['src'], t/1024, teintes, 100*orph,
                     '' if jeu else '  EN ATTENTE'))
    print('%d fiches dans le jeu, %.0f Ko, %.1f Ko en moyenne  ·  '
          'orphelins %.1f %% en moyenne, %.1f %% au pire%s'
          % (n, tot/1024, tot/1024/max(n,1),
             100*float(np.mean(orphTot or [0])), 100*float(np.max(orphTot or [0])),
             ('  ·  %d planches en attente de commerce' % parkes) if parkes else ''))

def planche(sortie='30_production.png', zoom=1):
    T = table(); rads = sorted(T)
    C = cadres(); pal, gammes = palette()
    cw, ch = LARG*zoom, HAUT*zoom
    pl = Image.new('RGB', (3*(cw+20)+20, len(rads)*(ch+32)+20), (244,239,229))
    d = ImageDraw.Draw(pl)
    for r, rad in enumerate(rads):
        for cI, h in enumerate(HUMEURS):
            x = 20+cI*(cw+20); y = 20+r*(ch+32)
            reg = T[rad].get(h)
            if not reg:
                d.text((x+8, y+ch//2),
                       'manque' if h in (T[rad].get('humeurs') or HUMEURS) else 'sans objet',
                       fill=(170,120,100) if h in (T[rad].get('humeurs') or HUMEURS)
                            else (178,168,150))
                continue
            d.rectangle([x-1,y-1,x+cw,y+ch], outline=(216,206,188))
            rgb, couv = C[rad + '-' + h]
            idx, op = fiche(rgb, couv, pal, gammes)
            orph, _ = X.orphelins(idx, op)
            v = X.dessiner(idx, op, pal, zoom)
            pl.paste(v, (x, y), v)
            d.text((x, y+ch+6), '%s — %s  ·  %d teintes  ·  %.1f %% orphelins'
                   % (T[rad].get('site') or (rad + ' (en attente)'), h,
                      len(set(idx[op].tolist())), 100*orph),
                   fill=(88,74,58) if T[rad].get('site') else (150,120,96))
        d.line([12, 20+r*(ch+32)+int(YEUX_Y*ch), pl.width-12, 20+r*(ch+32)+int(YEUX_Y*ch)],
               fill=(206,116,86))
    pl.save(sortie); print('->', sortie, pl.size)

if __name__ == '__main__':
    if '--palette' in sys.argv: batirPalette('--refaire' in sys.argv)
    elif '--planche' in sys.argv: planche(zoom=2 if '--zoom' in sys.argv else 1)
    else: fabriquer()
