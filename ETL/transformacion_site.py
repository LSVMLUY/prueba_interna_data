def transformacion_site(data):
    # Estandarización de 'site_id' y mapeo a códigos
    data["site_id"] = data["site_id"].str.lower()
    site_mapping = {
        'mexico': "MLM",
        'ecuador': "MEC",
        'chile': "MLC",
        'colombia': "MCO",
        'argentina': "MLA",
        'venezuela': "MLV",
        'peru': "MPE",
        'uruguay': "MLU",
        'brazil': "MLB"
    }
    data['site_id'] = data['site_id'].replace(site_mapping)