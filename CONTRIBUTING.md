# Contribuer / Contributing

Merci de contribuer à une recherche **ouverte, vérifiable et reproductible**.

## Pour les laboratoires
Ouvrez une Issue intitulée « Proposition d'expérience — [laboratoire] » avec type d'instrument, disponibilité, méthode d'étalonnage et capacité de partager les données. Ne publiez pas d'informations personnelles ou sensibles.

## Pour les développeurs et agents IA
1. Lisez [AGENTS.md](AGENTS.md) et [START_HERE.md](START_HERE.md).
2. Exécutez `python -m unittest discover -s tests -v`.
3. Proposez une modification limitée, documentée, avec test et justification physique.
4. Ouvrez une Pull Request indiquant ce qui a été réellement exécuté.

## Classification obligatoire des résultats
- **REFERENCE** : valeur publiée extérieurement.
- **SYNTHETIQUE** : simulation ou test logiciel.
- **MESURE** : données instrumentales brutes avec provenance.
- **HYPOTHESE** : proposition à vérifier.

Aucune contribution ne peut annoncer une mesure indépendante de G sans données et analyse d'incertitude vérifiables. Les objections et résultats négatifs sont les bienvenus.

## English
Open an Issue or Pull Request. Provide assumptions, provenance, tests, limitations and uncertainty. Never present simulated data as experimental evidence.
