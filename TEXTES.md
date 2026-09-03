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

**Écran d'accueil** — titre `MOISSON`, sous-titre « Votre partie est sauvegardée automatiquement. », boutons : « Commencer » · « Mode libre ».

**Première fenêtre de la campagne**, juste après le bouton *Commencer* :

> **UN HÉRITAGE**  
> *« Mon oncle m'a laissé sa terre, son tracteur et sa maison.  
> Je n'ai jamais conduit autre chose qu'une voiture. »*  
> — suite : *On commence par retourner le sol, paraît-il*

---

## 2. Le tutoriel — 11 marches

Une marche **attend le doigt** : elle ne part pas toute seule. Elle allume aussi un cercle jaune au sol et une flèche au bord de l'écran vers l'endroit à rejoindre.

### 1. PRÉPARER LA TERRE
> PRÉPARER LA TERRE — Première leçon : on ne sème pas directement dans l’herbe. La charrue est au parc. Il faut l’atteler au tracteur.

- **Arrive** : Dès la première seconde de la campagne, après la fenêtre « UN HÉRITAGE ».
- **Se solde** : Quand 98 % de la parcelle est labourée.
- **Où elle envoie** : champ

### 2. SEMER DU BLÉ
> SEMER DU BLÉ — La terre est prête. Maintenant, il faudrait peut-être y mettre quelque chose. Le semoir est au parc.

- **Arrive** : Dès que le labour est fini.
- **Se solde** : Quand 98 % de la parcelle est semée.
- **Où elle envoie** : champ

### 3. LAISSER POUSSER
> LAISSER POUSSER — Et maintenant… on attend. Je découvre que l’agriculture demande beaucoup de patience.

- **Arrive** : Dès que le semis est fini.
- **Se solde** : Quand tout le blé semé est mûr — le dernier épi, pas 98 %.
- **Où elle envoie** : champ

### 4. PREMIÈRE RÉCOLTE
> PREMIÈRE RÉCOLTE — Ça y est. Le blé est mûr. La grosse machine avec la barre devant ? C’est notre moissonneuse.

- **Arrive** : Dès que le blé est mûr.
- **Se solde** : Quand 98 % de la parcelle est moissonnée ET qu'au moins 30 kg sont rentrés.
- **Où elle envoie** : champ

### 5. VIDER AU SILO
> VIDER AU SILO — La moissonneuse ne va pas garder le grain éternellement. Direction le silo.

- **Arrive** : Dès que le champ est moissonné.
- **Se solde** : Quand 30 kg de blé sont entrés au silo.
- **Où elle envoie** : silo

### 6. RANGER LA MOISSONNEUSE
> RANGER LA MOISSONNEUSE — Première récolte terminée. On va déjà essayer de rendre la machine entière.

- **Arrive** : Dès que le silo a reçu la récolte.
- **Se solde** : Quand la moissonneuse est garée au parc à outils.
- **Où elle envoie** : parc

### 7. LANCER L’AUTOMATISATION
> LANCER L’AUTOMATISATION — Je ne vais pas tout conduire moi-même jusqu’à la fin de mes jours. Le bouton A lance l’automatisation : j’appuie dessus, je choisis ma parcelle sur la carte, et le tracteur se débrouille.

- **Arrive** : Dès que la moissonneuse est rangée. Le bouton A bat en jaune ; la carte qui s'ouvre fait battre la parcelle, puis la destination, puis LANCER.
- **Se solde** : Quand un premier chantier est lancé.

### 8. REPRENDRE LE PICK-UP
> REPRENDRE LE PICK-UP — Le grain est à l’abri, la machine est garée. Avant d’aller plus loin, j’irais bien voir à quoi ressemblent les environs. Le pick-up fera l’affaire.

- **Arrive** : Dès que le premier chantier est lancé.
- **Se solde** : Quand on conduit le pick-up.
- **Où elle envoie** : parc

### 9. EXPLORER LES ENVIRONS
> EXPLORER LES ENVIRONS — Un tour de reconnaissance. Jusqu’au croisement, là-haut au milieu des parcelles, pour voir à quoi ressemble le coin.

- **Arrive** : Dès qu'on conduit le pick-up. Cercle jaune au croisement des chemins, en haut des parcelles ; à l'arrivée, la fenêtre « DES POSSIBILITÉS D'EXPANSION ».
- **Se solde** : Deux secondes après l'arrivée au croisement : le téléphone sonne.
- **Où elle envoie** : croisement

### 10. LE TÉLÉPHONE SONNE
> LE TÉLÉPHONE SONNE — Le téléphone de la ferme. Qui ça peut bien être, qui appelle sur ce numéro ? Personne n’est censé l’avoir. Rentrons voir.

- **Arrive** : CAMPAGNE UNIQUEMENT — deux secondes après le croisement. C'est la marche qui fait sonner le téléphone chez soi.
- **Se solde** : Quand on prend la mission, au cercle vert de la ferme.
- **Où elle envoie** : ferme
- **En mode libre, elle dit autre chose** : **PRÉPARER UNE VENTE** — PRÉPARER UNE VENTE — Trente kilos devraient suffire pour voir ce que vaut notre première récolte.

### 11. PREMIÈRE VENTE
> PREMIÈRE VENTE — La Coopérative achète le grain directement. Voyons maintenant si tout ce travail rapporte quelque chose.

- **Arrive** : MODE LIBRE UNIQUEMENT — dès que le tour de reconnaissance est fait.
- **Se solde** : À la première vente, quel que soit le commerce.
- **Où elle envoie** : Coopérative

### Et à la fin, en mode libre seulement
> **VOUS SAVEZ L'ESSENTIEL**  
> *« Préparer, semer, attendre, récolter, stocker, vendre.  
> Bon… ça commence à ressembler à un métier. »*  
> — suite : *Cultivez, élevez, transformez et développez votre ferme comme vous le souhaitez*

---

## 3. Les leçons — 20, une seule fois chacune

Une leçon se lève **quand le geste devient possible ou nécessaire**, jamais deux fois dans la même partie. Un **MUR** est un blocage (le fermier fait la tête) ; une **porte** est une possibilité qui s'ouvre (il est surpris).

### REMPLIR LE SEMOIR  — *mur*
> **LE SEMOIR EST VIDE** — Je me demandais pourquoi rien ne sortait. Les graines sont dans la cuve de la cour. Sinon, direction le Comptoir agricole.

- **Arrive quand** : L'outil attelé a une cuve VIDE, et il reste de quoi la remplir à la ferme.
- **Où elle envoie** : reserve

### TRÉMIE PLEINE  — *mur*
> **TRÉMIE PLEINE** — Plus de place. Il faut vider le grain au silo avant de continuer.

- **Arrive quand** : La trémie de la moissonneuse est pleine.
- **Où elle envoie** : silo

### CARBURANT  — *mur*
> **LA JAUGE BAISSE** — Il serait peut-être temps de penser au plein avant de finir à pied. La citerne est dans la cour.

- **Arrive quand** : Un engin descend sous 40 % de gazole et la citerne de la cour n'est pas vide.
- **Où elle envoie** : gazole

### COMPTOIR AGRICOLE
> **LE COMPTOIR AGRICOLE** — Graines, engrais, carburant… quand les réserves de la ferme baissent, c’est ici qu’on se ravitaille.

- **Arrive quand** : Une des deux cuves de la cour tombe sous 10 %, ou le gazole sous 25 %.
- **Où elle envoie** : Comptoir agricole · fenêtre comptoir / semences

### GARAGE
> **LE GARAGE** — Tracteurs, outils, machines… si la ferme doit grandir, il faudra forcément passer par ici.

- **Arrive quand** : On a de quoi acheter le moins cher des engins ou outils en vitrine.
- **Où elle envoie** : Garage · fenêtre achat / engins

### AMÉLIORATIONS
> **AMÉLIORER LE MATÉRIEL** — Plus rapide, plus large, plus de capacité. Avant d’acheter une nouvelle machine, améliorer l’ancienne peut être une bonne idée.

- **Arrive quand** : On a de quoi payer le cran suivant d'un engin ou d'un outil déjà possédé.
- **Où elle envoie** : Garage · fenêtre amelio / engins

### NOUVELLE CULTURE
> **UNE NOUVELLE CULTURE** — Une nouvelle semence est disponible au Comptoir. Une fois achetée, le semoir pourra l’utiliser définitivement.

- **Arrive quand** : Une culture est ouverte par le palier et on a de quoi l'acheter.
- **Où elle envoie** : Comptoir agricole · fenêtre comptoir / semences

### CHANGER DE CULTURE
> **CHOISIR LA SEMENCE** — Le semoir sait maintenant planter plusieurs cultures. Le bouton de culture permet de choisir laquelle.

- **Arrive quand** : Le semoir est attelé et au moins deux cultures sont débloquées.

### ACHETER UNE PARCELLE
> **UNE TERRE À VENDRE** — Une parcelle voisine est disponible. Arrêtez-vous dessus pour connaître son prix.

- **Arrive quand** : Une parcelle est à vendre et on a de quoi la payer.
- **Où elle envoie** : parcelle

### PLAN DE TRAVAIL
> **LE PLAN DE TRAVAIL** — On n’est pas obligé de tout conduire soi-même. Depuis la carte, une machine peut être envoyée travailler seule sur une parcelle.

- **Arrive quand** : On possède un outil de travail et une parcelle cultivable.

### SILO
> **LE SILO SE REMPLIT** — Il commence à manquer de place. Sa capacité peut être augmentée depuis le menu Stockage.

- **Arrive quand** : Le silo dépasse 85 % et on a de quoi l'agrandir.
- **Où elle envoie** : silo · fenêtre stockage / agrandir

### MÉTIER D’ATELIER
> **TRANSFORMER POUR MIEUX VENDRE** — Vendre du blé, c’est bien. Le transformer en farine peut rapporter davantage. Les métiers s’installent à l’atelier.

- **Arrive quand** : Un métier d'atelier est ouvert par le palier et on a de quoi l'acheter.
- **Où elle envoie** : atelier · fenêtre production / metiers

### LANCER UNE PRODUCTION
> **LANCER UN LOT** — La matière est prête. Choisissez une recette et lancez la production depuis l’atelier.

- **Arrive quand** : L'atelier a au moins un métier, sa file est vide, et il y a de quoi lancer un lot.
- **Où elle envoie** : atelier · fenêtre production / produire

### ENTREPÔT
> **L’ENTREPÔT** — Le silo garde les récoltes en vrac. L’entrepôt accueille les produits transformés.

- **Arrive quand** : On roule avec une caisse dont le contenu se range à l'entrepôt.
- **Où elle envoie** : entrepot

### RÉGLAGES DE L’ATELIER
> **AMÉLIORER L’ATELIER** — Des lots plus gros, une production plus rapide ou davantage de commandes en attente. À vous de choisir ce qui vous ralentit le plus.

- **Arrive quand** : L'atelier a un métier et on a de quoi payer une de ses trois améliorations.
- **Où elle envoie** : atelier · fenêtre production / reglages

### ÉLEVAGE
> **INSTALLER UN ÉLEVAGE** — Une parcelle libre peut devenir un enclos. Après ça, il faudra encore acheter les animaux… et les nourrir. Évidemment.

- **Arrive quand** : Aucun enclos encore monté, une espèce ouverte, une parcelle libre et l'argent.
- **Où elle envoie** : champ

### ACHETER UN ANIMAL
> **PEUPLER L’ENCLOS** — L’enclos est prêt. Approchez-vous et utilisez INTERAGIR pour acheter vos premiers animaux.

- **Arrive quand** : Un enclos a de la place et on a de quoi acheter une bête.
- **Où elle envoie** : pature

### MANGEOIRE
> **ILS ONT FAIM** — Pas de nourriture, pas de production. Chargez de l’aliment et remplissez la mangeoire.

- **Arrive quand** : Un enclos habité tombe sous 35 % de mangeoire.
- **Où elle envoie** : pature

### PRODUCTION ANIMALE
> **PRODUCTION À RÉCUPÉRER** — Il y a quelque chose à récupérer dans l’élevage. Revenez avec un véhicule adapté et utilisez INTERAGIR.

- **Arrive quand** : Un enclos a de quoi être récolté (lait, laine, œufs, miel).
- **Où elle envoie** : pature

### CONTRATS
> **UN CONTRAT DISPONIBLE** — Un commerce cherche un fournisseur. Sa pastille bleue indique qu’un contrat est disponible.

- **Arrive quand** : Les contrats sont ouverts et un commerce en propose un.

---

## 4. Les 30 missions de campagne

Une mission se **prend chez soi** : le téléphone sonne, on rentre à la ferme, on lit la demande. Elle se **solde** en livrant, et le commerçant répond.


### Palier 1 — Le fermier
*Le blé, la coopérative, une parcelle*

#### 1. Livrer 30 kg de blé – Coopérative
- **Chez** : Coopérative  ·  **Demande** : 30 kg de blé  ·  **Prime** : 200 €  ·  **XP** : 60  ·  **En-tête** : UNE PREMIÈRE COMMANDE

> **À la prise** — *« Alors c’est vous qui avez repris la vieille ferme ? Bienvenue. Si votre première récolte est prête, apportez-moi 30 kg de blé. On va commencer tranquillement. »*

> **À la livraison** — *« Voilà, première vente. Pas mal pour un début. Et retenez une chose : même sans contrat, je rachète vos récoltes. »*

> *Page suivante — **VENTE LIBRE DÉBLOQUÉE** : La Coopérative achète vos récoltes à tout moment. / Les prix sont modestes, mais elle accepte facilement les gros volumes.*

> *Page suivante — **LA COOPÉRATIVE** (visage : Coopérative (bravo)) : « Je ne serai pas toujours celui qui paie le mieux. Mais quand il faut vendre vite, vous savez où me trouver. »*

> *Page suivante — **LE VILLAGE VOUS A REPÉRÉ** : Votre première récolte n’est pas passée inaperçue. / D’autres entreprises pourraient bientôt appeler.*

#### 2. Livrer 80 kg de blé – Usine céréales
- **Chez** : Usine céréales  ·  **Demande** : 80 kg de blé  ·  **Prime** : 300 €  ·  **XP** : 80

> **À la prise** — *« La Coopérative m’a parlé de votre blé. J’aimerais vérifier ce qu’il donne chez nous. Apportez-moi 80 kg. »*

> **À la livraison** — *« Hum… bonne tenue, grain régulier. Ça ira très bien. Gardez cette qualité et nous pourrons parler de volumes plus sérieux. »*


### Palier 2 — Productivité
*L'épandeur : la même terre, plus vite*

#### 3. Livrer 150 kg de blé – Coopérative
- **Chez** : Coopérative  ·  **Demande** : 150 kg de blé  ·  **Prime** : 600 €  ·  **XP** : 100

> **À la prise** — *« J’ai une commande un peu plus grosse : 150 kg de blé. Et si vous commencez à manquer de temps, regardez du côté de l’épandeur. L’engrais peut accélérer les choses. »*

> **À la livraison** — *« Très bien. Vous commencez à produire régulièrement. C’est généralement à ce moment-là qu’on commence à acheter trop de machines. »*

> *Préambule — **PRENDRE L’ÉPANDEUR** : PRENDRE L’ÉPANDEUR — Il est au garage du village, 250 €. On verra vite si l’engrais vaut son prix.*

> *Préambule — **REMPLIR L’ÉPANDEUR** : REMPLIR L’ÉPANDEUR — La cuve blanche de la cour est pleine d’engrais. Autant s’en servir.*

#### 4. Livrer 250 kg de blé – Usine céréales
- **Chez** : Usine céréales  ·  **Demande** : 250 kg de blé  ·  **Prime** : 900 €  ·  **XP** : 120

> **À la prise** — *« Le premier lot nous a convaincus. Cette fois, j’en voudrais 250 kg. Voyons si vous savez tenir le volume. »*

> **À la livraison** — *« Parfait. Quantité, qualité, délai. Vous commencez à devenir un fournisseur intéressant. »*


### Palier 3 — Première transformation
*Le moulin, la farine, la boulangerie*

#### 5. Livrer 72 kg de farine – Boulangerie
- **Chez** : Boulangerie  ·  **Demande** : 72 kg de farine  ·  **Prime** : 1400 €  ·  **XP** : 150

> **À la prise** — *« Votre blé est bon, mais moi, ce qu’il me faut, c’est de la farine ! Installez un moulin et apportez-m’en 72 kg. Je m’occupe du reste. »*

> **À la livraison** — *« Ah, ça c’est une farine qui me plaît ! Vous voyez ? Même blé… mais déjà beaucoup plus de valeur. »*


### Palier 4 — Le maïs et les poules
*Une deuxième parcelle, le broyeur, le poulailler*

#### 6. Livrer 180 kg de maïs – Usine céréales
- **Chez** : Usine céréales  ·  **Demande** : 180 kg de maïs  ·  **Prime** : 1800 €  ·  **XP** : 170

> **À la prise** — *« Le blé fonctionne. Passons au maïs. 180 kg pour un premier test. »*

> **À la livraison** — *« Très bien. Continuez comme ça. Une exploitation capable de fournir plusieurs céréales nous intéresse beaucoup plus. »*

#### 7. Livrer 24 œufs – Boulangerie
- **Chez** : Boulangerie  ·  **Demande** : 24 œufs  ·  **Prime** : 2500 €  ·  **XP** : 180

> **À la prise** — *« La farine, j’ai. Maintenant il me faut des œufs. Quelques poules, un peu de patience… et 24 œufs pour moi. »*

> **À la livraison** — *« Parfait ! Avec votre farine et vos œufs, je vais finir par ne plus avoir besoin de personne d’autre. »*


### Palier 5 — Deux chaînes à la fois
*La farine ET les œufs dans la même tournée*

#### 8. Livrer 72 kg de farine et 36 œufs – Boulangerie
- **Chez** : Boulangerie  ·  **Demande** : 72 kg de farine, 36 œufs  ·  **Prime** : 2800 €  ·  **XP** : 200

> **À la prise** — *« Cette fois je veux le panier complet : 72 kg de farine et 36 œufs. Voyons si vous arrivez à faire tourner deux productions en même temps. »*

> **À la livraison** — *« Tout est là, et en même temps. Ça, c’est déjà une vraie organisation de ferme. »*


### Palier 6 — L'orge
*L'orge, la cuve de brassage, le restaurant*

#### 9. Livrer 140 L de bière – Restaurant
- **Chez** : Restaurant  ·  **Demande** : 140 L de bière  ·  **Prime** : 3200 €  ·  **XP** : 220

> **À la prise** — *« On me demande de plus en plus de produits du coin. Si vous arrivez à faire une bière avec votre propre orge, je vous prends 140 litres. »*

> **À la livraison** — *« Très bonne. Et surtout : brassée juste à côté. Celle-là, je vais pouvoir la mettre en avant sur la carte. »*

#### 10. Livrer 60 L de bière et 120 kg de farine – Épicerie
- **Chez** : Épicerie  ·  **Demande** : 60 L de bière, 120 kg de farine  ·  **Prime** : 3600 €  ·  **XP** : 240

> **À la prise** — *« J’ai goûté votre bière au restaurant. Les clients en parlent déjà. Je monte un rayon local : 60 litres de bière et 120 kg de farine. »*

> **À la livraison** — *« Parfait. Votre ferme a maintenant son petit coin dans mon magasin. Essayez de ne pas me laisser les rayons vides. »*


### Palier 7 — L'avoine
*L'avoine et son usine*

#### 11. Livrer 200 kg d’avoine – Usine avoine
- **Chez** : Usine avoine  ·  **Demande** : 200 kg d’avoine  ·  **Prime** : 4000 €  ·  **XP** : 260

> **À la prise** — *« Nous cherchons justement un producteur d’avoine du secteur. Faites-moi parvenir 200 kg et nous testerons votre récolte. »*

> **À la livraison** — *« Très bon résultat. Continuez à en produire : ce ne sera probablement pas notre dernière commande. »*


### Palier 8 — Les vaches
*Le mélangeur premium, l'étable, la laiterie*

#### 12. Produire 184 kg d’aliment premium
- **Chez** : —  ·  **Demande** : alimentPlus  ·  **Prime** : 4500 €  ·  **XP** : 280  ·  **Qui parle** : Moi  ·  **En-tête** : NOURRIR MIEUX

> **À la prise** — *« Maïs, orge, avoine… j’ai tout ce qu’il faut. Avec un mélangeur, je pourrais fabriquer mon propre aliment premium. Deux lots devraient donner 184 kg. »*

> **À la livraison** — *« Voilà. Maintenant même les animaux mangent mieux que moi. »*

#### 13. Livrer 200 L de lait – Laiterie
- **Chez** : Laiterie  ·  **Demande** : 200 L de lait  ·  **Prime** : 5500 €  ·  **XP** : 300

> **À la prise** — *« On m’a dit que votre ferme continuait de s’agrandir. Si vous vous lancez dans les vaches, je vous réserve une première collecte de 200 litres. »*

> **À la livraison** — *« Très bon lait. Pour un premier troupeau, c’est prometteur. Si vous augmentez la production, appelez-moi. »*


### Palier 9 — Fromage fermier
*La fromagerie de la ferme*

#### 14. Livrer 350 L de lait – Laiterie
- **Chez** : Laiterie  ·  **Demande** : 350 L de lait  ·  **Prime** : 6000 €  ·  **XP** : 320

> **À la prise** — *« J’aurais besoin de 350 litres cette fois. Plus de vaches ou plus de patience : je vous laisse choisir. »*

> **À la livraison** — *« Parfait. Là, on ne parle plus d’un essai. Votre production laitière commence à compter. »*

#### 15. Livrer 28 kg de fromage – Restaurant
- **Chez** : Restaurant  ·  **Demande** : 28 kg de fromage  ·  **Prime** : 7000 €  ·  **XP** : 340

> **À la prise** — *« Votre lait est bon. Maintenant, faites-en quelque chose qu’on puisse mettre sur une assiette. Je vous prends 28 kg de fromage. »*

> **À la livraison** — *« Excellent. Celui-là reste sur la carte. Et je veux pouvoir écrire “fabriqué à la ferme”. »*


### Palier 10 — Gros volumes
*Le supermarché et son rayon fermier*

#### 16. Livrer 56 kg de fromage et 48 œufs – Supermarché
- **Chez** : Supermarché  ·  **Demande** : 56 kg de fromage, 48 œufs  ·  **Prime** : 8000 €  ·  **XP** : 360

> **À la prise** — *« Nous ouvrons un rayon producteurs locaux. Pour le lancement : 56 kg de fromage et 48 œufs. Il faut que le rayon paraisse rempli dès le premier jour. »*

> **À la livraison** — *« Parfait. Les quantités sont bonnes. Votre ferme est officiellement référencée chez nous. »*


### Palier 11 — La bergerie
*Les moutons et leurs brebis : la laine et le lait*

#### 17. Livrer 40 kg de laine – Atelier textile
- **Chez** : Atelier textile  ·  **Demande** : 40 kg de laine  ·  **Prime** : 8500 €  ·  **XP** : 380

> **À la prise** — *« Je prépare une petite série en laine locale. Si vous montez une bergerie, je peux utiliser vos 40 premiers kilos. »*

> **À la livraison** — *« Très belle matière. J’avais besoin d’un producteur régulier dans le secteur. Je crois que je viens de le trouver. »*

#### 18. Livrer 160 L de lait de brebis – Fromagerie
- **Chez** : Fromagerie  ·  **Demande** : 160 L de lait de brebis  ·  **Prime** : 9000 €  ·  **XP** : 400

> **À la prise** — *« Vos brebis donnent de la laine… mais elles peuvent faire beaucoup mieux que ça. Apportez-moi 160 litres de lait de brebis. »*

> **À la livraison** — *« Ah oui… beaucoup plus riche que le lait de vache. Avec ça, on peut faire quelque chose de vraiment intéressant. »*


### Palier 12 — Fromage de brebis
*Le produit le mieux payé de la ferme*

#### 19. Livrer 40 kg de fromage de brebis – Restaurant
- **Chez** : Restaurant  ·  **Demande** : 40 kg de fromage de brebis  ·  **Prime** : 9500 €  ·  **XP** : 420

> **À la prise** — *« J’ai goûté le fromage fait avec votre lait de brebis. Maintenant je veux le vôtre. Quarante kilos. »*

> **À la livraison** — *« Celui-là a du caractère. Gardez-moi une place dans votre prochaine production. »*


### Palier 13 — L'apiculture
*Le rucher, le miel, le marché du village*

#### 20. Livrer 100 kg de laine – Atelier textile
- **Chez** : Atelier textile  ·  **Demande** : 100 kg de laine  ·  **Prime** : 10000 €  ·  **XP** : 450

> **À la prise** — *« La première série est partie plus vite que prévu. Cette fois j’en veux 100 kg. »*

> **À la livraison** — *« Parfait. Votre bergerie est officiellement devenue mon fournisseur. »*

#### 21. Livrer 12 kg de miel – Marché
- **Chez** : Marché  ·  **Demande** : 12 kg de miel  ·  **Prime** : 11000 €  ·  **XP** : 480

> **À la prise** — *« On me demande du miel local toutes les semaines. Installez quelques ruches et gardez-moi les 12 premiers kilos. »*

> **À la livraison** — *« Regardez-moi ça… Celui-là ne va pas rester longtemps sur l’étal. »*


### Palier 14 — La gamme fermière
*Farine, œufs et miel dans la même commande*

#### 22. Livrer 72 kg de farine et 36 œufs et 12 kg de miel – Boulangerie
- **Chez** : Boulangerie  ·  **Demande** : 72 kg de farine, 36 œufs, 12 kg de miel  ·  **Prime** : 12000 €  ·  **XP** : 500

> **À la prise** — *« J’ai une idée : votre farine, vos œufs et votre miel. Si ça fonctionne comme je l’imagine, on tient quelque chose. »*

> **À la livraison** — *« Exactement ! Tout vient de votre ferme. Là, je peux vraiment raconter une histoire aux clients. »*


### Palier 15 — Le colza
*Le colza et le pressoir*

#### 23. Livrer 300 kg de colza – Coopérative
- **Chez** : Coopérative  ·  **Demande** : 300 kg de colza  ·  **Prime** : 13000 €  ·  **XP** : 520

> **À la prise** — *« Le colza se vend bien cette saison. Si vous avez envie d’essayer, je vous prends 300 kg pour commencer. »*

> **À la livraison** — *« Très bien. Et avant de tout revendre brut, regardez ce qu’un pressoir peut en tirer. »*

#### 24. Livrer 68 L d’huile de colza – Restaurant
- **Chez** : Restaurant  ·  **Demande** : 68 L d’huile de colza  ·  **Prime** : 14500 €  ·  **XP** : 560

> **À la prise** — *« J’aimerais remplacer une partie de nos huiles par quelque chose produit ici. Apportez-moi 68 litres d’huile de colza. »*

> **À la livraison** — *« Parfait. Produit à quelques kilomètres de la cuisine : difficile de faire plus local. »*


### Palier 16 — Les olives
*L'oliveraie, l'enjambeuse, l'huile d'olive*

#### 25. Livrer 200 kg d’olives – Supermarché
- **Chez** : Supermarché  ·  **Demande** : 200 kg d’olives  ·  **Prime** : 17000 €  ·  **XP** : 600

> **À la prise** — *« Les clients demandent davantage de produits frais locaux. Je vous réserve une place pour 200 kg d’olives. »*

> **À la livraison** — *« Très bien. Les caisses partent directement en rayon. Maintenant, j’attends de voir ce que vous allez faire avec l’huile. »*


### Palier 17 — Le raisin
*La vigne, et ce qu'elle promet*

#### 26. Livrer 40 L d’huile d’olive – Restaurant
- **Chez** : Restaurant  ·  **Demande** : 40 L d’huile d’olive  ·  **Prime** : 18000 €  ·  **XP** : 650

> **À la prise** — *« Les olives étaient très bonnes. Mais moi, ce que je veux vraiment, c’est 40 litres de votre huile. »*

> **À la livraison** — *« Voilà. Là, on change de catégorie. Cette huile vaut clairement plus que les olives vendues brutes. »*

#### 27. Livrer 200 kg de raisin – Supermarché
- **Chez** : Supermarché  ·  **Demande** : 200 kg de raisin  ·  **Prime** : 20000 €  ·  **XP** : 700

> **À la prise** — *« On aimerait ajouter du raisin local au rayon fruits. Une première livraison de 200 kg fera l’affaire. »*

> **À la livraison** — *« Très bien. Il se vendra facilement comme ça. Mais connaissant le caviste… il ne va pas vouloir le manger. »*


### Palier 18 — Le vin
*La cave et le caviste*

#### 28. Livrer 140 L de vin – Caviste
- **Chez** : Caviste  ·  **Demande** : 140 L de vin  ·  **Prime** : 22000 €  ·  **XP** : 750

> **À la prise** — *« Votre raisin m’intrigue. Ne le vendez pas tout. Installez une cave, laissez-le travailler… et apportez-moi 140 litres de votre première cuvée. »*

> **À la livraison** — *« Hm… intéressant. Vraiment intéressant. Vous ne cultivez plus seulement des produits. Vous commencez à avoir une signature. »*


### Palier 19 — Les cochons
*La porcherie et la boucherie*

#### 29. Livrer quatre porcs à la boucherie
- **Chez** : —  ·  **Demande** : porcs4  ·  **Prime** : 26000 €  ·  **XP** : 850  ·  **Qui parle** : Boucherie

> **À la prise** — *« Vous produisez maintenant assez d’aliment pour élever correctement des porcs. Montez une porcherie et préparez-moi quatre bêtes. »*

> **À la livraison** — *« Très bien. Bêtes saines, bon gabarit. Si vous augmentez l’élevage, je prendrai des lots plus importants. »*


### Palier 20 — Exploitation complète
*La grande réception, et toute la vallée à prendre*

#### 30. Livrer 72 kg de farine et 60 œufs et 28 kg de fromage et 20 kg de fromage de brebis et 12 kg de miel et 34 L d’huile de colza et 20 L d’huile d’olive et 140 L de vin – Restaurant
- **Chez** : Restaurant  ·  **Demande** : 72 kg de farine, 60 œufs, 28 kg de fromage, 20 kg de fromage de brebis, 12 kg de miel, 34 L d’huile de colza, 20 L d’huile d’olive, 140 L de vin  ·  **Prime** : 40000 €  ·  **XP** : 1000  ·  **En-tête** : UNE GRANDE COMMANDE

> **À la prise** — *« J’organise une réception entièrement consacrée aux producteurs du village. Et pour être franche… j’aimerais construire presque tout le menu autour de votre ferme.
Farine, œufs, fromage de vache, fromage de brebis, miel, huiles et vin. Pas besoin de courir. Organisez-vous. »*

> **À la livraison** — *« Tout est là. Absolument tout. Quand je pense que votre première livraison faisait trente kilos de blé… »*

> *Page suivante — **L’EXPLOITATION** (visage : Moi (bravo)) : « Trente kilos de blé… / J’avais presque oublié. »*

> *Page suivante — **L’EXPLOITATION** (visage : Moi (rire)) : « Finalement, l’oncle ne m’avait peut-être pas laissé une vieille ferme. / Il m’avait laissé un début. »*

> *Page suivante — **EXPLOITATION ÉTABLIE** : Vous maîtrisez maintenant les principales filières de la ferme.*

> *Page suivante — **LA FERME CONTINUE** : La campagne principale est terminée, mais votre exploitation continue de vivre. / Contrats illimités  ·  Vente libre  ·  Parcelles  ·  Élevages  ·  Production  ·  Améliorations — suite : À vous de décider de la suite*

> *Page suivante — **MAINTENANT, C’EST LA VÔTRE** : Continuez à acheter des terres, développer vos élevages, améliorer votre matériel et répondre aux contrats du village. — suite : CONTINUER À JOUER*

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

### CONTRAT TERMINÉ — à chaque mission finie
> **CONTRAT TERMINÉ**  
> *le titre de la mission, puis la réponse du commerçant (ci-dessus)*  
> **+ prime en gros**  
> *+ XP · + valeur de la marchandise · nouveau palier s'il y en a un*  
> — suite : *Prochaine mission – <lieu>*, ou *La campagne est finie*

### LA FERME CONTINUE — après la dernière mission
> **LA FERME CONTINUE**  
> La campagne principale est terminée, mais votre exploitation continue de vivre.  
> Contrats illimités · Vente libre · Parcelles · Élevages · Production · Améliorations  
> — suite : *À vous de décider de la suite*  
> *(c'est l'avant-dernière page de la mission 30, ci-dessus ; le dernier mot est le bouton CONTINUER À JOUER)*

### NOUVEAU CLIENT — quand un palier ouvre un commerce
> **NOUVEAU CLIENT** — *<NOM DU COMMERCE>*  
> Ce commerce achète désormais certains de vos produits, même en dehors des missions.  
> *<les produits acceptés, en vignettes — jusqu'à huit>*  
> — suite : *À retrouver sur la carte*

### LIVRAISON ACCEPTÉE — reçu, à chaque livraison qui solde une ligne
> **LIVRAISON ACCEPTÉE**  
> *<quantité et marchandise> → <LIEU>*  
> **+ <gain>**  
> *<combien> × <prix à l'unité>*  
> — suite : *La caisse est à <argent>*

*Une livraison **incomplète** n'ouvre aucune fenêtre : elle passe en bandeau volant, sur une ligne — « 6 / 29 kg de farine · BOULANGERIE ».*

### STOCK SATURÉ — quand un commerce ne peut plus rien prendre
> **STOCK SATURÉ** — *<NOM DU COMMERCE>*  
> *« Pas de <marchandise> en plus pour le moment. J'en ai encore plein les étagères. »*  
> Autres acheteurs : *<jusqu'à quatre, avec le prix à l'unité — Restaurant → 1,15 € / kg>*

### PANNE SÈCHE — quand un engin tombe à sec
> **PANNE SÈCHE**  
> *« Voilà. Plus une goutte.  
> Et bien sûr, je suis à l'autre bout du champ. »*  
> — suite : *La citerne est dans la cour*

---

## 6. Les bandeaux volants — 96 messages, 88 textes distincts

La ligne noire en capitales, au milieu de l'écran, deux à trois secondes. Elle confirme un geste ou signale un blocage ; elle ne raconte rien.

`<…>` marque ce qui se calcule au moment où le message paraît : un nom de commerce, une quantité, un nombre de kilos. Quand deux textes se partagent un même message — « pleine » ou « vide » —, les deux sont donnés, séparés d'une barre.

*(9 messages de plus ne portent aucun texte à eux : ils affichent une valeur calculée ailleurs — le nom d'un engin, une quantité — et il n'y a rien à y relire.)*

**Boucle**

- `<…> EN PREND`
- `CHANTIER TERMINÉ – PARCELLE <…>`
- `CONDUITE AUTOMATIQUE ACTIVÉE`
- `ÉLEVAGE TERMINÉ – PARCELLE <…>`

**Bouton contextuel de service**

- `<…> RENDUS À LA CUVE / LA CUVE DE LA COUR EST PLEINE`
- `EN ROUTE POUR LA BOUCHERIE`
- `MISSION PRISE – <…>`
- `NOUVELLE COLONIE INSTALLÉE / NOUVEL ANIMAL AJOUTÉ`

**Carburant**

- `RÉSERVOIR PLEIN`

**Ce qu'on peut faire ici, et qui choisit**

- `<…> AU SILO`
- `<…> CHARGÉ`
- `<…> LIVRÉ À <…> – <…> €`
- `<…> RENTRÉ`
- `<…> RENTRÉ À L’ENTREPÔT`
- `<…> VENDU – <…> €`
- `<…> – <…><…> LIVRÉ À <…>`
- `ANIMAL LIVRÉ À LA BOUCHERIE – <…>`
- `ATELIER – <…>`
- `ATELIER – <…> <…>`
- `ATELIER – <…> ATTEND SA MATIÈRE`
- `ATELIER – <…> LOTS EN FILE`
- `ATELIER – LA FILE EST PLEINE`
- `MANGEOIRE REMPLIE`

**Ce qu'une commande attend encore**

- `<…> – PLAN TERMINÉ`
- `CHAMP NETTOYÉ – <…> PIED<…> LAISSÉ<…>`
- `CONTRAT EXPIRÉ – <…>`
- `CONTRAT HONORÉ – <…> · +<…> XP · RENOMMÉE`
- `RIEN À FAIRE POUR CET OUTIL`
- `SILO PLEIN · MOISSON INTERROMPUE`
- `SILO PLEIN – LA TRÉMIE NE PEUT PAS SE VIDER`
- `TRAVAIL TERMINÉ`

**Ce que chaque commerce fait de ce qu'on lui apporte**

- `MISSION FAITE<…><…>`
- `NIVEAU <…> – <…>`

**Consommables : les deux cuves de la cour**

- `PLUS DE QUOI PLANTER VIDE · REMPLIR À LA CUVE DE LA COUR / ACHETER AU COMPTOIR`

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
- `ENGIN EN MODE AUTOMATIQUE`
- `NOUVELLE PARCELLE ACHETÉE`
- `OBJECTIF ATTEINT`
- `PAUSE / REPRISE`
- `SEMOIR RÉGLÉ SUR <…> EN CUVE`

**Le barème de l'élevage**

- `PÂTURE AMÉNAGÉE – RESTE À ACHETER DES BÊTES`

**Le barème du matériel**

- `BENNE OCCUPÉE PAR DU / TRÉMIE OCCUPÉE PAR DU <…>`
- `BENNE PLEINE`
- `SILO AGRANDI – <…> KG`
- `TRÉMIE PLEINE · VIDER AU SILO`

**Les colis : la marchandise, enfin visible**

- `<…> A UN CONTRAT À PROPOSER`
- `<…> – CONTRAT REFUSÉ, RENOMMÉE <…>`
- `CONTRAT ACCEPTÉ – <…>`
- `MAXIMUM <…> CONTRATS EN COURS`

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
- `NOUVELLE COLONIE INSTALLÉE / NOUVEL ANIMAL AJOUTÉ`

**Panneau : boutique, améliorations, réglages**

- `<…> ACHETÉ`
- `<…> ACHETÉ – AU PARKING DE LA FERME`
- `<…> DISPONIBLE AU SEMOIR`
- `<…> – NIVEAU <…>`
- `NOUVELLE PARCELLE ACHETÉE`

**Progression**

- `CUVE À ENGRAIS PRESQUE VIDE – À REMPLIR AU COMPTOIR AGRICOLE`
- `CUVE À GRAINES PRESQUE VIDE – À REMPLIR AU COMPTOIR AGRICOLE`
- `SILO À <…> %`

**Sauvegarde**

- `PARTIE SAUVEGARDÉE`
- `SAUVEGARDE INDISPONIBLE ICI`

**Son**

- `SON ACTIVÉ / SON COUPÉ`

**Écran d'accueil**

- `SAUVEGARDE ENDOMMAGÉE · NOUVELLE PARTIE CRÉÉE`

---

*Produit par `outils/textes` — `node relever.js` puis `python3 composer.py`. Les textes sont relevés dans le jeu qui tourne ; relancez les deux après toute modification pour que ce document reste vrai.*
