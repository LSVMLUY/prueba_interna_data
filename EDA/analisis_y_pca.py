import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

def analisis_y_pca(data):
    
    # Initial feature set (excluding the target variable 'y' and verification_date)
    features = [col for col in data.columns if col != 'y' and col != 'verification_date']
    
    # 1. Estandarización de los datos
    df= data[features]
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df)  
    # 2. Aplicar PCA
    pca = PCA()
    principal_components = pca.fit_transform(scaled_data)
    
    # 3. Varianza explicada por cada componente
    explained_variance_ratio = pca.explained_variance_ratio_
    
    # Varianza explicada acumulada
    cumulative_explained_variance = explained_variance_ratio.cumsum()
    
    # 4. Visualización de la varianza explicada acumulada
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, len(cumulative_explained_variance) + 1), cumulative_explained_variance, marker='o', linestyle='--')
    plt.title('Varianza explicada acumulada por componentes')
    plt.xlabel('Número de componentes')
    plt.ylabel('Varianza explicada acumulada')
    plt.grid(True)
    plt.show()
    
    # Si deseas obtener las cargas de los componentes para las características originales:
    loadings = pca.components_
    
    # Por ejemplo, las cargas para el primer componente serían:
    first_component_loadings = loadings[0, :]
    
    
    # 1. Determine the number of components that sum up to 95% variance
    num_components = np.where(cumulative_explained_variance >= 0.95)[0][0] + 1
    
    # 2. Examine the loadings for these components
    significant_loadings = pca.components_[:num_components]
    
    # 1. & 2. Determine the number of components that sum up to 95% variance
    # and get the features with significant loadings for these components
    features_weights = np.zeros(len(significant_loadings[0]))
    for component in significant_loadings:
        features_weights= features_weights + abs(component)
    
    features_weights_perc = features_weights/features_weights.sum()
    
    weights_df =pd.DataFrame({'Variables': list(df.columns), 'Pesos': list(features_weights_perc)})
    weights_df= weights_df.sort_values("Pesos", ascending=False)
    weights_df['Suma Acumulativa'] = weights_df['Pesos'].cumsum()
    
    print(weights_df)
