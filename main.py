from prefect import flow, task
import requests
import pandas as pd


@task
def fetch_data():
    url = "https://randomuser.me/api/?results=10"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Erreur lors de la récupération des données : {response.status_code}"


@task
def transform_data(data):
    try:
        df = pd.json_normalize(data["results"])
        df = df.query("`registered.age`>18")
        return df
    except Exception as e:
        return f"Erreur lors de la transformation des données : {e}"


@task
def save_data(df):
    df.to_csv("output.csv", index=False)
    return "Data saved to output.csv"


@flow
def etl_pipeline():
    try:
        data = fetch_data()
        df = transform_data(data)
        result = save_data(df)
        return result
    except Exception as e:
        return f"Erreur durant l'exécution du pipeline : {e}"


if __name__ == "__main__":
    etl_pipeline()
