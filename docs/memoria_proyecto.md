# Memoria Técnica: Sistema de Predicción de Calidad de Vino (MLOps)

**Autor:** Enrique Sánchez Antuña  
**Repositorio Oficial:** https://github.com/kike220981/mlops-wine-quality-production  
**Asignatura:** 20GIAR - Metodologías de desarrollo y despliegue de aplicaciones para ciencia de datos  

---

## 1. Introducción y Objetivos

Este proyecto aborda el diseño e implementación de un ciclo de vida completo de Machine Learning Operations (MLOps) para la predicción de la calidad del vino tinto. En el ámbito académico del Grado de IA, el objetivo no es solo obtener un modelo preciso, sino garantizar que dicho modelo sea reproducible, testeable y escalable en un entorno de producción real.

El sistema integra:

- **Ingeniería de Datos:** Automatización de la ingesta y limpieza  
- **Modelado Avanzado:** Uso de técnicas de ensamble (Random Forest)  
- **Calidad de Software:** Implementación de pruebas unitarias y CI/CD  
- **Infraestructura:** Contenedorización con Docker y despliegue automatizado  

---

## 2. Metodología de Gestión (Agile/Kanban)

Siguiendo los principios de desarrollo ágil, el proyecto se dividió en tres Sprints críticos:

### 2.1. Sprint 1: Pipeline de Datos

Se estableció la infraestructura básica para la obtención de datos desde el UCI Machine Learning Repository. Se puso especial énfasis en la normalización de cabeceras (estándar `snake_case`) para evitar errores en las etapas posteriores del pipeline y facilitar la lectura técnica de los datos fisicoquímicos.

---

### 2.2. Sprint 2: Modelado, Validación y Calidad

Se entrenó un modelo robusto y se implementó una estrategia de validación rigurosa. El hito principal de este sprint fue alcanzar una cobertura de tests del 88% mediante Pytest, asegurando que cualquier cambio en la lógica de preprocesamiento sea validado automáticamente antes de llegar a producción.

---

### 2.3. Sprint 3: Despliegue e Infraestructura (IaC)

Se transformó el modelo en un producto de software mediante FastAPI. Se utilizó Docker para encapsular el entorno y Terraform para definir la infraestructura necesaria, garantizando que el sistema sea agnóstico al proveedor de nube utilizado.

---

## 3. Análisis Técnico del Dataset y Preprocesamiento

### 3.1. Diccionario de Variables

Para un análisis de IA riguroso, se consideran 11 variables de entrada:

1. **Acidez fija:** Ácidos orgánicos no volátiles  
2. **Acidez volátil:** Ácidos que pueden provocar un sabor a vinagre  
3. **Ácido cítrico:** Aporta frescura y sabor  
4. **Azúcar residual:** Cantidad de azúcar tras la fermentación  
5. **Cloruros:** Cantidad de sal en el vino  
6. **Dióxido de azufre (libre y total):** Previene la oxidación y el crecimiento microbiano  
7. **Densidad:** Relación masa/volumen influenciada por alcohol y azúcar  
8. **pH:** Nivel de acidez/alcalinidad  
9. **Sulfatos:** Aditivos que actúan como antimicrobianos  
10. **Alcohol:** Porcentaje de volumen de alcohol  

---

### 3.2. Normalización Estadística

Se implementó **StandardScaler** de Scikit-Learn. En el entrenamiento de modelos de IA, esto es fundamental para evitar que variables con rangos numéricos elevados (como el dióxido de azufre) dominen sobre aquellas con rangos pequeños (como el pH), permitiendo que el algoritmo aprenda la importancia real de cada característica independientemente de su unidad de medida.

---

## 4. Arquitectura de Inferencia y MLOps

### 4.1. El Algoritmo: RandomForestClassifier

Se seleccionó Random Forest por ser un método de **Ensemble Learning** que combina múltiples árboles de decisión. Esto proporciona una alta capacidad de generalización y resistencia ante el sobreajuste (*overfitting*), características esenciales cuando se trabaja con datasets químicos con posibles valores atípicos.

---

### 4.2. Contenedorización con Docker

El uso de Docker garantiza la inmutabilidad del entorno. El archivo Dockerfile define:

- La imagen base de Python  
- La instalación de dependencias vía `requirements.txt`  
- La exposición del puerto 8000 para la API  
- La carga del artefacto `.joblib` generado en el entrenamiento  

---

## 5. Integración Continua (CI/CD)

El proyecto utiliza GitHub Actions para automatizar la calidad. Cada push al repositorio desencadena:

1. **Linting:** Verificación de estilo de código  
2. **Unit Testing:** Comprobación de funciones de limpieza  
3. **Integration Testing:** Prueba de la API y carga del modelo  
4. **Artifact Check:** Validación de que el modelo `.joblib` se genera correctamente  

---

## 6. Conclusiones y Ética

Este proyecto demuestra que el valor de la IA no reside solo en el algoritmo, sino en la solidez del sistema que lo soporta. Se ha logrado un flujo de trabajo donde el código es la ley (*Code as Law*), desde la definición de la infraestructura con Terraform hasta la respuesta JSON de la API.

Como visión futura, se recomienda la implementación de **DVC (Data Version Control)** para gestionar el versionado de los datasets físicos y la monitorización de la degradación del modelo en producción.
