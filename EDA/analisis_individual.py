import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math as m

def grid_dist_graphs(data, desde_graf=0 , hasta_graf=20, bins=30):
    """
    Genera gráficos de distribución para variables en el conjunto de datos.

    Parameters:
    data (DataFrame): El DataFrame que contiene los datos a analizar.
    desde_graf (int): El índice de la primera variable a graficar.
    hasta_graf (int): El índice de la última variable a graficar.
    bins (int): El número de bins para el histograma.

    Returns:
    None
    """
    nro_graficos=hasta_graf-desde_graf
    columns=data.columns
    fontsize=18
    plt.figure(figsize=(30, 20))
    subplot_idx_1 = m.floor(nro_graficos**0.5)
    subplot_idx_2 = subplot_idx_1 +1 
    for idx, col in enumerate(columns[desde_graf:hasta_graf]):
        plt.subplot(subplot_idx_1, subplot_idx_2, idx + 1)
        sns.histplot(data[col], bins=bins)
        plt.title(f'Distribución de {col}',fontsize=fontsize)
        plt.xlabel(col)
        plt.ylabel('Frecuencia')
        plt.tight_layout()
    plt.show()
    


def analisis_individual(data):
    """
    Realiza un análisis individual de las variables en el conjunto de datos.

    Parameters:
    data (DataFrame): El DataFrame que contiene los datos a analizar.

    Returns:
    None
    """
    grid_dist_graphs(data, desde_graf=0 , hasta_graf=12)
    grid_dist_graphs(data, desde_graf=12 , hasta_graf=24)
    grid_dist_graphs(data, desde_graf=24 , hasta_graf=36)
    grid_dist_graphs(data, desde_graf=36 , hasta_graf=48)
    grid_dist_graphs(data, desde_graf=48 , hasta_graf=60)        
    grid_dist_graphs(data, desde_graf=60 , hasta_graf=72)        

    print("Descripcion de principales estadisticos invididuales : \n")
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    descriptive_stats = data.describe()
    selected_stats = descriptive_stats.loc[['mean', 'min', 'max', 'std']]
    pd.set_option('display.float_format', '{:.3f}'.format)
    print(selected_stats.T)
    pd.reset_option('display.max_columns')
    pd.reset_option('display.max_rows')