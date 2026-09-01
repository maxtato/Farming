# -*- coding: utf-8 -*-
"""ALIGNER LES TROIS HUMEURS D UN PERSONNAGE, ET ECRIRE LA CORRECTION DANS LA TABLE.

    python3 aligner.py            # mesure et corrige commerces.json
    python3 aligner.py --mesurer  # mesure seulement, ne touche a rien

La mesure est dans `calage.py`, et elle rend un RAPPORT entre deux cadres. Reste a decider
sur quoi aligner, et c est la seule decision du fichier : LA MEDIANE DES TROIS. Si deux
humeurs s accordent et que la troisieme derape, la mediane est du bon cote ; prendre la
premiere reviendrait a corriger deux planches justes pour en suivre une fausse.

On boucle, on ne calcule pas d un coup. Le rapport se mesure autour du point d ancrage
THEORIQUE (le milieu du cadre, a la ligne des yeux), alors que `ech` agrandit autour de
l ancrage REEL, decale de `dx`/`dy`. Les deux coincident quand dx et dy sont nuls, et
s ecartent un peu sinon — au lieu de demeler ca par le calcul, on recadre et l on remesure.
Trois tours suffisent : le residu tombe sous le demi-pour-cent, ce que la mesure elle-meme
ne distingue plus.
"""
import fabriquer as F, calage as K, numpy as np, json, os, sys

LARGE  = np.linspace(0.80, 1.26, 24)
SERRE  = np.linspace(0.96, 1.04, 33)
SEUIL  = 0.0015                      # un millieme et demi : en dessous, on ne mesure plus rien
GROS, FIN = 192, 288                 # degrossir vite, finir juste

def _net(reg):
    """Une correction nulle ne s ecrit pas : la table doit rester lisible."""
    for k, neutre in (('ech', 1.0), ('dx', 0.0), ('dy', 0.0)):
        if k in reg and abs(reg[k] - neutre) < 1e-4: del reg[k]
    return reg

def ecrireTable(T):
    """LA TABLE EST FAITE POUR ETRE RELUE, DONC ON LA REECRIT COMME ELLE EST ECRITE.
       `json.dump(indent=1)` eclate chaque ancre sur quatre lignes : une correction de trois
       nombres devient un diff de cinq cents lignes, et l on ne voit plus ce qui a change.
       Une humeur par ligne, comme a la main."""
    ordre = ['site', 'humeurs'] + F.HUMEURS
    j = lambda v: json.dumps(v, ensure_ascii=False)
    blocs = []
    for rad in sorted(T):
        champs = ['%s: %s' % (j(k), j(T[rad][k])) for k in ordre if k in T[rad]]
        blocs.append(' %s: {%s}' % (j(rad), (',\n   ').join(champs)))
    open(os.path.join(F.ICI, 'commerces.json'), 'w', encoding='utf-8').write(
        '{\n' + ',\n'.join(blocs) + '\n}\n')

VERIF = np.linspace(0.88, 1.14, 53)

def mesureFine(R, C):
    """LE CONTROLE N EST PAS LA PREMIERE PASSE DE LA CORRECTION, et il a fallu s en rendre
       compte. La passe large de `aligner` balaie de 0,80 a 1,26 par pas de deux pour cent :
       sur trois personnages du lot elle accroche un maximum secondaire, annonce dix pour
       cent d ecart, puis converge en deux tours vers les reglages qui etaient DEJA dans la
       table. Autrement dit elle se trompe d abord et se rattrape ensuite — bon pour
       corriger, inutilisable pour constater.
       Ici on degrossit a la grille de 192 sur une plage etroite, puis on finit a 288 autour
       du vainqueur. Une plage etroite n est pas une petition de principe : si le rapport
       vrai etait de 1,15, la recherche saturerait au bord et rendrait 14 %, donc l ecart se
       verrait quand meme."""
    s, dx, dy, _ = K.rapport(R, C, yYeux=F.YEUX_Y, echs=VERIF, dmax=8, pas=2, grille=GROS)
    s, dx, dy, _ = K.rapport(R, C, yYeux=F.YEUX_Y,
                             echs=np.linspace(s - 0.02, s + 0.02, 17), dmax=3, pas=1, grille=FIN)
    return s

def tailles(cad, hs):
    """LES TAILLES RELATIVES DES HUMEURS, PAR TOUTES LES PAIRES ET NON PAR UNE SEULE.

       Mesurer bravo contre neutre, puis refus contre neutre, laisse la planche du neutre
       decider seule : si c est elle que la correlation lit mal — un chapeau de papier plie
       autrement, une chevelure bouclee, une source si petite qu il a fallu l agrandir deux
       fois et qu elle est floue —, les deux mesures heritent de son erreur et rien ne le
       signale. Les TROIS paires, elles, forment un triangle : neutre>bravo, bravo>refus,
       refus>neutre. Si les trois mesures sont justes, le produit des trois rapports vaut un.
       Sinon, le triangle ne se ferme pas, et de combien il ne se ferme pas EST la mesure de
       la confiance qu on peut leur faire.
       On resout donc les trois tailles au sens des moindres carres sur les logarithmes — ce
       qui repartit l erreur au lieu de la coller sur une seule planche — et l on rend le
       residu avec."""
    n = len(hs)
    A, y = [], []
    for i in range(n):
        for j in range(i+1, n):
            s = mesureFine(cad[hs[i]], cad[hs[j]])     # agrandir j pour venir sur i
            ligne = [0.0]*n; ligne[j] = 1.0; ligne[i] = -1.0
            A.append(ligne); y.append(-np.log(s))       # log t_j - log t_i = -log s
    A2 = np.array(A + [[1.0]*n]); y2 = np.array(y + [0.0])   # somme des logs nulle
    sol = np.linalg.lstsq(A2, y2, rcond=None)[0]
    residu = float(np.abs(np.array(A) @ sol - np.array(y)).max()) if len(A) > 1 else 0.0
    return {h: float(np.exp(sol[i])) for i, h in enumerate(hs)}, residu

def verifier(T=None, titre='table courante'):
    """L ECART D ECHELLE ENTRE LES HUMEURS, MESURE ET RIEN D AUTRE. Ne corrige pas, n ecrit
       pas : c est le controle qu on relance quand une planche change."""
    T = T if T is not None else F.table()
    pires = []; residus = []
    for rad in sorted(T):
        hs = [h for h in F.HUMEURS if T[rad].get(h)]
        if len(hs) < 2: continue
        pl = {h: F.plaque(T[rad][h]) for h in hs}
        cad = {h: F.cadrer(pl[h][0], pl[h][1], T[rad][h])[0] for h in hs}
        tail, residu = tailles(cad, hs)
        med = sorted(tail.values())[len(hs)//2]
        e = max(tail.values())/min(tail.values()) - 1.0
        pires.append(e); residus.append(residu)
        print('%-16s ecart %5.1f %%  (triangle %.1f %%)   %s' % (rad, 100*e, 100*residu,
              '  '.join('%s %+.1f %%' % (h[:3], 100*(tail[h]/med - 1)) for h in hs)))
    print('%s : %d personnages · ecart moyen %.1f %% · pire cas %.1f %% · '
          'le triangle se ferme a %.1f %% pres au pire'
          % (titre, len(pires), 100*np.mean(pires), 100*max(pires), 100*max(residus)))
    return pires

def aligner(ecrire=True, tours=3):
    T = F.table()
    bilan = []
    for rad in sorted(T):
        hs = [h for h in F.HUMEURS if T[rad].get(h)]
        if len(hs) < 2:
            continue
        pl = {h: F.plaque(T[rad][h]) for h in hs}
        cad = {h: F.cadrer(pl[h][0], pl[h][1], T[rad][h])[0] for h in hs}
        avant = None
        for t in range(tours):
            # 1. les tailles relatives, par les trois paires
            rel, _r = tailles(cad, hs)
            e = max(rel.values())/min(rel.values()) - 1.0
            if avant is None: avant = e
            # 2. LA CIBLE EST LA MEDIANE. Si deux humeurs s accordent et que la troisieme
            #    derape, la mediane est du bon cote ; prendre la premiere reviendrait a
            #    corriger deux planches justes pour en suivre une fausse.
            med = sorted(rel.values())[len(hs)//2]
            M = min(hs, key=lambda h: abs(rel[h] - med))
            if e < SEUIL: break
            # 3. l echelle, par le facteur exact
            for h in hs:
                if h == M: continue
                reg = T[rad][h]
                reg['ech'] = round(reg.get('ech', 1.0)*(med/rel[h]), 4)
                _net(reg)
                cad[h] = F.cadrer(pl[h][0], pl[h][1], reg)[0]
            # 4. puis la place de la tete, a echelle figee
            for h in hs:
                if h == M: continue
                _, dx, dy, _ = K.rapport(cad[M], cad[h], yYeux=F.YEUX_Y, echs=np.array([1.0]),
                                         dmax=6, pas=1, grille=FIN)
                reg = T[rad][h]
                reg['dx'] = round(reg.get('dx', 0.0) + dx, 4)
                reg['dy'] = round(reg.get('dy', 0.0) + dy, 4)
                _net(reg)
                cad[h] = F.cadrer(pl[h][0], pl[h][1], reg)[0]
        res, _r2 = tailles(cad, hs)
        apres = max(res.values())/min(res.values()) - 1.0
        bilan.append((rad, M, avant, apres, {h: T[rad][h].get('ech', 1.0) for h in hs}))
        print('%-16s ref=%-7s  ecart %5.1f %% -> %4.1f %%   %s'
              % (rad, M, 100*avant, 100*apres,
                 '  '.join('%s x%.3f' % (h[:3], T[rad][h].get('ech', 1.0)) for h in hs)))
    if ecrire:
        ecrireTable(T)
        print('-> commerces.json')
    m = [b[3] for b in bilan]
    print('%d personnages a plusieurs humeurs · ecart moyen %.1f %% avant, %.1f %% apres · '
          'pire cas %.1f %%' % (len(bilan), 100*np.mean([b[2] for b in bilan]),
                                100*np.mean(m), 100*max(m)))
    return bilan

if __name__ == '__main__':
    if '--verifier' in sys.argv:
        i = sys.argv.index('--verifier')
        if i + 1 < len(sys.argv):
            verifier(json.load(open(sys.argv[i+1])), sys.argv[i+1])
        else:
            verifier()
    else:
        aligner(ecrire='--mesurer' not in sys.argv)
