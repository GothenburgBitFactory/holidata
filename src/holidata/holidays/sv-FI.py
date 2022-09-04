# coding=utf-8
from dateutil.easter import EASTER_WESTERN

from holidata.utils import SmartDayArrow
from .holidays import Locale, Holiday

"""
source: https://almanakka.helsinki.fi/en/flag-days-and-holidays-in-finland.html
"""


class sv_FI(Locale):
    """
    01-01: [NF] Nyårsdagen
    01-06: [NRF] Trettondedagen
    05-01: [NF] Första maj
    12-06: [NF] Självständighetsdagen
    12-25: [NRF] Juldagen
    12-26: [NRF] Annandag jul
    2 days before Easter: [NRV] Långfredagen
    Easter: [NRV] Påskdagen
    1 day after Easter: [NRV] Annandag påsk
    39 days after Easter: [NRV] Kristi himmelfärdsdag
    49 days after Easter: [NRV] Pingst
    """

    locale = "sv-FI"
    easter_type = EASTER_WESTERN

    def holiday_midsommardagen(self):
        """
        Saturday between 20 and 26 June: Midsommardagen
        """
        return [Holiday(
            self.locale,
            "",
            SmartDayArrow(self.year, 6, 19).shift_to_weekday("saturday", order=1, reverse=False),
            "Midsommardagen",
            "NRV"
        )]

    def holiday_alla_helgons_dag(self):
        """
        Saturday between 31 October and 6 November: Alla helgons dag (All Saints' Day)
        """
        return [Holiday(
            self.locale,
            "",
            SmartDayArrow(self.year, 10, 30).shift_to_weekday("saturday", order=1, reverse=False),
            "Alla helgons dag",
            "NRV"
        )]
