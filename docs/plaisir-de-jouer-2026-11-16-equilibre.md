# Équilibre des filières — 16 novembre 2026

Demande : « joue plus longtemps pour voir tous les types de culture, d'élevage, de reventes, la
gestion du bois et de la pêche. Et ajuste tout ça. »

## Ce qui a été joué

Banc local, horloge accélérée (une heure de jeu en moins d'une minute), mode libre, engins
débloqués, automatisation du jeu. Trente minutes de jeu par relevé. Ce n'est PAS une campagne
jouée à la main de bout en bout : les productions tournent pour de vrai (labour, semis, moisson,
coupe, pêche, traite, ponte, croissance des bêtes), les ventes sont calculées au prix de vente libre.

| filière | relevé avant | en € / min |
|---|---|---:|
| blé, une parcelle de départ automatisée | 144 kg par cycle de ~5,5 min | ~60 |
| bois (abatteuse) | dépôt plein (1 158 kg) en moins de 5 min, forêt repoussée | ~600 |
| chalutier | 92 kg / min | ~310 |
| caseyeur | 40 kg / min | ~250 |
| 2 vaches (lait) | 10 L / min | ~21 |
| 6 poules (œufs) | 0,29 kg / min | ~4 |
| revente : 2 vaches achetées 1 200 €, 6 kg de grain, 6 min | 7 000 € à la boucherie | ~970 par étable de 2 places |

## Ce qui a été ajusté

- **Revente des bêtes** : vache 3 500 → 760 €, cochon 1 640 → 480, brebis 1 560 → 250, poule 270 → 44
  (`prixBete` et lignes `betail_*`). C'était la faille : une étable de vingt places valait 58 000 €
  toutes les six minutes.
- **Cultures** : `RENDEMENT` 1,25 → 1,6 ; trémie de la moissonneuse 150/250/450 → 200/320/500 ;
  le silo suit (`siloMax` × `RENDEMENT`). Blé automatisé : ~80 € / min la parcelle.
- **Terres** : la grille s'arrête à 40 000 € la parcelle standard et se paie au prorata de la
  surface. Total ~1,1 M€ → ~520 000 €. Les petits carrés de 20 × 20 ne coûtent plus 27 000 / 162 000 €.
- **Bois** : grumes 2,60 → 1,90 € / kg.
- **Œufs** : 0,80 → 1,20 € pièce (les pâtisseries suivent, leur prix est dérivé).
- Pêche et lait : inchangés.

## Ce qui n'a pas été joué

La transformation (moulin, fromagerie, cave, huilerie), la vigne et les oliviers, les commandes
d'après campagne et la campagne complète mission par mission. Les 16 suites de tests passent.

## La marche entre la campagne et l'après

Demande : éviter « le paiement très bénéfique pendant la campagne » puis « des gains trop réduits »
une fois la campagne finie.

Relevé (400 commandes tirées au palier 20, ferme d'essai : 8 parcelles, 5 élevages au premier
cran, pas d'atelier) : commande médiane 3 230 € tout compris, 10 % à plus de 8 000 € ; les dix
dernières missions payaient 8 250 à 30 000 € de prime.

- Primes de mission : 3 000 premiers euros pleins, moitié du reste (`PRIME_PLEINE`, `PRIME_RESTE`).
  19 500 → 11 250, 30 000 → 16 500 ; rien ne change sous 3 000 €.
- Commandes : valeur visée × 1,8 (`APRES_CAMPAGNE`), prime × 1,4 (`PRIME_COMMANDE`).
  Même ferme d'essai après réglage : médiane 4 220 €, 10 % à plus de 13 100 €.

Non vérifié : que chaque achat obligatoire de la campagne reste finançable avec les primes
réduites (l'audit de septembre laissait 146 763 € de marge ; la baisse en retire environ 60 000,
et les terres coûtent moins cher). La vente libre se ferme toujours à la fin de la campagne.

## Le mode Négoce (première version)

Bouton « Négoce » à l'écran titre, sauvegarde à part (`moisson.partie.negoce.v1`, cours dans
`moisson.negoce.v1`). C'est un mode libre où aucun commerce n'achète : onglet « Marché » dans le
menu, un cours par produit (65 à 155 % du barème, nouveau cap toutes les 100 à 200 s, la vente
pèse sur le cours), bouton « Vendre » qui appelle un camion (1 500 kg au plus) ; il s'arrête
devant l'entrepôt, charge silo + entrepôt + quai de l'atelier, paie au prix du moment de l'appel.
Ni tutoriel, ni leçons, ni personnage. Le garage et le comptoir vendent toujours.
Non fait : vente des bêtes, camion qui évite le joueur et le trafic, onglet « Campagne » masqué.

## Trace du semoir et champs du Négoce (soir du 16)

- **Trace du semoir** : une image sur six ou sept ne peignait rien (le semoir sème la colonne de
  devant en avance, puis n'a plus que du déjà-semé sous lui : `eligible` tombait). Une cellule
  semée par ce passage depuis moins de 0,6 s compte maintenant pour peindre. Vérifié vu de
  dessus au banc, avant / après. Au passage : direction de secours quand l'outil n'a pas bougé,
  graines comptées au mètre et non à l'image.
- **Négoce** : bandeau « BLÉ MÛR – PARCELLE N À MOISSONNER » une fois par maturité, et section
  « Champs » dans l'onglet Marché (barre de pousse par parcelle). La jauge au-dessus du champ ne
  s'affiche toujours qu'à ~60 m de la parcelle, dans tous les modes.
