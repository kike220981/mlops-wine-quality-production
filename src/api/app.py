from fastapi import FastAPI, HTTPException
import joblib
import pandas as pd
from src.api.schemas import WineData
import os

app = FastAPI(title="Wine Quality API")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MODEL_PATH = os.path.join(BASE_DIR, "src", "models", "modelo_vino.joblib")
SCALER_PATH = os.path.join(BASE_DIR, "src", "models", "scaler.joblib")

@app.get("/")
def home():
    return {"status": "online", "message": "MLOps Wine Quality API funcionando"}

@app.post("/predict")
def predict(data: WineData):
    if not os.path.exists(MODEL_PATH) or not os.path.exists(SCALER_PATH):
        raise HTTPException(status_code=503, detail="Modelo o escalador no disponible")
    
    try:
        model = joblib.load(MODEL_PATH)
        scaler = joblib.load(SCALER_PATH)
        
        cols = ["fixed_acidity", "volatile_acidity", "citric_acid", "residual_sugar", 
                "chlorides", "free_sulfur_dioxide", "total_sulfur_dioxide", 
                "density", "pH", "sulphates", "alcohol"]
        
        data_dict = data.model_dump()
        df_input = pd.DataFrame([data_dict])[cols]
        
        X_scaled = scaler.transform(df_input)
        prediction = model.predict(X_scaled)
        
        return {
            "prediction": int(prediction[0]),
            "label": "Alta Calidad" if prediction[0] == 1 else "Calidad Estándar"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))