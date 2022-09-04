# coding=utf-8
from dateutil.easter import EASTER_WESTERN

from holidata.utils import SmartDayArrow
from .holidays import Locale, Holiday


class de_DE(Locale):
    """
    01-01: [NF] Neujahr
    01-06: [BW,BY,ST] [RF] Heilige drei Könige
    05-01: [NF] Erster Maifeiertag
    08-15: [SL] [RF] Mariä Himmelfahrt
    10-03: [NRF] Tag der Deutschen Einheit
    11-01: [BW,BY,NW,RP,SL] [RF] Allerheiligen
    12-24: [NRF] Heilig Abend
    12-25: [NRF] Weihnachtstag
    12-26: [NRF] Zweiter Weihnachtstag
    12-31: [NF] Silvester
    2 days before Easter: [NRV] Karfreitag
    Easter: [NRV] Ostern
    1 day after Easter: [NRV] Ostermontag
    39 days after Easter: [NRV] Christi Himmelfahrt
    49 days after Easter: [NRV] Pfingstsonntag
    50 days after Easter: [NRV] Pfingstmontag
    60 days after Easter: [BW,BY,HE,NW,RP,SL] [RV] Fronleichnam
    """

    locale = "de-DE"
    easter_type = EASTER_WESTERN

    def holiday_buss_und_bettag(self):
        """11 days before 4. sunday before 12-25: [SN] [RV] Buß- und Bettag"""

        return [Holiday(
            self.locale,
            "SN",
            SmartDayArrow(self.year, 12, 25).shift_to_weekday("sunday", order=4, reverse=True).shift(days=-11),
            "Buß- und Bettag",
            "RV"
        )]

    def holiday_reformationstag(self):
        """
        before 2018: 10-31: [BB, MV, SN, ST, TH] [RF] Reformationstag
        since 2018:  10-31: [BB, BH, HH, MV, NI, SH, SN, ST, TH] [RF] Reformationstag
        2017:        10-31: [NRF] Reformationstag (national holiday because of 500th anniversary)

        """
        if self.year == 2017:
            regions = [""]
        elif self.year < 2018:
            regions = ["BB", "MV", "SN", "ST", "TH"]
        else:
            regions = ["BB", "BH", "HH", "MV", "NI", "SH", "SN", "ST", "TH"]

        return [Holiday(
            self.locale,
            region,
            SmartDayArrow(self.year, 10, 31),
            "Reformationstag",
            "NRF" if regions == [""] else "RF"
        ) for region in regions]

    def holiday_frauentag(self):
        """
        03-08: [BE] [F] Frauentag

        Introduced 2019 for Berlin
        http://gesetze.berlin.de/jportal/?quelle=jlink&query=FeiertG+BE+%C2%A7+1&psml=bsbeprod.psml&max=true
        """
        if self.year >= 2019:
            return [Holiday(
                self.locale,
                "BE",
                SmartDayArrow(self.year, 3, 8),
                "Internationaler Frauentag",
                "F"
            )]
        else:
            return []

    def holiday_tag_der_befreiung(self):
        """
        2020-05-08: [BE] [F] 75. Jahrestag der Befreiung vom Nationalsozialismus und der Beendigung des Zweiten Weltkrieges in Europa

        Introduced 2019 for Berlin
        http://gesetze.berlin.de/jportal/?quelle=jlink&query=FeiertG+BE+%C2%A7+1&psml=bsbeprod.psml&max=true
        """
        if self.year == 2020:
            return [Holiday(
                self.locale,
                "BE",
                SmartDayArrow(self.year, 5, 8),
                "75. Jahrestag der Befreiung vom Nationalsozialismus und der Beendigung des Zweiten Weltkrieges in Europa",
                "F"
            )]
        else:
            return []
