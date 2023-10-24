import os
import pandas as pd
from sqlalchemy import create_engine

from duplicados_faltantes import duplicados_y_faltantes
from inspeccion_variables_categoricas import inspeccion_variables_categoricas
from transformaciones import transformaciones
from binarizacion_categoricas import binarizacion_categoricas

# ETL: Lectura de datos

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

## ETL: Limpieza y transformación de datos

# Verificaciones sobre duplicados y faltantes
duplicados_y_faltantes(data)

# Tratamiento de variables
inspeccion_variables_categoricas(data)

# Aplicar transformaciones
transformaciones(data)

# Creación de una copia para el análisis de negocio
bi_data_df = data.copy()

# Borrar la columna 'verification_date' del DataFrame original
bi_data_df.drop("verification_date", axis=1, inplace=True)
data.drop("verification_date_dt", axis=1, inplace=True)

# Binarización de variables categóricas
data = binarizacion_categoricas(data)

## ETL: Analisis de "consistencia" (logica de negocio y de los datos).
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', '{:.3f}'.format)
print(data.describe().loc[['min', 'max']].T )

MLB = data[data["site_id_MLB"]==1]
print("combinaciones unicas de un indice para un mes en MLB:")
print(MLB[['cons.price.idx', 'month']].drop_duplicates().sort_values("month"))

pd.reset_option('display.max_rows')

## ETL: Almacenamiento de datos
# Ruta relativa al directorio principal desde la subcarpeta ETL
db_path = os.path.join(parent_directory, 'mercadocredito.db')
print("db path: " + str(db_path))

# Crear una "base de datos" SQLite en un archivo
engine = create_engine(f'sqlite:///{db_path}')  # Esto creará o usará un archivo "mercadocredito.db"

# Cargar el DataFrame a una nueva tabla en SQLite
data.to_sql('stat_mc_ya', engine, if_exists='replace')
bi_data_df.to_sql('bi_mc_ya', engine, if_exists='replace')  # Creo tabla de Analisis de Negocio más amigable con variables categóricas

# Cerrar la conexión
engine.dispose()
