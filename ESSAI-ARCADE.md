# Essai arcade — septembre 2026

Cette proposition part du commit `77c729939c63704a1e27138f935866fe60b896bd`.
La branche d'essai est indépendante. Elle ne doit pas être promue en production avant validation du ressenti.

## Ce qui change

- Direction manuelle réactive, légère perte d'adhérence en virage rapide et retour d'adhérence au relâchement. Le pilotage automatique conserve sa direction et son adhérence.
- Suspension calculée par petits pas : roulis, tangage et débattement conservés.
- Impulsions de collision dissipatives, frôlements sans poussée ajoutée à chaque image, retour visuel distinct de la vitesse physique. Le choc sur une remorque agit d'abord sur sa suspension.
- Distance de freinage du trafic liée à la vitesse, redémarrage progressif, priorité supplémentaire aux carrefours après les retards provoqués par le joueur.
- Klaxons moins rapprochés, mixage du trafic et du dérapage plus discret, transitions de volume, silence en pause et suspension audio lorsque l'onglet est masqué.
- Interface papier existante affinée : contrastes, espacements, boutons, chiffres stables. Suppression de certains flous de fond.
- Calculs évités pour les engins garés au repos, rejet rapide des collisions éloignées et réduction des écritures répétées dans l'interface et les paramètres audio.

Les modèles 3D, textures, portraits, enregistrements audio, résolution et réglages graphiques sont conservés. Aucun paquet ni moteur physique ajouté. Le format des sauvegardes est inchangé.

## Vérifications

`node outils/arcade/tests.cjs` : 13 contrôles, dont conservation de la quantité de mouvement, dissipation d'énergie, contacts qui se séparent, capsules superposées, outils longs, suspension à 30/60/120 Hz, reprise d'adhérence et réduction des appels audio.

Dans Chromium, avec le jeu complet : démarrage, accélération/virage/relâchement, 6 minutes de trafic simulées sur routes dégagées (aucun véhicule immobilisé à la fin), arrêt derrière un engin puis reprise après son retrait, 120 images de la boucle complète sans erreur relevée, décodage des trois chocs, coupure/réactivation du son et extinction du dérapage.

Ces vérifications ne remplacent pas un essai sur le téléphone du joueur. Les chronométrages du navigateur varient et ne permettent pas de promettre un gain de FPS. Le fichier principal passe de 3 206 769 à 3 208 336 octets (+0,05 %), sans nouveaux médias.

## Essai conseillé

1. Prendre le tracteur puis le pick-up, accélérer et donner un virage vif. Relâcher la direction.
2. Frôler un véhicule puis le toucher de face à vitesse modérée. Essayer également une remorque.
3. Bloquer brièvement une voie, puis la dégager. Observer le freinage, le klaxon et la reprise.
4. Ouvrir les menus, régler le son, mettre en pause puis revenir au jeu.
5. Jouer quelques minutes sur le téléphone habituel, en paysage, avec les réglages graphiques habituels.

## Vercel et retour arrière

Le jeu reste un site statique avec `index.html` à la racine, comme le déploiement précédent. La branche séparée doit utiliser un déploiement **Preview** du projet existant. Aucune variable ni migration n'est nécessaire.

Tant que l'essai n'est pas fusionné/promu, revenir au lien de production suffit : rien n'y a changé. La sauvegarde du domaine Preview est séparée de celle du domaine de production par le navigateur.

Si cette proposition est ensuite mise en production, conserver son déploiement précédent et utiliser le retour arrière Vercel vers ce déploiement. Côté code, annuler le commit de cette proposition par un nouveau commit de revert plutôt que réécrire l'historique. Le format de sauvegarde étant conservé, aucune migration inverse n'est requise.
