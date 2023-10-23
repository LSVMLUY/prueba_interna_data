import pandas as pd

def duplicados_y_faltantes(data):
    """
    Identifica datos faltantes y verifica duplicados en un DataFrame.

    Args:
        data (pd.DataFrame): El DataFrame que se va a analizar.

    Returns:
        None
    """
    # Manejo de datos faltantes
    missing_values = data.isna().sum()
    print("\n ------  \n")
    print(f"Datos faltantes por columna:\n{missing_values}")
    data['site_id'].fillna('unknown', inplace=True)
    
    # Verificación de registros duplicados
    nro_duplicados = data.duplicated().sum()
    print("\n ------  \n")
    print(f"Número de registros duplicados: {nro_duplicados}")