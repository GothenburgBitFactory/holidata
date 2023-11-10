# coding=utf-8
from dateutil.easter import EASTER_WESTERN

from holidata.utils import SmartDayArrow
from .holidays import Holiday, Locale


class nl_NL(Locale):
    """
    01-01: [NF] Nieuwjaarsdag
    05-04: [NF] Dodenherdenking
    05-05: [NF] Bevrijdingsdag
    12-05: [NRF] Sinterklaas
    12-25: [NRF] Eerste Kerstdag
    12-26: [NRF] Tweede Kerstdag
    2 days before Easter: [NRV] Goede Vrijdag
    Easter: [NRV] Eerste Paasdag
    1 day after Easter: [NRV] Tweede Paasdag
    39 days after Easter: [NRV] Hemelvaartsdag
    49 days after Easter: [NRV] Eerste Pinksterdag
    50 days after Easter: [NRV] Tweede Pinksterdag
    """

    id = "nl-NL"
    easter_type = EASTER_WESTERN

    def holiday_koninginnedag(self, year):
        """
        04-27 or saturday before, if it falls on sunday: [NF] Koninginnedag
        Until 2013
        """
        if year > 2013:
            return []

        date = SmartDayArrow(year, 4, 30)

        if date.weekday() == "sunday":
            date = date.shift(days=-1)

        return [Holiday(
            locale=self.id,
            region="",
            date=date,
            description="Koninginnedag",
            flags="NV",
            notes="")]

    def holiday_koningsdag(self, year):
        """
        04-27 or saturday before if it falls on sunday: [NF] Koningsdag
        Since 2014
        """
        if year < 2014:
            return []

        date = SmartDayArrow(year, 4, 27)

        if date.weekday() == "sunday":
            date = date.shift(days=-1)

        return [Holiday(
            locale=self.id,
            region="",
            date=date,
            description="Koningsdag",
            flags="NV",
            notes="")]

    def holiday_koninkrijksdag(self, year):
        date = SmartDayArrow(year, 12, 15)

        if date.weekday() == "sunday":
            date = date.shift(days=1)

        return [Holiday(
            locale=self.id,
            region="",
            date=date,
            description="Koninkrijksdag",
            flags="NV",
            notes="")]
