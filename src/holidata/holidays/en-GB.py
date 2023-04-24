# coding=utf-8
from dateutil.easter import EASTER_WESTERN

from holidata.utils import SmartDayArrow, month_reference
from .holidays import Holiday, Locale


class en_GB(Locale):
    """
    01-01: [NF] New Year's Day
    12-25: [NRF] Christmas Day
    12-26: [NF] Boxing Day
    2 days before Easter: [NRV] Good Friday
    1 day after Easter: [NRV] Easter Monday
    1. monday in may: [NV] Early May Bank Holiday
    1. last monday in august: [NV] August Bank Holiday
    """

    locale = "en-GB"
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

    def holiday_spring_bank_holiday(self):
        """
        1. last monday in may: [NV] Spring Bank Holiday
        2012: Moved to June 4, because of Queen’s Diamond Jubilee
        2022: Moved to June 2, because of Queen's Platinum Jubilee
        """
        if self.year == 2012:
            date = SmartDayArrow(self.year, 6, 4)
        elif self.year == 2022:
            date = SmartDayArrow(self.year, 6, 2)
        else:
            date = month_reference(self.year,
                                   "may",
                                   first=False) \
                .shift_to_weekday("monday",
                                  order=1,
                                  reverse=True,
                                  including=True)

        return [Holiday(
            locale=self.locale,
            region="",
            date=date,
            description="Spring Bank Holiday",
            flags="NV",
            notes="")]

    def holiday_christmas_day_observed(self):
        date = SmartDayArrow(self.year, 12, 25)

        if date.weekday() == "saturday":
            return [Holiday(
                    locale=self.locale,
                    region="",
                    date=date.shift_to_weekday("monday", including=True),
                    description="Christmas Day (observed)",
                    flags="NV",
                    notes="")]

        elif date.weekday() == "sunday":
            return [Holiday(
                    locale=self.locale,
                    region="",
                    date=date.shift_to_weekday("tuesday", including=True),
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

    def holiday_coronation_charles_iii(self):
        """
        2023-05-08: Bank holiday for the coronation of King Charles III
        """
        if self.year == 2023:
            return [Holiday(
                locale=self.locale,
                region="",
                date=SmartDayArrow(self.year, 5, 8),
                description="Coronation of King Charles III",
                flags="NV",
                notes="")]

        return []

    def holiday_royal_jubilees(self):
        """
        2012-06-05: Queen's Diamond Jubilee
        2022-06-03: Queen's Platinum Jubilee
        """
        if self.year == 2012:
            return [Holiday(
                locale=self.locale,
                region="",
                date=SmartDayArrow(self.year, 6, 5),
                description="Queen's Diamond Jubilee",
                flags="NV",
                notes="")]

        if self.year == 2022:
            return [Holiday(
                locale=self.locale,
                region="",
                date=SmartDayArrow(self.year, 6, 3),
                description="Queen's Platinum Jubilee",
                flags="NV",
                notes="")]

        return []

    def holiday_state_funeral_of_queen_elizabeth_ii(self):
        if self.year == 2022:
            return [Holiday(
                locale=self.locale,
                region="",
                date=SmartDayArrow(self.year, 9, 19),
                description="State Funeral of Queen Elizabeth II",
                flags="NF",
                notes="")]

        return []
