# La chaîne des portraits

Une planche de personnage entre, un portrait de jeu sort : **288 × 360 ou 576 × 720 pixels
selon la fenêtre qui le montre**, **palette de 105 couleurs en 13 gammes, partagée par tout
le casting**, fond transparent, buste coupé sur un arrondi légèrement octogonal. Cinq
étapes, et une planche de contrôle après chacune — c'est la planche qui décide, pas le code.

    node    poses.js ../../index.html   # où le jeu pose ses images, et à quelle taille
    python3 fabriquer.py --palette    # (re)bat la palette du casting entier
    python3 aligner.py                # met les trois humeurs de chacun à la même échelle
    python3 aligner.py --verifier     # mesure l'écart d'échelle, sans rien corriger
    python3 fabriquer.py              # fabrique les fiches du jeu, et dit leur poids
    python3 fabriquer.py --planche    # la planche de contrôle, pour juger le cadrage
    python3 planche.py                # verifier.html — la planche à ouvrir dans un navigateur
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
charge : quarante-et-une fiches, quinze commerces, 276 Ko. Les planches normalisées dont on
ne connaît pas encore le métier attendent dans `outils/portraits/attente/`, qui est
aujourd'hui **vide** — le dernier pensionnaire, le roux à la veste blanche, était le
boulanger. Le mécanisme reste : une entrée dont le champ `site` est vide part en attente au
lieu de partir dans le jeu, et garde son groupement, son cadrage et ses réglages jusqu'à ce
qu'on apprenne son commerce. Il n'y a alors qu'un mot à écrire.

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

## Les trois humeurs d'un personnage à la même échelle

Le joueur, planche annotée à l'appui : « pour les personnages avec plusieurs images,
assure-toi que les proportions soient identiques sur les 3 images. » Le défaut était
**structurel** : `cadrerAncre` mesure chaque planche **isolément**. Les yeux, la boîte de
visage, le profil des largeurs — trois estimateurs qui se trompent chacun de quelques pour
cent, et rien dans la chaîne ne comparait la planche du pouce levé à celle du refus. Deux
demi-erreurs de sens contraire font dix pour cent, et dix pour cent sur une tête se voient
au premier coup d'œil quand les deux images se succèdent à l'écran.

**On ne mesure pas une taille, on mesure un rapport.** Aucun estimateur ne donne la taille
absolue assez juste ; un rapport, si — les deux planches montrent la même tête, la même
coiffure, le même couvre-chef, dessinés par la même main. `calage.py` cherche
l'agrandissement et le décalage qui font coïncider l'une sur l'autre, par corrélation
croisée normalisée, et rend un nombre. `aligner.py` décide quoi en faire et l'écrit dans
`commerces.json` comme n'importe quel autre réglage à la main.

Mesuré **sur les fichiers livrés**, par `controle.py` :

| écart d'échelle entre humeurs | avant | après |
|---|---|---|
| moyenne | 11,4 % | **1,0 %** |
| pire cas | 19,9 % (Supermarché) | **1,8 %** (le chef) |
| personnages que la mesure ne conclut pas | — | 1 (la Laiterie) |

Cinq choses ont dû être corrigées avant que la mesure soit fiable, et chacune se voyait sur
un chiffre :

1. **On ne regarde que la bande de la tête.** Les bras changent d'une humeur à l'autre — un
   pouce levé, une paume tendue, une bouteille — et un recalage qui les prend en compte va
   chercher un compromis entre deux poses différentes.
2. **La bande est pondérée vers son milieu.** Un pouce monte parfois jusqu'au menton et
   entre par le côté. Sur la Laiterie cela suffisait à faire mentir une des trois paires. Un
   cosinus surélevé qui vaut 1 au milieu et 0,15 aux bords réduit les intrus au bruit sans
   les exclure franchement — ce qui ferait dépendre le résultat d'une frontière arbitraire.
3. **L'interpolation est bilinéaire.** Au plus proche voisin, deux échelles distantes d'un
   pour cent rendent souvent *exactement* la même image — les arrondis tombent au même
   endroit —, le score ne varie plus continûment et la mesure plafonne à un pour cent près.
   C'est ce qui laissait deux à trois pour cent d'écart après correction.
4. **Les trois paires, et non deux.** Mesurer bravo contre neutre puis refus contre neutre
   laisse le neutre décider seul : si c'est *lui* que la corrélation lit mal, les deux
   mesures héritent de son erreur et rien ne le signale. Les trois paires forment un
   triangle dont le produit des rapports doit valoir un ; de combien il ne se ferme pas
   **est** la mesure de la confiance qu'on peut leur faire. On résout les trois tailles aux
   moindres carrés sur les logarithmes, ce qui répartit l'erreur au lieu de la coller sur
   une planche.
5. **La cible est la médiane des trois**, pas la première ni la « mieux ancrée ». Si deux
   humeurs s'accordent et que la troisième dérape, la médiane est du bon côté ; prendre la
   première reviendrait à corriger deux planches justes pour en suivre une fausse.

**Le contrôle n'est pas la première passe de la correction**, et il a fallu s'en rendre
compte. La passe large d'`aligner` balaie de 0,80 à 1,26 par pas de deux pour cent : sur
trois personnages elle accroche un maximum secondaire, annonce dix pour cent d'écart, puis
converge en deux tours vers les réglages qui étaient *déjà* dans la table. Elle se trompe
d'abord et se rattrape ensuite — bon pour corriger, inutilisable pour constater. D'où
`--verifier`, qui dégrossit sur une plage étroite puis finit sur la grille fine. Une plage
étroite n'est pas une pétition de principe : si le rapport vrai était de 1,15, la recherche
saturerait au bord et rendrait 14 %, donc l'écart se verrait quand même.

**Et la table se réécrit comme elle est écrite.** `json.dump(indent=1)` éclate chaque ancre
sur quatre lignes : une correction de trois nombres devient un diff de cinq cents lignes, et
l'on ne voit plus ce qui a changé. Une humeur par ligne, comme à la main.

### La Laiterie, que la corrélation n'a pas su mesurer

Un cas sur treize a résisté, et il vaut d'être écrit parce que c'est le cas où l'instrument
se trompe **sans le dire**. Ses trois rapports mesurés séparément :

    neutre > bravo   s = 1,171      bravo est 0,854 × neutre
    neutre > refus   s = 0,923      refus  est 1,083 × neutre
    bravo  > refus   s = 1,156      refus  est 0,865 × bravo   ← devrait être 1,268

Produit des trois : **1,57 au lieu de 1**. Deux mesures sur trois sont fausses. La cause est
dans le dessin : son bravo rit à pleines joues — les pommettes montent, le menton descend,
les yeux se ferment — et son refus tend une paume qui monte dans la fenêtre de mesure. Le
postulat « c'est la même tête » n'y tient plus.

Quatre bandes de mesure ont été essayées ; aucune ne ferme le triangle, et les trois plus
étroites dégradent les douze autres personnages. Un estimateur de rechange — la largeur du
crâne, prise sur le tronçon opaque qui contient l'axe — donne 14 % d'écart sur le chef là où
la corrélation en donne 1,8 : sa tignasse hérissée n'est pas dessinée pareil d'une humeur à
l'autre, et le contour n'est donc pas invariant. C'est le troisième proxy de taille de ce
projet qui ment ; la leçon commence à être connue.

Ce qui a tranché, c'est **la planche des silhouettes** : les trois contours tirés l'un sur
l'autre. Le refus y avait le crâne plus haut et plus large que les deux autres, qui se
confondaient — donc c'était `bravo > refus` qui mentait, et `neutre > refus` qui disait
vrai. Un facteur 0,937 posé à la main, et les trois contours se superposent. Un chiffre
agrégé n'aurait jamais dit *laquelle* des trois était en cause.

## Des couleurs plus franches, et le barème vient du jeu

> « Est-ce que tu peux changer le ton des couleurs pour avoir des couleurs un peu plus
> punchy, dans le style de couleur du reste du jeu ? »

« Punchy » se mesure, et le jeu donne l'étalon : ses trois boutons — l'or `#E8B33A`, le
vert `#5C8C3F`, le rouge `#C2503E` — tiennent à **0,138 de chroma** en Oklab, quand les
gammes des portraits tenaient à **0,083**. Il manquait les deux tiers du chemin.

**Le gain dépend de la chroma déjà présente**, et c'est ce qui rend le réglage utilisable.
Un multiplicateur sec de 1,55 réveille bien la chemise rouge du Restaurant, mais il porte
*aussi* le teint à la même enseigne — et une peau à 1,55 vire à l'orange fluorescent. La
règle du dessinateur est l'inverse : ce qui est déjà coloré devient franc, ce qui est
naturellement sourd — la peau, la pierre, le lin — le reste. Le gain court donc de **1,10**
pour une famille presque grise à **2,00** pour une famille pleinement colorée, la bascule
se faisant à `CREF = 0,115`, la chroma d'une étoffe teinte.

**Chaque marche repasse par `enGamut`**, qui rend la plus forte chroma tenant dans le sRGB
*à sa clarté et à sa teinte*. Sans ce repli, pousser la chroma ne rend pas la couleur plus
vive : elle sort de l'écran, le bornage écrase une composante sur 255 ou sur 0, et ce qui
revient a une **teinte différente** et une clarté fausse — un jaune poussé vire au vert. La
dichotomie ne touche ni la teinte ni la clarté : c'est la définition même d'un repli dans
le gamut, et c'est pour cela que le nuancier reste rangé en gammes après coup.

**Et l'on s'arrête là où la couleur cesse de payer.** Mesuré sur le casting entier : gain
maximal 1,70 → chroma moyenne 0,099 ; 2,00 → 0,105 ; 2,30 → 0,108. Passé 2,00, le gamut
absorbe la hausse — quinze pour cent de gain en plus rendent trois millièmes de chroma. Le
réglage se pose donc au genou de la courbe, pas au-delà.

Les neutres suivent, à `× 3,2` : le jeu n'a pas un seul gris pur — son papier est crème
(`#CFC3A4`, chroma 0,044) et son voile tire au bleu. Des neutres à 0,005 de chroma à côté
de gammes à 0,128 se lisent comme du carton photocopié.

## Pixels plus fins, plus de nuances — et la leçon du chantier

> « Fais aussi des pixels plus fins. Et fais plus de nuances de couleurs. »

**384 × 480**, choisi comme le seul palier qui se divise exactement par les trois tailles
d'affichage du jeu — 2 × 192, 4 × 96, 6 × 64. Ce palier a été remplacé depuis ; voir
*La grille commune* plus bas.

**105 couleurs en 13 gammes**, contre 67 en 11 : douze familles de teinte au lieu de dix (le
rouge et l'orange n'avaient qu'une frontière pour eux deux) et huit marches de clarté au
lieu de six, ce qui donne trois valeurs à une joue là où elle en avait deux.

**Et l'on ne colle jamais à la frontière du gamut.** Avec douze familles plus serrées, la
chroma mesurée de chacune monte, le gain la porte au-delà du possible, et `enGamut` rendait
alors *exactement* la frontière — qui, aux clartés basses, est l'encre pure. Toutes les
marches sombres se retrouvaient plaquées au même endroit : `#06006C`, `#4C0007`, `#480026`.
Des primaires, pas des ombres. On plafonne donc à **85 %** de ce que la clarté autorise, et
les mêmes marches deviennent `#060E60`, `#470A0D`, `#410925` : il reste du gris dedans.

### La leçon : la résolution de la fiche n'est pas celle de la détection

C'est l'erreur qui a coûté le plus cher de tout le chantier. Pour nourrir un cadre de
1 152 px, j'ai fait passer `charger` de 900 à 1 500 — et **les détecteurs de visage n'ont
plus mordu au même endroit**. Écart inter-oculaire mesuré autrement, étages d'ancrage qui
basculent (l'usine céréales passe de `yeux` à `visage`), et donc tout le cadrage absolu du
casting qui dérive : des têtes qui remplissent le cadre, des bustes coupés aux épaules.

Le pire est ce qui a suivi : l'aligneur ne sait faire que de l'accord **relatif** entre les
trois humeurs d'un personnage — il n'a aucune idée de ce qu'est un bon cadrage. Il a donc
consciencieusement recalé les humeurs les unes sur les autres **sur une base fausse**, et
tout paraissait converger pendant que le résultat empirait. Il a fallu regarder la planche
entière pour le voir.

La détection se fait maintenant **toujours à 900 px**, la taille à laquelle les seize
réglages à la main et les trois étages d'ancrage ont été étalonnés ; l'ancre est ensuite
remise à l'échelle de l'image de travail. Les ancres écrites à la main dans la table sont
dans ces mêmes coordonnées et suivent le même facteur. Les deux résolutions n'ont aucune
raison d'être la même : l'une veut du détail, l'autre veut un étalon stable.

**Un garde-fou en plus.** La correction d'échelle est multiplicative et itérée : une mesure
fausse ne rate pas son coup, elle se *compose*. Sur le Marché, cinq tours ont porté le refus
à 2,89 fois sa taille. L'aligneur retient désormais l'état de moindre écart et y revient à
la fin : au pire il ne change rien, jamais il n'aggrave.

**Et le détourage se garde sur le disque.** Il ne dépend d'aucun réglage — seulement de la
planche et de la taille de chargement. À 1 500 px, l'aligneur qui recadre chaque planche une
dizaine de fois dépassait les dix minutes avant d'avoir rien mesuré.

## La planche de vérification

    python3 planche.py     # -> verifier.html, à ouvrir dans un navigateur

Une planche PNG ne suffit pas pour juger du pixel art : il faut pouvoir la voir **à la
taille où le jeu l'affiche**, et aussi au point près pour compter les pixels. Trois partis
pris : les images sont **dans le fichier** en base 64 (la page s'ouvre depuis n'importe où
et se regarde sur un téléphone) ; les fonds sont **ceux du jeu** (un portrait détouré jugé
sur du blanc ment) ; les tailles sont **celles du jeu et aucune autre**. Le bouton ne règle
qu'un multiplicateur, parce que les trois humeurs n'ont plus la même taille de fichier : ×1
pose chaque humeur dans sa vraie boîte (96 pour le neutre, 192 pour le pouce levé), ×3 la
pose au pixel d'art près — et c'est aussi ce que voit un téléphone à trois points par
pixel CSS.

## La grille commune

> « Ce n'est PAS une conversion image par image, c'est une grille commune à tout l'écran. »

**Une seule constante : `PX_JEU` = 1/3**, la taille d'un **pixel d'art** en pixels CSS. Une
planche ne se choisit plus, elle se calcule : la boîte où le jeu pose l'image, divisée par
`PX_JEU`. L'écran de gain pose 192 px de large → 576 × 720. La fenêtre de contrat pose 96 →
288 × 360. C'est le seul montage où un pixel d'art mesure la même chose partout sur l'écran ;
à taille de fichier unique, la vignette de contrat aurait un grain deux fois plus fin que
l'écran de gain, et ça se voit en passant de l'un à l'autre.

### Les boîtes sont mesurées, pas devinées

    PORTRAITS_BANCS=<dossier avec node_modules> node poses.js ../../index.html

`poses.js` pilote une session complète — le contrat, l'écran de gain et le refus de chacun
des quinze commerces, puis les guichets et leurs onglets — et relève la boîte de chaque
`<img>` **après la fin des animations à nombre de tours fini**. Deux pièges y sont tombés :

- La première version lisait `getBoundingClientRect`, donc la boîte **multipliée par la
  matrice d'entrée** de la fenêtre, et rapportait *172 × 212* pour un visage de 192 × 240.
  On aurait taillé quarante et une planches sur ce chiffre. On lit `offsetWidth`.
- Elle attendait `Promise.all(document.getAnimations())` — les animations **en boucle** du
  jeu (clignotants, respiration des appels) ne finissent jamais, et la mesure ne rendait pas
  la main. On ne filtre que celles à nombre de tours fini, avec une demi-seconde de garde.
- Elle laissait **sept planches jamais posées** (les refus des commerces sans liste
  `achete`) et croyait avoir tout vu. La couverture fait partie de la mesure : 41 planches
  livrées, 43 poses relevées.

Le second instrument, `drawImage` sur les contextes 2D avec la matrice courante appliquée,
rend **zéro source** : le jeu ne pose aucune image par cette voie — les portraits sont des
`<img>` du document et le monde est en WebGL. Il reste en place pour le jour où une planche
de tuiles arrivera.

### Pourquoi un tiers

Le jeu vise le téléphone couché, et un téléphone moderne compte trois points d'écran par
pixel CSS : à 1/3, un pixel d'art y tombe sur un point, au point près. À deux points la
réduction vaut 1,5 — lisse, sans crénelage ; à un seul point elle vaut 3, une moyenne de
bloc exacte. Le palier précédent (384) était bâti pour deux points par pixel CSS et se
faisait *agrandir* de moitié sur un téléphone à trois.

**Et la source suit, c'est mesuré aussi.** Le cadre de chaque planche représente de 737 à
1 501 pixels de la photo d'origine, 1 025 en médiane : à 576 pixels d'art, la plus pauvre
des sources en fournit encore **1,28 par pixel d'art** et la médiane 1,78. Aucune fiche
n'est inventée. Le cadre de travail, lui, fait trois fois la grille — c'est la marge de
lissage exigée avant conversion, et elle est du double au moins.

**Un seul cadre pour deux tailles.** 1 728 se divise par 3 et par 6 : les deux planches
sortent de la *même* moyenne d'aire sur le *même* cadrage. 576 vaut donc exactement deux
fois 288, et le contrôle d'alignement des humeurs continue de tenir au pixel près — il
remonte simplement le neutre à 576 au plus proche voisin avant de comparer.

**Chaque fiche pèse autant dans la palette**, et il a fallu l'écrire : une planche de 576
porte quatre fois plus de pixels qu'une de 288, et sans correction les vingt-six pouces
levés et refus décideraient la palette à la place des quinze visages neutres. Le pas
d'échantillonnage suit la surface.

### Le second jeu de fiches : une palette par image

    python3 fabriquer.py --14        # -> portraits14/, quatorze couleurs relevées par fiche

Le jeu montre `portraits/` ou `portraits14/` selon le réglage **Visages**. Les deux sont sur
**exactement la même grille** — 288 × 360 et 576 × 720 —, si bien que basculer ne déplace pas un
pixel : seule la couleur change.

**La palette est mesurée, pas choisie.** K-moyennes en Oklab, **déterministe de bout en bout** —
aucun tirage au sort : deux fabrications de suite rendent les mêmes octets. Le premier centre est
la couleur la plus fréquente, chacun des suivants le point le plus loin de ce qui est déjà pris,
pondéré par la fréquence pour qu'un pixel isolé ne fonde pas une famille à lui tout seul.

**Fusion sous 22 unités RVB, jamais un coloré avec un neutre.** Deux gris à dix-huit unités l'un
de l'autre sont le même gris ; un gris et un bleu-gris à dix-huit unités sont deux décisions
différentes, et les fondre fait virer une chemise blanche au bleu sur toute sa surface. Neutre =
écart max−min entre canaux sous 18.

**Trois places réservées** aux couleurs qui pèsent ≥ 0,08 % des pixels et dont le remplaçant
serait à plus de 88 unités : le vert d'une bouteille, l'or d'un bouton — ce qu'on regarde en
premier et que la moyenne noie.

**Le trait gagne son bloc.** `reduire(..., encre=1.0)` tire la moyenne d'aire vers le pixel le
plus sombre du bloc, d'autant plus fort que l'écart dépasse 34 niveaux. Sans ça un cordon de
tablier large d'un pixel source ressort à un neuvième de sa force et disparaît à l'accrochage —
et avec quatorze couleurs il ne se rattrape plus. Sur une étoffe unie l'écart est nul et rien ne
bouge. La *couleur* du plus sombre est reprise, pas seulement sa noirceur : un trait brun reste
brun.

**Et il a fallu retrouver les gammes.** `cerner` fait descendre le liseré d'une marche dans sa
propre gamme, `unifier` demande quelle famille domine autour d'un pixel : les deux veulent des
groupes de teinte. La palette partagée les reçoit de sa construction ; une palette relevée arrive
en vrac. `gammesImage` les regroupe par angle de teinte en Oklab — distance **circulaire**, sans
quoi deux couleurs à cheval sur π se croiraient à six radians l'une de l'autre — et met tous les
neutres ensemble, quel que soit leur angle : sur un gris, l'angle tourne au hasard d'une unité de
bruit.

**41 fiches, 853 Ko, 12,5 couleurs par fiche en moyenne, 14 au plus, 0,1 % d'orphelins.**

### Le seul écart, et il est assumé

Le comptoir et le garage montrent leur visage **neutre à deux tailles** : 96 dans la fenêtre
de contrat, 64 au bandeau de leur guichet. Un fichier ne peut pas faire à la fois 288 et 192
de large. La planche suit la boîte la plus fréquente — quinze commerces contre deux — et le
guichet affiche donc à 64/288, soit **0,222 px CSS par pixel d'art au lieu de 0,333**. Ça ne
se voit pas, parce que le rendu est `auto` : une réduction lisse de 4,5 est une moyenne
pondérée, pas un pixel sur deux jeté ; le demi-pixel ne mordrait que sous `pixelated`.

Le fermer demanderait de porter `#fenface` à 96 × 120. Mesuré sur un téléphone couché de
740 × 360 : le bandeau de titre passerait de **80 à 115 px** et le rayon perdrait 35 px sur
les 192 dont il dispose — une ligne d'article. Ça ne valait pas deux fichiers sur quarante
et un. **41 poses sur 43 tombent exactement sur la grille.**
