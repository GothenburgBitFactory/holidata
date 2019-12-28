# coding=utf-8
from dateutil.easter import EASTER_WESTERN

from .holidays import Locale


class fr_BE(Locale):
    """
    01-01: [NF] Nouvel An
    05-01: [NF] Fête du Travail
    07-21: [NF] Fête nationale
    08-15: [NRF] Assomption
    11-01: [NRF] Toussaint
    11-11: [NF] Jour de l'armistice
    12-25: [NRF] Noël
    Easter: [NRV] Pâques
    1 day after Easter: [NRV] Lundi de Pâques
    39 days after Easter: [NRV] Ascension
    49 days after Easter: [NRV] Pentecôte
    50 days after Easter: [NRV] Lundi de Pentecôte
    """

    locale = "fr-BE"
    easter_type = EASTER_WESTERN
