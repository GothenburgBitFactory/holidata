# coding=utf-8
from dateutil.easter import EASTER_WESTERN

from .holidays import Locale


class fr_FR(Locale):
    """
    01-01: [NF] Jour de l'an
    05-01: [NF] Fête du premier mai
    05-08: [NF] Armistice 1945
    07-14: [NF] Fête nationale
    08-15: [NRF] Assomption
    11-01: [NRF] Toussaint
    11-11: [NF] Armistice 1918
    12-25: [NF] Noël
    1 day after Easter: [NRV] Lundi de Pâques
    39 days after Easter: [NRV] Ascension
    49 days after Easter: [NRV] Pentecôte
    50 days after Easter: [NRV] Lundi de Pentecôte
    """

    locale = "fr-FR"
    easter_type = EASTER_WESTERN
