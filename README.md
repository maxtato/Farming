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
| **Pilotage automatique** | bouton AUTO : la machine fait ses allers-retours seule |

Un **anneau lumineux au sol** signale un endroit où s'arrêter : livraison, plein de
gazole, chargement. Il est posé sur la dalle du commerce, juste en entrant dans le
parking : on franchit la porte de la clôture, on se gare dessus, ça se fait tout seul.
Sa couleur dit s'il y a quelque chose à y faire **avec ce qu'on transporte en ce
moment** :

| | |
|---|---|
| **Jaune, qui pulse** | en s'arrêtant ici maintenant, il se passe quelque chose |
| **Blanc, fixe** | un point de service, mais rien à y faire avec ce chargement |

La caisse est pleine de lait ? Seule la laiterie s'allume, sur toute la vallée. On la
vide, elle s'éteint et le silo s'allume à sa place. La condition ne tient pas compte de
la distance : c'est ce qui permet de choisir sa destination d'un bout à l'autre de la
carte, au lieu d'avoir à s'y rendre pour découvrir qu'on s'est trompé de tournée.

## Les élevages

Une parcelle possédée s'aménage en enclos. Quatre espèces, chacune avec son
aménagement, son produit et son acheteur :

| | donne | qui achète | à l'enclos |
|---|---|---|---|
| **Vaches** | du lait | la laiterie | tank à lait, auge, stabulation |
| **Poules** | des œufs | la boulangerie | casier à œufs, trémie, poulailler sur pilotis |
| **Cochons** | rien en continu, mais cher à la bête | la boucherie | auge, cabane, bauge de boue |
| **Moutons** | de la laine | l'usine bio | presse à balles, râtelier, bergerie |

L'espèce se choisit dans l'onglet Élevage, avant d'aménager. Toutes mangent le grain
du silo, apporté à la benne : une bête qui n'a rien à manger ne donne rien et ne
grandit pas. Un cochon n'a pas de poste de collecte, donc pas d'anneau devant : il ne
rapporte qu'en partant à la boucherie.

## L'atelier de la ferme

Le moulin du bord de route a fermé : on moud son propre blé, dans sa propre cour. À
l'est du garage, les deux cases de la rangée sud ne font plus qu'une seule dalle de
bitume — le chemin de sable qui les coupait a été déposé. Le silo y a déménagé, et
l'atelier s'y installe à côté.

On y verse le grain à la benne, il ressort transformé. Cinq paliers, achetés sur
place, et chacun se voit sur le bâtiment :

| | débloque | ce qu'on voit |
|---|---|---|
| **1 · Moulin** | blé → farine | la halle, sa trémie, son quai |
| **2 · Alimentation animale** | céréales → aliment | deuxième trémie, mélangeur, hall latéral |
| **3 · Pressoir** | colza → huile | deux cuves, passerelle, cheminée, bidons |
| **4 · Stockage** | plus de capacité et de débit | appentis, conteneur, palettes en nombre |
| **5 · Version complète** | le maximum | étage technique, auvent de quai, aire rangée |

La farine part à la boulangerie, l'huile à l'huilerie. L'aliment ne se vend pas : il se
donne aux bêtes, et il remplit la mangeoire une fois et demie mieux que le grain brut.
Le bouton sur l'anneau du quai sert à monter d'un palier, puis à choisir ce que
l'atelier transforme.

## Le gazole

Il n'y a pas de pompe publique. Le gazole s'achète en gros à la coopérative, livré dans
la cuve de la ferme, et c'est là que se font tous les pleins. Un engin à sec n'est pas
immobilisé : il se traîne au ralenti jusqu'à la cuve.

## La nuit

Les optiques sculptées sur chaque engin s'allument elles-mêmes — la lentille passe à
l'émissif — et projettent un faisceau au sol qui part du nez et s'ouvre devant. Un
engin garé reste éteint, comme il a le moteur coupé. Le gyrophare bat dès qu'on roule,
avec une flaque orange au sol la nuit.

## La boucle de jeu

```
                 comptoir agricole
                  (semences, engrais, gazole en gros)
                          |
   labour  ->  semis  ->  engrais  ->  moisson  ->  trémie
                                                      |
                            +-------------------------+
                            |
                 silo  ->  atelier  -+-> farine  -> boulangerie -> pain
                   |                 |-> huile   -> huilerie
                   |                 \-> aliment -> les mangeoires
                   |
                   +--> brasserie / huilerie / usines / coopérative
                   |         (selon la culture)
                   |
                   +--> supermarché : rachète tout produit fini, 14 % moins cher
                   |
                   +--> mangeoire -> vaches  -> lait  -> laiterie
                                  |-> poules  -> œufs  -> boulangerie
                                  |-> moutons -> laine -> usine bio
                                  \-> cochons          -> boucherie
                                       (et toute bête adulte, de n'importe
                                        quelle espèce, part à la boucherie)
```

Quatre cultures (blé, maïs, colza, avoine), chacune avec sa durée de pousse, son
rendement et son acheteur. Douze parcelles à racheter une à une, un matériel à
améliorer, des contrats à durée limitée, et une progression en onze paliers.

## Ce que contient le fichier

Le code est découpé en sections numérotées, dans l'ordre où on les lit :

| | |
|---|---|
| 1 – 3 | palette, moteur de rendu, outils de géométrie |
| 4 – 7 | sol peint par tuiles, grille de culture, peintures de travail |
| 8 – 9 | le blé en `InstancedMesh`, le décor et les props |
| 10 – 12 | machines, physique des véhicules, particules |
| 13 – 15 | monde, entrées, HUD |
| 16 – 20 | cycle jour/nuit, carburant, consommables, points de service, élevage |
| 21 – 25 | cuve de ferme, transport typé, boutons contextuels, jauges, boutique |
| 26 – 30 | son, sauvegarde, écran d'accueil, progression, boucle principale |

Quelques partis pris qui expliquent le reste :

- **Le sol est une texture peinte**, pas une géométrie. Chaque passage d'outil peint
  le quadrilatère réellement balayé entre deux images, ce qui aligne l'effet au
  centimètre sur la largeur de l'outil et évite les trous dans les virages.
- **Les outils sont indépendants des tracteurs.** Un outil dételé reste au sol ; ses
  caractéristiques de travail voyagent avec lui, pas avec l'engin qui le tire.
- **Un chargement a une nature** (grain, farine, lait, œufs, laine). Une caisse
  entamée n'accepte plus rien d'autre : c'est ce qui oblige à planifier ses tournées.
- **Un anneau ne s'allume jamais pour le seul fait qu'un panneau peut s'ouvrir.** Il
  s'allume quand quelque chose se passe dans le monde.
- **L'éclairage est presque uniforme**, avec des ombres longues mais claires. Les
  couleurs des faces doivent rendre pleines, pas modelées.

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
