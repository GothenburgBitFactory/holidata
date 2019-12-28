# coding=utf-8
from dateutil.easter import EASTER_WESTERN

from .holidays import Locale


class nb_NO(Locale):
    """
    01-01: [NF] Nyttårsdag
    05-01: [NF] Offentlig Høytidsdag
    05-08: [NF] Frigjøringsdag 1945
    05-17: [NF] Grunnlovsdag
    12-24: [NRF] Julaften
    12-25: [NRF] Juledag
    12-26: [NRF] Juledag
    12-31: [NF] Nyttårsaften
    49 days before Easter: [NRV] Fastelavn
    7 days before Easter: [NRV] Palmesøndag
    3 days before Easter: [NRV] Skjærtorsdag
    2 days before Easter: [NRV] Langfredag
    Easter: [NRV] Påskedag
    1 day after Easter: [NRV] Påskedag
    39 days after Easter: [NRV] Kristi Himmelfartsdag
    49 days after Easter: [NRV] Pinsedag
    50 days after Easter: [NRV] Pinsedag
    """

    locale = "nb-NO"
    easter_type = EASTER_WESTERN
