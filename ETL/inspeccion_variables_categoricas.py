def inspeccion_variables_categoricas(data):
    """
    Realiza e imprime una inspección inicial de variables categóricas (tipo object) en un DataFrame.

    Args:
        data (pd.DataFrame): El DataFrame que se va a inspeccionar.

    Returns:
        None
    """
    # Tratamiento de variables categoricas
    categorical_columns = data.select_dtypes(include=['object']).columns
    categorical_data = data[categorical_columns]
    print(categorical_data.head(10))
    
    unique_values = {column: categorical_data[column].unique() for column in categorical_data.columns}
    for clave, valor in unique_values.items():
        print(f"{clave}:")
        for elemento in valor:
            print(f"  - {elemento}")
