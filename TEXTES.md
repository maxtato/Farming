# Tous les textes du jeu, et quand ils arrivent

*Relevé automatique : les textes sont lus DANS le jeu qui tourne, pas recopiés à la main. Les descriptions de « quand » sont, elles, rédigées d'après la condition du code.*

Quatre surfaces disent quelque chose au joueur, et elles n'ont ni le même ton ni le même poids :

| surface | ce que c'est | combien de temps |
|---|---|---|
| **Fenêtre de papier** | la « bulle » : un titre, une phrase, un visage, une ligne de suite | 5 à 6 s, ou un doigt — sauf une marche de tutoriel, qui **attend le doigt** |
| **Bandeau de mission** | en haut à gauche, la mission en cours et ce qu'elle attend | tant que la mission court |
| **Bandeau volant** | la ligne noire au milieu de l'écran, en capitales | 2 à 3 s |
| **Écran d'accueil** | le titre au lancement et l'écran de fin | jusqu'au bouton |

---

## 1. L'ouverture

**Écran d'accueil** — titre `MOISSON`, sous-titre « La partie s'enregistre toute seule : tu peux fermer et revenir. », boutons : « Commencer » · « Mode libre ».

**Première fenêtre de la campagne**, juste après le bouton *Commencer* :

> **UN HÉRITAGE**  
> *« Mon oncle m'a laissé sa terre, son tracteur et sa maison.  
> Je n'ai jamais conduit autre chose qu'une voiture. »*  
> — suite : *On commence par retourner le sol, paraît-il*

---

## 2. Le tutoriel — 9 marches

Une marche **attend le doigt** : elle ne part pas toute seule. Elle allume aussi un cercle jaune au sol et une flèche au bord de l'écran vers l'endroit à rejoindre.

### 1. PRÉPARER LA PARCELLE
> PRÉPARER LA PARCELLE — on ne sème pas sur de l’herbe, paraît-il. La charrue est au parc : il faut l’accrocher derrière le tracteur.

- **Arrive** : Dès la première seconde de la campagne, après la fenêtre « UN HÉRITAGE ».
- **Se solde** : Quand 98 % de la parcelle est labourée.
- **Où elle envoie** : champ

### 2. SEMER DU BLÉ
> SEMER DU BLÉ — la terre est ouverte. Reste à y mettre quelque chose : le semoir attend au même endroit que la charrue.

- **Arrive** : Dès que le labour est fini.
- **Se solde** : Quand 98 % de la parcelle est semée.
- **Où elle envoie** : champ

### 3. LAISSER POUSSER
> LAISSER POUSSER — et maintenant on attend. Personne ne m’avait dit que ce serait la partie la plus longue.

- **Arrive** : Dès que le semis est fini.
- **Se solde** : Quand 98 % du blé est mûr.
- **Où elle envoie** : champ

### 4. PREMIÈRE RÉCOLTE
> PREMIÈRE RÉCOLTE — le blé est mûr. La moissonneuse, c’est la grosse machine avec la barre devant. Toute la parcelle, cette fois.

- **Arrive** : Dès que le blé est mûr.
- **Se solde** : Quand 98 % de la parcelle est moissonnée ET qu'au moins 30 kg sont rentrés.
- **Où elle envoie** : champ

### 5. STOCKER LA RÉCOLTE
> STOCKER LA RÉCOLTE — la trémie est pleine, la tour est vide. Ça doit bien aller quelque part.

- **Arrive** : Dès que le champ est moissonné.
- **Se solde** : Quand 30 kg de blé sont entrés au silo.
- **Où elle envoie** : silo

### 6. RANGER LA MOISSONNEUSE
> RANGER LA MOISSONNEUSE — le champ est fait. Autant la remettre où je l’ai trouvée.

- **Arrive** : Dès que le silo a reçu la récolte.
- **Se solde** : Quand la moissonneuse est garée au parc à outils.
- **Où elle envoie** : parc

### 7. REPRENDRE LE PICK-UP
> REPRENDRE LE PICK-UP — on ne descend pas au village en moissonneuse. J’ai essayé.

- **Arrive** : Dès que la moissonneuse est rangée.
- **Se solde** : Quand on conduit le pick-up.
- **Où elle envoie** : parc

### 8. LE TÉLÉPHONE SONNE
> LE TÉLÉPHONE SONNE — déjà quelqu’un qui veut de mon blé. Je ne l’ai même pas encore vendu.

- **Arrive** : CAMPAGNE UNIQUEMENT — dès qu'on a repris le pick-up. C'est la marche qui fait sonner le téléphone chez soi.
- **Se solde** : Quand on prend la mission, au cercle vert de la ferme.
- **Où elle envoie** : ferme
- **En mode libre, elle dit autre chose** : **PRÉPARER LA LIVRAISON** — PRÉPARER LA LIVRAISON — trente kilos suffiront pour voir ce que ça vaut.

### 9. PREMIÈRE VENTE
> PREMIÈRE VENTE — la Coopérative achète le grain. C’est le moment de savoir si tout ça valait la peine.

- **Arrive** : MODE LIBRE UNIQUEMENT — dès qu'on a repris le pick-up.
- **Se solde** : À la première vente, quel que soit le commerce.
- **Où elle envoie** : Coopérative

### Et à la fin, en mode libre seulement
> **TUTORIEL TERMINÉ**  
> *« Préparer la terre, semer, attendre, moissonner, stocker, vendre.  
> Voilà. Je suis agriculteur. »*  
> — suite : *Plus aucun objectif – cultivez, élevez, transformez et vendez comme vous voulez*

---

## 3. Les leçons — 20, une seule fois chacune

Une leçon se lève **quand le geste devient possible ou nécessaire**, jamais deux fois dans la même partie. Un **MUR** est un blocage (le fermier fait la tête) ; une **porte** est une possibilité qui s'ouvre (il est surpris).

### REMPLIR LE SEMOIR  — *mur*
> REMPLIR LA CUVE — un semoir vide ne sème rien, et il m’a fallu un demi-champ pour m’en apercevoir. La cuve verte est dans la cour, ou au comptoir.

- **Arrive quand** : L'outil attelé a une cuve VIDE, et il reste de quoi la remplir à la ferme.
- **Où elle envoie** : reserve

### LA TRÉMIE EST PLEINE  — *mur*
> LA TRÉMIE EST PLEINE — elle ne ramasse plus rien. Il faut aller vider au silo, puis revenir finir : une parcelle en donne plus qu’elle n’en tient.

- **Arrive quand** : La trémie de la moissonneuse est pleine.
- **Où elle envoie** : silo

### LE PLEIN DE GAZOLE  — *mur*
> LE PLEIN — arrête-toi sur le cercle de la citerne, dans la cour. Ça coule tout seul et c’est gratuit : la seule chose gratuite de la semaine.

- **Arrive quand** : Un engin descend sous 40 % de gazole et la citerne de la cour n'est pas vide.
- **Où elle envoie** : gazole

### FAIRE SES COURSES
> LE COMPTOIR AGRICOLE — c’est là qu’on remplit les deux cuves de la cour, et la citerne à gazole

- **Arrive quand** : Une des deux cuves de la cour tombe sous 10 %, ou le gazole sous 25 %.
- **Où elle envoie** : Comptoir agricole · fenêtre comptoir / semences

### ACHETER DU MATÉRIEL
> LE GARAGE — un engin de plus, ou un outil : deux onglets, une seule fenêtre

- **Arrive quand** : On a de quoi acheter le moins cher des engins ou outils en vitrine.
- **Où elle envoie** : Garage · fenêtre achat / engins

### AMÉLIORER SON MATÉRIEL
> AMÉLIORER — au garage aussi : plus large, plus vite, plus de charge, cran par cran

- **Arrive quand** : On a de quoi payer le cran suivant d'un engin ou d'un outil déjà possédé.
- **Où elle envoie** : Garage · fenêtre amelio / engins

### UNE CULTURE DE PLUS
> UNE NOUVELLE CULTURE — le droit de la semer s’achète une fois pour toutes, au comptoir

- **Arrive quand** : Une culture est ouverte par le palier et on a de quoi l'acheter.
- **Où elle envoie** : Comptoir agricole · fenêtre comptoir / semences

### CHANGER DE CULTURE
> LE BOUTON DE CULTURE — en haut à droite : il fait défiler ce que le semoir sait semer

- **Arrive quand** : Le semoir est attelé et au moins deux cultures sont débloquées.

### ACHETER UNE PARCELLE
> UNE TERRE DE PLUS — pose-toi DESSUS, à l’arrêt, et le prix s’affiche

- **Arrive quand** : Une parcelle est à vendre et on a de quoi la payer.
- **Où elle envoie** : parcelle

### LE PLAN DE TRAVAIL
> LE PLAN — le bouton en bas à gauche ouvre la carte : désigne une parcelle, un engin, et il travaille seul

- **Arrive quand** : On possède un outil de travail et une parcelle cultivable.

### AGRANDIR LE SILO
> LE SILO SATURE — il s’agrandit par l’onglet « Agrandir » du bouton Stockage

- **Arrive quand** : Le silo dépasse 85 % et on a de quoi l'agrandir.
- **Où elle envoie** : silo · fenêtre stockage / agrandir

### ACHETER UN MÉTIER
> L’ATELIER — un métier transforme ce qu’on récolte : le moulin fait la farine, et la farine se vend le double

- **Arrive quand** : Un métier d'atelier est ouvert par le palier et on a de quoi l'acheter.
- **Où elle envoie** : atelier · fenêtre production / metiers

### LANCER UN LOT
> PRODUIRE — verse la matière à l’atelier, puis lance le lot par l’onglet « Produire »

- **Arrive quand** : L'atelier a au moins un métier, sa file est vide, et il y a de quoi lancer un lot.
- **Où elle envoie** : atelier · fenêtre production / produire

### RANGER À L’ENTREPÔT
> L’ENTREPÔT — le silo garde le grain, l’entrepôt garde ce que l’atelier a fabriqué

- **Arrive quand** : On roule avec une caisse dont le contenu se range à l'entrepôt.
- **Où elle envoie** : entrepot

### RÉGLER L’ATELIER
> LES TROIS RÉGLAGES — plus gros lots, plus vite, plusieurs à la file : l’onglet « Améliorations »

- **Arrive quand** : L'atelier a un métier et on a de quoi payer une de ses trois améliorations.
- **Où elle envoie** : atelier · fenêtre production / reglages

### MONTER UN ÉLEVAGE
> UN ENCLOS — arrête-toi sur une parcelle à toi : le bandeau propose de la clôturer

- **Arrive quand** : Aucun enclos encore monté, une espèce ouverte, une parcelle libre et l'argent.
- **Où elle envoie** : champ

### ACHETER UNE BÊTE
> UNE BÊTE — devant l’enclos, le bouton INTERAGIR ouvre tout ce qui s’y fait

- **Arrive quand** : Un enclos a de la place et on a de quoi acheter une bête.
- **Où elle envoie** : pature

### REMPLIR LA MANGEOIRE
> LA MANGEOIRE — une bête qui mange produit ; charge du grain au silo et verse-le à l’enclos

- **Arrive quand** : Un enclos habité tombe sous 35 % de mangeoire.
- **Où elle envoie** : pature

### RÉCUPÉRER LA PRODUCTION
> LE TANK EST PLEIN — reviens avec une benne vide : INTERAGIR, et la production monte à bord

- **Arrive quand** : Un enclos a de quoi être récolté (lait, laine, œufs, miel).
- **Où elle envoie** : pature

### PRENDRE UN CONTRAT
> UN CONTRAT — un commerce en propose un : sa pastille est bleue, et le bouton aussi

- **Arrive quand** : Les contrats sont ouverts et un commerce en propose un.

---

## 4. Les 30 missions de campagne

Une mission se **prend chez soi** : le téléphone sonne, on rentre à la ferme, on lit la demande. Elle se **solde** en livrant, et le commerçant répond.


### Palier 1 — Le fermier
*Le blé, la coopérative, une parcelle*

#### 1. Livrer 30 kg de blé – Coopérative
- **Chez** : Coopérative  ·  **Demande** : 30 kg de blé  ·  **Prime** : 200 €  ·  **XP** : 60

> **À la prise** — *« Bonjour, vous êtes le nouveau propriétaire de la ferme ? Bienvenue dans le village. Pour commencer, je vais vous prendre 30 kg de votre blé. »*

> **À la livraison** — *« Parfait. Voilà votre première vente. Vous pouvez revenir ici quand vous voulez, même sans contrat : je peux acheter toute votre production immédiatement. »*

> *Page suivante — **VENTE LIBRE DÉBLOQUÉE** : La Coopérative agricole achète votre production à tout moment. Les prix sont faibles, mais vous pouvez y vendre librement vos surplus.*

> *Page suivante — **CE QUE ÇA PERMET** : « Je ne suis pas celui qui paie le mieux, mais je prends ce que vous avez. Ça peut vous permettre de payer vos graines, votre carburant ou quelques améliorations sans attendre le prochain contrat. »*

> *Page suivante — **LE VILLAGE VOUS A VU** : « Maintenant que votre exploitation tourne, d’autres entreprises du village vont commencer à s’intéresser à ce que vous produisez. »*

#### 2. Livrer 80 kg de blé – Usine céréales
- **Chez** : Usine céréales  ·  **Demande** : 80 kg de blé  ·  **Prime** : 300 €  ·  **XP** : 80

> **À la prise** — *« La Coopérative m'a parlé de votre première récolte. J'aimerais tester votre blé dans notre production. Préparez-moi 80 kg. »*

> **À la livraison** — *« Très bien. La qualité est bonne. On pourra augmenter les volumes la prochaine fois. »*


### Palier 2 — Productivité
*L'épandeur : la même terre, plus vite*

#### 3. Livrer 150 kg de blé – Coopérative
- **Chez** : Coopérative  ·  **Demande** : 150 kg de blé  ·  **Prime** : 600 €  ·  **XP** : 100

> **À la prise** — *« J'ai une demande un peu plus importante cette semaine : je peux vous prendre 150 kg de blé. Et avec les volumes qui augmentent, vous devriez jeter un œil à l'épandeur – l'engrais peut vous faire gagner du temps, mais libre à vous de l'utiliser ensuite. »*

> **À la livraison** — *« Très bien. Votre ferme commence à trouver son rythme. »*

> *Préambule — **PRENDRE L'ÉPANDEUR** : L'ÉPANDEUR — il t'attend au garage du village, pour 250 €*

> *Préambule — **REMPLIR L'ÉPANDEUR** : REMPLIR L'ÉPANDEUR — la cuve blanche de la cour en est pleine : sers-toi*

#### 4. Livrer 250 kg de blé – Usine céréales
- **Chez** : Usine céréales  ·  **Demande** : 250 kg de blé  ·  **Prime** : 900 €  ·  **XP** : 120

> **À la prise** — *« Le premier lot s'est bien comporté. Cette fois, je peux utiliser 250 kg de votre blé. »*

> **À la livraison** — *« Parfait. Je sais maintenant que vous pouvez répondre à de vraies commandes. »*


### Palier 3 — Première transformation
*Le moulin, la farine, la boulangerie*

#### 5. Livrer 72 kg de farine – Boulangerie
- **Chez** : Boulangerie  ·  **Demande** : 72 kg de farine  ·  **Prime** : 1400 €  ·  **XP** : 150

> **À la prise** — *« J'ai vu passer votre blé. Plutôt que de l'acheter brut, j'aimerais travailler directement avec votre farine. Installez un moulin et préparez-moi 72 kg. »*

> **À la livraison** — *« Voilà une farine qui me convient. Votre blé vient de prendre un peu plus de valeur. »*


### Palier 4 — Le maïs et les poules
*Une deuxième parcelle, le broyeur, le poulailler*

#### 6. Livrer 180 kg de maïs – Usine céréales
- **Chez** : Usine céréales  ·  **Demande** : 180 kg de maïs  ·  **Prime** : 1800 €  ·  **XP** : 170

> **À la prise** — *« Votre exploitation s'agrandit. J'aimerais maintenant tester une autre culture. Préparez-moi 180 kg de maïs. »*

> **À la livraison** — *« Très bien. Plus vous diversifiez vos cultures, plus nous pourrons travailler ensemble. »*

#### 7. Livrer 24 œufs – Boulangerie
- **Chez** : Boulangerie  ·  **Demande** : 24 œufs  ·  **Prime** : 2500 €  ·  **XP** : 180

> **À la prise** — *« Pour la farine, nous sommes au point. Il me manque maintenant de bons œufs. Si vous installez quelques poules, je vous prends les 24 premiers. »*

> **À la livraison** — *« Parfait. Farine et œufs provenant de la même ferme, ça commence à devenir intéressant. »*


### Palier 5 — Deux chaînes à la fois
*La farine ET les œufs dans la même tournée*

#### 8. Livrer 72 kg de farine et 36 œufs – Boulangerie
- **Chez** : Boulangerie  ·  **Demande** : 72 kg de farine, 36 œufs  ·  **Prime** : 2800 €  ·  **XP** : 200

> **À la prise** — *« Cette fois, j'ai besoin des deux. Préparez-moi 72 kg de farine et 36 œufs. »*

> **À la livraison** — *« Tout est là. C'est exactement le type d'approvisionnement que je recherchais. »*


### Palier 6 — L'orge
*L'orge, la cuve de brassage, le restaurant*

#### 9. Livrer 140 L de bière – Restaurant
- **Chez** : Restaurant  ·  **Demande** : 140 L de bière  ·  **Prime** : 3200 €  ·  **XP** : 220

> **À la prise** — *« Je cherche quelqu'un qui cultiverait de l'orge dans le coin et qui se lancerait dans une bière artisanale – une vraie, brassée ici. Si vous vous y mettez, je vous en prends 140 litres sans hésiter. »*

> **À la livraison** — *« C'est exactement ce que j'espérais. Une bière du village, brassée à la ferme d'à côté : la carte peut enfin le dire. »*

#### 10. Livrer 60 L de bière et 120 kg de farine – Épicerie
- **Chez** : Épicerie  ·  **Demande** : 60 L de bière, 120 kg de farine  ·  **Prime** : 3600 €  ·  **XP** : 240

> **À la prise** — *« Le Restaurant m'a fait goûter votre bière, et on me la réclame déjà au comptoir. J'ouvre un rayon de produits de la ferme : 60 litres et 120 kg de farine pour commencer. »*

> **À la livraison** — *« Le rayon est monté. Vos produits sont les premiers qu'on voit en entrant, maintenant. »*


### Palier 7 — L'avoine
*L'avoine et son usine*

#### 11. Livrer 200 kg d’avoine – Usine avoine
- **Chez** : Usine avoine  ·  **Demande** : 200 kg d’avoine  ·  **Prime** : 4000 €  ·  **XP** : 260

> **À la prise** — *« Nous cherchons un producteur local d'avoine. Une première livraison de 200 kg nous permettra de voir si votre récolte convient à notre procédé. »*

> **À la livraison** — *« Ça nous convient. Gardez de l'avoine en production, nous en aurons probablement encore besoin. »*


### Palier 8 — Les vaches
*Le mélangeur premium, l'étable, la laiterie*

#### 12. Produire 184 kg d'aliment premium
- **Chez** : —  ·  **Demande** : alimentPlus  ·  **Prime** : 4500 €  ·  **XP** : 280

> **À la prise** — *« Vous produisez maintenant suffisamment de céréales différentes pour préparer un aliment plus complet pour vos élevages. Montez le mélangeur : 40 kg de maïs, 30 d'orge et 30 d'avoine donnent 92 kg d'aliment premium. Il en faut deux cycles. »*

> **À la livraison** — *« Votre ferme peut désormais produire son propre aliment premium. »*

#### 13. Livrer 200 L de lait – Laiterie
- **Chez** : Laiterie  ·  **Demande** : 200 L de lait  ·  **Prime** : 5500 €  ·  **XP** : 300

> **À la prise** — *« Votre exploitation semble prête pour accueillir des vaches. Installez votre élevage et gardez-moi les 200 premiers litres de lait. »*

> **À la livraison** — *« Très bon début. Si votre troupeau grandit, je pourrai prendre davantage. »*


### Palier 9 — Fromage fermier
*La fromagerie de la ferme*

#### 14. Livrer 350 L de lait – Laiterie
- **Chez** : Laiterie  ·  **Demande** : 350 L de lait  ·  **Prime** : 6000 €  ·  **XP** : 320

> **À la prise** — *« La première collecte était bonne. Cette fois, j'aurais besoin de 350 litres. À vous de choisir : davantage de vaches, ou simplement un peu plus de temps. »*

> **À la livraison** — *« Parfait. Votre production laitière commence à devenir sérieuse. »*

#### 15. Livrer 28 kg de fromage – Restaurant
- **Chez** : Restaurant  ·  **Demande** : 28 kg de fromage  ·  **Prime** : 7000 €  ·  **XP** : 340

> **À la prise** — *« Votre lait est bon, mais j'aimerais servir quelque chose qui vienne vraiment de votre ferme. Préparez-moi 28 kg de fromage. »*

> **À la livraison** — *« Très réussi. Celui-là aura sa place sur la carte. »*


### Palier 10 — Gros volumes
*Le supermarché et son rayon fermier*

#### 16. Livrer 56 kg de fromage et 48 œufs – Supermarché
- **Chez** : Supermarché  ·  **Demande** : 56 kg de fromage, 48 œufs  ·  **Prime** : 8000 €  ·  **XP** : 360

> **À la prise** — *« Nous ouvrons un petit rayon consacré aux producteurs du village. Pour le lancement, il nous faudrait 56 kg de fromage et 48 œufs. »*

> **À la livraison** — *« Parfait. Le rayon local peut ouvrir. »*


### Palier 11 — La bergerie
*Les moutons et leurs brebis : la laine et le lait*

#### 17. Livrer 40 kg de laine – Atelier textile
- **Chez** : Atelier textile  ·  **Demande** : 40 kg de laine  ·  **Prime** : 8500 €  ·  **XP** : 380

> **À la prise** — *« Je cherche de la laine produite dans le secteur pour une petite série. Si vous installez une bergerie, je vous prends les premiers 40 kg. »*

> **À la livraison** — *« Cette laine me convient très bien. On pourra travailler sur des volumes plus importants. »*

#### 18. Livrer 160 L de lait de brebis – Fromagerie
- **Chez** : Fromagerie  ·  **Demande** : 160 L de lait de brebis  ·  **Prime** : 9000 €  ·  **XP** : 400

> **À la prise** — *« Vos brebis peuvent nous intéresser pour autre chose que leur laine. J'aimerais essayer 160 litres de leur lait. »*

> **À la livraison** — *« Très intéressant. Ce lait a vraiment son propre caractère. »*


### Palier 12 — Fromage de brebis
*Le produit le mieux payé de la ferme*

#### 19. Livrer 40 kg de fromage de brebis – Restaurant
- **Chez** : Restaurant  ·  **Demande** : 40 kg de fromage de brebis  ·  **Prime** : 9500 €  ·  **XP** : 420

> **À la prise** — *« J'ai goûté ce qui a été fait avec votre lait de brebis. Maintenant, j'aimerais servir votre propre fromage. Préparez-moi 40 kg. »*

> **À la livraison** — *« Excellent. Il se distingue clairement de votre fromage de vache. »*


### Palier 13 — L'apiculture
*Le rucher, le miel, le marché du village*

#### 20. Livrer 100 kg de laine – Atelier textile
- **Chez** : Atelier textile  ·  **Demande** : 100 kg de laine  ·  **Prime** : 10000 €  ·  **XP** : 450

> **À la prise** — *« La première série s'est bien vendue. Cette fois, j'aurais besoin de 100 kg de laine. »*

> **À la livraison** — *« Très bien. Votre bergerie est devenue une vraie source d'approvisionnement. »*

#### 21. Livrer 12 kg de miel – Marché
- **Chez** : Marché  ·  **Demande** : 12 kg de miel  ·  **Prime** : 11000 €  ·  **XP** : 480

> **À la prise** — *« Plusieurs clients me demandent du miel produit dans le coin. Installez quelques ruches et gardez-moi les premiers 12 kg. »*

> **À la livraison** — *« Parfait. Le miel local ne restera pas longtemps sur les étals. »*


### Palier 14 — La gamme fermière
*Farine, œufs et miel dans la même commande*

#### 22. Livrer 72 kg de farine et 36 œufs et 12 kg de miel – Boulangerie
- **Chez** : Boulangerie  ·  **Demande** : 72 kg de farine, 36 œufs, 12 kg de miel  ·  **Prime** : 12000 €  ·  **XP** : 500

> **À la prise** — *« J'ai une nouvelle recette en tête. Cette fois, j'aurais besoin de votre farine, de vos œufs et de votre miel. »*

> **À la livraison** — *« Tout vient de votre exploitation. C'est exactement ce que je voulais pour cette gamme. »*


### Palier 15 — Le colza
*Le colza et le pressoir*

#### 23. Livrer 300 kg de colza – Coopérative
- **Chez** : Coopérative  ·  **Demande** : 300 kg de colza  ·  **Prime** : 13000 €  ·  **XP** : 520

> **À la prise** — *« Le colza se vend bien en ce moment. Si vous voulez vous lancer, je peux prendre immédiatement 300 kg. »*

> **À la livraison** — *« Très bien. Et si vous voulez augmenter sa valeur, le pressoir à colza de votre atelier devrait vous intéresser. »*

#### 24. Livrer 68 L d’huile de colza – Restaurant
- **Chez** : Restaurant  ·  **Demande** : 68 L d’huile de colza  ·  **Prime** : 14500 €  ·  **XP** : 560

> **À la prise** — *« Je préférerais utiliser une huile produite autour du village. Faites transformer votre colza et apportez-moi 68 litres. »*

> **À la livraison** — *« Parfait. C'est exactement ce qu'il nous fallait pour la cuisine. »*


### Palier 16 — Les olives
*L'oliveraie, l'enjambeuse, l'huile d'olive*

#### 25. Livrer 200 kg d’olives – Supermarché
- **Chez** : Supermarché  ·  **Demande** : 200 kg d’olives  ·  **Prime** : 17000 €  ·  **XP** : 600

> **À la prise** — *« Nous aimerions proposer des olives locales directement en rayon. Plantez une oliveraie et préparez-nous une première livraison de 200 kg. »*

> **À la livraison** — *« Très bien. Les premières caisses peuvent partir en rayon. »*


### Palier 17 — Le raisin
*La vigne, et ce qu'elle promet*

#### 26. Livrer 40 L d’huile d’olive – Restaurant
- **Chez** : Restaurant  ·  **Demande** : 40 L d’huile d’olive  ·  **Prime** : 18000 €  ·  **XP** : 650

> **À la prise** — *« Les olives sont bonnes, mais ce qui m'intéresse vraiment, c'est votre huile. J'en voudrais 40 litres. »*

> **À la livraison** — *« Celle-ci vaut clairement plus que les olives vendues brutes. »*

#### 27. Livrer 200 kg de raisin – Supermarché
- **Chez** : Supermarché  ·  **Demande** : 200 kg de raisin  ·  **Prime** : 20000 €  ·  **XP** : 700

> **À la prise** — *« Nous voudrions maintenant ajouter du raisin local au rayon frais. Commencez avec 200 kg. »*

> **À la livraison** — *« Très bien. Il se vendra facilement comme ça… mais j'imagine que le Caviste aura une autre idée. »*


### Palier 18 — Le vin
*La cave et le caviste*

#### 28. Livrer 140 L de vin – Caviste
- **Chez** : Caviste  ·  **Demande** : 140 L de vin  ·  **Prime** : 22000 €  ·  **XP** : 750

> **À la prise** — *« J'ai vu passer votre raisin. Il a du potentiel. Installez une cave et faites-moi une première cuvée de 140 litres. »*

> **À la livraison** — *« Voilà qui est intéressant. Votre ferme produit désormais quelque chose qui mérite qu'on s'y attarde. »*


### Palier 19 — Les cochons
*La porcherie et la boucherie*

#### 29. Livrer quatre porcs à la boucherie
- **Chez** : —  ·  **Demande** : porcs4  ·  **Prime** : 26000 €  ·  **XP** : 850

> **À la prise** — *« Vous avez maintenant suffisamment de céréales et d'aliment pour développer un élevage porcin. J'aurais besoin de quatre porcs prêts à partir. »*

> **À la livraison** — *« Très bien. Si votre élevage grandit, je pourrai prendre des lots plus importants. »*


### Palier 20 — Exploitation complète
*La grande réception, et toute la vallée à prendre*

#### 30. Livrer 72 kg de farine et 60 œufs et 28 kg de fromage et 20 kg de fromage de brebis et 12 kg de miel et 34 L d’huile de colza et 20 L d’huile d’olive et 140 L de vin – Restaurant
- **Chez** : Restaurant  ·  **Demande** : 72 kg de farine, 60 œufs, 28 kg de fromage, 20 kg de fromage de brebis, 12 kg de miel, 34 L d’huile de colza, 20 L d’huile d’olive, 140 L de vin  ·  **Prime** : 40000 €  ·  **XP** : 1000

> **À la prise** — *« Nous préparons une grande réception consacrée aux producteurs du village. Cette fois, je voudrais construire presque tout le menu autour de votre ferme : de la farine, des œufs, vos deux fromages, du miel, les deux huiles et votre vin. Prenez le temps de vous organiser. »*

> **À la livraison** — *« Tout est là. En regardant cette livraison, on mesure le chemin parcouru depuis vos premiers 30 kg de blé. Votre ferme est devenue une véritable exploitation. »*

> *Page suivante — **EXPLOITATION ÉTABLIE** : Vous avez développé les principales filières de votre ferme.*

> *Page suivante — **À VOUS DE JOUER** : Les commerces continueront désormais à proposer des contrats, tandis que vous pouvez développer librement vos parcelles, vos élevages, vos ruches, vos bâtiments et votre matériel.*

---

## 5. Le bandeau de mission — en haut à gauche

Le papier déchiré du coin haut gauche. Il ne porte que **deux choses** : le nom de la mission en cours, et l'étape du moment. Ni le nombre de mètres — la flèche verte le dit déjà — ni le texte du scénario, qui a été lu à la prise.

| ligne | ce qu'elle dit | quand |
|---|---|---|
| **titre** | le nom court de la mission — *Livrer 30 kg de blé* | tant que la mission court |
| **détail** | l'étape du moment — *Charger le blé au silo* | à chaque changement d'étape |
| *(tutoriel)* | le titre de la marche seul, sans détail | pendant le tutoriel |

---

## 5 bis. Les fenêtres de circonstance

### BRAVO — à chaque mission finie
> **BRAVO**  
> *le titre de la mission, puis la réponse du commerçant (ci-dessus)*  
> **+ prime en gros**  
> *+ XP · + valeur de la marchandise · palier franchi s'il y en a un*  
> — suite : *Prochaine mission – <lieu>*, ou *La campagne est finie*

### EXPLOITATION LIBRE — après la dernière mission
> **EXPLOITATION LIBRE**  
> Contrats illimités · Vente libre · Développement de l'exploitation · Améliorations maximales  
> — suite : *La vallée est à vous*

### COMMERCE DÉBLOQUÉ — quand un palier ouvre un commerce
> **COMMERCE DÉBLOQUÉ** — *<NOM DU COMMERCE>*  
> Vous pouvez y déposer votre production quand vous voulez, sans mission, dans la limite de ce qu'il peut prendre.  
> Il prend : *<jusqu'à huit marchandises>*  
> — suite : *Un point de plus sur la carte*

### MERCI POUR LA LIVRAISON — reçu, à chaque livraison qui solde une ligne
> **MERCI POUR LA LIVRAISON**  
> *<marchandises> – <LIEU>*  
> **+ <gain>**  
> *<combien> · <prix au kilo>*  
> — suite : *La caisse est à <argent>*

*Une livraison **incomplète** n'ouvre aucune fenêtre : elle passe en bandeau volant, sur une ligne — « 6 / 29 kg de farine · BOULANGERIE ».*

### STOCK PLEIN — quand un commerce ne peut plus rien prendre
> **<NOM DU COMMERCE>** — tampon *Stock plein*  
> *« Plus besoin de <marchandise> pour le moment, mon étal est plein. »*  
> Qui en veut encore, et ce que ça ferait : *<la liste des autres acheteurs, avec le prix>*

### PANNE SÈCHE — quand un engin tombe à sec
> **PANNE SÈCHE**  
> *« Plus une goutte, au bout du champ.  
> J'avais vu la jauge clignoter. »*  
> — suite : *La citerne est dans la cour, et le plein est gratuit*

---

## 6. Les bandeaux volants — 96 messages, 88 textes distincts

La ligne noire en capitales, au milieu de l'écran, deux à trois secondes. Elle confirme un geste ou signale un blocage ; elle ne raconte rien.

`<…>` marque ce qui se calcule au moment où le message paraît : un nom de commerce, une quantité, un nombre de kilos. Quand deux textes se partagent un même message — « pleine » ou « vide » —, les deux sont donnés, séparés d'une barre.

*(9 messages de plus ne portent aucun texte à eux : ils affichent une valeur calculée ailleurs — le nom d'un engin, une quantité — et il n'y a rien à y relire.)*

**Boucle**

- `<…> EN PREND`
- `CHANTIER TERMINÉ – PARCELLE <…>`
- `L’AUTOMATISATION PREND LE VOLANT – ARRÊTEZ-LA DANS LE PLAN DE TRAVAIL`
- `ÉLEVAGE TERMINÉ – PARCELLE <…>`

**Bouton contextuel de service**

- `<…> RENDUS À LA CUVE / LA CUVE DE LA COUR EST PLEINE`
- `EN ROUTE POUR LA BOUCHERIE`
- `MISSION PRISE – <…>`
- `UNE COLONIE DE PLUS AU RUCHER / UNE BÊTE DE PLUS AU PRÉ`

**Carburant**

- `PLEIN FAIT`

**Ce qu'on peut faire ici, et qui choisit**

- `<…> AU SILO`
- `<…> CHARGÉ`
- `<…> LIVRÉ À <…> – <…> €`
- `<…> RENTRÉ`
- `<…> RENTRÉ À L’ENTREPÔT`
- `<…> VENDU – <…> €`
- `<…> – <…><…> LIVRÉ À <…>`
- `ATELIER – <…>`
- `ATELIER – <…> <…>`
- `ATELIER – <…> ATTEND SA MATIÈRE`
- `ATELIER – <…> LOTS EN FILE`
- `ATELIER – LA FILE EST PLEINE`
- `AUGE REMPLIE`
- `BÊTE ABATTUE – <…>`

**Ce qu'une commande attend encore**

- `<…> – PLAN TERMINÉ`
- `CHAMP NETTOYÉ – <…> PIED<…> LAISSÉ<…>`
- `CONTRAT EXPIRÉ – <…>`
- `CONTRAT HONORÉ – <…> · +<…> XP · RENOMMÉE`
- `MOISSON ARRÊTÉE – VIDE LE SILO, PUIS RELANCE`
- `RIEN À FAIRE POUR CET OUTIL`
- `SILO PLEIN – LA TRÉMIE NE PEUT PAS SE VIDER`
- `TRAVAIL TERMINÉ`

**Ce que chaque commerce fait de ce qu'on lui apporte**

- `MISSION FAITE<…><…>`
- `NIVEAU <…> – <…>`

**Consommables : les deux cuves de la cour**

- `PLUS DE QUOI PLANTER VIDE – REMPLIR À LA CUVE DE LA COUR / ACHETER AU COMPTOIR`

**Entrées**

- `<…> ATTELÉ`
- `<…> CHANTIERS ARRÊTÉS / CHANTIER ARRÊTÉ – PARCELLE <…>`
- `<…> CHANTIERS EN CONTINU / EN UNE FOIS / CHANTIER EN CONTINU / EN UNE FOIS – PARCELLE <…>`
- `<…> DÉTELÉ`
- `<…> – IL FAUT LE <…> POUR LE TIRER / AUCUN OUTIL À PORTÉE`
- `<…> – PLAN ARRÊTÉ`
- `CHANTIER ARRÊTÉ – PARCELLE <…>`
- `CHANTIERS LANCÉS / CHANTIER LANCÉ – PARCELLE · EN CONTINU`
- `ENCLOS AMÉNAGÉ – <…>`
- `ENGIN EN AUTOMATIQUE – ARRÊTEZ-LE DANS LE PLAN DE TRAVAIL`
- `PARCELLE ACHETÉE`
- `PAUSE / EN ROUTE`
- `QUANTITÉ ATTEINTE`
- `SEMOIR RÉGLÉ SUR <…> EN CUVE`

**Le barème de l'élevage**

- `PÂTURE AMÉNAGÉE – RESTE À ACHETER DES BÊTES`

**Le barème du matériel**

- `BENNE OCCUPÉE PAR DU / TRÉMIE OCCUPÉE PAR DU <…>`
- `BENNE PLEINE`
- `SILO AGRANDI – <…> KG`
- `TRÉMIE PLEINE – DIRECTION SILO`

**Les colis : la marchandise, enfin visible**

- `<…> A UN CONTRAT À PROPOSER`
- `<…> – CONTRAT REFUSÉ, RENOMMÉE <…>`
- `CONTRAT ACCEPTÉ – <…>`
- `DÉJÀ QUATRE CONTRATS EN COURS`

**Les trois écrans de la régie**

- `ATELIER – LOT RETIRÉ`
- `BALANCE CLEARED`
- `COLLISIONS – ACTIVÉES / DÉSACTIVÉES`
- `COMMANDES – boutons / BOUTONS / MANCHE`
- `ENTREPÔT +<…>`
- `ENTREPÔT VIDÉ`
- `FLUIDITÉ – <…> IMAGES PAR SECONDE`
- `INTERFACE SUR LA GRILLE / INTERFACE D’ORIGINE`
- `NETTETÉ – <…>`
- `SILO +<…>`
- `SILO PLEIN – <…>`
- `SILO VIDÉ`
- `TOUT EST DÉVERROUILLÉ / LES PALIERS REPRENNENT LA MAIN`
- `VISAGES – PALETTE PAR IMAGE / VISAGES – PALETTE PARTAGÉE`

**Nouveaux onglets de la boutique**

- `+ <…> <…> À LA CUVE DE LA COUR`
- `+ <…> DANS LA CUVE`
- `+ <…> D’ENGRAIS À LA CUVE DE LA COUR`
- `<…> AGRANDI – <…> PLACES`
- `<…> RENDUS À LA CUVE / LA CUVE EST PLEINE`
- `MANGEOIRE – <…> CYCLES D’AUTONOMIE`
- `UNE COLONIE DE PLUS AU RUCHER / UNE BÊTE DE PLUS AU PRÉ`

**Panneau : boutique, améliorations, réglages**

- `<…> ACHETÉ`
- `<…> ACHETÉ – AU PARKING DE LA FERME`
- `<…> DISPONIBLE AU SEMOIR`
- `<…> – NIVEAU <…>`
- `PARCELLE ACHETÉE`

**Progression**

- `CUVE À ENGRAIS PRESQUE VIDE – À REMPLIR AU COMPTOIR AGRICOLE`
- `CUVE À GRAINES PRESQUE VIDE – À REMPLIR AU COMPTOIR AGRICOLE`
- `SILO PRESQUE PLEIN`

**Sauvegarde**

- `PARTIE SAUVEGARDÉE`
- `SAUVEGARDE INDISPONIBLE ICI`

**Son**

- `SON ACTIVÉ / SON COUPÉ`

**Écran d'accueil**

- `SAUVEGARDE ILLISIBLE – NOUVELLE PARTIE`

---

*Produit par `outils/textes` — `node relever.js` puis `python3 composer.py`. Les textes sont relevés dans le jeu qui tourne ; relancez les deux après toute modification pour que ce document reste vrai.*
