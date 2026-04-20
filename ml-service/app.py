from fastapi import FastAPI
import joblib
import os

app = FastAPI()

MODEL_PATH = "model.pkl"

# Train if model not present
if not os.path.exists(MODEL_PATH):
    from train import train_model
    train_model()

model = joblib.load(MODEL_PATH)

@app.get("/")
def home():
    return {"message": "ML Service Running"}

@app.post("/predict")
def predict(data: dict):
    features = [[
        data["area"],
        data["bedrooms"],
        data["bathrooms"],
        data["age"]
    ]]

    prediction = model.predict(features)[0]

    return {
        "predicted_price": round(float(prediction), 2)
    }