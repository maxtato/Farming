# Port et portraits — essai du 10 septembre 2026

- Sept personnages, vingt expressions détourées, dans les deux réglages de palette.
- Images WebP avec transparence réelle : neutre 288 × 360, autres expressions 576 × 720. Même écart des yeux (15 % de la largeur), même ligne des yeux (31,8 % de la hauteur) et même coupe basse que les portraits d'origine.
- Suppression des dimensions et masquages CSS particuliers aux nouveaux personnages. Les fenêtres utilisent leurs cadres habituels.
- Quai prolongé sur la rive est : mêmes bordures, bollards, chaînes et pneus. Angle intérieur fermé, décor statique fusionné avec le quai existant.
- Suppression des mâts à fanions en forme de croix sur les bateaux, au quai de débarque et près du phare, ainsi que du petit obstacle devenu invisible au quai.
- Le vendeur devient le « Comptoir des pêcheurs » dans les fenêtres, missions, indications et étiquette. Les identifiants internes restent stables ; les anciennes présentations enregistrées sont converties au nouveau nom.

## Vérification

156 tests de régression validés. Contrôle supplémentaire des 40 fichiers : alpha réel, coins transparents, format 4:5, aucun résidu de fond magenta, copie de déploiement identique. Réglages de résolution inchangés.

Le phare, la rive et les bateaux ont été examinés dans le rendu 3D du jeu, sans erreur signalée. Les vingt expressions ont été comparées aux portraits d'origine sur une planche commune. Après rétablissement du navigateur, 36 affichages ont été contrôlés dans les fenêtres du jeu : les neuf personnages comparés occupent tous 96 × 120 pixels en contrat et le même cadre adaptatif en annonce. Le second réglage de palette a également été vérifié. Le guichet propose la barque, le chalutier et le caseyeur. Le portrait publié sur Vercel et l'accueil de la version d'essai se chargent correctement.

## Retour arrière

Version d'essai précédente : `e07963ec9235ccca859fea957c4d7b2a3b064271`. Restaurer ce déploiement ou annuler le commit de cette correction. Aucun changement de format de sauvegarde, aucune suppression des anciens portraits, aucune publication en production.

