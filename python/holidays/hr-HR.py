# coding=utf-8
from dateutil.easter import EASTER_WESTERN

from .holidays import Locale


class hr_HR(Locale):
    """
    01-01: [NF] Nova Godina
    01-06: [NRF] Bogojavljanje / Sveta tri kralja
    05-01: [NF] Praznik rada
    05-30: [NF] Dan državnosti   
    06-22: [NF] Dan antifašističke borbe
    08-05: [NF] Dan domovinske zahvalnosti
    08-15: [NRF] Velika Gospa
    10-08: [NF] Dan neovisnosti
    11-01: [NRF] Dan svih svetih
    11-18: [NF] Dan sjećanja na žrtve Domovinskog rata i Dan sjećanja na žrtvu Vukovara i Škabrnje
    12-25: [NRF] Božić
    12-26: [NRF] Sveti Stjepan
    Easter: [NRV] Uskrs
    1 day after Easter: [NRV] Uskršnji ponedjeljak
    60 days after Easter: [NRV] Tijelovo
    """

    locale = "hr-HR"
    easter_type = EASTER_WESTERN
