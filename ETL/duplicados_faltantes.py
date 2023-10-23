def duplicados_y_faltantes(data):
    # Manejo de datos faltantes
    missing_values = data.isna().sum()
    print("\n ------  \n")
    print(f"Datos faltantes por columna:\n{missing_values}")
    data['site_id'].fillna('unknown', inplace=True)
    
    # Verificación de registros duplicados
    nro_duplicados = data.duplicated().sum()
    print("\n ------  \n")
    print(f"Número de registros duplicados: {nro_duplicados}")

