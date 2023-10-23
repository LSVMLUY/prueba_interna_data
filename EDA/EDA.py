import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

from sql_analysis import *
from return_data_from_db import *
from analisis_individual import *
from analisis_correlacion_con_y import *
from pares_redundantes import  *
from analisis_y_pca import *

sql_analysis()


data= return_data_from_db()
data.drop('index', axis=1, inplace=True)
# EDA : Analisis distribuciones de forma individual

analisis_individual(data)

analisis_correlacion_con_y(data)

pares_redundantes(data)

analisis_y_pca(data)
