from transformacion_y import *
from transformacion_site import *
from transformacion_pdays import *
from transformacion_verification_date import *
from transformacion_month import *
from transformacion_day_of_week import *
from transformacion_duration import *


def transformaciones(data):
    transformacion_y(data)
    transformacion_site(data)
    transformacion_pdays(data)
    creacion_verification_date_to_date(data)
    transformacion_month(data)
    transformacion_day_of_week(data)
    transformacion_duration(data)