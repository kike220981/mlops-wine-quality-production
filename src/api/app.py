from fastapi import FastAPI, HTTPException
import joblib
import pandas as pd
from src.api.schemas import WineData
import os

app = FastAPI(title="Wine Quality API", description="API de producción para MLOps[cite: 2]")

# Rutas de los artefactos generados por el pipeline
MODEL_PATH = "src/models/modelo_vino.joblib"
SCALER_PATH = "src/models/scaler.joblib"

@app.get("/")
def home():
    return {"status": "online", "message": "MLOps Wine Quality API funcionando[cite: 1]"}

@app.post("/predict")
def predict(data: WineData):
    # 1. Verificar si existen el modelo y el escalador
    if not os.path.exists(MODEL_PATH) or not os.path.exists(SCALER_PATH):
        raise HTTPException(status_code=503, detail="Modelo no disponible. Ejecute el entrenamiento primero.[cite: 1]")
    
    try:
        # 2. Cargar artefactos
        model = joblib.load(MODEL_PATH)
        scaler = joblib.load(SCALER_PATH)
        
        # 3. Convertir input a DataFrame
        df_input = pd.DataFrame([data.dict().values()], columns=data.dict().keys())
        
        # 4. Escalar y Predecir[cite: 1]
        X_scaled = scaler.transform(df_input)
        prediction = model.predict(X_scaled)
        
        return {
            "prediction": int(prediction[0]),
            "label": "Alta Calidad" if prediction[0] == 1 else "Calidad Estándar"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))