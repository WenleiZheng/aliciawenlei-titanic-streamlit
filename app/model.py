import pandas as pd
from sklearn.linear_model import LogisticRegression

def train_model(df: pd.DataFrame):
    # Minimal feature set for demo purposes
    features = ["Pclass", "Age", "SibSp", "Fare"]
    X = df[features]
    y = df["Survived"]
    model = LogisticRegression(max_iter=200)
    model.fit(X, y)
    return model

def predict(model, pclass, age, sibsp, fare):
    X_new = pd.DataFrame([[pclass, age, sibsp, fare]],
                         columns=["Pclass", "Age", "SibSp", "Fare"])
    return model.predict_proba(X_new)[0, 1]  # survival probability
