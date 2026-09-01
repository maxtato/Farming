# La chaîne des vignettes de produit

Un rendu sur fond magenta entre, une vignette de menu sort : **78 × 78 pixels**, fond
transparent, palette de 64 couleurs relevée sur l'image. Le pendant des portraits, pour la
marchandise.

    python3 fabriquer.py             # fabrique, et dit le poids
    python3 fabriquer.py --planche   # controle.png : les vignettes grossies huit fois

## La table de production

```json
"ble":  {"src": "e23188c8-image.png"},
"orge": {"src": "6c61e32b-image.png"}
```

La clé est celle de `PRODUITS` dans `index.html` — ou celle d'`ESPECES` pour une bête, et
les deux jeux de clés ne se recoupent nulle part. Une table explicite, et non un dossier
balayé : l'orge et l'avoine sont deux gerbes jaunes, et leurs noms de fichier sont des
empreintes. Le fichier sorti s'appelle `produits/<clé>.png`, à côté d'`index.html`.

**Ajouter une vignette, c'est deux lignes.** Une entrée ici, et la clé dans `VIGNETTES`
côté jeu. Tant que la seconde manque, la ligne de menu garde son filet de couleur ; tant que
la première manque, il n'y a pas de fichier. Le banc `vignettes` compare les deux listes
dans les deux sens et signale l'oubli.

## Ce que fait la chaîne

1. **Détourage.** Le fond magenta part, le sujet reste, et les poches de fond *enfermées*
   entre deux tiges partent aussi — on n'inonde pas depuis le bord, contrairement aux
   portraits : le magenta ne se trouve nulle part dans le sujet.

2. **Alpha.** Il se lit sur `min(R,B) − G`, qui est **linéaire dans le mélange** : le fond
   est à +244, un blé à −134, et un pixel à moitié l'un et l'autre tombe pile au milieu. La
   distance au fond, elle, ne l'est pas — elle vaut `a × max|C − fond|`, où le second
   facteur dépend de la couleur du sujet, et c'est ce qui faisait sortir les barbes de
   l'orge en rose. Le calcul ne se fait que dans une frange de huit pixels autour du fond :
   au-delà c'est du sujet plein, et la ficelle brune d'une gerbe s'y serait retrouvée à demi
   transparente.

3. **Démêlage.** Un pixel de frange vaut `a·C + (1−a)·fond` ; on rend `C`, sans quoi la
   silhouette garde un liseré magenta une fois posée sur le papier du menu.

4. **Cadrage.** Recadrage sur le sujet, mise à l'échelle par le **plus grand côté** — les
   récoltes sont toutes debout, un fromage ou une vache seront couchés —, deux pixels de
   marge, centrage dans un carré.

5. **Réduction et palette.** La réduction se fait sur la couleur *prémultipliée*, sinon la
   moyenne d'un pixel de bord mélange le sujet au vide et la silhouette s'éclaircit sur tout
   son tour. Puis 64 couleurs relevées sur l'image : mesuré, le passage de RGBA à la palette
   ne se voit pas à 26 pixels CSS et divise le poids par trois et demi.

## Les tailles

| ce que c'est | valeur | pourquoi |
|---|---|---|
| `BOITE` | 26 px CSS | la hauteur exacte du filet de couleur que la vignette remplace : aucune ligne de menu ne bouge |
| `PX_JEU` | 1/3 | la règle de la maison, celle des portraits |
| `COTE` | 78 px | `BOITE / PX_JEU` — un pixel d'art sur un point d'écran de téléphone |
| `MARGE` | 2 px d'art | le sujet ne touche jamais le bord de la boîte |
| `COULEURS` | 64 | le poids divisé par trois et demi, sans écart visible |

## Où vivent les images

`produits/`, à côté d'`index.html`, ne contient que ce que le jeu charge — cinq récoltes,
8,9 Ko. Les sources sont les rendus envoyés par le joueur, dans le dossier des pièces
jointes de la session : `fabriquer.py` les lit là, comme la chaîne des portraits.
