# coding=utf-8
from dateutil.easter import EASTER_WESTERN

from holidata.utils import SmartDayArrow
from .holidays import Holiday, Locale


class en_AU(Locale):
    """
    01-01: [NF] New Year's Day
    01-26: [NF] Australia Day
    04-25: [NF] Anzac Day
    12-25: [NRF] Christmas Day
    12-26: [NF] Boxing Day
    2 days before Easter: [NRV] Good Friday
    1 day before Easter: [ACT,NT,NSW,QLD,SA,VIC] [RV] Easter Saturday
    1 day after Easter: [NRV] Easter Monday
    2 days after Easter: [TAS] [RV] Easter Tuesday
    1. monday in march: [WA] [V] Labour Day
    2. monday in march: [ACT] [V] Canberra Day
    2. monday in march: [SA] [V] Adelaide Cup Day
    2. monday in march: [TAS] [V] Eight Hours Day
    2. monday in march: [VIC] [V] Labour Day
    1. monday in may: [NT] [V] May Day
    1. monday in may: [QLD] [V] Labour Day
    1. monday in june: [WA] [V] Western Australia Day
    2. monday in june: [ACT,NT,NSW,SA,TAS,VIC] [V] Queen's Birthday
    1. monday in august: [NT] [V] Picnic Day
    1. monday in october: [ACT,NSW,SA] [V] Labour Day
    1. monday in october: [QLD] [V] Queen's Birthday
    1. tuesday in november: [VIC] [V] Melbourne Cup
    """

    locale = "en-AU"
    easter_type = EASTER_WESTERN

    def holiday_new_years_day_observed(self):
        date = SmartDayArrow(self.year, 1, 1)

        if date.weekday() in ["saturday", "sunday"]:
            return [
                Holiday(
                    locale=self.locale,
                    region="",
                    date=date.shift_to_weekday("monday", including=True),
                    description="New Year's Day (observed)",
                    flags="NV",
                    notes="",
                )
            ]
        return []

    def holiday_australia_day_observed(self):
        date = SmartDayArrow(self.year, 1, 26)

        if date.weekday() in ["saturday", "sunday"]:
            return [
                Holiday(
                    locale=self.locale,
                    region="",
                    date=date.shift_to_weekday("monday", including=True),
                    description="Australia Day (observed)",
                    flags="NV",
                    notes="",
                )
            ]
        return []

    def holiday_anzac_day_observed(self):
        date = SmartDayArrow(self.year, 4, 25)

        if date.weekday() in ["saturday", "sunday"]:
            return [
                Holiday(
                    locale=self.locale,
                    region=region,
                    date=date.shift_to_weekday("monday", including=True),
                    description="Anzac Day (observed)",
                    flags="V",
                    notes="",
                )
                for region in ["ACT", "NT", "QLD", "SA"]
            ]
        return []

    def holiday_reconciliation_day(self):
        return [
            Holiday(
                locale=self.locale,
                region="ACT",
                date=SmartDayArrow(self.year, 5, 27).shift_to_weekday(
                    "monday", order=1, reverse=False, including=True
                ),
                description="Reconciliation Day",
                flags="V",
                notes="",
            )
        ]

    def holiday_christmas_day_observed(self):
        date = SmartDayArrow(self.year, 12, 25)

        if date.weekday() == "saturday":
            return [
                Holiday(
                    locale=self.locale,
                    region="",
                    date=date.shift_to_weekday("monday", including=True),
                    description="Christmas Day (observed)",
                    flags="NV",
                    notes="",
                )
            ]
        elif date.weekday() == "sunday":
            return [
                Holiday(
                    locale=self.locale,
                    region="",
                    date=date.shift_to_weekday("tuesday", including=True),
                    description="Christmas Day (observed)",
                    flags="NV",
                    notes="",
                )
            ]
        return []

    def holiday_boxing_day_observed(self):
        date = SmartDayArrow(self.year, 12, 26)

        if date.weekday() == "saturday":
            return [
                Holiday(
                    locale=self.locale,
                    region="",
                    date=date.shift_to_weekday("monday", including=True),
                    description="Boxing Day (observed)",
                    flags="NV",
                    notes="",
                )
            ]
        elif date.weekday() == "sunday":
            return [
                Holiday(
                    locale=self.locale,
                    region="",
                    date=date.shift_to_weekday("tuesday", including=True),
                    description="Boxing Day (observed)",
                    flags="NV",
                    notes="",
                )
            ]
        return []
