# MLOps Wine Quality Production 🍷

Este proyecto implementa un pipeline completo de **MLOps** para la clasificación de la calidad del vino tinto, siguiendo los estándares de la asignatura **Metodologías de Desarrollo y Despliegue**.

## 🚀 Objetivo
Diseñar e implementar un ciclo de vida de ML automatizado que incluya ingesta de datos, entrenamiento con trazabilidad, pruebas de calidad y despliegue mediante contenedores.

## 🛠️ Stack Tecnológico
*   **Lenguaje:** Python 3.9+[cite: 1]
*   **ML Framework:** Scikit-learn[cite: 2]
*   **API:** FastAPI con validación Pydantic[cite: 1]
*   **Contenedores:** Docker (Multi-stage builds)[cite: 1, 2]
*   **CI/CD:** GitHub Actions[cite: 1, 2]
*   **IaC:** Terraform para despliegue en AWS[cite: 2]
*   **Gestión:** Metodología Ágil (Scrum/Kanban)[cite: 2]

## 📁 Estructura del Proyecto
Basada en el estándar industrial para Ciencia de Datos[cite: 1]:
*   `src/data/`: Scripts de ingesta y preprocesamiento de datos[cite: 1].
*   `src/models/`: Entrenamiento y evaluación de modelos[cite: 1].
*   `src/api/`: Interfaz de servicio para predicciones en tiempo real[cite: 1].
*   `infrastructure/`: Definición de recursos en la nube mediante Terraform[cite: 1].
*   `.github/workflows/`: Automatización de integración y despliegue continuo (CI/CD)[cite: 1, 2].

## ⚙️ Instalación y Uso Local

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/TU_USUARIO/mlops-wine-quality-production.git](https://github.com/TU_USUARIO/mlops-wine-quality-production.git)
   cd mlops-wine-quality-production
