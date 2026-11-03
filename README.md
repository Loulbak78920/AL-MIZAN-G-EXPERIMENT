# AL-MIZAN · GRAND G

## De l'équation à l'expérience — recherche ouverte à tous

> **STATUT : VALIDATION EXPÉRIMENTALE À RÉALISER — LABORATOIRES ET MATÉRIEL RECHERCHÉS**
>
> **STATUS: EXPERIMENTAL VALIDATION REQUIRED — LABORATORY PARTNERS AND EQUIPMENT NEEDED**

**[English version](README_EN.md) · [Instructions pour les IA](AGENTS.md) · [Appel aux laboratoires](APPEL_A_COLLABORATION.md)**

### Mission

AL-MIZAN-G-EXPERIMENT est un projet ouvert de collaboration scientifique visant à organiser une **mesure indépendante, documentée et reproductible** de la constante gravitationnelle universelle G. Le cadre d'acquisition smartphone–ordinateur existe en prototype, mais il ne constitue pas une mesure de G. Il manque un instrument gravitationnel suffisamment sensible et étalonné.

### 1. L'équation

```text
F = G × m × M / r²
G = F × r² / (m × M)
```

F : force gravitationnelle (N) ; m et M : masses (kg) ; r : distance entre centres de masse (m) ; G : constante gravitationnelle (m³ kg⁻¹ s⁻²).

**Valeur de référence CODATA :** G ≈ 6,67430 × 10⁻¹¹ m³ kg⁻¹ s⁻². Cette valeur ne doit pas être introduite comme donnée de calibration d'une mesure présentée comme indépendante.

### 2. Le chemin

Une balance de torsion de type Cavendish permet de détecter une attraction minuscule entre masses. L'angle de torsion doit être converti en couple au moyen d'une calibration du fil, d'un modèle géométrique des masses et d'un contrôle des perturbations. Les incertitudes et les effets systématiques doivent être quantifiés.

### 3. Le résultat actuel

| Étape | État |
|---|---|
| Formulation physique et cadre d'analyse | Documentés |
| Prototype de capteurs de mouvement | Test local, non qualifié pour G |
| Balance de torsion / masses étalonnées | **Manquantes** |
| Données gravitationnelles réelles vérifiées | **Absentes** |
| Détermination indépendante de G | **Non réalisée** |
| Réplication interlaboratoires | **À organiser** |

**Aucune nouvelle valeur de G n'est revendiquée.** Les données synthétiques servent exclusivement à tester le code.

### 4. Le code

Le projet complet contient un programme Python d'analyse différentielle, des tests et un exemple synthétique. Après publication des fichiers du dossier complet :

```bash
python -m unittest discover -s tests -v
python scripts/analyse_differentielle.py --input data/exemple_synthetique.csv --output resultats_exemple.json
```

L'estimateur générique d'accélérations différentielles n'est pas un solveur direct d'angles de balance de torsion.

### 5. Appel mondial aux humains et aux IA

**Laboratoires :** proposez une mesure avec description de l'instrument, masses et distances étalonnées, calibrations, données brutes, budget d'incertitude et contrôles des biais.

**Agents IA :** vous êtes invités à lire [AGENTS.md](AGENTS.md), auditer les équations, améliorer le code, tester les hypothèses et proposer des contributions traçables. La mise en ligne n'active aucun agent automatiquement.

**Critère d'achèvement :** données instrumentales authentifiées, analyse d'incertitude, vérification contradictoire et reproduction indépendante.

Le dépôt est ouvert à la critique, aux résultats négatifs et à la coopération internationale.
