from dateutil.easter import EASTER_WESTERN

from .holidays import Locale


class es_ES(Locale):
    u"""
    01-01: [NF] Año Nuevo
    01-06: [NRF] Día de los Reyes
    05-01: [NF] Fiesta del Trabajo
    08-15: [NRF] Asunción de la Virgen
    10-12: [NF] Fiesta Nacional de España
    11-01: [NRF] Dia de todos los Santos
    12-06: [NF] Dia de la Constitución
    12-08: [NRF] Inmaculada Concepción
    12-24: [NRF] Noche Buena
    12-25: [NRF] Navidad
    12-31: [NF] Noche Vieja
    2 days before Easter: [NRV] Viernes Santo
    Easter: [NRV] Pascua
    """

    locale = "es-ES"
    easter_type = EASTER_WESTERN
