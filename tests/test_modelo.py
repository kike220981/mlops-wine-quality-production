import joblib
import os

def test_model_exists():
    # Verifica que el entrenamiento generó el archivo .joblib
    model_path = "src/models/modelo_vino.joblib"
    assert os.path.exists(model_path), "El modelo no fue generado en el entrenamiento"

def test_model_prediction_logic():
    model_path = "src/models/modelo_vino.joblib"
    if os.path.exists(model_path):
        model = joblib.load(model_path)
        # Definimos los nombres de las columnas para evitar el UserWarning
        cols = ["fixed_acidity", "volatile_acidity", "citric_acid", "residual_sugar", 
                "chlorides", "free_sulfur_dioxide", "total_sulfur_dioxide", 
                "density", "pH", "sulphates", "alcohol"]
        dummy_input = pd.DataFrame([[7.4, 0.7, 0.0, 1.9, 0.076, 11.0, 34.0, 0.9978, 3.51, 0.56, 9.4]], 
                                   columns=cols)
        prediction = model.predict(dummy_input)
        assert len(prediction) == 1