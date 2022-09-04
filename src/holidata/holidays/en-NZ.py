# coding=utf-8
from dateutil.easter import EASTER_WESTERN

from holidata.utils import SmartDayArrow
from .holidays import Holiday, Locale


class en_NZ(Locale):
    """
    01-01: [NF] New Year's Day
    02-06: [NF] Waitangi Day
    04-25: [NF] ANZAC Day
    12-25: [NRF] Christmas Day
    12-26: [NF] Boxing Day
    2 days before Easter: [NRV] Good Friday
    1 day after Easter: [NRV] Easter Monday
    1. monday in june: [NV] Queen's Birthday
    4. monday in october: [NV] Labour Day
    """

    locale = "en-NZ"
    easter_type = EASTER_WESTERN

    def holiday_new_years_day_observed(self):
        date = SmartDayArrow(self.year, 1, 1)

        if date.weekday() in ["saturday", "sunday"]:
            return [Holiday(
                    locale=self.locale,
                    region="",
                    date=date.shift_to_weekday("monday", including=True),
                    description="New Year's Day (observed)",
                    flags="NV",
                    notes="")]

        return []

    def holiday_after_new_years_day(self):
        date = SmartDayArrow(self.year, 1, 2)

        if date.weekday() in ["sunday", "monday"]:
            return [Holiday(
                locale=self.locale,
                region="",
                date=date.shift_to_weekday("tuesday", including=True),
                description="Day after New Year's Day",
                flags="NV",
                notes="")]

        elif date.weekday() == "saturday":
            return [Holiday(
                locale=self.locale,
                region="",
                date=date.shift_to_weekday("monday", including=True),
                description="Day after New Year's Day",
                flags="NV",
                notes="")]

        return [Holiday(
                locale=self.locale,
                region="",
                date=date,
                description="Day after New Year's Day",
                flags="NV",
                notes="")]

    def holiday_waitangi_day_observed(self):
        date = SmartDayArrow(self.year, 2, 6)

        if self.year > 2016 and date.weekday() in ["saturday", "sunday"]:
            return [Holiday(
                    locale=self.locale,
                    region="",
                    date=date.shift_to_weekday("monday", including=True),
                    description="Waitangi Day (observed)",
                    flags="NV",
                    notes="")]

        return []

    def holiday_anzac_day_observed(self):
        date = SmartDayArrow(self.year, 4, 25)

        if self.year > 2015 and date.weekday() in ["saturday", "sunday"]:
            return [Holiday(
                    locale=self.locale,
                    region="",
                    date=date.shift_to_weekday("monday", including=True),
                    description="ANZAC Day (observed)",
                    flags="NV",
                    notes="")]

        return []

    def holiday_christmas_day_observed(self):
        date = SmartDayArrow(self.year, 12, 25)

        if date.weekday() == "sunday":
            return [Holiday(
                locale=self.locale,
                region="",
                date=date.shift_to_weekday("tuesday", including=True),
                description="Christmas Day (observed)",
                flags="NV",
                notes="")]

        elif date.weekday() == "saturday":
            return [Holiday(
                locale=self.locale,
                region="",
                date=date.shift_to_weekday("monday", including=True),
                description="Christmas Day (observed)",
                flags="NV",
                notes="")]

        return []

    def holiday_boxing_day_observed(self):
        date = SmartDayArrow(self.year, 12, 26)

        if date.weekday() == "sunday":
            return [Holiday(
                locale=self.locale,
                region="",
                date=date.shift_to_weekday("tuesday", including=True),
                description="Boxing Day (observed)",
                flags="NV",
                notes="")]

        elif date.weekday() == "saturday":
            return [Holiday(
                locale=self.locale,
                region="",
                date=date.shift_to_weekday("monday", including=True),
                description="Boxing Day (observed)",
                flags="NV",
                notes="")]

        return []
