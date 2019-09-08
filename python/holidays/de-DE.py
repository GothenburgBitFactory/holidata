from .holidays import Locale

from plugin import Holiday
from utils import SmartDayArrow


class de_DE(Locale):
    u"""
    01-01: [NF] Neujahr
    01-06: [BW,BY,ST] [NRF] Heilige drei Könige
    05-01: [NF] Erster Maifeiertag
    08-15: [SL] [NRF] Mariä Himmelfahrt
    10-03: [NRF] Tag der Deutschen Einheit
    10-31: [BB,MV,SN,ST,TH] [NRF] Reformationstag
    11-01: [BW,BY,NRW,RP,SL] [NRF] Allerheiligen
    12-24: [NRF] Heilig Abend
    12-25: [NRF] Weihnachtstag
    12-26: [NRF] Zweiter Weihnachtstag
    12-31: [NF] Silvester
    2 days before Easter: [NRV] Karfreitag
    0 days after Easter: [NRV] Ostern
    1 day after Easter: [NRV] Ostermontag
    39 days after Easter: [NRV] Christi Himmelfahrt
    49 days after Easter: [NRV] Pfingstsonntag
    50 days after Easter: [NRV] Pfingstmontag
    60 days after Easter: [BW,BY,HE,NRW,RP,SL] [NRV] Fronleichnam
    """

    locale = "de-DE"

    def holiday_buss_und_bettag(self, year):
        """11 days before 4. sunday before 12-25: [NRV] Buß- und Bettag"""

        return Holiday(
            self.locale,
            "SN",
            SmartDayArrow(self.year, 12, 25).shift_to_weekday('sunday', order=4, reverse=True).shift(days=-11),
            "Buß- und Bettag",
            "NRV",
            postpone=self.postpone
        )
