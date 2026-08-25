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
gazole, chargement. On se gare dessus, ça se fait tout seul.

## La boucle de jeu

```
                 comptoir agricole
                  (semences, engrais, gazole en gros)
                          |
   labour  ->  semis  ->  engrais  ->  moisson  ->  trémie
                                                      |
                            +-------------------------+
                            |
                 silo  ->  moulin  ->  farine  ->  boulangerie  ->  pain
                   |
                   +--> brasserie / huilerie / usines (selon la culture)
                   |
                   +--> auge  ->  vaches  ->  lait      ->  laiterie
                                          \-> bête adulte -> boucherie
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
- **Un chargement a une nature** (grain, farine, lait). Une caisse entamée n'accepte
  plus rien d'autre : c'est ce qui oblige à planifier ses tournées.
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
