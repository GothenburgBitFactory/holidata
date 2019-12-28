# coding=utf-8
from dateutil.easter import EASTER_WESTERN

from .holidays import Locale


class nl_BE(Locale):
    """
    01-01: [NF] Nieuwjaar
    05-01: [NF] Dag van de arbeid
    07-21: [NF] Nationale feestdag
    08-15: [NRF] Onze Lieve Vrouw hemelvaart
    11-01: [NRF] Allerheiligen
    11-11: [NF] Wapenstilstand
    12-25: [NRF] Kerstmis
    Easter: [NRV] Pasen
    1 day after Easter: [NRV] Paasmaandag
    39 days after Easter: [NRV] Onze Lieve Heer hemelvaart
    49 days after Easter: [NRV] Pinksteren
    50 days after Easter: [NRV] Pinkstermaandag
    """

    locale = "nl-BE"
    easter_type = EASTER_WESTERN
