# Rotation des cultures et partage des tracteurs

Les parcelles de blé, maïs et avoine partagent désormais les engins disponibles selon leur temps d'attente. Toutes les missions terminées sont libérées avant l'attribution ; les travaux des parcelles sont attribués avant les navettes de livraison.

Chaque ordre conserve sa culture. Le semoir va à la réserve pour changer de semence et restitue les graines restantes sans les perdre. Une réserve pleine peut échanger son stock avec le semoir si le chargement libère assez de place ; sinon un message précise le blocage. Le fonctionnement des casiers manuels et les sauvegardes existantes restent compatibles.

Un semoir vide en cours de passe quitte le champ par un bord libre, rejoint la citerne et revient au point où le travail a été interrompu. Les accès aux réserves vérifient les premiers tronçons et cherchent une autre entrée routière lorsqu'une haie ou une clôture barre la sortie. Ce calcul se fait uniquement à la création de l'itinéraire. Aucun changement de résolution, modèle, texture ou rendu.

La moissonneuse conserve son passage au silo avant un changement de récolte, y compris pour un très petit reste de grain. Les tâches peuvent attendre normalement si tous les outils adaptés sont occupés, si les cultures poussent ou si une réserve manque de stock.

## Vérification

- 201 tests automatisés, dont 13 nouveaux cas : trois cultures et deux tracteurs, équité, réservations libérées, changement de graines à l'arrêt, conservation du stock, reprise en cours de passe, réserve vide, sortie de champ, contournement d'un obstacle et vidage d'un fond de trémie avant la culture suivante.
- Simulation du jeu réel pendant 1 800 secondes, avec les tracteurs vert et jaune, la moissonneuse et trois parcelles. Capacités des semoirs volontairement réduites à 8 kg dans le test pour multiplier les ravitaillements.
- Les deux tracteurs ont chacun travaillé sur les trois parcelles ; 39 remplissages, 11 changements de semences et 13 missions de moisson attribuées.
- Plus de 226 kg de blé, 471 kg de maïs et 406 kg d'avoine livrés au silo dans cet essai. Zéro cellule semée avec la mauvaise culture ; aucune erreur d'exécution.
- Deux blocages reproduits puis corrigés : départ direct contre la haie pendant un ravitaillement, puis départ vers une route située derrière la clôture au cycle suivant.

Déploiement limité à la branche de prévisualisation. La révision précédente permet le retour arrière.
