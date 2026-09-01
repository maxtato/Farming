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

**Une planche peut servir deux clés**, et c'est `VIGNETTES` côté jeu qui le dit — elle
associe une clé à un *nom de planche*, pas un oui. Deux façons d'en arriver là, et ce ne sont
pas les mêmes : `mouton` et `alimentPlus` visent la planche d'une **autre clé** — le mouton
et la brebis sont le même animal, l'aliment premium tient dans le même sac —, tandis que
`ruche` vise une planche qui ne porte le nom d'**aucune** clé, parce qu'elle dessine une
abeille. Vingt clés, dix-huit planches.

**Ajouter une vignette, c'est deux lignes.** Une entrée ici, et la clé dans `VIGNETTES`
côté jeu. Tant que la seconde manque, la ligne de menu garde son filet de couleur ; tant que
la première manque, il n'y a pas de fichier. Le banc `vignettes` compare les deux listes
dans les deux sens et signale l'oubli.

## Ce que fait la chaîne

0. **Quel fond ?** Quatorze planches sur quinze sont sur magenta ; l'abeille est sur
   **blanc**, et sur un fond blanc la teinte ne dit plus rien — elle vaut zéro pour le fond
   comme pour un flanc de vache. Les deux cas se distinguent sur le fond *lui-même*, une
   fois pour toutes, et chacun a sa règle. Sur blanc, l'alpha se lit **partout** et non dans
   une frange : la frange repose sur une garantie que seule une teinte donne, et les ailes
   de l'abeille sont peintes translucides — les rendre opaques serait aussi faux que les
   effacer.

1. **Détourage.** Le fond magenta part — **son ombre portée avec lui** —, le sujet reste,
   et les poches de fond *enfermées* entre deux tiges partent aussi : on n'inonde pas depuis
   le bord, contrairement aux portraits, car le magenta ne se trouve nulle part dans le
   sujet. La classification se fait sur la teinte **divisée par la clarté**, ce qui met le
   fond plein et son ombre à la même valeur (0,73 à 0,97) quand le sujet reste sous 0,55 —
   mesuré : pas un pixel de sujet plein ne l'atteint sur les dix sources. Un plancher de
   clarté l'accompagne, sans quoi un noir presque pur (`3, 0, 4`) passerait pour du magenta.

2. **Alpha.** Il se lit sur `min(R,B) − G` *non divisé*, qui est **linéaire dans le
   mélange** : le fond est à +244, un blé à −134, et un pixel à moitié l'un et l'autre tombe
   pile au milieu. La distance au fond, elle, ne l'est pas — elle vaut `a × max|C − fond|`,
   où le second facteur dépend de la couleur du sujet, et c'est ce qui faisait sortir les
   barbes de l'orge en rose. Le calcul ne se fait que dans une frange de huit pixels autour
   du fond : au-delà c'est du sujet plein, et la ficelle brune d'une gerbe s'y serait
   retrouvée à demi transparente.

2 bis. **Ce qui touche le bord retourne au fond.** La planche de la vache porte au bord
   droit une colonne de neuf pixels d'un magenta délavé — un bord de capture — et la vache
   se retrouvait réduite et décentrée pour la loger. La règle a d'abord été une **aire**, et
   c'était faux : la flouée posée à côté du sac de farine pèse 0,36 % du sac, la colonne de
   la vache 1,51 %. Le débris est quatre fois plus gros que le morceau. Ce qui les sépare,
   mesuré sur les vingt-six sources : la colonne de la vache est la *seule* tache de sujet
   qui touche le bord, et aucun sujet n'y touche — pas même le plus gros. Plus de seuil ;
   une seule garde, on ne retire jamais la plus grosse tache.

2 ter. **Le fond vu au travers d'un verre.** Un bidon vide laisse voir le magenta, teinté
   et éclairci par la paroi — 0,44 de teinte au lieu de 0,95 —, et aucun seuil de teinte ne
   le sépare d'une olive noire à 0,42. Il faut trois mesures ensemble : teinte ≥ 0,30,
   **équilibre** `|R−B| / clarté` ≤ 0,18 (le fond a R ≈ B ; une olive noire est à 0,28, un
   fond de bouteille grenat à 0,60) et **clarté** ≥ 175 (le verre du vin est à 185 au plus
   sombre, le reflet de sa bouteille à 162 au plus clair). On ne la cherche qu'au cœur du
   sujet : au bord, un blanc à demi mélangé de fond a la même signature, et c'est la frange
   qui s'en occupe.

3. **Démêlage.** Un pixel de frange vaut `a·C + (1−a)·fond` ; on rend `C`, sans quoi la
   silhouette garde un liseré magenta une fois posée sur le papier du menu. Le `fond` en
   question est **local** — une moyenne gaussienne des pixels de fond voisins, pondérée par
   eux seuls : sous une ombre portée, le fond est le même magenta en plus sombre, et le
   démêler contre le magenta plein retirerait plus de fond qu'il n'y en a.

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
| `SEUIL_TEINTE` | 0,55 | entre le fond ombré (0,55 au pire) et le sujet le plus magenta (0,19) |
| `LUM_MIN` | 40 | en dessous, un pixel n'a pas de teinte, il a du bruit |
| `TOL_NEUTRE` | 6 | fond blanc : en dessous de cet écart, c'est le fond |
| `PLEIN_NEUTRE` | 60 | fond blanc : au-delà, c'est opaque — entre les deux, une aile |
| `SEUIL_VERRE` | 0,30 | teinte : en dessous c'est de la matière, pas du fond atténué |
| `EQ_VERRE` | 0,18 | `\|R−B\| / clarté` : le fond a R ≈ B, une olive noire non (0,28) |
| `LUM_VERRE` | 175 | le verre du vin est à 185, le reflet de sa bouteille à 162 |

## Où vivent les images

`produits/`, à côté d'`index.html`, ne contient que ce que le jeu charge — tout ce qui est
brut, cinq animaux et huit transformations : 45,8 Ko pour vingt-six planches, la plus lourde
à 2,3 Ko. Les sources sont les rendus envoyés par le joueur, dans le dossier des pièces
jointes de la session : `fabriquer.py` les lit là, comme la chaîne des portraits.
