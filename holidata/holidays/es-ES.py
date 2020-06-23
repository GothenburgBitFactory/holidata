# coding=utf-8
from dateutil.easter import EASTER_WESTERN

from .holidays import Locale

"""
Information taken from government websites around 2020-06
    https://www.boe.es/diario_boe/txt.php?id=BOE-A-2019-14552
"""

class es_ES(Locale):
    """
    01-01: [NF] Año Nuevo
    01-06: [NRF] Epifanía del Señor
    02-28: [AN] [F] Día de Andalucía
    03-13: [ML] [F] Estatuto de Autonomía de la Ciudad de Melilla
    03-19: [CM,GA,MC,NC,PV,VC] [RF] San José
    04-23: [AR] [RF] San Jorge / Día de Aragón
    04-23: [CL] [F] Fiesta de Castilla y León
    05-01: [NF] Fiesta del Trabajo
    05-02: [MD] [F] Fiesta de la Comunidad de Madrid
    05-30: [CN] [F] Día de Canarias
    06-09: [MC] [F] Día de la Región de Murcia
    06-09: [RI] [F] Día de La Rioja
    06-24: [CT,GA,VC] [RF] San Juan
    07-25: [GA,PV] [RF] Santiago Apóstol / Día Nacional de Galicia
    07-28: [CB] [F] Día de las Instituciones de Cantabria
    07-31: [CE] [RF] Fiesta del Sacrificio - Eidul Adha
    07-31: [ML] [RF] Fiesta del Sacrificio - Aid El Kebir
    08-15: [NRF] Asunción de la Virgen
    09-02: [CE] [F] Día de Ceuta
    09-08: [AS] [F] Día de Asturias
    09-08: [EX] [F] Día de Estremadura
    09-11: [CT] [F] Fiesta Nacional de Cataluña
    09-15: [CB] [RF] La Bien Aparecida
    10-09: [VC] [F] Día de la Comunitat Valenciana
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
    60 days after Easter: [CM] [RV] Corpus Christi
    """

    locale = "es-ES"
    easter_type = EASTER_WESTERN
