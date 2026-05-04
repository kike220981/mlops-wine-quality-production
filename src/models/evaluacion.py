import pandas as pd
import joblib
from sklearn.metrics import classification_report
import json
import os

def ejecutar_evaluacion():
    print("Iniciando evaluación...")
    
    # Cargar datos de test y modelo
    X_test = pd.read_csv('src/data/X_test.csv')
    y_test = pd.read_csv('src/data/y_test.csv')
    model = joblib.load('src/models/modelo_vino.joblib')
    
    # Predecir y evaluar
    y_pred = model.predict(X_test)
    reporte = classification_report(y_test, y_pred, output_dict=True)
    
    # Guardar métricas en JSON (formato estándar MLOps)
    with open('src/models/metrics.json', 'w') as f:
        json.dump(reporte, f, indent=4)
    
    print("Evaluación finalizada. Informe guardado en src/models/metrics.json")

if __name__ == "__main__":
    ejecutar_evaluacion()