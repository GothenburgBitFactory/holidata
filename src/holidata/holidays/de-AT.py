# coding=utf-8
from dateutil.easter import EASTER_WESTERN

from .holidays import Locale


class de_AT(Locale):
    """
    01-01: [NF] Neujahr
    01-06: [NRF] Heilige drei Könige
    03-19: [2,6,7,8] [RF] Josef
    05-01: [NF] Staatsfeiertag
    05-04: [4] [F] Florian
    08-15: [NRF] Mariä Himmelfahrt
    09-24: [5] [F] Rupert
    10-10: [2] [F] Tag der Volksabstimmung
    10-26: [NF] Nationalfeiertag
    11-01: [NRF] Allerheiligen
    11-11: [1] [F] Martin
    11-15: [9,3] [F] Leopold
    12-08: [NRF] Mariä Empfängnis
    12-24: [NRF] Heiliger Abend
    12-25: [NRF] Christtag
    12-26: [NF] Stefanitag
    12-31: [NF] Silvester
    2 days before Easter: [NRV] Karfreitag
    Easter: [NRV] Ostersonntag
    1 day after Easter: [NRV] Ostermontag
    39 days after Easter: [NRV] Christi Himmelfahrt
    49 days after Easter: [NRV] Pfingstsonntag
    50 days after Easter: [NRV] Pfingstmontag
    60 days after Easter: [NRV] Fronleichnam
    """

    locale = "de-AT"
    easter_type = EASTER_WESTERN
