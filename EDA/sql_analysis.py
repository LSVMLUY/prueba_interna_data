import sqlite3
import pandas as pd
import os

def print_resultados(title, query, df_query):
    print(title)
    print('"""')
    print(query)
    print('"""')
    print(df_query)
    print('')
    
    
def sql_analysis():
    # Obtiene la ruta del directorio actual del script (directorios superiores)
    script_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.dirname(script_directory)
    
    # Ruta relativa al directorio principal desde la subcarpeta ETL
    db_path = os.path.join(parent_directory, 'mercadocredito.db')    
        
    # Conectar a la base de datos
    conn = sqlite3.connect(f'{db_path}')
    
    with open('query_MLA_or_MLU.txt', 'r') as file:
        query1 = file.read()
    
    with open('query_+junio_+2m.txt', 'r') as file:
        query2 = file.read()
    
    print(query2)
    
    with open('query_MLB_lunes.txt', 'r') as file:
        query3 = file.read()
    
    # Usar pandas para ejecutar las consultas
    df_query1 = pd.read_sql_query(query1, conn)
    df_query2 = pd.read_sql_query(query2, conn)
    df_query3 = pd.read_sql_query(query3, conn)
    
    # Preview de los resultados
    print_resultados("Registros para Argentina y Uruguay \n",query1, df_query1)
    print_resultados("Registros cuya fecha de verificación es superior a Junio 2023 y cuya duración fue de más de 2 minutos \n",query3, df_query2)
    print_resultados("Registros de Brasil y dias Lunes \n",query3, df_query3)    
    conn.close()
