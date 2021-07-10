# coding=utf-8
from dateutil.easter import EASTER_WESTERN

from holidata.utils import SmartDayArrow
from .holidays import Locale, Holiday

"""
sources
THE LAW ON HOLIDAYS, MEMORIALS AND NON-WORKING DAYS IN THE REPUBLIC OF CROATIA
1996: https://narodne-novine.nn.hr/eli/sluzbeni/1996/33/674
"""


class hr_HR(Locale):
    """
    01-01: [NF] Nova godina
    01-06: [NRF] Sveta tri kralja
    05-01: [NF] Blagdan rada
    05-30: [NF] Dan državnosti
    06-22: [NF] Dan antifašističke borbe
    08-05: [NF] Dan domovinske zahvalnosti
    08-15: [NRF] Velika Gospa
    11-01: [NRF] Svi sveti
    12-25: [NRF] Božić
    12-26: [NRF] Sveti Stjepan
    Easter: [NRV] Uskrs
    1 day after Easter: [NRV] Uskrsni ponedjeljak
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
