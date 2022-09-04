# coding=utf-8
from dateutil.easter import EASTER_WESTERN

from holidata.utils import SmartDayArrow
from .holidays import Locale, Holiday

"""
source: https://almanakka.helsinki.fi/en/flag-days-and-holidays-in-finland.html
"""


class fi_FI(Locale):
    """
    01-01: [NF] Uudenvuodenpäivä
    01-06: [NRF] Loppiainen
    05-01: [NF] Vappu
    12-06: [NF] Itsenäisyyspäivä
    12-25: [NRF] Joulupäivä
    12-26: [NRF] Tapaninpäivä
    2 days before Easter: [NRV] Pitkäperjantai
    Easter: [NRV] Pääsiäispäivä
    1 day after Easter: [NRV] 2. pääsiäispäivä
    39 days after Easter: [NRV] Helatorstai
    49 days after Easter: [NRV] Helluntaipäivä
    """

    locale = "fi-FI"
    easter_type = EASTER_WESTERN

    def holiday_juhannuspaeivae(self):
        """
        Saturday between 20 and 26 June: Juhannuspäivä (Midsummer Day)
        """
        return [Holiday(
            self.locale,
            "",
            SmartDayArrow(self.year, 6, 19).shift_to_weekday("saturday", order=1, reverse=False),
            "Juhannuspäivä",
            "NRV"
        )]

    def holiday_pyhaeinpaeivae(self):
        """
        Saturday between 31 October and 6 November: Pyhäinpäivä (All Saints' Day)
        """
        return [Holiday(
            self.locale,
            "",
            SmartDayArrow(self.year, 10, 30).shift_to_weekday("saturday", order=1, reverse=False),
            "Pyhäinpäivä",
            "NRV"
        )]
