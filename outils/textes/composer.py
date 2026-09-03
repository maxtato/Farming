# -*- coding: utf-8 -*-
"""TEXTES.md : tout ce que le jeu dit au joueur, et quand il le dit.

       node relever.js          # lit les tables DANS le jeu qui tourne -> textes.json
       python3 composer.py      # + les bandeaux du source -> ../../TEXTES.md

   LES TEXTES SONT RELEVÉS, PAS RECOPIÉS. Les trente missions, les neuf marches du
   tutoriel et les vingt leçons sont lues dans le jeu chargé par un navigateur : le
   document ne peut donc pas mentir sur ce qui est écrit, ni prendre du retard sur une
   phrase changée. Les bandeaux volants, eux, se lisent dans le source — ils sont dans
   cent appels de `showHint` éparpillés, et aucun ne se laisse interroger de l'extérieur.

   LES « QUAND », EN REVANCHE, SONT ÉCRITS ICI. Une condition JavaScript ne se lit pas :
   `()=> partParcelle('labour') >= PART_ETAPE` doit se traduire en « quand 98 % de la
   parcelle est labourée ». Ce sont les deux tables QUAND_TUTO et QUAND_LECON, et elles
   sont la seule chose de ce fichier qu'il faut tenir à jour à la main.
"""
import json, io, re, os

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.abspath(os.path.join(ICI, '..', '..'))
JEU = os.path.join(RACINE, 'index.html')

src = io.open(JEU, encoding='utf-8').read()
lignes = src.split('\n')
def numero(pos): return src.count('\n', 0, pos) + 1

def args(s, i):
    """i pointe sur la parenthèse ouvrante : rend l'expression complète, parenthèses
       équilibrées, en sautant les chaînes."""
    prof, j, q = 0, i, None
    while j < len(s):
        c = s[j]
        if q:
            if c == '\\': j += 2; continue
            if c == q: q = None
        elif c in "'\"`": q = c
        elif c == '(': prof += 1
        elif c == ')':
            prof -= 1
            if prof == 0: return s[i+1:j]
        j += 1
    return ''

def litteraux(e):
    """toutes les chaînes d'une expression, scannées et non attrapées au filet : une
       expression ternaire en porte deux, et une expression régulière gourmande les
       aurait recollées en une seule."""
    out, i = [], 0
    while i < len(e):
        c = e[i]
        if c in "'\"":
            j, cur = i + 1, ''
            while j < len(e):
                if e[j] == '\\': cur += e[j:j+2]; j += 2; continue
                if e[j] == c: break
                cur += e[j]; j += 1
            out.append(cur); i = j + 1; continue
        i += 1
    return out


def morceaux(e):
    """coupe l'expression sur les + de premier niveau"""
    out, prof, q, cur = [], 0, None, ''
    for c in e:
        if q:
            cur += c
            if c == q and not cur.endswith('\\' + q): q = None
            continue
        if c in "'\"`": q = c; cur += c; continue
        if c in '([{': prof += 1
        elif c in ')]}': prof -= 1
        if c == '+' and prof == 0: out.append(cur); cur = ''; continue
        cur += c
    out.append(cur)
    return [m.strip() for m in out if m.strip()]

res, calcules = [], []
for m in re.finditer(r'showHint\s*\(', src):
    e = args(src, m.end() - 1)
    if not e: continue
    txt = ''
    for p in morceaux(e):
        L = litteraux(p)
        # UNE chaîne, et le morceau n'est QUE cette chaîne : sinon c'est une expression
        # qui commence et finit par une apostrophe — un ternaire, par exemple — et la
        # prendre pour un littéral recolle ses deux branches en une seule phrase.
        if len(L) == 1 and len(p) == len(L[0]) + 2 and p[0] in "'\"":
            txt += L[0]
        else:
            # un morceau CALCULÉ peut quand même porter des textes : un ternaire en
            # cache deux. On les sort tous, et l'on rend « A / B » plutôt que <…>.
            lit = [x for x in litteraux(p)
                   if len(x.strip()) >= 3 and re.search(r'[A-Za-zÀ-ÿ]{3}', x)]
            txt += (' / '.join(lit) if lit else '<…>')
    # les échappements du source : \\u00c0 est un À, \\' est une apostrophe
    txt = re.sub(r'\\u([0-9a-fA-F]{4})', lambda m: chr(int(m.group(1), 16)), txt)
    txt = txt.replace("\\'", "’").replace('\\n', ' ').replace('\\u2019', '’')
    txt = re.sub(r'\s+', ' ', txt).strip()
    # un message qui ne porte AUCUN texte — showHint(mal), showHint(q) — n'a rien à
    # relire : c'est une valeur calculée ailleurs, et elle paraît telle quelle.
    if txt and txt.replace('<…>', '').strip(' –·+') : res.append([numero(m.start()), txt])
    else: calcules.append(numero(m.start()))



d = json.load(open(os.path.join(ICI, 'textes.json'), encoding='utf-8'))
hints = res
lignes = src.split('\n')

# --- les chapitres du source, pour ranger les bandeaux volants ---
chap = []
for n, l in enumerate(lignes, 1):
    m = re.match(r"/\* -+ (?:\d+\.\s*)?([A-ZÀ-Ý][^-]*?)\s*-+ ", l)
    if m: chap.append((n, m.group(1).strip().rstrip('.').capitalize()))
def chapitre(n):
    nom = 'Divers'
    for ln, t in chap:
        if ln <= n: nom = t
        else: break
    return nom

# --- QUAND : traduit à la main, une fois, depuis la condition du jeu ---
QUAND_TUTO = {
 'labour':  ("Dès la première seconde de la campagne, après la fenêtre « UN HÉRITAGE ».",
             "Quand 98 % de la parcelle est labourée."),
 'semis':   ("Dès que le labour est fini.", "Quand 98 % de la parcelle est semée."),
 'pousse':  ("Dès que le semis est fini.", "Quand tout le blé semé est mûr — le dernier épi, pas 98 %."),
 'recolte': ("Dès que le blé est mûr.",
             "Quand 98 % de la parcelle est moissonnée ET qu'au moins 30 kg sont rentrés."),
 'silo':    ("Dès que le champ est moissonné.", "Quand 30 kg de blé sont entrés au silo."),
 'parking': ("Dès que le silo a reçu la récolte.",
             "Quand la moissonneuse est garée au parc à outils."),
 'auto':    ("Dès que la moissonneuse est rangée. Le bouton A bat en jaune ; la carte qui "
             "s'ouvre fait battre la parcelle, puis la destination, puis LANCER.",
             "Quand un premier chantier est lancé."),
 'pickup':  ("Dès que le premier chantier est lancé.", "Quand on conduit le pick-up."),
 'explorer': ("Dès qu'on conduit le pick-up. Cercle jaune au croisement des chemins, en haut "
              "des parcelles ; à l'arrivée, la fenêtre « DES POSSIBILITÉS D'EXPANSION ».",
              "Deux secondes après l'arrivée au croisement : le téléphone sonne."),
 'vente':   ("MODE LIBRE UNIQUEMENT — dès que le tour de reconnaissance est fait.",
             "À la première vente, quel que soit le commerce."),
 'appel':   ("CAMPAGNE UNIQUEMENT — deux secondes après le croisement. C'est la marche qui "
             "fait sonner le téléphone chez soi.",
             "Quand on prend la mission, au cercle vert de la ferme."),
}
QUAND_LECON = {
 'cuve':       "L'outil attelé a une cuve VIDE, et il reste de quoi la remplir à la ferme.",
 'tremie':     "La trémie de la moissonneuse est pleine.",
 'gazole':     "Un engin descend sous 40 % de gazole et la citerne de la cour n'est pas vide.",
 'courses':    "Une des deux cuves de la cour tombe sous 10 %, ou le gazole sous 25 %.",
 'garage':     "On a de quoi acheter le moins cher des engins ou outils en vitrine.",
 'amelio':     "On a de quoi payer le cran suivant d'un engin ou d'un outil déjà possédé.",
 'culture':    "Une culture est ouverte par le palier et on a de quoi l'acheter.",
 'semoirCulture': "Le semoir est attelé et au moins deux cultures sont débloquées.",
 'parcelle':   "Une parcelle est à vendre et on a de quoi la payer.",
 'plan':       "On possède un outil de travail et une parcelle cultivable.",
 'silo':       "Le silo dépasse 85 % et on a de quoi l'agrandir.",
 'metier':     "Un métier d'atelier est ouvert par le palier et on a de quoi l'acheter.",
 'produire':   "L'atelier a au moins un métier, sa file est vide, et il y a de quoi lancer un lot.",
 'entrepot':   "On roule avec une caisse dont le contenu se range à l'entrepôt.",
 'reglages':   "L'atelier a un métier et on a de quoi payer une de ses trois améliorations.",
 'elevage':    "Aucun enclos encore monté, une espèce ouverte, une parcelle libre et l'argent.",
 'bete':       "Un enclos a de la place et on a de quoi acheter une bête.",
 'mangeoire':  "Un enclos habité tombe sous 35 % de mangeoire.",
 'traire':     "Un enclos a de quoi être récolté (lait, laine, œufs, miel).",
 'contrat':    "Les contrats sont ouverts et un commerce en propose un.",
}

L = []
w = L.append
w("# Tous les textes du jeu, et quand ils arrivent\n")
w("*Relevé automatique : les textes sont lus DANS le jeu qui tourne, pas recopiés à la "
  "main. Les descriptions de « quand » sont, elles, rédigées d'après la condition du "
  "code.*\n")
w("Quatre surfaces disent quelque chose au joueur, et elles n'ont ni le même ton ni le "
  "même poids :\n")
w("| surface | ce que c'est | combien de temps |")
w("|---|---|---|")
w("| **Fenêtre de papier** | la « bulle » : un titre, une phrase, un visage, une ligne de suite | 5 à 6 s, ou un doigt — sauf une marche de tutoriel, qui **attend le doigt** |")
w("| **Bandeau de mission** | en haut à gauche, la mission en cours et ce qu'elle attend | tant que la mission court |")
w("| **Bandeau volant** | la ligne noire au milieu de l'écran, en capitales | 2 à 3 s |")
w("| **Écran d'accueil** | le titre au lancement et l'écran de fin | jusqu'au bouton |")
w("")
w("---\n")

# 1. OUVERTURE
w("## 1. L'ouverture\n")
a = d['accueil']
w("**Écran d'accueil** — titre `%s`, sous-titre « %s », boutons : %s.\n"
  % (a['titre'], a['sous'], ' · '.join('« %s »' % b for b in a['boutons'])))
w("**Première fenêtre de la campagne**, juste après le bouton *Commencer* :\n")
w("> **UN HÉRITAGE**  \n> *« Mon oncle m'a laissé sa terre, son tracteur et sa maison.  \n"
  "> Je n'ai jamais conduit autre chose qu'une voiture. »*  \n"
  "> — suite : *On commence par retourner le sol, paraît-il*\n")
w("---\n")

# 2. TUTORIEL
w("## 2. Le tutoriel — %d marches\n" % len(d['tuto']))
w("Une marche **attend le doigt** : elle ne part pas toute seule. Elle allume aussi un "
  "cercle jaune au sol et une flèche au bord de l'écran vers l'endroit à rejoindre.\n")
for E in d['tuto']:
    q = QUAND_TUTO.get(E['cle'], ('—', '—'))
    w("### %d. %s" % (E['i'] + 1, E['titre']))
    w("> %s\n" % E['txt'].replace('–', '—'))
    w("- **Arrive** : %s" % q[0])
    w("- **Se solde** : %s" % q[1])
    if E['ou']: w("- **Où elle envoie** : %s" % E['ou'])
    if E['libre']:
        w("- **En mode libre, elle dit autre chose** : **%s** — %s"
          % (E['libre']['titre'], E['libre']['txt'].replace('–', '—')))
    w("")
w("### Et à la fin, en mode libre seulement")
w("> **VOUS SAVEZ L'ESSENTIEL**  \n> *« Préparer, semer, attendre, récolter, stocker, "
  "vendre.  \n> Bon… ça commence à ressembler à un métier. »*  \n> — suite : *Cultivez, "
  "élevez, transformez et développez votre ferme comme vous le souhaitez*\n")
w("---\n")

# 3. LECONS
w("## 3. Les leçons — %d, une seule fois chacune\n" % len(d['lecons']))
w("Une leçon se lève **quand le geste devient possible ou nécessaire**, jamais deux fois "
  "dans la même partie. Un **MUR** est un blocage (le fermier fait la tête) ; une "
  "**porte** est une possibilité qui s'ouvre (il est surpris).\n")
for Le in d['lecons']:
    w("### %s%s" % (Le.get('nom') or Le['titre'], '  — *mur*' if Le['mur'] else ''))
    w("> **%s** — %s\n" % (Le['titre'], ' – '.join(Le['txt'].split(' – ')[1:]) or Le['txt']))
    w("- **Arrive quand** : %s" % QUAND_LECON.get(Le['cle'], '—'))
    if Le['ou']: w("- **Où elle envoie** : %s%s"
                   % (Le['ou'], (' · fenêtre %s / %s' % (Le['fen'], Le['onglet'])) if Le['fen'] else ''))
    w("")
w("---\n")

# 4. MISSIONS
w("## 4. Les %d missions de campagne\n" % len(d['missions']))
w("Une mission se **prend chez soi** : le téléphone sonne, on rentre à la ferme, on "
  "lit la demande. Elle se **solde** en livrant, et le commerçant répond.\n")
niv = None
for M in d['missions']:
    if M['niv'] != niv:
        niv = M['niv']
        N = d['niveaux'][niv-1]
        w("\n### Palier %d — %s" % (niv, N['nom']))
        w("*%s*\n" % N['resume'])
    w("#### %d. %s" % (M['i'] + 1, M['nom'] or (M['lieu'] or '')))
    dem = ', '.join(l['unite'] for l in M['lignes']) if M['lignes'] else (M['faire'] or '—')
    w("- **Chez** : %s  ·  **Demande** : %s  ·  **Prime** : %s €  ·  **XP** : %s%s%s"
      % (M['lieu'] or '—', dem, M['prime'], M['xp'],
         ('  ·  **Qui parle** : %s' % M['qui']) if M.get('qui') else '',
         ('  ·  **En-tête** : %s' % M['entete']) if M.get('entete') else ''))
    w("\n> **À la prise** — *« %s »*\n" % M['texte'])
    if M['fin']:
        w("> **À la livraison** — *« %s »*\n" % M['fin'])
    for E in M['prep']:
        w("> *Préambule — **%s** : %s*\n" % (E['titre'], E['txt'].replace('–', '—')))
    for A in M['apres']:
        w("> *Page suivante — **%s**%s : %s%s*\n"
          % (A['titre'], (' (visage : %s)' % A['face']) if A.get('face') else '',
             A['txt'].replace('<br>', ' / ').replace('<i>', '').replace('</i>', ''),
             (' — suite : %s' % A['suite']) if A.get('suite') else ''))
w("---\n")

# 5. FENETRES DE CIRCONSTANCE
w("## 5. Le bandeau de mission — en haut à gauche\n")
w("Le papier déchiré du coin haut gauche. Il ne porte que **deux choses** : le nom de "
  "la mission en cours, et l'étape du moment. Ni le nombre de mètres — la flèche verte "
  "le dit déjà — ni le texte du scénario, qui a été lu à la prise.\n")
w("| ligne | ce qu'elle dit | quand |")
w("|---|---|---|")
w("| **titre** | le nom court de la mission — *Livrer 30 kg de blé* | tant que la mission court |")
w("| **détail** | l'étape du moment — *Charger le blé au silo* | à chaque changement d'étape |")
w("| *(tutoriel)* | le titre de la marche seul, sans détail | pendant le tutoriel |")
w("")
w("---\n")
w("## 5 bis. Les fenêtres de circonstance\n")
w("### CONTRAT TERMINÉ — à chaque mission finie")
w("> **CONTRAT TERMINÉ**  \n> *le titre de la mission, puis la réponse du commerçant (ci-dessus)*  \n"
  "> **+ prime en gros**  \n> *+ XP · + valeur de la marchandise · nouveau palier s'il y en a un*  \n"
  "> — suite : *Prochaine mission – <lieu>*, ou *La campagne est finie*\n")
w("### LA FERME CONTINUE — après la dernière mission")
w("> **LA FERME CONTINUE**  \n> La campagne principale est terminée, mais votre exploitation "
  "continue de vivre.  \n> Contrats illimités · Vente libre · Parcelles · Élevages · Production · "
  "Améliorations  \n> — suite : *À vous de décider de la suite*  \n> *(c'est l'avant-dernière page "
  "de la mission 30, ci-dessus ; le dernier mot est le bouton CONTINUER À JOUER)*\n")
w("### NOUVEAU CLIENT — quand un palier ouvre un commerce")
w("> **NOUVEAU CLIENT** — *<NOM DU COMMERCE>*  \n> Ce commerce achète désormais certains de "
  "vos produits, même en dehors des missions.  \n"
  "> *<les produits acceptés, en vignettes — jusqu'à huit>*  \n> — suite : *À retrouver sur la carte*\n")
w("### LIVRAISON ACCEPTÉE — reçu, à chaque livraison qui solde une ligne")
w("> **LIVRAISON ACCEPTÉE**  \n> *<quantité et marchandise> → <LIEU>*  \n> **+ <gain>**  \n"
  "> *<combien> × <prix à l'unité>*  \n> — suite : *La caisse est à <argent>*\n")
w("*Une livraison **incomplète** n'ouvre aucune fenêtre : elle passe en bandeau volant, "
  "sur une ligne — « 6 / 29 kg de farine · BOULANGERIE ».*\n")
w("### STOCK SATURÉ — quand un commerce ne peut plus rien prendre")
w("> **STOCK SATURÉ** — *<NOM DU COMMERCE>*  \n> *« Pas de <marchandise> en plus pour le "
  "moment. J'en ai encore plein les étagères. »*  \n> Autres acheteurs : "
  "*<jusqu'à quatre, avec le prix à l'unité — Restaurant → 1,15 € / kg>*\n")
w("### PANNE SÈCHE — quand un engin tombe à sec")
w("> **PANNE SÈCHE**  \n> *« Voilà. Plus une goutte.  \n> Et bien sûr, je suis à l'autre "
  "bout du champ. »*  \n> — suite : *La citerne est dans la cour*\n")
w("---\n")

# 6. BANDEAUX VOLANTS
w("## 6. Les bandeaux volants — %d messages, %d textes distincts\n"
  % (len(hints), len(set(t for _, t in hints))))
w("La ligne noire en capitales, au milieu de l'écran, deux à trois secondes. Elle "
  "confirme un geste ou signale un blocage ; elle ne raconte rien.\n")
w("`<…>` marque ce qui se calcule au moment où le message paraît : un nom de commerce, "
  "une quantité, un nombre de kilos. Quand deux textes se partagent un même message — "
  "« pleine » ou « vide » —, les deux sont donnés, séparés d'une barre.\n")
w("*(%s messages de plus ne portent aucun texte à eux : ils affichent une valeur calculée "
  "ailleurs — le nom d'un engin, une quantité — et il n'y a rien à y relire.)*\n"
  % len(calcules))
par = {}
for n, t in hints:
    par.setdefault(chapitre(n), []).append(t)
for c in sorted(par):
    w("**%s**" % c)
    w("")
    for t in sorted(set(par[c])):
        w("- `%s`" % t.replace('\\u2019', '’').replace("\\'", "’"))
    w("")
w("---\n")
w("*Produit par `outils/textes` — `node relever.js` puis `python3 composer.py`. Les "
  "textes sont relevés dans le jeu qui tourne ; relancez les deux après toute "
  "modification pour que ce document reste vrai.*")

io.open(os.path.join(RACINE, 'TEXTES.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print('TEXTES.md :', len('\n'.join(L))/1024, 'Ko')
