def inspeccion_variables_categoricas(data):
    # Tratamiento de variables categóricas
    categorical_columns = data.select_dtypes(include=['object']).columns
    categorical_data = data[categorical_columns]
    print(categorical_data.head(10))
    
    unique_values = {column: categorical_data[column].unique() for column in categorical_data.columns}
    for clave, valor in unique_values.items():
        print(f"{clave}:")
        for elemento in valor:
            print(f"  - {elemento}")
        