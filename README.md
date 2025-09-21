![CI](https://github.com/aliciawenlei/titanic-streamlit/actions/workflows/ci.yml/badge.svg)
# Titanic Survival — Streamlit Demo

## Run locally
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest -q
streamlit run app/app.py
# open http://localhost:8501
```
## Docker
```bash
docker build -t titanic-app .
docker run --rm -p 8501:8501 titanic-app
# open http://localhost:8501
```
