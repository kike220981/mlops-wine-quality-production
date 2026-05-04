import pandas as pd
import joblib
from sklearn.metrics import classification_report
import json

def ejecutar_evaluacion():
    X_test = pd.read_csv('src/data/X_test.csv')
    y_test = pd.read_csv('src/data/y_test.csv')
    
    model = joblib.load('src/models/modelo_vino.joblib')
    predictions = model.predict(X_test)
    
    report = classification_report(y_test, predictions, output_dict=True)
    
    with open('src/models/metrics.json', 'w') as f:
        json.dump(report, f)
    print("Evaluación completada. Métricas guardadas en src/models/metrics.json")

if __name__ == "__main__":
    ejecutar_evaluacion()