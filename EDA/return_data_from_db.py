import sqlite3
import pandas as pd
import os

def return_data_from_db():
    """
    Obtiene datos de una base de datos SQLite.

    Returns:
    DataFrame: Los datos obtenidos desde la base de datos.
    """
    # Obtiene la ruta del directorio actual del script (directorios superiores)
    script_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.dirname(script_directory)
    
    # Ruta relativa al directorio principal desde la subcarpeta ETL
    db_path = os.path.join(parent_directory, 'mercadocredito.db')
    print("db_path: " + db_path)
    # Conectar a la base de datos
    conn = sqlite3.connect(f'{db_path}')
    
    with open('stat_data.txt', 'r') as file:
        query1 = file.read()
    # Usar pandas para ejecutar las consultas
    data= pd.read_sql_query(query1, conn)
    conn.close()
    return data
