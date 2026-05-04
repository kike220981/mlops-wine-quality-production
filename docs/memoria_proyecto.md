## 1. Memoria Técnica: Sistema de Predicción de Calidad de Vino (MLOps)
### 1. Introducción
Este proyecto implementa un ciclo de vida completo de Machine Learning (MLOps) para predecir la calidad del vino tinto. El objetivo es demostrar la capacidad de integrar ingeniería de datos, modelado predictivo y despliegue continuo (CI/CD) bajo una metodología ágil de desarrollo.

### 2. Metodología de Gestión (Agile/Scrum)
El desarrollo se ha estructurado en un Product Backlog de 6 User Stories, ejecutadas en tres iteraciones temporales (Sprints):

Sprint 1: Cimentación de Datos: Ingesta automatizada y normalización de cabeceras (snake_case) para asegurar la integridad del pipeline.

Sprint 2: Modelado y Calidad: Entrenamiento con RandomForestClassifier y validación exhaustiva con una cobertura de tests del 92.5%.

Sprint 3: Despliegue e Infraestructura: Desarrollo de la API con FastAPI, contenedorización con Docker y provisión de infraestructura con Terraform.

### 3. Arquitectura del Sistema
El sistema se divide en cuatro fases modulares:

Ingesta: Descarga y normalización desde UCI Machine Learning.

Preprocesamiento: Limpieza y escalado mediante StandardScaler.

Entrenamiento: Generación de artefactos .joblib e informes de métricas JSON.

Servicio de API: Interfaz FastAPI para predicciones en tiempo real (POST).

### 4. Integración y Despliegue Continuo (CI/CD)
Se ha configurado un flujo en GitHub Actions que garantiza la calidad en cada push:

Validación de entorno y dependencias.

Ejecución del pipeline de datos.

Pruebas unitarias y de integración con pytest (Cobertura alcanzada: 92.5%).
