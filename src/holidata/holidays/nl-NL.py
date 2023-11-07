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

    locale = "nl-NL"
    easter_type = EASTER_WESTERN

    def holiday_koningsdag(self):
        """04-27 or saturday before if it falls on sunday: [NF] Koninginnedag/Koningsdag"""
        if self.year < 2014:
            date = SmartDayArrow(self.year, 4, 30)
            description = "Koninginnedag"
        else:
            date = SmartDayArrow(self.year, 4, 27)
            description = "Koningsdag"

        if date.weekday() == "sunday":
            date = date.shift(days=-1)

        return [Holiday(
            locale=self.locale,
            region="",
            date=date,
            description=description,
            flags="NV",
            notes="")]

    def holiday_koninkrijksdag(self):
        date = SmartDayArrow(self.year, 12, 15)

        if date.weekday() == "sunday":
            date = date.shift(days=1)

        return [Holiday(
            locale=self.locale,
            region="",
            date=date,
            description="Koninkrijksdag",
            flags="NV",
            notes="")]
