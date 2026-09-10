# Le relevé des textes

`TEXTES.md`, à la racine : tout ce que le jeu dit au joueur, et quand il le dit.

    node relever.js          # lit les tables DANS le jeu qui tourne  -> textes.json
    python3 composer.py      # + les bandeaux du source              -> ../../TEXTES.md

## Pourquoi deux étapes

**Les textes sont relevés, pas recopiés.** Les trente missions, les neuf marches du
tutoriel et les vingt leçons sont lues dans le jeu chargé par un vrai navigateur : le
document ne peut donc pas mentir sur ce qui est écrit, ni prendre du retard sur une phrase
changée. Trois marches du tutoriel disent d'ailleurs autre chose en mode libre — leur
titre et leur texte sont des fonctions — et le relevé les lit **dans les deux modes**.

**Les bandeaux volants, eux, se lisent dans le source.** Ils sont dans une centaine
d'appels de `showHint` éparpillés dans le fichier, et aucun ne se laisse interroger de
l'extérieur. `composer.py` les extrait en scannant les parenthèses : il rend le texte
littéral, remplace ce qui se calcule par `<…>`, et sort les DEUX branches d'un ternaire
plutôt que de les recoller en une phrase qui n'existe pas.

## Ce qu'il faut tenir à jour à la main

Les deux tables `QUAND_TUTO` et `QUAND_LECON` de `composer.py`, et elles seules. Une
condition JavaScript ne se lit pas : `()=> partParcelle('labour') >= PART_ETAPE` doit se
traduire en « quand 98 % de la parcelle est labourée ». Ajouter une leçon sans ajouter sa
ligne ici laisse un « — » dans le document, ce qui se voit.

## `three.min.js`

`relever.js` charge le jeu, donc three.js. Il le cherche à côté de lui, ou à l'adresse
donnée par la variable `THREE` — c'est ainsi que les bancs le lui passent sans qu'une
copie de plus entre dans le dépôt.
