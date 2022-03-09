# coding=utf-8
from dateutil.easter import EASTER_WESTERN

from .holidays import Locale

"""
source: http://prawo.sejm.gov.pl/isap.nsf/download.xsp/WDU20150000090/O/D20150090.pdf
"""


class pl_PL(Locale):
    """
    01-01: [NF] Nowy Rok
    01-06: [NRF] Trzech Króli
    05-01: [NF] Święto Pracy
    05-03: [NF] Święto Konstytucji Trzeciego Maja
    08-15: [NRF] Wniebowzięcie Najświętszej Maryi Panny
    11-01: [NRF] Wszystkich Świętych
    11-11: [NF] Narodowe Święto Niepodległości
    12-25: [NRF] Boże Narodzenie (pierwszy dzień)
    12-26: [NRF] Boże Narodzenie (drugi dzień)
    Easter: [NRV] Wielkanoc
    1 day after Easter: [NRV] Poniedziałek Wielkanocny
    49 days after Easter: [NRV] Zielone Świątki
    60 days after Easter: [NRV] Boże Ciało
    """

    locale = "pl-PL"
    easter_type = EASTER_WESTERN
