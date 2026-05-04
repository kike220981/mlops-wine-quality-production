from fastapi.testclient import TestClient
from src.api.app import app
import os

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_predict():
    # Solo testeamos si el modelo existe tras la preparación del workflow[cite: 1]
    payload = {
        "fixed_acidity": 7.0, "volatile_acidity": 0.3, "citric_acid": 0.3,
        "residual_sugar": 1.0, "chlorides": 0.04, "free_sulfur_dioxide": 10.0,
        "total_sulfur_dioxide": 30.0, "density": 0.99, "pH": 3.2,
        "sulphates": 0.5, "alcohol": 10.0
    }
    response = client.post("/predict", json=payload)
    # Si el modelo se generó en el paso previo del Action, esto dará 200
    assert response.status_code == 200