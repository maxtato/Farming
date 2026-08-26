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
| **Changer d'engin** | bouton en bas, ou les touches 1 à 4 |
| **Atteler / dételer** | bouton ATTELER, à portée d'un outil posé au sol |
| **Vendanger** | l'**enjambeuse**, achetée au garage : elle seule passe au-dessus d'un rang |
| **Changer d'engin** | le bouton au nom de l'engin, en bas : la liste du parc s'ouvre |
| **Automatiser** | bouton **PLAN** : la carte en grand, on compose une file de tâches |
| **Acheter, améliorer** | au **garage**, sur la rocade ouest, et nulle part ailleurs |

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
| **Silo, atelier de la ferme, pâtures** | décharger **et** remplir : c'est chez toi |
| **Usines et points de vente du village** | décharger seulement — ils paient, ils gardent |
| **Garage, comptoir agricole** | ni l'un ni l'autre : un bouton, pas un transfert |

Une **jauge flottante** montre le remplissage au-dessus de l'engin pendant le transfert,
au-dessus du silo, au-dessus de l'atelier, et au-dessus de chaque parcelle qui pousse.
Elle ne se montre que dans les soixante mètres : de plus loin, la vallée reste un
paysage.

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

## L'atelier de la ferme

Le moulin du bord de route a fermé : on moud son propre blé, dans sa propre cour. À
l'est du garage, les deux cases de la rangée sud ne font plus qu'une seule dalle de
bitume — le chemin de sable qui les coupait a été déposé. Le silo y a déménagé, et
l'atelier s'y installe à côté.

On y verse la matière à la benne, elle ressort transformée. Cinq paliers, achetés sur
place, et chacun se voit sur le bâtiment :

| | module | débloque | ce qu'on voit |
|---|---|---|---|
| **1** | Moulin | blé → farine | la halle, sa trémie, son quai |
| **2** | Broyeur | maïs → aliment | deuxième trémie, mélangeur, hall latéral |
| **3** | Pressoir | colza → huile de colza | deux cuves, passerelle, cheminée, bidons |
| **4** | Mélangeur | maïs + orge + avoine → aliment premium | appentis, conteneur, palettes en nombre |
| **5** | Cave | raisin → vin | étage technique, auvent de quai, aire rangée |

L'atelier n'accepte que ce que sa recette du moment réclame : réglé sur le moulin, il
refuse le raisin. Le bouton sur l'anneau du quai sert à monter d'un palier, puis à
passer d'un module à l'autre. Les paliers 4 et 5 augmentent aussi la capacité et le
débit.

L'aliment ne se vend pas, il se donne aux bêtes. Tout le reste part sur la route.

## Le gazole

Il n'y a pas de pompe publique. Le gazole s'achète en gros à la coopérative, livré dans
la cuve de la ferme, et c'est là que se font tous les pleins. Un engin à sec n'est pas
immobilisé : il se traîne au ralenti jusqu'à la cuve.

## Le plan de travail

Le bouton **PLAN** ouvre la carte en grand — la seule vue d'ensemble du jeu. On y
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
                   +-> atelier -+-> farine          -> boulangerie / marché
                   |            |-> huile de colza  -> restaurant / marché
                   |            |-> aliment (+ premium) -> les mangeoires
                   |            \-> vin              -> caviste, meilleur prix
                   |
                   +-> usines du bord de route : on verse, elles PAIENT
                   |     orge   -> brasserie      -> bière
                   |     avoine -> usine d'avoine -> lait d'avoine
                   |     blé/maïs/avoine -> usine de céréales -> céréales
                   |     colza / olives  -> huilerie -> huiles
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

   et au bout : marché du village (petites quantités, bon prix)
                supermarché (tout, 14 % moins cher)
                restaurant (surpaie le transformé, 10 % de plus)
```

La vigne et l'olivier court-circuitent le silo : du champ à la cave, au pressoir ou à
l'étal. Vingt parcelles à racheter une à une, un matériel à améliorer, des contrats à
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
- **On ne charge que chez soi.** Silo, atelier de la ferme, pâtures : les deux sens. Le
  village achète, il ne rend rien. Faire des allers-retours pour récupérer chez une
  usine ce qu'on venait de lui vendre, c'était trois arrêts pour une seule récolte.
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
