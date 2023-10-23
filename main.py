import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine
import sqlite3

from duplicados_faltantes import *
from inspeccion_variables_categoricas import *
from transformaciones import *
from binarizacion_categoricas import *

## ETL : Lectura de datos

# Lectura del archivo brindado en la letra de la prueba
data = pd.read_csv("prueba_data_engineer.csv", sep=';')

# Verificar estructura inicial de los datos
print(data.head(10))
print(data.info())

## ETL : Limpieza y transformación de datos.

# Verificaciones sobre duplicados y faltantes
duplicados_y_faltantes(data)

# Tratamiento de variables
    # Inspeccion inicial de variables categoricas
inspeccion_variables_categoricas(data)

    # Transformaciones y, site_id, verification_date, pdays , month  y day_of_week
transformaciones(data)

# Genero copia de tabla previo a binarizacion de variables categoricas para analisis estadistico
bi_data_df = data.copy()

# Binarizacion de categoricas
data= binarizacion_categoricas(data)

## ETL : Análisis de "consistencia" (logica de negocio y de los datos).

## ETL : Almacenamiento de datos.

# Crear una "base de datos" SQLite en memoria (también puedes usar un archivo)
engine = create_engine('sqlite:///mercadocredito.db')  # Esto creará (o usará, si ya existe) un archivo "mercadocredito.db" en el directorio actual

# Carga el DataFrame a una nueva tabla en SQLite
data.to_sql('stat_mc_ya', engine, if_exists='replace')
bi_data_df.to_sql('bi_mc_ya', engine, if_exists='replace') # Creo tabla de Analisis de Negocio mas amigable con variables categoricas

# Cierro la conexion
engine.dispose()

