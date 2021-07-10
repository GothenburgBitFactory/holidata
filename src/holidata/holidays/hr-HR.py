# coding=utf-8
from dateutil.easter import EASTER_WESTERN

from holidata.utils import SmartDayArrow
from .holidays import Locale, Holiday

"""
sources
THE LAW ON HOLIDAYS, MEMORIALS AND NON-WORKING DAYS IN THE REPUBLIC OF CROATIA
2002: https://narodne-novine.nn.hr/eli/sluzbeni/2002/136/2194
2002: https://narodne-novine.nn.hr/eli/sluzbeni/2002/13/318
2001: https://narodne-novine.nn.hr/eli/sluzbeni/2001/96/1614
1996: https://narodne-novine.nn.hr/eli/sluzbeni/1996/33/674
"""


class hr_HR(Locale):
    """
    01-01: [NF] Nova godina
    01-06: [NRF] Bogojavljanje
    05-01: [NF] Praznik rada
    06-22: [NF] Dan antifašističke borbe
    06-25: [NF] Dan državnosti
    08-05: [NF] Dan pobjede i domovinske zahvalnosti
    08-15: [NRF] Velika Gospa
    10-08: [NF] Dan neovisnosti
    11-01: [NRF] Svi sveti
    12-25: [NRF] Božić
    12-26: [NRF] Sveti Stjepan
    Easter: [NRV] Uskrs
    1 day after Easter: [NRV] Uskrsni ponedjeljak
    60 days after Easter: [NRV] Tijelovo
    """

    locale = "hr-HR"
    easter_type = EASTER_WESTERN

    def holiday_dan_sjecanja_na_zrtve_domovinskog_rata_i_dan_sjecanja_na_zrtvu_vukovara_i_skabrnje(self):
        if self.year >= 2020:
            return [Holiday(
                self.locale,
                "",
                SmartDayArrow(self.year, 11, 18),
                "Dan sjećanja na žrtve Domovinskog rata i Dan sjećanja na žrtvu Vukovara i Škabrnje",
                "NF"
            )]
        else:
            return []
