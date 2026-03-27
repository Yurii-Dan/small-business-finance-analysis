import pandas as pd
import os


def load_transactions_data():

    base_path = os.path.dirname(__file__)
    data_path = os.path.join(base_path, "..", "data", "transactions.csv")

    df = pd.read_csv(data_path)

    # cleaning
    df["date"] = pd.to_datetime(df["date"])
    df["category"] = df["category"].astype("category")

    return df
