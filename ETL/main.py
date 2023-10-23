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

# Lectura del archivo brindado en la letra de la prueba
data = pd.read_csv("prueba_data_engineer.csv", sep=';')

# Verificar estructura inicial de los datos
print(data.head(10))
print(data.info())

# Verificaciones sobre duplicados y faltantes
duplicados_y_faltantes(data)

# TRATAMIENTO DE VARIABLES
    # Inspeccion inicial de variables categoricas
inspeccion_variables_categoricas(data)

    # Transformaciones y, site_id, verification_date, pdays , month  y day_of_week
transformaciones(data)

# # Genero copia de tabla previo a binarizacion de variables categoricas para analisis estadistico
bi_data_df = data.copy()


    # Binarizacion de categoricas a excepcion de y
binarizacion_categoricas(data,"site_id")



