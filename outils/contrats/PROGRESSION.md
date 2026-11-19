# Campagne guidée par les besoins

Version d’essai, 9 septembre 2026. Les 37 missions gardent leurs indices pour préserver les sauvegardes.

Les appels précèdent les achats. Le passage de niveau ouvre les possibilités sans afficher une fenêtre de commerce ni conseiller un métier prématurément. Les achats facultatifs gardent 150 € de fonctionnement ainsi que le coût des équipements et élevages manquants de la mission actuelle et des deux suivantes. Les montants viennent des tables du jeu ; cette réserve est un garde-fou, pas une simulation complète des dépenses de carburant, semences et choix personnels du joueur.

| Besoin reçu | Aide proposée après acceptation |
|---|---|
| 150 kg de blé à la Coopérative | Épandeur au garage, puis remplissage à la cuve blanche |
| Première farine du boulanger | Installer le moulin à 650 €, sans pousser ses améliorations |
| Maïs, orge, avoine, colza | Semence correspondant à la commande |
| Premiers œufs, lait, laine, miel, porcs | Terre supplémentaire si nécessaire, puis enclos et animaux ; conserver un champ cultivable |
| Préparation de la collecte laitière | Appel de la laiterie, mélangeur premium et 184 kg d’aliment avant le troupeau |
| Bière, fromages, huiles, vin | Métier de transformation correspondant |
| Olives puis raisin | Plants et enjambeuse, utilisable pour les deux récoltes |
| Tournées plus importantes | Fourgon proposé si le budget le permet ; obligatoire pour transporter les porcs |
| Volume de travail avancé | Tracteur lourd puis combiné 3-en-1 : labour, semis et fertilisation en une passe |
| Scierie | Abatteuse puis porteur, avec leurs rôles distincts |
| Chantier naval | Barque (ou chalutier déjà possédé), caseyeur et camion frigorifique |
| Grosses commandes maritimes | Chalutier facultatif ; le caseyeur garde son rôle pour les crustacés |
| Export | Semi facultatif et explication des remorques spécialisées |

La capacité d’atelier et la moissonneuse peuvent être conseillées quand le volume le justifie et que la réserve reste disponible. Un achat indispensable non finançable dirige vers une vente à la Coopérative pendant la campagne. Les commandes infinies et les ventes limitées aux demandes restent activées après la campagne.

## Transport

- Animaux : fourgon uniquement, cinq places, une espèce à la fois, aucun mélange avec des marchandises.
- Poisson et crustacés sur route : camion frigorifique ou semi avec remorque frigorifique. Les cales des bateaux restent dédiées à leur propre pêche.
- Porteur : grumes ; enjambeuse : olives et raisin ; remorques : leurs produits compatibles.
- Les chargements incompatibles déjà présents dans une ancienne sauvegarde peuvent terminer leur déchargement pour éviter une perte. Ils ne peuvent pas être rechargés. L’espèce et le tarif du bétail sont maintenant sauvegardés.

## Présentation des clients et images

Une page présente tous les produits acceptés après la première mission terminée de chaque client. Le chantier naval présente sa flotte. La liste des clients déjà présentés est sauvegardée et déduite des missions terminées pour les anciennes parties.

Les icônes poisson, crustacés et grumes remplacent les anciennes caisses génériques. Images générées avec imagegen, dans le style facetté des icônes blé et farine, puis exportées par le traitement d’assets : fond transparent, 78 × 78 pixels, palette de 64 couleurs. Poids total : 12 696 octets. Aucun ajout à la géométrie 3D ni changement de résolution.

## Vérification

155 tests automatisés passent, dont 24 vérifications de progression, budgets, transport, sauvegardes et catalogue illustré. Le build de déploiement passe. Les contrôles couvrent notamment le guidage réel vers l’atelier, le menu de l’épandeur, les appels des missions de préparation et les chargements issus d’actions automatiques anciennes.

Le navigateur de jeu n’était pas disponible dans cette session : une traversée visuelle et une campagne complète jouée restent à valider sur la preview.

## Retour arrière

État précédant cette modification : `fc2f40efba55a0a55b8fc5188e4564ea8b9b1477`, sur `codex/arcade-preview-20260907`. Revenir à cet état sur la branche d’essai restaure la progression antérieure. Aucun changement à la branche de production.
