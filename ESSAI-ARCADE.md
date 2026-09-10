# Essai arcade — septembre 2026

Cette proposition part du commit `77c729939c63704a1e27138f935866fe60b896bd`.
La branche d'essai est indépendante. Elle ne doit pas être promue en production avant validation du ressenti.

## Ce qui change

- Direction manuelle réactive, légère perte d'adhérence en virage rapide et retour d'adhérence au relâchement. Le pilotage automatique conserve sa direction et son adhérence.
- Suspension calculée par petits pas : roulis, tangage et débattement conservés.
- Impulsions de collision dissipatives, frôlements sans poussée ajoutée à chaque image, retour visuel distinct de la vitesse physique. Le choc sur une remorque agit d'abord sur sa suspension.
- Distance de freinage du trafic liée à la vitesse, redémarrage progressif, priorité supplémentaire aux carrefours après les retards provoqués par le joueur.
- Choc arrière : rotation calculée au point d'impact, avec inertie angulaire amortie. Le ressort qui ramenait latéralement le trafic sur sa voie est supprimé. Le véhicule braque et avance pour rejoindre sa trajectoire ; s'il est fortement désaxé ou bloqué, il effectue un court recul, puis repart en avant. Les volumes des autres véhicules et du décor sont vérifiés avant la manœuvre. La remorque suit son essieu pendant la récupération.
- Klaxons moins rapprochés, mixage du trafic et du dérapage plus discret, transitions de volume, silence en pause et suspension audio lorsque l'onglet est masqué.
- Interface papier existante affinée : contrastes, espacements, boutons, chiffres stables. Suppression de certains flous de fond.
- Calculs évités pour les engins garés au repos, rejet rapide des collisions éloignées et réduction des écritures répétées dans l'interface et les paramètres audio.

Les engins jouables, textures existantes, portraits, enregistrements audio, résolution et réglages graphiques sont conservés. La passe visuelle ci-dessous ajuste le décor. Aucun moteur physique ni dépendance supplémentaire n'est chargé par le navigateur. Le format des sauvegardes est inchangé.

## Cohérence visuelle et repères

- Audit de 57 vues : couverture de la carte en 18 secteurs, 21 sites commerciaux, ferme, port, forêt, maisons et les 15 véhicules du joueur. Les prises de vue comparent les mêmes positions avec un pick-up de référence.
- Les trois bateaux décoratifs de la marina utilisent désormais l'échelle commune du port (1,55). Espacement et distance au ponton ajustés ; aucun chevauchement entre bateaux ni avec le ponton dans le relevé des volumes.
- 24 faces d'enseignes portant noms ou symboles des activités : boutiques, industries, marché, scierie, menuisier, supermarché, criée, conserverie, export et dépôt forestier. Pictogrammes de poisson, bouteille, fromage, couverts, bois et textile. Le lettrage garde son rapport largeur/hauteur sur les différentes plaques.
- Parvis des commerces de proximité plus chauds, avec seuil clair peint dans les textures de sol existantes. Les cours industrielles restent distinctes. Chemins moins saturés pour mieux différencier sol, récoltes et anneaux d'action.
- Petit abri et râtelier vide au bord ouest du dépôt forestier. Son obstacle correspond à sa place, hors de la piste et du quai de chargement. Les piles restent liées au stock réel.
- Les dimensions et positions mesurées des 21 sites et des 15 engins sont identiques avant/après : portes, voies, quais et outils gardent leur calibrage. L'audit ne justifiait pas une réduction générale des maisons ni de l'entrepôt.

Coût mesuré sur 24 cadrages comparables : **un appel de dessin supplémentaire**, et deux dans la vue du dépôt avec l'abri. Les 24 enseignes partagent un atlas 512 × 512 et un seul maillage (48 triangles), sans animation ni nouvelle dépendance. Résolution du jeu et ombres inchangées. Le fichier principal livré passe de 1 772 890 à 1 778 413 octets (+0,31 %, environ 5,5 ko ; +2,3 ko en gzip local). Ce coût faible ne constitue pas une mesure de FPS sur téléphone.

Vérification de la version compacte : les 30 tests passent ; dans Chromium, six minutes de trafic simulé, reprise après obstacle, boucle complète et audio se terminent sans erreur relevée. Le passage et le chargement au dépôt restent dégagés. La version précédente de l'essai, avant cette passe visuelle, est conservée au commit `a79830468abc5eb77d3bca5ac607f3f9deb4fda5`.

Pistes visuelles suivantes : deux ou trois repères de paysage aux carrefours ruraux (haie courte, vieux chêne, petit pont), un rivage moins rectiligne par quelques rochers, des accès piétons reliant mieux les boutiques et une signalétique de quais à l'export. Préserver les surfaces cultivables et les zones de manœuvre ; privilégier les détails fixes regroupés plutôt que multiplier les objets animés.

## Allègement du jeu

### Champs denses et netteté maximale

Les réserves graphiques des cultures sont maintenant découpées en quatre secteurs par parcelle et par âge. Une boîte calculée d'après la géométrie, la rotation possible, la taille maximale et le décalage des semis remplace le grand test de sphère de chaque parcelle. Les secteurs hors du cadre ne sont pas envoyés au GPU. Les formes, couleurs, positions et nombres de plantes ne changent pas ; aucune réduction de densité ni changement de modèle à distance.

Les secteurs actifs sont suivis dans un ensemble ; un secteur vide est libéré à la récolte. Les changements cachés restent en attente. Au retour dans le cadre, le secteur reçoit toutes ses modifications avant son premier rendu, même si le budget ordinaire d'envoi est consommé. Le contrôle du cadrage et les envois ont lieu après la mise à jour de la caméra, y compris en pause.

Comparaison Chromium, même scène et même canevas 1280 × 720, parcelles activées et blé mûr :

| Cadrage | Touffes envoyées avant | Après | Réduction |
|---|---:|---:|---:|
| Au milieu des blés | 3 198 | 1 728 | 46 % |
| Plusieurs parcelles | 5 752 | 3 309 | 42 % |
| Bord des champs | 2 805 | 1 074 | 62 % |
| Vue très large | 7 089 | 6 766 | 5 % |

Les empreintes de tous les pixels sont identiques avant/après dans ces quatre cadrages, et le rendu optimisé est également identique au rendu qui soumet toutes les plantes. Une touffe de blé reste à 30 triangles. Le découpage augmente les appels de dessin des cultures ; le compromis réduit surtout le travail géométrique près des champs. Le gain est faible quand presque toute la ferme tient à l'écran. Les chronométrages GPU varient avec le navigateur et l'appareil : pas de promesse de cadence globale.

Le réglage **Netteté – Maximale**, avec **Grain de l'image = 1,00**, suit la définition native de l'écran, y compris au-delà d'un ratio de pixels de trois. Seule la limite matérielle du tampon graphique borne la taille. Les modes de netteté réduite restent des choix manuels ; aucune baisse automatique n'a été ajoutée. La description de résolution du curseur utilise le même calcul.

Six tests supplémentaires couvrent les secteurs et leurs limites, les cultures tournées et mises à l'échelle, la mise à jour au retour à l'écran, le budget d'envoi, la récolte et les limites de résolution. Un test de performance vérifie aussi qu'aucune plage de mise à jour n'est consommée pendant les images sautées en pause : l'envoi se fait dans le rendu effectif. Total : 37 tests.

Dans le navigateur, 36 états des sept cultures (dont les permanentes déjà installées) retrouvent les mêmes nombres, matrices et couleurs d'instances avant/après. Les volumes contiennent toutes les plantes testées ; récoltes partielles et libération des secteurs vides sont contrôlées. La copie compacte retrouve les mêmes pixels et les mêmes nombres de plantes envoyées que la source dans les quatre cadrages. Le format des sauvegardes reste identique. Retour à l'essai avant cette optimisation : commit `1a72e5e55e0428d8b4e4d52abff0972384533df9`.

### Allègement précédent

- Le fichier principal distribué passe de 3 214 383 à 1 772 890 octets, soit −44,8 %. La compression gzip locale passe de 1 486 800 à 961 491 octets (−35,3 %). Le transfert réel dépend de la compression du serveur. Ces chiffres concernent le fichier principal, pas l'ensemble des portraits téléchargés à la demande.
- Terser, installé uniquement pour la construction du site, retire commentaires et espaces inutiles des scripts. Aucune réduction des médias, aucune réécriture algébrique ni renommage des fonctions. Le fichier source demeure lisible dans le dépôt.
- Un quadrillage du décor limite les vérifications aux obstacles voisins, pour le véhicule conduit et les autres engins. L'ordre des contacts reste identique, même lorsqu'un contact déplace la machine. Ajouts et retraits du décor invalident l'index ; les arbres réservent leur taille adulte pour éviter de reconstruire l'index à chaque image pendant leur repousse.
- En pause et après stabilisation de la caméra, le décor fixe est redessiné au plus quatre fois par seconde. Les entrées et l'interface continuent de fonctionner ; déplacement de caméra, redimensionnement et reprise du jeu relancent le rendu immédiatement.
- Les libellés de service et repères de direction évitent les réécritures identiques.

Dans une comparaison Chromium sur 480 images simulées, le calcul des contacts avec le décor passe de 61,4 à 18,2 ms au total. La position et l'orientation finales sont strictement identiques, comme la taille du canevas, le réglage des ombres et les détails dessinés. Sur 120 images en pause stabilisée, le nombre de rendus passe de 120 à 8. Les durées de la boucle complète varient avec le navigateur et le GPU (5,54 puis 7,11 ms dans cette paire de mesures) : elles ne démontrent pas un gain global de FPS. Le banc accélère la simulation et ne mesure pas une cadence d'affichage réelle.

## Vérifications

`node outils/arcade/tests.cjs` : 20 contrôles, dont conservation de la quantité de mouvement entre engins, dissipation d'énergie, contacts qui se séparent, capsules superposées, outils longs, suspension à 30/60/120 Hz, reprise d'adhérence et réduction des appels audio. Les nouveaux contrôles couvrent le sens de rotation au choc arrière, l'absence de translation à l'arrêt, le déplacement dans l'axe des roues, le recul, les obstacles, la cohérence à 30/60/120 Hz et le retour d'une semi-remorque dans la circulation normale.

Dans Chromium, avec le jeu complet : démarrage, accélération/virage/relâchement, 6 minutes de trafic simulées sur routes dégagées (aucun véhicule immobilisé à la fin), arrêt derrière un engin puis reprise après son retrait, 120 images de la boucle complète sans erreur relevée, décodage des trois chocs, coupure/réactivation du son et extinction du dérapage.

Contrôles supplémentaires dans la scène réelle : choc sur un coin arrière de voiture et de semi-remorque ; voiture initialement désaxée de 97° effectuant un recul puis retrouvant sa voie ; circulation pendant six minutes après ces situations sans blocage final ni erreur numérique relevée. Le retour sur la voie se fait par déplacement dirigé ; seuls la séparation immédiate des volumes au contact et un raccord inférieur à 2,5 cm corrigent directement une position. Les manœuvres peuvent attendre lorsqu'aucun passage n'est libre.

`node outils/performance/tests.cjs` ajoute 10 contrôles : sélection conservative des obstacles, mutations du décor, repousse sans reconstruction, contacts successifs, grandes zones d'eau, comparaison des contacts et positions sur 1 200 situations, engins autonomes, rendu actif, réveil du rendu en pause et intégrité de la version compactée. Les images copiées et les contenus médias intégrés sont identiques octet pour octet. L'HTML et les styles hors scripts sont également identiques entre source et copie livrée.

Ces vérifications ne remplacent pas un essai sur le téléphone du joueur. Les chronométrages du navigateur varient et ne permettent pas de promettre un gain de FPS.

## Essai conseillé

### Travail en parallèle

Les parcelles placées dans le plan de travail peuvent employer des tracteurs différents en même temps. Le combiné reste prioritaire s'il est disponible ; sinon, une charrue, un semoir ou un épandeur compatible peut prendre l'autre parcelle. Le choix vérifie les consommables de l'outil retenu. Un outil est réservé dès qu'un véhicule part le chercher, et reste lié à son porteur lorsqu'il est attelé : aucune duplication ni emprunt à un engin occupé. Les réservations disparaissent avec les ordres, sans modifier les sauvegardes.

Les transports indépendants utilisent des véhicules terrestres libres dont la caisse accepte le produit. La benne sert de relais si les utilitaires sont pris ; elle bénéficie de la même réservation pendant l'attelage. Une seule mission de travail de la terre reste active par parcelle.

Validation : 50 tests (20 arcade, 11 performance, 6 cultures, 13 automatisation) et comparaison dans le jeu sur trois minutes simulées. Avant : combiné seul, second tracteur immobile, première parcelle 0/225 cellules travaillées. Après : deux tracteurs attribués dès le même tour, 224/225 cellules labourées dans la première parcelle pendant que le combiné travaille 289/345 cellules dans la seconde ; 179,1 secondes d'automatisation simultanée, aucune erreur. Ce contrôle vérifie la progression simultanée, pas la fin complète du cycle de récolte.

Pour essayer : programmer au moins deux parcelles dans le plan de travail, avec deux ensembles tracteur/outil achetés et compatibles. Avec un seul outil capable du travail demandé, la deuxième tâche attend sa disponibilité. Les autres parcelles non programmées ne sont pas lancées d'office. La production reste inchangée ; point de retour avant cet ajustement : `d917bdff19e030434c024fdfd5a3d0764d4f25d8`.

1. Prendre le tracteur puis le pick-up, accélérer et donner un virage vif. Relâcher la direction.
2. Frôler un véhicule puis le toucher de face à vitesse modérée. Essayer également une remorque.
   Toucher ensuite son coin arrière : il doit pivoter, contre-braquer et rejoindre sa voie en roulant. Laisser de la place devant et derrière pour les manœuvres.
3. Bloquer brièvement une voie, puis la dégager. Observer le freinage, le klaxon et la reprise.
4. Ouvrir les menus, régler le son, mettre en pause puis revenir au jeu.
5. Jouer quelques minutes sur le téléphone habituel, en paysage, avec les réglages graphiques habituels.

## Vercel et retour arrière

Le jeu reste un site statique. `vercel.json` construit et vérifie une copie compacte dans `dist/`, puis publie uniquement ce dossier. Terser est verrouillé à la version 5.51.2 dans `pnpm-lock.yaml`. En local : `pnpm install --frozen-lockfile --ignore-scripts`, puis `pnpm run build` et `pnpm test`. La branche séparée utilise un déploiement **Preview** du projet existant. Aucune variable ni migration n'est nécessaire.

Tant que l'essai n'est pas fusionné/promu, revenir au lien de production suffit : rien n'y a changé. La sauvegarde du domaine Preview est séparée de celle du domaine de production par le navigateur.

La version d'essai précédente, avant cet allègement, est conservée au commit `e49d1e66b4d3a07b30595bbc7d0ec2d5af047576`. Annuler le commit d'allègement permet de retrouver cette version sans annuler les chocs et manœuvres déjà validés.

Si cette proposition est ensuite mise en production, conserver son déploiement précédent et utiliser le retour arrière Vercel vers ce déploiement. Côté code, annuler le commit de cette proposition par un nouveau commit de revert plutôt que réécrire l'historique. Le format de sauvegarde étant conservé, aucune migration inverse n'est requise.
