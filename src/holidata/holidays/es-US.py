# coding=utf-8
from dateutil.easter import EASTER_WESTERN

from .holidays import Locale


class es_US(Locale):
    """
    01-01: [NF] Año Neuvo
    07-04: [NF] Día de la Independiencia
    11-11: [NF] Día de los Veteranos
    12-24: [NRF] Nochebuena
    12-25: [NRF] Navidad
    3. monday in January: [NV] Cumpleaños de Martin Luther King, Jr.
    3. monday in February: [NV] Día del Presidente
    3. monday in April: [MA,ME] [V] Día del Patriota
    1. last monday in May: [NV] Día de los Caídos
    1. monday in September: [NV] Día del Trabajo
    2. monday in October: [NV] Día de Columbus
    4. thursday in November: [NV] Día de Acción de Gracias
    4. friday in November: [NV] Día después de Acción de Gracias
    """

    locale = "es-US"
    easter_type = EASTER_WESTERN
