from app.utils.data import load_data

def test_load_data():
    df = load_data("data/titanic.csv")
    assert "Age" in df.columns
    # Age should be imputed (no missing values)
    assert df["Age"].isna().sum() == 0
