import pandas as pd

def pares_redundantes(data):
    """
    Identifica pares de variables altamente correlacionadas en el conjunto de datos.

    Parameters:
    data (DataFrame): El DataFrame que contiene los datos a analizar.

    Returns:
    None
    """
    # Inicializar una lista para almacenar los pares de correlaciones
    correlation_pairs = []
    
    # Obtener la lista de nombres de variables
    variable_names = data.columns.tolist()
    
    # Calcular las correlaciones y almacenar los resultados en la lista
    for i in range(len(variable_names)):
        for j in range(i + 1, len(variable_names)):
            var1 = variable_names[i]
            var2 = variable_names[j]
            correlation = data[var1].corr(data[var2])
            abs_correlation= abs(correlation)
            correlation_pairs.append([var1, var2, correlation,abs_correlation])
            
    
    # Crear un DataFrame a partir de la lista de pares de correlaciones
    correlation_df = pd.DataFrame(correlation_pairs, columns=['Variable 1', 'Variable 2', 'Correlation','Abs_correlation'])
    
    # Mostrar el DataFrame resultante
    top_correlation_pairs = correlation_df[correlation_df["Abs_correlation"]>=0.9]
    print("Pares de variables altamente correlacionados (indicio de redundancia) : ")
    print(top_correlation_pairs.sort_values("Abs_correlation" , ascending=False))
