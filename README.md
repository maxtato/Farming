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

Une fois à l'arrêt : s'il n'y a qu'une seule chose à faire, elle se fait toute seule.
S'il y en a plusieurs — cinq tas au silo, vendre ou livrer chez un commerce, remplir
l'auge ou charger le lait — le jeu s'arrête et **demande**, en une courte colonne de
boutons. Deviner à ta place, c'est te charger de l'orge quand tu venais chercher du blé.

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
                   +-> usines du bord de route : on verse, on revient chercher
                   |     orge   -> brasserie      -> bière
                   |     avoine -> usine d'avoine -> lait d'avoine
                   |     blé/maïs/avoine -> usine de céréales -> céréales
                   |     colza / olives  -> huilerie -> huiles
                   |     lait   -> laiterie   -> beurre + yaourt
                   |     lait   -> fromagerie -> fromage
                   |     laine  -> atelier textile (vend sur place)
                   |
                   \-> mangeoire -> vaches  -> lait
                                 |-> poules  -> œufs
                                 |-> moutons -> laine
                                 \-> toute bête adulte -> boucherie -> viande

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
- **Le sol est une texture peinte**, pas une géométrie. Chaque passage d'outil peint
  le quadrilatère réellement balayé entre deux images, ce qui aligne l'effet au
  centimètre sur la largeur de l'outil et évite les trous dans les virages.
- **Les outils sont indépendants des tracteurs.** Un outil dételé reste au sol ; ses
  caractéristiques de travail voyagent avec lui, pas avec l'engin qui le tire.
- **Un chargement a une nature** — une clé de la table des produits. Une caisse
  entamée n'accepte plus rien d'autre : c'est ce qui oblige à planifier ses tournées.
- **Un transformateur, c'est toujours la même mécanique** : une trémie, un stock, une
  recette entre les deux. L'atelier de la ferme et les usines du bord de route
  partagent le même code ; seule change la liste des recettes.
- **Une recette n'a rien à déclarer** : le nom du produit suffit, puisque la table des
  produits dit déjà de quoi il est fait, ce qu'il rend et à quel palier il appartient.
- **Un anneau ne s'allume jamais pour le seul fait qu'un panneau peut s'ouvrir.** Il
  s'allume quand quelque chose se passe dans le monde.
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
