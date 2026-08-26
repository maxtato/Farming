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

Une fois à l'arrêt, **rien ne part tout seul** : le jeu demande, toujours en deux
temps. D'abord **DÉCHARGER** ou **REMPLIR** — les deux seuls sens possibles. Puis, si ce
sens offre plusieurs possibilités, la liste de ce qui est disponible, et de quoi
revenir en arrière. Quand il n'y en a qu'une, le premier clic suffit. Le transfert en
cours reste affiché, plein, et un clic dessus l'arrête.

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

Le **restaurant** tient une commande permanente : trois produits à la fois, une grosse
prime à la clé. C'est la seule chose du jeu qui demande de composer une tournée au lieu
de remplir une benne d'un seul tenant. Elle s'affiche sur son enseigne, elle avance à
chaque livraison, et une nouvelle prend sa place dès qu'elle est honorée.

### Sept cultures

Blé, maïs, orge, avoine et colza vont au **silo**, qui tient un tas par céréale : la
trémie de la moissonneuse ne mélange pas, une culture à la fois. La **vigne** et
l'**olivier** sont pérennes — plantés une fois, ils restent sur leur parcelle et
repartent en croissance dès qu'on les a récoltés. Ils n'entrent pas au silo : du champ
au pressoir ou à l'étal, directement.

Chacune a sa plante : l'épi barbu de l'orge, la tige haute du maïs et ses feuilles
retombantes, les grappes de fleurs du colza, la panicule lâche de l'avoine, le rang
palissé de la vigne, l'olivier noueux. Un rang de vigne sur deux, un olivier toutes les
seize cellules — une plantation, pas un semis.

### Les élevages

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
- **Navette entre deux lieux** : on touche un départ, puis une arrivée. L'engin charge
  au premier, décharge au second, et recommence. Coché **EN BOUCLE**, il ne s'arrête
  plus : le silo vers l'usine de céréales, sans fin.

La file se lit en bas de la carte et se défait au doigt. En chemin entre deux étapes,
un engin en mission ne touche à rien : il traverse le silo sans s'y vider.

## La nuit

Les optiques sculptées sur chaque engin s'allument elles-mêmes : la lentille passe à
l'émissif, une bille de lumière s'épanouit autour, et un **halo se pose à plat sur le
sol** qu'elles éclairent — devant le nez pour les phares, au pied du mât pour les
lampadaires. Le halo tourne avec la machine. Un engin garé reste éteint, comme il a le
moteur coupé ; le gyrophare bat dès qu'on roule, et c'est la seule lampe sans halo :
sa flaque restait immobile sous l'engin, elle a été retirée.

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

La commande du restaurant échappe au plafond : ce qu'il a demandé, il a promis de le
prendre. C'est ce qui fait d'elle un débouché garanti, au meilleur prix, et ce qui
justifie d'aller composer une tournée pour elle.

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

**Un curseur de quantité** s'ouvre sur toute action qui se dose. Il est borné par le plus
contraignant des deux — la benne ou le tas — et la quantité choisie devient la limite du
transfert, qui s'arrête pile dessus : le dernier pas est raccourci exprès, sans quoi l'on
chargeait 204 kg là où l'on en avait demandé 200. Choisir le maximum ne pose aucune
limite. Embarquer des bêtes passe par le même curseur : on vient parfois chercher **une**
bête, pas tout l'enclos.

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

Trois plafonds, chacun posé après mesure, chacun tenu par un contrôle qui échoue si on
les retire.

**Les instances de cultures.** Chaque culture est un maillage instancié, et l'on ne
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

« Nouvelle partie », dans l'onglet Réglages, efface tout et repart d'une terre vierge.

Le même onglet règle la **netteté**. Le jeu rend en basse définition puis agrandit au
plus proche — c'est ce qui donne l'escalier de pixels des contours — mais sur un écran
très dense cela revient à remplir près de trois fois la définition de l'écran. Trois
positions : maximale (ce qui existait), élevée (plafonnée à deux fois la définition
CSS), douce (une fois et demie, le plus fluide). Sur un écran ordinaire, aucune des
trois ne change quoi que ce soit.
