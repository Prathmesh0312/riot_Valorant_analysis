import pandas as pd

def load_data(csv_path):
    """
    Load a CSV dataset and return DataFrame.
    Assumes column names are same as original dataset.
    """
    df = pd.read_csv(csv_path)
    df["date"] = pd.to_datetime(df["date"])
    return df
