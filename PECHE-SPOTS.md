# Zones de pêche variables — 10 septembre 2026

- Deux bancs de poissons bleus pour la barque et le chalutier ; une zone orange à crustacés pour le caseyeur.
- Positions tirées dans la mer à chaque nouvelle partie. Renouvellement après une pêche lorsque le bateau s'est éloigné, ou après 3 à 5 minutes sans utilisation. Les zones proches d'un bateau ou réservées par une automatisation restent stables.
- Espacement entre zones, marge avec les côtes, exclusion de la jetée et de la marina. Les positions candidates évitent également les bateaux présents.
- Les trois anneaux existants sont déplacés et recolorés, sans modèle ni texture supplémentaires. La résolution ne change pas. Vérification du renouvellement à 2 Hz avec le répartiteur existant.
- Pêche manuelle, tutoriel, guidage de mission et automatisation filtrent tous le produit de la zone. Un bateau incompatible ne récolte rien ; le caseyeur ne produit plus d'animation de poissons qui sautent.
- Les coordonnées, le délai et l'état d'utilisation sont sauvegardés. Les anciennes sauvegardes restent acceptées.

## Validation

188 tests : les 174 précédents et 14 tests ciblés sur les zones (3 000 positions tirées, séparation, réservations, bateau présent, renouvellement, sauvegarde, rejet des coordonnées invalides, prises et marqueurs).

Contrôle dans une copie du jeu : changement visuel des positions et des couleurs ; barque et caseyeur produisent zéro sur une zone incompatible, respectivement 10 kg de poissons et 20 kg de crustacés sur leur zone. Les trois automatismes choisissent les indices distincts 0/1/2, avec les bons produits. Les 300 positions supplémentaires contrôlées contre les collisions du décor sont libres. Sauvegarde des positions restaurée à l'identique, aucune erreur navigateur.

## Publication réversible

Branche d'essai : `codex/arcade-preview-20260907`. Point précédent : `8b948fe71594859debfb96c2806db645df835bf7`. Production inchangée.
