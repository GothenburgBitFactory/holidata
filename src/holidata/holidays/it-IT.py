# coding=utf-8
from dateutil.easter import EASTER_WESTERN

from .holidays import Locale


class it_IT(Locale):
    """
    01-01: [NF] Capodanno
    01-06: [NRF] Epifania
    04-25: [NF] Festa della liberazione
    05-01: [NF] Festa del lavoro
    06-02: [NF] Festa della repubblica
    08-15: [NRF] Assunzione (ferragosto)
    11-01: [NRF] Ognissanti
    12-08: [NRF] Immacolata concezione
    12-25: [NRF] Natale
    12-26: [NRF] S.to Stefano
    Easter: [NRV] Pasqua
    1 day after Easter: [NRV] Pasquetta
    """

    locale = "it-IT"
    easter_type = EASTER_WESTERN
