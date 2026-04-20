from fastapi import FastAPI
import joblib

app = FastAPI()
model = joblib.load("model.pkl")

@app.post("/predict")
def predict(data: dict):
    value = data["value"]
    result = model.predict([[value]]).tolist()
    return {"prediction": result}