from fastapi import FastAPI
import joblib
import numpy as np

from pydantic import BaseModel
from typing import List

from app.database import SessionLocal
from app.db_models import TransactionRecord

app = FastAPI()

# loading trained model - 
model = joblib.load("saved_models/xgboost_fraud_model.pkl")

# requesting schema - 
class Transaction(BaseModel):
    features:List[float]
 
# home route - 
@app.get("/")
def home():
    return {"message" : "Fraud Detection API Running"}


# prediction endpoint - 
@app.post("/predict")
def predict(transaction : Transaction):

    data = np.array(transaction.features).reshape(1, -1)
    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]

    # Database connection
    db = SessionLocal()

    try:
        record = TransactionRecord(
            features=transaction.features,
            prediction=int(prediction),
            probability=float(probability)
        )

        db.add(record)
        db.commit()

    finally:
        db.close()
    
    return {
        "fraud_prediction" : int(prediction),
        "fraud_probability" : float(probability)
    }


