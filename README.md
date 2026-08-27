# MOISSON

Jeu de ferme low-poly, en un seul fichier HTML. Vanilla JS + three.js, pensé pour
le mobile en paysage — et jouable au clavier sur ordinateur.

Ouvre `index.html` dans un navigateur. Rien à installer, rien à compiler.
La seule dépendance est three.js r128, chargée depuis un CDN : il faut donc une
connexion au premier lancement.

## Le mettre en ligne

Le jeu s'appelle `index.html` et vit à la racine : c'est le seul nom que tout
hébergeur statique sert sans configuration. Il n'y a donc rien à régler, ni sur
GitHub Pages, ni sur Vercel, ni ailleurs — pousser le dépôt suffit.

Mieux vaut y jouer depuis une vraie adresse qu'en `file://` : certains navigateurs
refusent le stockage local aux fichiers ouverts en direct, et la partie ne serait
alors pas conservée. Le jeu le dit sur son écran d'accueil quand il détecte le cas.

## Jouer

| | |
|---|---|
| **Volant** | manche à gauche, ou les flèches ← → |
| **Gaz** | manette à droite, ou ↑ ↓ |
| **Atteler / dételer** | le **crochet**, au centre : il porte un plus quand il y a un outil à prendre, un moins quand il y en a un à laisser |
| **Vendanger** | l'**enjambeuse**, achetée au garage : elle seule passe au-dessus d'un rang |
| **Changer d'engin** | le **garage**, tout en bas, ou les touches 1 à 4 : la liste du parc s'ouvre |
| **Automatiser** | le **A cerclé**, à droite du crochet : la carte en grand, on compose une file de tâches |
| **Voir où l'on en est** | la **barre de progression**, en haut : elle ouvre l'écran de campagne — le palier, la mission, les contrats en cours, la renommée du village, et les quinze paliers à venir |
| **Régler le semoir** | l'**épi**, à gauche du crochet — le seul bouton qui garde un mot, parce qu'aucun dessin ne dit « tournesol » |
| **Acheter, améliorer** | au **garage**, sur la rocade ouest, et nulle part ailleurs |

Les boutons de l'écran de jeu **ne portent pas de mot** : un pictogramme seul, tracé
en `currentColor`, qui prend donc la couleur du bouton — jaune quand un outil est à
portée, vert quand un plan tourne. Le nom de l'engin, lui, n'a pas disparu : il est
dans le bandeau qui s'affiche quand on en change, et dans la liste que le bouton du
garage ouvre. Les tracés sont dans `PICTOS`, et `picto('garage')` en rend un.

Un **anneau lumineux au sol** signale un endroit où s'arrêter : livraison, plein de
gazole, chargement. Il est posé sur la dalle du commerce, **devant la façade, sur l'axe
du bâtiment**, à la même distance du bord chez les seize : on franchit la porte de la
clôture, on se gare dessus. Sa couleur dit s'il y a quelque chose à y faire **avec ce
qu'on transporte en ce moment** :

| | |
|---|---|
| **Jaune, qui pulse** | en s'arrêtant ici maintenant, il se passe quelque chose |
| **Blanc, fixe** | un point de service, mais rien à y faire avec ce chargement |

Une fois à l'arrêt, **rien ne part tout seul** : le jeu demande. Et il montre **tout ce
qui est possible ici d'un seul coup** — ce qu'on dépose, ce qu'on prend, les gestes qui
ne passent pas par la benne, et jusqu'à ce qui est **empêché**, en gris, avec sa raison.
Un appui sur une action ouvre le **curseur de quantité** quand il y a quelque chose à
doser — et seulement alors : un dépôt part d'un seul appui, en entier.
Le transfert en cours reste affiché, plein, avec ce qu'il lui reste à faire ; un clic
dessus l'arrête.

Où peut-on faire quoi :

| | |
|---|---|
| **Silo, entrepôt, pâtures** | décharger **et** remplir : c'est chez toi |
| **Usines et points de vente du village** | décharger seulement — ils paient, ils gardent |
| **Garage, comptoir agricole** | ni l'un ni l'autre : un bouton, pas un transfert |
| **Atelier de la ferme** | rien : il se sert seul et dépose seul |

Une **jauge flottante** montre le remplissage au-dessus de l'engin pendant le transfert,
au-dessus du silo, de l'entrepôt, de l'atelier, de chaque enclos et de chaque parcelle
qui pousse. Elle ne se montre que dans les soixante mètres : de plus loin, la vallée
reste un paysage.

Et pendant un transfert, la marchandise **se voit**. En chargeant, des sacs et des
cageots montent un par un dans la benne du pick-up, au rythme réel du remplissage, et
ils y restent tant qu'elle est pleine. En déchargeant chez un client, les mêmes se
posent au sol à l'endroit où l'on s'est arrêté, puis s'effacent quand la barre est
finie. Ce qui coule en vrac — la trémie de la moissonneuse, une benne qu'on bascule
dans la grille du silo, le grain versé dans une auge — ne se met pas en sacs : ça
fume, à l'endroit exact où la matière arrive.

La caisse est pleine de lait ? Seule la laiterie s'allume, sur toute la vallée. On la
vide, elle s'éteint et le silo s'allume à sa place. La condition ne tient pas compte de
la distance : c'est ce qui permet de choisir sa destination d'un bout à l'autre de la
carte, au lieu d'avoir à s'y rendre pour découvrir qu'on s'est trompé de tournée.

## La campagne

Le jeu donnait tout tout de suite : sept cultures achetables à la première minute,
cinq espèces, six modules d'atelier, et l'unique frein était le prix. Qui accumulait
assez d'argent achetait le jeu entier sans avoir rien appris.

Une campagne le remplace, avec **deux valeurs globales** et pas une de plus :

- l'**argent** dit à quelle vitesse on exploite ce qu'on a ;
- l'**expérience** dit ce à quoi on a droit.

On ne peut donc pas sauter un maillon en payant. Et l'on ne peut pas non plus rester
bloqué : les contrats du village donnent de l'expérience eux aussi, et tout ce qui sort
de la ferme en donne un filet — un centième d'euro de marchandise vendue.

La règle de découverte est toujours la même : **un acheteur réclame quelque chose
qu'on ne sait pas encore produire**. C'est la demande qui enseigne la mécanique.

### Les quinze paliers

| | ouvre |
|---|---|
| 1 · Le fermier | blé, charrue, semoir, benne, tracteur, moissonneuse, pick-up, coopérative, usine de céréales |
| 2 · Productivité | l'épandeur, 350 € |
| 3 · Première transformation | le moulin, la farine, la boulangerie |
| 4 · Expansion | deuxième parcelle, maïs, deuxième tracteur |
| 5 · Élevage léger | broyeur, poules, marché |
| 6 · L'orge | troisième parcelle, orge, brasserie, fourgon |
| 7 · L'avoine | avoine, usine d'avoine, mélangeur premium, ruches |
| 8 · Les vaches | vaches, laiterie, fromagerie du village |
| 9 · Fromage fermier | fromagerie de la ferme, restaurant, troisième tracteur |
| 10 · Les moutons | moutons, brebis, atelier textile, fromagerie de brebis |
| 11 · Le colza | colza, pressoir, huile de colza |
| 12 · Les olives | oliveraie, enjambeuse, huile d'olive |
| 13 · Le raisin | vigne, cave, caviste |
| 14 · Les cochons | cochons, boucherie |
| 15 · Exploitation complète | supermarché, toute la vallée |

Un commerce est **bâti dès le premier jour** — on le voit, on passe devant — mais il
ne traite avec la ferme qu'à son palier, et sa bulle le dit depuis la route. C'est ce
qui donne à un village construit d'un bloc l'allure d'un village qui s'ouvre.

La table `NIVEAUX` est la seule source de tout cela. Elle est retournée **une fois**
en index inverse : les douze verrous du fichier l'interrogent vingt fois par seconde
sans jamais parcourir quinze niveaux.

### Les missions, et les seuils qui s'en déduisent

Vingt et une missions de campagne, une à la fois, dans l'ordre. Deux formes : **livrer**
des lignes chez un commerce nommé, ou **faire** quelque chose qui ne se livre pas —
s'équiper d'un épandeur, acheter une deuxième parcelle, monter un poulailler.

Les seuils d'expérience **ne se règlent pas** : le seuil du palier *n+1* est la somme
des expériences des missions du palier *n* et de tous ceux d'avant. Deux tables réglées
à la main finissent toujours par se contredire — un palier qu'on n'atteint pas en
faisant exactement ce que le jeu demande, ou un palier franchi avant sa mission. Faire
la campagne suffit donc toujours, très exactement, et les contrats du village permettent
d'aller plus vite sans jamais permettre de sauter un maillon.

### Les contrats se proposent, ils ne tombent plus du ciel

Quatre commandes apparaissaient toutes seules dans un coin de l'écran, sans qu'on les
ait demandées ni qu'on puisse les regarder de près : on subissait une liste au lieu de
traiter avec quelqu'un. C'est le **commerce** qui propose, maintenant, et il le dit sur
place.

Un **anneau vert** s'allume au sol, au centre de son anneau de livraison. On s'y arrête,
un bouton vert **VOIR LE CONTRAT** apparaît, et la fenêtre s'ouvre : ce qu'il réclame,
la marchandise au prix du jour, la prime à la clôture, le délai s'il y en a un, et la
renommée qu'on a chez lui. Trois réponses :

| | |
|---|---|
| **Accepter** | le contrat rejoint la liste, l'anneau vert s'éteint |
| **Refuser** | on perd **deux crans de renommée**, et il proposera moins bien, moins souvent |
| **Retour** | on n'a rien dit. L'offre reste sur place, on repassera |

Le tirage garde ses quatre natures — **brute**, **transformée**, **composée** (deux ou
trois produits chez le même client), **urgente** (en quantité, avec un délai, et elle se
perd). Le **client se choisit avant les lignes**, et pas l'inverse : en composant d'abord
un panier puis en cherchant qui le prend, une commande finissait par réclamer de l'huile
d'olive à l'usine de céréales. Relevé : **400 propositions, 0 indélivrable**.

**La renommée** est le seul état durable de cette relation : elle monte d'un cran à
chaque contrat honoré, descend de deux à chaque refus, d'un à chaque contrat urgent
laissé filer. Elle module la prime (**0,70 ×** chez qui l'on éconduit, **1,50 ×** chez
qui l'on sert depuis toujours) et l'attente entre deux propositions. Un commerce
plusieurs fois éconduit finit par ne presque plus rien offrir — sans jamais se fermer
tout à fait, parce qu'un débouché perdu pour de bon serait une partie perdue. Une
proposition laissée sur place s'efface au bout de trois minutes, sans rien coûter.

Le village ne propose jamais plus de **trois** contrats à la fois, on n'en tient jamais
plus de **quatre**, et un commerce qui a déjà une offre ou un contrat en cours ne se voit
rien proposer de plus.

**La récompense ne casse pas l'économie** : on est payé le prix normal de la marchandise
au moment où on la livre — le circuit habituel, celui des étals et des caisses d'usine —
puis la prime s'ajoute à la clôture. Les prix du village restent donc exacts.

### Rien à l'écran qu'on n'ait accepté

C'est la règle, et elle n'a pas d'exception. Une proposition qui attend sur un anneau vert
ne pose **aucune** puce au bandeau, et ne déroule ses lignes ni dans l'onglet Campagne, ni
dans l'onglet Filières : la Campagne dit seulement qu'un commerce « a quelque chose à
proposer — passer devant son quai pour l'entendre ». Un menu qui donnerait le détail
rendrait l'anneau décoratif : on choisirait ses contrats depuis un tableau, sans jamais
aller voir personne.

La seule chose du bandeau qu'on n'a pas acceptée quelque part est la **mission de
campagne**, et elle porte le mot pour qu'on ne la confonde pas avec un contrat.

### Le bandeau ne mange plus l'écran

Quatre pilules de commande, deux lignes chacune, occupaient la moitié gauche de
l'écran : on jouait derrière sa liste de courses. Un contrat accepté tient maintenant
dans une **puce d'une ligne** — le lieu, l'avancement, le délai s'il court — de 23 px de
haut, large de son seul texte. On la touche et la même fenêtre se rouvre, en lecture
seule cette fois, avec ce qui reste à livrer ligne par ligne.

Relevé, quatre contrats plus la mission de campagne : **406 × 190 px avant, 257 × 158
après** — de 8,5 % à 5,3 % de l'écran, et la largeur ne suit plus le bloc mais le texte.

### Les temps

| | pousse | avec engrais |
|---|---|---|
| Blé | 75 s | 55 s |
| Avoine | 90 s | 66 s |
| Orge | 100 s | 73 s |
| Maïs | 120 s | 88 s |
| Colza | 150 s | 110 s |
| Raisin | 210 s, puis **150** | 175 s |
| Olives | 240 s, puis **180** | 200 s |

Une permanente **repart plus vite qu'elle ne s'installe** : c'est ce qui paie l'attente
initiale, et ce qui la distingue d'une annuelle autrement que par le fait de ne pas
relabourer. Un cinquième plan de la grille, `replante[]`, dit qu'un pied est en place ;
il n'entre pas dans la sauvegarde compressée — quatre plans y sont empilés et leur
ordre est figé dans les parties enregistrées — il se redéduit à la relecture.

L'engrais gagne **27 % de temps sur les annuelles** et 17 % sur les permanentes, au lieu
de 44 % partout : à 44 %, la même terre devenait presque deux fois plus productive pour
trois euros d'épandage, et la décision n'en était plus une.

### L'échelle des prix

La première parcelle à racheter valait 4 000 € quand la ferme commence à zéro et qu'une
première livraison rapporte 135 : il fallait une trentaine de tournées avant le premier
agrandissement. Elle vaut **1 200 €**. L'échelle monte ensuite de moitié à chaque cran —
1 200, 2 500, 4 500, 7 500, 12 000 — puis s'aplatit à partir de la dixième : un empire
ne doit pas doubler de prix indéfiniment. Le total reste du même ordre qu'avant ; c'est
sa **répartition** qui change, et avec elle les vingt premières minutes.

## La chaîne

Rien ne se vend deux fois de la même façon. Chaque matière a **au moins une vente
directe**, et presque toujours une transformation qui paie mieux. C'est l'arbitrage
central du jeu : encaisser tout de suite, ou faire un détour.

| | vaut |
|---|---|
| **Brut**, vendu tel quel | ×1 |
| Après **une transformation** | ×1,5 |
| **Produit fini** | ×2 |
| Recette à **plusieurs ingrédients** | ×2,5 |
| **Commande** ou contrat | ×3 |

Le barème porte sur la matière engagée, pas sur le kilo produit, et le prix au kilo
s'en déduit tout seul. Un kilo de blé vaut 0,50 € ; moulu il rend 0,72 kg de farine,
qui doit valoir une fois et demie le blé de départ : la farine vaut donc 1,04 € le
kilo. Aucun prix n'est écrit à la main — on ne règle qu'un rendement et un palier.

L'onglet **Filières** affiche la chaîne entière, prix compris, relue dans les mêmes
tables que celles qui paient. Ce qui est affiché est ce qui sera versé.

Le **restaurant** portait une commande permanente : trois produits tirés au sort à
l'ouverture, peints sur son enseigne, payés d'une grosse prime dès qu'on l'avait remplie —
sans qu'on l'ait jamais acceptée. C'était le dernier contrat du jeu qu'on subissait au
lieu de le prendre, et il n'y avait nulle part où le refuser. Il propose maintenant comme
tout le monde, par son anneau vert. Sa tournée composée n'est pas perdue : c'est
exactement ce que fait le contrat **composé**, et le restaurant est celui qui accepte le
plus de produits.

### Sept cultures

Blé, maïs, orge, avoine et colza vont au **silo**, qui tient un tas par céréale : la
trémie de la moissonneuse ne mélange pas, une culture à la fois. La **vigne** et
l'**olivier** sont pérennes — plantés une fois, ils restent sur leur parcelle et
repartent en croissance dès qu'on les a récoltés. Ils n'entrent pas au silo : du champ
au pressoir ou à l'étal, directement.

Chacune a sa plante : l'épi barbu de l'orge, la tige haute du maïs et ses feuilles
retombantes, les grappes de fleurs du colza, la panicule lâche de l'avoine, le rang
palissé de la vigne, l'olivier noueux. Un rang de vigne sur deux, un olivier toutes les
vingt-cinq cellules — une plantation, pas un semis.

**La vigne n'est plus plate.** Sa souche était écrite petite et c'est `haut` qui la
montait — or ce coefficient ne multiplie QUE l'axe y. À 1,93 il étirait le pied de près du
double en hauteur sans rien lui donner en épaisseur : les boules de 0,40 m du feuillage
sortaient en ellipsoïdes de 0,63 m de large pour 1,44 de haut, et le fil devenait un ruban
deux fois plus haut que large. Relevé sur un pied mûr : 0,86 m en x pour 3,22 en y, un
rapport de 0,27 — vue de la caméra, la parcelle se lisait comme une suite de lames. Tout
est réécrit EN MÈTRES, à la cote que la plante doit vraiment avoir, `haut` et `large`
retombés à 1,00 : l'épaisseur passe de 0,86 à **1,26 m** pour un sommet inchangé à 3,21,
et le rapport épaisseur sur longueur de rang de 0,56 à 0,85. Trois masses de feuillage au
lieu de deux, décalées en x autant qu'en z. Huit triangles de plus par pied.

**L'olivier était plus bas qu'un pied de maïs.** 3,45 m au plus gros tirage, contre 3,80
pour le maïs et 3,54 pour l'orge, quand les arbres d'ornement de la même parcelle montent
à dix mètres : une oliveraie se lisait comme un champ de buissons. Il passe à **4,59 m**,
un tiers de plus, pour un houppier de 4,57 m. La maille suit l'arbre — une cellule sur
vingt-cinq au lieu d'une sur seize, 6,50 m d'entraxe au lieu de 5,20 — sans quoi il ne
resterait que huit centimètres entre deux voisins, c'est-à-dire le maquis que la maille
était censée éviter. Le rendement ne bouge pas : il se compte à la cellule récoltée, pas à
l'arbre. Et le tunnel de l'enjambeuse suit, 3,55 → **4,75 m**, avec sa tête de colonne
raccourcie en même temps pour que l'engin ne grandisse que de 55 cm au lieu de 1,20 m.

### Les élevages

**Un corps d'un seul tenant.** Le tronc d'une vache ou d'un cochon était un fût coiffé de
deux billes : trois volumes, et deux **raccords** bien visibles. Le fût a quatorze pans
réguliers, la bille est un icosaèdre subdivisé — leurs facettes ne tombent jamais en face,
et l'ombrage à facettes souligne la couture d'un anneau net à chaque épaule et à chaque
hanche. Un profil tourné donne le même volume — flanc droit, bouts arrondis et aplatis
comme ils l'étaient — en **une** géométrie, sans raccord, et pour **moins de triangles**
qu'avant : 356 contre 376 pour la vache, 556 contre 576 pour le cochon. Le flanc garde
son rayon, donc les taches de robe s'y posent sans rien changer.

Et les deux grandissent : la vache passe de 3,72 à 4,27 m de long et de 1,89 à 2,16 m au
garrot, le cochon de 2,77 à 3,22 m et de 1,40 à 1,62 m.


Une parcelle possédée s'aménage en enclos. Quatre espèces, chacune avec son
aménagement, son produit et son débouché :

| | donne | où ça va | à l'enclos |
|---|---|---|---|
| **Vaches** | du lait | laiterie (beurre, yaourt), fromagerie | tank à lait, auge, stabulation |
| **Poules** | des œufs | boulangerie, ou vente directe | casier à œufs, trémie, poulailler sur pilotis |
| **Cochons** | rien en continu | boucherie, en viande | auge, cabane, bauge de boue |
| **Moutons** | de la laine | atelier textile | presse à balles, râtelier, bergerie |

L'espèce se choisit dans l'onglet Élevage, avant d'aménager. Toutes mangent les
céréales du silo, apportées à la benne — ou l'aliment de l'atelier, qui remplit la
mangeoire une fois et demie mieux, deux fois pour l'aliment premium. Une bête qui n'a
rien à manger ne donne rien et ne grandit pas.

**Tout se fait devant le portail.** Un seul anneau par enclos, planté sur le chemin à
quatre mètres de l'entrée : on s'y arrête et la colonne propose ce qu'il y a à faire
ici — acheter une bête, remplir la mangeoire, charger le produit, embarquer pour la
boucherie. Rien n'oblige plus à franchir la clôture ni à chercher lequel des trois
anneaux dispersés dans l'enclos était le bon.

Deux jauges flottent au-dessus de chaque enclos, comme la pousse au-dessus d'une
parcelle : ce qu'il reste à manger et pour combien de temps, puis où en est la cuve du
produit — grise et « à l'arrêt » quand la mangeoire est vide, rouge quand elle
déborde.

La boucherie ne paie pas de billets : elle abat et met la carcasse en chambre froide.
On revient la charger, et c'est le restaurant qui la paie le mieux. Une bête vaut
ainsi deux fois son prix de marché, au prix d'une tournée de plus.

## L'atelier : huit métiers, trois réglages

Il portait cinq paliers, chacun donnant à la fois un module et de la capacité, et le
premier était offert. Les deux choses se séparent.

**Huit métiers**, qu'on monte un par un — et chacun a son propre temps, qui dit sa
valeur :

| | | les 100 kg engagés |
|---|---|---|
| Moulin | blé → farine | 20 s |
| Broyeur | maïs → aliment | 15 s |
| Mélangeur premium | maïs + orge + avoine → aliment premium | 30 s |
| Fromagerie | lait → fromage | 90 s |
| Fromagerie de brebis | lait de brebis → fromage de brebis | 120 s |
| Pressoir à colza | colza → huile | 60 s |
| Pressoir à olives | olives → huile d'olive | 90 s |
| Cave | raisin → vin | 120 s |

**Trois réglages universels**, qui ne donnent aucun métier neuf mais changent le
rythme : la **capacité** d'un lot (100 → 250 → 500 → 1 000 kg de matière engagée), la
**vitesse** (100 → 150 %), et la **file** (1 → 5 lots empilés). En début de partie on
revient lancer chaque transformation ; à la fin on prépare cinq lots et l'on part faire
les foins. Un joueur qui ne fera jamais de vin n'a plus à payer la cave pour avoir du
débit.

Un lot se mesure en **matière engagée** et non en produit sorti : « cent kilos par lot »
doit vouloir dire la même chose au moulin, où cent kilos de blé donnent 72 kg de farine,
et à la cave, où cent kilos de raisin en donnent 70.

La silhouette du bâtiment grandit en **huit crans** au lieu de cinq et finit exactement
aux mêmes cotes qu'avant — 13,4 m de large. Ce qui change, c'est qu'on la voit grandir
huit fois.

## Le lait de brebis et les deux fromages

La brebis se conduit comme un mouton — même silhouette, mêmes robes claires, même
clôture — mais elle donne du **lait en plus de la laine**. C'est la première espèce du
jeu à porter deux produits, sur deux tanks et une seule jauge : celle-ci suit le tank le
plus plein, c'est-à-dire celui qui va déborder, et son étiquette nomme les deux.

Cent kilos de lait de vache font **12 kg** de fromage ; cent kilos de lait de brebis en
font **20**. Le fromage de brebis n'est pas un fromage plus cher : c'est un **produit
fini**, qui vaut donc le palier ×2 et non ×1,5 — le mieux payé que la ferme sache
fabriquer, à 11,00 € le kilo contre 7,75.

La fromagerie du village reste utile : elle achète le lait directement. Le choix est
donc entier — lait à la fromagerie, argent tout de suite ; ou lait à l'atelier, fromage
au restaurant, davantage d'argent contre du temps et du transport.

## Deux magasins, et un atelier qui travaille seul

La chaîne tenait en trois trajets sur la même dalle : charger du blé au silo, le porter
vingt mètres plus loin à l'atelier, revenir chercher la farine. Elle tient maintenant en
deux magasins.

| | prend | rend |
|---|---|---|
| **Silo** | les cinq céréales, et rien d'autre | de quoi nourrir les bêtes ou livrer la coopérative |
| **Entrepôt** | tout le reste : raisin, olives, lait, œufs, laine, miel — et tout ce que l'atelier produit | tout ce qu'il a |

L'**atelier** n'a plus de quai : il tire tout seul de quoi travailler dans les deux
magasins, et pousse tout seul ce qu'il a fini dans l'entrepôt. On ne s'y arrête plus,
on n'y verse plus rien, on ne vient plus rien y chercher.

**Mais il ne fabrique rien de lui-même.** Il tournait en permanence sur la dernière
recette choisie : on rangeait du blé au silo et l'on retrouvait de la farine à
l'entrepôt sans l'avoir demandé, ce qui décidait à la place du joueur de ce que valait
sa récolte. Il honore maintenant une **commande** — tant de kilos de tel produit — et
ne touche à rien tant qu'on ne lui en a pas passé une. Il s'arrête pile sur la quantité
demandée, et s'arrête aussi, en le disant, s'il n'y a plus de matière.

L'écran de production, ouvert au bouton **usine**, met en avant les deux chiffres qui
décident — ce qu'on a en magasin et ce qu'on peut en sortir — en vert quand on peut
lancer, en rouge quand la matière manque, en bleu quand le module n'est pas encore
construit. Le bouton **Produire** suit la même règle : vert s'il y a de quoi, gris
sinon. Il ouvre un **curseur de quantité** — un quart, la moitié, tout, ou n'importe
quoi entre les deux — qui annonce ce qui sortira, ce que ça consommera, et ce que la
même matière vaudrait vendue brute.

Trois boutons en bas à gauche disent l'état de la ferme sans qu'on ait à traverser le
menu. Chacun est tenu par la couleur de l'écran qu'il ouvre, et chacun ouvre **sa
propre fenêtre** — un titre, une liste, une croix. Ils menaient au menu général sur un
onglet : on arrivait dans une barre de huit onglets, au milieu de choses qui n'avaient
rien à voir avec le geste demandé. Ces trois écrans ne sont d'ailleurs plus des onglets
du menu : deux chemins vers le même endroit, c'était un de trop.

| | |
|---|---|
| **les caisses empilées** | ce qui dort au silo, à l'entrepôt, et ce qui roule dans les bennes |
| **l'usine** | pour chaque module, la conversion en clair — cent kilos de blé donnent soixante-douze kilos de farine —, ce que le stock permet d'en sortir, ce que la même matière vaudrait brute, et le bouton qui lance la production |
| **l'étiquette** | qui achète quoi et à combien, du mieux-disant au moins cher, avec la place restante sur les étals et ce que la matière rapporterait transformée |

Cinq paliers, et chacun se voit sur le bâtiment :

| | module | débloque | ce qu'on voit |
|---|---|---|---|
| **1** | Moulin | blé → farine | la halle, sa trémie, son quai |
| **2** | Broyeur | maïs → aliment | deuxième trémie, mélangeur, hall latéral |
| **3** | Pressoir | colza → huile de colza, **et** olives → huile d'olive | deux cuves, passerelle, cheminée, bidons |
| **4** | Mélangeur | maïs + orge + avoine → aliment premium | appentis, conteneur, palettes en nombre |
| **5** | Cave | raisin → vin | étage technique, auvent de quai, aire rangée |

L'atelier ne travaille qu'une recette à la fois : réglé sur le moulin, il laisse le
raisin tranquille. Le module et le palier suivant se choisissent au bouton
**PRODUCTION**. Les paliers 4 et 5 augmentent aussi la capacité et le débit.

L'aliment ne se vend pas, il se donne aux bêtes. Tout le reste part sur la route.

## Le gazole

Il n'y a pas de pompe publique. Le gazole s'achète en gros à la coopérative, livré dans
la cuve de la ferme, et c'est là que se font tous les pleins. Un engin à sec n'est pas
immobilisé : il se traîne au ralenti jusqu'à la cuve.

## Le plan de travail

Le bouton du **A cerclé** ouvre la carte en grand — la seule vue d'ensemble du jeu. On y
désigne un engin, ce qu'on lui demande, et où :

- **Travailler des parcelles** : on touche les parcelles à la suite. L'engin les fait
  dans l'ordre, avec l'outil qu'il porte, en serpentin. La moissonneuse va vider au
  silo quand sa trémie est pleine, puis reprend sa passe.
- **Navette entre deux lieux** : on touche un départ, puis une arrivée, puis **ce
  qu'elle transporte**. L'engin charge au premier, décharge au second, et recommence.
  Coché **EN BOUCLE**, il ne s'arrête plus : le silo vers l'usine de céréales, sans fin.

La file se lit en bas de la carte et se défait au doigt. En chemin entre deux étapes,
un engin en mission ne touche à rien : il traverse le silo sans s'y vider.

**Une navette a une nature.** La file disait « Silo → Usine céréales » et rien de plus :
l'engin chargeait le premier tas venu, et l'on découvrait au retour qu'il avait livré de
l'avoine là où l'on attendait du blé. La question se pose donc à la création du trajet,
et ne propose que ce qui a un sens dessus — ce que le départ peut donner ET ce que
l'arrivée veut bien prendre : trois céréales pour l'usine de céréales, l'orge seule pour
la brasserie, les quatre grains que mangent les bêtes pour une pâture. Les deux tables
raisonnent en POSSIBLE et non en présent : un plan est un ordre permanent, il doit se
composer même quand le tas est momentanément vide. Répondre **Tout**, ou reprendre un
plan composé avant que la question existe, rend le comportement d'origine — on prend ce
qui vient. Et quand le tas demandé est vide, l'engin repart à vide plutôt que de charger
autre chose. Le libellé de la tâche rouvre le choix, la croix l'efface.

**La carte se pince pour grossir.** Elle tenait le monde entier dans un rectangle de
trois cents pixels : une parcelle y faisait vingt pixels de côté et un point de
chargement cinq de rayon, si bien que désigner le bon relevait de la chance. Deux doigts
qui s'écartent grossissent jusqu'à six fois, autour du point qu'ils encadrent ; un doigt
qui glisse déplace le cadrage, qui ne sort jamais de la carte. La désignation se fait
alors au RELÂCHEMENT et non plus à l'appui : tant qu'on appuie, on ne sait pas encore si
le doigt va rester en place — c'est un choix — ou partir — c'est un déplacement. Huit
pixels de tolérance, la largeur d'un doigt qui tremble.

**La carte dit ce qu'il y a à faire.** Elle montrait vingt rectangles de la même couleur :
on savait où étaient ses parcelles, pas lesquelles attendaient quelque chose. Chacune
prend maintenant la couleur de son état — violet pour un élevage, jaune pour une culture
à moissonner, vert pour une culture en pousse, terre pour une parcelle à semer, brun pour
une parcelle à labourer — et, dès qu'on grossit assez pour la lire, elle porte son
écriteau : le nom de la culture et son avancement en pour-cent, « à moissonner » quand
elle est mûre, l'espèce et le nombre de bêtes sur ses places pour un enclos. C'est ce qui
permet de choisir quel engin envoyer où sans quitter la carte.

## La nuit

Les optiques sculptées sur chaque engin s'allument elles-mêmes : la lentille passe à
l'émissif et une bille de lumière s'épanouit autour. Un engin garé reste éteint, comme il
a le moteur coupé ; le gyrophare bat dès qu'on roule.

**La lumière s'éteint sur ses bords.** La bille et le halo au sol étaient d'une couleur
unie : ils se terminaient au couteau. Mesuré à la verticale d'un lampadaire, la flaque
perdait 43,8 niveaux de luminance sur 255 en un pixel, et la bille 103,4 — c'est cette
découpe qu'on voyait, pas de la lumière. Une seule texture de dégradé radial, 64 × 64 et
16 Ko, partagée par les quatre-vingt-dix halos du jeu : la marche tombe à 7,2 et 27,8, le
cœur ne bouge pas (75,1 avant comme après), et la bille devenue lutin coûte deux triangles
au lieu de quatre-vingts. Le dégradé ne mord que sur le dernier tiers du rayon.

**Deux cônes par engin, un par phare.** Il n'y avait qu'un rond posé devant le nez, sans
lien visible avec les deux optiques. Chaque phare avant projette maintenant son faisceau,
tronqué à la largeur du verre, incliné vers le sol et ouvert de 8,8° — et il s'y dissout
au loin par une couleur de sommet qui tend vers le noir, ce qui en mélange additif revient
à disparaître. La pente n'est pas écrite, elle se déduit de la hauteur du phare — 1,75 m
sur un tracteur, 6,90 sur l'enjambeuse. Les cônes sont enfants de la CAISSE, pas du
groupe : le faisceau prend le roulis et le tangage, et balaie le paysage quand la machine
passe une bosse. Le halo au sol des engins a disparu avec eux — le cône entre dans le sol,
et le sol opaque y découpe la flaque tout seul, à la bonne place et de la bonne forme. Les
lampadaires gardent le leur.

**Et c'est le BAS du faisceau qui vise le sol, pas son axe.** En pointant l'axe sur le
point d'atterrissage, la moitié basse du tronc passait sous le sol bien avant le bout — et
le sol, opaque, écrit sa profondeur : cette paroi-là était retirée. Or c'est de la
traversée des DEUX parois que le cône tient son cœur clair. Le faisceau se fendait donc en
deux rails lumineux encadrant une arche sombre : mesuré, le milieu tombait à 46 % de ses
bords sur le quart à la moitié de la longueur, le fourgon et le pick-up étant les pires
parce que leurs phares sont bas. On vise maintenant avec le bas du cône, on le coupe là où
ce bas touche la terre — plus un cinquième, où sa couleur est déjà sous un dixième — et on
l'écrase de moitié, un faisceau de phare étant plus large que haut. La part creuse tombe
de 25-57 % à **16 %**, sur la seule portion où l'on ne voit plus rien.

## La boucle de jeu

```
              comptoir agricole
               (semences, engrais, gazole en gros)
                       |
   labour -> semis -> engrais -> moisson -> trémie
                                              |
                       +----------------------+
                       |
             silo -+-> coopérative : rachète les cinq céréales, tout de suite
                   |
                   +-> atelier (il se sert seul) -+-> farine       -> entrepôt
                   |                              |-> huile        -> entrepôt
                   |                              |-> aliment      -> entrepôt
                   |                              \-> vin          -> entrepôt
                   |                                       |
                   |   entrepôt -+-> boulangerie / marché / restaurant / caviste
                   |             |-> les mangeoires, pour l'aliment
                   |             \-> raisin, olives, lait, œufs, laine, miel en attente
                   |
                   +-> usines du bord de route : on verse, elles PAIENT
                   |     orge   -> brasserie      -> bière
                   |     avoine -> usine d'avoine -> lait d'avoine
                   |     blé/maïs/avoine -> usine de céréales -> céréales
                   |     lait   -> laiterie   -> beurre + yaourt
                   |     lait   -> fromagerie -> fromage
                   |     laine  -> atelier textile
                   |     (elles vendent elles-mêmes : rien à revenir chercher)
                   |
                   +-> nourrisseur -> ruches -> miel (le brut le mieux payé)
                   |
                   \-> mangeoire -> vaches  -> lait
                                 |-> poules  -> œufs
                                 |-> moutons -> laine
                                 \-> toute bête adulte -> boucherie (paie sur place)

   et au bout, l'échelle des acheteurs — chacun plafonné par nature :
                caviste      +15 %, 600 kg    (vin, raisin)
                restaurant   +10 %, 900 kg
                coopérative    0 %, 7 000 kg  (les cinq céréales)
                marché        −6 %, 2 000 kg
                supermarché  −14 %, 9 000 kg
```

**Le mieux-disant ne peut pas tout prendre.** Chaque acheteur a un plafond par nature,
et ce plafond est l'inverse de son prix : le caviste paie le vin le mieux de tous mais
n'en écoule que six cents kilos, le supermarché paie le moins et en prend neuf mille.
Tous se refont en deux minutes. D'où la seule vraie question d'une tournée — vendre le
haut de la benne au prix fort puis descendre l'échelle, ou tout donner d'un coup au
moins-disant et repartir travailler. Deux mille kilos de vin rapportent 6 940 € en
descendant l'échelle, 5 400 € si l'on vide tout au supermarché.

**Un contrat accepté échappe au plafond** : le commerce qui a demandé cent vingt kilos de
lait a promis de les prendre, et son étal ne peut pas les lui refuser même à zéro de
place. C'est ce qui fait d'un contrat un débouché garanti, au meilleur prix, et ce qui
justifie d'aller monter une tournée pour lui. La règle ne valait que pour le restaurant,
parce qu'il était le seul à commander ; elle vaut maintenant partout où l'on a signé.

La vigne et l'olivier court-circuitent le silo : du champ à l'entrepôt, puis à la cave,
au pressoir ou à l'étal. Vingt parcelles à racheter une à une, un matériel à améliorer, des contrats à
durée limitée, et une progression en onze paliers.

## Ce que contient le fichier

Le code est découpé en sections numérotées, dans l'ordre où on les lit :

| | |
|---|---|
| 1 – 3 | palette, produits et barème, moteur de rendu, géométrie |
| 4 – 7 | sol peint par tuiles, grille de culture, peintures de travail |
| 8 – 9 | le blé en `InstancedMesh`, le décor et les props |
| 10 – 12 | machines, physique des véhicules, particules |
| 13 – 15 | monde, entrées, HUD |
| 16 – 20 | cycle jour/nuit, carburant, consommables, points de service, élevage |
| 21 – 25 | cuve de ferme, transport typé, boutons contextuels, jauges, boutique |
| 26 – 30 | son, sauvegarde, écran d'accueil, progression, boucle principale |

Quelques partis pris qui expliquent le reste :

- **Un bâtiment n'apporte pas son propre socle.** Le jeu pose une dalle sous chaque
  commerce ; un socle par-dessus ferait une seconde épaisseur, dans un autre gris. Les
  places, la terrasse, le plancher d'une halle sont peints SUR la dalle, à plat.
- **Un enclos s'ouvre sur un chemin, jamais ailleurs.** Le portail était au milieu du
  bord nord quoi qu'il y ait devant : sur une parcelle de bordure il donnait droit sur
  la clôture de la ferme, et l'enclos devenait inaccessible sans que rien ne le dise.
  Le côté d'entrée se choisit maintenant sur la trame des chemins, et tout
  l'aménagement — clôture, postes, quai, rangs de ruches, sentes — se lit dans un
  repère lié au portail.
- **Et il TOURNE avec lui.** Le tank, la mangeoire et l'abri étaient déplacés dans ce
  repère mais jamais pivotés : tant que tous les portails donnaient au nord ça ne se
  voyait pas, mais depuis qu'un enclos s'ouvre là où passe un chemin, un enclos sur
  deux avait son tank en travers, sa mangeoire perpendiculaire aux bêtes et son abri
  ouvert sur une clôture. Ils reçoivent l'angle du portail, et leur emprise de
  collision suit le quart de tour. L'abri fait demi-tour de plus : sa façade ouverte
  regarde le pré, pas le fond.
- **Ce qui arrête un engin est un mur, pas un terrain.** L'emprise de collision d'un
  commerce couvrait sa dalle entière, parvis compris : l'anneau de livraison tombait
  4,60 m à l'intérieur, et l'on butait sur du bitume vide six mètres avant la façade.
  Un engin lancé droit sur l'anneau n'en atteignait aucun des seize ; il les atteint
  tous, avec quatre mètres de marge. On ne pousse que la bâtisse, aux cotes relevées
  sur son modèle.
- **Un sol de couleur se peint, il ne se pose pas.** Le rucher faisait exception : ses
  fleurs poussaient sur une dalle verte de six centimètres, seul enclos du jeu à
  empiler un volume coloré sur l'herbe déjà peinte. Les fleurs sont dans l'herbe.
- **Un bâtiment qui refait ce qu'on fait chez soi n'est pas un débouché, c'est un
  détour.** L'huilerie du bord de route pressait le colza que l'atelier de la ferme
  presse déjà ; elle a été déposée, et son pressoir à olives est passé à l'atelier — le
  palier 3 en porte donc deux, seul palier double du jeu.
- **Aucun acheteur ne doit être strictement dominé.** Un commerce qui paie moins ET
  prend moins qu'un autre n'a aucune raison d'exister ; c'était le cas du supermarché
  sur ses huit produits et du marché sur huit de ses neuf. Le prix et le plafond vont
  maintenant en sens inverse, produit par produit, et la vérification en est un test.
- **Ce qui ne bouge pas se recuit en une géométrie.** Un commerce était fait de jusqu'à
  cent vingt-cinq volumes séparés, donc de cent vingt-cinq appels de dessin ; le
  village en demandait deux cent dix-huit par image, et c'est le nombre d'appels qui
  étrangle un téléphone. Les parties fixes sont fusionnées, couleurs comprises : mêmes
  pixels, un appel. Ce qui tourne ou grandit reste dehors, marqué `userData.anime`.
- **Une bricole ne projette pas d'ombre.** La passe d'ombre redessinait deux mille
  objets par image — les quatre cinquièmes du temps de rendu — dont la moitié faisait
  moins d'un mètre quarante d'emprise. À la distance de la caméra, l'ombre d'un cageot
  fait trois pixels. C'est l'emprise au sol qui décide, pas la hauteur.
- **Le sol est une texture, et une texture se paie en octets.** Une tuile salie par un
  passage d'outil est redonnée en entier à la carte graphique. Elle mesure donc 27,5 m
  pour 320 pixels et non 55 m pour 640 : même définition au pixel près (11,64 px/m),
  même mémoire (39 Mo), mais quatre fois moins d'octets par envoi. La boucle n'en
  redonne que deux par image, en tourniquet. Le budget — 0,8 Mo par image, où qu'on
  travaille — est vérifié par un test, parce que c'est le genre d'invariant qu'un
  décalage d'origine casse sans prévenir : c'est exactement ce qui était arrivé quand
  la rangée nord a déplacé une couture à cinq mètres d'un chemin de sable.
- **Ce qui ne change pas soixante fois par seconde n'est pas calculé soixante fois par
  seconde.** La condition des anneaux se relit huit fois par seconde, l'interface vingt
  ; la respiration des anneaux, elle, reste à chaque image — c'est elle qu'on voit. La
  liste des actions, en revanche, n'est PAS mémorisée : elle est relue juste après
  chaque transfert, et une liste vieille d'un transfert ment.
- **On travaille en escargot, jamais en serpentin.** Le pilote débordait de 2,5 m hors
  de la parcelle pour en travailler les bords : sur une parcelle de bordure, ces
  2,5 m tombaient dans la clôture. Il tourne maintenant autour de la parcelle en se
  resserrant d'une largeur d'outil à chaque tour, en entrant par le coin le plus
  proche. Rien ne sort du rectangle, et le premier segment est toujours parallèle à
  un bord.
- **Un champ ne se traverse que lorsqu'on y travaille.** Pour aller d'un lieu à un
  autre, l'automatisation rejoint la grille des chemins de sable et des rocades, la
  suit, et ne la quitte qu'au dernier moment — au lieu de viser sa destination en
  ligne droite à travers les semis.
- **Une espèce n'est qu'une ligne de table.** Prix, ration, produit, silhouette,
  places : tout l'élevage se lit dans `ESPECES`, et le reste du code ne connaît aucun
  nom d'animal. C'est ce qui a permis d'ajouter un rucher — une espèce qui ne marche
  pas, ne se revend pas et n'a pas de portail — sans toucher à la mécanique.
- **Le sol est une texture peinte**, pas une géométrie. Chaque passage d'outil peint
  le quadrilatère réellement balayé entre deux images, ce qui aligne l'effet au
  centimètre sur la largeur de l'outil et évite les trous dans les virages.
- **Les outils sont indépendants des tracteurs.** Un outil dételé reste au sol ; ses
  caractéristiques de travail voyagent avec lui, pas avec l'engin qui le tire.
- **Chaque récolteuse ses cultures.** Une coupe couche ce qu'elle traverse : elle ne
  passe pas dans une vigne. Une enjambeuse enjambe un rang : elle n'a rien à faire dans
  un blé. La moissonneuse ne prend que les annuelles, l'enjambeuse que les pérennes, et
  chacune remplit son propre réservoir — la trémie globale pour l'une, sa benne pour
  l'autre. Deux récolteuses qui partageraient une trémie se bloqueraient l'une l'autre.
- **Un chargement a une nature** — une clé de la table des produits. Une caisse
  entamée n'accepte plus rien d'autre : c'est ce qui oblige à planifier ses tournées.
- **Un transformateur, c'est toujours la même mécanique** : une trémie, un stock, une
  recette entre les deux. L'atelier de la ferme et les usines du bord de route
  partagent le même code ; seule change la liste des recettes — et, chez les usines,
  le stock est remplacé par une caisse : elles vendent ce qu'elles font.
- **On ne charge que chez soi.** Silo, entrepôt, pâtures : les deux sens. Le village
  achète, il ne rend rien. Faire des allers-retours pour récupérer chez une usine ce
  qu'on venait de lui vendre, c'était trois arrêts pour une seule récolte.
- **Deux magasins, pas trois.** Le silo prend les céréales, l'entrepôt prend tout le
  reste, et l'atelier fait la navette entre les deux sans qu'on s'en mêle. Charger du
  blé pour le porter vingt mètres plus loin, c'était un trajet qui n'apprenait rien et
  ne décidait rien — le seul trajet qui compte est celui qui va vendre.
- **Ce qui change de main se voit.** Un transfert n'était qu'une barre qui montait :
  la benne d'un pick-up qu'on venait de remplir de six cents kilos restait vide à
  l'œil. Les sacs et les cageots y montent maintenant un par un, et se posent au sol
  quand on décharge. Ce qui coule en vrac fume au lieu de s'emballer.
- **Un transfert ne démarre jamais sans qu'on l'ait demandé.** Deux boutons, deux
  temps, toujours les mêmes : le sens, puis la marchandise.
- **Une recette n'a rien à déclarer** : le nom du produit suffit, puisque la table des
  produits dit déjà de quoi il est fait, ce qu'il rend et à quel palier il appartient.
- **Un anneau ne s'allume jamais pour le seul fait qu'un panneau peut s'ouvrir.** Il
  s'allume quand quelque chose se passe dans le monde.
- **Le texte est petit, et c'est voulu.** Tout s'écrit entre 8 et 13 px : sur un
  téléphone en paysage, chaque pixel de hauteur gagné est une ligne de liste en plus.
  Un menu qu'on fait défiler est un menu qu'on ne lit pas.
- **L'éclairage est presque uniforme**, avec des ombres longues mais claires. Les
  couleurs des faces doivent rendre pleines, pas modelées.
- **Une lampe brille, et pose un halo sur ce qu'elle éclaire.** Trois pièces, les
  mêmes partout : un corps émissif, une bille additive autour, un disque additif à plat
  sur le sol. Rien de dégradé, rien de calculé — c'est de la lumière peinte, et elle ne
  coûte rien. Seul le gyrophare n'a pas de halo : sa flaque ne suivait rien. Les autres
  marques lumineuses au sol sont les anneaux d'action.
- **Ce qui allume un anneau est ce qui agira.** La liste des transferts possibles à un
  endroit sert à la fois à colorer l'anneau, à remplir la colonne de choix et à déplacer
  la marchandise : il ne peut donc exister ni anneau jaune sans effet, ni effet sans
  anneau jaune.

## Tout ce qu'on peut faire ici, d'un seul coup d'œil

La colonne de l'anneau demandait d'abord **DÉCHARGER** ou **REMPLIR**, puis quoi : deux
appuis, et la moitié des possibilités cachée derrière le premier. Elles sont maintenant
toutes montrées, à plat, dans l'ordre où l'on y pense — ce qu'on dépose, ce qu'on prend,
puis les gestes qui ne passent pas par la benne.

**Et ce qui est empêché s'affiche aussi**, en gris, avec sa raison. C'est ce qui manquait
le plus : arrivé à l'enclos avec un tracteur nu, on ne voyait pas « charger le lait »,
rien ne disait qu'il fallait une benne, et l'on en concluait que le jeu ne le permettait
pas. Le même enclos annonce désormais :

| | |
|---|---|
| **ACHETER UNE VACHE · 1 200 €** | en or : on peut |
| CHARGER LAIT — IL FAUT UNE BENNE OU UN UTILITAIRE | en gris, et l'on sait quoi aller chercher |
| REMPLIR L'AUGE — IL FAUT APPORTER DE QUOI NOURRIR | |
| EMBARQUER UNE BÊTE — IL FAUT LE PICK-UP OU LE FOURGON | |

L'entrepôt explique de même qu'il ne prend pas les céréales — elles se rentrent au silo —
au lieu de rester muet.

**Un curseur de quantité, mais pas pour un dépôt.** Il s'ouvrait sur TOUT transfert de
plus de deux kilos : rentrer une benne au silo demandait deux appuis — l'action, puis
« valider » sur un curseur déjà poussé au maximum — pour un geste où il n'y a rien à
choisir. On ne dépose pas les trois quarts d'une benne dans la grille du silo, on la vide.
Le dosage ne survit que là où la quantité change ce qu'on emporte ou ce qu'on gagne : ce
qu'on **récupère** d'un stock — silo, entrepôt, étal, traite — parce qu'une caisse entamée
n'accepte plus d'autre nature ; ce qu'on **vend**, parce que l'étal a un plafond et qu'on
garde le reste pour le mieux-disant ; et les **bêtes qu'on embarque**, parce qu'on vient
parfois chercher une bête et pas tout l'enclos. Silo, entrepôt, auge et trémie d'usine
partent d'un appui : personne n'y est payé au kilo versé, et rien n'y est plafonné qu'on
puisse ménager — le curseur de la trémie d'usine mentait d'ailleurs, faute d'être borné
par la place restante.

**Et la trémie de la moissonneuse ne se demande même pas.** On arrive au silo avec neuf
cents kilos d'une seule céréale, le silo tient un tas de cette céréale-là, et il n'y a
rien d'autre à en faire : poser la question, c'était demander de confirmer la seule
réponse possible, à chaque tour de champ. La trémie se vide donc d'office dès que la
machine s'arrête sur la grille — sans bouton, sans colonne, sans rien. Le reste ne bouge
pas : une BENNE qui arrive au silo se voit bien demander lequel des cinq tas elle charge,
parce qu'elle a le choix.

**Ce qui est en cours se lit, il ne se clique plus.** La ligne portait un ⏹ qui arrêtait
le transfert : un bouton pour rien, puisqu'il suffit de repartir — la liste des actions se
tait dès que l'engin dépasse 2,5 m/s, et le transfert s'oublie de lui-même. La ligne reste,
elle dit ce qui se passe ; le bouton est parti.

Quand il s'ouvre, il est borné par le plus contraignant des deux — la benne ou le tas — et
la quantité choisie devient la limite du transfert, qui s'arrête pile dessus : le dernier
pas est raccourci exprès, sans quoi l'on chargeait 204 kg là où l'on en avait demandé 200.
Choisir le maximum ne pose aucune limite.

## Ce que l'écran donne à lire

Les trois tracteurs s'appellent **Tracteur**. « Vert », « Rouge », « Bleu » disaient leur
couleur là où l'écran la montre déjà : une pastille accompagne chaque nom, dans la liste
du parc comme sur la carte du plan. Le nom sert donc enfin à dire ce qu'est l'engin, et
la pastille correspond au modèle — celle du pick-up annonçait du rouge alors que sa
caisse est bleue depuis toujours.

Le bouton d'**automatisation** est descendu à côté du **garage** : ce sont les deux
boutons qui parlent de l'engin — lequel je pilote, et est-ce que je le pilote moi-même.
La rangée du dessus ne garde que ce qui touche à l'outil, l'attelage et le semoir.

**Les listes se resserrent.** Une ligne prenait 58 px de haut pour trois mots et un
bouton : quatre lignes par écran de téléphone, et l'on passait son temps à faire défiler.
Tout descend d'un cran — 11 px pour le nom, 9 pour le détail — et les rembourrages d'un
tiers ; le détail gagne en contraste pour compenser sa taille. La pastille devient un
filet de quatre pixels plutôt qu'un pavé de dix, et chaque titre de rayon est suivi d'un
filet horizontal : le groupe se voit avant d'être lu.

**Les bulles des commerces** calaient le nom à gauche et le prix à droite, chacun sans se
soucier de l'autre : « Aliment premium » et son tarif se chevauchaient. On mesure d'abord
le prix, on en déduit la place qui reste, et l'on rétrécit le nom jusqu'à ce qu'il tienne
— comme sur les enseignes et les jauges. Le prix, lui, prenait la couleur du toit du
commerce : un toit sombre le rendait illisible sur un fond déjà sombre. Il passe à un
blanc chaud, très clair, qui ressort sans crier.

## Le village

**Des quartiers, et une seule ligne de façades.** Le village n'avait ni l'un ni l'autre :
une usine entre deux boutiques, des maisons neuf mètres en retrait quand les dalles n'en
gardent que trois, et vingt-six objets de village semés au hasard des bords, qui
finissaient derrière les bâtiments. Trois règles maintenant.

Les **six usines sont rassemblées** sur la bande est — coopérative, atelier textile,
laiterie, usine céréales, usine avoine, garage — en trois paquets jointifs séparés de
bosquets. C'est le quartier industriel, et il ne contient que ça.

Les bandes ouest et nord sont **la rue du village** : maisons et commerces y ALTERNENT,
tous jointifs, sous une clôture commune. Relevé, bande par bande :
`M B B ~ B M B ~ B` à l'ouest, `B M B ~ M B M ~ B M` au nord, `U U ~ U U ~ U U` à l'est.
Une seule jointure commerce-contre-commerce dans tout le village, à l'ouest : cette bande
porte cinq dalles dont le supermarché, et depuis que le bâti est à l'échelle des engins
elle ne tient plus que deux maisons. On la place entre la brasserie et le caviste, les
deux plus petites — trente-neuf mètres de devanture d'un tenant — plutôt qu'entre le
marché et le supermarché, qui en feraient cinquante-deux. Partout ailleurs c'est une
maison qui s'intercale.

Une **maison est au recul de la dalle voisine**, trois mètres, et pas un de plus — sans
quoi on ne peut pas la coller à son voisin, et la rue a deux lignes de façades au lieu
d'une. Son mur se retrouve en avant de celui du commerce, ce qui est juste : le commerce
met dix mètres de parvis derrière sa clôture, la maison son jardin de devant.

Un **objet de village ne se pose que dans un creux**, avec les arbres, et il se CHOISIT à
la taille du creux : on prend le plus gros des dix modèles qui y tienne, un mètre de jeu
compris, et l'on ne réserve que son encombrement déclaré. Il fallait sept mètres pour
recevoir quoi que ce soit et l'objet réservait ensuite huit mètres quelle que soit sa
taille — un banc de 4,65 m comme un lavoir de 5,60 : les creux ayant rétréci, deux sur
quatre auraient perdu leur objet en silence. Chaque modèle est rayé de la liste une fois
posé, si bien que quatre creux donnent quatre objets différents.

**Une maison qui n'a personne à qui se coller garde sa propre barrière.** Le pan mitoyen
n'appartient qu'à un seul des deux voisins : entre deux maisons à la première, entre une
maison et un commerce au commerce — sa clôture court sur toute la profondeur de sa dalle,
là où le lot d'une maison n'en fait que quinze mètres. Encore faut-il que le voisin ferme
pour de bon : cinq commerces sont déclarés `cloture:'trottoir'` et ne posent qu'une
bordure de vingt-six centimètres. La maison s'effaçait quand même, et celle qui est prise
entre le marché et le supermarché n'avait AUCUN de ses deux flancs fermé.

Et surtout, `panCloture()` **jetait en silence tout pan décrit à l'envers** : sa longueur
partait négative et la fonction sortait sans poser un piquet, sans une erreur. Or les deux
mitoyennes de toute maison de bande étaient décrites du fond vers la route, et sur les
bandes ouest et nord on s'éloigne du bitume dans le sens décroissant. Pas une des sept
maisons n'avait jamais eu de clôture latérale à elle. Relevé : **118,83 m de jardin sans
barrière, ramenés à 0,00**.

**Un village se fait par paquets, pas par un peigne.** Les quinze commerces étaient
répartis sur leur bande en divisant le jeu restant en parts égales : 8,97 m entre chaque
dalle à l'ouest, 20,13 à l'est, 31,76 au nord — la même valeur répétée d'un bout à
l'autre, quinze bâtiments à la parade. `BANDES` écrit maintenant l'ORDRE et la NATURE
de chaque bloc : deux ou trois usines **collées bord à bord**, clôture commune ; un vrai
creux planté d'arbres, de buissons et de rochers ; les commerces de bouche encadrés de
maisons ; et de loin en loin un creux plus court où un abri de bus ou un lavoir se pose
sur l'herbe, à cinq mètres du bitume. Les largeurs ne sont pas écrites — ce sont les
cotes mesurées des bâtiments et des lots — et le jeu restant se partage entre les creux
seuls, au prorata. Relevé : **huit dalles jointives** à zéro centimètre.

**Mais un creux a une largeur maximale.** Tout le mou de la bande allait aux creux et rien
qu'aux creux : la bande nord, la moins chargée des trois, leur donnait 18,6 et 16,8 m —
soit 22,6 et 20,8 m d'un bord de dalle au bord de dalle suivant une fois les deux jeux
comptés. Ce n'est plus le creux d'un village, c'est un terrain vague entre deux hameaux.
La bande ouest, elle, est pleine et n'en lâche que 8,4 : c'est ce chiffre-là qui fait une
rue, et on le prend pour plafond (`CREUX_MAX = 8,5`). Ce que le plafond refuse ne va
surtout pas dans les marges — dans nos trois plans chaque marge borde un creux, l'y verser
rouvrirait exactement l'écart qu'on vient de fermer — mais RECULE LES DEUX BOUTS de la
bande, où il se confond avec le recul qu'elle garde déjà sur la rocade perpendiculaire :
un abord de carrefour dégagé se lit comme un abord de carrefour, là où le même vide entre
deux boutiques se lit comme un bâtiment manquant. Relevé, une fois le bâti à l'échelle :
le plus grand écart d'un bord de dalle au suivant tombe de **22,62 à 12,50 m**.

Le pan mitoyen n'est posé qu'une fois : il appartient au premier des deux voisins le
long de la bande, sinon deux murets se superposent au centimètre près. Et l'ordre du
tableau `SITES` ne bouge pas d'un cran — une sauvegarde y repère un commerce par son
indice ; on ne change que `bat`, l'ancrage le long de la bande.

Les maisons de bande suivent la même mécanique que le rang du bord sud : `lotMaison()`
bâtit, met à l'échelle et mesure ; `poserLotBande()` pose. Les quatre bandes ne diffèrent
que par l'axe le long duquel elles courent et le sens dans lequel on s'éloigne de la
chaussée — d'où deux petites tables plutôt que quatre branches de code. La rotation des
modèles court sur tout le village : une maison de bande et sa voisine de rang ne sont
jamais le même modèle.

Trois silhouettes de maison se répétaient en enfilade le long de la façade sud — et en
vérité elles n'étaient même pas construites : le code qui les dessinait n'était appelé
de nulle part, il réservait la place sans rien y poser. **Dix maisons prises dans six
modèles** forment maintenant une rue : chaumière au toit débordant, maison de pierre à
volets bleus, chalet à balcon, maison de bourg étroite, longère à appentis, maison à
colombages. Chacune apporte son portillon, son allée et ses abords.

**À l'échelle des commerces.** Les six modèles venaient d'une planche dessinée pour
elle-même : porte de 2,20 m, corps de 6,40 × 5,07 m, quand la boutique d'en face porte
une porte de 2,65 m sur un corps de 8,25 × 6,43. Deux échelles dans le même village, et
la maison faisait maquette contre le commerce. Le facteur n'a pas été choisi mais
relevé — rapport des emprises bâties 1,28, rapport des largeurs de porte 1,37, rapport
des hauteurs de mur 1,02 : les trois se rejoignent à **1,30**. Une maison couvre alors
86 % de l'aire au sol d'une boutique et monte 26 % plus haut, ce qui est exactement ce
qu'on veut d'un toit pentu devant un commerce de plain-pied.

**Et tout le bâti à l'échelle des engins.** 1,30 est un RAPPORT, pas une cote : le jeu
s'était mis à avoir deux mètres au lieu d'un. Les engins ont été agrandis deux fois et à
la main — le pick-up de 1,38, le fourgon de 1,40 — et le tracteur lui-même, mesuré contre
le vrai, sort à 1,136 en longueur, 1,376 en largeur, 1,466 au toit et 1,594 au gyrophare :
moyenne géométrique 1,383. Le monde roulant est bâti à 1,38 ; les bâtiments étaient restés
à 1,00. Relevés de la même façon, ils demandaient 1,216 (commerces) et 1,138 (maisons),
soit **`BAT_ECHELLE = 1,18`** pour les deux — ce qui laisse le rapport maison/commerce
intact à 1,30. La preuve ne demande aucune référence extérieure : la grande porte de
l'entrepôt de la ferme montait à 4,61 m sous linteau pour un tracteur de 5,18 m hors-tout,
et la porte roulante du garage du village — là où l'on ACHÈTE les tracteurs — à 4,08 m. Ni
la remise ni le magasin ne laissaient entrer leur propre machine. Elles passent à 5,44 et
5,78 m. L'échelle est posée AVANT la mesure du modèle : la dalle, la clôture, le parvis,
le quai, l'anneau et l'emprise de collision s'en déduisent tous et suivent d'un coup.

Le prix est payé sur la **bande ouest**, la plus chargée des trois : elle demandait 177,4 m
pour 172,3 disponibles, et rien ne l'aurait dit — `repartirBandes()` borne le reste à zéro,
si bien que la dalle de la boucherie serait simplement allée finir deux mètres sur le
bitume. Elle perd donc une maison sur trois. Un budget de bande négatif se partage
désormais entre les DEUX bouts au lieu de crever par le bas.

**Au bord de la route.** Elles étaient semées sur les trois bords extérieurs, à dix ou
vingt mètres derrière les chaussées, et **trois d'entre elles tombaient dans la dalle
d'un commerce** — quatre dalles en tout, l'une des trois chevauchant deux voisins :
les bandes ouest et nord sont pleines du bitume jusqu'au bord de
carte, il ne reste derrière les dalles que trois à cinq mètres. Le brin sud de la rocade
est le seul bord de route encore libre, et il l'est sur toute sa longueur. Les maisons
s'y alignent, façades tournées vers la chaussée.

**Combien de maisons ? Autant qu'il en tient.** Le nombre n'est pas écrit : les quatre
brins de la rocade **courent d'un bord du monde à l'autre** — ils ne s'arrêtent pas aux
angles, c'est ce qui leur donne l'air d'une route de passage — et le bitume des brins
ouest et est passe donc au droit du rang, pour tout `z`. Le rang doit leur laisser la
même verge qu'à la chaussée de devant. On empile donc les lots tant qu'ils tiennent
entre les deux chaussées latérales, verge comprise, une fois l'écart déduit : huit, et la
neuvième (18,1 m) ne rentre plus. Relevé : 5,31 m de verge à l'ouest comme à l'est. Sans
cette borne, les deux pignons tombaient à **34 cm** de l'asphalte.

**Et un écart au milieu.** Huit maisons collées sur cent cinquante-sept mètres, cela se lit
comme un mur depuis la chaussée, et le village n'a nulle part où poser un calvaire. Dix
mètres s'ouvrent donc au milieu du rang — le nombre est relevé, pas choisi : il faut qu'un
engin puisse passer À CÔTÉ de ce qu'on y met, et la collision ajoute 1,35 m de demi-machine
au rayon de l'obstacle. La mitoyenne coupée est celle dont l'écart tombe le plus près du
milieu, à l'exclusion de celle qui mettrait deux fois le même modèle en vis-à-vis. Le rang
n'est alors plus d'un seul tenant : sa clôture ferme chaque tronçon par son propre pignon
est, et son rectangle d'obstacle devient DEUX rectangles — un seul reboucherait l'écart
pour les engins et en ferait un mur invisible de dix mètres. Relevé : 1,80 m de couloir
franchissable, 432 sommets de clôture sur chacun des deux jambages. Dedans : un calvaire,
un banc et un puits, trois des dix modèles de mobilier que le village ne montrait nulle
part.

**Mitoyennes, et clôturées en commun.** Chaque maison avait sa clôture, et deux voisines
en dressaient donc deux, parallèles, avec entre elles une bande d'herbe qui n'était le
jardin de personne. Les lots sont maintenant **jointifs** — bord contre bord, écart nul
aux neuf jonctions — et la clôture est **une seule** : un devant qui court sur 155 m et
s'ouvre d'un portillon devant chaque allée, un fond, deux pignons, et une mitoyenne à
chaque bord de lot interne. Le pas des piquets reste celui de `dJardin()` — chaque
tronçon entre deux points fixes divise sa propre longueur en parts égales, d'où 1,33 à
1,95 m d'écart. Une trame unique ancrée sur le rang a été essayée pour lisser ce
rythme : elle l'a empiré (217 % d'écart au lieu de 46), parce que les bords de lot ne
tombent pas sur la trame et qu'un piquet venait s'y coller à 78 cm d'un piquet d'angle.
Une clôture rurale n'a pas de trame.

Commune, mais **pas un seul objet**. Fusionnée d'un tenant, elle faisait un maillage de
177 m dont la sphère englobante mesurait 89 m de rayon : le tronc de vue ne l'écartait
plus jamais, et ses triangles partaient au GPU même en lui tournant le dos. La
mitoyenneté est donc dans le **découpage** — chaque lot porte sa part du devant, sa part
du fond et la clôture de son bord gauche, le dernier fermant le rang par son pignon est —
et chaque lot fusionne la sienne : dix maillages de 13,5 m de rayon. Face au rang,
14 178 → **10 194 triangles** pour deux appels de dessin de plus ; dos au rang,
8 136 → **7 516**. Et les bouts de pan sont partagés : deux pans qui se rejoignent
poseraient chacun leur poteau au même point, quatre volumes exactement superposés aux
quatre coins.

Aucune cote n'est écrite : chaque modèle **déclare** son lot dans `dJardin()` — largeur,
profondeur, décalage, axe de l'allée — et le rang met ces cotes bout à bout, centrées sur
le brin sud. Le drapeau `jardinsPoses` est ce qui distingue les deux emplois : dans le
rang, `dJardin()` note la cote et ne pose rien ; hors du rang, une maison garde sa
clôture à elle. L'allée, elle, est prolongée jusqu'au portillon que le rang vient de
percer — sinon elle s'arrêterait dans l'herbe à un mètre de la barrière.

**Et le rang n'est pas sur la route.** Il se tenait à `RECUL_ROCADE`, les trois mètres de
verge des commerces — mais un commerce met dix mètres de **parvis** entre sa dalle et sa
façade, quand une maison n'a que son jardin de devant : vue de la chaussée, la clôture
tombait au ras du bitume. `RUE_VERGE` vaut neuf mètres, ce qui met les **murs** de
façade des maisons à 12,64–13,16 m du bitume, contre 13 pour ceux des commerces — la
même ligne. (L'avant-toit, lui, avance de quarante centimètres devant son mur : 12,2 à
12,9 m. Deux lignes, à ne pas confondre.) Ce qui arrête l'engin est **un seul
rectangle** pour tout le rang, élargi de la demi-section d'un poteau : les lots étant
jointifs, il n'y a plus rien à traverser entre deux maisons — on fait le tour par les
bouts, avec 6,0 m de marge à l'ouest et 2,1 m à l'est.

**La verge est une rue, pas une pelouse.** Neuf mètres de large sur cent cinquante-quatre
de long, interdits à la verdure par le filtre du semis : il en restait une bande d'herbe
rase, vide et garantie vide, devant tout le village. Le mobilier qui a sa place au bord
d'une route s'y installe — abri de bus, banc, calvaire, puits — aux bornes de lot,
c'est-à-dire à mi-chemin de deux portillons ; et sept lampadaires côté village, décalés
d'une demi-portée pour alterner avec ceux d'en face, éclairent une route dont les mâts
étaient tous du côté de la ferme et s'effaçaient devant sa cour. Le rang faisait un aplat
noir à la nuit tombée.

**L'ordre des maisons n'est plus celui de la table.** Pris à la file — 0, 1, 2, 3, 4, 5,
0, 1, 2, 3 — la moitié est du rang était le calque exact de la moitié ouest : six modèles
pour dix lots, et le regard fait le rapprochement d'un coup d'œil. `MAI_ORDRE` passe les
six une fois puis les reprend autrement.

**Et plus rien n'est planté sur le bitume.** Le rang a révélé un défaut bien plus vieux
que lui : `surRoute()` bornait chaque brin à l'anneau — un point n'était « sur la route »
que s'il tombait *aussi* entre les deux brins perpendiculaires — alors que le sol peint
quatre bandes qui **courent d'un bord du monde à l'autre**, dont les quatre bouts
dépassent des angles. Douze arbres, buissons et rochers poussaient donc en plein sur
l'asphalte, et trois houppiers la surplombaient. Sans les deux gardes, le test est plus
court et il est juste : **zéro**, et zéro houppier.

**Vingt-six petits objets** se sèment entre elles : abri de bus, tonnelle, lavoir, table
de pique-nique, bûcher, puits, calvaire, entrée de village, banc de place, poteau
télégraphique. L'épouvantail et le muret de pierre sèche sont écartés — le premier
appartient au champ et non au village, le second ferait doublon avec les clôtures.

Chaque bloc est **fusionné en une seule géométrie** avant d'entrer dans la scène :
soixante à cent primitives deviennent un objet, donc un appel de dessin. C'est ce qui
permet d'en poser cinquante sans que la carte s'alourdisse — 31 700 triangles pour
l'ensemble, et pas un obstacle sur une route. Agrandir les maisons ne coûte rien : une
échelle ne crée pas de géométrie.

## Le pilote automatique

**L'escargot est strictement orthogonal.** Il ne l'était pas : le tour se refermait sur
son coin de départ, puis le suivant commençait au coin rentré d'une passe — un saut en
diagonale à chaque tour, **32 segments obliques** et jusqu'à 17 m de biais par parcelle.
On resserre maintenant UN bord à la fois, juste après l'avoir longé, et le resserrage est
bridé au milieu : sans cette butée le rectangle se retournait et il restait au centre une
bande que les deux passes opposées, trop écartées, n'avaient pas jointe. Le cœur, lui, se
fait en lignes droites plutôt qu'en un dernier tour : un outil traîné quatre à six mètres
derrière ne suit pas un chapelet de virages. Mesuré sur cinq outils × quatre tailles de
parcelle : **0 oblique, 100 % du tracé sur la terre, 0 cellule oubliée**.

**Le tour suivant mord sur le précédent, et le premier sort de la parcelle.** Deux
passes espacées d'une largeur d'outil se touchent en théorie et se manquent en pratique :
l'outil est traîné quatre à six mètres derrière le tracteur, il coupe donc les virages, et
c'est dans les angles que restaient des coins jamais travaillés. Le recouvrement passe
d'un huitième à un quart. Et la marge tenait le TRACTEUR à l'intérieur, pas l'outil : une
charrue de trois mètres voyait sa bordure extérieure tomber pile sur la limite, et
quelques centimètres de dérive suffisaient à ce que la dernière rangée ne soit jamais
retournée. Le premier tour — celui qui longe les quatre bords — sort donc de la parcelle,
sur la bande de sable de 6,40 m qui la sépare de sa voisine. Les deux chiffres sont
mesurés et non choisis — le paysage n'est pas lisse.

**Le débord s'est raccourci, le recouvrement s'est resserré.** Quatre-vingt-dix
centimètres dehors, c'était le tracteur — 2,70 m de large — posé pour un tiers sur la
bande de sable, et l'on voyait le premier tour se faire hors du champ : **40 cm**
suffisent à ce que la bordure de l'outil couvre la dernière rangée de cellules. Et il
restait des morceaux de terre entre deux passes, là où l'outil traîné dérive vers
l'intérieur du virage sur les premiers mètres : le pas descend de **0,74 à 0,66** largeur
d'outil. Relevé sur les seize cas du banc — 0,60 et 0,70 font moins bien, 86,4 % et 86,0 %
au pire.

**Une passe finie se vérifie, et se termine dehors.** Le tracé épuisé, le pilote regarde
ce qui n'a pas été travaillé et y renvoie l'engin — jusqu'à trois fois, et l'on s'arrête
dès qu'un passage n'a plus rien rattrapé. Le rattrapage ne refait pas la parcelle : il
trace des LIGNES DROITES sur l'emprise de ce qui reste, et les fait dépasser franchement
de part et d'autre, de sorte que les demi-tours — seul endroit où l'outil ne suit pas le
tracé — se prennent EN DEHORS de ce qu'il faut rattraper. Un escargot resserré sur les
trous avait été essayé : il faisait moins bien, parce qu'il virait précisément là où il
fallait travailler.

Ce qui reste ne se lit d'ailleurs pas dans `from` : la charrue accepte la terre labourée
et l'épandeur sort du semé pour rendre du semé — leur reste ne diminuerait jamais et la
vérification tournerait en rond. On regarde donc ce que l'outil LAISSE DERRIÈRE LUI :
l'état de sortie pour les trois outils qui en changent, la marque d'engrais pour celui
qui n'en change pas.

Puis l'engin **ressort de la parcelle** : il s'arrêtait net sur le bord, à cheval sur la
dernière rangée qu'il venait de travailler. Un point de sortie est ajouté quatre mètres
au-delà de la limite, dans le sens où l'on roulait — un point posé sur le bord le plus
proche ferait finir par un quart de tour à l'arrêt. Il se choisit LIBRE : le décor pousse
entre les parcelles, et une sortie posée sur un arbre, c'est une machine qui finit son
champ le nez contre un tronc ; cinq sorties sont essayées, on prend la première dont le
trajet ne rencontre rien. Et ce point-là se valide sur la position de la MACHINE et non de
l'outil, contrairement à tous les autres : la moissonneuse porte sa coupe DEVANT, et
s'arrêtait le nez encore dans le blé.

**Un point qu'on n'atteint pas ne retient plus la machine toute la nuit.** Un plan est
tracé à la règle, sans rien savoir de ce qui pousse entre deux parcelles : un arbre, un
rocher, une clôture peuvent tomber sur un point de passage, et l'engin poussait alors
contre l'obstacle indéfiniment, plan gelé — mesuré, quatre cents secondes de jeu sans
avancer d'un point, sur trois des seize cas du banc. Si la distance au point visé ne
descend plus pendant huit secondes, on l'abandonne ; le rattrapage de fin de passe
retrouvera ce qui n'a pas été fait là.

Relevé sur les seize cas du banc, machine pilotée image par image et marquage du sol
actif : la couverture du pire cas passe de **88,9 % à 96,2 %**, la moyenne de 93,6 à
**99,0 %**, les cellules jamais touchées de **370 à 49**, les passes qui se terminent
d'elles-mêmes de **13 sur 16 à 16 sur 16** — et le tout en un tiers de temps de moins,
parce que plus rien ne reste coincé. La distance au plus proche obstacle ne bouge pas :
1,50 m.

**On ressort d'une impasse en marche arrière.** Un point de dépose est au fond d'un
cul-de-sac : dix mètres de parvis entre la façade et le bitume, ou la grille du silo au
pied de sa tour. Repartir en pivotant sur place y demande un demi-tour plus large que
l'impasse — et la moissonneuse allait chercher la tour du silo, s'y plantait pleins gaz
et n'en repartait jamais. Elle ressort maintenant par où elle est entrée : l'itinéraire
retient le COUDE de son dernier trajet, celui où il quitte la chaussée à l'équerre, et
l'engin y recule — vraie marche arrière, gaz négatifs, braquage inversé par le train
arrière comme sur un vrai engin. Il recule même huit mètres AU-DELÀ du coude, et c'est ce
qui évite le demi-tour : le coude repasse alors devant lui, il repart en marche avant sans
jamais se retourner à côté du bâtiment. Relevé au silo, le passage le plus serré du jeu :
la distance à la tour passe de **1,35 m — c'est-à-dire collé dessus — à 3,44 m**.

**Un point de passage se valide quand on l'a DÉPASSÉ, et c'est l'outil qui doit l'avoir
dépassé.** Deux défauts d'un coup. Un attelage tourne sur un rayon de 3,5 m et le point
se validait à 2 : la charrue arrivait sur un coin, le manquait, et tournait autour
indéfiniment — bloquée au point 3 sur 17 pendant six mille images. Et valider sur la
position du tracteur, c'est amorcer le virage alors que l'outil n'y est pas encore : il
coupe l'angle. La couverture réelle, machine pilotée image par image, passe de **37 % au
pire à 84–98 %**.

Deux autres réglages, chacun mesuré : la marge qui tient le tracteur dans la parcelle
vaut une demi-largeur d'outil et 1,80 m au plus, au lieu d'une demi-passe — un épandeur
de 12 m se retrouvait à tracer un carré de 8 m au milieu d'un champ de 19 ; et le
marquage n'est plus coupé sous 0,60 m/s mais sous 0,05, si bien qu'un virage appuyé
travaille le sol au lieu de le sauter.

**Et pour aller quelque part, on roule sur la voie.** Le dernier trajet doit tomber
perpendiculairement sur le point jaune, et la voie qui le dessert est celle dont il est
le plus proche — on choisissait la voie la plus proche du DÉPART, si bien que le dernier
trajet se faisait toujours en z : la bonne perpendiculaire pour les quatre commerces de
la bande nord, et un abordage par le travers pour les onze autres. Un commerce se dessert
par la rocade et jamais par un chemin de sable, qui s'arrête à la ferme. Et le raccourci
en ligne droite passe de 18 m à 8 — la longueur d'un attelage, de quoi finir de se
ranger, pas de quoi couper. Relevé sur 45 trajets : **0 oblique, 0 abordé de travers,
12,6 m pour le plus long des derniers trajets**.

## Trois âges par culture

Une culture n'avait qu'**une** silhouette : celle de la plante mûre, rapetissée à mesure
qu'on remontait dans le temps. Un blé qui vient de lever était donc un épi mûr de vingt
centimètres de haut, barbes comprises. La croissance ne se lisait qu'à la taille et à la
couleur — jamais à la **forme**.

Chaque culture a maintenant plusieurs états **physiques**, et l'on passe de l'un à
l'autre en changeant de géométrie :

| | |
|---|---|
| **Pousse** | deux brins sortis de terre. Commun aux cinq céréales — une levée ne se reconnaît pas d'une espèce à l'autre |
| **Montée** | une tige montée, trois feuilles, rien au bout. Commune elle aussi |
| **Adulte** | là seulement l'espèce paraît : l'épi du blé, les barbes de l'orge, la panicule lâche de l'avoine, les grappes du colza, la feuille arquée du maïs |

Les deux permanentes en ont **quatre**, parce qu'elles vivent plus longtemps que leur
récolte : jeune plant, charpente montée, adulte en feuilles, adulte en fruits. Une vigne
vendangée ne redevient pas un bouton de bois — elle repart de l'état « en feuilles », qui
est exactement ce qu'elle est une fois la vendange faite. C'est le drapeau `replante`,
celui-là même qui lui donne sa repousse plus courte, qui le dit.

**Deux briques, et rien d'autre**, reprises de la planche du joueur : le **brin**, fût à
trois pans ouvert et évasé (6 triangles) — tiges, feuilles, barbes, grains, épillets ; et
la **touffe**, deux cônes à six pans dos à dos (12 triangles) — tout le feuillage des
vignes et des oliviers, qui se lit comme une masse arrondie là où un tronc de cône donnait
un abat-jour.

**Et c'est moins cher qu'avant.** Un pied de blé qui lève coûte 12 triangles au lieu de
36, un pied monté 24 : une parcelle passe les deux tiers de son cycle sous le prix qu'elle
payait en permanence.

| | pousse | montée | adulte | en fruits | avant |
|---|---|---|---|---|---|
| Blé | 12 | 24 | 54 | — | 36 |
| Maïs | 12 | 24 | 36 | — | 42 |
| Colza | 12 | 24 | 60 | — | 48 |
| Avoine | 12 | 24 | 72 | — | 48 |
| Orge | 12 | 24 | 72 | — | 72 |
| Raisin | 54 | 84 | 120 | 138 | 136 |
| Olives | 36 | 66 | 156 | 186 | 208 |

**La talle, pas la tige.** La planche sème quatre-vingt-dix pieds au mètre carré et peut
se permettre des épis de treize centimètres ; le jeu ne pose qu'une instance par cellule
de 1,30 m. Relevé au premier essai : la terre se voyait entre les tiges là où le champ
formait un tapis fermé. Chaque céréale est donc une **touffe de trois talles** écartées —
la silhouette de la planche, répétée — et l'épi est grossi de moitié : la densité du jeu,
sans un triangle de plus.

**Les cotes du jeu sont tenues au centimètre.** La planche dessine une vigne d'1,75 m sans
fil de palissage : transposée telle quelle, elle repasserait sous l'enjambeuse sans qu'on
voie ce qu'on récolte — la régression déjà corrigée une fois — et les rangs cesseraient de
se rejoindre. Le vocabulaire de la planche est donc repris, mais écrit **en mètres** à la
cote du jeu : piquet à 3,21 m, fil de 1,40 m pour une cellule de 1,30. Les sept hauteurs
mûres sont inchangées à deux centimètres près, l'olivier reste sous la poutre de
l'enjambeuse (4,60 m pour 4,75) et aucune céréale ne dépasse la moissonneuse.

**Le raccord d'un âge au suivant ne se voit pas.** Trois géométries de hauteurs
différentes, chacune montant de son échelle de départ à 1, feraient sauter le champ d'un
tiers à chaque palier. L'échelle de départ de chaque âge est donc calculée pour que sa
hauteur au départ soit celle de l'âge précédent à son arrivée. Mesuré d'un millième avant
et d'un millième après chaque borne, sur les sept cultures : **le pire écart est de 2 %.**
Le piquet d'une vigne, lui, ne grandit jamais — un palissage se plante d'un coup, et le
faire monter avec le cep ferait onduler le rang entier.

**Un maillage par culture, par âge et par parcelle.** Un maillage instancié ne porte
qu'une géométrie : le tampon est donc indexé par `culture × 4 + âge`. Une parcelle n'en
paie jamais plus d'un ou deux à la fois — ses pieds sont semés d'un même passage, donc ils
franchissent leurs paliers presque ensemble — et le tampon d'un âge qui se vide est rendu
au pilote graphique. Les deux premiers âges des cinq céréales sont **littéralement** la
même géométrie, bâtie une fois et partagée.

**Et les tampons d'instances grandissent au besoin.** Chacun des sept maillages réservait
9 500 instances, soit **4,82 Mio** pour les sept, alors que la somme de leurs comptes ne
peut jamais dépasser 9 500 : une cellule ne porte qu'une culture. Une ferme qui sème deux
céréales payait cinq maillages vides plein tarif. Ils démarrent maintenant à 512 et
doublent quand il le faut : **0,26 Mio** sur une partie fraîche, 0,91 Mio sur une ferme
entièrement semée.

## Le zoom, et ce qu'il apprend

La caméra tenait sur un décalage fixe : trente-huit mètres de côté, soixante-deux de haut,
soit **82 m** de recul pour un champ de trente degrés. Un seul cadrage pour tout le monde,
alors que la bonne distance n'est pas la même selon qu'on conduit dans un champ ou qu'on
organise une tournée dans le village.

Une **barre de pourcentage** dans Réglages › Image le règle de 55 à 160 %. Cent, c'est le
cadrage d'origine au mètre près. Le décalage est simplement divisé par le rapport, ce qui
garde l'**angle** de vue identique : c'est un recul, pas un changement d'objectif, et la
ferme garde sa perspective isométrique. Le brouillard et le plan lointain reculent avec
lui, sans quoi zoomer arrière donnerait un monde qui se dissout. Le réglage se sauvegarde
en champ facultatif — une partie d'avant repart à 100 %.

| zoom | recul | largeur vue au sol | parcelles envoyées au rendu |
|---|---|---|---|
| 160 % | 51 m | 43 m | 7 / 20 |
| **100 %** | **82 m** | **69 m** | **9 / 20** |
| **75 %** | **109 m** | **93 m** | **12 / 20** |
| 55 % | 149 m | 126 m | 13 / 20 |

(La dernière colonne est le test d'écartement par parcelle, celui qui décide vraiment ce
qui part au processeur graphique : il retient une parcelle dès qu'elle mord le cadre.)

### Le test à 75 % : ce ne sont pas les véhicules qui coûtent

La question était de savoir si l'on peut alléger le détail des engins quand on s'éloigne.
Mesuré, ferme entière plantée, caméra au milieu des champs :

| | 100 % | 75 % |
|---|---|---|
| Triangles à l'image | 235 100 | 309 100 |
| — dont **cultures** | 234 162 (**99,6 %**) | 305 136 (**98,7 %**) |
| — dont décor | 924 | 3 930 |
| Appels de dessin | 92 | 116 |
| Maillages de champ visibles | 9 | 12 |
| Temps par image (rendu logiciel) | 141 ms | 182 ms (**+29 %**) |
| L'engin à l'écran | 354 × 324 px | 265 × 245 px |

**Le parc entier — sept engins et quatre outils — pèse 10 458 triangles**, et l'on n'en
voit jamais qu'un à la fois avec son outil, soit environ **1 600 triangles : 0,7 % d'une
image**. Simplifier les véhicules à distance ne rendrait donc rien de mesurable ; et à
75 % l'engin occupe encore 265 px de large, c'est-à-dire qu'on verrait très bien la perte.

Le vrai levier est ailleurs, et le zoom le montre : **ce qui coûte, c'est le nombre de
parcelles à l'écran.** Reculer d'un tiers en ajoute cinq, et 70 000 triangles de cultures.
La bonne réponse serait un niveau de détail sur les **plantes**, pas sur les engins — et
les trois âges viennent justement de doter chaque culture d'une silhouette à 24 triangles
à côté de sa silhouette à 72. Une parcelle éloignée pourrait dessiner la première. Ce
n'est pas fait : cela touche au rendu de ce qu'on regarde, et se propose avant de se
décider.

## Le décor est tiré au sort, mais toujours le même

Arbres, buissons, rochers, touffes d'herbe, fleurs des ruchers, taches de terre : tout
cela était semé avec `Math.random()`, donc redessiné autrement à chaque lancement. Un
joueur qui reprenait sa partie ne reconnaissait pas sa vallée. Relevé sur la version
d'avant : **294 objets fixes changeaient de place entre deux ouvertures**, dont les
cent trente arbres, et le sol peint avec eux.

Deux générateurs, et plus un seul `Math.random()` dans la construction du monde.

`alea()` est un **flux global**, semé sur une graine fixe. La construction initiale se
fait toujours dans le même ordre, donc il rend toujours la même suite, donc le monde est
toujours le même. **Changer `GRAINE` change toute la vallée d'un coup** : c'est le
bouton à tourner quand un décor ne plaît pas, et il n'y en a qu'un.

`aleaLieu(x, z)` rend un flux **propre à un endroit**. Il sert à tout ce qui se construit
en cours de partie — une parcelle achetée au bout d'une heure, un rucher posé après coup
— car ceux-là ne peuvent pas dépendre de l'endroit où en est le flux global. Le même
point rend toujours la même suite, quel que soit le moment : une parcelle achetée à la
première minute ou à la trentième porte exactement les mêmes pieds.

Ce qui est **passager** garde `Math.random()` : la fumée, la poussière, les oiseaux, les
traces d'outil, l'allure d'une bête qu'on vient d'acheter. On ne veut surtout pas qu'une
bouffée de fumée soit identique d'une partie à l'autre — et rien de cela n'est du décor.

Rien de tout ceci n'est recalculé en cours de partie : le décor se construit une fois au
chargement. Ce qui change, c'est qu'il se construit **à l'identique**.

## Ce qui tient la fluidité

Quatre plafonds, chacun posé après mesure, chacun tenu par un contrôle qui échoue si on
les retire.

**Les cultures ne partent au GPU que si on les regarde.** C'est le plus gros des trois,
et il tenait à une ligne : les sept maillages de culture portaient `frustumCulled = false`.
Ils n'avaient pas le choix — un maillage instancié couvrant la ferme entière est toujours
à l'écran, et three teste la sphère de la GÉOMÉTRIE, celle d'un seul pied posé à l'origine.
Résultat : tout planté en orge, **612 000 triangles partaient au nuanceur de sommets à
chaque image**, où que la caméra regarde, alors que quatre parcelles sur vingt sont dans
le champ de vision.

Chaque culture se découpe donc **par parcelle** : un maillage par couple (parcelle,
culture), bâti au premier pied qu'on y plante, et vingt tests de sphère par image
décident lesquels se dessinent. Le rectangle d'une parcelle ne bouge jamais, donc sa
sphère ne peut pas être périmée — c'est ce qui rend l'écartement sûr, là où la sphère
d'un maillage instancié ment toujours. Relevé sur cent poses de caméra balayant tout le
terrain : **23,1 % des plantes envoyées en moyenne** (61,7 % au pire cadrage, à la
jonction de quatre parcelles), **0 parcelle perdue** — celle dont un coin est à l'écran
est toujours dessinée. Sur la vue de jeu, l'orge tombe de 618 824 à 151 904 triangles
pour quatre appels de dessin de plus sur les 283 que fait déjà la scène.

Et un maillage vide **rend ses tampons** : une parcelle qui change de culture libère
l'ancienne au lieu de la garder à sa taille. Après avoir semé les sept cultures partout,
les réserves d'instances passent de **4,07 Mio à 0,09** ; sur une ferme entièrement semée
d'une seule culture, de 0,91 à 0,62. Un maillage qu'on ne dessine pas ne renvoie rien non
plus, et sa plage s'accumule au lieu de s'écraser : elle part d'un bloc quand la caméra
revient.

**La plage renvoyée est un min-max.** Chaque culture est un maillage instancié, et l'on ne
renvoie au GPU que la plage qui a bougé. Mais cette plage est un simple min-max : il
suffit que deux plantes éloignées franchissent un palier de croissance dans la même
image pour qu'elle s'étale d'un bout à l'autre du maillage, et l'on renvoie alors le
tampon entier — 594 Kio de matrices plus 36 Kio de couleurs, à multiplier par le nombre
de cultures qui poussent. Sur une ferme semée d'un coup, c'est exactement ce qui arrive :
tous les pieds franchissent leur palier ensemble. Relevé sur vingt secondes de pousse,
avant : cinq images à 630 Kio d'un bloc. On plafonne donc à mille instances par image,
toutes cultures confondues, et le reliquat part à l'image suivante — le tableau côté
processeur fait foi, une instance renvoyée deux images plus tard porte la même matrice.
Après : trente-trois images à 74 Kio. Un palier qui met cent millisecondes de plus à
paraître ne se voit pas ; il en met trois mille à venir.

L'émission se fait en **un seul endroit, une fois par image**, juste avant le rendu.
three ne lit `updateRange` qu'au rendu : appeler deux fois dans la même image — ce que
faisaient `work()` puis `grow()` — écrasait la première plage par la seconde, et ces
instances-là ne partaient jamais.

**La bande passante des tuiles du sol.** Les tuiles font 27,5 m sur 320 px, et
`flushTiles` n'en réveille que deux par image : 0,78 Mio au pire, contre 3,13 avant
qu'elles soient coupées en quatre.

**La mémoire des textures.** C'est le poste qui étrangle un téléphone : au-delà de
quelques centaines de mégaoctets, le navigateur évince des textures et les recharge en
boucle — le jeu tombe alors à une image par seconde pendant plusieurs secondes. Les
bulles de prix des seize commerces étaient dessinées en double définition « pour la
netteté » : 1280 px de large pour une bulle qui en mesure deux cents à l'écran, soit
trente-six fois trop de pixels, et 59 Mio à elles seules. À définition simple elles
restent trois fois plus fines que l'écran et tombent à 15 Mio : **la scène passe de
101,4 à 57,1 Mio de textures**, sans différence visible sur une capture au plus près.
`SUR`, dans `bulleTex`, est le seul chiffre à toucher pour revenir en arrière.

**L'empaquetage de la sauvegarde.** La grille part toutes les six secondes. Les deux
tampons de travail sont gardés d'un enregistrement à l'autre : l'ancienne version
allouait à chaque fois 180 Kio, puis un tableau JS de près de cinquante mille nombres
boîtés, puis une copie par tranche de huit mille — le genre de rafale qui finit par
déclencher un ramassage de miettes au milieu d'une image. La sortie est identique au
bit près.

## Sauvegarde

La partie s'enregistre toute seule dans le stockage local du navigateur, toutes les
six secondes et à chaque fois que l'onglet passe en arrière-plan. Le terrain complet
en fait partie : les 28 561 cellules sont compressées en RLE puis en base64, ce qui
tient dans quelques kilo-octets.

Les traînées d'outil, elles, ne sont pas sauvegardées — les rejouer à l'identique
demanderait de conserver toutes les trajectoires. Au chargement, chaque cellule est
repeinte selon son état : le champ est un peu plus carré qu'à la sortie de la
machine, mais il dit exactement la même chose du terrain.

**La version de la sauvegarde ne bouge jamais.** La garde de relecture est une égalité
stricte — `S.v !== 1` — et l'incrémenter rejetterait d'un coup toutes les parties en
cours avec « sauvegarde illisible ». La campagne s'y est donc greffée en **champs
facultatifs** : une partie d'avant n'a pas de bloc `campagne`, et se relit sans lui.

Elle reçoit alors le palier que son avancement mérite, **déduit de ce qu'elle possède**
— ses cultures, ses engins, ses outils, ses métiers d'atelier, ses enclos, ses parcelles.
C'est la lecture la plus généreuse, et c'est voulu : mieux vaut rendre un palier de trop
que reprendre un tracteur payé. La règle générale est que **les paliers sont un plancher,
la propriété l'emporte toujours** — rien de ce qui a été acheté n'est jamais reverrouillé.

Ses cinq anciens paliers d'atelier deviennent les six métiers correspondants, rendus
gratuitement : un joueur qui avait payé la cave se réveillerait sans elle autrement.

Les **contrats acceptés** et la **renommée** de chaque commerce se sont greffés de la
même façon, en champs facultatifs du bloc `campagne` : une partie d'avant repart sans
contrat en cours et devant un village qui n'a rien contre elle. Les **propositions en
attente**, elles, ne se sauvegardent pas — un commerce qui nous attendrait depuis trois
semaines n'aurait aucun sens, et la première proposition retombe de toute façon huit
secondes après le chargement.

« Nouvelle partie », dans l'onglet Réglages, efface tout et repart d'une terre vierge.

Le même onglet règle la **netteté**. Le jeu rend en basse définition puis agrandit au
plus proche — c'est ce qui donne l'escalier de pixels des contours — mais sur un écran
très dense cela revient à remplir près de trois fois la définition de l'écran. Trois
positions : maximale (ce qui existait), élevée (plafonnée à deux fois la définition
CSS), douce (une fois et demie, le plus fluide). Sur un écran ordinaire, aucune des
trois ne change quoi que ce soit.
