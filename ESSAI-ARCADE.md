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

Les modèles 3D, textures, portraits, enregistrements audio, résolution et réglages graphiques sont conservés. Aucun moteur physique ni dépendance supplémentaire n'est chargé par le navigateur. Le format des sauvegardes est inchangé.

## Allègement du jeu

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
