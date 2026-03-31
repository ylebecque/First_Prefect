# Votre premier script Prefect

Ce dossier contient un pipeline Prefect permettant d'interroger une API pour générer aléatoirement les informations d'utilisateurs.

## Les tâches

Le pipeline est composé de trois tâches :
* **fetch_data()** : interroge une API pour récupérer les informations nécessaires
* **transform_data()** : transforme les données en filtrant les résultats en fonction de l'âge
* **save_data()** : enregistre les données sous forme d'un fichier CSV

## Le flow

Le pipeline appelle les trois tâches ci-dessus l'une après l'autre.

## L'exécution du pipeline

Pour exécuter le pipeline, vous pouvez taper la commande suivante dans le terminal :
`uv run python3 main.py`

Cela générera le fichier `output.csv`dans le dossier où vous vous trouvez, contenant les données récupérées sur l'API et filtrées.
