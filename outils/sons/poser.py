# Pose les sons encodés (<cle>.b64) dans la table SONS de index.html : remplace la ligne de
# la clé si elle existe, l'ajoute sinon. Usage : python3 poser.py [cle…]
import os, re, sys, json
ICI = os.path.dirname(os.path.abspath(__file__))
JEU = os.path.join(ICI, '..', '..', 'index.html')
T = json.load(open(os.path.join(ICI, 'sons.json'), encoding='utf-8'))
cles = sys.argv[1:] or [k for k in T if k != '_']
s = open(JEU, encoding='utf-8').read()
a = s.index('const SONS = {'); b = s.index('\n};', a)
bloc = s[a:b]
for cle in cles:
    b64 = open(os.path.join(ICI, cle + '.b64'), encoding='utf-8').read().strip()
    ligne = '  %s: "%s"' % (cle, b64)
    m = re.search(r'^  %s: "[^"]*"' % re.escape(cle), bloc, re.M)
    if m: bloc = bloc[:m.start()] + ligne + bloc[m.end():]
    else: bloc = bloc.rstrip() + ',\n' + ligne
    print('posé', cle, len(b64)//1024, 'Ko')
open(JEU, 'w', encoding='utf-8').write(s[:a] + bloc + s[b:])
