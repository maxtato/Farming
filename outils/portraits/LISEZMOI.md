# La chaîne des portraits

Une planche de personnage entre, un portrait de jeu sort : 192 × 240 pixels, palette de
32 couleurs, fond transparent, buste coupé sur une ligne brisée. Cinq étapes, et une
planche de contrôle après chacune — c'est la planche qui décide, pas le code.

    python3 fabriquer.py              # fabrique les fiches du jeu, et dit leur poids
    python3 fabriquer.py --planche    # la planche de contrôle, pour juger le cadrage
    python3 rendre.py 15_controle.png # balaie un lot NON TRIÉ, pour voir ce qu'il contient

**Deux scripts, et ils ne servent pas à la même chose.** `rendre.py` balaie un dossier
d'images pour voir ce qu'il contient — c'est ce qu'on lance quand un lot arrive et qu'on ne
sait pas encore quel personnage va à quel métier. `fabriquer.py` produit les fiches du
JEU, et il part de `commerces.json` : un commerce, trois humeurs, un fichier source par
humeur. C'est la seule façon d'être sûr qu'on ne livre pas le pouce levé d'un métier à la
place du refus d'un autre, et c'est ce qui rend le travail **reproductible** — les réglages
faits à la main sont dans le fichier, pas dans une séance de mise au point.

## La table de production

```json
"caviste": {"site": "Caviste",
  "neutre": {"src": "52aeef1c-image.jpg", "ancre": [77, 394, 170]},
  "bravo":  {"src": "04056996-image.jpg", "ancre": [83, 353, 202]},
  "refus":  {"src": "dc312b7f-image.png", "ancre": [85, 348, 195]}}
```

Trois réglages facultatifs par humeur, dans l'ordre où l'on y a recours : `ech`, `dx`, `dy`
corrigent ce que les détecteurs ont trouvé ; `ancre` — `[écart, x, y]` — impose les yeux
quand aucun détecteur ne mord. Le caviste a eu droit à la troisième sur ses trois planches :
ses lunettes rondes et sa tignasse ont tenu les deux détecteurs en échec, et le détecteur de
visage visait la bouteille de vin.

**Où vivent les images.** `portraits/`, à côté d'`index.html`, ne contient QUE ce que le jeu
charge. Les planches normalisées dont on ne connaît pas encore le métier attendent dans
`outils/portraits/attente/`.

## Ce que fait la chaîne

1. **Détourage.** Le fond part, le sujet reste, et les blancs *intérieurs* restent aussi —
   les dents d'un rire, le col d'une chemise. On inonde depuis les bords, on ne seuille
   pas. La couleur du fond se lit sur le pourtour entier et non sur les quatre coins :
   trois planches du lot ont le buste qui déborde par le bas, et leurs coins inférieurs
   sont dans la veste.

2. **Cadrage.** Toutes les planches n'ont ni la même taille ni le même cadrage. On les
   aligne sur **l'écart entre les yeux** — la seule mesure qui veuille dire la même chose
   d'un dessin à l'autre. Trois étages, du plus sûr au plus grossier :

   | étage | ce qu'il mesure | combien de planches |
   |---|---|---|
   | `yeux` | les deux yeux, cherchés dans la boîte de visage | 17 / 37 |
   | `visage` | la boîte de visage × 0,41 (rapport étalonné sur les 17 ci-dessus) | 13 / 37 |
   | `largeur` | le profil des largeurs, faute de mieux — à corriger à la main | 7 / 37 |

   Les étages 2 et 3 se corrigent dans `reglages.json`, trois nombres par planche :
   `ech` (échelle), `dx`, `dy` (centrage), ou `ancre: [écart, x, y]` pour poser les yeux
   à la main quand les détecteurs se trompent franchement.

3. **Coupe.** Le buste se termine sur une ligne brisée à quatre segments, posée aux mêmes
   fractions du cadre pour tous : c'est elle qui donne aux fiches leur air de famille.

4. **Pixels.** Réduction à 192 px de large, puis quantification en aplats. **Aucun
   tramage** : le tramage double le nombre de motifs et ruine la compression.

5. **Poids.** PNG indexé, 9,6 Ko en moyenne. Mesuré, jamais estimé.

## Pourquoi pas les autres ancrages

- *La boîte englobante* : un personnage qui tend le bras a une boîte deux fois plus large
  qu'un autre. Cadrer dessus les met à deux échelles.
- *La « tête » mesurée par les largeurs* : une casquette plate rallonge le crâne, une
  coiffure volumineuse le double, un cadrage serré fait commencer les épaules tout de
  suite. Trois cas qui reviennent dans le lot.
- *La boîte de visage de Haar, seule* : elle mord huit fois sur dix, mais rend tantôt le
  visage, tantôt toute la tête. Elle **situe**, elle ne **mesure** pas — d'où son emploi
  comme région de recherche, et non comme échelle.
