import pandas as pd
def creacion_verification_date_to_date(data):
    # Conversión de 'verification_date' a datetime
    data['verification_date_dt'] = pd.to_datetime(data['verification_date'], unit='s')
    
