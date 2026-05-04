import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib
import os

def ejecutar_preprocesamiento():
    print("Iniciando preprocesamiento...")
    
    # 1. Leer el archivo descargado por ingesta.py
    df = pd.read_csv('src/data/raw_data.csv')
    
    # 2. Definir X e y
    X = df.drop('quality', axis=1)
    y = (df['quality'] > 6).astype(int) # 1 si es bueno, 0 si no
    
    # 3. Dividir datos
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 4. Escalar
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # 5. GUARDAR ARCHIVOS (Asegúrate de que estas rutas coincidan con entrenamiento.py)
    os.makedirs('src/data', exist_ok=True)
    os.makedirs('src/models', exist_ok=True)
    
    pd.DataFrame(X_train_scaled, columns=X.columns).to_csv('src/data/X_train.csv', index=False)
    pd.DataFrame(X_test_scaled, columns=X.columns).to_csv('src/data/X_test.csv', index=False)
    y_train.to_csv('src/data/y_train.csv', index=False)
    y_test.to_csv('src/data/y_test.csv', index=False)
    
    # Guardar el escalador para la API
    joblib.dump(scaler, 'src/models/scaler.joblib')
    print("Archivos de preprocesamiento creados con éxito.")

if __name__ == "__main__":
    ejecutar_preprocesamiento()