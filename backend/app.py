from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

ML_URL = "https://ml-1-e6yo.onrender.com/predict"

# Allow frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://ml-3-dur5.onrender.com/"],  # frontend URL
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

    response = requests.post(ML_URL, json={"value": value})
    return response.json()