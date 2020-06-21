# coding=utf-8
from dateutil.easter import EASTER_WESTERN

from .holidays import Locale


class es_ES(Locale):
    """
    01-01: [NF] Año Nuevo
    01-06: [NRF] Epifanía del Señor
    05-01: [NF] Fiesta del Trabajo
    08-15: [NRF] Asunción de la Virgen
    10-12: [NF] Fiesta Nacional de España
    11-01: [NRF] Todos los Santos
    12-06: [NF] Día de la Constitución Española
    12-08: [NRF] Inmaculada Concepción
    12-25: [NRF] Natividad del Señor
    2 days before Easter: [NRV] Viernes Santo
    Easter: [NRV] Pascua
    """

    locale = "es-ES"
    easter_type = EASTER_WESTERN
