import joblib
import os
import pandas as pd

def test_model_exists():
    model_path = "src/models/modelo_vino.joblib"
    assert os.path.exists(model_path)

def test_model_prediction_logic():
    model_path = "src/models/modelo_vino.joblib"
    if os.path.exists(model_path):
        model = joblib.load(model_path)
        # Nombres exactos del dataset original de UCI
        cols = ["fixed_acidity", "volatile_acidity", "citric_acid", "residual_sugar", 
                "chlorides", "free_sulfur_dioxide", "total_sulfur_dioxide", 
                "density", "pH", "sulphates", "alcohol"]
        
        # Creamos un ejemplo con los nombres de columna correctos
        dummy_input = pd.DataFrame([[7.4, 0.7, 0.0, 1.9, 0.076, 11.0, 34.0, 0.9978, 3.51, 0.56, 9.4]], 
                                   columns=cols)
        
        prediction = model.predict(dummy_input)
        assert len(prediction) == 1