def transformacion_month(data):
    # Estandarización de 'site_id' y mapeo a códigos
    month_mapping = {
       "jan":1,
       "feb":2,
       "mar":3,
       "apr":4,
       "may":5,
       "jun":6,
       "jul":7,
       "aug":8,
       "sep":9,
       "oct":10,
       "nov":11,
       "dec":12
    }
    data['month'] = data['month'].replace(month_mapping)