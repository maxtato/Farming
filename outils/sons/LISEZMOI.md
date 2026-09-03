# Les sons du jeu

Le joueur envoie les sons ; ils entrent dans le jeu par la même porte que les deux moteurs :
un WAV 16 bits mono, rééchantillonné bas, en base64 dans la table `SONS` de `index.html`.

- `sons.json` — la table : pour chaque clé, le fichier envoyé (`src`), la fréquence retenue
  (`hz`, la moitié de ce que le son a de plus aigu), la crête (`crete`), les bornes (`debut`, `fin`).
- `node encoder.js [cle…]` — Chromium décode le fichier (MP3, WAV, OGG…), le rééchantillonne,
  le met en mono, le ramène à la crête, et écrit `<cle>.b64`. Il dit ce qu'il a fait.
- `python3 poser.py [cle…]` — pose chaque `.b64` dans la table `SONS` du jeu.

Les fichiers envoyés restent dans le dossier des envois (`U` dans `encoder.js`), pas ici :
ils ne sont pas à nous.
