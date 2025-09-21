from app.utils.data import load_data
from app.model import train_model, predict

def test_model_predict():
    df = load_data("data/titanic.csv")
    model = train_model(df)
    prob = predict(model, 3, 22, 1, 7.25)
    assert 0.0 <= prob <= 1.0
