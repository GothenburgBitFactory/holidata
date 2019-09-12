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
    11-01: [BW,BY,NW,RP,SL] [NRF] Allerheiligen
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
    60 days after Easter: [BW,BY,HE,NW,RP,SL] [NRV] Fronleichnam
    """

    locale = "de-DE"

    def holiday_buss_und_bettag(self, year):
        u"""11 days before 4. sunday before 12-25: [NRV] Buß- und Bettag"""

        return [Holiday(
            self.locale,
            "SN",
            SmartDayArrow(self.year, 12, 25).shift_to_weekday('sunday', order=4, reverse=True).shift(days=-11),
            "Buß- und Bettag",
            "NRV",
            postpone=self.postpone
        )]

    def holiday_reformationstag(self, year):
        u"""
        10 - 31: [NRF] Reformationstag

        before 2018: [BB, MV, SN, ST, TH]
        since 2018: [BB, BH, HH, MV, NI, SH, SN, ST, TH]
        2017: national holiday because of 500th anniversary
        """
        if year == 2017:
            regions = [""]
        elif year < 2018:
            regions = ["BB", "MV", "SN", "ST", "TH"]
        else:
            regions = ["BB", "BH", "HH", "MV", "NI", "SH", "SN", "ST", "TH"]

        return [Holiday(
            self.locale,
            region,
            SmartDayArrow(self.year, 10, 31),
            "Reformationstag",
            "NRF",
            postpone=self.postpone
        ) for region in regions]
