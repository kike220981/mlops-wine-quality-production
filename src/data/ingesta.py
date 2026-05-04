import pandas as pd
import os

def ejecutar_ingesta():
    print("Iniciando descarga de datos...")
    
    # URL oficial del dataset de vino tinto (UCI Machine Learning Repository)
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
    
    try:
        # Los datos vienen separados por punto y coma (;)
        df = pd.read_csv(url, sep=';')
        
        # Asegurar que la carpeta existe
        os.makedirs('src/data', exist_ok=True)
        
        # Guardar como CSV estándar para el resto del pipeline
        df.to_csv('src/data/raw_data.csv', index=False)
        print(f"Ingesta completada: {len(df)} registros guardados en src/data/raw_data.csv")
        
    except Exception as e:
        print(f"Error en la ingesta: {e}")

if __name__ == "__main__":
    ejecutar_ingesta()