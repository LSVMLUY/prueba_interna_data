import pandas as pd

def binarizacion_categoricas(data, *cols_to_exclude):
    """
    Realiza la binarización de variables categóricas en un DataFrame.

    Args:
        data (pd.DataFrame): El DataFrame que se va a binarizar.
        *cols_to_exclude: Columnas a excluir de la binarización.

    Returns:
        pd.DataFrame: El DataFrame con las variables binarizadas.
    """
    # Binarización de variables categóricas
    categorical_columns = data.select_dtypes(include=['object']).columns
    categorical_columns = list(categorical_columns)
    
    categorical_columns_a_binarizar = [i for i in categorical_columns if i not in list(cols_to_exclude)]
    
    for column in categorical_columns_a_binarizar:
        dummies = pd.get_dummies(data[column], prefix=column, prefix_sep='_')
        data = pd.concat([data, dummies], axis=1)
        data.drop(column, axis=1, inplace=True)
    return data
