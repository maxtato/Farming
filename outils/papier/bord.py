# -*- coding: utf-8 -*-
"""TRACER LE BORD DECHIRE DU BANDEAU, une fois, hors du jeu.

   Le chemin est pose en image de fond sur les blocs du bandeau, etire par
   `background-size:100% 100%` : l amplitude verticale suit la HAUTEUR du bloc et
   l ecart entre sommets suit sa LARGEUR. On raisonne donc en unites de viewBox, et
   l on convertit a la fin pour dire ce que ca donne a l ecran.

   L ANCIEN : 27 points sur 400, amplitude 6,4 sur 60. Sur le bloc du tutoriel
   (438 x 52 px) cela faisait un creux de 5,7 px avec un sommet tous les 16 px —
   c est-a-dire une dent plus haute que la moitie des capitales de 10 px qui sont
   dessous. Le joueur : « reduis le fait de decoupage sur le papier blanc pour que ca
   reste fin, pas trop grossier. »
   LE NEUF : trois fois plus de points, moitie moins d amplitude. Releve sur fond plat,
   aux tailles reelles des blocs :

       bloc                 ancien                        neuf
       tutoriel 439 x 50    5,33 px, sommet / 34,6 px     2,17 px, sommet / 8,6 px
       mission  187 x 21    2,33 px, sommet / 14,7 px     1,00 px, sommet / 3,8 px
       mission  169 x 21    2,33 px, sommet / 13,3 px     1,00 px, sommet / 3,3 px

       python3 bord.py            # le chemin, et ce qu il donne a l ecran
       python3 bord.py --css      # la meme chose, encodee pour l url() du CSS

   LA GRAINE EST FIXE, ET C EST TOUT L OBJET DU FICHIER. Le premier bord dechire avait ete
   tire au sort dans une seance et colle dans le CSS ; personne ne pouvait le REFAIRE, donc
   personne ne pouvait le retoucher sans tout redessiner. Ici on change PAS ou AMP, on
   relance, et le reste du papier ne bouge pas d un pixel.
"""
import random, math

W, H = 400.0, 60.0
PAS    = 5.0     # un sommet tous les 5 unites (contre 15) -> 3 x plus dense
AMP    = 1.5     # +/- 1,5 unite autour de la ligne (contre +/- 3,2) -> moitie moins
Y_HAUT = 4.6     # la ligne moyenne du bord haut
Y_BAS  = 55.4    # celle du bord bas, symetrique
GRAINE = 20260902

def bord(y0, xs, rnd):
    """Un bruit a deux echelles : une longue ondulation, plus le grain du dechirement.
       Une seule echelle donne soit une vague (basse frequence) soit une brosse a dents
       (haute frequence) ; un papier dechire a les deux."""
    ph = rnd.uniform(0, 6.283)
    out = []
    for x in xs:
        lent = 0.42*AMP*math.sin(x/47.0 + ph)      # l ondulation du geste
        vif  = rnd.uniform(-0.58, 0.58)*AMP        # le grain de la fibre
        out.append((x, round(y0 + lent + vif, 2)))
    return out

def tracer():
    rnd = random.Random(GRAINE)
    xs = [round(x, 1) for x in
          [PAS] + [PAS + i*PAS for i in range(1, int((W - 2*PAS)//PAS) + 1)]]
    if xs[-1] < W - PAS: xs.append(round(W - PAS, 1))
    haut = bord(Y_HAUT, xs, rnd)
    bas  = bord(Y_BAS, list(reversed(xs)), rnd)
    # LES DEUX PETITS COTES GARDENT LEUR AMPLITUDE D ORIGINE, et c est deliberé : eux ne
    # sont pas trop grossiers, ils sont trop DISCRETS. La meme etirure qui ecrase la
    # dechirure du haut sur 24 px de haut ecrase celle des cotes sur 400 unites de large :
    # a moins de deux unites de jeu ils se lisent comme un coup de ciseaux. Quatre unites,
    # cinq points, et le bout redevient dechire lui aussi.
    JEU_COTE = 2.0
    cd = [(round(W - PAS + rnd.uniform(-JEU_COTE, JEU_COTE), 1), round(y, 1))
          for y in (10, 20, 30, 40, 50)]
    cg = [(round(PAS + rnd.uniform(-JEU_COTE, JEU_COTE), 1), round(y, 1))
          for y in (50, 40, 30, 20, 10)]
    pts = haut + cd + bas + cg
    return 'M' + ' L'.join('%.1f %.2f' % (x, y) for x, y in pts) + ' Z'

def css():
    """Le chemin dans l url() du CSS : seuls < > et # y sont echappes, comme l existant."""
    svg = ("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 %d %d' "
           "preserveAspectRatio='none'>"
           "<linearGradient id='p' x1='0' y1='0' x2='0.4' y2='1'>"
           "<stop offset='0' stop-color='#F6F0DF'/>"
           "<stop offset='0.55' stop-color='#F1E9D4'/>"
           "<stop offset='1' stop-color='#E7DEC6'/>"
           "</linearGradient>"
           "<path d='%s' fill='url(#p)'/></svg>") % (W, H, tracer())
    return svg.replace('<', '%3C').replace('>', '%3E').replace('#', '%23')

if __name__ == '__main__':
    import sys
    if '--css' in sys.argv:
        print('data:image/svg+xml,' + css()); raise SystemExit
    d = tracer()
    print(d)
    print()
    print('%d points, %d caracteres' % (d.count('L') + 1, len(d)))
    # Les trois tailles que les blocs prennent vraiment a l ecran, relevees dans le jeu
    # sur un telephone en paysage (844 x 390).
    for lib, larg, haut in (('mission courte  ', 169, 21),
                            ('mission longue  ', 187, 21),
                            ('marche tutoriel ', 439, 50)):
        print('  %s %3d x %2d px  ->  creux %.2f px, sommet tous les %.1f px'
              % (lib, larg, haut, 2*AMP/H*haut, PAS/W*larg))
