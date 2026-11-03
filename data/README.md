# Format de données

Le fichier `modele_mesure.csv` est un **gabarit de colonnes, sans mesures**.

Colonnes :
- `timestamp_utc` : ISO 8601 avec fuseau
- `configuration` : A, B ou contrôle
- `theta_rad` : angle observé, radians
- `theta_unc_rad` : incertitude-type de lecture, radians
- `temperature_K` : température
- `notes` : événement ou remarque

Conserver séparément la calibration de l'angle, les dimensions et positions, masses, propriétés du fil et incertitudes corrélées. Ne jamais remplacer une donnée manquante par une valeur inventée.
