import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

def ejecutar_entrenamiento():
    print("Iniciando entrenamiento...")
    
    # Cargar datos preprocesados
    X_train = pd.read_csv('src/data/X_train.csv')
    y_train = pd.read_csv('src/data/y_train.csv').values.ravel()
    
    # Configurar y entrenar el modelo
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Asegurar que la carpeta existe
    os.makedirs('src/models', exist_ok=True)
    
    # Guardar modelo
    joblib.dump(model, 'src/models/modelo_vino.joblib')
    print("Modelo guardado en src/models/modelo_vino.joblib")

if __name__ == "__main__":
    ejecutar_entrenamiento()