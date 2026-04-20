import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import joblib

def train_model():
    data = pd.DataFrame({
        "area": [1000,1500,2000,2500,3000,3500],
        "bedrooms": [2,3,3,4,4,5],
        "bathrooms": [1,2,2,3,3,4],
        "age": [10,5,8,2,1,0],
        "price": [50,80,120,200,250,300]
    })

    X = data[["area","bedrooms","bathrooms","age"]]
    y = data["price"]

    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("model", RandomForestRegressor(n_estimators=200))
    ])

    pipeline.fit(X, y)
    joblib.dump(pipeline, "model.pkl")

if __name__ == "__main__":
    train_model()