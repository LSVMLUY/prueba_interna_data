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

# Obtiene la ruta del directorio actual del script (directorios superiores)
script_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(script_directory)

# Combinar la ruta del directorio padre con el nombre del archivo CSV
csv_file_path = os.path.join(parent_directory, "prueba_data_engineer.csv")

# Cargar el archivo CSV
data = pd.read_csv(csv_file_path, sep=';')

# Verificar estructura inicial de los datos
print(data.head(10))
print(data.info())

## ETL : Limpieza y transformación de datos.

# Verificaciones sobre duplicados y faltantes
duplicados_y_faltantes(data)

# Tratamiento de variables
    # Inspeccion inicial de variables categoricas
inspeccion_variables_categoricas(data)

    # Transformaciones y, site_id, verification_date, pdays , month  , day_of_week, duration
transformaciones(data)
    # En la version BI me quedo solo con la formato fecha y en la estadistica solo en formato unix
bi_data_df= data.copy()
bi_data_df.drop("verification_date",axis=1,inplace=True)
data.drop("verification_date_dt",axis=1,inplace=True)

# Binarizacion de categoricas
data= binarizacion_categoricas(data)

## ETL : Análisis de "consistencia" (logica de negocio y de los datos).

## ETL : Almacenamiento de datos.

# Ruta relativa al directorio principal desde la subcarpeta ETL
db_path = os.path.join(parent_directory, 'mercadocredito.db')
print("db path : " + str(db_path))

# Crear una "base de datos" SQLite en un archivo
engine = create_engine(f'sqlite:///{db_path}') # Esto creará (o usará, si ya existe) un archivo "mercadocredito.db" en el directorio actual

# Carga el DataFrame a una nueva tabla en SQLite
data.to_sql('stat_mc_ya', engine, if_exists='replace')
bi_data_df.to_sql('bi_mc_ya', engine, if_exists='replace') # Creo tabla de Analisis de Negocio mas amigable con variables categoricas

# Cierro la conexion
engine.dispose()

