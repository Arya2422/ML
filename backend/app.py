from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv

load_dotenv()  

app = FastAPI()

ML_URL = os.getenv("ML_URL")

class HouseInput(BaseModel):
    area: float
    bedrooms: int
    bathrooms: int
    age: int

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # restrict later
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Backend Running"}

@app.post("/predict")
def predict(data: HouseInput):
    try:
        response = requests.post(
            f"{ML_URL}/predict",
            json=data.dict(),
            timeout=5
        )
        return response.json()
    except Exception as e:
        return {"error": str(e)}