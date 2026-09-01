# La chaîne des portraits

Une planche de personnage entre, un portrait de jeu sort : 192 × 240 pixels, **palette de
67 couleurs partagée par tout le casting**, fond transparent, buste coupé sur un arrondi
légèrement octogonal. Cinq étapes, et une planche de contrôle après chacune — c'est la
planche qui décide, pas le code.

    python3 fabriquer.py --palette    # (re)bat la palette du casting entier
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

3. **Coupe.** Le buste se termine sur une ligne brisée de cinq cordes, posée aux mêmes
   fractions du cadre pour tous : c'est elle qui donne aux fiches leur air de famille.

   Première version : cinq points qui montaient et redescendaient tour à tour. C'était une
   denture, et la raison en est géométrique — une ligne brisée qui alterne les deux sens
   *est* une scie, quelle que soit la longueur des dents. Ce qui fait la coupe de l'image
   de référence, c'est qu'elle est **convexe de bout en bout** : elle descend, elle court à
   plat, elle remonte, et pas une fois elle ne rebrousse. Deux biseaux courts aux angles,
   un fond presque plat au milieu — le bas d'un octogone dont on aurait adouci les angles.
   Ni le fond horizontal ni les deux biseaux égaux : une symétrie parfaite se lirait comme
   un gabarit. `coupeConvexe()` vérifie la propriété, et c'est un contrôle, pas un
   commentaire.

4. **Pixels — et c'est là qu'était le raccourci.** L'étape tenait en deux lignes :
   `resize(LANCZOS)` puis `quantize(32)`. Cela rend une **image réduite**, pas un pixel
   art, et cela se **mesure** : sur `restaurant-neutre`, 15,9 % des pixels livrés n'avaient
   aucun de leurs quatre voisins de leur propre couleur. Un pixel isolé est la signature
   d'un rééchantillonnage — personne n'en pose un seul à la main. `pixels.py` refait
   l'étape pour de bon :

   | | avant | après |
   |---|---|---|
   | pixels orphelins | 15,9 % | **0,2 %** en moyenne, 0,4 % au pire |
   | palette | 32 couleurs trouvées **dans chaque image** | 67 rangées en **11 gammes**, une pour tout le casting |
   | réduction | LANCZOS, sujet moyenné avec le fond blanc | moyenne d'aire pondérée par l'alpha, cadre = 3 × la fiche |
   | poids | 9,8 Ko en moyenne, 371 Ko | **6,7 Ko en moyenne, 253 Ko** |

   - **La palette est décidée, partagée, rangée en gammes.** Trente-deux couleurs trouvées
     par statistique *dans chaque image* laissent chaque facette du rendu low-poly garder
     sa nuance : on obtient un dégradé en trente-deux marches, pas des aplats. Ici la
     palette est une pour les trente-huit fiches, bâtie en gammes — une famille de teinte,
     six marches de clarté —, et les marches sont **régularisées** : clarté à demi mesurée
     à demi régulière, saturation qui se tient dans l'ombre, teinte qui bascule vers le
     froid en bas et vers le chaud en haut. Un commerce n'en touche qu'une trentaine, et
     le reste devient de l'aplat tout seul.
   - **Aucune gamme de couleur ne descend au noir.** Avec un plancher trop bas, les dix
     familles posaient chacune une marche presque noire : dix cases de palette pour dix
     noirs indiscernables. Un dessinateur n'en peint qu'un et le partage.
   - **Les neutres ne se mesurent pas, ils se posent.** Mesurés, ils suivaient la masse —
     le tableau d'ardoise du Restaurant et les vestes sombres donnaient cinq gris presque
     noirs et un blanc, sans rien entre les deux, donc pas de quoi peindre une blouse
     blanche. Sept marches à pas constant, et le problème n'existe plus.
   - **Une étoffe, une gamme.** Accrochée pixel par pixel, une facette sur deux d'une
     chemise rouge tombait dans la famille orange et l'autre dans la rouge : un damier là
     où il n'y a qu'un tissu. Une passe regarde quelle famille domine autour de chaque
     pixel et l'y ramène si la meilleure marche de cette famille n'est pas plus loin que
     0,075 en Oklab. La marche de clarté, elle, reste libre : c'est le modelé qui doit
     survivre, pas la teinte accidentelle.
   - **Nettoyage et cerne.** On efface les pixels orphelins, on bouche les trous d'un pixel
     dans la silhouette, et l'on assombrit d'une marche **de sa propre gamme** le liseré
     extérieur — la manche bleue est cernée de bleu sombre, la joue de brun. Un noir plaqué
     tout autour ferait un autocollant.
   - **Aucun tramage**, toujours : il double le nombre de motifs et ruine la compression.

   Toute la comparaison de couleurs se fait en **Oklab**. En RVB, le bleu marine est « plus
   proche » du noir que le brun clair ne l'est du beige — le regroupement en familles,
   l'accrochage et le choix du voisin de remplacement s'y tromperaient tous les trois.

5. **Poids.** PNG indexé, **6,7 Ko en moyenne**, 253 Ko pour les trente-huit. Mesuré,
   jamais estimé.

## La palette

`palette.json` est **versionné** : c'est la décision de couleur du jeu, et refabriquer les
fiches deux fois de suite doit rendre les mêmes octets. On ne la rebat qu'en le demandant
(`--palette`), et l'on regarde le nuancier avant de la garder. Onze gammes : une de neutres
à sept marches, dix de teinte à six marches, groupées par un k-moyennes **sur l'angle de
teinte seul**, pondéré par la chroma pour qu'un beige presque gris ne tire pas le centre
d'une famille.

## Pourquoi pas les autres ancrages

- *La boîte englobante* : un personnage qui tend le bras a une boîte deux fois plus large
  qu'un autre. Cadrer dessus les met à deux échelles.
- *La « tête » mesurée par les largeurs* : une casquette plate rallonge le crâne, une
  coiffure volumineuse le double, un cadrage serré fait commencer les épaules tout de
  suite. Trois cas qui reviennent dans le lot.
- *La boîte de visage de Haar, seule* : elle mord huit fois sur dix, mais rend tantôt le
  visage, tantôt toute la tête. Elle **situe**, elle ne **mesure** pas — d'où son emploi
  comme région de recherche, et non comme échelle.
