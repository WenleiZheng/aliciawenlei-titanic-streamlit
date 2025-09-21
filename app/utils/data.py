import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    # Basic cleaning: fill Age missing values with median
    if "Age" in df.columns:
        df["Age"] = df["Age"].fillna(df["Age"].median())
    return df
