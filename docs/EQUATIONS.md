# Équations : de la force à la mesure

## Loi de Newton
```text
F = G m M / r²
G = F r² / (m M)
```
Unités SI : F en N ; masses en kg ; r en m ; G en m³ kg⁻¹ s⁻².

Cette formule ponctuelle ne suffit pas pour une vraie balance de Cavendish : les corps ont une taille, la force exerce un **couple** et l'instrument a une réponse dynamique.

## Balance de torsion
Pour un angle θ(t), un modèle mécanique simplifié est :
```text
I θ¨ + b θ˙ + κ θ = τ_grav(G, géométrie, masses) + τ_perturbations
```
I : inertie de rotation ; b : amortissement ; κ : raideur de torsion ; τ : couples.

La force gravitationnelle entre éléments de masse s'obtient en intégrant les contributions géométriques. Pour une géométrie fixe, le couple gravitationnel peut s'écrire :
```text
τ_grav = G K(positions, masses, dimensions)
```
K doit être calculé à partir de la géométrie réelle, et non choisi pour retrouver la valeur de référence.

## Mesures différentielles
Après calibration, une série de couples mesurés peut être modélisée :
```text
y_i = G k_i + b_i + ε_i
```
où k_i est calculé indépendamment, b_i représente les biais et ε_i le bruit.

Si les biais sont maîtrisés et si Σ est une covariance inversible :
```text
G_hat = (kᵀ Σ⁻¹ y) / (kᵀ Σ⁻¹ k)
u_stat²(G_hat) = 1 / (kᵀ Σ⁻¹ k)
```
Cette incertitude statistique ne comprend pas automatiquement les erreurs de calibration et de géométrie.

## Ce que l'équation ne démontre pas
Le simple réarrangement de F = GmM/r² n'est pas une prédiction nouvelle de G. Utiliser une masse terrestre inférée à partir de GM et de G serait circulaire. Il faut une mesure indépendante et une analyse des biais.
