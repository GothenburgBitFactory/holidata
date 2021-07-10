# coding=utf-8
from dateutil.easter import EASTER_WESTERN

from holidata.utils import SmartDayArrow
from .holidays import Locale, Holiday

"""
sources
THE LAW ON HOLIDAYS, MEMORIALS AND NON-WORKING DAYS IN THE REPUBLIC OF CROATIA
2019: https://narodne-novine.nn.hr/eli/sluzbeni/2019/110/2212
2011: https://narodne-novine.nn.hr/eli/sluzbeni/2011/130/2613 (no changes)
2011: https://narodne-novine.nn.hr/eli/sluzbeni/2011/74/1576 (no changes)
2008: https://narodne-novine.nn.hr/eli/sluzbeni/2008/55/1911
2006: https://narodne-novine.nn.hr/eli/sluzbeni/2006/59/1428 (no changes)
2005: https://narodne-novine.nn.hr/eli/sluzbeni/2005/112/2062 (no changes)
2002: https://narodne-novine.nn.hr/eli/sluzbeni/2002/136/2194
2002: https://narodne-novine.nn.hr/eli/sluzbeni/2002/13/318
2001: https://narodne-novine.nn.hr/eli/sluzbeni/2001/96/1614
1996: https://narodne-novine.nn.hr/eli/sluzbeni/1996/33/674
"""


class hr_HR(Locale):
    """
    01-01: [NF] Nova Godina
    01-06: [NRF] Bogojavljenje
    05-01: [NF] Praznik rada
    06-22: [NF] Dan antifašističke borbe
    08-15: [NRF] Velika Gospa
    11-01: [NRF] Svi sveti
    12-25: [NRF] Božić
    12-26: [NRF] Sveti Stjepan
    Easter: [NRV] Uskrs
    1 day after Easter: [NRV] Uskrsni ponedjeljak
    60 days after Easter: [NRV] Tijelovo
    """

    locale = "hr-HR"
    easter_type = EASTER_WESTERN

    def holiday_dan_neovisnosti(self):
        if self.year < 2020:
            return [Holiday(
                self.locale,
                "",
                SmartDayArrow(self.year, 10, 8),
                "Dan neovisnosti",
                "NF"
            )]
        else:
            return []

    def holiday_dan_pobjede_i_domovinske_zahvalnosti_i_dan_hrvatskih_branitelja(self):
        if self.year >= 2008:
            name = "Dan pobjede i domovinske zahvalnosti i Dan hrvatskih branitelja"
        else:
            name = "Dan pobjede i domovinske zahvalnosti"

        return [Holiday(
            self.locale,
            "",
            SmartDayArrow(self.year, 8, 5),
            name,
            "NF"
        )]

    def holiday_dan_drzavnosti(self):
        if self.year >= 2020:
            date = SmartDayArrow(self.year, 5, 30)
        else:
            date = SmartDayArrow(self.year, 6, 25)

        return [Holiday(
            self.locale,
            "",
            date,
            "Dan državnosti",
            "NF"
        )]

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
