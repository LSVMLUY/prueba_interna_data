def transformacion_day_of_week(data):
    # Estandarización de 'site_id' y mapeo a códigos
    dow_mapping = {
       "mon":1,
       "tue":2,
       "wed":3,
       "thu":4,
       "fri":5,
       "sat":6,
       "sun":7
    }
    data['day_of_week'] = data['day_of_week'].replace(dow_mapping)