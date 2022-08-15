# coding=utf-8
from dateutil.easter import EASTER_WESTERN

from holidata.utils import SmartDayArrow
from .holidays import Locale, Holiday

"""
sources: http://www.pisrs.si/Pis.web/pregledPredpisa?id=ZAKO865#
"""


class sl_SI(Locale):
    """
    01-01: [NF] Novo leto
    02-08: [NF] Prešernov dan
    04-27: [NF] Dan upora proti okupatorju
    05-01: [NF] Praznik dela
    05-02: [NF] Praznik dela
    06-25: [NF] Dan državnosti
    08-15: [NRF] Marijino vnebovzetje
    10-31: [NRF] Dan reformacije
    11-01: [NF] Dan spomina na mrtve
    12-25: [NF] Božič
    12-26: [NF] Dan samostojnosti in enotnosti
    Easter: [NRV] Velikonočna nedelja
    1 day after Easter: [NRV] Velikonočni ponedeljek
    50 days after Easter: [NRV] Binkošti
    """

    locale = "sl-SI"
    easter_type = EASTER_WESTERN

    def holiday_novo_leto(self):
        """
        From 1955 until May 2012, when the National Assembly of Slovenia passed the Public Finance Balance Act,
        2 January was a work-free day. It was reintroduced in 2017.
        2012<: https://www.uradni-list.si/1/objava.jsp?sop=2012-01-1700
        2016<: https://www.uradni-list.si/1/objava.jsp?sop=2016-01-3568
        """
        return [Holiday(
            self.locale,
            "",
            SmartDayArrow(self.year, 1, 2),
            "Novo leto",
            "NF"
        )] if self.year not in [2013, 2014, 2015, 2016] else []
