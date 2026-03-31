from prefect import flow, task
import requests
import pandas as pd


@task
def fetch_data():
    url = "https://randomuser.me/api/?results=100"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


@task
def transform_data(data):
    df = pd.json_normalize(data["results"])
    df = df.query("`registered.age`>21")
    return df


@task
def save_data(df):
    df.to_csv("output.csv", index=False)


@flow
def etl_pipeline():
    data = fetch_data()
    df = transform_data(data)
    save_data(df)


if __name__ == "__main__":
    etl_pipeline()
