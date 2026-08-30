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
| **Voir où l'on en est** | la **barre de progression**, en haut : elle ouvre l'écran de campagne — le palier, la mission du moment, et les vingt paliers à venir |
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
bloqué : tout ce qui sort de la ferme donne un filet d'expérience — un centième d'euro de
marchandise vendue — en plus de ce que paient les missions.

La règle de découverte est toujours la même : **un acheteur réclame quelque chose
qu'on ne sait pas encore produire**. C'est la demande qui enseigne la mécanique.

### Les vingt paliers

| | ouvre |
|---|---|
| 1 · Le fermier | blé, charrue, semoir, benne, tracteur, moissonneuse, pick-up, coopérative, comptoir agricole, garage, usine de céréales |
| 2 · Productivité | l'épandeur |
| 3 · Première transformation | le moulin, la farine, la boulangerie |
| 4 · Le maïs et les poules | deuxième parcelle, maïs, broyeur, poules |
| 5 · Deux chaînes à la fois | rien — c'est la tournée qui change, pas l'outillage |
| 6 · L'orge | troisième parcelle, orge, fourgon, cuve de brassage, épicerie, restaurant |
| 7 · L'avoine | avoine, usine d'avoine |
| 8 · Les vaches | quatrième parcelle, mélangeur premium, vaches, laiterie |
| 9 · Fromage fermier | la fromagerie de la ferme |
| 10 · Gros volumes | cinquième parcelle, supermarché |
| 11 · Les brebis | moutons, brebis, atelier textile, fromagerie du village |
| 12 · Fromage de brebis | sixième parcelle, fromagerie de brebis |
| 13 · L'apiculture | ruches, marché |
| 14 · La gamme fermière | septième parcelle |
| 15 · Le colza | colza, pressoir |
| 16 · Les olives | huitième parcelle, oliveraie, enjambeuse, huile d'olive |
| 17 · Le raisin | vigne |
| 18 · Le vin | neuvième parcelle, cave, caviste |
| 19 · Les cochons | cochons, boucherie |
| 20 · Exploitation complète | toute la vallée, autant de parcelles qu'on en veut |

Un commerce est **bâti dès le premier jour** — on le voit, on passe devant — mais il
ne traite avec la ferme qu'à son palier, et sa bulle le dit depuis la route. C'est ce
qui donne à un village construit d'un bloc l'allure d'un village qui s'ouvre.

**Un palier ouvre ce que sa mission va demander, pas ce qu'elle vient de faire gagner.**
Le barème donne pour chaque mission le « niveau après » — celui où l'on arrive une fois
qu'elle est finie — et les ouvertures sont donc posées **un cran plus tôt**, au palier où
la mission s'affiche. Écrites au niveau d'arrivée, vingt-huit des trente missions
réclamaient quelque chose d'encore verrouillé : on lisait « apportez-moi 72 kg de farine »
avec un moulin invendable. Un banc parcourt les trente missions, ligne par ligne, et
compte les demandes impossibles : **zéro**.

La table `NIVEAUX` est la seule source de tout cela. Elle est retournée **une fois**
en index inverse : les douze verrous du fichier l'interrogent vingt fois par seconde
sans jamais parcourir vingt niveaux.

Le **nombre de parcelles** monte de un tous les deux paliers, et il tient compte de ce que
la campagne oblige à garder en terre — le blé jusqu'au bout, le colza, les olives et la
vigne qui sont permanentes, les enclos qui le sont aussi. Le même banc vérifie qu'à chaque
palier le droit couvre le besoin.

### Les trente missions, et les seuils qu'un banc vérifie

Trente missions de campagne, une à la fois, dans l'ordre : de 30 kg de blé à la
coopérative jusqu'à une réception de village qui réclame **huit marchandises de sept
filières** à la fois. Deux formes : **livrer** des lignes chez un commerce nommé, ou
**faire** quelque chose qui ne se livre pas — monter le mélangeur premium et en sortir un
premier aliment, engraisser quatre porcs pour la boucherie.

Chacune parle. Le texte est celui du client, pas celui du jeu : *« La Coopérative m'a
parlé de votre récolte. J'aimerais tester 80 kg de blé. »* On n'y explique jamais comment
faire — c'est le rôle du guidage — seulement ce qu'on veut et pourquoi.

**Les seuils d'expérience sont écrits, et c'est un banc qui prouve qu'ils tombent juste.**
Ils étaient déduits : le seuil du palier *n+1* valait la somme des expériences du palier
*n*. La déduction ne se trompe jamais, mais elle interdit aussi de vouloir qu'un palier
arrive plus tôt que la somme ne le voudrait. Les vingt seuils sont donc posés à la main —
0, 100, 250, 450, 700, 1 000 … 10 450 — et un banc joue la campagne mission par mission,
en ajoutant chaque prime d'expérience, pour vérifier que **chacune des trente tombe très
exactement sur le palier que le barème lui donne** :

```
paliers : N1 N2 N2 N3 N4 N4 N5 N6 N6 N7 N8 N8 N9 N9 N10
          N11 N11 N12 N13 N13 N14 N15 N15 N16 N17 N17 N18 N19 N20 N20
```

La campagne entière vaut **11 640 XP** pour un dernier seuil à 10 450 : faire la campagne
suffit toujours, avec de la marge, et c'est la seule chose qu'il y ait à faire — la mission
du moment est le seul ordre du jeu. Une preuve vaut mieux qu'une dérivation : elle survit
au jour où l'on voudra déplacer un seuil.

**Les primes suivent l'échelle de ce qu'on livre**, de 200 € pour les trente premiers
kilos de blé à 40 000 € pour la réception finale, et les prix du matériel qu'une mission
exige sont ceux du barème d'équipement : épandeur 250 €, poulailler 800 €, mélangeur
premium 1 200 €, fromagerie 1 800 €, cave 4 500 €, enjambeuse 5 000 €.

### Le mode libre, hors campagne

Un troisième bouton à l'accueil, après *Reprendre* et *Nouvelle partie* : **MODE LIBRE**.
Aucun palier n'y verrouille quoi que ce soit — tout s'achète dès qu'on en a les moyens — il
n'y a pas de mission, et ce sont les contrats du village qui prennent le relais. C'est le
même interrupteur qui les tenait fermés.

Il court-circuite **`ouvert()`**, le seul point de passage des six familles : cultures,
outils, engins, modules, espèces et commerces tombent d'un coup, sans une exception
disséminée dans les treize appelants. Relevé : **34 verrous au premier palier de campagne,
0 en libre**.

Trois choses ne passent pas par là et sont traitées à part. Les **parcelles** ont leur propre
juge : la vallée entière devient achetable. Les **huit comparaisons écrites à la main** dans
les menus passent par un jumeau — sans elles le verrou serait levé mais le bouton resterait
gris, « Niveau 12 requis » écrit sur ce qu'on a le droit d'acheter. Et l'**écran de fin** se
déclenchait sur *dernier palier ET plus de mission* : en libre il n'y a jamais de mission, et
le premier joueur à atteindre le palier 20 par l'expérience aurait vu l'accueil reprendre la
main, boutons effacés, jeu en pause.

Le bouton n'est **jamais le principal** : dix bancs entrent dans le jeu en cliquant le premier
`.accbtn.pri`. Il refait les enseignes au passage, sans quoi treize d'entre elles resteraient
à « NIVEAU 8 » sur des commerces désormais ouverts.

Le mode se sauvegarde en **champ facultatif**, la version ne bouge pas, et une sauvegarde
d'avant vaut campagne. Il se restaure **deux fois** à la relecture : une avance dès la garde,
parce que la relecture des engins interroge `ouvert()` deux cents lignes avant que la campagne
ne soit restaurée, puis pour de bon ensuite.

### Pendant la campagne, la mission est le seul ordre

Le village proposait, **en plus** de la campagne, ses propres contrats : quatre à la fois,
avec leurs délais, leurs primes et une renommée qui montait ou descendait. On se retrouvait
devant deux listes au lieu d'une histoire — et les deux ne jouaient pas dans la même cour.
Relevé au huitième palier : la mission paie **4 500 € et 280 XP**, un contrat **107 € et
4 XP**. Il aurait fallu **112 contrats pour gagner un niveau**, quand le village n'en
propose que trois à la fois.

La campagne ne propose donc plus qu'une chose : **la mission du moment**. Un mode **libre**,
hors campagne, rouvrira les contrats — la machinerie reste entière derrière un seul
interrupteur, `MODE_LIBRE`, et il n'y a pas une ligne morte ailleurs.

Relevé : **une heure de jeu simulée, zéro proposition**. Une sauvegarde qui portait un
contrat revient sans lui. Et l'écran de campagne ne parle plus ni de contrats ni de
renommée — une section vide intitulée « Les contrats en cours » ferait chercher toute la
partie une mécanique qui n'existe pas ici.

Ce que la campagne garde de ce système, c'est sa **façon de proposer**, et c'est la mission
qui l'a reprise : une pastille au sol, un bouton, une fenêtre. La section suivante la
décrit.

#### Ce que le mode libre rouvrira

Le moteur dort, il ne disparaît pas, et un banc continue de le tenir pour qu'il n'ait pas
dérivé le jour où l'on rouvrira l'interrupteur.

C'est le **commerce** qui propose, et il le dit sur place : une pastille verte pleine
s'allume au sol, au centre de son anneau de livraison. On s'y arrête, un bouton vert
**VOIR LE CONTRAT** apparaît, et la fenêtre s'ouvre — ce qu'il réclame, la marchandise au
prix du jour, la prime à la clôture, le délai s'il y en a un, et la renommée qu'on a chez
lui. **Accepter** le prend, **Refuser** coûte deux crans de renommée, **Retour** ne dit
rien et l'offre reste sur place.

Le tirage garde ses quatre natures — brute, transformée, composée, urgente — et le
**client se choisit avant les lignes** : en composant d'abord un panier puis en cherchant
qui le prend, une commande finissait par réclamer de l'huile d'olive à l'usine de céréales.
Relevé : **400 propositions, 0 indélivrable**.

**La quantité se mesure en argent, pas en kilos.** Une échelle en poids, commune à tous les
produits, réclamait trois cents kilos de miel comme trois cents kilos de blé : cinq fois la
valeur pour le même geste, et une ruche qui sort deux kilos par minute et demie contre une
moissonneuse qui rentre une parcelle. Depuis que l'œuf se compte à la pièce, c'était pire —
le jeu stocke en kilos, un œuf pèse soixante grammes, et la boulangerie demandait
**7 500 œufs** au dernier palier, **667 au quatrième**, quand on a six poules.

L'échelle est donc une **valeur de marchandise** — 14 € au premier palier, 273 € au
vingtième — que le prix du produit traduit en quantité, chacun dans son unité. C'est très
exactement l'ancienne courbe en kilos multipliée par le prix du blé : le blé, sur lequel
elle avait été réglée, **ne bouge pas d'un kilo** (25 kg à la première commande hier, 25 kg
aujourd'hui), et tout le reste vient se ranger à côté de lui. Écart entre la ligne la mieux
et la moins bien payée d'un même palier : **14,58 × avant, 1,18 × après** — ce qui reste
est l'arrondi.

Le pas d'arrondi descend d'ailleurs **à l'unité sous la quinzaine**. Arrondir cinq kilos de
fromage de brebis au pas de cinq, c'était en perdre deux — trente pour cent de la commande.

**La cible est un vœu, la capacité est une limite.** On arrondit au plus près — c'est ce qui
donne 25 kg de blé pour une cible de 23 — mais jamais au-dessus de ce que la ferme peut
sortir. Le plancher d'une ligne valait un pas d'arrondi pris sur la *cible* et non sur le
possible : un pas de vingt litres imposait **vingt litres de lait à qui n'a qu'une vache**
et n'en tire que quinze, et la commande naissait déjà perdue. Et le repli garde le filtre de
capacité : quand aucun produit d'une nature n'était réalisable, le tirage rouvrait **tout**
ce que le palier avait débloqué et proposait du lait de brebis à qui n'a pas une seule
brebis. S'il n'y a rien à proposer, on ne propose rien.

**La récompense ne casserait pas l'économie** : on est payé le prix normal de la marchandise
au moment où on la livre — le circuit habituel, celui des étals et des caisses d'usine —
puis la prime s'ajoute à la clôture. Les prix du village restent donc exacts.

### La mission de campagne se prend sur place

La première mission s'affichait dès la seconde zéro, en haut à gauche : on démarrait avec
un ordre qu'on n'avait demandé à personne, et c'était le dernier endroit du jeu où quelque
chose tombait du ciel. Une mission qui nomme un **lieu** est maintenant proposée par ce
lieu — pastille verte, `VOIR LA MISSION`, fenêtre, on prend.

Le cercle de son quai passe au **vert**, et pendant la campagne il n'y en a jamais qu'un.
C'est la même forme que partout ailleurs — voir la section suivante.
Tant qu'on ne l'a pas prise, elle n'est nulle part à l'écran, et **livrer d'avance ne
compte pas** : on ne peut pas honorer un engagement qu'on n'a pas pris.

Elle ne se **refuse** pas — c'est le fil du jeu. La fenêtre n'offre que *Prendre la
mission* et *Retour* ; retour la laisse sur place, elle attendra. Une mission **sans lieu**
— s'équiper, acheter une parcelle, monter un enclos — n'a personne pour la proposer :
celle-là s'affiche directement, il n'y a nulle part où aller la chercher.

En mode libre, aucune offre commerciale ne viendra se poser par-dessus : deux choses
derrière la même pastille, on n'en verrait qu'une.

### Une seule forme au sol, et la couleur seule parle

Il y avait deux formes de marque au sol, et il fallait apprendre les deux : un **anneau**
jaune, creux et additif, pour ce qu'on peut faire ici, et une **pastille** pleine, verte ou
bleue, plus petite, pour ce que le guidage a à dire. Aux quinze commerces les deux se
superposaient — un disque au milieu d'un cercle — et il fallait deviner lequel des deux
venait de changer.

C'est maintenant un **cercle**, un seul : un liseré franc et un centre de la même couleur,
nettement plus transparent. Trois déclinaisons, rien d'autre qui change :

| | |
|---|---|
| **jaune** | une action possible ici, ou l'objectif du moment |
| **vert** | une mission à prendre |
| **bleu** | un service permanent — Garage, Comptoir agricole, Coopérative, la cuve à gazole |

En veille, le même cercle en blanc froid, très transparent : le quai reste visible, il ne
dit simplement rien. Relevé : **dix-huit marques, une seule forme, un seul rayon**.

Et **un seul cercle par commerce**. Depuis qu'ils ont la même forme, deux marques au même
point seraient deux cercles concentriques identiques. Le sol ajoute une chose à la règle du
guidage — *ce qu'on peut faire ici, maintenant* — parce qu'il est la seule surface qui parle
de l'endroit où l'on est : la carte et les flèches, elles, disent où aller et gardent un
seul jaune. Un comptoir où l'on a de quoi acheter passe donc au jaune, et redevient bleu une
fois la remorque pleine.

Un service bleu **respire moins**. La forme est la même, mais « le bleu représente une
possibilité, pas une obligation » : donner aux quatre lieux permanents le battement de la
seule chose qu'on ait à faire les mettrait à son rang, et ils clignoteraient d'un bout à
l'autre de la partie.

**La cuve à gazole est un service comme les autres**, donc bleue et allumée en permanence.
Elle passait au jaune quand on pouvait faire le plein — mais on ne va pas au gazole parce
qu'une lumière s'allume, on y va parce qu'on en manque, et la jauge le dit déjà. Son cercle
a aussi changé de place : il était au **bout** de la cuve, quatre mètres au-delà du pistolet,
et l'on se rangeait nez à nez avec ses six mètres quarante. Il est maintenant sur son
**flanc est** — le seul libre, le hangar occupant tout l'ouest à deux mètres vingt — et l'on
se range le long d'elle, comme à une pompe.

### L'étiquette d'un commerce ne dit que son nom

Elle déroulait ce qu'il achète, à quel prix, ce qu'il vend, ce qu'il transforme et ce qu'il
propose : jusqu'à onze lignes sur un panneau de **dix-neuf mètres** de large, quinze fois
dans le village. On ne voyait plus les bâtiments derrière, et l'on ne lisait de toute façon
aucun de ces prix en roulant — le détail est dans le menu Filières, où on le consulte assis.

Reste ce dont on a besoin depuis la route : **savoir où l'on est**. Le nom, une barre à la
couleur du toit, **8,60 m** de large. Un commerce encore fermé garde la seule ligne qui
manquerait sans elle — le palier qui l'ouvrira — parce que ce n'est pas ce qu'il achète,
c'est la raison pour laquelle il n'achète rien ; et sa plaque est plus transparente, son nom
gris au lieu de blanc, de sorte qu'on le distingue sans lire.

La densité y **gagne** : 560 px sur 8,60 m font 65 pixels par mètre, contre 34 pour les
640 px de l'ancien panneau de dix-neuf mètres. L'étiquette est deux fois plus fine par mètre
en pesant six fois moins.

### Tous les pictogrammes ont le trait de la pompe à gazole

Ils portent tous `stroke-width="2"` dans une boîte de 24, mais ne sont pas rendus à la même
taille : les jauges de droite demandent 18 pixels, les boutons 22. Relevé à l'écran, la
pompe traçait **1,95 px** et le bouton d'à côté **2,38** — un quart plus épais, et c'est ce
quart qui se voyait. L'épaisseur est maintenant **déduite de la taille demandée** pour que le
trait rendu soit toujours celui de la pompe : 2,00 à dix-huit pixels, 1,64 à vingt-deux. Le
dessin reste écrit une seule fois.

### Les roues suivent le roulis au-delà de trois degrés

La caisse prenait du roulis, les roues restaient plates : en virage serré, la carrosserie
basculait de dix degrés au-dessus d'un essieu immobile et le haut du pneu ressortait à
travers l'aile. Les roues sont réunies sous un **train** qui peut basculer lui aussi, sans
rien changer à leur roulement ni à leur braquage, qui restent locaux.

La suspension d'un vrai véhicule a une **course** : sous un petit roulis la caisse bouge
seule, les roues restent au sol — c'est ce qu'on voulait et on le garde — mais la course a
une **butée**, et au-delà l'essieu part avec. Le roulis de caisse est inchangé, c'est lui
qu'on voit, et l'écart entre les deux ne dépasse plus jamais **0,052 rad**, soit trois
degrés. Le roulis étant borné à ±0,17, la butée en reprend les deux tiers dans un virage à
fond, et rien du tout en ligne droite.

### Une mission éclaire tout son chemin, et rien d'autre

Un seul lieu s'allumait : celui de l'étape du moment. Tout le reste était gris — sauf les
commerces où l'on pouvait faire quelque chose, qui passaient au jaune parce qu'ils achètent
ce qu'on transporte. Pour « livrer 30 kg de blé à la Coopérative », **l'usine de céréales
s'allumait donc en jaune** : elle achète du blé. Ça n'a aucun sens pendant une mission, et
ça noyait le seul lieu qui comptait.

Une mission éclaire maintenant **tout son chemin**, et lui seul :

| | |
|---|---|
| **jaune vif** | l'étape du moment — et elle seule porte la flèche du bord |
| **jaune doux** | les étapes suivantes, dans l'ordre, sans flèche |
| **vert** | une mission à prendre |
| **bleu** | un service permanent |

Pour la première mission, cela donne **CHAMP → SILO → COOPÉRATIVE** : le champ en vif, les
deux autres en doux. Si l'on avait déjà moissonné avant d'aller prendre la mission, le champ
sort de la chaîne et c'est le **silo** qui passe vif ; la benne pleine, il ne reste que le
client. C'est la même règle qui décide dans les trois cas — le juge dit où l'on en est, le
chemin dit ce qui vient après.

**Et avant d'avoir pris la mission, il n'y a qu'un vert.** Aucune chaîne, donc aucun jaune :
le seul lieu qui parle est celui qui a une mission à donner. On ne peut pas se tromper de
premier geste.

**Une seule flèche jaune**, celle de l'étape du moment. Trois flèches pour une seule mission
borderaient l'écran et l'on ne saurait plus laquelle suivre : le bord dit où aller
maintenant, le sol dit le reste du chemin. Et le jaune doux respire au tiers du vif — même
marque, même forme, mais elle n'appelle pas.

**Le silo, l'entrepôt et les enclos portent la couleur du guidage**, eux aussi. Ils n'avaient
qu'un jaune fixe et ne pouvaient donc dire ni « c'est ici » ni « et ensuite », alors que le
silo est le maillon central de presque toutes les chaînes. Hors mission — en mode libre, ou
avant d'avoir pris la première — leurs cercles retrouvent leur rôle d'origine et disent ce
qu'on peut faire ici, maintenant.

**Le pictogramme d'action a été retiré.** Une caisse, une flèche, un épi posés sur
l'objectif : il ajoutait un vocabulaire de plus à apprendre là où la couleur suffit, et il
encombrait l'objectif au lieu de le désigner. Restent trois **cercles mobiles**, pour les
étapes sans domicile fixe : un champ n'a pas d'anneau à lui, et c'est pourtant lui qu'il faut
aller récolter neuf fois sur dix.

### Bravo, mission terminée

Une mission se soldait sur une ligne de bandeau qui s'effaçait en deux secondes et demie,
entre deux autres. C'est le seul moment de la campagne où l'on a fini quelque chose.

Un écran s'ouvre maintenant : **BRAVO**, le nom de la mission, et le détail de ce qu'on a
gagné — la prime, l'expérience, la valeur de la marchandise livrée, et le palier s'il vient
de tomber. Les lignes entrent l'une après l'autre, à quatre-vingt-dix millisecondes
d'intervalle. Puis la mission suivante est nommée.

**Mais le jeu ne s'arrête pas.** Pas de pause — elle gèlerait les pièces, le décompte et le
bandeau lui-même — pas de bouton, et surtout aucun `.accbtn` : c'est par le premier
`.accbtn.pri` que toute la suite de bancs entre dans le jeu. Le calque se ferme seul au bout
de cinq secondes, ou d'une pression si l'on est pressé, et l'on continue de conduire
pendant qu'il est là. Un dégradé radial plutôt qu'un aplat : on voit sa ferme derrière.

**Et l'ordre a changé, parce que c'était un bug.** Le bandeau annonçait « MISSION FAITE
+2 800 € » *puis* l'on gagnait l'expérience — et si elle faisait monter d'un palier,
l'annonce du palier écrasait la phrase deux millisecondes plus tard : on ne voyait jamais ce
qu'on venait de gagner. L'expérience se compte d'abord, la fête ensuite, le bandeau en
dernier.

### Elle saute en arrivant, elle s'allume, et une flèche dit de continuer

Elle était trop figée : les lignes entraient l'une après l'autre, mais la **boîte**, elle,
était posée. Le joueur :

> « Dès qu'il y a une fenêtre qui apparaît avec un gros message, fais-la bouger, fais-la
> vibrer un petit peu, fais-la s'allumer, et tu mets un bouton un peu marrant avec une
> flèche à droite en bas de la fenêtre pour continuer. »

Trois choses, et pas une de plus :

- **Elle tombe.** Vingt-six pixels au-dessus, un dépassement de quatre centièmes, deux
  degrés de gîte, et elle se recale en 0,52 s — un ressort, pas un fondu.
- **Elle s'allume.** Un voile jaune posé à l'intérieur du cadre, qui monte à 0,55 d'opacité
  en un cinquième de seconde et s'efface en une seconde. C'est un pseudo-élément et une
  `opacity` : rien à repeindre.
- **La flèche.** Un rond jaune en bas à droite, qui pousse vers la droite tout seul et
  grossit d'un dixième sous le doigt. Il n'a **pas de gestionnaire à lui** : le clic remonte
  à la boîte, qui fait déjà passer à la suite. Toucher n'importe où marche encore — le bouton
  ne fait qu'annoncer ce qu'on pouvait déjà faire.

**Et les appels se dandinent.** *« Pareil pour les onglets, ou pour les trucs qui font une
pulsation, ou pour les boutons pour changer de véhicule dans la mission : fais vibrer un
petit peu ces boutons, une petite animation qui bouge un peu de gauche à droite, dans le
sens horaire, anti-horaire. »*

C'est une **secousse, pas une oscillation** : le mouvement tient dans la première moitié
d'un cycle de 2,1 s, la seconde est immobile. Un bouton qui tremblerait sans arrêt sous le
pouce pendant qu'on conduit deviendrait vite pénible ; celui-ci fait signe, se tait, refait
signe.

| ce qui appelle | ce qu'il fait |
|---|---|
| `#engins`, les trois boutons de régie | un anneau qui s'écarte + une gîte de 3,4° |
| `#veh`, `#service`, `#atelier` | le même, avec une gîte de 2,4° |
| un onglet, une ligne d'article | un cadre plat qui bat + une respiration à 0,965 |
| une ligne du parc | un cadre plat + un glissement de 4 px |

**Deux pièges, et ils sont dans le CSS.** Le premier : `#veh`, `#service` et `#atelier` sont
centrés par `transform:translateX(-50%)`. Une animation de `transform` qui l'oublierait les
ferait sauter d'une demi-largeur vers la droite — d'où deux jeux d'images, dont l'un
reconduit le centrage à chaque étape. Le second : un onglet ne peut pas **grandir**.
`#fenonglets` a `overflow-x:auto` et `#fenliste` un `overflow-y:auto` — qui force l'autre axe
à `auto` lui aussi — si bien qu'un débordement d'un seul pixel ferait apparaître une barre de
défilement, et la barre d'onglets se mettrait à glisser toute seule. Elle **rétrécit** donc,
de trois centièmes et demi : un mouvement qui ne peut pas sortir de la boîte, par
construction.

Tout cela n'anime que `transform` et `opacity`, sans exception. C'est la leçon payée une
fois : une `box-shadow` animée coûtait un dixième des images du jeu, 8,7 contre 9,6.

**Et le bouton de service appelle enfin.** Le cercle sous les roues passait au jaune quand la
mission envoyait là, et le bouton en prenait la couleur — mais il n'appelait pas. C'était le
dernier bouton du jeu que le guidage désignait sans le désigner. Il porte maintenant la même
marque que la régie, avec `a.ok` en garde : un bouton grisé qui trépignerait promettrait une
action qu'il refuse d'exécuter.

### Des pièces, quand on est payé

L'argent tombait en silence. On déchargeait quatre cents kilos de blé, le chiffre du bandeau
montait, et rien à l'écran ne disait qu'on venait d'être payé — le seul encaissement qui
parlait était celui de la boucherie.

Vingt-huit jetons préalloués, une géométrie partagée, zéro allocation en jeu. **Un pool à
part, jamais celui des bouffées** : les particules de poussière sont un anneau de cent trente
que le transfert, l'échappement et les cheminées se disputent déjà, et y glisser les pièces
couperait la poussière au moment précis où elle sert.

Le nombre de jetons suit un **logarithme** : quatre pour vingt-cinq euros, huit pour deux
mille cinq cents, neuf au plafond — sans quoi une prime de quarante mille en cracherait
quarante. Et ce qui se paie en continu — une vente d'étal appelle l'encaissement à *chaque
image* — passe par un accumulateur qui sort une pièce tous les seizièmes de seconde : un
filet pendant qu'on décharge, qui s'arrête tout seul.

### Le service permanent sous les roues se nomme

Les trois services permanents sont bleus au sol et bleus sur la carte, mais leur anneau ne
dit pas ce qu'on y fait : on s'arrête au **Comptoir agricole** sans savoir qu'il vend aussi
le gazole, et l'on repart le chercher ailleurs.

Dès qu'on entre dans la zone de l'un d'eux, le bandeau écrit son **nom et sa fonction** —
celle du cahier des charges, la même que sous la flèche du bord — et l'efface dès qu'on en
sort :

> **COMPTOIR AGRICOLE**  Graines & consommables
> **GARAGE**  Matériel & améliorations
> **COOPÉRATIVE**  Vente libre

C'est du **contexte, pas une tâche** : ni barre d'avancement, ni puce, et il ne survit pas
au fait de repartir. La mesure de la zone est celle de l'anneau de livraison, la même que
partout — on ne peut pas être « dedans » selon le bandeau et « dehors » selon le bouton
d'action. Un commerce qui n'est pas un service permanent ne se nomme pas.

Le bandeau y gagne **sept pixels** dans son pire cas — quatre contrats, la mission, et l'on
est arrêté au Comptoir : de 5,3 % à 7,0 % de l'écran, le temps de l'arrêt.

### La flèche verte du bord

Une pastille qui tombe à l'autre bout de la vallée n'existe pour le joueur que s'il passe
devant par hasard. Une **flèche verte** au bord de l'écran pointe donc vers chacune de
celles qui sont hors cadre, avec le nom du commerce et la distance : on sait qu'il y a
quelque chose, dans quelle direction, et si ça vaut le détour. Dès que la pastille entre
dans le cadre, la flèche s'efface.

Le calcul tient en trois temps : on projette le point ; on regarde s'il est dans le cadre
**utile** — celui qui exclut le bandeau du haut et les commandes du bas, sinon la flèche
se pose sous le manche ; sinon on coupe le rayon partant du centre sur ce rectangle. Un
point derrière la caméra sort de la projection avec ses signes inversés, et il faut le
retourner sans quoi la flèche pointe à l'exact opposé. La vignette entière est rentrée
dans l'écran, libellé compris — sur un bord latéral on lisait « COOPÉRATIV ».

**Et plus petites.** Trente pixels de flèche et huit et demi de libellé : sur une route
bordée de commerces, trois vignettes de cette taille occupaient un bon quart du bord de
l'écran. Vingt-deux et sept — la pointe reste franche, le nom reste lisible, et c'est une
indication de direction, pas un panneau.

**Un triangle, mais pointu.** Le premier était équilatéral — trois angles de soixante
degrés — et un triangle dont tous les angles se valent ne pointe nulle part : tourné d'un
quart de tour on le reconnaît encore comme un triangle, pas comme une direction. Celui-ci
est **étiré** : sa pointe fait **28°** quand les deux angles de base en font **76°**.
C'est cet écart, et lui seul, qui dit où aller. Trois sommets, rien de plus.

**Et elle ne sautille plus.** Elle était posée par `left`/`top` en pixels entiers,
recalculés vingt fois par seconde : chaque écriture remettait l'élément en page, et le
pas d'un pixel se voyait. Elle est posée par `transform`, au centième de pixel, à
**soixante images par seconde** — le compositeur s'en charge sans remise en page.

Trois sommets, un aplat, **rien d'autre** : ni contour, ni ombre, ni filtre. Un filtre
force un repeint complet à chaque déplacement, et c'était cher pour un halo qu'on ne
regardait pas ; le vert vif se détache seul.

### Rien à l'écran qu'on n'ait accepté

C'est la règle, et elle n'a pas d'exception. Une mission qu'on n'a pas encore prise ne pose
**aucune** puce au bandeau, et ne déroule ses lignes nulle part : livrer d'avance ne compte
pas, et l'on ne peut pas honorer un engagement qu'on n'a pas pris.

En mode libre, la même règle vaudra pour les propositions du village : la Campagne dira
seulement qu'un commerce « a quelque chose à proposer — passer devant son quai pour
l'entendre ». Un menu qui donnerait le détail rendrait l'anneau décoratif : on choisirait
ses contrats depuis un tableau, sans jamais aller voir personne.

### Le bandeau ne mange plus l'écran

Quatre pilules de commande, deux lignes chacune, occupaient la moitié gauche de
l'écran : on jouait derrière sa liste de courses. Un contrat accepté tient maintenant
dans une **puce d'une ligne** — le lieu, l'avancement, le délai s'il court — de 23 px de
haut, large de son seul texte. On la touche et la même fenêtre se rouvre, en lecture
seule cette fois, avec ce qui reste à livrer ligne par ligne.

Relevé, quatre contrats plus la mission de campagne : **406 × 190 px avant, 257 × 158
après** — de 8,5 % à 5,3 % de l'écran, et la largeur ne suit plus le bloc mais le texte.

Pendant la campagne, le bandeau ne porte plus que la **mission** : ces puces sont celles
que le mode libre rouvrira, et la mesure ci-dessus est leur pire cas.

### Les volumes : une parcelle rend 250 kg, la trémie en tient 100

Une parcelle de blé rendait **1 104 kg** quand la première mission du jeu en demande
trente. On récoltait plus d'une tonne d'un coup, on remplissait le silo en deux passages,
et les commerces devenaient des puits sans fond. Les rendements sont divisés par **4,44**
et la parcelle de départ — 552 cellules — rend maintenant **248 kg**.

| | par cellule | une parcelle de 552 | en trémies |
|---|---|---|---|
| Blé | 0,45 kg | 248 kg | 2,5 |
| Maïs | 0,79 kg | 436 kg | 4,4 |
| Colza | 0,56 kg | 309 kg | 3,1 |
| Avoine | 0,38 kg | 210 kg | 2,1 |
| Orge | 0,40 kg | 221 kg | 2,2 |
| Raisin | 0,34 kg | 188 kg | 1,9 |
| Olives | 0,29 kg | 160 kg | 1,6 |

**La trémie de la moissonneuse fait l'unité**, à **100 kg**, et tout ce qui transporte ou
range se règle sur elle — divisé par trois, en gardant ses proportions à la trémie :
benne 400 → **135**, pick-up 200 → **70**, fourgon 460 → **155**, enjambeuse 300 → **100**,
silo 8 000 → **2 700**, entrepôt 4 000 → **1 350**, trémie d'usine 1 000 → **335**, lot
d'atelier 50 → **20** au premier palier.

**Et l'argent n'a pas bougé d'un euro.** Les prix au kilo sont multipliés par le même
4,44 : le blé passe de 0,50 à **2,22 € le kilo**, et une parcelle rapporte toujours
**551 €** au lieu de 552. Tout ce qui se compte en euros — le prix des parcelles, des
engins, des métiers d'atelier, les primes de mission — reste tel quel, et la progression
avec. Semer une parcelle coûte toujours 37 € ; une cuve de lait pleine vaut toujours
373 € et met toujours 14 minutes à se remplir ; le moulin met toujours 3 min 40 pour une
parcelle de blé. Seuls les **nombres de kilos** ont changé.

Le seul écart voulu est celui que la trémie impose : la terre a été divisée par 4,44 et
le transport par 3, donc **un voyage vaut une fois et demie plus qu'avant**. C'est la
conséquence directe des deux chiffres demandés — 250 kg par parcelle, 100 kg de trémie —
et cela fait 2,5 voyages par parcelle de blé au lieu de 3,7.

Les **missions de campagne** sont recalées là-dessus : elles demandaient entre 2,7 % et
70 % de ce qu'une parcelle produit, sans ordre ; elles dessinent maintenant une rampe
régulière de **12 % à 69 %**, du premier palier au treizième.

| palier | mission | part d'une parcelle ou d'une cuve |
|---|---|---|
| 1 | 30 kg de blé | 12 % |
| 1 | 60 kg de blé | 24 % |
| 2 | 120 kg de blé | 48 % |
| 3 | 50 kg de farine | 28 % |
| 4 | 120 kg de maïs | 28 % |
| 5 | 60 kg de farine + 13 d'œufs | 34 % / 41 % |
| 6 | 100 kg d'orge | 45 % |
| 7 | 100 kg d'avoine | 48 % |
| 8 | 80 kg de lait | 59 % |
| 9 | 10 kg de fromage + 60 de farine | 62 % / 34 % |
| 10 | 28 kg de laine | 62 % |
| 11 | 60 kg d'huile de colza | 57 % |
| 12 | 22 kg d'huile d'olive | 69 % |
| 13 | 80 kg de vin | 61 % |

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
première livraison rapporte 187 — trente kilos de blé à 2,22 €, plus 120 € de prime : il
fallait une vingtaine de tournées avant le premier agrandissement. Elle vaut **1 200 €**. L'échelle monte ensuite de moitié à chaque cran —
1 200, 2 500, 4 500, 7 500, 12 000 — puis s'aplatit à partir de la dixième : un empire
ne doit pas doubler de prix indéfiniment. Le total reste du même ordre qu'avant ; c'est
sa **répartition** qui change, et avec elle les vingt premières minutes.

### Ce que l'audit de l'échelle a trouvé

Diviser tous les kilos d'un jeu par 4,44 et tous les contenants par trois laisse forcément
des constantes derrière. Une relecture systématique en a trouvé quarante-trois, dont
vingt-huit tenaient à la vérification. Les défauts de jeu :

- **La trémie de l'enjambeuse sautait à 1 215 kg au premier cran d'amélioration.** Sa
  formule disait `900 × 1,35ⁿ` quand la caisse neuve en valait 300 : une seule
  amélioration la triplait déjà avant le facteur. La remise à l'échelle a divisé la caisse
  par trois sans toucher à la formule, et l'écart est passé de ×4 à ×12 — plus que
  l'entrepôt entier, de quoi emporter cinq parcelles de raisin d'un coup. Elle fait
  maintenant **100 / 135 / 182**, exactement comme la trémie de la moissonneuse.
- **Améliorer une enjambeuse au garage plantait le jeu.** La garde de l'amélioration
  d'outil excluait la coupe de la moissonneuse par son nom, pas le tunnel de
  l'enjambeuse : `T.group.scale` sur un outil intégré qui n'a pas de modèle. L'argent
  était déjà retiré, et l'exception emportait la fin du gestionnaire. La garde teste
  maintenant la présence du modèle, ce qui couvre les deux.
- **L'enseigne du comptoir agricole annonçait 0,35 € le kilo de semences quand la caisse
  en prenait 1,55.** C'était le seul prix au kilo du jeu écrit en toutes lettres, et il
  vivait quatre mille lignes avant la table qui le contredisait. Une seule constante
  sert maintenant aux deux.
- **La migration divisait par 4,44 des choses qui ne sont pas des kilos.** `STAT` mêle des
  poids et trois compteurs : `betes`, `labour`, `semis`. Un joueur qui avait vendu six
  bêtes se réveillait à 1,35, ce qui décochait la mission du palier 14 et ses 20 000 € de
  prime. Liste blanche des dix clés qui sont des poids.
- **Cinq champs de kilos des versions antérieures échappaient à la conversion** —
  `siloKg`, `flourKg` et les trois tas de la halle. Le pire était `siloKg`, affecté
  directement au silo sans garde de capacité : 8 000 kg de l'époque revenaient tels quels
  dans un silo qui en tient 2 700, soit 13 764 € offerts.
- **Une partie migrée n'avait pas la même benne qu'une partie neuve.** Les contenants
  n'ont pas été divisés par exactement trois — la benne est passée de 400 à 135, le
  pick-up de 200 à 70 — alors que la migration applique un trois rond : 133 et 67 au lieu
  de 135 et 70, définitivement. Au niveau 1, c'est désormais la table qui fait foi.
- **Quatre espèces sur cinq annonçaient « 0,00 kg / s ».** Deux décimales suffisaient tant
  qu'une vache donnait 0,07 kg/s ; les cadences sont maintenant à la **minute** — vache
  0,95, mouton 0,08 — et le jeu ne dit plus au joueur que sa bête ne produit rien.
- **La borne du dernier pas d'un transfert dosé** valait 420 kg/s pour un débit réel de
  47 : chaque image ne résorbait plus que 11 % du reste, et l'engin restait immobilisé
  près d'une seconde à écouler des grammes. Elle vaut 140.
- **Le premier palier de lot d'atelier** avait été divisé par 2,5 quand les onze autres
  contenants l'étaient par trois : le lot du débutant immobilisait l'atelier 1,78 fois
  plus longtemps qu'avant au lieu des 1,48 accordés partout ailleurs — et c'est le palier
  qu'on subit le plus longtemps, le suivant coûtant 900 €. Les quatre paliers sont
  maintenant les anciens divisés par trois : **17, 40, 84, 167**.

Le reste était de la dérive de commentaire — un écran qui expliquait au joueur que le
caviste écoule six cents kilos de vin quand son étal en tient trente-cinq, un en-tête qui
faisait le calcul de la farine avec l'ancien prix du blé. L'écran des prix lit maintenant
les deux plafonds dans la table plutôt que de les recopier.

### Ce qu'on trouve en ouvrant le jeu

Une partie neuve démarre **dans le pick-up**, pas dans la moissonneuse : celle-ci arrive
avec ses huit mètres de coupe déployés devant le capot, et c'est la première chose qu'on
voyait d'un jeu qu'on ne connaît pas. Le pick-up est court, rapide, sans outil.

Les **commandes à boutons** sont le réglage de départ, le **zoom à 75 %** — on voit venir
de plus loin — et la **netteté sur Élevée** plutôt que Maximale : la définition de l'écran
telle quelle coûte cher sur un portable pour une différence qu'on ne voit pas à cette
distance. Rien de tout cela n'est figé, les trois se règlent dans les Réglages.

**La cuve de gazole fait partie de la ferme.** Elle coûtait 7 500 € qu'on n'a pas au palier
1 : le seul moyen de faire le plein était donc la pompe du village, à 1,85 € le litre au
lieu de 1,48 en gros — on payait 25 % de plus précisément pendant les heures où l'on n'a
pas un sou. Elle est livrée pleine, et porte au-dessus d'elle la même étiquette flottante
que le silo et l'entrepôt : « Cuve 840 L / 3 000 L », qui vire à l'orange puis au rouge.
Ce qui s'achète, c'est ce qu'on met dedans.

**Le bac à engrais, lui, est vide.** Il contenait vingt-sept kilos, et c'était un cadeau
sans usage : l'épandeur est sous verrou et coûte 250 €, on ne peut donc ni les épandre ni
les revendre. Ils avaient en revanche un effet, et il était fâcheux — ils rendaient
*vraie d'avance* l'étape « acheter de l'engrais » du préambule de la troisième mission, qui
se testait par `STOCK.engrais > 0.5`. Voir [Un préambule, et un seul](#un-préambule-et-un-seul).

**La tour du silo suit la terre.** Elle tenait 2 700 kg quel que soit l'état de la ferme :
au palier 1, avec une seule parcelle qui rend 248 kg de blé, c'était onze récoltes d'avance
— elle ne se remplissait jamais et ne décidait rien. Elle vaut maintenant **deux récoltes
et demie de ce qu'on cultive**, plus un fond de cale : 662 kg avec une parcelle, 6 200 avec
vingt. Rentrer une moisson redevient une décision.

**Sous quinze pour cent de gazole, la jauge clignote.** Le rouge seul se confond avec
l'orange du palier au-dessus quand on a les yeux sur la route ; c'est le battement qu'on
voit du coin de l'œil.

**Le halo du gyrophare ne se fait plus trancher.** Sa bille de cinquante centimètres est
posée à cheval sur le toit de la cabine — elle descend à 4,18 m quand le toit plafonne à
4,47 — et le test de profondeur en découpait le tiers inférieur au couteau : on voyait un
demi-disque. Une lueur ne se découpe pas, elle déborde. Les optiques, elles, gardent le
test : un phare ne doit pas traverser le bâtiment devant lequel il est garé.

**Et le bouton d'achat de parcelle attend l'arrêt**, comme le bandeau de service. Le
panneau « à vendre » se voit à quatorze mètres, deux secondes de route : « PALIER ATTEINT —
3 PARCELLES » n'avait pas le temps d'être lu qu'il était déjà parti.

### Le barème : rendements et prix

Le jeu a reçu son **barème économique** — un tableau de rendements, de temps de pousse et
de prix par acheteur, écrit hors du code — et les tables du jeu s'y calent.

**Sept cultures, entre 110 et 140 kg la parcelle.** `kg` est ce que rend une cellule, et la
parcelle de départ en compte 552 : c'est elle, la parcelle standard du barème. Blé 120 kg
en 75 s, maïs 140 en 110, orge 130 en 95, avoine 125 en 90, colza 110 en 140 ; raisin 140
et olives 120, qui repoussent en 150 et 180 s. Une culture longue rend plus, mais pas assez
pour qu'on l'attende sans raison : c'est le prix qui décide, pas le rendement.

**La hiérarchie des acheteurs tient en cinq coefficients.** Le barème donne un prix par
produit et par commerce ; en les divisant les uns par les autres on retrouve toujours les
mêmes rapports — supermarché 1,00, marché 1,09, restaurant 1,28, spécialiste 1,33 et plus.
Ce sont donc des coefficients de site, et le prix de référence d'un produit est celui du
supermarché. Relevé, les prix obtenus tombent à deux centimes près sur le barème :

| | coop | supermarché | marché | restaurant | spécialiste |
|---|---:|---:|---:|---:|---:|
| blé | **0,50** | | | | |
| olives | | **1,03** | 1,12 | 1,32 | |
| raisin | | **0,95** | 1,04 | 1,22 | 1,26 caviste |
| farine | | **0,90** | 0,98 | 1,15 | 1,26 boulangerie |
| lait | | **0,53** | 0,58 | 0,68 | 0,75 laiterie |
| vin | | **2,71** | 2,96 | 3,47 | 3,61 caviste |
| huile d'olive | | **7,72** | 8,42 | 9,89 | |
| miel | | **2,75** | 3,00 | 3,52 | 3,85 boulangerie |
| laine | | | **1,97** | | 3,14 atelier textile |

**La coopérative est le plancher**, à 0,85, et elle ne prend que ce qui sort de la terre en
vrac. Le barème l'autorisait à prendre aussi le raisin, les olives et la laine : cela en
aurait fait un acheteur **strictement dominé** sur ces trois-là, le supermarché payant plus
et prenant plus, ce que le jeu s'interdit depuis toujours. Sa raison d'être est ailleurs —
elle est la seule à prendre les céréales, et elle en prend sept tonnes.

**Deux prix sont écrits à la main.** La formule des paliers — ×1,5 pour une transformation,
×2 pour un produit fini, ×2,5 pour une recette composée — manque la farine (elle en donnerait
1,22 là où le barème dit 0,90) et l'huile de colza (4,67 contre 3,41). On ne tord pas le
palier pour deux produits : ils portent un `tarif`, et un contrôle vérifie que **les
dix-neuf transformations paient toujours plus que vendre la matière** — la plus maigre à
+9 %, la plupart à +50 %.

### Chaque produit porte son unité

Le barème donne à chaque produit son **unité officielle** : le kilo pour un grain, le litre
pour un lait, une huile, un vin ou une bière, la pièce pour un œuf. Et il l'écrit noir sur
blanc : *ne jamais afficher le vin, le lait ou les huiles en kg.*

**Le jeu continue de tout stocker en kilos, et c'est ce qui rend le chantier sûr.** C'est le
kilo qu'une benne porte, qu'un silo compte et sur quoi s'appuie chaque recette. L'unité ne
sert qu'à deux choses : **afficher une quantité** et **afficher un prix**. Elle tient dans un
seul nombre par produit — `parKg`, combien d'unités officielles dans un kilo — et rien du
moteur ne la voit. Pas un nombre stocké ne bouge, donc **aucune sauvegarde n'a été reprise**
et pas un prix n'a changé de valeur : le contrôle relève blé 0,588, lait 0,53, huile 3,41,
exactement comme avant.

Pour les sept liquides, `parKg` vaut 1 — un litre de lait pèse un kilo, seule l'étiquette
change. C'est aussi ce qui fait tomber juste les rendements du barème sans toucher à un
chiffre : « 100 kg de colza → 34 L d'huile », « 100 kg de raisin → 70 L de vin ». Pour l'œuf,
`parKg` vaut 16,67 : un œuf pèse soixante grammes.

**Et la note sur les œufs disparaît.** Le prix n'est plus un équivalent bricolé à la main : on
écrit `parUnite: 0,20` — le chiffre du barème, à la pièce — et le prix au kilo s'en déduit,
3,33 €. Écrire 0,20 le *kilo* rendait une viennoiserie moins chère qu'un pain, l'échelle de
la boulangerie à l'envers ; la conversion était ce qui manquait, pas le chiffre.

**Trente endroits écrivaient une quantité ; aucun n'a à se demander laquelle.** Quatre
tournures suffisent, selon la phrase qui accueille le nombre :

| | |
|---|---|
| `qteNom` | « 34 L d'huile de colza » — au fil d'une phrase |
| `nomQte` | « Huile de colza 34 L » — sur une étiquette du monde |
| `nomQteBas` | « huile de colza 34 L » — dans une énumération |
| `qteNomHaut` | « HUILE DE COLZA 34 L » — sur un bouton d'action |

Toutes les quatre se taisent sur le nom **quand l'unité le porte déjà** : le bouton dit
« CHARGER 240 ŒUFS » et non « CHARGER ŒUFS 240 ŒUFS ». C'est le seul rôle d'un drapeau
`nomme` posé sur les œufs, et c'est ce qui évite d'y penser trente fois.

Le contrôle qui garde tout cela ne se contente pas de vérifier les helpers : il **ouvre les
douze écrans**, en relit le texte et cherche toutes les formes interdites — « 14 kg de lait »
comme « Lait 340 kg » — pour les huit produits concernés. Sur la version précédente il tombe
seize fois ; il relève au passage un « 13 kg de œufs » où l'élision manquait aussi.

**Ce qui reste à faire porte un nom.** La viande est le dernier produit qui se pèse à tort :
le barème la veut à la bête — « livrer 4 porcs », jamais « livrer 150 kg de porc » — et c'est
une unité qu'on ne peut pas poser aujourd'hui, puisqu'une carcasse de cochon et une de vache
ne font pas le même poids et que le jeu n'a qu'une viande générique. Cela se réglera avec
l'élevage, quand chaque espèce portera sa viande et son poids de carcasse.

Une chose devient visible du même coup : la commande de la boulangerie au palier 5 demandait
« 13 kg d'œufs ». Elle en demande **217**. La quantité n'a pas changé d'un gramme — c'est
l'affichage qui la disait mal. C'est le genre de chiffre que la refonte de la campagne aura à
reprendre, avec le barème des missions sous les yeux.

### Chaque graine a son prix et sa dose

Il n'y avait qu'un sac. On achetait « des semences » à 1,55 € le kilo, et le semoir y puisait
43 g par cellule quoi qu'il sème. Le barème en veut cinq, chacune avec son tarif et sa
quantité à la parcelle :

| | prix | dose / parcelle | coût | récolte | part |
|---|---:|---:|---:|---:|---:|
| blé | 0,18 € / kg | 25 kg | 4,50 € | 70,56 € | 23,4 % |
| maïs | 0,27 | 18 kg | 4,86 € | 107,09 € | 15,7 % |
| orge | 0,20 | 23 kg | 4,60 € | 84,11 € | 19,7 % |
| avoine | 0,22 | 22 kg | 4,84 € | 88,23 € | 19,1 % |
| colza | 0,36 | 12 kg | 4,32 € | 116,50 € | 14,0 % |

La dernière colonne compte aussi l'engrais. **Elle valait 62,5 % pour le blé** : semer et
fertiliser coûtaient les deux tiers de ce que la parcelle rendait, ce qui n'est pas une ferme
mais un péage. Le barème remet les intrants où ils doivent être — bien en dessous de ce que la
terre rend — et le colza, qui se sème le plus clair, reste le mieux payé au sac comme au kilo.

**Un hangar, plusieurs sacs.** Le stock n'est plus un nombre mais un tas par culture, dans un
hangar unique de 450 kg toutes graines confondues : on choisit encore ce qu'on stocke, ce
qu'un bac séparé par culture aurait supprimé. Le semoir puise dans le sac de la culture qu'il
sème et dans aucun autre — le contrôle le vérifie sac par sac, avec un témoin à côté.

**La vigne et l'oliveraie ne se sèment pas.** Elles se plantent, une fois, et repartent seules
après chaque récolte : 1 600 € la parcelle de vigne, 1 200 € l'oliveraie, payés à la cellule
au fur et à mesure que le semoir avance. Il n'y a pas de sac à remplir, et il n'y en aura
jamais — c'est le sens même d'une culture permanente. Si la bourse se vide en cours de rang, la
plantation s'arrête où elle en est, exactement comme un sac vide arrête un semis.

**L'engrais passe de 2,22 € à 0,80 € le kilo**, et de 20 kg à 15 par parcelle : douze euros
pour un quart de pousse en moins sur une récolte qui en vaut soixante-dix. Il reste facultatif
— aucune mission ne l'exige — mais à ce tarif-là on comprend pourquoi on le prend.

**Le gazole vaut 2,00 € le litre**, le prix de référence du barème, et 1,60 € livré en gros
dans la cuve de la ferme. Les réservoirs ont fondu de moitié et la soif avec, dans le même
rapport : tracteur 40 L à 0,8 L/min, moissonneuse 60 à 1,2, enjambeuse 50 à 1,0, pick-up 45 à
0,6, fourgon 70 à 0,8. Chaque engin tient donc **cinquante minutes** de travail à pleine
charge, contre trente avant, et le pick-up une heure et quart puisqu'il ne tire rien. Ce n'est
pas une simulation : c'est une petite dépense de fonctionnement, et elle ne doit pas devenir
punitive.

Rien de tout cela n'oblige à recommencer une partie. Une sauvegarde d'avant le barème n'a
qu'un seul tas de graines : il devient du blé, la seule culture que tout le monde possède et
celle dont la dose est la plus proche de l'ancienne — vingt-cinq kilos la parcelle contre
vingt-quatre.

Le contrôle qui garde ce barème mesure les trente-quatre chiffres sur pièces : il sème une
parcelle entière de chaque culture et pèse le sac avant et après, plante une vigne et compte
les euros, vide une bourse pour voir la plantation s'arrêter, et relit l'enseigne du comptoir
pour vérifier qu'elle annonce bien la graine la moins chère. Sur la version précédente, il
tombe trente et une fois.

### On garde son matériel, on l'améliore

Il y avait **un seul bouton** au garage, et il achetait tout à la fois : l'engin *et* l'outil
qu'il tire, vitesse ×1,18, largeur ×1,22, capacité ×1,4, pour une somme unique. On ne pouvait
ni savoir ce qu'on payait, ni n'améliorer que le semoir. Trois crans, et c'était fini.

Chaque matériel a maintenant **son échelle écrite**, avec ce que chaque cran donne et ce qu'il
coûte, et **chacun s'achète seul** :

| | ce qui monte | crans | prix |
|---|---|---|---|
| tracteur (vert, rouge, bleu) | vitesse | 100 · 112 · 125 · 140 · 155 % | 600 · 1 800 · 4 500 · 9 000 € |
| charrue | largeur | 100 · 125 · 155 · 190 % | 700 · 2 000 · 5 000 € |
| semoir | largeur | 100 · 125 · 155 · 190 % | 800 · 2 500 · 6 000 € |
| épandeur | largeur | 100 · 130 · 165 · 200 % | 750 · 2 200 · 5 000 € |
| moissonneuse | vitesse, trémie, coupe | 150 · 250 · 450 · 800 kg | 1 500 · 4 500 · 10 000 € |
| enjambeuse | vitesse, capacité | 120 · 220 · 400 · 700 kg | 1 800 · 5 000 · 11 000 € |
| pick-up | capacité, vitesse | 150 · 250 · 400 · 600 kg | 700 · 2 200 · 5 000 € |
| fourgon | capacité, vitesse | 600 · 900 · 1 400 · 2 200 kg | 1 600 · 4 500 · 9 000 € |
| benne | capacité | 200 · 350 · 550 · 850 kg | 600 · 1 800 · 4 200 € |

**Un pourcentage porte sur le NEUF, jamais sur le cran précédent.** 140 % veut dire 140 % du
neuf, quel que soit le chemin par lequel on y est arrivé — le contrôle monte au maximum et
redescend trois fois de suite pour vérifier que rien ne dérive.

**Il n'y a plus de gros tracteur à acheter.** C'est le principe même du cahier des charges :
on garde son matériel. Les deux tracteurs qui s'achetaient aux paliers 4 et 9 sortent du
catalogue ; leurs deux entrées restent en place dans la table, parce que la sauvegarde
sérialise les engins **par position** et que les retirer ferait repartir chaque partie en
cours sur la mauvaise machine. Une partie qui en possède déjà un le garde et le conduit.

**La barre de coupe s'allonge vraiment.** À 180 % elle passe de huit à quatorze mètres, et
c'est la première chose qu'on voit d'une moissonneuse améliorée. Le tunnel de l'enjambeuse, à
l'inverse, ne bouge plus : il enjambe **un rang**, et un rang de vigne ne s'élargit pas parce
qu'on a payé. La direction non plus ne s'achète plus — l'ancienne amélioration ajoutait 6 % de
braquage à chaque cran, et la conduite changeait sous les doigts sans qu'on l'ait demandé.

**La sauvegarde ne stocke plus qu'un numéro de niveau.** Elle portait des valeurs *dérivées* —
vitesse, accélération, largeur, capacité — parce que l'ancienne amélioration les accumulait et
qu'il n'existait nulle part de table pour les retrouver. Une source de vérité au lieu de deux :
le contrôle abîme exprès la capacité écrite dans la sauvegarde (7 kg pour un pick-up de
niveau 3) et vérifie qu'elle revient à 400. C'est aussi ce qui met d'office les parties en
cours sur les nouvelles valeurs, au lieu de leur laisser les anciennes pour toujours.

Les capacités de niveau 1 viennent de cette même table : trémie 150 au lieu de 100, benne de
pick-up 150 au lieu de 70, remorque 200 au lieu de 135. Deux endroits qui disent la capacité
d'un matériel neuf finissent toujours par diverger.

### Le semoir perd vraiment les graines qu'il sème

Il puisait dans le hangar de la ferme, depuis l'autre bout de la vallée. Il **porte**
maintenant ce qu'il sème : 50 kg au neuf, 350 au dernier cran, soit deux parcelles de blé
contre quatorze. C'est la seule amélioration du jeu qui se compte en allers-retours épargnés,
et c'est ce qui donne enfin un sens à la capacité du barème.

#### Un sac par semence, et non une cuve pour tout

La cuve ne mélangeait pas : elle contenait **une** graine, comme une benne contient une seule
nature. Changer de culture renvoyait ce qui restait au hangar — et si le hangar était plein,
le réglage était **refusé**, pour ne pas jeter vingt kilos de blé. C'était prudent, et c'était
un piège, dont le joueur est tombé dedans mot pour mot :

> « Quand je choisissais avec le semoir, maïs, la capacité était vide, et maintenant j'essaye
> de revenir dessus, j'arrive plus à sélectionner le maïs. »

La chaîne, reconstituée : il achète du maïs au comptoir ; le semoir porte encore du blé ; le
transvasement veut d'abord rendre ce blé au hangar ; le hangar est presque plein ; le
transvasement échoue, le maïs reste au hangar, **et le semoir n'est pas réglé sur le maïs** —
d'où la « capacité vide ». Puis il touche le bouton de culture pour y aller lui-même : le
bouton appelle le même transvasement, échoue sur le même hangar plein, et **rend la main sans
changer de culture**. Il est bloqué sur le blé avec du maïs acheté qu'il ne peut pas semer.

Le semoir porte donc maintenant **un casier par semence**, chacun plafonné à `cuveMax` :
cinquante kilos de blé ET cinquante kilos de maïs à bord, comptés séparément. Le joueur l'a
demandé en propre : « fais bien en sorte qu'on puisse sélectionner le type de graines, tout en
gardant le même semoir, et qui a un décompte de la capacité différent pour chacune des
semences. »

Changer de culture ne déplace donc plus un gramme, et **ne peut plus échouer**. Le bouton dit
au passage ce qu'il y a dans le sac où l'on vient d'arriver. Vider reste possible, sur la cour
ou au comptoir : *Vider le semoir* rend **tous** les sacs.

La sauvegarde écrit le dictionnaire `cuves` **et** l'ancien couple `cuveQ`/`cuveCle`, qui porte
le casier courant — une version plus ancienne du jeu relit donc une partie neuve sans rien
comprendre au reste, et une partie d'avant les casiers se relit en reconstituant le sien. La
version de sauvegarde ne bouge pas : la garde de relecture est une égalité stricte, et
l'incrémenter rejetterait d'un coup toutes les parties en cours.

**Et la place d'achat, c'est le hangar PLUS le casier.** Elle ne comptait que le hangar — or
le hangar est un plafond *commun* à toutes les graines. Hangar plein de blé, le guidage disait
« ACHETER LA SEMENCE — MAÏS », on allait au comptoir, et le rayon répondait « Hangar plein » :
un ordre inexécutable, et la mission bloquée. L'achat sert pourtant la cuve dans la foulée, ce
qui passe par le hangar n'y reste qu'un instant. On compte donc aussi le casier que l'outil
peut recevoir — et seulement s'il y a un outil pour le recevoir, sans quoi le hangar
déborderait pour de bon. Hangar plein **et** casier plein, l'achat est toujours refusé : le
plafond veut encore dire quelque chose.

**Et un cran d'amélioration ne détruit plus de graine.** Le code disait « le trop-plein
retourne quand même au hangar plutôt que de s'évaporer » et faisait
`Math.min(trop, grainesPlace())` : ce qui dépassait la place **disparaissait**. Mesuré sur une
sauvegarde abîmée portant 1 200 kg dans un casier de 50 : **1 150 kg évaporés**. Ce qui ne
tient nulle part reste maintenant dans le casier — il se videra au premier transvasement, là
où une graine détruite ne revient pas — et `grainesPlace()` est relu à chaque casier, sans quoi
deux casiers se partageraient deux fois la même place.

Le banc `cuves.js` compte **40 contrôles** depuis ce chantier, contre 25, et huit d'entre eux
énoncent ce que l'ancien contrat interdisait.

On remplit sur la **cour de la ferme** — c'est là que sont le hangar et le parc à outils, donc
là qu'on attelle — et au **comptoir agricole**, où l'on vient acheter : on repart chargé au
lieu de refaire le trajet.

**Le semoir part plein.** Le jeu commence à zéro euro et donne de quoi faire un aller-retour
complet dès la première minute ; un semoir vide, avec un hangar qu'on n'a pas les moyens de
vider dans une cuve qu'on ne sait pas encore remplir, ferait échouer la première mission sans
rien expliquer. Cinquante kilos de blé dedans, dix-huit au hangar : deux parcelles, ce qu'il
faut très exactement pour la première mission et la suivante.

Le bouton de culture porte **le nom et une jauge**, et **passe au rouge à zéro**. Depuis que
le semoir porte ses graines, tomber en panne au milieu d'un rang est possible ; le seul endroit
où l'on regarde en semant, c'est ce bouton, et c'est donc là que la cuve doit se lire. Elle s'y
lisait en chiffres — « BLÉ 47 », « BLÉ 46 », « BLÉ 45 », un nombre qui défile à chaque cellule
semée, et c'est justement ce qu'on ne peut pas lire en conduisant. Une barre de trente-six
pixels dit la même chose sans qu'on ait à la lire, et dit en plus la **part** de cuve, ce que
le chiffre nu ne disait pas. Le message qui suit ne dit pas la même chose selon ce qui manque :
*remplir au comptoir* si le hangar a de quoi, *acheter des semences* s'il est vide lui aussi.

### L'élevage se compte à la bête

Acheter une étable ne donne pas « du lait ». Chaque animal produit et mange **pour lui**, et
deux vaches donnent deux fois plus qu'une. Le barème écrit ce que fait UNE bête sur UN cycle :

| | par cycle | aliment | ce qu'un kilo de grain rend |
|---|---|---:|---:|
| poule | 2 œufs | 0,25 kg | ×2,7 |
| vache | 25 L de lait | 2 kg | ×11 |
| brebis | 2 kg de laine + 10 L de lait | 1 kg | ×19 |
| mouton | 2 kg de laine | 0,8 kg | ×7,7 |
| ruche | 2 kg de miel / 90 s | — | passive |

La dernière colonne compare ce que le grain vaut **donné à une bête** contre **vendu tel
quel**. C'est très exactement l'ordre dans lequel la campagne ouvre les trois élevages, et
c'est ce qui fait qu'on ne vend pas son blé quand on a des bêtes à nourrir. Les prix suivent
le barème : poule 30 €, brebis 180, cochon 220, vache 600, ruche 250.

**Le cycle vaut cinq minutes** pour tout ce qui mange, et c'est ce qui rend l'autonomie
comparable d'une espèce à l'autre : une mangeoire de quatre cycles tient vingt minutes, qu'elle
nourrisse six poules ou dix vaches. La ruche garde les quatre-vingt-dix secondes du barème, ce
qui ne gêne personne puisqu'elle ne se remplit pas — **les abeilles se nourrissent seules**,
c'est une activité passive, et on leur comptait jusqu'ici du sirop dans une mangeoire.

**La mangeoire se dimensionne sur le troupeau, et non l'inverse.** Elle valait 235 kg pour tout
le monde : de quoi tenir trois jours avec deux poules et une demi-heure avec quatorze vaches.
Sa capacité est maintenant

> consommation par bête et par cycle × nombre de bêtes × autonomie

et l'amélioration n'augmente pas une capacité arbitraire — elle augmente **l'autonomie** :
4, 6, 10 puis 16 cycles, à 500, 1 500 et 4 000 €. Dix vaches à quatre cycles font 80 kg ; les
mêmes à dix cycles en font 200. Ce sont les deux chiffres que le cahier des charges donne en
exemple, et le contrôle les vérifie sur la formule elle-même.

**Le tank suit la même règle.** Une cuve de 50 L n'a pas de sens quand dix vaches produisent
250 L par cycle : la capacité est ce que le troupeau sort en quatre cycles, et elle grandit
avec lui — 100 L pour une vache, 1 000 pour dix. Le miel en garde six, comme dit le barème.

**Le bâtiment a sa propre échelle**, indépendante de l'autonomie : on agrandit son étable bien
avant de vouloir passer trois fois moins souvent, et le barème leur donne des prix séparés
pour cette raison.

| | places | prix |
|---|---|---|
| poulailler | 6 · 12 · 20 · 32 | 600 · 1 500 · 3 500 € |
| étable | 2 · 5 · 10 · 20 | 1 500 · 4 000 · 9 000 € |
| bergerie | 4 · 8 · 16 · 30 | 900 · 2 500 · 6 000 € |
| porcherie | 4 · 8 · 16 · 30 | 1 200 · 3 200 · 7 500 € |
| zone apicole | 2 · 5 · 10 · 20 | 700 · 2 000 · 5 000 € |

La **parcelle** reste le dernier mot : un enclos de vingt ares ne tient pas vingt vaches quoi
qu'on paie, et c'est ce qui empêche d'entasser un troupeau sur un mouchoir.

Une partie en cours peut avoir plus de bêtes que le premier cran n'en autorise — quatorze
vaches là où l'étable neuve en tient deux. On ne reprend pas un troupeau au joueur : le
bâtiment monte au cran qui le contient, celui qu'il aurait payé s'il l'avait acheté.

Un défaut trouvé en chemin, invisible à l'œil : le **second tank d'une brebis** était écrit
sous un `if` sans accolades, donc hors de la garde qui vérifie que les bêtes ont mangé. Il ne
s'en voyait rien — la ligne multiplie par le nombre de bêtes nourries, donc elle ajoutait
zéro — mais toute condition ajoutée devant aurait cessé de le couvrir.

Et une commande de la campagne a dû suivre : la boulangerie demandait « 13 kg d'œufs », ce qui
fait **217 œufs** une fois qu'on les compte, et une heure et demie de ponte avec un poulailler
plein. Le cahier des charges donne lui-même l'exemple d'une commande de **cent** œufs ; c'est
l'échelle juste, et c'est celle-là. La refonte de la campagne reprendra les trente commandes
ensemble — celle-ci ne pouvait pas attendre, elle bloquait le palier 5.

### Un cochon ne vieillit pas, il engraisse

Les autres bêtes grandissent à l'horloge — une vache donne du lait pendant ce temps-là, ce qui
n'est pas la même économie. Le cochon, lui, ne produit rien : il **mange**, et c'est ce qu'il a
mangé qui le rend prêt. Vingt-cinq kilos d'aliment, dit le barème. Deux cochons dans un enclos
vide n'engraissent plus d'une seconde, et quatre bien nourris sont prêts en même temps.

**Et la boucherie paie à la bête.** Elle payait déjà le bon prix, mais par un détour : on
convertissait l'animal en kilos de carcasse, on multipliait par le prix du kilo de viande, et
l'on retombait — à l'arrondi près — sur le prix de la bête fois deux. Le cahier des charges
veut qu'on ne pèse jamais une viande : « livrer 4 porcs », jamais « livrer 150 kg de porc ».
On paie donc la tête, directement. La ligne qui suivait, censée compter la viande livrée, ne
comptait rien du tout : sa clé n'est pas dans la table des compteurs, et elle retombait dans le
vide depuis toujours.

### Livrer une commande n'est pas vendre

On arrivait à la coopérative avec cent kilos de blé pour une commande de trente, et l'on
repartait les mains vides. Le stock qu'on avait mis de côté pour le moulin partait avec le
reste, sans qu'on l'ait voulu.

**Une commande prélève exactement ce qu'elle attend encore.** Trente kilos demandés, cent à
bord : trente partent, **soixante-dix restent dans la benne**. Et ce que le client attend
encore, c'est *demandé moins déjà livré*, jamais le total initial — soixante kilos livrés sur
cent, et la ligne annonce d'elle-même « LIVRER LA COMMANDE — BLÉ 40 KG » au retour. Le commerce
garde ce qu'il a reçu ; on ne refait jamais une livraison complète.

Les deux gestes coexistent devant un commerce qui a une commande en cours, et c'est la
distinction que le cahier des charges demande :

| | |
|---|---|
| **LIVRER LA COMMANDE** | la quantité est celle du client, exacte, sans curseur |
| **VENDRE** | le joueur choisit combien, au curseur, jusqu'au dernier kilo |

La commande passe la première — c'est ce qu'on est venu faire — et la ligne du dessous reste là
pour qui veut tout écouler.

La borne se relit **à chaque image** plutôt que d'être calculée une fois : le crédit de la
livraison vient d'en retirer ce qu'on a versé, donc elle fond au même rythme et le transfert
s'arrête pile. Rien n'a été ajouté au moteur de transfert — c'est le même code qui vend, verse
et charge, avec un plafond de plus.

Deux commandes de blé au même quai ? Une seule livraison les crédite toutes les deux, donc on
prépare **la plus grosse**. Et la mission de campagne du moment compte comme une commande : elle
prend ses trente kilos et laisse les autres.

### Quatre couleurs, un seul juge

Le joueur doit comprendre en quelques secondes où prendre une mission, quoi faire *maintenant*
pour celle qu'il a acceptée, et quels lieux restent ouverts en permanence. Trois questions,
trois couleurs, et une quatrième pour tout le reste :

| | |
|---|---|
| **JAUNE** | l'objectif du moment — « je dois aller ICI, maintenant » |
| **VERT** | une mission à prendre |
| **BLEU** | un service permanent : comptoir, garage, coopérative |
| **GRIS** | un lieu connu dont on n'a rien à faire à cet instant |

La priorité est stricte : **jaune > vert > bleu > gris**. La coopérative est bleue, mais si la
mission demande d'y livrer du blé elle passe au jaune, et redevient bleue une fois la commande
soldée. Un seul endroit tranche — `couleurGuide` — et tout ce qui affiche une couleur la lui
demande : les pastilles au sol, les flèches du bord. Deux écrans qui décideraient chacun de leur
côté finiraient par se contredire.

La pastille au sol ne disait qu'une chose et elle était verte : « il y a une mission ici ». Elle
porte maintenant les trois sens, et le joueur n'a plus qu'un signal à apprendre. Un service bleu
reste **plus petit et ne respire presque pas** : c'est une possibilité, pas une obligation.

**Et le jaune est dynamique.** Il ne suit aucun script : il regarde l'état réel de l'exploitation
et désigne l'endroit *le plus avancé* qui rapproche du résultat.

| l'état | l'objectif |
|---|---|
| la benne porte de quoi | livrer chez le client |
| le silo ou l'entrepôt en a | aller charger |
| l'atelier en fabrique | c'est là que ça sort |
| l'atelier a la matière | lancer la production |
| un champ est mûr, un tank est plein | récolter, collecter |
| il manque la graine | comptoir agricole |
| il manque le matériel | garage |

C'est l'exemple du cahier des charges, à la lettre : la moissonneuse verse trente-cinq kilos au
silo, le compte y est, **le champ perd son cercle et le silo l'allume** — sans qu'on ait à finir
le champ. Rien n'est mémorisé d'un appel à l'autre ; c'est relu, donc ça ne peut pas mentir.

Pour une farine dont on n'a pas un grain de blé, l'objectif n'est ni l'atelier ni la boulangerie :
c'est le **champ**. Le résolveur remonte la recette d'un cran — l'ingrédient dont on manque le
plus — et redemande d'où il sort.

**Le matériel indispensable, jamais le confort.** Sans enjambeuse on ne récolte pas d'olives : le
garage passe au jaune. Avec une enjambeuse de niveau 1, on récolte plus lentement — le garage
reste bleu, et la mission ne demandera jamais de l'améliorer.

Le bord de l'écran suit la même règle et **ne se sature pas** : la flèche jaune de l'objectif,
puis au plus trois missions vertes, les plus proches. Aucune flèche bleue en permanence — les
trois services ne sont pas là pour encombrer.

**La carte parle la même langue**, et elle le dit par-dessus : les points de navette sont tous
du même bleu clair — c'est leur rôle, on les touche pour composer un trajet — et une pastille
posée dessous disparaissait sous eux. Le guidage est donc une **couronne** autour du point : elle
ne cache rien, elle qualifie. L'objectif du moment y figure même quand ce n'est pas un commerce —
un champ, le silo, l'atelier. Une légende de trois points sous la carte, pas un panneau.

**Le bandeau dit le résultat ET l'étape.** Le titre porte ce que le client veut, une ligne jaune
en dessous porte ce qu'il faut faire maintenant et à quelle distance. C'est le même jaune qu'au
sol et au bord de l'écran, et c'est le même calcul : trois surfaces, un seul juge.

Deux mesures ont tranché deux hésitations. La première : mettre l'objectif en mémoire un dixième
de seconde pour éviter de le recalculer soixante fois par seconde. Chronométré, il coûte **une
microseconde et demie** par appel — un dix-millième d'image. La mémoire ne faisait rien gagner et
coûtait cher : après avoir versé au silo, l'objectif restait faux le temps qu'elle expire. Elle a
sauté. La seconde : la ligne d'objectif ajoute **dix-neuf pixels** au bandeau, qui passe de 5,4 %
à 6,1 % de l'écran dans le pire cas — quatre contrats et une mission ensemble. C'est ce que vaut
le fait de savoir où aller, et l'on reste loin des 10,6 % dont ce banc est né.

### Le bouton prend la couleur de son cercle

Les cercles au sol disaient déjà trois choses — jaune la chaîne de la mission, vert quelque
chose à prendre ici, bleu un service permanent — et **les boutons qui s'ouvraient dessus
étaient ambre quoi qu'il arrive**. On arrivait au garage sans pouvoir dire, sans lire, si
l'achat qu'on venait faire était l'étape jaune d'une mission — le pulvérisateur — ou une
emplette ordinaire. Le vert était pire : il ne servait qu'à la ligne du contrat, mais le
bouton *ACHETER* du garage était vert lui aussi, alors que vert veut dire « une mission à
prendre » partout ailleurs.

La couleur du bouton est maintenant **celle du cercle sous les roues**. On la voit du
cercle, on la retrouve sur le bouton, et il n'y a rien de plus à apprendre.

| ce qu'on lit | ce que ça veut dire |
|---|---|
| **jaune** | la mission t'envoie ici, et c'est ce bouton qu'elle attend |
| **vert** | il y a quelque chose à prendre : un contrat, une mission |
| **bleu** | un service ordinaire — tu es venu de toi-même |

On lit **le cercle le plus proche**, et non le lieu : la colonne de choix s'ouvre aussi bien
sur un commerce que sur le silo, l'entrepôt, une pâture ou l'atelier, et il aurait fallu
savoir sur lequel on se tient. Ce savoir est déjà posé au sol — chaque cercle connaît sa
position, sa condition d'allumage et sa couleur du moment — et le lire là a l'avantage de ne
pouvoir **jamais mentir** : si le bouton et le cercle divergeaient, ce serait exactement le
défaut qu'on cherche à corriger.

Trois états gardent leur couleur, parce qu'ils ne parlent pas du *lieu* : le **gris** de ce
qui est empêché ou impayable — c'est un état, « je ne peux pas », et c'est la seule
distinction qui compte au moment d'appuyer — l'**aplat plein** d'un transfert en cours, et
l'**effacé** du bouton retour. La teinte entre dans la signature qui décide de repeindre la
colonne : sans elle, un panneau déjà peint resterait figé au moment où le cercle passe du
bleu au jaune.

**Le garage a deux boutons et un seul cercle.** Quand la mission y envoie chercher
l'épandeur, le cercle passe au jaune — mais c'est *ACHETER* qu'elle attend, pas *AMÉLIORER*.
Les teindre tous deux les rendrait indiscernables. Aucune mission de la campagne ne demande
une amélioration — « une mission ne demande jamais un confort » — donc *AMÉLIORER* est
**toujours bleu**, et *ACHETER* ne prend le jaune que si l'objectif du moment vise vraiment
le matériel. Deux façons de le savoir, et il faut les deux : une étape guidée le dit par la
fenêtre qu'elle vise, un objectif ordinaire par ce qu'il cherche. L'achat de parcelle, qui
n'a pas de cercle — c'est un bord de champ, pas un quai — est bleu par la même règle : ce
n'est jamais une étape de mission.

### On travaille le champ tant que la ferme n'a pas le compte

*« Je veux vraiment que tu l'aies compris : on travaille le champ tant qu'on n'a pas assez
de blé dans le silo ; dès le moment qu'on a assez de blé dans le silo, on doit livrer. Si on
a récolté suffisamment pour que, ajouté à ce qu'il y a dans le silo, ça équivaille à ce dont
on a besoin, il faut que ça nous demande d'aller emmener le blé déjà récolté dans le silo,
même si le champ n'est pas fini de récolter. »*

Le jeu faisait le contraire, et cela tenait à un seuil : `auSilo > 0.5`. Un demi-kilo au fond
du silo suffisait à faire dire CHARGER. Mesuré sur la première mission — trente kilos de blé
à la Coopérative — un silo à **un kilo** faisait afficher *CHARGER BLÉ 1 KG* : l'aller-retour
pour un trentième de la commande, alors que le champ n'était pas coupé.

La règle est maintenant celle-là, dans cet ordre :

| l'état de la ferme | ce que dit le jeu |
|---|---|
| ce qu'on porte, tous engins confondus, suffit | **LIVRER** au commerce |
| silo + entrepôt + ce qu'on porte soldent la ligne | **CHARGER** au silo, puis livrer |
| + la trémie de la moissonneuse soldent la ligne | **VIDER AU SILO**, champ non fini |
| rien de tout cela | **AU CHAMP** |
| et la ferme ne peut plus rien produire | livrer ce qu'on a, plutôt qu'attendre en vain |

Le seuil se mesure : silo 29 → au champ, silo 29,99 → au champ, silo 30 → charger. Silo 4 et
trémie 25 → au champ ; silo 4 et trémie 26 → *VIDER AU SILO — BLÉ 26 KG*, et la chaîne du
bandeau tombe de « champ ▸ silo ▸ Coopérative » à « silo ▸ Coopérative » : le champ perd son
cercle jaune au milieu d'une moisson, ce qui est exactement ce qui était demandé.

Deux trous ont été trouvés après coup, et corrigés :

- **le juge ne comptait que l'engin piloté.** Trente kilos de blé dans le pick-up garé, on
  remonte dans la moissonneuse, et il redemandait d'aller récolter du blé déjà rentré. Le
  compte se fait sur toute la cour ; sept `caisseDe` de plus par appel, et le juge coûte
  pourtant 1,23 µs contre 1,45 avant — la porte du compte court-circuite plus qu'elle
  n'ajoute ;
- **la règle ne valait que pour le chemin du silo.** Hors céréales, un tank momentanément
  vide faisait tomber dans le filet de fin : pour une commande de deux cents litres de lait,
  cinq litres oubliés à l'entrepôt donnaient *CHARGER LAIT 5 L* — le même défaut, vivant dans
  une autre filière. Un enclos qui sait produire la marchandise reste l'objectif, tank vide
  compris : il se remplit tout seul.

**Et deux missions n'avaient aucun objectif du tout.** « Produire 184 kg d'aliment premium »
et « Livrer quatre porcs » n'ont pas de lieu ; le juge cherchait un commerce de ce nom, n'en
trouvait pas, et rendait null sur toute leur durée — pas un cercle au sol, pas une flèche,
pas une ligne au bandeau. L'aliment premium se lit maintenant comme n'importe quelle
marchandise, par la même chaîne : la semence qui manque, puis le mélangeur, puis la
production. Les porcs, qui n'ont pas de clé de produit, désignent l'enclos quand il y a des
bêtes à charger et la boucherie sinon.

### L'ordre est : la culture, la graine, puis le champ

Au quatrième palier, la mission demande 180 kg de maïs. Le joueur :

> « La mission ne m'a pas dit d'aller au comptoir agricole alors que j'avais pas encore de
> maïs, on m'a déjà direct demandé de livrer, ça va pas. Il faut qu'on me demande dans un
> premier temps d'aller acheter le maïs que je n'ai pas encore, c'est la suite logique, puis
> après cultiver mon terrain avec le maïs, puis après on continue. »

**Deux verrous étaient invisibles au juge.** Le premier : `CROPS[i].verrou`, le droit de
semer la culture — personne dans `origineFerme` ne le regardait, donc rien ne l'annonçait, et
`outilManquant` ne le connaissait pas non plus. Le second : `parcelleDe` rend `null` quand
toutes les parcelles portent une *autre* culture, si bien que la porte de la semence, gardée
par `champ.quoi === 'semer'`, ne s'ouvrait jamais. La chaîne rendait `null` — non parce
qu'elle était épuisée, mais parce que deux verrous la coupaient — et le **filet de fin**
traduisait « rien à faire » par « livre ce que tu as » : *LIVRER 180 KG DE MAÏS*, avec zéro
kilo de maïs dans toute la ferme.

L'ordre est maintenant écrit, et c'est celui que le joueur décrit :

| l'état de la ferme | ce que dit le jeu |
|---|---|
| la culture n'est pas acquise, et le palier est atteint | **ACQUÉRIR LA CULTURE** au comptoir |
| acquise, mais pas de graine, et rien de cette culture en terre | **ACHETER LA SEMENCE** au comptoir |
| pas la machine qu'il faut — moissonneuse, enjambeuse, **ou semoir** | **IL FAUT…** au garage |
| une terre à travailler | **AU CHAMP** |
| plus de terre, mais une friche à vendre au palier | **IL FAUT UNE PARCELLE** |
| plus de terre du tout | **LIBÉRER UNE PARCELLE** |

La condition « la parcelle doit déjà être prête à semer » a disparu : on achète la graine
**avant** de préparer la terre, ce qui est l'ordre dans lequel on travaille. On ne l'achète en
revanche pas quand cette culture pousse déjà ou attend la moissonneuse — c'est elle qu'il faut
aller chercher, pas un sac de plus.

Et le filet de fin ne ment plus. Il livre toujours un stock **partiel** — « une livraison
partielle vaut mieux qu'un objectif qu'on ne peut pas atteindre » reste la règle — mais une
livraison de rien du tout n'est pas une livraison partielle, c'est un mensonge : quand la
ferme détient zéro kilo partout, silo, entrepôt et bennes comprises, il ne dit **rien**. La
flèche s'éteint et le bandeau se tait. C'est désagréable, et c'est vrai.

#### Et dix missions sur trente n'avaient aucun objectif

Une contre-lecture adverse a parcouru les trente missions sur une ferme neuve, et en a
trouvé **dix** qui rendaient `null` : les œufs du quatrième palier, le lait du huitième, les
fromages, la laine, le miel. Pas un cercle au sol, pas une flèche, pas une ligne au bandeau,
pour un tiers de la campagne — et la deuxième mission après le maïs.

La cause tient en une ligne : `origineFerme` cherchait `CROPS[CROP_DE[cle]]`, qui n'existe ni
pour un œuf ni pour du lait, et rendait `null`. Les deux passes qui précèdent ne parlaient
qu'aux enclos **déjà posés**. Un produit d'élevage suit maintenant le même ordre qu'une
culture : le palier, puis l'enclos à aménager sur une terre à soi — le bouton du bandeau y
fait défiler les espèces — puis la bête à acheter à son quai. Mesuré après : **zéro mission
sans objectif sur trente**.

Le banc `guidage.js` compte **76 contrôles** depuis ce chantier, contre 69, et l'un des sept
nouveaux parcourt la chaîne du maïs de bout en bout : culture non acquise → *ACQUÉRIR*,
acquise et sans graine → *ACHETER LA SEMENCE*, semoir verrouillé → *IL FAUT LE SEMOIR* (onglet
**Outils** du garage, pas Véhicules), graine achetée → *AU CHAMP*, et jamais *LIVRER*.

### Une seule étiquette au quai

À la livraison, **trois** choses disaient le même poids de blé dans le même coin de l'écran :
l'enseigne du commerce, qui annonce ce que la mission attend ; la jauge du bandeau, qui porte
le chargement en permanence ; et une jauge flottante posée au-dessus de l'engin, qui répétait
la seconde à côté de la première — 126 pixels d'écart sur un écran de 1 200, même famille de
plaque, mot pour mot le même texte.

La troisième est **supprimée**, et non éteinte : un objet qu'on garde invisible coûte encore
son parcours de scène et revient au premier réglage distrait. Rien n'est perdu — le bandeau
porte le poids, la nature et la couleur, et il reste lisible quand la caméra ne cadre pas la
machine. Les étiquettes de **lieu** restent toutes : le silo, l'atelier, l'entrepôt, la cuve,
les enclos et les parcelles nomment ce qu'on ne peut pas lire autrement.

### Là où la mission t'envoie, il n'y a que la mission

On arrivait à la Coopérative avec les trente kilos du tutoriel et l'on y trouvait **deux
boutons** : *VOIR LA MISSION* en vert, et *VENDRE BLÉ · 0,50 € / kg · 30 kg* juste dessous —
le second bradant à moitié prix, en un geste, précisément la marchandise que le premier
attendait. Le joueur guidé n'a pas à arbitrer entre les deux.

La vente en vrac est donc retirée **au lieu de l'étape en cours**, et là seulement. Ailleurs,
rien ne change : c'est même pour elle qu'on repasse à la Coopérative entre deux livraisons,
et le marchand l'a promis en payant la première — *« je prends ce que vous avez »*. Une
**livraison de contrat** n'est pas une vente en vrac : c'est le geste que la mission attend,
et c'est justement celui qu'on garde.

Pendant le tutoriel, le bouton dit **le geste, pas le mot « mission »** : *VENDRE 30 KG DE
BLÉ*. On n'a pas encore appris qu'il existe des missions — on est venu vendre son blé, et
c'est en le vendant que le marchand se présente et propose la première commande. La fenêtre
qui s'ouvre derrière est la même.

### Le chemin bat jusqu'à la ligne qu'il faut toucher

*« Quand il faut faire évoluer l'atelier pour acheter le moulin à farine, je veux que le
bouton pour la production pulse en jaune, et à l'intérieur l'onglet pour acheter le moulin
pulse en jaune aussi. Fais des pulsations vraiment visibles, pareil à chaque fois pour
toutes les actions. »*

Le battement des menus existait déjà — le bouton du parc bat, on l'ouvre, la ligne de la
machine bat à son tour — mais **seulement pendant le tutoriel**, qui écrit lui-même sa cible
dans sa table : la fenêtre, l'onglet, la ligne. Passé le premier quart d'heure, plus rien ne
battait.

**Une mission ne peut pas écrire sa cible.** Il y en a trente, et l'objectif change tout
seul avec l'état de la ferme. On la **déduit** donc du juge, qui porte déjà ce qu'il cherche
et sur quoi :

| ce que l'objectif cherche | ce qui bat |
|---|---|
| un métier d'atelier qui manque | Production · Métiers · la ligne du moulin |
| un lot à lancer | Production · Produire · la ligne du produit |
| une semence | Comptoir · Semences · la ligne de la culture |
| un engin qui manque | Acheter · Véhicules · la ligne de la machine |

Le bouton de régie, le bouton du garage, l'onglet et la ligne lisent tous la **même**
fonction : s'ils divergeaient, ce serait exactement le défaut qu'on corrige. Et chacun
s'éteint dès qu'on y est — le bouton quand la fenêtre est ouverte, l'onglet quand c'est
celui qu'on regarde — sans quoi deux appels battraient l'un sur l'autre.

**Le moulin à farine était le cas type, et il était pire que discret.** La quatrième mission
demande 72 kg de farine ; sans moulin, le juge remontait la recette d'un cran jusqu'au blé
et renvoyait **au champ** — moissonner un silo déjà plein — sans que le moulin soit désigné
nulle part. Il l'est maintenant, et seulement une fois la matière là : tant qu'il n'y a pas
de blé, l'objectif reste le champ ; dès qu'il y en a, c'est le moulin.

**Et le battement se voit enfin.** Le cadre qui grandit partait de 0,7 d'opacité et
s'écartait de 42 % en 1,4 s ; il part maintenant **plein**, s'écarte de 62 % et recommence
toutes les 1,05 s. Le cadre plat des rangées de menu — qu'on ne peut pas mettre à l'échelle,
les trois conteneurs coupant ce qui dépasse — passe de deux à trois pixels et reçoit un
**lavis jaune à treize pour cent**, si bien que c'est la rangée entière qui respire et non
son contour. Tout cela reste `transform` et `opacity`, les deux seules propriétés que le
compositeur traite sans repasser par la peinture : une `box-shadow` animée avait coûté un
dixième des images du jeu.

**Et l'on écrit ACHETER.** *« Au lieu de marquer monter pour le moulin, et pour tout le
reste, écris acheter. »* Les huit métiers de l'atelier étaient les seuls du jeu à se
« monter » — le garage, le comptoir et l'agence disaient déjà acheter. Un verbe par geste,
et le même partout : le bouton, l'état une fois payé, et les deux phrases qui renvoyaient à
l'écran des métiers.

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
s'en déduit tout seul. Un kilo de blé vaut 2,22 € ; moulu il rend 0,72 kg de farine,
qui doit valoir une fois et demie le blé de départ : la farine vaut donc 4,63 € le
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

## L'étiquette d'un commerce : debout, et tournée vers le regard

Trois états successifs, et le troisième est le bon.

1. **Un plan orienté comme la façade.** Les commerces des bandes est et ouest le
   présentaient de trois quarts : on lisait leur nom en oblique, écrasé.
2. **Un sprite.** Il fait face à la caméra quoi qu'on fasse — mais *entièrement*, tangage
   compris. La caméra du jeu regarde d'en haut à 49° : le panneau se couchait donc en
   arrière pour se mettre perpendiculaire à l'axe de vue, et il se lisait de biais dans
   l'autre sens.
3. **Un plan qui ne pivote que du lacet.** Il reste vertical dans le monde — planté comme
   un panneau de rue, ce qu'il est — et ne tourne qu'autour de Y pour présenter sa face au
   joueur d'où qu'il vienne. Une ligne de trigonométrie : `atan2` du vecteur bulle →
   caméra dans le plan du sol.
4. **Un plan qui ne pivote plus du tout.** Le joueur : « celle des commerces pivote
   toujours, alors que celle du silo, de l'essence et de la production sont fixes ; essaye
   de me les faire toutes fixes, mais en trois dimensions comme celle des commerces. » Il
   avait raison, et pour une raison que l'état 3 avait manquée : **la caméra ne tourne
   jamais**. Son décalage `CAM_BASE = (38, 62, 38)` n'est pas tourné par le zoom, il est
   seulement divisé — l'azimut du regard vaut `atan2(38, 38)` = **45°**, à toute distance
   et à tout niveau de zoom, et pas une ligne du fichier ne touche à `camera.rotation`.
   Un panneau qui « se tourne vers la caméra » ne fait donc que suivre sa propre position
   relative : il se dévisse lentement quand on roule devant, pour rien.
   Ils sont maintenant plantés une fois pour toutes à ce cap, `CAP_PANNEAU = π/4`. Une
   étiquette au pied de la machine est exactement en face ; une à l'autre bout de l'écran
   est vue de biais d'une vingtaine de degrés. Mesuré sur une capture avant / après : le
   nom d'un commerce passe **d'incliné à horizontal**, et le lettrage y gagne.

**Et l'on rattrape le raccourci.** Un panneau debout vu d'en haut se tasse : sa hauteur
apparente vaut le cosinus de l'élévation du regard. Mesuré sur les seize enseignes du
village, ce cosinus va de **0,74 à 0,97** — jusqu'à un quart de la hauteur perdu sur les
plus proches, celles qu'on lit justement. On le rend en étirant le panneau d'autant
(1,03× à 1,36×, plafonné à 1,82×) : il reste vertical dans le monde, et il retrouve à
l'écran le rapport dans lequel le texte a été tracé. Mesuré : 0,217 et 0,328 vus pour
0,221 et 0,336 dessinés, soit **1,8 % d'écart** au lieu du quart manquant.

Le rattrapage, lui, se pose **après** que la caméra a bougé : calculé avec le flottement, il
serait en retard d'une image. C'est tout ce qui reste dans cette boucle de fin de trame —
`rattraperRaccourci(m)`, un `scale.y` et rien d'autre.

### Et les étiquettes de lieu sont devenues les mêmes

Le silo, l'atelier, l'entrepôt, la cuve à gazole, les mangeoires, les tanks et les parcelles
portaient une **jauge** : un sprite de 384 × 114, parfaitement plat, parfaitement face à
l'écran. Deux espèces d'étiquette sur le même écran, et le joueur voyait la différence.

Elles sont maintenant du même bois que les enseignes — un plan de 11 m au cap π/4, la même
plaque sombre, la même fonte, la même barre d'accent — avec **trois étages au lieu d'un** :
un nom, une ligne de détail, une barre de remplissage. « Silo » et « 900 kg sur 2 700 · Blé »
et la barre orange, sur une seule plaque.

**Et l'entrepôt n'a plus qu'une étiquette.** Il en portait deux, sur la même verticale au
millimètre : une enseigne « ENTREPÔT » plantée à la construction du monde, et la barre de
stock qui s'allumait à la première livraison, soixante-huit centimètres plus haut. Mesuré :
**2,21 m de recouvrement**, soit 83 % de la hauteur de l'enseigne et 71 % de celle de la
jauge — et l'enseigne était peinte *par-dessus* (renderOrder 6 contre 4). Le joueur : « il y
a une étiquette avec marqué entrepôt, et quand on livre à l'entrepôt il y a une étiquette
qui se met en arrière-plan, ça fait doublon. » L'enseigne a été retirée ; l'étiquette de
stock porte le nom.

**Puis une contre-lecture adverse a mesuré ce que ça coûtait, et trois choses ont bougé.**

- **Le canevas était deux fois et demie trop gros pour rien.** 560 × 206 = 461 Kio par
  étiquette, contre 175 pour l'ancienne jauge — et la hauteur d'une lettre *en mètres* ne
  dépend pas du canevas, seulement de sa taille en pixels et du rapport `PAN_LARGE / PAN_W`.
  On payait donc 2,6 fois la mémoire pour une ligne de chiffres qui avait **rétréci de
  32 %**, et pour 4,09 texels par pixel d'écran sans pyramide de mipmaps — c'est-à-dire un
  texte *haché*, pas affiné. Le canevas descend à **470 × 200 (376 Kio, 3,4 texels par
  pixel)** et les deux lignes grossissent : le nom à **1,22 m** d'em, la ligne de chiffres à
  **1,08**, contre 1,04 pour la ligne unique d'avant. Plus lisible et moins lourd.
- **Le rattrapage s'arrête plus tôt.** Le plancher à 0,55 autorisait un étirement de
  **1,82**, et à ce régime la pile d'un enclos se recouvrait de 20 % de son aire, tandis que
  l'étiquette de la cuve entrait de **58 cm** dans le fût qu'elle nomme. Le cosinus
  réellement rencontré par les seize enseignes va de 0,74 à 0,97 : un plancher à **0,72** ne
  les touche jamais et ne coupe que l'excès. Étirement maximum : 1,39. Les cotes suivent —
  cuve 6,6 → 7,4 ; entrepôt 12,0 → 12,4 × l'échelle ; mangeoire 11,0 → 12,4 ; tank 5,6 →
  5,2 ; parcelle 6,0 → **8,0**, parce qu'un olivier mûr monte à 4,59 m et que l'étiquette
  descendait dans son houppier.
- **Le rayon de réserve suivait la portée de douze mètres trop loin.** Entre 62 et 74 m,
  une étiquette était *réservée* — donc un canevas et sa texture — pour n'être jamais peinte,
  `montrerJauge` s'arrêtant avant. Mesuré au pire trajet : six panneaux retenus pour rien, et
  le vivier poussé à dix-neuf. Deux mètres de battement suffisent.

**Et les quatre étiquettes de la cour restent allumées.** Elles ne s'affichaient qu'en
travaillant : l'atelier seulement pendant un lot, l'entrepôt seulement s'il contenait
quelque chose, le silo seulement s'il n'était pas vide. Le bâtiment le plus cher de la ferme
n'avait de nom que quand il tournait. « Je veux que l'étiquette de l'entrepôt et l'étiquette
de l'atelier de production restent tout le temps visibles. » Elles le sont, dans les 62 m du
rayon d'affichage, et elles disent ce qu'elles ont à dire quand elles n'ont rien à dire :
« halle nue · aucun métier », « vide · 1 350 kg de place ».

La pente qui reste — le nom penche un peu vers le bord de l'écran — n'est pas un défaut :
une arête horizontale du monde ne se projette horizontalement que sur l'axe de vue, et
c'est ce qui donne au panneau son assise, comme aux lignes de faîte des toits autour. Le
banc le mesure ainsi : au milieu de l'écran la pente tombe à 0,04–0,15, au bord elle monte
à 0,46, et le **roulis propre de l'objet reste nul**.

Au passage, une fuite : la bulle est détruite et recréée à chaque changement de texte — un
commerce qui s'ouvre, une mission qui change ce qu'elle attend — et rien n'était rendu au
pilote graphique. Trente repeintes laissaient trente textures de 560 pixels derrière elles.
Elles sont maintenant `dispose()`ées, géométrie comprise : **87 textures avant, 87 après**.

**Elles ne flottent plus qu'à peine.** Trente-deux centimètres de battement, c'était un
tiers de la hauteur du panneau : quinze enseignes qui montaient et descendaient chacune à
son rythme faisaient bouger tout l'horizon, et l'on cherchait celle qu'on voulait lire.
Cinq centimètres, et deux fois plus lentement — mesuré à **0,10 m creux à crête** sur une
période contre 0,64 auparavant. Il reste juste de quoi distinguer une enseigne d'un élément
du décor.

**Et elles passent devant les cercles au sol.** Un cercle jaune posé devant un commerce se
dessinait *par-dessus* son enseigne, et l'on ne lisait plus le nom de celui chez qui on
allait. Le piège est dans three.js : `renderOrder` posé sur un `Group` devient le
`groupOrder` de ses enfants, et le tri des transparents compare le **groupOrder avant le
renderOrder**. Les cercles mobiles passaient donc devant tout, quel que soit l'ordre donné
aux enseignes. L'ordre se pose maintenant sur les maillages — 3 pour les cercles, 6 pour
les enseignes — et le nom se lit.

### Puis tout est repassé à plat, et c'était le bon état depuis le début

Le joueur, en voyant le résultat : **« vos étiquettes, elles ne font plus en 3D, on refait
à plat comme l'ancienne du silo. »** Il a raison, et le défaut se mesure au lieu de se
discuter : un plan vertical vu d'un azimut de 45° et d'une élévation de 49° **ne se projette
pas en rectangle**, il se projette en parallélogramme. Relevé à l'écran sur les quatre
étiquettes de la cour et quatre enseignes du village, l'angle entre les deux bords de la
plaque allait de **50,8° à 100,2°** au lieu de 90 — près de quarante degrés d'écart sur
l'atelier — et le rapport des proportions de **0,825 à 1,206**. Le rattrapage de raccourci ne
pouvait rien contre ça : il corrigeait la *hauteur*, pas le *cisaillement*, et c'est le
cisaillement qui met le texte en italique. Sur une capture, « Silo » et « Entrepôt »
penchent visiblement.

Les deux familles redeviennent donc des **sprites** — les étiquettes de lieu *et* les quinze
enseignes de commerce, sans quoi l'incohérence que le joueur reprochait au tour d'avant
reviendrait par l'autre bout. Mesuré après : **90,00° et 1,000 partout**, à toute distance,
et la largeur à l'écran ne bouge pas (160 → 165 px sur le silo, 71 → 72 sur une enseigne).

Ce qui a été gagné entre-temps **reste** : une seule étiquette par lieu au lieu de deux,
trois étages sur la même plaque, l'entrepôt et l'atelier allumés en permanence, le canevas
à 470 × 200. Seul le porteur change. Ce qui disparaît avec lui : `CAP_PANNEAU`, le
rattrapage de raccourci, et la seule correction par image qui restait — un sprite a ses
proportions par construction. Ce qu'on perd, et il faut le dire : un sprite ne paraît plus
*planté* dans le sol ; c'est une étiquette posée sur l'image, pas un panneau de rue. C'est
exactement ce qui est demandé, et c'est ce qu'était l'ancienne jauge du silo.

## La tour s'agrandit

**La capacité du silo était une formule, et rien d'autre :** `160 + terre × 0,30`. Elle
suivait la terre possédée, automatiquement, et l'on n'avait aucune prise dessus. Le joueur :
« il manque des améliorations pour le silo pour augmenter la capacité ; crée ces
améliorations en lien avec l'accroissement de l'activité. »

La mesure lui donne raison **au-delà de ce qu'il dit**. Relevé palier par palier sur les
vingt de la campagne — terre possédée, kilos d'une moisson complète de blé, capacité de la
tour :

| palier | parcelles | une moisson | la tour tient | soit |
|---|---|---|---|---|
| 1 · Le fermier | 1 | 49 kg | 228 kg | **4,66 moissons** |
| 6 · L'orge | 3 | 199 kg | 435 kg | 2,19 |
| 10 · Gros volumes | 5 | 352 kg | 646 kg | 1,83 |
| 14 · La gamme fermière | 7 | 582 kg | 963 kg | 1,65 |
| 20 · Exploitation complète | 20 | 1 848 kg | 2 710 kg | **1,47 moisson** |

Le commentaire du code promettait « deux récoltes et demie quel que soit le nombre de
parcelles ». C'est faux : la tour **se resserre** à mesure que la ferme grandit, parce que le
fond de cale de 160 kg domine tant qu'on a une parcelle et ne pèse plus rien quand on en a
vingt. Le pincement arrive donc exactement au moment où l'on a le plus de grain à rentrer —
et c'est ça, « en lien avec l'accroissement de l'activité ».

**Le barème multiplie la formule au lieu de la remplacer**, pour que la tour continue de
suivre la terre : ×1, ×1,5, ×2,1, ×2,9, à **1 200, 4 000 et 11 000 €**. Au dernier palier,
1,47 moisson devient 4,25 ; au sixième, 2,19 devient 6,33. Les prix sont ceux de la capacité
de l'atelier (900, 3 400, 9 000) décalés d'un cran vers le haut : le silo sert *toutes* les
filières et non une seule, et son premier cran s'achète au palier où les primes de mission
passent 3 000 €.

Il s'achète dans la fenêtre du **stockage**, troisième onglet — c'est là qu'on lit déjà ce
que la tour contient, et le bouton du stockage est un des trois boutons permanents de
l'écran. La ligne dit les trois chiffres qui décident : ce que la tour tient, ce qu'elle
tiendrait, et **combien de moissons** cela fait — parce que « 646 kg » ne veut rien dire tant
qu'on ne sait pas ce qu'une moisson rapporte.

## Deux missions qu'on ne pouvait pas finir

> Cette passe a réparé les deux lignes impossibles ; le palier six a été refait *ensuite*, et
> la Brasserie du village y a laissé la place à une Épicerie — voir
> « [La Brasserie devient l'Épicerie, et la bière se brasse à la ferme](#la-brasserie-devient-lépicerie-et-la-bière-se-brasse-à-la-ferme) ».
> Ce qui suit raconte l'état d'avant.

**« Après la brasserie, il me demande de la bière alors que j'ai pas de quoi fabriquer de la
bière. »** Le joueur a raison, et il y en avait une seconde qu'il n'avait pas encore
rencontrée. Sur les trente-neuf lignes de marchandise que réclament les trente missions,
deux étaient impossibles :

- **140 litres de bière au Restaurant, au palier six.** La bière n'était fabriquée que par
  la Brasserie du village, qui *encaisse* — « il vend lui-même, il n'y a rien à emporter » —
  et aucun des huit métiers de la halle ne la faisait. Le Restaurant ne l'achetait pas non
  plus. Une passe précédente avait justement **retiré** la bière des étals, en écrivant que
  « l'afficher ici, c'était promettre au joueur des lignes qu'il ne pourrait jamais
  honorer » : la correction avait été portée aux étals, et pas aux missions.
- **12 kg de miel à la Boulangerie, au palier quatorze.** Le boulanger dit « j'ai une
  nouvelle recette en tête, il me faut votre farine, vos œufs et votre miel » — et n'avait
  aucune recette au miel. Ce qu'une usine accepte dans sa trémie **se déduit de ses
  recettes** (« pas de liste à tenir à jour en double, donc pas de liste qui se
  désynchronise ») : elle refusait donc le miel au quai.

**La ferme brasse maintenant sa bière.** Une neuvième cuve entre à l'atelier — 950 €,
165 secondes pour cent kilos d'orge —, au palier six, celui qui ouvre justement l'orge, la
Brasserie et le Restaurant. On vend son orge au village *et* on brasse la sienne chez soi ;
la bière rejoint le fromage du côté de ce que l'atelier transforme, et se vend donc comme
lui, au Restaurant, au Marché et au Supermarché. Le tableau des modules est rangé par
palier, donc la cuve se place après le broyeur ; le palier d'un module se lit dans `NIVEAUX`
**par clé** et non par position, donc rien ne se décale.

**Et la boulangerie a sa recette au miel** — farine, œufs, miel, exactement ce que le texte
décrit. Elle passe *devant* les deux autres recettes à trois ingrédients : le choix prend la
première réalisable, et le miel est l'entrée la plus chère de la boulangerie. Qui n'en
apporte pas retombe sur la pâtisserie premium, comme avant.

**Le banc pose maintenant les deux questions**, pour chacune des trente-neuf lignes : la
ferme sait-elle *produire* la marchandise — culture, bête ou métier de la halle —, et le lieu
de livraison la *prend*-il, en l'achetant ou en l'employant dans une recette. Aucune des deux
n'était posée. Éprouvé sur l'état d'avant : il rend « MANQUE n10 bière @Restaurant » et
« REFUSE n10 bière @Restaurant, n22 miel @Boulangerie ».

## Le garage : acheter, améliorer

Le garage avait **deux boutons, et chacun ne portait qu'une seule chose**. Celui d'achat
sortait *un* article — le moins cher de la liste, ou celui qu'on était allé désigner dans
l'onglet Engins, trois écrans plus loin : pour arriver à l'enjambeuse, il fallait avoir
acheté le tracteur d'avant. Celui d'amélioration ne proposait qu'un cran, celui de la
machine où l'on était assis et de l'outil qui y était attelé : pour savoir ce que coûtait
la trémie de la moissonneuse, il fallait aller chercher la moissonneuse.

Les deux boutons restent — **ACHETER** et **AMÉLIORER** — mais ils **ouvrent une liste**
au lieu de payer, et chacune a deux onglets :

| | véhicules | outils & remorques |
|---|---|---|
| **Acheter** | ce qui est en vente, ce qui ouvre plus tard, ce qu'on a déjà | l'épandeur, la benne, la charrue, le semoir |
| **Améliorer** | tous les engins possédés, cran par cran | tous les outils possédés, cran par cran |

Le bouton dit **combien il y a à vendre au palier du moment**, pas combien il existe
d'articles : il annonçait cinq articles au palier 1 alors que trois attendaient un palier
de campagne. La liste s'ouvre quand même, pour montrer ce qui vient.

Le menu Engins, lui, redevient ce qu'il prétendait être : un **catalogue**. Il montre ce
qu'on a et ce qui reste à prendre ; il ne fait plus désigner l'article que le garage
sortira, puisque le garage les sort tous.

### Le tracteur rouge et le bleu reviennent à la vente

Ils avaient été **retirés** au nom du « pas de gros tracteur » : on garde son matériel et
on l'améliore, on n'en rachète pas un plus gros tous les cinq paliers. La règle tient
toujours, et c'est pour ça qu'ils peuvent revenir — **ils ne sont pas plus gros, ils sont
en plus.** Ce qu'on achète avec le deuxième tracteur n'est pas de la puissance, c'est un
**attelage permanent** : la charrue reste sur l'un, le semoir sur l'autre, et l'on cesse de
faire l'aller-retour au parc à outils entre deux passages. Deux engins peuvent aussi
travailler seuls en même temps.

Chacun garde donc **la même échelle de cinq crans que le vert**, et prend son palier :

| | prix | palier | ce que le palier demande |
|---|---|---|---|
| Tracteur vert | offert | 1 | — |
| Tracteur rouge | 4 500 € | 5 | « Deux chaînes à la fois » |
| Tracteur bleu | 18 000 € | 14 | « La gamme fermière » |

Les deux paliers n'ouvraient rien d'autre, et ce sont exactement ceux où l'on commence à
mener deux puis trois filières de front — c'est-à-dire le moment où l'attelage permanent
se paie. Un banc vérifie que **rien de payant n'échappe à la table des paliers** : sans
cette ligne, les deux tracteurs auraient été en vente dès la première minute.

Ils ne changent pas de place dans `MACHINES` : la sauvegarde sérialise cette table **par
position**. Et ils portent enfin leur robe dans le nom — trois lignes « Tracteur » l'une
sous l'autre, à 4 500 et 18 000 €, ne se distinguaient plus. Le nom reste « Tracteur » au
bandeau et sur la carte, où la couleur du modèle est sous les yeux.

## Un tour, puis des lignes — et le retour de l'escargot

Le pilote traçait un **escargot** : des tours de plus en plus serrés jusqu'au centre. Il
couvrait bien — 94 à 100 % — mais il tournait sans arrêt. Sur une parcelle de trente
mètres à la charrue : quatre tours complets, seize virages, et un outil traîné quatre
mètres derrière qui coupe chacun d'eux. C'est dans les virages que la terre se perd, et
c'est aussi là que la machine déborde.

Le plan est maintenant celui d'un vrai fermier, et il est plus simple : **un tour de
périphérie**, puis **des lignes droites** entre les deux tournières. Les demi-tours
tombent tous sur la bande déjà travaillée ; les lignes, elles, ne tournent pas du tout.
Les lignes **s'arrêtent au niveau de la périphérie**, pas au bord du champ : la tournière
est faite, la ligne la rejoint exactement, et le demi-tour se prend *dans* le champ.

Tout reste strictement orthogonal — pas une diagonale dans le plan. Le raccord entre le
tour et la première ligne se prend **en deux temps** : on longe le bord jusqu'au bout de
la ligne, puis on rentre. Relier les deux directement faisait une diagonale, et la
machine la prenait en biais en balayant large : jusqu'à cinq mètres et demi hors de la
parcelle.

### Et la clôture reste debout

**Aucun banc ne mesurait ça.** `pilote_couv.js` relève bien une « marge obstacle », mais
depuis l'axe du tracteur, une image sur dix, et dans une scène où il met toutes les autres
parcelles hors jeu — donc **sans une seule clôture**. Le seul danger réel du jeu n'était
pas mesuré. Le banc `cloture.js` le mesure : il cherche les parcelles qui longent vraiment
la clôture de la ferme, pilote image par image, et compte les courses **couchées** — c'est
le jeu lui-même qui pose l'état, cette mesure-là ne peut pas mentir.

Le relevé sur l'escargot est sans appel : **cinq courses couchées** sur douze passes, et
l'axe du tracteur jusqu'à **5,36 m** hors de sa terre.

Deux causes, et deux corrections.

**Le retrait se décide bord par bord.** Il valait `T.width/6` partout — un tiers de l'outil
dehors, ce que demande le cahier des charges. C'est juste au *milieu* d'une passe, beaucoup
moins dans un *virage* : mesuré à l'image près, le tracteur dépasse le coin de 2,30 m sur
une petite parcelle et de 3,50 sur une grande. Or la clôture de la ferme passe à 2,10 m du
bord des parcelles de bordure et son mur de collision à 1,85 : **il reste vingt-cinq
centimètres**. Sur un bord adossé à quelque chose, le retrait vaut donc au moins ce
dépassement. L'outil, lui, mord toujours dehors — à 1,95 m de retrait une charrue de 4,80
couvre encore 45 cm au-delà du bord.

**Et l'on lève le pied avant le coin.** `viser` roule plein gaz tant que le cap est bon et
ne ralentit qu'une fois le cap faussé — c'est-à-dire *après* le coin. Reculer la ligne
d'autant coûterait un mètre et demi de terre par bord, soit douze points de couverture : on
paierait la clôture avec le champ. Un conducteur, lui, ralentit avant de tourner. Quinze
mètres avant un point marqué, le gaz décroît jusqu'au quart.

Le rattrapage partage tout cela — il rentrait d'un sixième partout et plaçait ses lignes sur
la boîte brute des cellules restantes, qui touche le bord : **la moitié des clôtures
tombaient là**, pas dans le plan principal.

| | escargot | un tour puis des lignes |
|---|---|---|
| courses de clôture couchées | **5** | **2** |
| l'axe hors de sa parcelle | **5,36 m** | **1,99 m** |
| couverture, pire des seize cas | 94,2 % | 90,7 % |
| images pour seize passes | 93 000 | 93 600 |

Ce qu'on paie, ce sont **trois points et demi de couverture** sur le pire cas — l'épandeur
de douze mètres sur une parcelle de dix-neuf, où la bande du milieu ne tient plus un pas
une fois les deux tournières faites. Les quinze autres cas restent entre 96 et 100 %. Ce
qu'on achète, c'est la clôture debout.

Les deux courses qui tombent encore le font toutes deux sur le **raccord du rattrapage** —
la machine vient de finir sa passe, souvent le nez dehors, et rejoint sa première ligne au
plus court. Jamais pendant le travail lui-même.

### Le demi-tour se prend au pas

Le joueur l'avait vu à l'œil : *« le tracteur va trop vite quand il fait son demi-tour. Si
tu vas tout doucement avec les roues braquées à fond, il va tourner plus serré, il va
pouvoir revenir sur ses traces sans avoir à manœuvrer. »* Le modèle du jeu lui donne
raison, et cela tient dans une ligne de `Vehicle.update` :

```
this.cap += steerX * this.turn * min(1, |vf|/2.2) * dt
```

Le rayon vaut donc `R = |v| / (braquage × turn)`. **Au-dessus de 2,2 m/s il est
proportionnel à la vitesse** : un tracteur neuf lancé à douze mètres par seconde tourne sur
6,3 m de rayon, à deux sur 1,2 m — et un tracteur *amélioré*, qui monte à 18,6 m/s, sur 9,8.
Au-dessous de 2,2 m/s l'adhérence diminue exactement au rythme de la vitesse, les deux se
compensent, et le rayon ne descend plus. **2,2 m/s est le point le plus serré**, ni plus
lent ni plus vite, et c'est la vitesse à laquelle on prend une tournière.

Trois choses ont changé, et aucune ne touche au tracé :

- **On freine sur toute l'approche**, selon `v² = v_pivot² + 2·a·d` : à vingt mètres du bout
  de la ligne on roule encore à dix mètres par seconde, à cinq mètres à cinq, et l'on aborde
  le point exactement à la vitesse qui tourne le plus court. `viser` ne levait le pied
  qu'une fois le cap *déjà* faussé — c'est-à-dire après avoir dépassé le coin.
- **Le gaz de virage se donne en mètres par seconde**, plus en fraction de la vitesse
  maximale. Les deux paliers valaient 0,22 et 0,45 : 2,6 et 5,4 m/s pour un tracteur neuf,
  mais 4,1 et 8,4 pour le même au dernier cran — améliorer sa machine dégradait son travail.
- **On ne vise pas plus serré que son propre rayon de braquage.** Deux points de tournière
  sont distants d'un pas, et la machine en plein virage décrit un cercle d'un à trois
  mètres : elle tournait *autour* du point sans jamais l'atteindre, jusqu'à ce que le
  garde-fou des huit secondes l'abandonne — et abandonne avec lui la ligne entière. Mesuré :
  trois lignes perdues sur cinq, vingt-six pour cent de la parcelle jamais labourée. Le
  rayon de capture suit donc le braquage, mais **seulement quand la machine tourne
  vraiment** : abordé de face, un point se prend à deux mètres comme avant.

### Et l'on ne revient pas

*« Une fois qu'il a fini les passages jusqu'au bout de la parcelle, il faut s'arrêter et
sortir de la parcelle, pas revenir encore une fois. »* C'était le défaut le plus visible, et
il ne venait pas du tracé : le rattrapage se déclenchait dès qu'il restait **une** cellule,
et il traçait alors **plus de lignes que le balayage lui-même** — sept traversées complètes
de la parcelle pour rattraper trois coins, et jusqu'à trois fois de suite. Une cellule
perdue au milieu d'un champ valait deux traversées d'un bout à l'autre.

Il ne part plus que quand la passe a *vraiment* échoué : panne sèche au milieu, machine
bloquée, plan interrompu. Mesuré sur seize cas — quatre outils par quatre tailles de
parcelle, pilotés image par image —, un plan qui va au bout laisse entre 0 et 10,7 % de la
terre, 4,7 % en moyenne. Au-delà de **quinze pour cent** ce n'est plus un reliquat de
virages, c'est du travail qui ne s'est pas fait : on repasse une fois, et une seule.

Ce que les douze chantiers du banc de clôture disent des deux changements réunis :

| | avant | après |
|---|---|---|
| vitesse d'entrée en demi-tour, charrue | 11,2 m/s | **4,2 m/s** |
| — et donc rayon de virage | 5,9 m | **2,2 m** |
| vitesse d'entrée, moissonneuse | 8,7 m/s | **5,2 m/s** |
| passes par parcelle | jusqu'à 4 | **1** |
| images pour les douze chantiers | 59 824 | **30 204** |
| clôtures couchées en travaillant | 2 | **0** |
| l'axe sort de sa terre de | 1,99 m | **1,29 m** |
| terre du voisin travaillée | 1 cellule | **0** |
| terre faite, au pire des douze | 90,7 % | 93,3 % |

### Et le joueur redemande l'escargot

*« On va repartir sur le dessin en escargot : une fois que le contour a été fait, on
redessine en reprenant un tiers sur ce qui a déjà été fait, jusqu'au centre. Une fois au
centre et qu'on a fait un tour sur nous-mêmes, on sort du champ sans faire de passage
supplémentaire. N'essaie pas de chercher à remplir complètement le champ. Fais juste ce
dessin, t'occupe pas de la charrue que tu traînes derrière ; tu fais ce dessin avec tous
les véhicules. »*

C'est une demande de **dessin**, pas de rendement, et elle défait volontairement ce que le
balayage avait gagné. Elle est appliquée telle quelle.

Le tracé tient en une boucle : on pose le coin suivant, **puis** on resserre le seul bord
qu'on vient de longer, d'un pas qui vaut **deux tiers d'une largeur d'outil** — donc un
tiers repris sur la passe précédente, exactement ce qui est demandé. Resserrer les quatre
bords à la fois ferait un cadre concentrique et un saut en diagonale à chaque tour ; un
bord à la fois ferme la spirale sur elle-même. La boucle s'arrête quand le rectangle
restant est plus petit qu'un demi-pas, et le tracé se termine par **quatre points** qui
dessinent un tour sur place au centre, puis par la sortie de parcelle.

| | mesuré |
|---|---|
| pas d'une passe à la suivante | **0,667** largeur d'outil (2/3 exact) |
| segments en biais dans tout le plan | **0** |
| tours qui repartent vers l'extérieur | **0** |
| rayon, du premier tour au dernier | 14,4 m → **1,6 m** |
| le premier tour mord dehors de | 1,6 à 4,0 m selon l'outil |
| l'axe du tracteur, lui, reste dedans | −0,8 m |
| passes qui se terminent d'elles-mêmes | **4 sur 4** |
| la machine finit hors de la parcelle | 3,35 à 9,14 m |

**Le piège était dans la validation des coins, et il a coûté seize points de couverture.**
Un point de passage se valide à 2 m normalement, à 1 m s'il est marqué « bord » ou
« sortie ». Les coins de la spirale n'étaient marqués que « virage » : la machine les
validait deux mètres trop tôt, coupait l'angle, se retrouvait à viser un point *derrière
son épaule*, sortait du champ par le coin nord-est, et le garde-fou des huit secondes
abandonnait trois points d'affilée. Couverture réelle sur la moissonneuse en 30,4 × 30,4 :
**79,8 %**. Les mêmes coins marqués « bord » — donc validés à un mètre — la remontent à
**96,8 %**. Le tracé n'avait pas changé d'un centimètre.

**Le tour sur place se borne au rectangle.** Sur une petite parcelle avec un outil large, la
pirouette finale sortait l'axe du tracteur de 0,40 m au-delà de la limite : ses quatre points
sont donc rabattus dans le rectangle de la parcelle. Le rayon du tour vaut le plus petit du
rayon de braquage à la vitesse de pivot et de la demi-parcelle.

**Et l'on ne repasse plus du tout.** `planRattrapage` — quatre mille neuf cents octets qui
retraçaient des lignes droites sur ce qui restait — est **supprimé**, et `finDePlan` ne
remplace plus le plan : il sort. C'est la seconde moitié de la demande, et elle a sa propre
vertu : une fonction que plus rien n'appelle ment sur ce que le pilote fait. `SEUIL_REPASSE`
reste écrit parce que l'écran s'en sert pour dire combien il reste à faire ; ce n'est plus
une décision.

**Ce que ça coûte, et c'est le prix demandé.** Machine pilotée image par image sur les seize
cas du banc :

| | un tour puis des lignes | l'escargot |
|---|---|---|
| couverture réelle, moyenne | 97,7 % | **86,8 %** |
| couverture réelle, pire cas | 89,3 % | **67,1 %** |
| le tracé géométrique couvre | 100 % | 97,7 % |
| clôtures couchées en travaillant | 0 | 1 (tolérance : 2) |
| l'axe sort de sa terre de | 1,29 m | 1,42 m |
| passes par parcelle | 1 | 1 |
| distance au plus proche obstacle | 1,50 m | 1,50 m |

Les onze points de couverture perdus sont **le dessin lui-même** : un escargot vire seize
fois là où un balayage vire deux fois, et c'est dans les virages que l'outil traîné coupe.
Le pire cas — l'épandeur de douze mètres sur une parcelle de dix-neuf — n'a la place que
d'un tour et demi. Le joueur a vu venir précisément cela et a tranché : *« n'essaie pas de
chercher à remplir complètement le champ »*. Ce qu'on garde en échange, c'est ce qui avait
été acheté au prix fort et qui ne se rend pas : une seule passe par parcelle, une sortie
franche, la clôture debout et le demi-tour au pas.

## Le premier quart d'heure

Le jeu commençait par **un anneau vert à la Coopérative**. Il fallait deviner qu'on y
prenait une mission, la lire, et *alors seulement* le guidage s'allumait. Or la première
chose qu'un fermier doit apprendre n'est pas où prendre une commande : c'est le tour
complet.

Sept étapes, sept phrases, dans l'ordre où on les fait :

| | ce qu'il dit | franchi quand |
|---|---|---|
| **PRÉPARER LA PARCELLE** | attelle la charrue et travaille le sol | **les trois quarts** de la parcelle sont travaillés |
| **SEMER DU BLÉ** | attelle le semoir et sème ta première parcelle | **les trois quarts** de ce qui est travaillé sont semés |
| **LAISSER POUSSER** | le blé mûrit, la moisson vient | **les trois quarts** de ce qui est semé sont mûrs |
| **PREMIÈRE RÉCOLTE** | moissonne au moins 30 kg de blé | 30 kg rentrés **et** les trois quarts coupés, ou la trémie pleine |
| **STOCKER LA RÉCOLTE** | décharge ton blé dans le silo | 30 kg au silo |
| **PRÉPARER LA LIVRAISON** | charge 30 kg de blé dans le pick-up | 30 kg à bord |
| **PREMIÈRE VENTE** | rends-toi à la Coopérative agricole | on y prend la mission |

Quatre choses à comprendre sur ce mécanisme.

**Il ne déplace rien.** Chaque étape désigne un lieu que le guidage sait déjà éclairer — le
champ, le silo, la Coopérative — et passe par `objectifMission()`, donc par le cercle mobile
au sol, la flèche du bord et la ligne du bandeau. Pas une deuxième machinerie d'affichage :
la même, avec d'autres mots. La greffe tient en cinq lignes.

**Les trois quarts, et non le premier sillon.** Chaque étape de travail se soldait au
premier geste : deux mètres de labour, et la fenêtre s'ouvrait déjà pour dire d'aller
chercher le semoir, sur un champ qu'on venait à peine d'entamer. On croyait avoir *fini*
quelque chose qu'on n'avait pas *commencé*, et l'on repartait au parc à outils en laissant
les trois quarts de la parcelle en jachère. Le seuil est donc à 75 % : assez pour que le
geste soit compris et que la fin ne soit plus qu'une formalité, pas assez pour qu'un angle
oublié retienne tout le tutoriel.

Et **chaque étape se mesure sur ce que la précédente a laissé**, non sur la parcelle
entière. Semer les trois quarts d'un champ labouré aux trois quarts, c'est avoir semé tout
ce qu'on pouvait semer : rapporté à la surface totale, cela ferait 56 % et l'étape ne
passerait jamais. Le labour se compte donc sur la parcelle, le semis sur ce qui est
travaillé, la pousse sur ce qui est semé, la moisson sur ce qui était mûr.

La moisson a une seconde porte : **la trémie pleine**. Trente kilos coupés ne suffisent plus
seuls, mais un champ qui rend plus que la trémie enfermerait le joueur — il devrait aller
vider sans que rien le lui ait dit. Trémie pleine, l'étape passe : c'est exactement ce que
la suivante demande.

**Et le premier cercle jaune est sous la charrue.** *« Quand on commence avec la charrue, on
ne sait pas où est la charrue. »* Le cercle se posait sur la parcelle, à cent mètres du parc
à outils où la charrue attend, dételée, avec les trois autres : on envoyait labourer
quelqu'un qui n'avait rien pour labourer. Tant que l'outil de l'étape n'est pas au crochet,
l'étape **désigne l'outil** — un champ `outil` de plus dans la table, résolu par `lieuTuto`
— et rien d'autre ne change, puisque c'est le même objectif : même cercle mobile, même
flèche au bord, même ligne de bandeau. Attelée, le cercle repart au champ tout seul. Le
semoir a le même traitement à l'étape d'après.

Cela revient en partie sur une décision plus ancienne — *« le guidage vers une machine se
dit dans les menus, et non dans le paysage »*, écrite quand une flèche jaune descendait sur
la machine à prendre. La distinction tient : une **machine** se choisit dans le parc, où
l'on va de toute façon, et le bouton du parc bat ; un **outil dételé** n'a pas de menu — il
est posé dans l'herbe, et il n'y a que le paysage pour le montrer.

**Il se cliquette, il ne se devine pas.** `CAMPAGNE.tuto` est un index qui n'avance jamais à
reculons, et c'est indispensable : les étapes sont des **événements**, pas des états. On
laboure, puis on sème — et la terre labourée disparaît. On verse au silo, puis on recharge —
et le silo se vide. Un test relu sans mémoire renverrait le joueur à l'étape d'avant à
chaque fois. Le cliquet saute aussi plusieurs cases d'un coup : arriver avec sa benne déjà
pleine ne repose pas quatre questions.

**La mission se prend toujours à la Coopérative, et à la fin.** Le tutoriel ne la prend pas
à la place du joueur : il l'y conduit avec ses trente kilos, et c'est là que le marchand
parle. `CAMPAGNE.prise` reste donc faux tout du long — la Coopérative garde sa pastille
verte de mission à prendre, il n'y a **aucun commerce en jaune**, et le bandeau ne porte ni
pilule ni puce puisqu'on n'a rien accepté. Le jaune est au champ, où il doit être.

Le premier mot du jeu — *« Cette ferme est maintenant entre vos mains »* — emprunte l'écran
de fête, qui a exactement ce qu'il faut : du texte centré, une animation, un doigt pour
passer, et surtout **aucune pause**. L'écran d'accueil, lui, met le jeu en pause et porte les
boutons `.accbtn.pri` par lesquels dix bancs entrent dans la partie.

**Chaque étape s'annonce dans cette même fenêtre.** Elle ne passait que par le bandeau
fugace du haut — le titre, deux secondes, là où l'on regarde la route : on ne le voyait
pas. La fenêtre le dit en grand, avec la phrase qui explique quoi faire, et le bandeau du
bas garde la consigne tout du long, pour quand on l'a fermée. Une annonce qui tombe pendant
qu'une autre défile **prend la file** au lieu d'effacer ce qu'on est en train de lire.

**Et la fenêtre est une vraie boîte.** Ces mots-là tombaient sur un champ de blé au soleil
ou sur une façade claire, et l'on ne les lisait pas — c'est vrai de la fin de mission comme
des étapes. Ils prennent donc le fond, le rayon et l'ombre portée de la fenêtre des
missions, au jaune près, qui est la couleur du guidage. Le titre d'une étape passe à quinze
pixels et quatre d'interlettrage : « PRÉPARER LA PARCELLE » à vingt-six et onze déborde d'un
écran de téléphone en paysage. La boîte n'attrape pas le doigt ailleurs que sur elle-même —
on continue de conduire.

**Mais une étape ne se met pas au milieu de l'écran, ni dans le noir.** La fin de mission,
oui : c'est un temps d'arrêt, on a fini quelque chose, et l'on accepte volontiers que la
vallée s'efface derrière. Une étape de tutoriel, non — elle arrive *pendant* qu'on conduit
et elle explique ce qu'on doit faire *à l'écran* : poser le regard au milieu, sur un fond
presque opaque, c'est cacher précisément la chose dont on parle. Elle remonte donc sous le
bandeau du haut (`min(15vh, 104px)`) et sa boîte laisse voir au travers — de `#1B2429` plein
à `rgba(27,36,41,.80)`. Le voile radial s'éclaircit d'autant : de 0,72 au centre à 0,30, et
de 0,18 sur les bords à 0,06. Une classe suffit à séparer les deux cas — `#bravo.etape` — et
la fin de mission garde son costume.

**Le guidage jaune se poursuit dans les menus.** Le tutoriel disait « moissonne au moins
30 kg » à qui pilotait encore son tracteur, sans dire laquelle des six machines de la cour
prendre. Une flèche jaune est descendue un temps sur la machine ; elle a été retirée. Le
chemin est maintenant celui qu'on prendrait de toute façon, et il se suit d'un battement à
l'autre :

| on veut que le joueur… | ce qui bat |
|---|---|
| change d'engin | le bouton du parc, puis **la ligne de la machine à prendre** |
| achète l'épandeur | l'onglet **Outils & remorques** du garage, puis **la ligne de l'épandeur** |
| achète l'engrais | l'onglet **Engrais & gazole** du comptoir, puis **la ligne de l'engrais** |

Chaque étape porte donc quatre champs de désignation : `engin`, puis `fen`, `onglet` et
`art`. Un onglet **déjà ouvert** cesse de battre — quand on y est, c'est l'article qui prend
le relais — et la garde sur la fenêtre est indispensable : les deux étapes de l'épandeur
visent toutes deux un article nommé `engrais`, mais l'une au garage et l'autre au comptoir.
Rien n'est verrouillé : on peut labourer avec le tracteur bleu si on l'a. C'est une
indication, et elle s'éteint dès qu'on a fait le geste.

**Ce qu'on a le droit d'animer, et rien d'autre.** Le halo du bouton du parc est un **cadre
qu'on met à l'échelle**, et non une `box-shadow` qui s'étale. Animer une ombre portée est
une propriété de *peinture* : le bouton se repeignait à chaque image, et **cela seul**
coûtait un dixième des images du jeu — 8,7 contre 9,6 au banc, arrêté sur la même scène. Un
pseudo-élément mis à l'échelle et effacé ne touche que le compositeur.

Dans les menus, une différence de forme, et elle est obligatoire : sur une rangée large et
basse, un cadre mis à l'échelle déborderait de sa boîte — et les trois conteneurs
(`#parcliste`, la barre d'onglets, la liste de la fenêtre) coupent ce qui dépasse ; la barre
d'onglets se mettrait même à défiler toute seule. Ces trois-là ne font donc battre que
l'**opacité** d'un cadre posé au ras du bord. L'opacité est, comme la transformation, une
propriété du compositeur.

### Un préambule, et un seul

Le même mécanisme sert quand un client demande d'aller chercher quelque chose avant de
pouvoir le servir. La **troisième mission** présente l'épandeur : au garage pour l'acheter,
au comptoir pour acheter l'engrais, puis la chaîne normale reprend. La seconde étape
s'intitulait *« remplir l'épandeur »* mais ne regardait que la cuve de l'outil : le joueur
achetait ses vingt-cinq kilos au comptoir, les voyait arriver au bac, et l'étape restait
jaune. Acheter suffit ; le transvasement dans la cuve est le geste d'après, et il la
franchit aussi. Deux étapes qui **indiquent et
ne bloquent rien** — livrer les cent cinquante kilos sans avoir acheté l'épandeur solde
quand même la mission, et l'engrais redevient facultatif dès la suivante, comme le cahier
des charges le demande.

**Et l'étape de l'engrais ne s'affichait jamais.** *« La flèche va directement au champ. »*
La ferme démarrait avec **vingt-sept kilos d'engrais au bac** — invendables, inépandables,
puisque l'épandeur est sous verrou et coûte 250 €. Ils ne servaient qu'à une chose : rendre
la seconde étape *vraie d'avance*, puisqu'elle se teste par `STOCK.engrais > 0.5`. On
achetait l'épandeur, le cliquet franchissait les deux étapes **dans le même tour**, et la
chaîne reprenait au champ sans qu'on soit jamais passé au comptoir.

Le stock de départ est donc nul. C'est le correctif le plus petit qui soit vrai : le premier
engrais du jeu s'achète, et c'est précisément ce que le préambule demande. L'autre forme
possible — *« la quantité possédée a augmenté depuis l'ouverture de l'étape »* — obligerait à
mémoriser un jalon de plus dans la sauvegarde pour la seule mission qui en a besoin.

Le guidage de cette étape, lui, existait déjà et n'attendait qu'elle : l'anneau du comptoir
passe au **jaune vif**, la flèche du bord y mène, l'onglet *Engrais & gazole* bat, puis la
ligne de l'engrais. Un banc le vérifie maintenant de bout en bout — épandeur verrouillé,
épandeur acheté, engrais acheté — au lieu de mesurer les trois seuls états d'une liste que
le joueur ne voyait pas.

Une sauvegarde d'avant le tutoriel le considère comme déjà vu : sans ce défaut, toute partie
en cours se réveillerait à la première étape et s'entendrait expliquer comment labourer. Le
cliquet repart à zéro à chaque mission finie, si bien qu'une vieille partie ne saute que les
étapes de la mission où elle dormait.

## Ce que les clients disent

Chaque mission portait déjà une phrase — trente répliques écrites une par une — et elle
ne s'affichait **que dans l'onglet Campagne du menu**, c'est-à-dire nulle part au moment
où on prend la mission. Elle en porte maintenant **deux**, et chacune se lit à l'endroit
où elle a un sens :

- **Ce qu'il demande** (`texte`) → dans la fenêtre où l'on prend la mission. On entre chez
  quelqu'un, il demande quelque chose, il le dit avec ses mots. Retrait à gauche et barre
  verte : c'est quelqu'un qui parle, pas l'interface.
- **Ce qu'il répond en payant** (`fin`) → sur l'écran *Bravo*. Sans elle, une mission se
  termine sur un chiffre ; avec elle, quelqu'un a été content du travail.

`missionEnContrat()` ne garde d'une mission que ses lignes et son prix — elle jetait la
réplique avec le reste. La fenêtre reçoit donc maintenant **la mission elle-même** au lieu
d'un booléen : tout le code qui suit teste la vérité de `mission`, ce qu'un objet satisfait
aussi bien qu'un `true`.

### La fête se lit en plusieurs temps

Un seul écran suffisait tant qu'il n'y avait qu'une chose à dire. Mais la **première
mission en dit quatre** : le marchand remercie, il explique qu'on peut lui revendre
n'importe quoi n'importe quand, il dit à quoi cet argent sert, et il annonce que le village
va s'intéresser à nous. Tout empiler sur une page ferait un mur qu'on ne lit pas.

L'écran *Bravo* enchaîne donc des **pages** — une page, cinq secondes, ou un doigt pour
passer à la suivante :

| | pages |
|---|---|
| mission 1 | le gain · **vente libre débloquée** · ce que ça permet · le village vous a vu |
| missions 2 à 29 | le gain, et rien d'autre |
| mission 30 | le gain · **exploitation établie** · à vous de jouer · **exploitation libre** |

La dernière page ne vient pas de la mission : elle vient du fait qu'il n'y en a plus.

### Et la campagne finie rouvre les contrats

Le dernier client le promet en payant sa grande réception : *« les commerces continueront
désormais à proposer des contrats, tandis que vous pouvez développer librement votre
exploitation »*. Sans une bascule, la promesse était fausse — la trentième mission soldée,
la vallée devenait muette, puisque `contratsOuverts()` ne rendait vrai qu'en mode libre.
Elle rend maintenant vrai aussi quand la campagne est finie. La condition est là et nulle
part ailleurs, comme le mode libre.

## Le comptoir agricole, chez lui

Il ouvrait **le menu de la ferme** sur un onglet. On venait acheter un sac de graines et
l'on arrivait devant la campagne, les engins, l'élevage et les réglages — au milieu d'une
barre de onze onglets qui n'avaient rien à voir avec le geste demandé. C'est exactement le
défaut que les fenêtres dédiées avaient corrigé pour le stock, la production et les prix ;
le comptoir le gardait seul.

Il a maintenant **sa fenêtre et trois onglets** :

| onglet | ce qu'on y trouve |
|---|---|
| **Semences** | une ligne par culture — prix au kilo, dose d'une parcelle, ce qu'il reste au hangar — puis les deux permanentes, qui ne se vendent pas au sac mais se paient au champ |
| **Engrais & gazole** | l'engrais du bac, et le gazole livré en gros à 1,60 € / L au lieu de 2,00 € à la pompe |
| **Remplir les cuves** | la cuve de l'outil attelé : ce qu'elle porte, ce que le hangar peut y verser, et de quoi la vider |

**On achète au kilo, au curseur.** Le rayon vendait par lots écrits d'avance — 10 kg, 25 kg,
« remplir le hangar » — soit **quatre lignes par culture**, vingt-huit lignes à faire défiler
pour sept cultures. Il en a **une par culture**, et le curseur dit le reste : combien ça
coûte, combien de parcelles ça sème, ce qu'il restera en caisse.

Le curseur s'ouvre sur **la dose utile, pas sur tout**. « Tout » est le bon défaut pour une
production — on transforme ce qu'on a — mais pour un achat il s'ouvrait sur les 450 kg que
la bourse permettait : deux appuis vidaient la caisse pour remplir le hangar de blé. Il
s'ouvre sur une parcelle de semence, une parcelle d'engrais, et les trois raccourcis restent
là pour aller plus haut d'un doigt. Son bouton dit enfin ce qu'il fait : il était écrit en
dur dans le HTML — « Lancer la production » — alors que le même curseur sert à embarquer des
bêtes, remplir une benne et maintenant acheter au kilo.

**Le troisième onglet est celui qu'on cherchait sans le savoir** : remplir la cuve du semoir
se faisait déjà ici, mais par un bouton flottant à quai, sans qu'on puisse voir ce qu'il
restait au hangar. C'est pourtant le geste qui suit l'achat — on vient acheter vingt-cinq
kilos, et l'on veut repartir avec.

**Et c'est ici, et nulle part ailleurs.** La cour de la ferme le proposait aussi, et c'était
une fausse commodité : on attelait le semoir, on s'arrêtait n'importe où chez soi, et le
bandeau demandait de le remplir alors que rien ne disait ce qu'il restait au hangar. Le
geste appartient au comptoir — on y voit le bac, on y achète, on repart chargé. Ce qui reste
dans la cuve, lui, se lit en haut à droite pendant tout le travail.

**Acheter, c'est remplir — et de loin.** C'était deux trajets pour un sac : on venait
acheter vingt-cinq kilos d'engrais, on repartait, et il fallait *revenir avec l'épandeur
attelé* pour les transvaser — alors que l'outil dort au parc à outils, à deux cents mètres
de là. L'achat sert donc la cuve **dans la foulée, où que soit l'outil**, attelé ou non, et
ce qui ne tient pas dedans reste au hangar comme avant. Le semoir se *règle* au passage sur
la graine achetée : sans quoi la cuve porte de l'orge et la machine sème encore du blé,
c'est-à-dire rien. Une cuve entamée d'une autre graine se vide d'abord au hangar — rien ne
se perd — et si le hangar est plein, elle refuse le transvasement plutôt que de jeter.

Le troisième onglet liste du même coup **toutes les cuves de la ferme**, et non plus la
seule de l'outil attelé : les deux autres restaient invisibles ici, et l'on repartait les
chercher.

`ongletComptoir()` déroule toujours les trois vues à la suite : l'aiguillage du menu n'a pas
de repli, et trois bancs lisent encore le comptoir dans `#pliste`.

### Et il vend aussi le droit de cultiver

Une culture, c'est deux achats : le **droit** de la semer, payé une fois — 600 € pour le
maïs, 7 500 € pour l'oliveraie — et la **semence**, payée au kilo à chaque parcelle. Le
second se vendait au comptoir ; le premier ne se prenait qu'à l'onglet *Graines* du menu.

Le rayon des semences du comptoir affichait donc, pour une culture non acquise, une ligne
grise, un bouton mort marqué « Fermé », et cette phrase :

> « La culture n'est pas encore acquise — elle se prend à l'onglet Graines du menu. »

Or c'est précisément cette ligne-là que le guidage fait battre en jaune quand la mission du
quatrième palier demande du maïs. Le jeu envoyait au comptoir, et le comptoir renvoyait au
menu. Le joueur :

> « Je vais au comptoir agricole et je peux pas acheter le maïs, ils me disent d'aller par le
> menu. Je veux plus ça. »

Le bouton fait maintenant ce qu'il annonce : **Acquérir**, 600 €, et la ligne devient
*Acheter* dans la foulée. Les deux permanentes apparaissent au même rayon, sous « Ce qui se
plante », avec le même bouton — elles n'y existaient tout simplement pas tant qu'on ne les
avait pas prises au menu. La fonction est la même des deux côtés : `acquerirCulture(c)`.

### Le menu ne garde que la vue d'ensemble et les réglages

Il portait neuf onglets, dont **six étaient des rayons** : engins, outils, graines, comptoir,
élevage, parcelles. Chacun de ces six a sa porte dans le monde — le garage pour les engins et
les outils, le comptoir pour les graines et les consommables, le quai de l'enclos pour les
bêtes, le panneau « À VENDRE » planté sur la friche pour les parcelles. Un deuxième chemin
vers le même achat, c'est un de trop : c'est exactement ce qui avait été corrigé pour le
stock, la production et les prix quand ils ont reçu leur fenêtre.

> « Le menu, on va le garder que pour les paramètres et avoir une vue globale de la
> progression ; sinon tout se fait par les boutons. »

Il reste donc **Campagne · Filières · Réglages**, et le bouton du menu s'ouvre sur la
campagne au lieu du rayon des outils. Les six autres ne sont pas supprimés, ils sont
**cachés de la barre** : les fonctions restent, l'aiguillage les appelle toujours, et un
bouton du monde peut encore y déposer d'un coup — le quai d'un enclos plein ouvre encore
l'élevage. Un rayon caché où l'on se trouve **réapparaît dans la barre**, sinon on ne
saurait pas où l'on est.

Trois choses ne passaient par aucun bouton du monde, et la contre-lecture les a comptées une
par une : sur quinze achats et réglages, **treize** avaient leur porte, deux ne l'avaient pas.

D'abord **le choix de l'espèce du prochain enclos**. Le message le disait lui-même — « appuie encore pour
confirmer · MENU ÉLEVAGE POUR CHANGER D'ESPÈCE ». Une fois l'achat armé, un second bouton
fait maintenant défiler les espèces ouvertes, et remet le compteur d'armement à quatre
secondes à chaque passage : parcourir la liste ne désarme plus.

Sauf que le premier jet posait ce bouton **après** le test du prix, et c'était un cul-de-sac
mesuré : on désignait les cochons avec neuf cents euros en poche, le bandeau répondait
« ENCLOS : IL MANQUE 1 900 € » en gris, et plus rien ne ramenait au choix — on pouvait payer
un poulailler et ne plus jamais en poser un. Pire, `especeChoisie` n'est pas dans la
sauvegarde : un rechargement le remettait sur les **vaches**, à trois mille cinq cents euros.
Le défilement sort donc **toujours**, quel que soit l'argent et quel que soit le palier, et il
sort en premier.

Ensuite **agrandir l'enclos et rallonger la mangeoire**. Leurs deux boutons vivent dans le
rayon Élevage, et la seule porte du monde qui y menait était la ligne « … · COMPLET » du
bandeau — conditionnée à un enclos **plein**. Or la mangeoire est justement ce qu'on veut
rallonger *avant* de partir en tournée ; il fallait d'abord acheter toutes les bêtes, et une
seule bête embarquée pour la boucherie refermait la porte. Le quai d'un enclos porte
maintenant cette ligne en permanence.

Et enfin un détail qui n'était pas une porte manquante mais un mensonge : aux paliers 1 à 3,
aucune espèce n'étant ouverte, le bouton de la parcelle annonçait « **VACHES — NIVEAU 8
REQUIS** » — quatre paliers d'attente de trop, alors que le poulailler ouvre au quatrième. Il
nomme désormais l'espèce la plus proche d'ouvrir.

## Un onglet, une question

Une fenêtre répondait à deux questions à la fois. Le **stockage** disait ce qu'on a *et* ce
que le stock permettrait d'en produire ; la **production** listait les métiers, leurs
réglages *et* le potentiel du magasin, dans la même colonne de quatre-vingts lignes. Les
trois fenêtres n'avaient qu'un écran chacune — « un titre, une liste, une croix, rien
d'autre » — ce qui était juste tant qu'elles ne portaient qu'un sujet.

Elles portent maintenant **la barre d'onglets du menu**, à la pastille près : le joueur en
connaît déjà le geste, et deux barres d'onglets différentes dans le même jeu seraient une
leçon à réapprendre pour rien.

| fenêtre | onglet | ce qu'on y trouve |
|---|---|---|
| **Stockage** | En magasin | le silo, l'entrepôt, et ce qui roule dans les bennes |
| | Ce que ça devient | par matière détenue, ses débouchés chiffrés — **sans un seul bouton** |
| **Production** | Produire | la file en cours, puis **un bouton par métier acheté** |
| | Métiers | **les huit métiers** avec leur recette, leur temps, leur prix |
| | Améliorations | la capacité, la vitesse, la file |
| **Acheter** | Véhicules · Outils | *voir le garage, plus haut* |
| **Améliorer** | Véhicules · Outils | *idem* |
| **Prix des commerces** | *(sans onglet)* | il ne pose qu'une question |

**« Ce que le stock permet » a fait deux fois le voyage.** Ce bloc vivait d'abord dans la
production ; il en est parti parce qu'il ne parle pas de l'atelier mais du stock — combien
de farine dort dans le blé qu'on a — et il a emporté avec lui le bouton *Produire*, ce qui
était l'erreur : on ouvrait le stock pour faire tourner l'atelier. Le **bouton** est
revenu à l'atelier, dans son onglet *Produire*, et le stock a gardé la **question**, sous le
nom « ce que ça devient ». Chacun sa moitié, et cette fois c'est la bonne : *qu'est-ce que
ma matière vaudrait transformée* est une question de stock, *lance ce lot* est un geste
d'atelier. Dans les deux, **ce qui sort aujourd'hui vient en premier** : la liste suivait
l'ordre du tableau, si bien qu'un atelier à deux métiers montrait six lignes grises avant la
première ligne verte — et c'est la ligne verte qu'on vient chercher.

**Les huit métiers sont tous montrés, et chacun se monte pour lui-même.** L'écran n'en
proposait qu'un, le prochain de la liste : on découvrait la cave en arrivant à la cave, et
pour l'avoir il fallait payer les sept autres, alors que le palier de campagne est déjà là
pour dire à quoi on a droit. L'ordre du tableau ne décide plus que de la **silhouette du
bâtiment** — la liste des modules est retriée à chaque achat, exactement comme elle l'est à
la relecture d'une sauvegarde, sinon la cave pousserait avant le moulin.

L'onglet ouvert est retenu **par fenêtre**, hors de la fonction qui dessine : n'importe quel
geste redessine l'écran, et une mémoire locale ramènerait au premier onglet à chaque achat.
Et cet aiguillage-ci **a un repli**, à la différence de celui du panneau : il porte dix
vues au lieu de trois écrans, et une entrée oubliée laisserait la fenêtre vide, *le jeu en
pause*, sans rien pour comprendre pourquoi.

### Produire se fait à l'atelier, plus au stock

Le bouton qui LANCE un lot vivait dans la fenêtre du **stock**, sous « production
possible » : pour transformer du blé en farine, il fallait ouvrir le stock. Le joueur :

> « Je veux que la production se passe dans l'onglet produire, dans les petits boutons
> produire. Là, aujourd'hui, pour produire on est obligé de passer par le stock, je veux
> pas. Pour la production, faut que ça passe par le bouton de l'atelier de production ; il
> y aura donc un onglet pour acheter des nouveaux métiers, pour les améliorer, et pour
> produire. »

Trois onglets, trois questions : **qu'est-ce que je lance**, **qu'est-ce que j'achète**,
**qu'est-ce que j'améliore**. La file d'attente monte dans *Produire* — c'est ce qu'on vient
regarder — et *Métiers* ne garde que les huit lignes d'achat. Le guidage suit : un objectif
`produire` ouvre désormais **Production · Produire**, et plus **Stockage · possible**.

Et le stock, en échange, **détaille**. Le joueur : « tu peux détailler le produit qu'on a, et
marquer en dessous ce que ça peut devenir, pour que ce soit suffisamment lisible et
détaillé. » L'onglet s'appelle donc *Ce que ça devient*, et il liste, matière par matière et
du plus gros tas au plus petit : le métier qui la reprend, ce que le magasin **entier**
permet d'en sortir, la conversion pour cent kilos engagés, et le gain de la transformation en
euros. Aucun bouton : une ligne en tête dit où l'on va pour lancer.

Un piège au passage, trouvé en regardant l'écran : la première version divisait la quantité
détenue par la seule dose de la matière qu'on regardait, et annonçait **1 227 kg d'aliment
premium pour 400 kg d'orge** — une recette à trois entrées, dont on ne comptait qu'une. Le
chiffre passe par `potentiel()`, qui prend l'ingrédient le plus court, et la ligne dit
lequel : « limité par le blé ».

## L'atelier : huit métiers, trois réglages

Il portait cinq paliers, chacun donnant à la fois un module et de la capacité, et le
premier était offert. Les deux choses se séparent.

**Huit métiers**, qu'on monte un par un — et chacun a son propre temps, qui dit sa
valeur :

| | | les 100 kg engagés |
|---|---|---|
| Moulin | blé → farine | 90 s |
| Broyeur | maïs → aliment | 65 s |
| Mélangeur premium | maïs + orge + avoine → aliment premium | 130 s |
| Fromagerie | lait → fromage | 400 s |
| Fromagerie de brebis | lait de brebis → fromage de brebis | 530 s |
| Pressoir à colza | colza → huile | 265 s |
| Pressoir à olives | olives → huile d'olive | 400 s |
| Cave | raisin → vin | 530 s |

(Ces durées ont été multipliées par 4,44 en même temps que les volumes ont été divisés
d'autant : le temps de traiter **une parcelle** de récolte n'a pas bougé d'une seconde —
3 min 40 pour une parcelle de blé au moulin, 16 min 30 pour une parcelle de raisin à la
cave.)

**Trois réglages universels**, qui ne donnent aucun métier neuf mais changent le
rythme : la **capacité** d'un lot (20 → 45 → 85 → 170 kg de matière engagée), la
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
fabriquer, à 48,90 € le kilo contre 34,50.

La fromagerie du village reste utile : elle achète le lait directement. Le choix est
donc entier — lait à la fromagerie, argent tout de suite ; ou lait à l'atelier, fromage
au restaurant, davantage d'argent contre du temps et du transport.

### On ne se cogne plus dans le vide en longeant l'atelier

*« Quand on passe sur le côté droit, on se cogne alors qu'on est loin de le toucher. »*
L'emprise de collision était **un rectangle centré** sur le bâtiment, dont le demi-côté
valait `max(débord gauche, débord droit)`. Or l'atelier ne pousse pas de front : la
trémie, le hangar d'aliment, la fromagerie et le conteneur s'ajoutent tous **à gauche**,
le pressoir et l'appentis n'arrivent à droite qu'aux paliers 6 et 7. Le côté droit
héritait donc de la largeur du gauche.

| palier | débord gauche | débord droit | mur fantôme à droite |
|---|---|---|---|
| 0–1 | 8,6–8,9 m | 5,6–5,8 m | **3,1 m** |
| 2–3 | 9,9–10,2 m | 6,1–6,4 m | **3,8 m** |
| 4–5 | 11,8–12,1 m | 6,7–7,0 m | **5,1 m** |
| 6 | 12,4 m | 11,1 m | 1,3 m |
| 7–8 | 12,7–13,0 m | 12,6–12,9 m | 0,1 m |

Le pire tombe précisément quand la fromagerie arrive et que la droite n'a encore rien.
Mesuré en poussant un vrai tracteur contre la façade est, au palier 5 il s'arrêtait à
x = 97,45 alors que le mur est à 91,02 : **5,08 m de vide**, plus qu'une largeur de
machine. Le couloir libre du côté est passait de 12,3 m à 7,2 m — 41 % mangés par rien.

L'emprise se pose maintenant en **deux ou trois rectangles** — l'annexe de gauche, le
corps, celle de droite — chacun mesuré sur ce qu'il contient vraiment. Un obstacle ne
sait pas faire un L, mais trois obstacles côte à côte le font très bien, et la boucle de
collision n'en parcourt que deux de plus. Relevé après : **0,00 à 0,04 m** de mur fantôme
aux neuf paliers, et rien de solide laissé dehors.

**La profondeur se mesure aussi.** Elle était *déclarée* — la cote `D` du modèle — et le
bâtiment la dépassait : les tanks de la fromagerie de 1,68 m par l'arrière dès le palier
4, le cuvier du pressoir de 1,69 m par l'avant à partir du palier 6. On roulait au
travers. Ce qui *sélectionne* les maillages reste leur centre, à un mètre près de la
profondeur déclarée : sans ce filtre, le conteneur et l'auvent du quai, plantés devant,
allongeraient l'emprise jusqu'à interdire le quai. C'est un compromis assumé — les deux
poteaux de l'auvent restent traversables.

### La dalle du quai, et rien qu'elle

Le quai de l'atelier portait **trois bandes blanches** — des places de parking dessinées
avec le bâtiment. Elles disaient *« garez-vous ici »*, ce qui est faux : l'atelier se
sert tout seul au silo et à l'entrepôt, il n'y a rien à venir y faire, et il n'a même plus
d'anneau. Elles **grandissaient** en plus avec les paliers : le même trait de 0,165 m,
mais un entraxe de 2,31 m au premier cran contre 3,79 m au huitième, soit +64 % — trois
places trop étroites pour un pick-up qui devenaient trois places larges. Un marquage qui
s'étire n'est plus un marquage. Au palier 8, une des caisses de bois enjambait carrément
la bande de gauche.

Elles n'étaient l'exception nulle part ailleurs : **tous** les autres marquages du jeu
sont *peints dans la texture du sol* — la cour de ferme et le garage par
`marquageParking()`, les quinze parvis de commerce par `buildCommerce`, l'allée de la cour
de transformation par `paintStaticGround` — à la largeur canonique 4/PPU = 0,344 m. Ces trois-là étaient de la géométrie posée par-dessus la
dalle, 3 maillages et 36 triangles. Elles partent ; il reste le béton et son liseré, qui
n'ont jamais rien promis.

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
  dans l'ordre, avec l'outil qu'il porte, en escargot. La moissonneuse va vider au
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
l'arrivée veut bien prendre : trois céréales pour l'usine de céréales, l'avoine seule pour
l'usine d'avoine, les quatre grains que mangent les bêtes pour une pâture. Les deux tables
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

## La circulation de la rocade

Elle existait depuis le premier jour, **éteinte** : les modèles, le tracé, l'attelage
articulé, tout était là derrière un `NB_VEHICULES = 0`. Ce qui manquait n'était pas le
code mais une idée juste de ce qu'est une route de passage — et il a fallu trois versions
ratées pour l'attraper.

### Trois versions, et pourquoi les deux premières échouent

1. **L'ANNEAU.** Les véhicules faisaient le tour des quatre brins indéfiniment : on
   reconnaissait la même berline tous les trois quarts de minute.
2. **LES ITINÉRAIRES OUVERTS AVEC ARBITRAGE AU CARREFOUR.** Chacun entre par un bord et
   ressort par un autre — c'était la bonne idée —, mais il fallait bien empêcher deux
   trajectoires de se couper, et l'on s'y prenait **en freinant** : priorité de chaussée,
   puis classement de préséance à quatre rangs, puis places de carrefour réservées avec
   file d'attente. Chaque règle était juste et chacune arrangeait un cas ; ensemble elles
   faisaient des embouteillages. Mesuré sur la dernière : **74 % des véhicules collés à
   celui de devant, des pelotons de sept, et vingt-six traversées en cinq minutes** là où
   il en fallait cent cinquante. Le joueur a vu exactement cela — « ils tournent en rond
   et se retrouvent les uns derrière les autres ».
3. **LE FLUX VÉRIFIÉ À L'ENTRÉE**, celle d'aujourd'hui.

Le défaut commun aux deux premières est de **décider trop tard**. Freiner, c'est résoudre
au dernier moment un conflit qu'on aurait pu ne jamais créer.

### On décide à l'entrée, et une fois pour toutes

Un véhicule roule **à vitesse constante** d'un bout à l'autre de son trajet, et son trajet
n'est accepté que si, sur toute sa durée, il ne s'approche jamais trop d'un seul de ceux
qui roulent déjà. S'il ne passe pas, on ne le fait pas entrer : on attend une seconde et
l'on retire au sort. Personne ne freine donc jamais, personne ne s'arrête, et aucun peloton
ne peut se former — non pas « rarement », mais **jamais**, et sans qu'aucun réglage de
seuil n'ait à être juste.

La vérification tient en deux tests **exacts**, et non en un échantillonnage :

- **Dans une même file**, deux véhicules à vitesse constante ont un écart qui varie
  *linéairement* dans le temps. Il suffit donc de le calculer aux deux bouts de la période
  où ils partagent la file : s'il tient à ces deux instants, il tient partout entre les
  deux. Vingt mètres entre carrosseries.
- **À un carrefour**, chacun l'occupe pendant un intervalle de temps qu'on sait calculer
  d'avance — du moment où son capot y entre à celui où sa remorque en sort. Deux
  intervalles disjoints, c'est deux véhicules qui ne se rencontrent pas. Sont dispensés
  ceux qui suivent la même chaussée sans y tourner : les deux sens d'une route se croisent
  mille fois par partie sans jamais se toucher, et les mettre à la file viderait la route
  pour rien.

**Les quarante itinéraires possibles sont bâtis au chargement** — huit files, et pour
chacune un trajet tout droit plus quatre virages — et ils se *partagent* entre les
véhicules qui les empruntent. Rien n'y est jamais écrit.

### Les routes ne s'arrêtent pas

Elles commencent et finissent quarante-deux mètres au-delà du monde dessiné : un véhicule
est **déjà lancé, et à sa place dans la circulation**, quand il paraît au bord de la carte,
et il continue tout droit quand il en sort. On le cache dès que sa carrosserie a
entièrement quitté le monde — le bitume peint s'arrête là lui aussi, et il n'y a plus de
sol dessous. Au passage, cela corrige un défaut ancien : les véhicules roulaient jusque-là
trente-quatre mètres **au-dessus du vide**, en projetant leur ombre sur rien.

Trois voitures sur dix tournent une fois puis continuent jusqu'au bout ; les sept autres
traversent sans dévier. Les semi-remorques ne tournent jamais — vingt-sept mètres
d'attelage dans un carrefour de village, c'est le trottoir (mesuré : deux mètres de
bas-côté balayés).

### Les quatre pièges qu'il a fallu mesurer pour voir

- **La boîte d'un carrefour se mesure, elle ne se choisit pas.** Elle valait 7,50 m de
  demi-côté, « la chaussée plus deux mètres cinquante », choisis à vue. Or ce qu'un
  véhicule doit éviter, c'est la bande où passe la carrosserie de ceux qui viennent de
  l'autre route : la file d'en face plus la demi-largeur d'un camion, soit **5,10 m**.
  L'occupation étant proportionnelle à la taille de la boîte, chacun la bloquait moitié
  plus longtemps qu'il n'était nécessaire, les créneaux ne se trouvaient plus, et le semeur
  ralentissait les arrivants **jusqu'à quatre mètres par seconde** pour leur en fabriquer —
  ce qui les faisait occuper le carrefour encore plus longtemps. Une spirale, qui a mis la
  rocade au pas.
- **On cherche son créneau en changeant de route, pas en ralentissant.** D'où deux crans de
  vitesse au plus, et cinq tracés essayés : les cinq trajets d'une file franchissent les
  carrefours à des instants très différents, c'est là qu'est le jeu.
- **Le tirage se biaisait tout seul, deux fois.** D'abord parce qu'on retirait le type à
  chaque essai : un trajet qui tourne libère sa file au carrefour, il se glisse donc plus
  facilement qu'un trajet tout droit qui l'occupe d'un bout à l'autre — on demandait une
  voiture sur quatre qui tourne, il en passait **sept sur dix**. Ensuite parce qu'un trajet
  tout droit n'a qu'une seule forme par file : il ne peut chercher son créneau qu'en jouant
  sur la vitesse, là où un virage a cinq tracés au choix. On lui accorde donc plus de crans.
- **Qui tourne occupe tout son arc**, et pas seulement la boîte : la boîte fait onze mètres
  de côté, l'arc en fait treize à dix-sept. Une voiture qui pivote balayait encore la
  chaussée quand son intervalle était fini — un frôlement à cinquante centimètres, une fois
  en cinq minutes. Une fois de trop : le système est fait pour que ce soit jamais.

### Ce que ça donne

Mesuré sur quinze minutes, à la cadence de l'époque — vingt-huit places dans le vivier et
vingt-deux véhicules vivants en moyenne ; la cadence a depuis été divisée par trois, voir
plus haut :

| | avant (arbitrage au frein) | après (flux vérifié) |
|---|---|---|
| véhicules collés à celui de devant | 74 % | **1,7 %** |
| plus long peloton | 7 | **3** |
| traversées complètes en 5 min | 26 | **139** |
| images où quelqu'un freine | — | **0** |
| dégagement au plus juste | −4,4 m (contact) | **+0,21 m** |
| images hors chaussée | 0 | **0** |

Cadence : une voiture toutes les **7,6 à 8,4 s** sur chacune des quatre routes — la
fourchette demandée était 4 à 10. Dix-huit véhicules visibles à la fois en moyenne, vingt-
trois au plus. Débord de carrosserie en virage : 0,90 m pour une voiture, 0,09 m pour un
camion — et 0,94 m depuis que l'autocar roule, qui est le plus long des seize.

### Puis la cadence a été divisée par trois

Dix-huit véhicules en vue en permanence, c'est le trafic d'une rocade urbaine aux heures
de pointe, pas celui qu'on voit d'une ferme. L'intervalle entre deux départs sur une file
passe donc de 7–16 s à **21–48**, et la part de semi-remorques de un sur six à **un sur
quatorze**. Les parts de modèles se déplacent dans le même sens : voitures 64 % au lieu de
56, camions de travail 18 au lieu de 23, secours 2 au lieu de 3.

| | avant | après |
|---|---|---|
| véhicules en vue, en moyenne | 17,8 | **6,8** |
| cadence par route | 7,5 à 8,8 s | 15 à 20 s |
| traversées complètes en 5 min | 127 | 70 |
| attelages en 5 min | 34 | **3** |
| dégagement au plus juste | +0,21 m | +0,67 m |
| plus long peloton | 2 | 2 |
| contacts, images hors chaussée | 0 | 0 |

Le débit tombe de 127 à 70 et non de 127 à 42, et la raison est intéressante : à l'ancienne
cadence, la rocade était **saturée** — un départ sur deux ne trouvait pas son créneau et
n'avait pas lieu. Le réglage était donc à 11,5 s de moyenne mais le débit réel à 20. À
34,5 s de moyenne, plus rien n'échoue : le débit vaut exactement la cadence, huit files ×
300 s ÷ 34,5 = 69,6, mesuré 70. Ce qui a été divisé par trois, c'est le RÉGLAGE ; ce qu'on
voit à l'écran est divisé par deux et demi.

**Et le vivier suit.** Vingt-huit places étaient calibrées sur l'ancienne cadence ; mesuré
sur dix minutes, il n'y a plus jamais plus de **treize** véhicules vivants à la fois, 9,2 en
moyenne. Il en garde **dix-huit** — cinq de marge sur le pire cas, et pas un départ refusé
faute de place sur la mesure. Les objets de scène tombent de 2 472 à **2 331** : cent
quarante et un de moins à traverser à chaque image pour ne rien montrer.

**Et cela se paie en temps de calcul, dans le bon sens.** `updateTrafic` tourne sur les
véhicules vivants, pas sur les places : son coût par appel tombe de **17,0 à 7,2 µs**. Le
rendu logiciel du banc fait trop de bruit pour qu'une mesure d'images par seconde tranche
quoi que ce soit, mais elle penche du même côté — 7,59 le jour et 8,26 la nuit contre 7,29
et 7,89, avec douze véhicules à l'écran au lieu de vingt-deux, et le même nombre d'appels
de rendu.

Le seul dégagement qui reste juste est celui de **deux semis qui se croisent** : 0,21 m. Ce
n'est pas un réglage mais une fatalité géométrique — voir plus bas.

### À l'échelle une et demie, sauf en largeur pour les poids lourds

Les véhicules avaient été dessinés plus petits que les engins de la ferme — une berline de
4,40 m à côté d'un tracteur de 4,80 — et la route, vue de la cour, avait l'air d'un circuit
de voitures miniatures. Le facteur porte sur *tout* : la caisse, mais aussi la sellette, le
timon de la remorque et les distances de sécurité.

Sauf que les camions du modèle sont taillés large : **5,73 m** de carrosserie une fois
grandis d'une moitié, sur une chaussée de dix. Deux files à 2,60 m de part et d'autre de
l'axe laissent 5,20 m entre les deux essieux de file — un demi-mètre de moins qu'il n'en
faut, et deux semis qui se croisaient se traversaient. On ne peut ni élargir la rocade,
dont le bord dessine la cour de ferme, ni écarter les files sans sortir du bitume. Le camion
est donc **affiné de treize pour cent en largeur seulement** : sa longueur et sa hauteur
restent à une fois et demie — c'est là que se lit la taille.

**La remorque suit le rail, elle n'est plus traînée.** Le modèle traîné est celui des outils
de la ferme, et il est juste tant que le timon est plus *court* que le rayon du virage. À
cette échelle le timon d'un semi fait douze mètres et les virages huit à onze : la remorque
coupait le coin en ligne droite — cinq mètres soixante dans l'herbe, essieux au ras de la
clôture. Posée sur le tracé, un timon d'abscisse curviligne derrière le tracteur, elle reste
dans sa file au centimètre, et son cap diffère naturellement de celui du tracteur dans les
courbes. Débord ramené de 5,60 m à 2,17.

**Le camion orange n'a plus qu'une remorque : la citerne.** Le plateau porte-engins et le
fourgon restent écrits — ils ne coûtent rien tant qu'on ne les fabrique pas — mais ne sont
plus assemblés.

### La citerne entrait dans la cabine

Le joueur l'a vu en virage : *« fais un peu plus d'espace entre la cabine et la remorque
pour que, quand le camion s'articule, la remorque ne rentre pas trop en collision avec la
cabine. »* Mesuré sur la géométrie, il avait raison à vingt-deux centimètres près : le dos
de la cabine est à z = −3,00, le nez du fût à −2,78 une fois la sellette déduite. Et les
deux caisses n'ont pas la même suspension — elles tanguent chacune de son côté et se
traversent au premier dos d'âne, même en ligne droite.

L'espace nécessaire ne se choisit pas à l'œil, il se calcule. Le coin avant du fût est à
2,50 m de l'axe de la remorque ; quand l'attelage se plie d'un angle θ, ce coin **avance**
de 2,50 · sin θ. Un jeu de 0,22 m ne tenait donc que jusqu'à 5° — autant dire jamais. La
sellette recule de 1,60 à **2,35** fois l'échelle du trafic : le jeu passe à **0,91 m**,
et l'attelage tient jusqu'à **vingt-trois degrés**, plus que ce qu'un virage de la rocade
lui demande jamais.

Reculer la sellette allonge l'attelage d'autant, et c'est la seule chose qu'il fallait
vérifier : le timon se mesure depuis la sellette, donc l'essieu de la remorque recule avec
elle et l'ensemble prend 1,12 m. Ce qui décide si la remorque monte sur l'herbe, ce n'est
pas cette longueur mais le tracé qu'elle suit — elle est posée dessus, pas traînée — et le
banc le confirme : sur cinq minutes de rocade, **zéro image hors chaussée** et zéro contact,
comme avant.

### Les phares du camion étaient enfoncés dans sa calandre

Ils sont là depuis le portage : deux pavés crème de 0,42 × 0,30 × 0,16 à 1,02 m de l'axe.
Mais ils occupent z ∈ [5,00 ; 5,16] quand la calandre, elle, avance jusqu'à 5,20 : **leur
face avant est derrière celle de la calandre**. Il n'en dépassait que deux liserés de vingt
centimètres sur les côtés, et le camion paraissait n'avoir pas de phares du tout. C'est le
patron du monospace qu'on reprend — entourage sombre, lentille par-dessus, « posés sur la
calandre, non enfoncés » —, calé pour rester en deçà du pare-chocs : le porte-à-faux avant
ne bouge pas, et avec lui la ligne d'entrée des carrefours.

### Tout le trafic s'allume la nuit

*Ce qui suit décrit l'état d'alors ; la section suivante dit ce que le joueur en a fait.*

Un véhicule de passage portait les mêmes lumières qu'un engin de la ferme, et par le même
mécanisme : deux billes additives crème devant, deux rouges derrière — **sur la citerne**
pour un attelage, sur la caisse pour une voiture —, et deux faisceaux en tronc de cône. Les
lumières sont **enfants de la carrosserie** : elles prennent le cap, le roulis et le
pompage de la suspension, et le faisceau balayait le paysage quand la voiture passait une
bosse.

Le calcul des cotes du faisceau — pente déduite de la hauteur du phare, longueur coupée là
où sa génératrice basse touche le sol, écrasement de moitié — était écrit au milieu de la
construction des éclairages de nuit. Il est devenu une fonction, `reglageFaisceau()`, et il
a **servi deux fois** : un tracteur et une berline de passage éclairaient selon la même
règle. Vérifié par différentiel : les faisceaux des sept engins du joueur sont inchangés au
bit près après l'extraction. Depuis que la rocade n'éclaire plus, il ne sert qu'à la ferme —
et la fonction reste, parce qu'une règle de géométrie n'a pas à vivre au milieu d'une boucle
d'affichage.

Deux économies avaient été trouvées, parce qu'il y avait vingt-deux véhicules et non sept :

- **les faisceaux ne s'allument que de près** (95 m). Deux troncs additifs par véhicule sur
  toute la carte, cela fait quarante volumes transparents à remplir pour des voitures
  grosses comme un ongle ; au-delà, les deux billes disent déjà tout ce qu'il y a à savoir —
  qu'une voiture arrive, et par où. Cinq ou six faisceaux allumés à la fois, mesuré ;
- **huit pans sur quatre anneaux** pour un cône de décor, au lieu des quatorze sur huit des
  engins du joueur : 224 triangles économisés par phare. La finesse est un argument par
  défaut de `faisceauPhare()`, les engins gardent la leur.

### Puis le trafic a cessé d'éclairer

*« Pour les véhicules du trafic ne mets pas l'effet d'éclairage, fais juste allumer les
phares en jaune mais ne mets pas l'effet d'éclairage au sol. »*

Les deux économies ci-dessus rendaient le cône **moins cher**. Elles ne répondaient pas à la
question de savoir s'il avait sa place. Il ne l'avait pas : on ne conduit pas ces
voitures-là, et un phare qui repeint la chaussée devant une voiture qu'on ne pilote pas est
un effet pour personne. Les trente-six cônes du vivier sont donc **supprimés**, et non
éteints — un objet qu'on garde invisible coûte encore son parcours de scène, et revient au
premier réglage distrait.

| mesuré, la nuit | avec | sans |
|---|---|---|
| maillages de faisceau dans la scène | 50 | **14** (ceux du joueur) |
| triangles de géométrie | 5 440 | 3 136 |
| objets de scène | 2 329 | 2 293 |
| triangles rendus, plein écran de nuit | 39 468 | 38 436 |
| appels de rendu | 567 | 564 |
| `majEclairagesNuit`, par appel | 2,05 µs | **1,65 µs** |

Le vrai gain ne se lit dans aucune de ces lignes. Échantillonné cent cinquante fois sur
trente secondes de nuit tenue : **6,37 cônes allumés en moyenne**, couvrant 10,7 % de
l'écran, 13,0 % au pire. Un cône est additif et peint des **deux côtés** — le regard le
traverse deux fois — si bien que c'est un cinquième de l'écran qui était repeint à chaque
image pour un éclairage que personne ne regardait.

Ce qui reste : **l'optique s'allume**. Elle brillait d'un crème 0xFFEFC0, qui est la couleur
du VERRE et non celle de la lumière — de loin, ça se lit comme un phare éteint qu'on
éclaire. Elle passe au **jaune 0xFFD24A**, une nuance en deçà du jaune du guidage pour qu'un
phare qui passe ne se confonde pas une seconde avec un cercle d'objectif, et elle monte d'un
tiers en opacité et en taille — 0,62 à 0,74, 0,85 + 0,30 k à 0,85 + 0,35 k — parce qu'elle
porte désormais seule ce que le cône disait.

Les **engins du joueur gardent leurs deux faisceaux chacun**, et c'est la moitié de la
demande : lui conduit, il a besoin de voir devant. Les vingt et un lampadaires gardent leur
flaque au sol. Le contrôle du banc porte sur la **géométrie** et non sur la visibilité —
`t.m.traverse(o => o.name === 'faisceauPhare')` doit rendre zéro pour le trafic et
quatorze pour la ferme — parce qu'un cône rendu invisible passerait un contrôle d'opacité
sans rien économiser.

Où sont les optiques de chaque modèle ? **On le note en les posant**, au lieu d'aller le
redécouvrir sur la boîte englobante : un monospace au museau court et une bétaillère à long
capot ne les portent pas au même endroit, et une lueur posée à côté de son verre se voit
tout de suite.

Coût mesuré de l'ensemble — le flux, les vingt-deux véhicules, et l'éclairage de nuit de
tous : **2 à 3 % des images**, de jour comme de nuit.

### Les seize de la planche

La planche du joueur en portait **seize** ; le jeu n'en faisait rouler que six. Les dix
autres roulent maintenant : pick-up, fourgon de livraison, camion à caisse, citerne à
lait, camion-benne, autocar de village, camping-car, camion de pompiers, fourgonnette
postale, dépanneuse. Chacun est fusionné en **une** géométrie, donc un appel de rendu, et
tous sont bâtis avec les mêmes six pièces que les six premiers — châssis, serre ou
cabine-sandwich, feux, roues — ce qui est précisément ce qui les fait appartenir à la
même famille. Trois pièces manquaient et ont été ajoutées : la **caisse fermée** (le
fourgon, le camion à caisse et la postale portent le même volume à la taille près), le
**gyrophare**, et une boîte **penchée** — le plateau incliné de la dépanneuse est le seul
volume du trafic qui ne soit pas d'aplomb.

Trois détails de portage, et le troisième était un vrai piège :

- la planche peignait en `DoubleSide`, ce qui masquait un enroulement de faces inversé sur
  les capots ; ici la matière n'a qu'une face, et il a fallu retourner les triangles ;
- la citerne à lait couche son fût **le long** du camion — une rotation autour de X, pas
  de Z. Tournée sur Z elle se mettrait en travers de la route ;
- **le camion-benne tirait son gravier au sort.** Cinq `Math.random()` dans la
  construction de la géométrie : deux ouvertures du jeu n'auraient pas donné le même
  camion, et la règle du fichier est que le décor est tiré au sort mais **toujours le
  même**. Cinq largeurs écrites, et c'est réglé.

**Seize modèles tirés à égalité ne font pas un village.** Un camion de pompiers passerait
aussi souvent qu'une berline, et une dépanneuse toutes les seize voitures. Les parts se
lisent donc comme un pourcentage — elles font cent — dans l'esprit des deux autres tirages
du trafic, `PART_LOURD` et `PART_VIRAGE`, qui sont eux aussi des parts écrites en clair :

| | | |
|---|---|---|
| **voitures** | 56 % | berline 14, citadine 13, break 11, monospace 9, pick-up 9 |
| **utilitaires** | 11 % | fourgon 8, postale 3 |
| **camions de travail** | 23 % | bétaillère 5, plateau à bottes 5, camion à caisse 5, citerne 4, benne 4 |
| **car et camping-car** | 7 % | autocar 4, camping-car 3 |
| **secours et dépannage** | 3 % | dépanneuse 2, pompiers 1 |

**Et chacun son allure — mais l'éventail reste étroit**, entre 0,90 et 1,05. C'est une
contrainte et non un goût : sur trois cent cinquante mètres de file, une voiture rapide
rattrape immanquablement une voiture lente, si loin devant soit-elle, et le créneau
n'existe alors pour personne. Quinze pour cent d'écart se voient sans rien casser. Un
**porteur** — un camion rigide — roule en plus sur le ressort long, celui de l'attelage :
c'est ce qui fait qu'une caisse haute dodeline là où une berline reste plate.

**Le gyrophare est un signal, pas un phare** — et il est **posé** sur son pavillon, non
flottant au-dessus. La planche le plaçait 31 cm au-dessus du toit de cabine des pompiers
et 37 cm au-dessus de celui de la postale : à l'échelle une et demie du trafic, cela fait
un demi-mètre d'air sous une lampe, et cela se voit tout de suite. Le socle mesure douze
centimètres : son centre va donc à `toit + 0,06`, mesuré au banc à zéro centimètre d'air
aux trois modèles. Sa bille, du coup, doit **traverser la tôle** — une lueur posée à
cheval sur un pavillon qui garde le test de profondeur se fait trancher au couteau et
l'on en voit un demi-disque ; c'est la même règle que le gyrophare des engins du joueur.
 Trois modèles en portent un — les pompiers
en bleu, la postale en bleu, la dépanneuse en orange. Il bat de jour comme de nuit, mais
le jour le lave : 0,29 d'opacité au plus fort du battement au soleil, 0,81 au clair de
lune. Sans cela on aurait au choix un feu de détresse en plein midi ou un camion de
pompiers aux dômes éteints qui ne servent à rien. Il ne balaie pas le paysage — un cône
de plus par véhicule pour un feu qui tourne coûterait cher pour un effet qu'on ne verrait
qu'en passant à côté. Et **une seule bille**, même quand le toit en porte deux : à trente
mètres une rampe se lit comme une lueur unique.

Ce que ça change, mesuré sur cinq minutes de circulation, six modèles contre seize :

| | 6 modèles | 16 modèles |
|---|---|---|
| véhicules visibles en moyenne | 18,4 | 17,8 |
| cadence par route | 6,8 à 9,4 s | 7,5 à 8,8 s |
| traversées complètes | 149 | 127 |
| images où quelqu'un freine | 0 | 0 |
| contacts entre carrosseries | 0 | 0 |
| pire dégagement | +0,21 m | +0,21 m |
| images hors chaussée | 0 | 0 |
| débord de carrosserie en virage | 0,90 m | 0,94 m |
| plus long peloton | 3 | **2** |

La cadence se **resserre** au lieu de s'étaler et le peloton raccourcit : les allures plus
variées désynchronisent les départs. Le débit perd 15 % — un autocar occupe son créneau
plus longtemps qu'une citadine — mais le nombre de véhicules à l'écran ne bouge que de
0,6, parce qu'ils y restent d'autant plus longtemps. On ne voit pas la différence.

Le coût, lui, se mesure sur ce qui ne bouge pas d'une exécution à l'autre, parce que le
rendu logiciel du banc fait trop de bruit pour qu'une mesure d'images par seconde dise
quoi que ce soit (7,1 à 8,0 le jour des deux côtés) :

| | 6 modèles | 16 modèles |
|---|---|---|
| `updateTrafic`, par appel | 18,9 µs | 17,0 µs |
| `majEclairagesNuit`, de nuit | 2,15 µs | 2,35 µs |
| triangles des modèles | 4 980 | 12 344 |
| géométries en mémoire | 175 Kio | 434 Kio (+265) |
| objets de scène | 2 416 | 2 472 |

Le temps de calcul ne bouge pas — c'est le nombre de véhicules qui compte, pas le nombre
de modèles — et 265 Kio de géométrie de plus se lisent contre les 57 Mio de textures que
le jeu porte déjà. Les 56 objets de scène en plus sont les vingt-huit billes de gyrophare
et leur halo, une par place du vivier, éteintes tant que la place ne porte pas un des
trois modèles qui en ont un.

Le trafic n'a **aucune emprise de collision** vis-à-vis du joueur, et c'est voulu :
`obstacles` est un tableau balayé à chaque image par le pilote, et y injecter vingt-deux
cercles mobiles transformerait un croisement en accrochage. On les traverse, comme tout le
décor mobile.

### Les dix nouveaux grandissent de huit pour cent, sauf ceux qui touchent les lampadaires

Portés tels quels, ils étaient plus fins que les six premiers : côte à côte au feu, un
fourgon avait l'air d'une maquette à côté d'une bétaillère. **Huit pour cent** les remettent
au même poids — le plus large des dix passe de 3,76 m à **4,05**, quand le semi affiné, qui
est le gabarit maximal de la rocade, en fait 4,99. Le facteur s'écrit par modèle dans
`TAILLE_TRAFIC`, et il porte à la fois sur la carrosserie, sur les dimensions qui servent au
suivi de file et sur la portée des phares — sans quoi un camion grandi éclairerait toujours
à la taille de l'ancien.

**Et ce n'est pas la chaussée qui borne la taille : c'est la hauteur libre sous les
lampadaires.** On cherchait la limite du mauvais côté. Le dessous de l'ampoule d'un
lampadaire est à **5,87 m** au-dessus de la route, et la potence passe au-dessus des files.
Le camping-car, le plus haut du lot, culmine à 5,82 m au repos — mais la suspension le
soulève et le fait tanguer, et il monte à **6,09 m** en roulant : à huit pour cent il
traversait la lampe de **vingt et un centimètres**, sur deux mille images de circulation.
Rien ne le disait, parce qu'aucun banc ne mesurait la hauteur libre. Deux contrôles la
mesurent maintenant, l'un au repos et l'autre sur cinq minutes de circulation.

Le facteur est donc **raboté par le calcul**, modèle par modèle, au lieu d'être écrit à la
main : une réserve de 45 cm — les 30 cm de suspension mesurés, plus 15 de jeu — et le reste
suit tout seul si un modèle grandit ou si les lampadaires bougent. Quatre des seize sont
rabotés : le camion à caisse et la citerne à lait à 6,6 %, l'autocar à 7,5 %, et le
camping-car à **0,6 %** — il ne peut pas grandir, il est déjà au plafond. Mesuré sur cinq
minutes, il reste **15,3 cm** entre la tôle la plus haute et l'ampoule la plus basse.

### Quarante-trois robes pour seize carrosseries

Deux berlines identiques qui se croisent, on les voit ; trois, on ne voit plus qu'elles.
Chaque modèle reçoit donc des teintes de plus que celle de sa planche, et le vivier tire au
sort à la naissance. Le compte exact, pour qui vient vérifier : douze modèles en reçoivent
deux, le camion à caisse trois, et trois n'en reçoivent aucune — **quarante-trois
géométries** pour seize carrosseries.

Ce qui rend la chose gratuite tient en deux lignes : une variante **partage les positions
et les normales** de son original et ne possède que son propre tableau de couleurs. Ce sont
les mêmes sommets aux mêmes endroits — seule la couleur change. Vingt-sept variantes ne
coûtent donc que vingt-sept tableaux de couleurs, pas vingt-sept maillages.

Et la teinte ne se pose pas au hasard sur les sommets : chaque modèle **déclare sa robe**
au moment où il se dessine — la couleur de sa caisse, et éventuellement celle de son accent
— et le repeint ne touche que les sommets qui portaient exactement l'une des deux. Les
roues, les vitres, les pare-chocs et les feux gardent leur couleur, comme sur une vraie
voiture. L'accent, lui, se reporte en **rapport** et non en valeur absolue : la bande de
toit d'un autocar ambre est d'un ambre plus sombre, celle d'un monospace anthracite d'un
anthracite plus sombre, sans qu'on ait eu à l'écrire.

**Trois modèles n'ont qu'une robe, et c'est voulu** : un camion de pompiers est rouge, une
fourgonnette postale est jaune, et le car du village est jaune lui aussi. Ce n'est pas une
couleur, c'est une livrée — la repeindre en vert donnerait un véhicule qu'on ne reconnaît
plus.

**Le piège du remplacement par égalité : une couleur, un rôle.** Substituer par valeur veut
dire que deux pièces qui partagent exactement la même teinte changent ensemble, qu'on le
veuille ou non. Le camion à caisse avait pour robe le rouge des **feux arrière** : ses
soixante-douze sommets de feux passaient au bleu avec la caisse, et le camion roulait avec
des veilleuses bleues. La dépanneuse avait pour robe l'orange de son **gyrophare** : le dôme
changeait de couleur tandis que la bille de halo, elle, restait orange. Les deux pièces ont
donc reçu leur propre teinte — un rouge de feu et un orange de gyrophare distincts d'un
demi-pour-cent, invisibles à l'œil — et la règle est écrite là où on la lit : une couleur,
un rôle. Vérifié sommet par sommet : soixante-douze feux et soixante-douze sommets de dôme,
zéro qui bouge.

Un troisième cas dormait depuis le début : la variante bleue du fourgon valait exactement le
bleu de son **marquage latéral**. Sur un fourgon sur trois, les trente-six sommets du bandeau
fusionnaient dans la tôle et le van roulait tout nu. Le contrôle qui l'a trouvé est
maintenant au banc, et il est général : on compte les couleurs distinctes de chaque géométrie
et l'on exige qu'une variante en ait autant que son original. Une pièce qui disparaît, c'est
une couleur en moins.

Le coût est celui qu'on attend, et il est mesuré : les seize carrosseries pèsent 1 302 Kio
d'attributs, les quarante-trois géométries **2 032** — 730 Kio pour vingt-sept robes, quand
les recopier entièrement en aurait coûté 1 460 de plus. À comparer aux cinquante-sept
mégaoctets de textures que le jeu porte déjà. Le temps de calcul par image ne bouge pas : on
ne fabrique rien à la naissance, on désigne une géométrie déjà construite.

### Et plus un seul rouge sur la rocade

*« Je veux plus de rouge, puisque moi je l'ai en tant que véhicule perso, je veux pas qu'on
confonde. »* Le joueur pilote un **tracteur rouge** — 0xD44435, la deuxième des trois robes
du parc.

La part du problème se mesure. En tirant deux cent mille véhicules avec le vrai tirage de
modèle et le vrai tirage de robe : **21,3 % du trafic portait une carrosserie rouge ou
brique**, dont 14,6 % de rouge franc. Un véhicule sur cinq. Et ce n'était pas une affaire de
nuance : les rouges de la rocade tombaient à un à cinq degrés de teinte de celui du
tracteur, seulement plus sombres — 0xC0392B pour 6,95 % des passages, 0x9C3B33 pour 5,63,
0x8E4436 pour 5,39, 0xB8342A pour 2,01, 0xA8443A pour 1,32.

Sept teintes changent donc de main, et l'une d'elles était une **carrosserie d'origine** :

| modèle | ce qui était rouge | ce qui le remplace |
|---|---|---|
| berline | bordeaux 0x9C3B33 | kaki 0x6B7040 |
| break | brun-rouge 0x8E4436 *(sa robe d'origine)* | brun-taupe 0x7A6A52 |
| citadine | rouge 0xC0392B | sarcelle 0x357F72 |
| plateau à bottes | brique 0xA8443A | moutarde 0xB08A2E |
| benne | brique 0x8E4436 | brun-taupe 0x7A6A52 |
| camion à caisse | rouge 0xC0392B *(sa robe d'origine)* | bleu 0x2F6B8E |
| dépanneuse | rouge 0xC0392B | ardoise 0x4A5560 |

Mesuré sur la même simulation de deux cent mille véhicules : **1,02 %**, et c'est le camion
de pompiers, seul. On le garde rouge, et l'argument tient en une phrase : personne ne prend
un fourgon d'incendie à échelle et gyrophares pour un tracteur.

**Le car du village n'a plus qu'une robe, et elle est jaune.** *« Le bus, tu le laisseras
qu'en jaune. »* C'est le bon instinct : un car repeint chaque semaine ne serait plus LE car
du village, celui qu'on reconnaît de loin. Il rejoint donc les pompiers et la postale au
rang des **livrées** — une couleur qui fait partie du modèle, pas un habillage.

**Et le camion à caisse en reçoit une de plus que tout le monde.** *« Le fourgon avec la
caisse, tu lui fais toutes les couleurs, sauf en rouge, qui était la couleur originale. »*
Il en a **quatre** — bleu, ardoise, kaki, crème — là où les autres en ont trois : c'est lui
qui était le rouge, on lui devait bien ça. Le compte final tombe de quarante-quatre
géométries à **quarante-trois** : l'autocar en perd deux, le camion à caisse en gagne une.

### Et il a cessé de tourner son gyrophare

*« Pour les véhicules du trafic, n'allume pas leur gyrophare. »* Trois modèles en portent un
— les pompiers, la fourgonnette postale, la dépanneuse — et leur lueur battait deux fois par
seconde, **de jour comme de nuit**, sur une route de campagne : trois véhicules en
intervention perpétuelle, pour un signal qui ne s'adresse à personne. On ne conduit pas ces
voitures-là.

La bille additive est retirée du vivier entier — trente-quatre lutins, dormants pour
trente et un d'entre eux — avec sa cote notée, sa pose à la naissance et son bloc
d'animation. Mesuré : **150 sprites dans la scène avant, 128 après**.

**Les dômes, eux, restent sculptés.** Ils font partie de la silhouette qui distingue une
dépanneuse d'un plateau, et ils sont fondus dans la même géométrie que le reste de la
carrosserie : ils ne coûtent rien de plus. Ce qui reste allumé sur le trafic tient en une
phrase — deux optiques jaunes devant, deux rouges derrière, et seulement la nuit.

### Et la couchette du camping-car s'est posée sur la cabine

Le joueur, en le voyant passer : « le camping-car, la couchette en haut de la cabine est
trop haute, elle ne touche pas le toit de la cabine de conduite ; descends-la pour qu'elle
touche. »

C'est vrai, et ça se mesure sans discuter. En sondant la géométrie fusionnée par une
colonne verticale — pour un x et un z donnés, les hauteurs où le rayon rencontre de la
matière —, sur tout le porte-à-faux (z de 1,50 à 2,85) : le toit de la cabine plafonne à
**2,14**, le plancher de la couchette commençait à **2,89**. **Soixante-quinze centimètres
d'air**, et un bloc pâle suspendu au-dessus du pare-brise.

Son plancher tombe à 2,14 pile. Et son toit **monte** à 3,04, celui de la cellule : la ligne
du dessus devient continue de l'arrière au pare-brise, ce que dit la première ligne de la
fonction — « la cellule la coiffe d'une capucine ». La descendre sans la grandir l'aurait
enfoncée vingt centimètres *sous* le toit de la cellule, ce qui n'est plus une capucine mais
un décrochement.

**Et le véhicule cesse d'être raboté.** Sa hauteur hors tout tombe de 3,59 à 3,19 — c'est la
trappe de toit qui devient le point haut. Le gabarit des lampadaires (5,87 m moins 45 cm de
battement de suspension) le bridait à 1,0065 fois sa taille, seul de sa catégorie : il
repasse à **1,08** comme les quinze autres, et se dresse tout de même **plus bas** sur la
route — 5,17 m contre 5,42.

**Aucun banc ne pouvait voir ce défaut**, parce qu'aucun ne regardait l'*intérieur* d'une
silhouette : on mesurait des emprises, des largeurs, des hauteurs hors tout, jamais ce qu'il
y a entre deux volumes. Le banc du trafic sonde maintenant les seize modèles par colonnes
verticales. Deux pièges ont dû être écartés pour que la mesure dise vrai :

- **la parité ne marche pas sur une union de boîtes qui se chevauchent.** Compter les
  traversées comme sur une surface fermée simple dit « dehors » dès qu'on entre dans une
  deuxième boîte sans être sorti de la première : la sonde annonçait 0,90 m de vide en plein
  milieu de la matière. On lit donc la **normale** de chaque face — vers le haut, c'est une
  sortie ; vers le bas, une entrée — et un compteur de profondeur s'occupe des
  recouvrements ;
- **un trou doit avoir du volume.** Une colonne tirée un centimètre en dehors d'une cabine
  ne rencontre que ses deux liserés de ceinture, qui dépassent d'un centimètre, et annonce
  0,75 m de « vide » là où il n'y a que du vitrage. On exige donc le trou des **deux côtés**
  de l'axe et sur **deux tranches voisines**.

Résultat : **0,00 m** sur les seize modèles, contre 0,75 sur le camping-car avant.

## Le son du moteur

Il y en avait déjà, en **synthèse pure** : deux dents de scie désaccordées passées au
filtre. Ça ne coûtait pas un octet, et c'était sa seule qualité — ça sonnait comme une
sirène de jouet. Deux vraies boucles les remplacent, et **tout le reste se fait avec
ces deux-là** :

| | échantillon | vitesse de lecture |
|---|---|---|
| Tracteur vert | diesel | 1,00 |
| Tracteur rouge / bleu | diesel | 0,94 / 0,88 |
| Moissonneuse | diesel | 0,76 |
| Enjambeuse | diesel | 1,14 |
| Pick-up / Fourgon | voiture | 1,06 / 0,86 |
| Trafic léger | voiture | 0,95 × la vitesse |
| Camion de la rocade | voiture | 0,58 × la vitesse |

Un moteur plus gros tourne plus bas : c'est la seule chose qu'il faut savoir, et un
troisième échantillon serait du poids pour rien. Le **filtre passe-bas** fait le reste — il
s'ouvre de 230 à 1 125 Hz avec l'effort, et c'est lui, bien plus que le volume, qui donne
l'impression d'un moteur qui force.

**Réséchantillonnées à 6 000 Hz, et c'est sans perte ici.** Les originaux sont à 44 100 Hz
et pèsent 280 000 caractères de base64 — vingt-sept pour cent de plus sur un fichier qui
doit tenir en un seul HTML et se télécharger sur mobile. Mesuré à la transformée de
Fourier : ces deux sons n'ont **rien** au-dessus de 2 000 Hz (0,000 000 % de l'énergie),
leur pic est à 105 et 114 Hz, et le jeu leur passe de toute façon un passe-bas à 240 Hz.
Six mille hertz laissent trois mille de bande passante, le double de ce qui s'y trouve, et
l'aller-retour 44 100 → 6 000 → 44 100 rend un écart de **0,006 %**. Ce qu'on gagne :
38 000 caractères au lieu de 280 000, soit 3,5 % du fichier au lieu de 21.

**Le trafic n'a que deux voix pour dix-huit places.** Chacune suit le plus proche de sa
sorte et son volume décroît au carré de la distance jusqu'à s'éteindre à cinquante-cinq
mètres. Dix-huit boucles tournant en permanence coûteraient dix-huit fois plus pour un
décor qu'on n'entend qu'un à la fois.

Deux voix, mais **trois moteurs**. La chaîne grave ne prenait que l'attelage articulé : un
autocar, un camion de pompiers, une citerne à lait et une benne sonnaient donc exactement
comme une berline. Un **camion rigide** la rejoint — c'est la même table `PORTEUR_TRAFIC`
qui lui donne déjà le ressort long — et la voix se lit alors à **0,72** au lieu de 0,58 :
entre la voiture et le semi, ce qui est exactement où il est. Mesuré au banc, l'allure du
véhicule mise de côté : 0,95 pour une berline, 0,718 pour un porteur, 0,58 pour un semi.

L'interrupteur et le volume étaient déjà dans les Réglages, et déjà sauvegardés : rien à
ajouter, et la version du fichier de partie ne bouge pas. Couper le son coupe **toutes** les
chaînes, moteur et trafic. Coût mesuré de la circulation et du son réunis : deux pour cent
des images.

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
                   |                              |-> bière        -> entrepôt
                   |                              \-> vin          -> entrepôt
                   |                                       |
                   |   entrepôt -+-> boulangerie / épicerie / marché / restaurant / caviste
                   |             |-> les mangeoires, pour l'aliment
                   |             \-> raisin, olives, lait, œufs, laine, miel en attente
                   |
                   +-> usines du bord de route : on verse, elles PAIENT
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
                caviste      +15 %,  35 kg   (vin, raisin)
                restaurant   +10 %,  50 kg
                coopérative    0 %, 400 kg   (les cinq céréales)
                marché        −6 %, 110 kg
                supermarché  −14 %, 500 kg
```

**Le mieux-disant ne peut pas tout prendre.** Chaque acheteur a un plafond par nature,
et ce plafond est l'inverse de son prix : le caviste paie le vin le mieux de tous mais
n'en écoule que trente-cinq kilos, le supermarché paie le moins et en prend cinq cents.
Tous se refont en deux minutes. D'où la seule vraie question d'une tournée — vendre le
haut de la benne au prix fort puis descendre l'échelle, ou tout donner d'un coup au
moins-disant et repartir travailler. Relevé sur 450 kg de vin — trois parcelles et demie
de raisin pressées : **5 839 €** en descendant l'échelle, **5 407 €** en vidant tout au
supermarché. Huit pour cent, pour quatre arrêts au lieu d'un. (Le même relevé avant la
remise à l'échelle des volumes, sur 2 000 kg : 5 834 contre 5 406. Le rapport n'a pas
bougé d'un point — c'était le but.)

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
- **On travaille en escargot, jamais en serpentin.** Le pilote tourne autour de la
  parcelle en se resserrant, en entrant par le coin le plus proche, et le premier
  segment est toujours parallèle à un bord.
- **Deux tiers de l'outil sur la terre, un tiers sur l'herbe.** Le premier tour posait
  l'axe du tracteur quinze centimètres DEHORS : l'outil, centré sur lui, était à moitié
  sur le chemin, et la moitié du premier passage était perdue — relevé, 47 à 49 % de la
  largeur travaillait de la terre. L'axe rentre maintenant d'un **sixième de largeur à
  l'intérieur**, la bordure sort d'un tiers, et 67 % travaille. C'est aussi plus sûr :
  sur les trois bords que longe la clôture de la ferme, l'axe passait à dix centimètres
  d'un mur de collision, il en a maintenant de quatre-vingts à quatre cents.
- **Et un tiers de recouvrement entre deux tours.** Le pas était réglé au banc à trois
  cinquièmes de largeur ; deux tiers font mieux — sur les seize cas du banc de
  couverture, le pire passe de **88,4 % à 94,2**.
- **Le milieu, c'est un tour sur place, et il est carré.** Le joueur l'a demandé ainsi :
  arrivé au centre, l'engin fait un tour sur lui-même et sort. Ce tour est tracé en
  quatre points à angle droit, pas en cercle — un chapelet de points rapprochés remettrait
  les diagonales que le plan n'a pas, et l'outil traîné ne les suivrait pas : le timon
  impose rayon² + attelage² − longueur², sans solution pour le semoir ni l'épandeur, qui
  se mettent en portefeuille. Les quatre points sont bornés au rectangle de la parcelle,
  faute de quoi une petite parcelle avec un outil large voit la pirouette sortir l'axe du
  tracteur de quarante centimètres.
- **Un champ ne se traverse que lorsqu'on y travaille.** Pour aller d'un lieu à un
  autre, l'automatisation rejoint la grille des chemins de sable et des rocades, la
  suit, et ne la quitte qu'au dernier moment — au lieu de viser sa destination en
  ligne droite à travers les semis.
- **Et l'on roule sur la voie de droite.** Les points étaient posés sur l'AXE de la
  chaussée : deux engins se croisant se rentraient dedans. Chaque tronçon est décalé
  d'un quart de chaussée à droite de son sens de marche — trente tronçons mesurés, zéro
  à contresens.
- **On repart en avançant quand il y a la place.** On ressortait toujours en marche
  arrière. C'est juste au fond d'un parvis de commerce, où la façade est à 5,40 m ; pas
  au silo, devant lequel s'ouvrent dix-neuf mètres de cour, et où l'on reculait pourtant
  de dix-huit mètres.
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

**Rien ne s'affiche tant qu'on roule.** Le bandeau s'allumait dès qu'on entrait dans le
rayon d'un lieu, donc en roulant : on traversait sa propre parcelle et la proposition
d'enclos clignotait tout du long, on longeait la coopérative et son bouton passait le
temps d'une seconde. Un bouton qu'on ne peut pas viser n'annonce rien, il occupe l'écran.
Il faut maintenant **s'arrêter dessus** — le seuil est à 0,35 m/s, de quoi laisser passer
le dernier mètre de roulement d'un engin qui décide lentement. L'ancien seuil, qui ne
valait que pour la parcelle, laissait passer 1,5 m/s, c'est-à-dire une bonne marche.
Repartir désarme au passage l'enclos qu'on venait d'armer.

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

**Mais seulement à qui peut y remédier.** La moissonneuse n'a pas d'attelage : arrivé au
silo pour y vider sa trémie, on lisait « CHARGER AU SILO — IL FAUT UNE BENNE OU UN
UTILITAIRE » sous la seule ligne qui servait. Un conseil qu'on ne peut pas suivre n'est pas
un empêchement, c'est du bruit. Le tracteur nu, lui, garde la ligne : il *peut* atteler une
benne.

**Et pendant une mission, une seule ligne.** Devant un commerce qui attend une livraison,
le joueur trouvait deux boutons jumeaux — « LIVRER LA COMMANDE — BLÉ 30 KG » et « VENDRE
BLÉ » — sans rien qui dise lequel fait avancer la mission. Les deux la faisaient avancer,
mais l'un vidait toute la benne. Tant que la mission attend *cette* marchandise *ici*, elle
est donc seule à s'afficher ; la vente libre revient d'elle-même dès la commande comblée.

La règle s'est élargie à tout le lieu, et pas seulement à la marchandise. Voir
[Là où la mission t'envoie, il n'y a que la mission](#là-où-la-mission-tenvoie-il-ny-a-que-la-mission) :
au **lieu de l'étape en cours**, aucune vente en vrac ne s'affiche — même quand il n'y a
encore rien à livrer, ce qui est précisément le cas du tutoriel, où l'on arrivait à la
Coopérative avec ses trente kilos et deux boutons pour les écouler.

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

### Le bandeau se range par sujet

Six éléments ont changé de place le même jour, et pour la même raison : chacun était posé
là où il y avait de la place, pas là où l'œil le cherche.

**Une seule rangée pour l'engin.** Le garage, l'attelage et le plan de travail parlent
tous de la machine qu'on pilote — lequel, ce qu'il traîne, qui le conduit. Ils tenaient
sur deux rangées, l'attelage seul au-dessus : on montait d'un étage pour atteler, et la
rangée du bas restait une paire dépareillée. Ils sont maintenant sur une ligne **souple** :
quand l'attelage n'a pas lieu d'être — moissonneuse, utilitaire — il disparaît et les
deux autres se recentrent d'eux-mêmes. C'est ce que trois boutons posés en `left: 50% ± 60px`
n'auraient pas su faire : masquer celui du milieu aurait laissé un trou de 72 px. La rangée
passe de 108 à **168 px**, toujours centrée. Au passage elle corrige un défaut ancien —
l'attelage montait à 112 px alors que le bouton d'achat commence à 104, et les deux se
recouvraient de huit pixels au garage.

**Le type de graine monte en haut.** En bas il occupait une rangée à lui tout seul pour un
réglage qu'on change une fois par parcelle. Il se pose sous le menu et la pause, contre le
bord droit — et **non à côté d'eux** : la barre de palier est centrée et large de 282 px,
un téléphone en paysage fait 568, et la mesure dit que les deux ne tiennent sur la même
ligne qu'au-delà de 696 px de large. Sur la deuxième rangée il n'a plus de voisin : le
bandeau des contrats est borné à 52 % de la largeur depuis la gauche. Il reste accroché
par son bord **droit**, car c'est le seul bouton qui grandit avec son texte — de 80 px pour
« BLÉ » à 105 pour « AVOINE » — et il pousse donc vers la gauche, où il n'y a personne.

**La régie descend contre la commande.** Les trois boutons — stockage, production, prix —
flottaient à 56 px au-dessus des flèches de direction : trois pastilles perdues au milieu
du décor, qu'on ne rattachait à rien. Elles se posent à **dix pixels** de la commande. Le
pédalier et le manche ne montent pas à la même hauteur, alors une classe sur `#hud` dit au
CSS lequel des deux est à l'écran — c'est la seule chose que la feuille de style ait besoin
de savoir du mode de conduite.

**Les deux jauges de droite portent leur signe.** C'étaient deux traits de huit pixels,
nus, l'un sur l'autre : rien ne disait lequel comptait le gazole et lequel la charge, il
fallait en vider un pour l'apprendre. Chacune reçoit son pictogramme — une **pompe**, un
**poids de balance** — et le gazole passe **en bas**, à huit pixels de la pédale
d'accélérateur : c'est la jauge qu'on surveille en roulant, elle se lit sans quitter le
pouce des yeux. Une barre claire à 22 % sur un champ de blé au soleil ne se voyait pas :
un liseré sombre d'un pixel la détache de n'importe quel fond, et le pictogramme porte la
même ombre. Ni l'un ni l'autre ne bouge, le filtre ne coûte donc qu'un calcul, une fois —
contrairement aux flèches du bord, qui se déplacent.

**Et le bandeau du haut perd une ligne.** Le poids du silo occupait celle du milieu : un
chiffre qu'on ne lit qu'au moment de rentrer une récolte, et qui figure déjà en toutes
lettres dans l'écran Stockage. Restent l'argent — ce qui décide de tout — et l'heure, qui
décide du reste. La pilule passe de 71 à **52 px** de haut.

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
elle ne tient plus que deux maisons. On la place entre l'épicerie et le caviste, les
deux plus petites — trente-huit mètres et demi de devanture d'un tenant, trente-neuf du
temps de la brasserie qui l'a précédée — plutôt qu'entre le marché et le supermarché, qui
en feraient cinquante-deux. Partout ailleurs c'est une
maison qui s'intercale.

Une **maison est au recul de la dalle voisine**, trois mètres, et pas un de plus — sans
quoi on ne peut pas la coller à son voisin, et la rue a deux lignes de façades au lieu
d'une. Son mur se retrouve en avant de celui du commerce, ce qui est juste : le commerce
met dix mètres de parvis derrière sa clôture, la maison son jardin de devant.

Un **objet de village se pose dans un creux** — ou, depuis peu, dans un des quatre coins du
monde, voir plus bas — et il se CHOISIT à la taille du creux : on prend le plus gros des
**sept** modèles candidats qui y tienne, un mètre de jeu compris, et l'on ne réserve que
son encombrement déclaré. Sept et non dix : le lavoir, le calvaire et le panneau d'entrée
sont partis aux coins. Il fallait sept mètres pour
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
maisons ; et de loin en loin un creux plus court où un abri de bus ou une tonnelle se pose
sur l'herbe, à 5,9 m du bitume. Les largeurs ne sont pas écrites — ce sont les
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
pour les engins et en ferait un mur invisible de dix mètres. Relevé : **1,76 m** de couloir
franchissable, 432 sommets de clôture sur chacun des deux jambages. Dedans : un **poteau
télégraphique**, un banc et un arbre. Le poteau y a remplacé le calvaire, parti aux quatre
coins : il monte à 7,55 m — plus haut qu'un mât de lampadaire —, il tient donc le même rôle
de silhouette qu'on voit du bitume par-dessus la clôture, il est bien plus étroit, et il
n'était dans aucune partie.

Le couloir valait 2,02 m avant que le mobilier ne grandisse de dix-huit pour cent : **c'est
ce que la taille coûte ici**, et il fallait résister à la tentation de le rendre en décalant
l'axe vers l'est. Mesuré : à quarante centimètres de plus à l'est, le banc élargi déborde de
l'écart de six centimètres et **entre de quatorze dans le maillage du pignon de clôture**.
La contrainte est là, et elle est exacte — le banc s'étend de 2,86 m à l'est de son axe une
fois grandi, le pignon commence à x = 33,046. L'axe est calé pour laisser quinze centimètres
de jeu. Et 1,76 m est un jeu de CENTRE, la demi-machine y étant déjà comptée : un engin
passe. Le pilote automatique, lui, ne s'y risque pas et ne s'y est jamais risqué — dans sa
métrique à lui, plus large, le couloir vaut 0,66 m contre 0,92 avant, et il était déjà
infranchissable des deux côtés du changement.

L'arbre de l'écart a rétréci au passage, de 0,9 à 0,7 : mesuré, son houppier arrivait à
**trois centimètres** du pignon — plus près que le banc, qui était pourtant l'objet dont on
se méfiait. Un contrôle de banc garde maintenant les deux, en comparant le bord est du
mobilier de l'écart au début du maillage de clôture.

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

### Le mobilier était à l'échelle 1, dans un monde qui ne l'est pas

Les commerces sont posés à `BAT_ECHELLE` = 1,18 et les maisons à 1,30 fois cela ; l'abri de
bus, le lavoir, le calvaire et les sept autres sortaient de leur fabrique **à l'échelle
1,00**, c'est-à-dire aux cotes réelles, au milieu d'un monde agrandi. Le joueur l'a vu :
*« augmente la taille des éléments de décor du village. »*

Le relevé, fait à la manière du fichier — cote du jeu ÷ cote réelle, ramené au 1,383 du
monde roulant — dirait 1,295 : assise de banc 1,353, plateau de table 1,383, sous-toit
d'abri 1,252, margelle de puits 1,250, panneau d'entrée 1,277, croix 1,410. **Et 1,30
casse la pose.** Le mobilier doit entrer dans les creux entre commerces, et le plus large
de tous, l'abri de bus, ne tient dans le plus grand creux — 8,22 m — que jusqu'à 1,2236 ;
au-delà, les quatre creux retombent sur les quatre plus petits modèles et le village perd
d'un coup son abri, son lavoir, sa tonnelle et son bûcher.

On prend donc **`BAT_ECHELLE`**, et on l'écrit comme telle plutôt qu'en clair : le mobilier
est dessiné aux cotes réelles exactement comme l'étaient les bâtiments, il mérite la même
correction, et une constante partagée interdit aux deux de se désaccorder. Il reste 26 cm
de marge sous le plafond mesuré.

Deux corrections suivent l'échelle, et toutes deux sont mesurées :

- **Le choix d'un creux porte sur l'emprise, plus sur le rayon.** Le test comparait `2r`.
  Or `r` n'est pas un rayon circonscrit : c'est un **disque de collision réglé à la main**,
  toujours plus petit que la boîte — 3,20 contre 3,46 pour l'abri de bus, 2,60 contre 3,91
  pour le panneau d'entrée. `2r` n'a donc aucun rapport fiable avec la place prise le long
  de la bande : il la surestimait d'un demi-mètre pour l'abri et la sous-estimait d'autant
  pour le bûcher. Résultat : l'abri ratait le grand creux du nord de **deux millimètres et
  neuf**, et c'est pour cela qu'on n'en voyait jamais. Chaque fabrique déclare maintenant
  sa largeur réelle en plus de son rayon ; la marge de l'abri y passe à **25,7 cm**, et la
  plus serrée des quatre est celle de la tonnelle, à 14,3. Cette largeur est déclarée et
  non mesurée à l'exécution : la tonnelle tire son feuillage au sort et sa boîte englobante
  varie de 4,80 à 5,15 m d'une construction à l'autre — le choix du creux se mettrait à
  dépendre d'un tirage de feuilles.
- **Le test admet sur la largeur, mais choisit sur le rayon**, et il faut le savoir : dans
  le creux nord, le bûcher entre aussi, et c'est l'abri qui l'emporte parce que son disque
  est plus gros. C'est voulu — on veut le plus imposant de ceux qui tiennent — mais c'est
  ce qui laisse le bûcher **sans emplacement dans toute la vallée**. Neuf modèles sur dix
  sont posés, pas dix.
- **Le mobilier recule de 5,0 à 5,9 m du bitume.** À cinq mètres, un abri de bus agrandi
  laisse son disque de collision mordre la chaussée de 68 cm au sens de `voieLibre` et de
  13 au sens de `Vehicle.update` : le pilote automatique s'écarterait d'une route libre. Le
  mordant devient une marge — 22 cm dans la première métrique, 77 dans la seconde — et,
  mesuré après coup, plus un seul objet de village ne touche le bitume dans l'une ou
  l'autre.

### Les quatre coins du monde

Les quatre rocades traversent la carte de bord à bord. Au-delà de leurs croisements, elles
découpent quatre morceaux d'herbe que **rien** n'occupait : pas un lot, pas une clôture, pas
un lampadaire — les vingt et un mâts sont tous à l'intérieur de l'anneau —, pas une
parcelle, pas une destination du pilote. Mesurés : 36,2 × 36,2 m au nord-ouest, 40,8 × 36,2
au nord-est, 36,2 × 40,5 au sud-ouest, 40,8 × 40,5 au sud-est, dont un rectangle vraiment
utilisable de 26 × 26 à 30 × 30 une fois qu'on s'écarte de six mètres du bitume et de quatre
du bord du monde. Le semis général y déposait deux à trois arbres et quelques buissons, et
c'était tout — alors que ce sont les quatre entrées du village.

Chacun reçoit son objet, et c'est lui qui lui donne son nom :

| coin | ce qu'on y trouve |
|---|---|
| nord-ouest | le **calvaire**, déplacé de l'écart du rang |
| nord-est | un **abri de bus**, qui n'était nulle part |
| sud-ouest | le **lavoir**, déplacé du grand creux du nord |
| sud-est | le **panneau d'entrée du village**, qui n'était nulle part |

Chacun est tourné vers la chaussée qui passe devant, et l'orientation est vérifiée sur la
géométrie et non devinée : l'abri de bus s'ouvre vers son +z local — dossier plein d'un
côté, banc tourné de l'autre —, le panneau se lit depuis son +z, le lavoir montre ses trois
battoirs en +z.

**Quatre arbres, quatre buissons et deux rochers** les habillent, et tous dans le seul
quadrant qui tourne le dos aux deux routes. Ce n'est pas une préférence de composition :
`addTree` refuse tout tronc à moins de 4,50 m d'une chaussée, pour que le houppier ne
surplombe jamais la route, et un secteur plus large ne plantait rien de plus — il faisait
disparaître deux à quatre arbres sur seize, en silence. Les arbres se posent entre 11 et
16 m de l'objet, et non entre 8 et 11 : relevé à l'écran, à huit mètres ils enterrent
l'objet et l'on ne voit plus ni le panneau ni l'abri depuis la route.

Un coin passe ainsi de **5-11 maillages à 13-18** dans un rayon de dix-huit mètres.

**Ils se posent en dernier, et sur leur propre flux de hasard.** `addTree` consomme
trente-six tirages du flux général pour ses feuilles tombées et peint une tache d'ombre sur
la tuile de sol : le glisser plus haut décalerait tout le décor et toute la peinture qui
suivent — mesuré sur un prototype posé avant `marquageParking()`, l'empreinte du sol peint
avait changé. Et leur verdure est semée sur un troisième flux à graine fixe, sur le modèle
de ceux qui sèment déjà la vallée : le décor reste identique d'une partie à l'autre, sans
qu'aucun `Math.random` n'entre en jeu.

**Le compte y retombe presque juste.** Quatre coins, quatre creux et deux places dans
l'écart du rang : dix emplacements pour **neuf** modèles distincts. Trois d'entre eux —
l'abri de bus, le panneau d'entrée et le poteau télégraphique — n'étaient dans **aucune**
partie. Le lavoir libérant le grand creux du nord, l'abri de bus y entre enfin : c'est
l'« autre arrêt de bus » que le joueur demandait, à la place même du lavoir. Le bûcher, lui,
reste sans emploi, et c'est écrit plutôt que tu.

Le coût, mesuré : **+24 maillages** de scène et +2 156 triangles de géométrie ; à la caméra
de départ, +4 appels de rendu et +272 triangles ; les emprises de collision ne bougent pas.

**Puis ils sont descendus au bord de la route.** Ils étaient posés au MILIEU de leur carré
d'herbe : le calvaire se tenait à **11,5 m** du bitume de la rocade ouest, c'est-à-dire
nulle part — on passait devant sans le voir, et un calvaire qui n'est pas au bord du chemin
n'est pas un calvaire. Chacun a donc deux places : l'ancre de la verdure reste au centre du
carré, là où les arbres ont de la place, et l'objet descend au plus près du croisement. La
cote se déduit et ne se choisit pas — bord de chaussée, plus le rayon du disque de
collision, plus une marge — et cette marge ne descend jamais sous **1,35 m**, la distance à
laquelle `Vehicle.update` commence à repousser une machine d'un obstacle : à 1,20 m, la zone
de répulsion du calvaire mordait de dix-sept centimètres sur le bitume, et un véhicule qui
longe l'accotement se serait senti écarté par une croix qu'il ne touche pas. Mesuré après :
**1,38 m** au calvaire, 1,82 à l'abri de bus, 1,79 au lavoir, 1,83 au panneau d'entrée ; le
calvaire est passé de 6,70 m à **3,30 m** du bitume, à onze mètres de son ancre. La
clairière réservée couvre maintenant l'union des deux places : sans cela le semis général
aurait repris la bande de terrain gagnée, et l'on aurait eu un caillou sous la croix.

## Le pilote automatique

> Cette section raconte l'escargot, et l'escargot n'existe plus : le plan de travail est
> devenu un va-et-vient de lignes droites — voir « Juste des lignes, et un demi-tour au
> bout », plus bas. Ce qui suit reste vrai de ce qui a été essayé, et des règles qui ont
> survécu au changement : le tracé strictement orthogonal, la sortie de parcelle, le
> retrait bord par bord, le pilote qui suit une ligne au lieu de courir après un point.

**L'escargot est strictement orthogonal.** Il ne l'était pas : le tour se refermait sur
son coin de départ, puis le suivant commençait au coin rentré d'une passe — un saut en
diagonale à chaque tour, **32 segments obliques** et jusqu'à 17 m de biais par parcelle.
On resserre UN bord à la fois, juste après l'avoir longé, et le resserrage est bridé au
milieu : sans cette butée le rectangle se retournait et il restait au centre une bande que
les deux passes opposées, trop écartées, n'avaient pas jointe. C'est la règle qui a
survécu à toutes les versions du plan, y compris la dernière — **0 oblique** sur les seize
cas du banc, hier comme aujourd'hui.

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

**Une passe finie se vérifie, mais ne se refait plus.** Le tracé épuisé, le pilote sait
compter ce qui n'a pas été travaillé — l'écran s'en sert pour dire où en est la parcelle —
mais il ne renvoie plus l'engin dessus : c'est ce que le joueur a demandé, et le plan de
rattrapage a été supprimé. Deux rattrapages avaient été essayés avant qu'il ne disparaisse :
des lignes droites sur l'emprise de ce qui restait, qui traversaient la parcelle sept fois
pour trois coins ; et un escargot resserré sur les trous, qui faisait moins bien encore,
parce qu'il virait précisément là où il fallait travailler.

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
descend plus pendant huit secondes, on l'abandonne et l'on passe au suivant. Ce qui n'a
pas été travaillé là reste à faire : c'est une passe imparfaite plutôt qu'une machine
bloquée jusqu'au matin.

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

### Le trajet refait : parallèle, à cheval, à demi-recouvrement, un rond, dehors

Le cahier des charges a été redonné mot pour mot, et il change quatre choses.

**On entrait en queue de billard.** Le plan commençait AU COIN de la parcelle. Le pilote
y menait la machine par la grille des chemins, donc en travers, et le premier point
qu'elle visait ensuite était le coin d'EN FACE, à trente mètres : elle franchissait la
limite de biais et se redressait tout le long du premier côté. Mesuré au moment exact où
l'axe passe le bord, sur neuf cas — trois parcelles, trois outils : **26°, 38°, 69°, 71°
de travers**, et jusqu'à **1,81 m** de décalage à la ligne du bord. On pose donc un point
d'ALIGNEMENT en amont du coin, sur la ligne du premier côté : les trois premiers points du
plan sont alors colinéaires, il n'y a plus de virage à l'entrée du champ, et le dernier se
fait dehors, sur le chemin. Avec le pied au plancher cela ne suffisait pas — le rayon de
braquage est proportionnel à la vitesse, et il restait dix degrés — alors le point
d'alignement ET le coin de départ portent `lent` : on entre au pas, comme un conducteur.
Après : **1,1° au pire des neuf cas, 0,12 m d'écart maximal, 0,02 m en moyenne**.

La longueur de l'alignement n'est pas choisie, elle est bornée par le couloir : 9,60 m
entre deux parcelles, et ce n'est pas la machine qu'il faut y faire tenir mais l'OUTIL,
traîné quatre à six mètres derrière. À neuf mètres du coin, la charrue est à treize —
trois mètres et demi dans le champ d'en face, et `work()` ne demande jamais à qui
appartient la cellule qu'il peint. L'échelle descend donc de neuf mètres à 2,20 ; avec
quatre échelons seulement, l'épandeur de douze mètres n'en trouvait aucun sur deux
parcelles et entrait de biais là où cela se voit le plus.

**Le premier tour se fait à cheval sur le bord.** « Une roue sur la terre et une roue dans
l'herbe, bien au milieu » : le retrait de base tombe à zéro, l'axe de la machine roule SUR
la limite, et l'outil travaille exactement la moitié de sa largeur. Deux planchers
subsistent, et aucun n'est un confort. La clôture de la ferme longe trois colonnes de
parcelles : son mur de collision est à vingt centimètres DEHORS et le dépassement de
virage mesure 2,20 m, donc sur ces bords-là seulement la machine s'écarte de
`VIRAGE_BORD − jeu`, soit **2,00 m**. Et le voisin : l'épandeur au dernier cran fait
vingt-quatre mètres, sa demi-largeur dépasserait le couloir, donc le débord est borné à
huit mètres — ce qui ne rentre aucun outil de seize mètres ou moins. Mesuré : **48 bords
libres à zéro exactement, 16 bords adossés à 2,00 m, zéro clôture couchée**.

**Chaque tour reprend la MOITIÉ du précédent**, et non plus le tiers. Le pas vaut une
demi-largeur d'outil : le premier passage est à cheval sur le bord, donc à moitié sur
l'herbe ; le deuxième est à cheval sur la trace du premier, donc à moitié sur la terre
brute ; et ainsi jusqu'au centre. Ce qu'on paie est un tour de plus par parcelle et le
tiers du temps de passe — la charrue met 73,7 s au lieu de 55,9 sur une parcelle de
30,4 × 19,6. Ce qu'on achète est une couverture qui ne dépend plus de la finesse du
virage : sur les neuf cas, le pire passe de **84,9 % à 98,0 %**, et sur les douze passes du
banc de clôture, de **84,3 % à 96,9 %**.

**Et la spirale s'arrêtait mal.** Son test de fin portait sur les DEUX dimensions à la
fois. Une parcelle n'est presque jamais carrée : le petit côté se referme le premier, et
la spirale continuait à glisser le long du grand — un aller de onze mètres, un retour de
huit, un aller de six, un retour de quatre, TOUS SUR LA MÊME LIGNE. Cinq points pour
quatre passages superposés au milieu du champ, et les deux derniers confondus, ce qui
donnait un cap d'arrivée nul et retournait le rond du centre sur lui-même. Elle s'arrête
maintenant dès qu'UN côté descend sous la moitié du pas : la bande qui reste est plus
mince que ce qu'un seul passage couvre, donc elle est déjà faite.

**Au centre, un rond, une fois.** C'était un rectangle de quatre points — quatre angles
droits pris au pas, ce qui se voit et ne ressemble à rien. C'est un octogone de 3,20 m de
rayon, tangent à la dernière passe et pris dans le sens où la spirale tournait déjà.
Puis on part un tout petit peu, on revient au centre, et sur cette lancée on sort du
champ : deux points, pas un de plus, et le sens de l'écart se déduit du sens de la sortie
— on le demande à `pointSortie` elle-même, faute de quoi la machine faisait son écart vers
l'ouest pour sortir à l'est, puis ressortait à l'ouest en retraversant tout le champ
qu'elle venait de faire. Le point de retour se valide sur la MACHINE et non sur l'outil :
l'outil étant traîné, il était déjà de l'autre côté du centre au moment où la machine
arrivait au bout de l'écart, le point se consommait en une image, et le demi-tour n'avait
pas lieu.

**Et une machine en automatique ne travaille que la parcelle de son plan.** `work()` ne
demandait jamais à qui appartient la cellule qu'il peint : il suffisait que son état
figure dans `from`. Un tracteur qui rejoint son chantier traîne son outil derrière lui, et
l'outil rasait le coin du champ d'à côté en passant — relevé au banc de clôture, quatre
cellules de la terre du voisin retournées à l'image soixante-huit, avant même que la passe
ait commencé. Cela ne coûte aucune couverture : ce qui déborde de la parcelle visée, c'est
du chemin, et un chemin est déjà ignoré. La conduite à la main n'est pas concernée — au
volant on travaille où l'on veut, et le banc le vérifie dans les deux sens : **0 cellule
en automatique, 51 au volant**, sur la même traversée.

### Puis le pilote a cessé de courir après un point

Le joueur a regardé le dessin du plan et il a dit ce qu'il fallait faire : « en allant d'un
point à un autre, ça fait un dessin en forme de queue de billard par rapport à la parcelle,
étant donné qu'on sort d'un virage donc prend un peu plus large et qu'on repart tout droit.
Et avec la vitesse du tracteur et le rayon de braquage, quand le véhicule n'arrive pas à
recoller parfaitement au tracé, il se met à tourner en rond. Il faut absolument qu'on
empêche ça. Est-ce qu'on peut pas juste dire : tu vas tout droit, tu tournes à quel endroit,
puis tu vas tout droit, tu tournes à quel endroit, plutôt que de lui faire suivre un tracé
qui n'arrivera pas à suivre parfaitement. »

C'est exactement ce que fait le pilote maintenant, et le tracé n'a pas changé d'un point :
c'est la façon de le suivre qui a changé.

**Le pilote visait le point au bout du tronçon, à trente mètres.** Viser un point n'est pas
suivre une ligne. Quand la machine sort d'un virage décalée d'un mètre et demi, l'angle vers
un point situé à trente mètres ne vaut que trois degrés : elle ne se redresse presque pas et
rejoint sa ligne EN DIAGONALE, pour n'être dessus qu'au dernier mètre. C'est la queue de
billard, et elle se mesure — écart maximal au milieu d'un côté, relevé sur douze cas (deux
tailles de parcelle, trois outils, deux crans de vitesse) : **1,64 m au pire, 1,37 m en
moyenne**.

**Trois règles l'ont remplacé, et rien d'autre.**

**1. Il vise un point posé sur sa ligne, pas le bout du tronçon.** Le cap voulu est celui de
la ligne, moins un rappel `atan(2·écart / vitesse)` borné à soixante-quinze degrés. Le
rappel est un ANGLE et il se divise par la vitesse : à 2,2 m/s un mètre d'écart demande
soixante degrés de correction, à 18,6 il en demande sept — parce qu'un engin lancé met sept
mètres à corriger ce qu'un engin au pas corrige en un. C'est ce qui rend la même règle bonne
pour le tracteur de départ et pour le même tracteur au dernier cran de vitesse, où le rayon
de braquage passe de 1,16 m à 9,8 m. Et les deux termes se SOUSTRAIENT quand la machine
traverse déjà vers sa ligne : c'est ce qui l'empêche de la dépasser.

**2. Il tourne à un endroit, et cet endroit se calcule.** Un virage d'angle `a` pris au rayon
`R` commence exactement `R·tan(a/2)` avant le coin — c'est la tangente, la seule façon
d'enchaîner deux droites sans couper ni déborder. Pour un angle droit et le tracteur de
départ, cela fait 1,26 m. On ne demande donc plus « l'outil a-t-il dépassé le point ? » —
question dont la réponse arrivait quatre à six mètres trop tard, l'outil étant traîné —
mais « suis-je arrivé au point où l'on tourne ? ».

**3. Il ne peut plus tourner en rond.** Le point visé avance TOUJOURS avec la machine : il ne
peut jamais lui passer derrière l'épaule ni tomber dans son cercle de braquage. Et par-dessus
cette garantie géométrique, un compteur : au-delà de quatre cents degrés de cap accumulés sur
un même tronçon, on abandonne ce tronçon et l'on repart droit sur le suivant. Quatre cents
degrés laissent passer le demi-tour de l'écart (180) et les huit sommets du rond (45 chacun)
sans jamais les interrompre.

**Et le dernier mètre du défaut ne venait pas du tracé, mais d'un seuil de gaz.** `viser` rend
la vitesse de pivot tant que le cap est faux de plus de soixante-huit degrés, et une fois et
demie cette vitesse en deçà. Or un virage à l'équerre commence justement sous ce seuil — le
rappel latéral en mange déjà cinquante. La machine reprenait donc **3,7 m/s au lieu de 2,2 en
plein virage**, et le rayon étant proportionnel à la vitesse, elle tournait sur deux mètres là
où le point de tangence en supposait 1,16 : elle traversait sa ligne et ressortait de l'autre
côté. Relevé image par image sur la charrue, l'écart passait de −1,28 m à **+1,29 m en deux
mètres de trajet**, puis mettait vingt mètres à se refermer. Tant que le cap n'est pas repris
à dix-sept degrés près, la machine reste donc à la vitesse qui tourne le plus court. C'est ce
que fait un conducteur : il ne rend les gaz qu'une fois le volant rendu.

**La spirale, enfin, ne trace plus de côté plus court que son propre diamètre de braquage.**
Un tronçon de 1,20 m entre deux virages à l'équerre est un tracé « qui n'arrivera pas à être
suivi parfaitement » : la machine tourne sur 1,16 m de rayon au mieux, il lui en faudrait 2,32
pour enchaîner les deux. Elle s'arrête donc au plus tard quand le rectangle restant descend
sous deux rayons. Ce qu'on laisse, l'outil le couvre — 2,32 m de large contre 4,80 pour la
plus étroite des charrues — et le rond du centre repasse dessus.

**Ce que ça donne**, sur les douze cas, avant puis après :

| | tracteur de départ | tracteur au dernier cran (×1,55) |
|---|---|---|
| écart au pire | 1,54 m → **0,26 m** | 1,64 m → **0,40 m** |
| écart moyen | 1,28 m → **0,23 m** | 1,37 m → **0,33 m** |
| tronçons parcourus en rond | 0 → **0** | 0 → **0** |
| couverture moyenne | 98,7 % → 98,6 % | 98,9 % → 98,5 % |
| temps par parcelle | 58,1 s → 68,9 s | 57,0 s → 67,8 s |

Et sur la parcelle du dessin — charrue en 30,4 × 19,6 — l'axe du tracteur ne sort plus que
de **0,43 m** de sa terre contre 1,36, et il reste **une cellule sur 345** au lieu de deux.

L'écart est divisé par quatre à six ; la couverture ne bouge pas ; le temps monte de dix-neuf
pour cent, et c'est le prix assumé de la règle 3 — la machine passe une demi-seconde de plus
au pas dans chaque virage, vingt-cinq fois par parcelle.

**Et le banc mentait sur le pire du défaut.** Le dessin envoyé au joueur montrait une longue
diagonale en travers du champ. Elle n'existe pas dans le jeu : la sonde appelait
`activateParcel` directement, ce qui prépare la terre mais ne retire pas le cylindre de
collision du panneau « À VENDRE » — 1,60 m de rayon, planté 2,40 m à l'intérieur du coin de
chaque parcelle. Les trois chemins d'achat du jeu le retirent tous (`ongletParcelles`,
`refreshBuyButton`, `degagerFriche`) ; la sonde, non. La machine s'y cognait douze secondes,
le garde-fou des huit secondes abandonnait le point, et elle repartait en diagonale vers le
suivant. Toutes les sondes de trajet retirent maintenant `p.signObs` en même temps que le
décor, et les chiffres ci-dessus sont mesurés sans lui.

**Et il n'y a plus qu'un pilote de champ, pour les deux conduites — c'est là que se cachait
le vrai défaut.** Il y en avait deux, et un seul avait été refait. `autoDrive` mène la machine quand le joueur lance le travail
lui-même ; `missionDrive` la mène pendant TOUTE la campagne et tout le tutoriel — et
celui-là visait encore le point au bout du tronçon, avec un rayon de capture de deux mètres.
Le défaut réparé serait donc resté entier là où le joueur passe le plus clair de son temps.
Les deux rangent le plan sous les mêmes noms (`v.plan`, `v.plan.i`, `v.plan.entre`) : le
bloc « au champ » est sorti d'`autoDrive` tel quel dans `piloteChamp`, et les deux
l'appellent. Une règle écrite deux fois est une règle qui diverge.

**Et c'est le pilote de campagne qui allait le plus mal**, parce que son rayon de capture
valait deux mètres au lieu d'un et qu'il ne freinait pas du tout avant les coins. Mesuré sur
quatre passes conduites par une mission, tracteur au dernier cran de vitesse :

| | avant | après |
|---|---|---|
| écart au pire | **6,18 m** | **0,40 m** |
| tronçons parcourus en rond | **11** | **0** |
| passes qui vont au bout | 3 / 4 | **4 / 4** |
| temps par parcelle | 167 s | **77 s** |
| couverture moyenne | 99,6 % | 98,9 % |

Six mètres d'écart sur un côté de trente, et onze tronçons où la machine tourne sur
elle-même : c'est exactement ce que le joueur décrivait, et cela n'arrivait que sur ce
pilote-là. La passe est aussi deux fois plus courte, parce qu'une machine qui suit sa ligne
ne perd plus son temps à la rattraper.

**Trois garde-fous sont venus d'une relecture adverse**, et chacun répond à un scénario
précis. Le premier : le seuil de virage est géométrique, donc il peut être vrai DÈS LA
PREMIÈRE IMAGE d'un tronçon — après un abandon, ou sur un virage de plus de quatre-vingt-dix
degrés, la projection de départ tombe déjà au-delà. Le plan se serait vidé de plusieurs
points en autant d'images. On exige donc trente centimètres de trajet réel, sauf sur un
tronçon plus court que cela — qui est toujours le premier, la route ayant déjà déposé la
machine sur son point de départ — **et sauf si la machine était déjà au-delà du seuil en
arrivant**. Cette dernière exception n'était pas dans la relecture, et c'est le banc de
clôture qui l'a réclamée : la projection étant bornée au bout du tronçon, « trente
centimètres de plus » y devient impossible, plus rien ne libère la machine avant les huit
secondes du garde-fou de distance, et elle part droit devant pendant ce temps. Relevé :
l'axe du tracteur sortait de **23,97 m** de sa terre et couchait trois courses de clôture,
sur un cas qui ne faisait rien de tel avant. Ce qu'on risque en laissant passer est borné —
une image par point, un demi-tour de plan au pire — et la machine reprend sa ligne au
tronçon suivant. Le deuxième : le compteur de quatre cents degrés ne
s'accumule que TANT QU'ON N'AVANCE PAS ; un demi-tour qui progresse le long de sa ligne
n'est pas un rond, et le compteur se remet à zéro dès que la projection gagne quinze
centimètres — sans quoi il coupait au bout de 3,7 secondes, contre 8 pour le garde-fou de
la distance. Le troisième : le point de sortie se capture à un mètre vingt, parce qu'on y
recule — `marcheArriere` rend la main à un mètre du but, et sans capture de proximité la
machine repassait en marche avant pour un point situé dans son dos.

**Et le plancher de braquage de la spirale ne laisse jamais plus large qu'un passage.** Deux
rayons font 3,26 m pour l'enjambeuse, dont le tunnel de vendange n'en couvre que 2,80 : le
plancher aurait laissé au centre une bande plus large que l'outil, c'est-à-dire de la vigne
jamais vendangée. Il est donc borné par la largeur d'un passage, et c'est le seul outil du
jeu que cette borne concerne.

**La même relecture annonçait une perte de couverture dans les coins**, l'outil traîné
n'étant plus compensé nulle part. Le raisonnement se tient — la charrue est 4,05 m derrière
l'axe, et l'on tourne maintenant 1,26 m AVANT le coin au lieu de déborder de 4 m après.
La mesure le dément : sur les quatre parcelles les plus serrées contre la clôture de la
ferme (vingt centimètres de jeu), trois outils chacune, tracteur au dernier cran de vitesse,
la couverture moyenne passe de **98,49 % à 98,70 %** et l'écart de 1,60 m à 0,40. Ce que le
virage à la tangente ne travaille plus, le tour de périphérie et le demi-recouvrement
l'avaient déjà fait.

### Et en automatique, la machine roule à sa vitesse d'origine

Le joueur l'a demandé, et cela répare un défaut de conception : « brider la vitesse même
quand on est avec une amélioration de trois ou quatre pour le tracteur et même les autres,
tu laisses la vitesse standard en automatique pour le traitement de la parcelle, comme ça
y a pas de mauvaise surprise. »

**Pourquoi acheter de la vitesse dégradait le travail.** Le rayon de braquage est
proportionnel à la vitesse — `R = v / (braquage × turn)` — et la direction, elle, ne
s'achète pas : `turn` vaut la même chose au premier cran qu'au dernier, et c'est écrit dans
le jeu depuis longtemps. Le palier de vitesse n'achetait donc, au champ, qu'un rayon de
virage plus grand sans rien qui le compense : 9,8 m au dernier cran contre 6,3 au premier,
sur des bords où la clôture de la ferme ne laisse que vingt-cinq centimètres de jeu.

**La règle a deux moitiés, et c'est une leçon payée.** La vitesse se borne au GAZ, dans
`piloteChamp` : la consigne y est une fraction de `vmax`, on la plafonne à `vmax0/vmax`. La
reprise, elle, ne s'y borne pas — dans ce moteur `vf` avance de `accel·dt` par image quelle
que soit la consigne — et se borne donc dans `Vehicle.update`. Les mettre toutes les deux
dans le moteur a été essayé et mesuré : plafonner `vmax` là où la consigne est une fraction
de `vmax`, c'est diviser la consigne d'autant. La machine roulait à **64 % de la vitesse
voulue** et la passe passait de 108 à 160 secondes. Une borne par endroit, celui qui la
comprend.

**Et la règle ne tient à aucun drapeau.** Elle se lit dans l'état du véhicule : il conduit
tout seul, il a un plan, il est entré dans sa terre et n'en est pas sorti. Les deux pilotes
rangent le plan sous les mêmes noms, donc elle vaut pour les deux sans qu'aucun ait à la
connaître. Elle s'arrête au bord du champ : sur la route, au volant et pour les navettes,
le cran acheté sert exactement comme avant. Et c'est la vitesse de CHAQUE machine, pas un
chiffre — 12 m/s pour le tracteur de départ, 9,5 pour la moissonneuse, 8,5 pour
l'enjambeuse.

**Ce que ça donne**, douze cas, tracteur au dernier cran (×1,55) :

| | avant | après |
|---|---|---|
| écart à la ligne, au pire | 0,40 m | **0,26 m** — celui du tracteur de départ |
| temps par parcelle | 68 s | **68 s** — inchangé |
| couverture moyenne | 98,5 % | 98,6 % |

Le cran de vitesse ne change donc plus rien au champ, ni en bien ni en mal, et il ne coûte
rien en temps : la rampe de freinage tenait déjà la machine autour de 12 m/s sur des
parcelles de trente mètres, et ce qui restait de l'écart venait entièrement de la REPRISE.

**Et il reste quatre clôtures couchées, toutes sur la route.** Mesuré en attribuant chaque
choc à sa phase, sur les quatre parcelles collées au mur, trois outils chacune, tracteur au
dernier cran : **route 4, travail 0, sortie 0**. Le champ est propre ; ce qui accroche
encore, c'est l'approche, où le cran de vitesse continue de s'appliquer — c'est le choix
assumé de laisser l'amélioration servir là où elle a été achetée.

## Le silo et l'entrepôt ont leur voie, et c'est le joueur qui l'a tracée

Il a dessiné en rouge, sur la carte du plan de travail, les chemins par lesquels il veut
qu'on accède au silo et à l'entrepôt. La photo se relève au pixel près : quatre pastilles
de position connue — Supermarché, Usine avoine, Entrepôt, Silo — donnent **6,426 pixels par
mètre**, et les quatre se retrouvent à moins d'un pixel de leur place calculée. Le tracé
converti donne, sur la trame du jeu :

| | ligne | de … à |
|---|---|---|
| **Silo** | verticale **x = 59**, qui le traverse | z = 40 (chemin) → z = 74 (rocade sud) |
| **Entrepôt** | rocade sud **z = 74**, puis montée **x = 11** | jusqu'au quai, z = 66,85 |

**Et le dessin dit vrai sur un point qu'il ne pouvait pas connaître.** L'entrepôt n'y est
accessible que par le sud. Mesuré : la voie x = 11 est libre de z = 74 à z = 68, et bouchée
de z = 40 à z = 66 — le hangar est une emprise de 16,5 × 17,7 m centrée sur (11, 54), posée
en travers de cette même verticale côté nord. La voie du silo, elle, est libre sur toute sa
hauteur : la tour est à x = 52, sept mètres à l'ouest.

**Ce que ça répare.** La grille d'itinéraires n'a que six voies nord-sud (−74, −40, 0, 40,
80, 114) et six est-ouest. Le silo, à x = 59, n'est sur aucune : on le desservait par la
plus proche, 40, et donc **toujours par le nord**. Partant de la rocade sud — à vingt-cinq
mètres du silo — la machine remontait au chemin z = 42,5, traversait tout le champ vers
l'est, puis redescendait sur la goulotte. Et de l'entrepôt au silo, deux voisins, elle
repartait vers l'ouest, montait au nord, revenait à l'est et redescendait.

**La voie sert dans les deux sens.** On y entre par un bout, on en sort par un bout, et
entre les deux c'est la grille comme avant. Le bout se choisit sur la **longueur du trajet
entier**, pas sur la simple proximité : venant de la rocade sud à l'est, le bout nord est à
trente-quatre mètres et le bout sud à deux, mais c'est 125 m par le nord contre 72 par le
sud. On construit donc les deux — quatre au plus si l'on part aussi d'une voie — et l'on
garde le plus court. Deux lieux du même couloir s'y rejoignent sans passer par la grille.

**Et l'on ne change plus de rangée quand on y est déjà.** Une chaussée fait dix mètres :
partant du silo à z = 74 pour aller à l'entrepôt à z = 74, la machine allait quand même
chercher une voie de traverse — elle roulait jusqu'à x = 40 pour n'y rien faire, puis
revenait. Si le départ est déjà sur la rangée qui dessert le but, on longe, un point c'est
tout.

**Mesuré**, sur six trajets caractéristiques :

| trajet | avant | après |
|---|---|---|
| rocade sud est → silo | 125,5 m | **72,5 m** |
| rocade sud ouest → silo | 140,5 m | **125,5 m** |
| entrepôt → silo | 96,8 m, 1 tronçon bloqué | **84,2 m, 0** |
| silo → entrepôt | 74,2 m, 1 tronçon bloqué | 84,2 m, **0** |
| garage → silo | 96,0 m | 96,0 m |
| usine avoine → entrepôt | 166,1 m | 171,1 m |

Les deux tronçons « bloqués » d'avant sont le même : de la goulotte, la machine partait
plein ouest à z = 50 et passait **dans la tour du silo**, à x = 52. Le trajet est dix mètres
plus long qu'avant dans ce sens ; il ne traverse plus le silo.

Sur deux cent cinquante-quatre itinéraires tirés d'un quadrillage de départs, la longueur
totale bouge de **0,4 %** et le nombre de tronçons qui frôlent un obstacle descend de 131 à
126 : la voie d'accès ne coûte rien à l'ensemble.

**Ce qui n'a pas été fait, et pourquoi.** Le joueur a aussi tracé la verticale x = 0 pour
descendre du chemin nord vers la rocade sud. Faire préférer au routeur la voie de traverse
comprise ENTRE le départ et le but — c'est-à-dire x = 0 plutôt que la voie sous les roues —
a été écrit, puis retiré : le premier tronçon d'un itinéraire se parcourt à la hauteur
courante, ce qui n'est roulable que si l'on est déjà sur une chaussée. En partant du garage,
la machine traversait alors soixante-huit mètres de champs à z = 52 pour aller chercher sa
voie. Les deux choix se valent de toute façon en distance — toutes les voies comprises entre
les deux donnent la même longueur —, et l'écart de dessin ne vaut que deux fois le décalage
de conduite à droite, cinq mètres.

## Cinq demandes d'un coup

### Le pas de la spirale s'élargit

« Fais un espacement un petit peu plus large entre chaque passe, là tu remords trop sur tes
traces et du coup le temps de la passe complète est trop long. » Il a valu deux tiers, puis
la moitié ; il vaut 0,70 — un tiers de recouvrement. Douze cas, deux tailles de parcelle,
trois outils, deux crans de vitesse :

| pas | couverture moyenne | pire cas | temps par parcelle |
|---|---|---|---|
| 0,50 | 98,5 % | 95,6 % | 69 s |
| **0,70** | **97,6 %** | **95,6 %** | **57 s** |
| 0,80 | 95,1 % | 86,7 % | 52 s |

Dix-sept pour cent de temps rendus pour neuf dixièmes de point, et le pire cas ne bouge pas
d'un dixième. 0,80 s'effondre : l'épandeur de douze mètres sur une petite parcelle tombe à
86,7 %, un outil traîné qui coupe les virages ne rattrapant plus un recouvrement d'un
cinquième. La constante s'appelle `PAS_PASSE`, et le banc la LIT au lieu de la recopier —
un chiffre écrit deux fois est un banc qui échoue au premier réglage sans rien dire d'utile.

### La moissonneuse finit toujours par vider, et revient où elle s'est arrêtée

Elle partait déjà au silo trémie pleine. Il manquait l'autre bout : **la fin du champ**. Le
plan terminé, elle rendait la main là où elle était, quatre-vingt-dix kilos dans le ventre,
et il fallait aller la chercher à la main. Elle va verser, puis s'arrête — dans les deux
pilotes, celui du joueur et celui de la campagne.

**Et le retour est maintenant exact.** La passe reprenait au point courant du plan,
c'est-à-dire à la FIN du tronçon interrompu : tout ce qui restait de cette ligne — jusqu'à
trente mètres — était sauté. `quitterLieu` note l'endroit précis où la trémie s'est remplie,
et c'est là qu'on redescend.

### Ce qui reste debout après une moisson finit par tomber

« S'il reste 5 % du terrain qui n'a pas été moissonné correctement, au bout d'une dizaine de
secondes je veux que le reste de la culture disparaisse. » C'est le pendant de « n'essaie pas
de remplir le champ » : l'escargot laisse ce que tout escargot laisse, on a retiré le
rattrapage qui coûtait sept traversées pour trois coins, mais ces pieds restaient DEBOUT — la
parcelle ressortait dans la liste de ce qu'il y a à faire et la passe suivante repartait pour
rien. Cinq pour cent, dix secondes ; au-delà ce n'est plus un reliquat mais du travail qui ne
s'est pas fait, et l'effacer masquerait le vrai problème. **La vigne est épargnée** : un pied
pérenne qu'on n'a pas vendangé reste un pied.

### Un andain qui mord sur une autre culture n'est plus refusé en entier

« Si on commence à mettre des grains sur un terrain par erreur mais qu'on n'a pas continué,
et qu'on demande une automatisation sur ce terrain, il faut pas qu'on soit bloqué par le peu
de grains qui ne serait pas de la même semence. » Une poignée de cellules d'une autre semence
suffisait à faire refuser TOUT andain qui les touchait : la machine repassait dessus sans rien
couper, le garde-fou des huit secondes abandonnait le point, et la passe s'arrêtait là. On
garde maintenant les cellules de la bonne nature et les autres restent debout, ni coupées ni
peintes — exactement ce que le code faisait déjà pour la vigne qu'une moissonneuse traverse.
La trémie, elle, ne mélange toujours pas : c'est une règle de contenant, et elle est juste.

### Une caisse porte plusieurs natures

« Je veux qu'on puisse transporter plusieurs produits différents tant que la capacité de
charge n'est pas atteinte. » `T.charge` est un dictionnaire {nature: kilos} et `T.load` en
reste la SOMME : les cent lectures qui affichent une jauge, bornent un chargement ou lisent un
poids continuent de marcher sans rien savoir du reste. La seule limite est la capacité.

Ce qui a demandé du soin n'est pas le dictionnaire, ce sont les endroits qui supposaient une
nature unique. **Les bornes de transfert** prenaient `T.load` pour « ce que je porte de CETTE
nature » : non corrigées, elles auraient vendu à la Coopérative du blé prélevé sur la réserve
de lait, le compte global tombant juste et la nature partant au hasard. **Le juge d'objectif**
écartait toute caisse dont la nature ne collait pas : la campagne se serait arrêtée d'avancer
sans un mot. **La remise à l'échelle** des vieilles parties divise `load` par trois et aurait
laissé les lots trois fois trop lourds. Et **la relecture** rogne `load` quand la capacité a
baissé : les lots sont maintenant rognés au prorata et `load` se redéduit d'eux.

La sauvegarde ne change pas de version : `charge` est un champ facultatif de plus, écrit à
côté de `load` et `type`, et `type` continue d'être écrit. Une partie d'avant n'a que `type`
et `load` : le dictionnaire se fabrique à la première écriture, et une benne de trois cents
kilos de blé se retrouve avec `{ble: 300}`. Rien à convertir, rien à migrer.

### La navette se compose en trois questions, dans l'ordre

« Je prends le fourgon, je choisis l'entrepôt, il y a dans l'entrepôt de la farine et des
œufs ; si je choisis œufs je peux livrer à la boulangerie, supermarché, marché — à condition
que ces lieux aient une demande en cours pour ces produits. »

C'était deux touches — le départ, l'arrivée — et la marchandise se demandait après coup. C'est
maintenant trois : **le départ**, puis **ce qu'on emporte** parmi ce qu'il y a vraiment là
(avec la quantité écrite à côté du nom), puis **où le livrer** — et seuls les preneurs sont
allumés, les autres restent dessinés à un quart d'opacité. Toucher un lieu qui n'en veut pas
ne fait rien, ce qui vaut mieux qu'un trajet qui ne livrera rien.

**Une demande en cours, et pas seulement une porte ouverte.** Un commerce fermé par le palier,
un étal déjà plein, une usine dont la trémie déborde : la marchandise y arriverait pour rester
sur le quai. On pose donc exactement les questions que se pose le transfert lui-même —
`acheteMaintenant` pour la revente, `accepteMaintenant` pour l'entrée d'une recette — et pour
les trois lieux de la ferme, la place qui reste. Relevé sur l'exemple du joueur : entrepôt →
farine 120 kg et œufs 667 ; œufs → **Marché, Supermarché, Boulangerie, Restaurant** ; le
garage reste éteint.

Et si le lieu de départ est vide, la rangée montre quand même tout ce qu'il sait donner : on
prépare une navette en boucle avant que le silo ne se remplisse, et une liste vide n'aurait
rien laissé choisir.

## Trois couleurs, trois rôles, et la mission qu'on ne signe plus au bout du travail

Le joueur, arrivant à la Coopérative avec les trente kilos du tutoriel : « on a un bouton vert
marqué commencer la mission, et un autre bouton vert en dessous pour vendre du blé en vrac. Je
veux pas qu'au moment de choisir la mission on ait une autre alternative — à part plus tard à
la coopérative quand on aura débloqué la vente libre — et le bouton pour vendre, je veux qu'il
soit bleu, pas vert, ça crée une incompréhension par rapport à la mission. »

**La couleur disait le LIEU.** La colonne prenait la teinte du cercle sous les roues et tous
ses boutons avec : à la Coopérative du tutoriel le cercle est vert, donc « VENDRE 30 KG DE
BLÉ » était vert, et « VENDRE BLÉ · 0,50 € / KG » juste dessous aussi — deux boutons de la même
couleur pour deux gestes opposés, dont l'un bradait à moitié prix la marchandise que l'autre
attendait. Elle dit maintenant le **rôle** :

| | |
|---|---|
| **vert** | prendre une nouvelle mission — il n'y en a jamais qu'un |
| **jaune** | une action de la mission EN COURS |
| **bleu** | le jeu continu : acheter, améliorer, vendre librement, charger, ranger |

Le gris de l'empêché et le plein de ce qui est en cours restent des ÉTATS, et ne changent pas.
Les boutons flottants suivent la même règle : au garage, ACHETER et AMÉLIORER sont bleus, et
seul celui que l'objectif désigne vraiment passe au jaune — le vert n'y vient jamais, puisque
acheter un engin n'est pas prendre une mission.

**La vente libre n'existe plus avant d'avoir été débloquée.** Le jeu l'annonce en toutes
lettres à la fin de la première mission — « VENTE LIBRE DÉBLOQUÉE · la Coopérative achète votre
production à tout moment » — et la proposait pourtant AVANT, à côté du bouton de cette même
mission. C'est donc la fin de la mission zéro qui l'ouvre.

**Et l'on ne signe plus une mission qu'on vient de faire.** « Comme on est déjà dans une phase
de jeu et qu'on va livrer les 30 kg, il faut pas qu'on voie le bouton prendre la mission, il
faut qu'on passe direct au bouton jaune. » Le tutoriel a envoyé labourer, semer, moissonner et
charger trente kilos POUR cette mission : arriver au bout et se voir demander si l'on veut bien
la prendre, c'est demander une signature après le travail. Quand la marchandise attendue est
DÉJÀ À BORD, la mission se prend donc toute seule et le bouton jaune de livraison apparaît
directement. Si l'on arrive les mains vides, rien ne change : le bouton vert est là, avec son
texte. Relevé au banc, à la Coopérative du tutoriel — un seul bouton, et c'est
`ch jaune | LIVRER LA COMMANDE — BLÉ 30 KG`.

**Là où la mission envoie, il n'y a que la mission** — sauf chez les trois fournisseurs. Le
garage, le comptoir agricole et la Coopérative gardent leur jeu continu en bleu, sous les
jaunes : on n'y va pas seulement quand la campagne le demande, on y va parce qu'on a besoin de
quelque chose. Partout ailleurs, sur le lieu de l'étape en cours, les actions qui ne servent
pas la mission sont retirées.

## Juste des lignes, et un demi-tour au bout

Le pilote savait enfin accélérer, freiner et tourner court. Le joueur en tire la
conséquence : « maintenant qu'on fait des demi-tours serrés, on va essayer de faire juste
des lignes. On commence à ras de la terre avec juste un tiers de l'outil qui est sur
l'herbe, on avance à fond, puis on ralentit sur les derniers mètres, brusquement on fait un
demi-tour à 180°, puis on fait une ligne dans l'autre sens avec un tiers de l'outil qui mord
sur la ligne tracée précédemment. On fait des lignes l'une après l'autre. »

C'est le dessin le plus ancien de l'agriculture, et c'est aussi le plus rapide. Une spirale
passe un quart de son temps en virages ; un aller-retour n'en passe qu'aux deux bouts.
Mesuré sur la parcelle que le joueur avait fait dessiner — charrue sur 30,4 × 19,6 m :

|                        | escargot | lignes |
|------------------------|---------:|-------:|
| durée d'une passe      |   75,7 s | **44,0 s** |
| cellules travaillées   |   99,7 % | **100 %** |
| clôtures couchées      |        0 |    **0** |

**Les trois chiffres du dessin viennent tous de la même phrase.** « Un tiers de l'outil sur
l'herbe » : la ligne extrême rentre d'un *sixième* de largeur à l'intérieur du bord —
l'outil étant centré sur l'axe, il déborde alors d'un tiers. « Un tiers qui mord sur la
ligne précédente » : le pas vaut *deux tiers* de largeur, et c'est `PAS_PASSE`, lu par le
banc au lieu d'être recopié. « Un demi-tour à 180° » : il se prend au-delà du bout de la
ligne, sur un rayon d'un demi-pas — celui qui amène exactement sur la ligne suivante.

**Le nombre de lignes s'arrondit par le haut.** Une bande ne se divise pas en un nombre
entier de pas. Arrondi au plus proche, le pas réel dépassait parfois les deux tiers demandés
— 8,80 m au lieu de 8,00 pour l'épandeur, un quart de recouvrement au lieu d'un tiers, et
9,3 % de la parcelle carrée laissée derrière. Arrondi par le haut, il ne fait plus que se
resserrer : une ligne de plus coûte **5 % de temps** sur les douze chantiers du banc et rend
la couverture — 90,7 % au pire devient 98,2, la moisson 94,7 devient 97,8.

**Les lignes suivent l'axe dont les deux bouts sont les plus dégagés**, et le grand côté ne
tranche qu'à égalité. Le grand côté seul serait plus rapide — moins de lignes, donc moins de
demi-tours — mais le demi-tour se prend *hors* du champ, et les trois colonnes de parcelles
adossées à la clôture de la ferme n'ont que vingt centimètres derrière le bord. Relevé au
banc : la charrue sur la parcelle carrée tirait ses lignes en x, faisait demi-tour à l'ouest,
et couchait la clôture au huitième point. Regarder d'abord ce que les deux bouts laissent
suffit à faire tourner les lignes d'un quart de tour et à rendre les demi-tours au couloir.

**Quand le mur est trop près, c'est le demi-tour qui se serre, pas la ligne qui recule.** On
avait d'abord rentré le bout de la ligne d'un rayon pour que le tour tienne dans le champ.
Mesuré ensuite : cette bande-là n'est jamais travaillée, et elle coûte **un cinquième d'une
parcelle de bordure** — l'épandeur tombait à 79,6 % sur la parcelle carrée. La ligne va donc
jusqu'au bout ; le sommet du demi-tour reste borné à `VIRAGE_BORD` du premier mur, et le
pilote y roule de toute façon à la vitesse de pivot. Après : **99,1 %** au pire, la même
clôture debout, et 1,70 m de jeu au mur au lieu de 0,96.

**On entre droit, pas en queue de billard.** Le plan commence par un point d'*amont* posé
hors du champ, exactement dans l'axe de la première ligne : les deux premiers segments sont
colinéaires, le dernier virage se fait dehors sur le chemin, et la machine franchit le bord
déjà droite. La longueur est bornée par le couloir — 9,60 m entre deux parcelles — et c'est
l'*outil* qu'on mesure, traîné quatre à six mètres derrière. Un dernier garde-fou : le point
d'amont doit lui aussi rester à `VIRAGE_BORD` du premier mur. `voieLibre` échantillonne son
segment tous les 1,20 m et cherche un piquet dans un rayon de 2,25 ; la clôture a ses piquets
tous les 1,56 m, et l'amont d'une ligne peut tomber pile entre deux — le segment passe alors
pour libre alors qu'il longe la clôture à vingt centimètres. La géométrie tranche là où
l'échantillonnage se trompe.

**Et le demi-tour ne sort pas de la terre.** « On va trop loin, on dépasse trop ; je veux que
pour chacun des véhicules tu ailles jusqu'au bout de la terre mais que tu dépasses pas sur
l'herbe — c'est quand on fera le demi-tour que ça nettoiera correctement. »

La ligne, elle, s'arrêtait déjà au bord : `retraitsDe` ne rend jamais de retrait négatif. Ce
qui sortait, c'était le **sommet du demi-tour**, posé un demi-pas au-delà du bout de ligne —
quatre mètres pour un épandeur, et l'axe du tracteur relevé jusqu'à **4,35 m dans l'herbe**.
Le sommet est maintenant borné par le bord de la parcelle : on arrive au bout, on tourne, on
traverse d'un pas le long du bord, on repart. Ce qui reste au bout des lignes, c'est ce
demi-tour lui-même qui le balaie.

Le prix est mesuré, et il est petit. Sur les douze chantiers de bordure :

|                        | avant | après |
|------------------------|------:|------:|
| axe hors de sa terre   | 4,35 m | **0,61 m** |
| ce que le plan prévoit dehors | 3,90 m | **0** |
| couverture au pire     | 99,1 % | 97,1 % |
| temps                  | 24 950 img | **22 868** |

Trois cellules de tournière sur les 345 d'un épandeur de douze mètres, qui est le plus large
des outils et donc celui qui tourne le plus large. Un rayon de braquage de tolérance a été
essayé et rejeté : il rend 0,7 point de couverture pour 2,4 m d'herbe et huit pour cent de
temps en plus.

Le mur reste prioritaire. Sur un bord adossé à la clôture de la ferme, `VIRAGE_BORD` moins le
jeu rentre le sommet **plus loin** que le bord de la parcelle : c'est ce terme-là qui garde la
clôture debout, et il domine. Mesuré : le sommet ne sort de la terre nulle part, et il garde
2,20 m du premier mur là où ce mur est plus près que le bord.

### Ce que les bancs disent, et ce qu'ils disaient de faux

Trois bancs mesuraient l'escargot ; ils mesurent maintenant les lignes. Deux d'entre eux
mentaient sur autre chose, et c'est en les réécrivant qu'on l'a vu.

**Le panneau « À VENDRE » restait planté au milieu du champ mesuré.** `activateParcel`
n'enlève pas le décor — c'est l'*achat* qui le fait, et les trois chemins d'achat du jeu
retirent bien `signObs`, un renversable de 1,60 m planté 2,40 m à l'intérieur du coin. Les
bancs, eux, appelaient `activateParcel` directement et le laissaient là. Ils mesuraient donc
un plan qui contourne un poteau invisible que le joueur n'a jamais : la machine s'en écartait
et allait coucher la clôture d'à côté. Une fois le panneau retiré comme le jeu le retire,
**les deux dernières clôtures couchées disparaissent** et la couverture du pire cas passe de
82,9 à 90,7 %.

**Le banc posait la machine derrière la clôture de la ferme.** Il la plaçait à neuf mètres
du coin nord-ouest de la parcelle. Sur les parcelles de bordure, ce point tombe *sept mètres
derrière* la clôture, hors du réseau de chemins : la route vers le chantier devait alors la
franchir, et le banc comptait comme défaut du pilote ce qui n'était que sa propre mise en
place. Elle part maintenant du croisement de chemins le plus proche — là où le jeu amène
lui-même un tracteur qui vient de la ferme.

**« De combien l'axe sort de sa terre » ne mesure plus rien tout seul.** Le demi-tour demandé
se fait *dehors*, sur la tournière : la borne de 2,50 m interdisait le demi-tour lui-même. La
mesure se coupe donc en deux, et chaque moitié dit quelque chose — le *plan* sort de tant, et
c'est `planAuto` qui le décide, borné à `VIRAGE_BORD` du premier mur ; la *machine* ne doit
pas sortir plus loin que son plan, à un dépassement de virage près. Le second chiffre est le
seul qui parle du pilote, et c'est celui qui dérapait : **1,31 m** au-delà d'un plan qui sort
de 3,90, pour 2,20 admis. Ce qui protège la clôture, ce n'est plus l'excursion mais la
**marge au mur** — continue, là où le compte de courses couchées est un seuil.

Relevé final sur les douze chantiers de bordure, les plus contraints du jeu : **zéro clôture
couchée** en venant, en travaillant et en repartant, **99,1 %** de la terre faite au pire,
1,70 m de jeu au mur, une seule passe par parcelle.

## Le bouton prend la couleur de son cercle, et la mission se signe

Deux défauts signalés le même jour, et qui tiennent tous les deux à ce que la colonne de
boutons sait de la mission en cours.

**« Le point de chargement au silo est jaune, mais le bouton pour charger est bleu, c'est
n'importe quoi. Le chargement fait partie de la mission, ça doit être jaune. »** Il avait
raison, et voici pourquoi. `estMission()` lisait `missionVisible().lignes`, c'est-à-dire ce
qu'il faut **livrer au commerce**. Charger trente kilos de blé au silo n'y figure pas : c'est
une *étape du chemin*, pas une ligne de commande — et `Sic`, le commerce où l'on se tient,
vaut `null` au silo. La condition tombait à faux avant même de regarder l'action. Ce qui
sait, lui, c'est `objectifMission()` : c'est déjà lui qui allume l'anneau au sol. On lui
demande donc.

**Et seulement le bon bouton.** Recopier la couleur de l'anneau sur tous les boutons du lieu
serait faux deux fois. Hors mission, l'anneau du silo est déjà jaune pour dire « il y a
quelque chose à faire ici », et le jeu continu se joue en bleu. Et sur un poste il y a
plusieurs boutons : arrivé au silo avec vingt kilos dans la benne pendant qu'on vient en
chercher, on trouve `RENTRER BLÉ 20 KG` et `CHARGER BLÉ 80 KG` — même lieu, même
marchandise, sens opposés. On exige donc les trois à la fois : le même lieu, la même
marchandise, et le même **sens**. L'objectif dit `charger`, le bouton doit remplir. Le banc
mesure exactement ce cas-là.

Cela ne retire aucun bouton : le filtre « là où la mission envoie, il n'y a que la mission »
ne se déclenche que sur un *commerce*, et les postes de la ferme n'en sont pas.

**« Après la mission de la Coopérative, j'avais encore du chargement avec moi ; à la
deuxième, à l'Usine céréales, ça n'a pas demandé de valider la mission. C'est valable
uniquement pour la première mission de la Coopérative. Après il faut rejouer la mission du
début à chaque fois. »** Le raccourci — arriver chargé de ce que la mission attend la signe
toute seule — avait été demandé pour la sortie du tutoriel, où le jeu vient de faire
labourer, semer, moissonner et charger trente kilos *pour cette mission-là*. Il s'appliquait
aux trente. Il ne s'applique plus qu'à la première, et pas seulement par goût : le tutoriel
ne fait charger que la première commande. Aux suivantes, le blé qui reste dans la benne est
un reliquat, pas une intention — **mesuré, un seul kilo oublié après la Coopérative suffisait
à signer les quatre-vingts kilos de l'Usine céréales**, et le joueur n'avait jamais lu ce que
le client lui demandait.

**Un troisième défaut est tombé avec le deuxième**, invisible tant que la signature était
automatique. Devant un client qui propose encore sa mission, on trouvait côte à côte le
bouton vert `VOIR LA MISSION` et le bouton bleu qui brade au même guichet la marchandise que
la mission attend — exactement l'alternative dont le joueur ne voulait pas. Le juge qui
retire la vente libre ne regardait que la mission *déjà signée*. Il regarde maintenant aussi
celle **à prendre**. La Coopérative garde sa vente libre : c'est l'exception nommée, et elle
tient par `LIEUX_SERVICE`, qui la range avec le garage et le comptoir.

**Et le premier quart d'heure aussi, qui était la scène exacte du joueur.** Le tutoriel envoie
au silo deux fois — vider la trémie, puis charger trente kilos dans le pick-up — et l'anneau y
est jaune. Mais l'objectif du tutoriel ne portait que `quoi:'tuto'`, sans clé ni geste : la
colonne ne pouvait pas savoir laquelle de ses lignes l'étape attendait, et les peignait toutes
en bleu. Les deux étapes concernées déclarent maintenant ce qu'elles veulent — `quoi` et
`prod`, deux **champs facultatifs sur des lignes existantes**, parce que `CAMPAGNE.tuto` est
un indice dans cette table et qu'ajouter ou déplacer une ligne renverrait une partie
sauvegardée à la mauvaise étape. Une étape sans geste, elle, ne désigne rien : au champ il n'y
a pas de bouton à peindre.

Un défaut latent est tombé avec : `traire2` manquait à la table des rangs de la colonne.
`rang[A.sens]` rendait `undefined`, la soustraction rendait `NaN`, et le comparateur de `sort`
recevait `NaN` — l'ordre des boutons devenait celui du moteur JavaScript. C'est le second tank
d'une brebis, qui donne de la laine en plus de son lait : deux boutons CHARGER au même enclos.

## L'atelier au bout de la cour, et deux réserves au milieu

**« Déplace l'atelier de production tout à droite de la parcelle — attention, tiens compte du
fait que cet atelier peut évoluer en taille — parce qu'on va ajouter au milieu, entre le silo
et l'atelier, des cuves à graines et engrais, l'une au-dessus de l'autre, avec les cercles
pour s'approvisionner à droite des bâtiments. »**

**Le piège est dans l'incise.** La cour de transformation va de x = 43,2 à x = 104,4.
L'atelier ne fait pas la même taille à tous les paliers : mesuré, 14,55 m d'emprise visible
au palier zéro et 27,55 m au dernier, dont 13,51 m à droite de son point d'ancrage. Le poser
au bord au palier zéro, c'est le faire sortir du terrain au palier neuf. Il est donc calé sur
sa **taille finale** : à x = 90,8, son flanc droit tombe à 104,31 au dernier palier — neuf
centimètres du bord — et il n'en sortira jamais. Le banc le vérifie palier par palier.

Son flanc gauche, lui, recule de 81,95 (palier 0) à 76,76 (palier 9). C'est cette borne-là
qui décide de la place des cuves, et non celle d'aujourd'hui. Entre le cercle du silo, qui
porte jusqu'à x = 63,5, et ce flanc gauche au pire, il reste une bande de treize mètres : les
cuves s'y posent à x = 67, leurs cercles à x = 72 — cinq mètres à leur droite, comme demandé,
et 1,93 m de dégagement devant l'atelier le plus grand qu'on puisse construire.

**Ce qu'elles sont.** Le hangar à graines et le bac à engrais avaient un compte —
`STOCK.graines`, `STOCK.engrais` — et aucun bâtiment : on achetait au comptoir, on
remplissait au comptoir, et le stock de la ferme n'existait que dans un menu. Il a maintenant
deux cuves dans la cour, avec leur jauge et leur vanne, et c'est là qu'on vient s'y servir.
**L'achat ne bouge pas** : il reste au Comptoir agricole, où l'on voit le bac et le prix.

La règle d'avant disait « remplir la cuve de l'outil : au comptoir, et nulle part ailleurs »,
et son argument était juste — la cour le proposait *partout*, donc nulle part en particulier,
et rien ne disait ce qu'il restait au hangar. Ce qui a changé, c'est que le hangar existe. Et
chaque cuve ne sert que ce qu'elle contient : devant la verte on remplit un semoir, devant la
blanche un épandeur, l'inverse ne propose rien.

**Elles ne se ressemblent pas, et c'est voulu.** On les voit de loin, de trois quarts : c'est
la silhouette qui doit dire laquelle est laquelle avant qu'on lise quoi que ce soit. La
graine est une cuve trapue en polyéthylène vert, cerclée de son armature, goulotte à hauteur
de semoir ; l'engrais est haute, blanche, perchée sur charpente contreventée, parce qu'elle
se vide par gravité. Leurs échelles sont mesurées et non choisies : posées à `BAT_ECHELLE`,
elles faisaient 2,64 m de diamètre et la cuve verte n'arrivait pas au toit de la cabine du
pick-up garé devant — on n'y lisait pas une réserve de ferme mais une maquette. La verte
monte donc à ×1,60 (3,58 m de diamètre, 7,36 m de haut) et la blanche à ×1,35 (8,50 m de
haut) : le modèle est déjà haut par construction, et le multiplier autant que sa voisine
l'aurait fait culminer au niveau du silo, qui est le repère de la cour.

Les deux cercles sont **bleus et restent allumés**, comme celui de la cuve à gazole et pour
la même raison : on ne va pas chercher de la graine parce qu'une lumière s'allume, on y va
parce qu'on en manque — et la jauge du bandeau le dit déjà.

## Plus de dalles, et du fourbi autour du silo

**« Supprime les dalles des nouvelles citernes de ressources, et aussi de l'atelier et de ses
évolutions. »** La cour de transformation est déjà une dalle de bitume d'un seul tenant, du
chemin de sable jusqu'au bord est — c'était le premier arbitrage de sa refonte. Poser une
seconde dalle dessus, c'était peindre du gris sur du gris et découper le sol en petits carrés
là où il doit se lire d'un tenant. Trois disparaissent :

- le socle des deux cuves à graines et à engrais ;
- le **quai de béton** de l'atelier, qui grandissait en plus avec les paliers — sept mètres
  sur quatre au premier, douze sur six au dernier — si bien que le découpage changeait de
  forme à chaque métier acheté ;
- le socle sous chacun des tanks de la fromagerie et du pressoir.

Les cuves et les tanks descendent de l'épaisseur qu'ils n'ont plus : ils étaient dessinés
*posés sur* leur socle et flottaient de dix-huit à trente centimètres une fois celui-ci
retiré. Ce qui reste au sol devant l'atelier, ce sont les sacs, les palettes et les caisses :
du travail posé, et non un dessin de sol.

**« Mets des caisses et des objets à côté du silo pour donner des petits détails à cet
espace. »** La tour se dressait sur vingt mètres de bitume vide : rien au sol, rien contre ses
tôles. Elle a maintenant ses palettes de sacs, ses fûts, ses jerricans, ses caisses de bois,
sa pile de pneus, sa brouette et son diable appuyé contre la tôle — plus un tas entre les deux
réserves, qui sont deux magasins et devant lesquels ce qu'on range finit toujours par traîner.

**Où, et pourquoi pas ailleurs.** Trois choses interdisent le reste de l'espace, et elles sont
mesurées : la **voie d'accès** du silo, large de neuf mètres, court en x = 59 du nord au sud —
c'est par là que tout arrive et repart ; l'**emprise** de la tour vaut 3,30 m de rayon ; et le
bitume s'arrête à x = 43,2. Tout tient donc à l'ouest, au nord et au sud de la tour, entre son
emprise et le bord de la dalle, plus le creux entre les deux cuves — le seul endroit du milieu
de cour où rien ne roule, la voie s'arrêtant à 63,5 et les cercles d'approvisionnement
commençant à 68,4.

**Et rien de tout cela n'arrête un engin.** Aucun de ces objets ne pousse d'obstacle : c'est la
règle que suit déjà le fourbi de l'atelier, et c'est la bonne, parce qu'un décor qui bloque un
épandeur de douze mètres dans sa propre cour est un piège et non un détail.

## La Brasserie devient l'Épicerie, et la bière se brasse à la ferme

**« Vu que la Brasserie nous demande de l'orge, mais que juste après on va fabriquer sa propre
bière, la Brasserie n'a plus lieu d'être. »** Le joueur a vu juste, et le défaut était visible
au palier six : la mission 9 lui faisait porter 200 kg d'orge à la Brasserie *pour qu'elle en
brasse la bière*, la mission 10 lui faisait livrer 140 L de bière au Restaurant, et le même
palier lui vendait la **cuve de brassage** de sa halle. Le village achetait donc la matière
première d'un métier qu'on venait tout juste d'acquérir. Pire, l'arithmétique tournait en
rond : 200 kg d'orge × 0,70 de rendement font très exactement 140 L, c'est-à-dire **la même
orge comptée deux fois**, payée deux fois, sur deux missions.

**Ce qui remplace les deux.** Le rang 9 va maintenant au **Restaurant**, qui ne commande pas de
la bière mais *cherche quelqu'un qui la brasserait* : « Je cherche quelqu'un qui cultiverait de
l'orge dans le coin et qui se lancerait dans une bière artisanale — une vraie, brassée ici. »
C'est l'orge et la cuve d'un seul mouvement, et le joueur reste propriétaire de sa filière d'un
bout à l'autre. Le rang 10 va à l'**Épicerie**, qui ouvre un rayon de produits de la ferme —
60 L de bière et 120 kg de farine — sur la recommandation du Restaurant. On retombe donc bien
sur **trente missions**, et les primes et l'expérience ne bougent pas d'un euro : 3 200 € /
220 XP au rang 9, 3 600 € / 240 XP au rang 10, comme avant.

**L'Épicerie prend la place de la Brasserie, sur place.** Le rang 0 de `SITES` est **renommé**,
jamais déplacé : `negoce` est sérialisé par position, et sortir la Brasserie pour ajouter
l'Épicerie en fin de table déplacerait le contenu de tous les commerces d'un cran. Elle garde
donc le rang, la bande ouest, le `bat` et — comme demandé — les **clôtures en muret** de la
Brasserie. Elle n'apporte **pas de dalle** : le jeu en pose déjà une sous chaque commerce, et
une seconde épaisseur à deux centimètres au-dessus de la première est un défaut que ce fichier
a déjà corrigé une fois.

**Sa taille.** L'ancienne Brasserie faisait 22,82 m de large — pas parce qu'une brasserie est
grande, mais parce que ses trois cuves de cuivre sortaient six mètres sur le côté. C'était
l'exception du village, pas la règle. L'Épicerie est mesurée à **16,04 × 13,31 m**, ce qui la
range entre le Marché (16,76) et la Fromagerie (16,65), et bien au-dessus de la Boulangerie
(10,62), de la Boucherie (10,03) et du Caviste (10,50) : une devanture de commerce de village,
à la taille des autres. Le rang ouest — maison, Épicerie, Caviste — mesure maintenant
**38,54 m** d'un tenant contre 39,32 du temps de la Brasserie ; il reste le plus court des
appariements possibles, et les deux plus grosses dalles restent séparées par une maison.

**Ce qu'elle achète, et pourquoi à ce prix.** Le fichier tient une hiérarchie stricte entre
acheteurs — plus on paie cher, moins on tient — et se méfie des acheteurs strictement dominés,
qui n'auraient aucune raison d'exister. L'Épicerie s'y insère à **1,18 pour 1 200** : caviste
1,33 pour 600, restaurant 1,28 pour 900, **épicerie 1,18 pour 1 200**, marché 1,09 pour 2 000,
supermarché 1,00 pour 9 000. Elle ne domine personne et personne ne la domine. Elle prend ce
qu'une épicerie de village met en rayon — tout ce qui se mange, de la ferme d'à côté. Pas la
laine : ce n'est pas de l'épicerie.

### Ce qu'une vieille sauvegarde traversait sans garde

Trois choses, et deux d'entre elles étaient **silencieuses**. Elles ne tiennent pas au dessin
du bâtiment mais à la façon dont le fichier range son état.

- **`CAMPAGNE.mission` est un INDICE**, pas un nom de mission ; et `CAMPAGNE.faits` est indexé
  par *ligne* de la mission de ce rang. Une partie arrêtée au rang 9 avec `faits:[150]` — cent
  cinquante kilos d'orge déjà portés à la Brasserie — se relisait sur la nouvelle mission du
  même rang, qui demande 140 L de bière : `veillerMission()` la soldait **à la première
  image**. Trois mille deux cents euros, deux cent vingt points d'expérience et la découverte
  de la cuve, sautés d'un coup, sans un mot. C'est la régression la plus coûteuse des trois.
  La sauvegarde écrit donc maintenant `mv`, le **rang de la table des missions**, et
  `MISSIONS_REECRITS` dit lesquelles ont changé de contenu depuis. Le chargement remet ces
  missions-là à zéro, et **elles seules** : le rang 12 garde son avancement, et une partie
  enregistrée depuis garde le sien. On perd au pire une mission à moitié faite, jamais une
  mission finie — le rang n'avance qu'une fois la mission soldée. Elle est aussi **rendue au
  commerce qui la propose** : une mission réécrite a changé de marchandise *et* de commerce,
  la garder « prise » ferait porter au joueur un ordre qu'aucun marchand ne lui a donné et lui
  ferait sauter le seul endroit où le nouveau texte se lit. Ajouter une mission *à la fin* ne
  coûtera toujours rien ; c'est insérer ou réécrire qui se paie ici.
- **La renommée est le seul état durable rangé par NOM de commerce.** La clé écrite hier était
  `'Brasserie'`, celle qu'on cherche aujourd'hui est `'Épicerie'` : le test échouait, la
  renommée retombait à zéro, et un joueur qui avait servi ce commerce dix fois — prime ×1,5,
  attente −70 % — repartait de rien sans que rien ne l'en avertisse. Une table d'anciens noms,
  `SITES_ANCIENS_NOMS`, rattrape la clé, et ne sert que si le nouveau nom est absent.
- **Un contrat est repéré par nom de lieu.** Un contrat d'orge accepté chez la Brasserie
  devenait insolvable chez l'Épicerie, qui n'en achète pas ; et comme le temps ne court que sur
  les contrats à délai, il occupait *pour toujours* une des quatre places. Le chargement le
  laisse donc tomber — la règle est générale, et vaudra pour le prochain commerce qui changera
  de métier. Elle ne se voit qu'en **mode libre** : en campagne, `remplirCommandes(0)` balaie
  déjà les contrats au chargement.

Ce que la trémie du rang 0 contenait, enfin, est filtré à la relecture : l'Épicerie héritait
sinon de jusqu'à 335 kg d'orge, invisibles et éternels, puisqu'elle ne fabrique plus rien.

**Sept contrôles nouveaux dans le banc `campagne`** tiennent tout cela : que la sauvegarde
écrit le rang de la table, qu'une mission réécrite repart de zéro, qu'elle est rendue au
Restaurant qui la propose, qu'une mission intacte garde son avancement, qu'une sauvegarde
d'aujourd'hui garde le sien *et* sa prise, que la renommée change de nom sans que celle des
autres bouge, et qu'en mode libre le contrat du commerce disparu tombe pendant que les deux
autres restent. Le banc `chaine` mesurait, lui, une vraie règle — « on
verse dans une trémie d'usine, elle transforme, elle paie toute seule, on repart vide, on ne
peut rien y recharger » — mais il l'avait écrite sur le seul commerce qui disparaissait. Il est
repointé sur l'**usine à avoine**, qui a exactement le même profil, plutôt que supprimé : la
règle valait mieux que l'exemple.

## Une plante, moins de triangles — et deux ceps sur trois

**« Est-ce que tu peux faire qu'une vigne égale un objet, un olivier égale un objet,
pareil pour les plantes ? »** Une vigne *était déjà* un objet : chaque pied est une
géométrie unique, fusionnée une fois pour toutes au démarrage par `mergeParts`, et les
8 500 pieds de la ferme ne coûtent que **vingt appels de dessin**. Il n'y avait donc rien
à fusionner. Ce qui pesait, c'est le nombre de triangles *dans* cet objet — et le relevé
était sans appel : sur une image prise à la caméra de jeu, vingt parcelles plantées,
**96,2 % des triangles étaient des cultures** (459 546 sur 477 852).

Le détail disait où. Un olivier, c'était un tronc, **cinq** charpentières, **cinq** masses
de feuillage et **cinq** olives ; une vigne, un piquet, un fil, un cep, **quatre**
sarments, **trois** masses et **trois** grappes ; une céréale, **trois** talles.

| plante | avant | après | |
| --- | --- | --- | --- |
| Blé | 54 | **36** | −33 % |
| Orge | 72 | **36** | −50 % |
| Avoine | 72 | **36** | −50 % |
| Colza | 60 | **42** | −30 % |
| Maïs | 36 | **36** | inchangé — il était déjà le moins cher |
| Vigne | 138 | **66** | −52 % |
| Olivier | 186 | **78** | −58 % |

**Une seule masse par pied, sauf pour l'olivier.** Trois masses de feuillage coûtaient
soixante-douze triangles sur les cent trente-huit d'une vigne — plus de la moitié — pour
un relief qu'on ne lit qu'en s'agenouillant dans le rang. Une masse assez longue fait la
même haie, parce que c'est le **recouvrement d'un cep sur l'autre** qui la ferme, et non
l'empilement sur un même cep. L'olivier, lui, a résisté : réduit à une seule masse il
devenait un parasol plat — très exactement le défaut que le commentaire d'origine disait
avoir corrigé une fois. Il en garde **deux**, décalées en hauteur *et* au sol, la
principale plus haute que large : c'est ce qui la rend ronde.

**Et la densité est compensée, ce qui ne coûte pas un triangle.** Au premier essai le
champ s'éclaircissait : on voyait la terre entre les rangs là où le tapis était fermé —
le défaut que le commentaire des talles annonçait, mot pour mot. Les deux talles
s'écartent donc autant que les trois d'avant, et ce qui reste grossit : épis d'un quart,
barbes plus longues, grains d'avoine plus écartés, grappes de colza plus larges. Le maïs
n'a pas changé d'un triangle : il sert de témoin dans les captures avant/après.

### Deux ceps sur trois le long du rang

**« Sur les lignes de vigne, divise le nombre de vigne par 1,5 sur chacune des lignes. »**
Le masque de la vigne ne décidait que de l'écartement des **rangs** — un sur deux, soit
2,60 m — et posait un pied dans chaque cellule du rang, tous les 1,30 m. Il garde
maintenant deux mailles sur trois : l'entraxe moyen passe à **1,95 m**, et le nombre de
ceps dessinés sur une parcelle tombe de **276 à 180** — un rapport de 1,53 pour 1,5
demandé, l'écart venant des rangs de bordure.

**La grille ne permet pas un écartement régulier.** Sur un pas de 1,30 m, deux tiers
donnent 1,30 puis 2,60, en alternance. On étire donc le feuillage le long du fil pour que
la haie reste fermée même sur le grand écart — et l'étirement se **calcule** : une touffe
est un cylindre à six pans, dont l'emprise vaut 1,73 fois son rayon et non deux. Un
premier essai à 1,66 laissait dix-neuf centimètres de jour et le rang se lisait en
pointillé ; il faut 2,60 / (1,73 × 0,84) = 1,79, on prend **2,00**, soit 2,90 m d'emprise
pour 2,60 m de jour. Le fil de palissage suit : **2,75 m** au lieu de 1,40, de quoi
rejoindre le voisin le plus lointain. Il se recouvre franchement sur le petit écart —
un fil qui se superpose à lui-même ne se voit pas, un fil qui s'interrompt se voit tout
de suite.

**Et la récolte ne bouge pas d'un gramme.** Le fichier l'avait déjà écrit pour l'olivier :
« le masque de plantation ne réduit pas la récolte, il ne décide que des pieds DESSINÉS ».
Toutes les cellules du rang sont semées et toutes se moissonnent. Ni les missions, ni les
contrats, ni la capacité de la ferme ne s'en aperçoivent — et les dix-neuf bancs passent
sans qu'on ait touché à un seuil.

**Le relevé, à la caméra de jeu, vingt parcelles plantées :**

| | avant | après |
| --- | --- | --- |
| triangles par image | 235 578 | **143 358** (−39 %) |
| appels de dessin | 86 | 85 |
| triangles d'une parcelle de vigne | 38 088 | **11 880** (−69 %) |

Les appels ne bougent pas, et c'est la preuve que le levier n'était pas là.

## La passe d'ombre, qu'aucun compteur ne comptait

**« Supprime les ombres sur les champs, ça peut peut-être alléger aussi. »** Les cultures
ne **projettent** pas d'ombre — `champDe` ne lève que `receiveShadow` : il n'y avait rien
à supprimer de ce côté. En cherchant, on est tombé sur autre chose.

**`renderer.info.render.calls` ne compte pas la passe d'ombre.** 468 appels avec les
ombres, 468 sans. Tous les chiffres d'appels de ce fichier — et ceux du README — ne
parlaient que de la passe principale, et la seconde passait sous le radar depuis toujours.
Comptée à la main, dans les cultures : **90 appels pour l'image, 250 pour son ombre.**
Près de trois fois plus, pour un dixième des triangles — 80 triangles par appel, c'est-à-
dire des miettes redessinées une à une.

**Une ombre a une portée, et elle se calcule.** Le soleil est en (50, 78, 24) : une ombre
s'étend horizontalement de √(50² + 24²) / 78 = **0,71 fois la hauteur de l'objet**. Le
plus haut du jeu — un arbre de douze mètres — jette donc la sienne à 8,5 m. Un objet à
plus de neuf mètres hors du cadre ne peut *pas* y poser d'ombre : le redessiner est du
travail pur. Or la boîte d'ombre couvrait **170 m de côté pour une caméra qui voit 93 m**.

Elle passe à **130** : 93 m vus, plus 18,5 m de marge à chaque bout, soit plus du double
de ce que la plus longue ombre du jeu réclame.

| | avant | après |
| --- | --- | --- |
| dans les cultures | 250 appels d'ombre | **118** (−53 %) |
| devant le village | 169 | **92** (−46 %) |
| dans la cour de la ferme | 316 | **265** (−16 %) |

Les captures avant/après sont les mêmes au trafic près — 2,8 % de pixels dans les champs
et 4,2 % dans la cour, pour un **bruit de fond de 2,0 %** relevé entre deux rendus de la
même image, une voiture ayant avancé entre les deux. Et la carte y **gagne** en finesse :
2 048 pixels sur 130 m font 15,7 px/m au lieu de 12,0.

**On ne descend pas plus bas.** À 110 m le gain monterait à −76 % dans les cultures, mais
la marge tomberait à 8,5 m — très exactement la portée de l'ombre d'un arbre : le premier
peuplier au bord du cadre verrait la sienne apparaître d'un coup. C'est la marge qui fixe
le nombre, pas le gain.

### Ce qu'on n'a PAS fait, et pourquoi

Le premier relevé annonçait « 125 projetants de moins de cinquante centimètres, à couper ».
C'était une **erreur de critère** : ces cinquante centimètres étaient l'ÉPAISSEUR de
l'objet, pas sa hauteur au-dessus du sol. Les couper aurait emporté les lisses de clôture,
les fils, les rives de toit — tout ce qui est mince et haut placé, et dont l'ombre se voit
parfaitement. Le fichier avait d'ailleurs déjà tranché la question dans l'autre sens :
`OMBRE_MIN = 1,4 m` écarte les bricoles **sur leur emprise au sol**, et son commentaire dit
mot pour mot « une lisse de clôture de trois mètres garde son ombre, le piquet qui la porte
non ».

Ce qui restait honnêtement à prendre — les objets à la fois plats *et* posés au sol, dont
l'ombre tombe sous eux — vaut **9 à 16 appels sur 317**, soit 3 à 5 %. Le seul endroit où
l'appliquer proprement serait une passe qui parcourt la scène après chaque construction :
beaucoup de mécanique fragile pour neuf appels de dessin. On s'en passe, et on l'écrit ici
pour que la question ne se repose pas.

## Trente images plutôt que soixante, si on veut

**« Je sais qu'on peut changer les FPS pour que ça rame moins, en passant à 30 au lieu de
60 — c'est possible ? »** Oui, et la boucle s'y prêtait déjà : elle est entièrement pilotée
par `dt`, clampé à 50 ms, donc rien de la simulation ne dépend de la cadence. Mais il faut
dire ce que le plafond fait, et surtout ce qu'il ne fait pas.

**Plafonner ne rend aucune image moins chère.** Une image qui coûte quarante millisecondes
en coûtera toujours quarante, et sur un appareil déjà sous les trente images le plafond ne
change rien du tout. Ce qu'il change, c'est le travail par **seconde** — de moitié — donc
la chaleur, donc la batterie, donc le moment où le téléphone se bride lui-même. C'est ce
bridage thermique qui fait qu'une partie devient poussive au bout de cinq minutes, et pas
le coût d'une image. Et il change une seconde chose, qui se voit tout de suite : un
appareil qui tient quarante à cinquante-cinq images de façon **irrégulière** paraît plus
saccadé qu'un trente parfaitement régulier. La régularité se lit mieux que le nombre.

**La manière compte autant que le principe.** Refuser une image tant qu'il ne s'est pas
écoulé 33,3 ms donnerait, sur un écran à soixante hertz, une image à 16,7 puis une à 33,3 :
deux images d'affilée d'inégale durée, c'est-à-dire du sautillement — pire que pas de
plafond du tout. Une tolérance de quatre millisecondes fait qu'on prend le battement
d'écran le plus proche : un sur deux à 60 Hz, un sur trois à 90, un sur quatre à 120.
`last` n'avance qu'aux images **rendues**, si bien que le `dt` d'une image plafonnée vaut
les deux battements écoulés et que rien ne ralentit.

Relevé — le banc ne tient que onze images par seconde et ne peut donc pas *mesurer* un
plafond à trente : on appelle `loop()` à la main, avec les battements exacts de chaque
écran, et l'on regarde lesquels sont rendus.

| écran | plafond | images rendues | durées vues | temps simulé |
| --- | --- | --- | --- | --- |
| 60 Hz | aucun | 60 /s | 16,7 ms | 2,000 s |
| 60 Hz | 30 | **30 /s** | 33,3 ms | 2,000 s |
| 90 Hz | 30 | **30 /s** | 33,3 ms | 2,000 s |
| 120 Hz | 30 | **30 /s** | 33,3 ms | 2,000 s |
| 30 Hz | 30 | 30 /s | 33,3 ms | 2,000 s |

Une seule durée par ligne : la cadence est **régulière** sur les trois écrans. Et le temps
simulé est identique partout — la ferme ne pousse ni plus vite ni moins vite.

**Le réglage vit dans « Image », à côté du zoom**, et il vaut soixante par défaut : on ne
bride personne d'office. Il se sauvegarde comme le zoom et le choix des commandes, en champ
facultatif — une partie d'avant vaut soixante, et `v` ne bouge pas.

### Une chance « par image » n'en est pas une

Quinze bouffées du jeu — poussière de roues, menue paille du batteur, fumée à la grille,
vapeurs de transfert — étaient tirées à `Math.random() < p` **une fois par image**. Tant
que le jeu tournait à soixante, cela faisait 60 p bouffées par seconde et personne ne s'en
apercevait ; le jour où l'on plafonne à trente, le décor se vide de moitié. Pire : sur un
téléphone qui peine, la poussière se serait raréfiée exactement quand le jeu ralentit,
c'est-à-dire au pire moment. La probabilité se lit donc maintenant **par seconde** et se
ramène à l'image écoulée, avec un plafond à quatre images de retard pour qu'un à-coup d'une
demi-seconde ne crache pas trente bouffées d'un coup.

## Le bouton dit le geste, et la lame prend ce qu'elle a couché

**« Quand on veut déposer ou charger des produits qu'on sélectionne avec le curseur, le
bouton s'appelle "lancer la production". Ce nom ne doit être que pour produire ; pour le
reste il doit porter le nom de ce qu'on veut faire. »** Le libellé était écrit **en dur
dans le HTML** — c'est celui de l'atelier, le premier endroit qui a eu un curseur — et
`ouvrirQuantite` savait pourtant déjà le remplacer. Seuls l'achat de semence et celui
d'engrais s'en servaient : partout ailleurs on demandait au fermier de « lancer la
production » pour charger une benne de blé ou vendre son lait.

Chaque sens dosable porte maintenant son verbe, dans une table jumelle de celle qui dit
quels sens ouvrent un curseur — même liste, mot pour mot, et c'est voulu : le jour où l'on
rendra un sens dosable, il faudra lui donner son verbe, faute de quoi il retombera sur le
libellé de l'atelier. Un banc le vérifie.

| sens | bouton |
| --- | --- |
| `prendre`, `prendreEntrepot`, `reprendre` | **Charger** |
| `traire`, `traire2` | **Collecter** |
| `vendre` | **Vendre** |
| `tremieVente` | **Déposer** |
| embarquer une bête | **Embarquer** |
| l'atelier, et lui seul | **Lancer la production** |

### Ce qui est sous et derrière la lame

**« Là il faut vraiment toucher parfaitement une culture pour la moissonner, du coup c'est
très facile de louper un brin lors d'un demi-tour. »** Le défaut était une asymétrie que
personne n'avait vue : le SOL était peint avec **92 cm de tolérance** autour de la bande
balayée, mais la PLANTE n'était fauchée que si son point tombait très exactement dedans —
**marge nulle**. Les deux ne disaient donc pas la même chose, et l'on voyait le passage
peint avec un brin resté debout au milieu.

**Deux tolérances, et pas une seule**, parce qu'elles ne se valent pas.

- **Côté, trente centimètres** : de quoi rattraper un pied semé au bord de la coupe — un
  pied porte un décalage de semis de ±28 cm — sans que la machine fauche visiblement plus
  large que sa barre.
- **Arrière, quatre-vingts centimètres, et rien devant** : « en prenant en compte ce qui
  est sous et derrière la lame, pas juste devant la lame ». C'est aussi ce qui se passe
  pour de vrai — un rabatteur ramasse ce qu'il vient de coucher — et c'est ce qui sauve le
  demi-tour, où la barre balaie un arc et frôle l'intérieur du virage. Une marge **avant**
  serait fausse : le champ se coucherait devant la machine.

`inSweep` gagne donc un paramètre `arriere` qui n'étire la bande que vers l'arrière, le
vecteur `(-rz, rx)` étant l'axe d'avance de l'outil.

**Relevé, au volant, sur une parcelle entière** — ce qui reste debout après un passage
complet :

| outil | avant | après |
| --- | --- | --- |
| labour | 2 cellules | **0** |
| semis | 1 | **0** |
| engrais | 5 | **0** |
| moisson | 3 | **0** |

Et en automatique, la couverture au pire cas passe de **97,1 % à 100 %**. Tout le reste du
relevé est identique au chiffre près — même nombre d'images (2 389, 1 809, 1 257, 2 280),
même dépassement hors de la terre (7,02, 7,58, 8,90, 2,93 m), même marge aux obstacles,
même nombre de passes, aucune clôture couchée. La machine roule donc exactement comme
avant, met exactement le même temps : c'est la lame seule qui est devenue clémente. La
couverture du SOL, elle, ne bouge pas d'un dixième — elle avait déjà sa tolérance.

## La poussière coûtait un tiers de l'image

**« Ça lag actuellement lorsque, en auto, mon tracteur laboure un champ et que je dérape
avec mon pick-up à côté. »** Une scène précise, donc reproductible : on l'a montée au banc
plutôt que de deviner.

**Le sol n'y était pour rien.** La première hypothèse — la charrue qui salit des tuiles de
terrain et les renvoie à la carte graphique, deux par image et 819 200 octets — ne tient
pas : mesuré dans cette scène, **zéro tuile salie par image**. On l'écrit ici pour que la
piste ne soit pas rouverte.

**Ce sont les bouffées.** Chacune était un `Mesh` à elle, avec SON matériau — c'est ce qui
lui donnait sa couleur et son estompage. Relevé dans la scène décrite : **trente-sept
bouffées vivantes en moyenne, quarante-deux au pire**, et elles font **quarante des cent
dix-huit appels de dessin**. Un tiers de l'image, pour 720 triangles. Rien ne pouvait les
grouper : cent trente objets, cent trente matériaux, chacun avec son programme et ses
uniformes. Et elles sont transparentes, c'est-à-dire la sorte qui coûte cher sur un
téléphone — triées à chaque image, et repeignant les mêmes pixels plusieurs fois.

Elles deviennent **un seul maillage instancié** : un appel, un matériau, la couleur par
instance. Les mortes restent dans le tampon à l'échelle zéro — la carte graphique les
traite, mais un sommet dégénéré ne peint aucun pixel, et cent trente icosaèdres de vingt
triangles font 2 600 triangles, moins qu'un pied de vigne sur une parcelle.

| dans la scène du joueur | avant | après |
| --- | --- | --- |
| objets pour la poussière | 130 | **1** |
| matériaux | 130 | **1** |
| appels de dessin pour la poussière | **40** | **1** |
| l'image entière | 118 appels | **72** |

**Le premier essai était raté, et la capture l'a dit.** Un matériau partagé n'a qu'UNE
opacité pour tout le monde : en exprimant la disparition par la seule échelle — la bouffée
grossit puis se résorbe — on obtenait des cailloux blancs opaques au lieu d'un nuage.
L'alpha revient donc **par instance**, avec un attribut `alpha` sur la géométrie et trois
lignes greffées au nuanceur par `onBeforeCompile` : les chaînes de three sont en clair même
dans la version compactée, et `gl_FragColor = vec4( outgoingLight, diffuseColor.a )` se
laisse multiplier. La formule d'estompage est celle d'avant, `op × (1 − t²)`, écrite
ailleurs — le rendu est le même.

Le **tri**, lui, disparaît : une seule maille se dessine dans l'ordre de son tampon et non
plus du fond vers l'avant. Sans conséquence ici — les bouffées d'un même nuage ont la même
couleur, et c'est très exactement le cas où l'ordre ne se voit pas.

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

## Deux façons de conduire

Le manche et la manette des gaz demandent de **doser une position** au doigt : c'est
précis, mais il faut regarder son pouce. Un réglage — *Réglages › Conduite* — les
remplace par des **boutons** : deux flèches à gauche, deux pédales à droite. Les deux
jeux vivent au même endroit et ne s'affichent jamais ensemble ; le reste du jeu ne sait
rien de ce choix, puisque les boutons écrivent dans les mêmes `steer` et `throttle`.

Les tracés viennent de la planche du joueur : une flèche pleine aux angles arrondis — pas
un chevron —, une grande **semelle d'accélérateur** dont le bord gauche est décroché en
bas, et un petit **frein** carré à deux barrettes. Les deux flèches se touchent presque,
et les deux pédales aussi : le pouce passe de l'une à l'autre sans lever la main. C'est le décrochement, plus que la
taille, qui distingue l'accélérateur au premier coup d'œil. Aucun dégradé : le contraste
vient du fond sombre de la pédale et d'une ombre portée statique — elle ne bouge pas,
donc le filtre ne coûte qu'un calcul, une fois.

**La pédale basse freine d'abord.** Un appui bref ralentit ; il faut la maintenir **et**
que l'engin soit presque arrêté pour qu'il parte en marche arrière. Sans ce verrou, un
coup de frein devant le silo ferait reculer la moissonneuse dans le champ. Une fois la
marche arrière engagée elle le reste jusqu'au relâchement : sinon, dès que l'engin
reprend de la vitesse en reculant, la condition se retournerait et l'on repasserait au
freinage en boucle.

Le frein au pied vaut **trois fois le frein moteur** — c'est ce qui rend la pédale
utile : relâcher les gaz ralentit, appuyer sur le frein arrête. Mesuré sur une seconde à
6 m/s : **0,01 m/s** au frein contre 0,72 en roue libre.

**Le bouton suit le doigt.** Chaque bouton capturait le pointeur pour lui seul : on
appuyait sur la flèche gauche, on glissait le pouce sur la droite, et c'était toujours la
gauche qui restait enfoncée — il fallait relever le doigt entre les deux, ce qui coûte le
temps d'un virage. La capture se pose maintenant sur le **groupe**, et c'est le point sous
le doigt qui désigne le bouton actif à chaque déplacement : gauche → droite, accélérateur
→ frein, sans décoller. L'écart entre deux boutons ne relâche rien — tant que le doigt
reste dans le cadre du groupe on garde le dernier appuyé, sinon traverser les six pixels
du milieu couperait les gaz le temps d'une image.

**Et aucun appui ne se perd.** Deux symptômes, une même cause : « parfois j'appuie et ça
ne fait rien », « parfois un bouton reste enclenché même quand je relâche ». L'état des
flèches et des pédales était **recopié à la main**, à trois endroits, à partir
d'événements qui n'arrivent pas toujours — un `pointerup` qui part sur le calque d'un menu
venu se poser par-dessus, un écran qui se verrouille sans rien émettre du tout, un
changement de mode qui cache l'élément en pleine capture.

Il n'y a plus qu'**une source de vérité** : la table des pointeurs de chaque groupe. `.on`
et `BTN` en sont *déduits* à chaque changement, et `relacherCommandes()` rend tout d'un
seul appel — à l'ouverture d'un menu, d'une fenêtre, du parc ou d'un curseur, quand
l'onglet passe derrière, quand le téléphone tourne, à chaque changement de mode. Trois
détails complètent le remède : le bouton sous le doigt se trouve par sa **boîte** avec six
pixels de tolérance (`.dir.on` rétrécit la flèche de sept pour cent — le dessin se
dérobait sous le doigt et le voisin répondait à sa place) ; on écoute
`lostpointercapture`, seul événement émis quand un élément est caché pendant la capture ;
et `touch-action:none` sur les quatre commandes empêche un geste du navigateur de voler le
doigt en chemin. Dix-sept contrôles rejouent les neuf chemins connus.

## Deux détails d'engin

**La roue braquée ne se voile plus.** Une roue directrice reçoit deux angles : le braquage
autour de Y, la rotation autour de son axe X. Dans l'ordre de composition par défaut de
three.js — `XYZ` —, c'est le braquage qui s'applique en premier dans le repère local et la
rotation qui s'ajoute ensuite autour du X de l'engin : la roue braquée tourne donc autour
d'un axe qui n'est plus le sien, et le pneu décrit un cône. C'est exactement l'aspect
d'une jante voilée, et cela ne se voyait qu'en virage — d'où la difficulté à le nommer.
Les roues composent maintenant en **`YXZ`** : la roue tourne d'abord autour de son propre
axe, l'ensemble est braqué après. La mesure est nette — on braque à 0,38 rad, puis on fait
tourner la roue d'un quart puis d'un demi-tour et l'on relève la direction de son axe :
**0,7062 d'écart avant, 0 après**. Le braquage visible passe au passage de 25,8° à 21,8°,
ce qui suffisait déjà à adoucir l'effet sans le corriger.

**Le passage de roue du pick-up.** Il se lisait comme une baguette posée le long de la
ridelle : six centimètres trop bas pour qu'on le prenne pour un caisson, et trop étroit
pour coiffer le pneu à l'aise — les sacs chargés le traversaient. Il a gagné **huit
centimètres de hauteur** et **huit de largeur** (0,70 m contre 0,62), puis **huit de plus
en hauteur** quand le joueur l'a redemandé : le caisson faisait 0,60 m pour une roue dont
le sommet est à 1,24, c'est-à-dire vingt-deux centimètres de tôle au-dessus du pneu, et il
se lisait encore comme une planche. À 0,68 son dessus passe à 1,54 et son liseré à 1,61, en
gardant **neuf centimètres sous celui des ridelles** (1,70) : le plateau se lit toujours
comme un plateau ouvert. Le plancher de la benne (0,86) ne bouge pas — c'est par le haut
que le caisson grandit.

**Et ses feux arrière sortent enfin du hayon.** Ils étaient posés à z = −3,47 ; le hayon,
lui, va de −3,51 à −3,61. La lentille se trouvait donc **devant** la tôle, entièrement
masquée par elle, et l'on n'en voyait que ce que le tri en profondeur laissait passer —
d'où l'impression, que le joueur décrit, d'un feu « à moitié enfoncé dans la benne ». Ils
reculent à −3,66 : mesuré, le boîtier sombre mord de cinq centimètres dans le panneau,
comme un enjoliveur, et **la lentille dépasse de dix**, sa face avant affleurant exactement
la tôle. On les voit de l'arrière, ce qui est la seule chose qu'on demande à un feu arrière. Le dehors ne bouge pas : il est plaqué contre la ridelle,
et le déborder ferait saillie sur le flanc. C'est donc vers l'**intérieur** de la benne
qu'il s'élargit — ce qui est aussi la seule chose qu'on en voie depuis la caméra, et ce
qui borne l'élargissement : les deux colonnes de sacs se rangent entre les caissons, et
elles ont dû se resserrer de 0,56 à 0,33 m de l'axe pour ne plus mordre la tôle. Elles la
mordaient déjà avant — un demi-sac fait 0,32 m de large, le caisson commençait à 0,74.

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

## Une parcelle n'est plus un rectangle posé sur l'herbe

Le sol est peint, et il l'était **à la règle** : quatre rectangles de terre, des chemins de
sable à bords parallèles, et pas un écart. Vu d'en haut, la ferme ressemblait à un plan
cadastral. Le joueur a demandé « un peu de variation et une structure moins rectiligne », et
« des petites taches de terre autour des parcelles de terre ».

**Le contour suit un bruit, pas un tirage.** Un hasard indépendant à chaque point donnerait
un contour hérissé, pas une lisière. La valeur est donc ancrée sur les entiers et interpolée
entre eux par une courbe douce, et l'on somme **deux octaves** : la première donne la grande
ondulation, la seconde — deux fois et demie plus courte, deux fois moins ample —
l'irrégularité de détail. Les quatre côtés d'une parcelle sont échantillonnés tous les
1,20 m et remplis en **un seul polygone** : un contour dessiné côté par côté laisserait
quatre coins ouverts.

**L'amplitude est bornée par le terrain, et c'est mesuré.** Une parcelle a 1,60 m d'herbe
devant elle avant le sable — c'est la plus courte des marges du monde, la parcelle voisine
est à 9,60 m et le bitume à 4,60. La crête théorique du bruit vaut 0,725 fois l'amplitude,
soit 0,40 m pour la terre et 0,56 pour le sable ; relevé sur le monde réel, 0,34 et 0,47.
Il reste au pire **0,93 m d'herbe** entre une terre qui gonfle et un chemin qui gonfle vers
elle. Les deux ne se touchent jamais.

**Les mouchetures suivent un carré.** Autour de chaque parcelle, des taches de terre
débordent sur l'herbe ; leur distance au bord est tirée en `u²`, ce qui les fait très
nombreuses contre la terre et de plus en plus rares au loin. Semées à distance égale, elles
auraient formé un liseré — c'est-à-dire une seconde ligne droite, exactement l'inverse du
but. Elles sont refusées sur le sable et sur le bitume : une tache de terre au milieu d'un
chemin ne se lit pas comme un débord de labour, elle se lit comme une salissure.

**La grille de culture, elle, reste rectangulaire — et c'est voulu.** Ce qui ondule est le
sol *peint*, pas ce qui se laboure. La terre qui déborde du rectangle est un décor : l'outil
qui passe dessus ne marque rien, puisque ces cellules-là sont hors parcelle. On voit donc
une lisière de terre non cultivable sur une quarantaine de centimètres, ce qu'un bord de
champ fait exactement dans la vraie vie — et pas une ligne du pilote, du marquage ou de la
sauvegarde n'a eu à changer.

**Le coût se paie une fois.** Tout cela est peint au démarrage dans la texture du sol, et
le remplissage passe par `worldDraw`, qui **borne** la recherche de tuiles : peindre une
parcelle de vingt mètres salit quatre tuiles et non les cent de la carte — une tuile déclarée
sale est redonnée en entier à la carte graphique. `paintStaticGround` prend **10 ms** au
chargement ; à l'image, rien.

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

### D'abord, ce qui était déjà fondu

Le joueur a demandé de fusionner en une seule forme tout ce qui ne bouge pas : la carcasse
des voitures du trafic, les animaux hors parties animées, et chaque pied de culture — « un
épi de maïs doit être un objet, une vigne doit être un objet, un olivier doit être un
objet, et tu conserves trois tailles de pousse ».

**Les trois l'étaient déjà**, et c'est la première chose à dire :

| ce qui était demandé | l'état réel, mesuré |
|---|---|
| la carcasse d'une voiture de trafic | **une seule géométrie**, 16 modèles, 595 primitives, 12 344 triangles au total — et un seul maillage par véhicule vivant |
| un épi de maïs | **6 primitives fondues**, 36 triangles |
| une vigne | **13 primitives** (16 en fruit), piquet et fil compris |
| un olivier | **16 primitives** (21 en fruit) |
| trois tailles de pousse par culture | `AGES_CULTURE` : **3 âges** pour les cinq céréales, **4** pour les deux permanentes, chacun sa géométrie |
| un animal, parties animées à part | **2 à 7 maillages** selon l'espèce — corps, tête, quatre pattes, queue —, le corps fondu, les pivots dehors |

**Et les roues du trafic ne doivent surtout pas en sortir.** « Isoler la carcasse des roues,
en laissant juste l'effet de suspension et de roulis » suppose que les roues aient besoin
d'être séparées pour que la suspension marche. Elles ne l'ont pas : la suspension et le
roulis sont portés par la **transformation du maillage entier** — `t.m.rotateX(t.pitch)`,
`t.m.rotateZ(t.roll)`, `t.m.position.y = t.heave` — et aucune roue de trafic ne tourne sur
elle-même. Les sortir de la géométrie ferait passer chaque véhicule vivant de **1 à 5 ou 7
maillages** : à treize véhicules au pire cas, **soixante-cinq appels de dessin de plus**
pour zéro pixel de différence. Elles restent donc dedans, et l'animation ne perd rien.

Même raisonnement pour les quatre pattes d'une bête : elles battent en diagonale par
paires, mais chacune pivote **autour de sa propre hanche**. Les fondre deux par deux ferait
tourner la patte arrière autour de l'épaule avant — deux maillages gagnés contre une
démarche fausse. On n'y touche pas.

### Puis la cour est passée au four

Le vrai gisement était ailleurs, et la passe de fusion l'avait sauté : elle avait pris les
quinze commerces, les maisons du rang et des bandes, les clôtures, le mobilier du village
et l'atelier — et **pas la cour de la ferme**, c'est-à-dire l'endroit où le joueur passe le
plus de temps.

| ce qui n'était pas fondu | maillages |
|---|---:|
| la maison de ferme | ~26 |
| le puits | 12 |
| le silo | 5 |
| le tuyau de chargement | 5 |
| les six bottes de paille | 6 |
| la cuve à gazole | 6 |
| l'aménagement d'un enclos (poste, mangeoire, abri) | 3 groupes, par pâture |

Tout cela est maintenant cuit. Mesuré, à l'identique sur les mêmes poses de caméra :

| | avant | après |
|---|---:|---:|
| objets dans la scène | 2 319 | **2 232** |
| maillages | 1 814 | **1 766** |
| géométries en mémoire | 348 | **312** |
| appels de dessin, vue de la cour | 255 | **220** |
| appels de dessin, vue du silo | 204 | **190** |

Trente-cinq appels de moins là où l'on conduit, soit **13,7 %**. Le prix : la boîte
englobante d'un objet fondu est celle de l'ensemble, donc quelques centaines de triangles
partent au GPU quand un seul volume serait visible — relevé à **+4 %** sur la vue de la
cour. C'est le compromis que la clôture du rang avait déjà appris à doser : on fond par
objet, jamais d'un tenant.

**Et la fusion a cassé une chose, exactement celle que son propre commentaire annonçait.**
`fusionnerGroupe` retire les volumes qu'il avale et appelle `dispose()` sur leur géométrie ;
tout ce qui bouge doit donc porter `userData.anime`. Le **tas de grain de la mangeoire** ne le
portait pas — il est construit, ajouté au groupe, et le groupe est fusionné dans la foulée. Le
jeu gardait son handle et continuait de l'étirer à chaque ration mangée, sur un maillage qui
n'était plus dans la scène : le tas était **cuit à taille pleine** dans la géométrie, et
l'auge paraissait pleine en permanence, pour les six espèces. Mesuré : boîte englobante de la
mangeoire **vide** à 0,95 m avant, 1,10 après — les quinze centimètres sont le tas. Une
contre-lecture adverse l'a trouvé, avec les deux captures côte à côte. Un drapeau, et c'est
réglé.

**Et sept matériaux n'en font plus qu'un.** `MAT_FUSION`, `treeMat`, `fenceMat`, `lampMat`,
`bushMat`, `birdMat` et `traficMat` étaient **identiques ligne pour ligne** — même classe,
même `vertexColors`, même `flatShading`, même `shininess` à zéro, même `specular` noir — et
aucun n'est modifié en cours de partie. Sept programmes compilés là où un suffit. Ce qui
les distinguait, la couleur, n'a jamais été dans le matériau : elle est dans les sommets, et
c'est tout l'intérêt du procédé.

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

**L'échelle des volumes** s'est greffée de la même façon, avec un champ `echelle: 2`.
Une sauvegarde qui ne le porte pas est écrite dans l'ancienne échelle : `remettreAEchelle`
la convertit à la lecture — kilos divisés par 4,44, capacités de contenants par 3 — de
sorte que la ferme du joueur garde exactement la **même valeur** et les mêmes proportions,
seuls les nombres changeant. Sans quoi son silo vaudrait d'un coup quatre fois et demie
plus, et sa benne serait trois fois trop grande.

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
