# Retrospectiva del Proyecto: MLOps Wine Quality

## Sprint 1: Ingesta y Estandarización de Datos
Logros: Se estableció el pipeline inicial de datos logrando una carga limpia y automatizada del dataset.

Desafío Técnico: El modelo fallaba al recibir nombres de columnas con espacios (ej. fixed acidity).

Solución: Se implementó una capa de limpieza en ingesta.py para normalizar todos los nombres a formato snake_case desde el inicio.

## Sprint 2: Inteligencia y Garantía de Calidad
Logros: Entrenamiento exitoso del modelo y cumplimiento de métricas de calidad, alcanzando una cobertura de tests del 92.5%.

Desafío Técnico (Rutas CI): Los tests fallaban en GitHub Actions al no encontrar los archivos .joblib por rutas relativas.

Solución: Se configuró el uso de rutas absolutas dinámicas calculadas desde la raíz del proyecto para asegurar la consistencia en el entorno de Integración Continua.

## Sprint 3: Servicio de Predicción e Infraestructura
Logros: Despliegue de la API y preparación de la infraestructura como código con Terraform.

Desafío Técnico (FastAPI): Incompatibilidad de métodos en Pydantic V2 (error con el método .dict()).

Solución: Se actualizó el código de la API para utilizar .model_dump(), garantizando la estabilidad del servicio y una gestión de errores controlada (HTTP 503/500).

## Análisis Global de Lecciones Aprendidas
Consistencia de Features: La importancia de mantener nombres de variables idénticos entre el entrenamiento y la inferencia en Scikit-Learn.

Automatización: La utilidad de los logs detallados en GitHub Actions para diagnosticar errores de sintaxis en tiempo real.

Infraestructura: El valor de Terraform para asegurar que el entorno de despliegue sea idéntico al de desarrollo.

## Futuras Mejoras
Implementación de un sistema de versionado de modelos (Model Registry).

Despliegue de contenedores en un clúster de Kubernetes para mejorar la disponibilidad
