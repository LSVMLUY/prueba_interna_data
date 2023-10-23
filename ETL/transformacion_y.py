def transformacion_y(data):
    # Conversion de la columna 'y' a binaria
    data['y'] = data['y'].replace({'yes': 1, 'no': 0})