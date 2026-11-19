# Automatisations et livraisons — 10 septembre 2026

Le panneau conserve toutes les activités en cours au-dessus du formulaire. Une activité se sélectionne pour passer immédiatement en continu ou l'arrêter ; sa croix ne retire que cette activité et ses propres véhicules.

La création commence par Culture, Élevage, Forêt ou Port. Les parcelles possédées, adaptées à l'activité et sans chantier sont vertes. Les réglages suivent la sélection, puis la destination. La forêt et les bateaux peuvent garder la production au dépôt/quai ou livrer un commerce ayant une demande acceptée pour leur produit. Un véhicule routier compatible est attribué indépendamment au transport.

Les missions et contrats acceptés sont identifiés au lancement. Chaque chargement tient compte du reste demandé et des marchandises déjà en route. Chaque transfert est borné à la quantité restante. Une demande terminée arrête sa livraison et l'activité lorsqu'elle n'a plus de destination ; un élevage peut continuer à fournir son autre produit. Un nouveau contrat ne réactive pas une ancienne automatisation. Une saturation de stock ou l'absence de camion disponible met le travail en attente.

Les sauvegardes gardent les destinations et identifiants des commandes. Les activités nature retrouvent également leur camion chargé ; les anciennes sauvegardes restent lisibles.

## Vérifications

- Compilation et suite de 174 tests, dont 18 nouveaux cas de livraisons : identités des commandes, réservations partagées, arrêt isolé, saturation, reprise après sauvegarde, deux activités simultanées et quantité exacte.
- Dans une copie de test du jeu, sans sauvegarde personnelle : sélection Culture → parcelle → silo → lancement d'une seconde culture ; accès à une pêche en cours, passage en continu puis arrêt sans supprimer l'abatteuse ou la culture.
- Filtrage Culture/Élevage vérifié dans le navigateur ; affichage contrôlé à 1280 × 720 et 740 × 390. Les destinations prioritaires restent visibles et les réglages défilent si nécessaire.
- Transferts réels du jeu avec positions préparées aux points de service : 50 kg débarqués par la barque, 50 kg chargés dans le frigorifique, 50 kg vendus à la criée, cargaison restante nulle et automatisation supprimée. Le test contrôle les actions et les stocks ; il ne constitue pas un parcours routier chronométré de toute la carte.
- Aucun nouveau modèle, texture ou effet graphique. Résolution inchangée. Le répartiteur de livraison travaille deux fois par seconde.

## Retour arrière

Modifications destinées à la branche d'essai `codex/arcade-preview-20260907`. Point précédent : `16675d083961d1053f202682429439417b86c2f9`. La production n'est pas modifiée. Le changement peut être annulé par un commit de restauration sur la branche d'essai.
