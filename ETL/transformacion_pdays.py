import numpy as np
def transformacion_pdays(data):
    # Transformación de la variable "pdays"
    data['contacted_previously'] = np.where(data['pdays'] == 999, 0, 1)
    data['pdays_less_30'] = np.where(data['pdays'] < 30, 1, 0)
    data['pdays_30_to_180'] = np.where((data['pdays'] >= 30) & (data['pdays'] < 180), 1, 0)
    data['pdays_more_than_180'] = np.where(data['pdays'] >= 180, 1, 0)
    data.drop('pdays', axis=1, inplace=True)
