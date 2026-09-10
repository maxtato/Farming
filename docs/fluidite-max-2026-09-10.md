# Qualité maximale : partage des sommets

Les géométries regroupées conservent les indices des primitives au lieu de déplier chaque triangle. Les variantes de couleur du trafic reprennent aussi ces indices. Positions, normales, couleurs, ordre des triangles et silhouettes restent inchangés. Résolution native, grain 1, densité des cultures, textures, ombres PCF et fréquence de simulation sont conservés.

Mesure sur les 370 modèles regroupés lors de la construction du monde :

| Donnée cumulée de construction | Avant | Après |
|---|---:|---:|
| Sommets stockés | 504 090 | 318 047 |
| Octets des positions, normales, couleurs et indices | 18 147 240 | 12 401 232 |

Cela représente 36,9 % de sommets et 31,7 % de stockage en moins pour ces modèles. Ce cumul inclut des géométries intermédiaires : ce n'est pas une mesure de la mémoire totale du jeu ni de la mémoire GPU résidente. Le nombre de triangles n'est pas réduit.

Validation : construction réussie et 221 tests réussis, dont cinq nouveaux contrôles des indices (mélange de primitives, transformations, indices clairsemés, grands modèles, géométries sans indices). Le banc utilisant le vrai moteur compare les positions, normales et couleurs dépliées des 370 modèles à la fonction originale : aucune différence.

Six rendus à 1280 × 720 sont comparés avec et sans partage des sommets : blés, grands champs, village, forêt, port, village de nuit. Aucun pixel différent dans ces six vues. Le banc ne transforme que les géométries concernées ; transformer aussi les géométries natives du moteur donnait des écarts sans rapport avec la modification.

Un trajet déterministe de 480 images, toutes les parcelles plantées, termine à la même position et au même cap : x=-10.75805473243297, z=26.651585825744643, cap=1.2643477975679722. Même rendu final de 67 410 triangles et 237 appels, aucun message d'erreur. Coût moyen instrumenté des 420 dernières images : 24,94 ms avant et 17,43 ms après. Les lectures d'horloge et les images exécutées par lots perturbent cette mesure ; elle ne constitue pas un relevé des FPS en conditions normales.

Les mesures de rendu synchronisé varient fortement entre passages et selon la scène. Les champs bénéficient du partage ; les autres scènes n'affichent pas un gain systématique. Aucun engagement de 60 images/seconde sur tous les téléphones. Prochaines pistes à mesurer séparément : regroupements supplémentaires de détails compatibles, mises à jour inutiles des transformations et téléversements de textures lors du travail des champs. Aucune baisse de qualité automatique ajoutée.

Production de référence conservée : 087bdbea43fecec537716796384275f857ef09fc. Publication de cette modification limitée à la branche d'essai codex/arcade-preview-20260907.
