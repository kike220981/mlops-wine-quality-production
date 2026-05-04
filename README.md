# MLOps Wine Quality Production 🍷

Este proyecto implementa un pipeline completo de MLOps para la clasificación de la calidad del vino tinto, siguiendo los estándares de la asignatura **Metodologías de Desarrollo y Despliegue de Aplicaciones para Ciencia de Datos**.

---

## 🚀 Objetivo

Diseñar e implementar un ciclo de vida de Machine Learning automatizado que incluya:

* Ingesta de datos
* Entrenamiento con trazabilidad
* Pruebas de calidad
* Despliegue mediante contenedores

---

## 🛠️ Stack Tecnológico

* **Lenguaje:** Python 3.9+
* **ML Framework:** Scikit-learn
* **API:** FastAPI con validación Pydantic V2
* **Contenedores:** Docker (estrategia separada para API y entrenamiento)
* **CI/CD:** GitHub Actions (workflow automatizado)
* **IaC:** Terraform (despliegue en AWS EC2)
* **Gestión:** Metodología Ágil con GitHub Projects (Kanban)

---

## 📁 Estructura del Proyecto

Basada en estándares industriales para Ciencia de Datos:

```
src/
  data/           # Ingesta y normalización de datos
  models/         # Entrenamiento y artefactos (.joblib)
  api/            # API para predicciones
infrastructure/   # Terraform (IaC)
tests/            # Tests unitarios e integración
.github/workflows/ # CI/CD
```

---

## ⚙️ Instalación y Uso Local

### 1. Clonar el repositorio

```bash
git clone https://github.com/kike220981/mlops-wine-quality-production.git
cd mlops-wine-quality-production
```

### 2. Configurar entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Ejecutar pipeline

* **Ingesta y limpieza:**

```bash
python src/data/ingesta.py
```

* **Entrenamiento:**

```bash
python src/models/entrenamiento.py
```

* **Levantar API:**

```bash
uvicorn src.api.app:app --reload
```

---

## 🧪 Calidad y Testing

El proyecto prioriza la robustez mediante pruebas automatizadas:

* Cobertura de tests: **92.5%** (supera el 70% requerido)

```bash
pytest --cov=src tests/
```

---

## 🐳 Dockerización

Se incluyen Dockerfiles separados por etapa:

```bash
# Construir imagen API
docker build -t wine-api -f docker/Dockerfile.api .

# Ejecutar contenedor
docker run -p 8000:8000 wine-api
```

---

## 📊 Metodología Ágil

Gestión basada en SCRUM/Kanban con GitHub Projects:

* Product Backlog con historias de usuario
* 3 sprints completados
* Retrospectiva en `docs/retrospectiva.md`

---

## 📑 Documentación

* Memoria del proyecto (arquitectura y decisiones)
* Retrospectiva (lecciones aprendidas)

---

## 👤 Autor

* **Kike**
* Asignatura: Metodologías de Desarrollo y Despliegue de Aplicaciones para Ciencia de Datos (20GIAR)
* Profesor: Federico Muñoz Babiano
