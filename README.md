Repositorio de referencia de la prueba de Luciano Spinelli para entrar en el equipo de DATA-IDD

---
# A - PROPUESTA DE PRUEBA
Mercado Pago ha implementado una nueva campaña de marketing para un producto de Mercado Crédito. Esta prueba tiene como objetivo comprender y analizar el comportamiento de los clientes en base a un conjunto de datos de esta campaña.

## Etapas Generales de Procesamiento
1. Lectura de datos.
2. Limpieza y transformación de datos.
3. Almacenamiento de datos.
4. Análisis estadístico de los datos.

## Parte 1: ETL
Dado un conjunto de datos en un CSV llamado `prueba_data_engineer.csv`, se debe realizar las siguientes tareas:
1. **Lectura del CSV** y obtención de los datos.
2. **Procesamiento de datos**: Realizar limpieza o transformaciones según se considere necesario para un análisis estadístico posterior.
3. **Almacenamiento de datos** en una base de datos para su posterior uso.

### Especificaciones del archivo CSV
| NOMBRE | DESCRIPCIÓN | TIPO |
| ------ | ----------- | ---- |
| age | Edad | numeric |
| ... | ... | ... |
| y | Indica si el cliente está inscripto a Mercado Crédito Ya | binary |

## Parte 2: Análisis
Con los datos curados y disponibles en una base de datos, se debe:
1. **Consultas SQL**:
    - Extraer registros para Argentina y Uruguay.
    - Obtener registros cuya fecha de verificación es superior a Junio 2023 y duración fue de más de 2 minutos.
    - Obtener registros que hayan sido realizados un lunes y sean de Brasil.
2. **Análisis Estadístico (Exploratory Data Analysis)**:
    - Considerar distribuciones de las variables de forma independiente.
    - Correlación entre variables y con el target "y".
    - Visualizaciones (e.g histogramas, boxplots, scatter plots, matrices de confusión).
    - Media y desviación estándar de cada variable.

**Nota**: El lenguaje de programación y el motor de base de datos a utilizar queda a elección del candidato.


---

---
# B - PROCESO SEGUIDO
Voy a proceder a explicar los pasos que me he planteado para resolver los pedidos de la propuesta. Los mismos, van a seguir el siguiente orden:

## ETL
1. Lectura de datos.
2. Limpieza y transformación de datos.
3. Análisis de "consistencia" (logica de negocio y de los datos).
4. Almacenamiento de datos.

## ANALISIS
  ### SQL
  1. Conexion a BD
  2. Consultas solicitadas y visualización preliminar de resultados
  ### EDA (Exploratory Data Analysis) 
  1. Analisis distribuciones de forma independiente
  2. Pares de correlaciones con variable objetivo 'y'
  3. Variables de mayor importancia descriptiva
  4. Analisis de variables dada la evidencia encontrada y comentarios

---


