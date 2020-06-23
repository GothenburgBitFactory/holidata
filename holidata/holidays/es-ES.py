# coding=utf-8
from dateutil.easter import EASTER_WESTERN

from .holidays import Locale


class es_ES(Locale):
    """
    01-01: [NF] Año Nuevo
    01-06: [NRF] Epifanía del Señor
    02-28: [AN] [F] Día de Andalucía
    03-19: [CM,GA,MC,NC,PV,VC] [RF] San José
    05-01: [NF] Fiesta del Trabajo
    06-24: [CT,GA,VC] [RF] San Juan
    07-25: [GA,PV] [RF] Santiago Apóstol / Día Nacional de Galicia
    08-15: [NRF] Asunción de la Virgen
    10-12: [NF] Fiesta Nacional de España
    11-01: [NRF] Todos los Santos
    12-06: [NF] Día de la Constitución Española
    12-08: [NRF] Inmaculada Concepción
    12-25: [NRF] Natividad del Señor
    12-26: [CT,IB] [RF] San Esteban
    3 days before Easter: [AN,AR,AS,CN,CB,CL,CM,CE,EX,GA,IB,MD,ML,NC,PV,RI] [RV] Jueves Santo
    2 days before Easter: [NRV] Viernes Santo
    Easter: [NRV] Pascua
    1 day after Easter: [CB,CM,CT,IB,NC,PV,RI,VC] [RV] Lunes de Pascua
    """

    locale = "es-ES"
    easter_type = EASTER_WESTERN
