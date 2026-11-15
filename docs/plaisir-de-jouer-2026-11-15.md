# Le plaisir de jouer — 15 novembre 2026

Branche `claude/moisson-gains-defis`, partie de `codex/arcade-preview-20260907` (commit `d58bd6e`).
Tout le code est dans le chapitre **29 bis** d'`index.html`, plus quatre accroches d'une ligne
(boucle, aiguillage du menu, bandeau de la caisse, réglage des vibrations).

## Ce qui change pour le joueur

- **La caisse bouge.** Le solde défile jusqu'à sa nouvelle valeur, bat quand il monte, et une
  étiquette dit de combien : jaune « + 128 € » pour ce qui rentre, sombre « − 650 € » pour un achat.
  Un grelot monte d'un degré pendant qu'on décharge. Vibration courte (Android ; réglable).
- **Un palier se fête** : bandeau « NIVEAU n », carillon, pluie de pièces. Aucune fenêtre, aucune pause.
- **Défis du jour** (menu → Défis) : trois par jour de calendrier, tirés de la date, à la mesure du
  palier. Un défi de produit n'apparaît que si la ferme en a déjà sorti. Prime + XP, et une prime
  « journée pleine » pour les trois.
- **Fidélité** : série de jours joués ; prime du jour à partir du deuxième jour, plafonnée au septième.
- **Records et carnet** : plus grosse vente d'un arrêt, meilleure journée, cumul encaissé, kilomètres,
  commandes honorées.
- **Retour** : les cultures semées poussent pendant l'absence (vingt minutes de jeu au plus). Après
  trente minutes d'absence, une page « BON RETOUR » résume série, défis et cultures mûres.

## Garde-fous

- **Aucune prime ne tombe seule.** Défis, journée pleine et fidélité s'encaissent d'un toucher dans
  l'onglet. La pastille jaune du bouton de menu signale qu'il y a quelque chose à prendre.
- **Rien pendant le tutoriel** : ni défis, ni prime, ni page de retour.
- **La sauvegarde de la partie n'est pas modifiée.** L'état vit sous `moisson.plaisir.v1` : il
  appartient au joueur et survit à « Nouvelle campagne ».
- **Les fonctions découpées par les bancs sont intactes.** `encaisser` et `solderContrat` sont
  enveloppées à l'exécution, pas réécrites.
- Seules les cultures avancent hors ligne : bêtes, ateliers et étals consomment, on ne dépense rien
  à la place d'un joueur absent.

## Réglages à surveiller en jouant

| Réglage | Valeur | Où |
|---|---|---|
| Prime d'un défi | 35 € × palier × poids, 30 € au moins | `plaisirTirer` |
| XP d'un défi | (3 + palier) × poids | `plaisirTirer` |
| Prime de fidélité | 20 € × palier × jours (7 au plus) | `primeFidelite` |
| Journée pleine | moitié des trois primes | `primePleine` |
| Pousse hors ligne | 20 min au plus | `ABSENCE_POUSSE_MAX` |

Ces montants n'ont pas été éprouvés sur de longues parties : ils sont volontairement modestes face aux
primes de mission (150 € à la première, 4 000 € et plus au palier 8).

## Vérification

13 contrôles dans `outils/plaisir/tests.cjs`, ajoutés à `npm test`. Contrôle visuel dans Chromium en
844 × 390 et 667 × 375. Les vibrations et le rendu sur un vrai téléphone restent à valider.

## Passe propreté (même jour)

Un audit a joué le début de la campagne en 844 × 390 et 667 × 375 : 23 constats, aucune erreur JS.
Corrigé ici :

- **« Nouvelle campagne » demande deux touchers** ; un seul effaçait la partie, contre « Reprendre ».
- **La pause se voit** : voile, mot, bouton passé en ▶ ; toucher l'écran la lève.
- Libellé du palier sur fond sombre (illisible sur le blé mûr) ; titre « Que faire ici ? » lisible ;
  nom des flèches de guidage de 7 à 9 px.
- **Cibles tactiles élargies sans grossir les boutons** : boutons des listes, flèche des dialogues,
  croix de la liste des engins, barre de progression.
- Bouton du garage « Voir le catalogue » au lieu de « Rien à vendre à ce palier » ; accord
  « charrue … attelée » ; guillemet fermant insécable dans « Un héritage ».

Relevé mais NON corrigé, à trancher : outils de développement et « Tout déverrouiller » visibles dans
les réglages ; étiquettes du monde qui passent sous le HUD ; écran d'automatisation (lignes coupées,
mini-carte, consignes en triple, onglets verrouillés non grisés) ; vocabulaire mission / commande /
contrat et niveau / palier / cran ; tutoiement et vouvoiement mêlés ; étape de labour bloquée sous
98 % sans montrer le reliquat ; bandeau « plan terminé » pendant que le chantier continue.
