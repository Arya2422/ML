from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import os

app = FastAPI()

ML_URL = os.getenv("ML_URL")  # 👈 from env

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Backend Running"}

@app.post("/predict")
def predict(data: dict):
    value = data.get("value")

    if value is None:
        return {"error": "value is required"}

    try:
        response = requests.post(ML_URL, json={"value": value}, timeout=5)
        return response.json()
    except Exception as e:
        return {"error": str(e)}