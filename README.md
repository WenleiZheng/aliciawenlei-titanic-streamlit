# Titanic Survival — Streamlit Demo 🚢

[![CI](https://github.com/WenleiZheng/aliciawenlei-titanic-streamlit/actions/workflows/ci.yml/badge.svg)](https://github.com/WenleiZheng/aliciawenlei-titanic-streamlit/actions/workflows/ci.yml)

A demo project for Titanic survival prediction using **Streamlit**.  
Includes:
- Data loading and filtering functions (with tests ✅)
- Logistic regression model for survival prediction
- Containerized with Docker
- CI pipeline via GitHub Actions

## Run locally
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest -q
streamlit run app/main.py
# open http://localhost:8501
```
## Docker
```bash
docker build -t titanic-app .
docker run --rm -p 8501:8501 titanic-app
# open http://localhost:8501
```
