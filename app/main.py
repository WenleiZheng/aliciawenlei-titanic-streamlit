import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from app.utils.data import load_data
from app.model import train_model, predict

st.set_page_config(page_title="Titanic Survival", page_icon="🚢", layout="wide")
st.title("🚢 Titanic Survival Prediction")

df = load_data("data/titanic.csv")
model = train_model(df)

st.write("### Preview")
st.dataframe(df.head())

st.write("### Predict survival for a passenger")
pclass = st.selectbox("Ticket Class (1=First, 3=Third)", [1, 2, 3], index=2)
age = st.slider("Age", 0, 80, 30)
sibsp = st.slider("Siblings/Spouses aboard", 0, 8, 0)
fare = st.slider("Fare", 0.0, 600.0, 50.0)

if st.button("Predict Survival Probability"):
    prob = predict(model, pclass, age, sibsp, fare)
    st.success(f"Predicted survival chance: {prob*100:.2f}%")
