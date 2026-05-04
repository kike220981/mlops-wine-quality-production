import joblib
import os

def test_model_exists():
    # Verifica que el entrenamiento generó el archivo .joblib
    model_path = "src/models/modelo_vino.joblib"
    assert os.path.exists(model_path), "El modelo no fue generado en el entrenamiento"

def test_model_prediction_logic():
    # Verifica que el modelo cargado puede predecir
    model_path = "src/models/modelo_vino.joblib"
    if os.path.exists(model_path):
        model = joblib.load(model_path)
        # Probamos con un dummy de 11 columnas (características del vino)
        dummy_input = [[7.4, 0.7, 0.0, 1.9, 0.076, 11.0, 34.0, 0.9978, 3.51, 0.56, 9.4]]
        prediction = model.predict(dummy_input)
        assert len(prediction) == 1