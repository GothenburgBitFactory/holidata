from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import day, date, first, Month, Weekday

__all__ = [
    "SG",
]

"""
Legal sources:
- Holidays Act 1998 https://sso.agc.gov.sg/Act/HA1998
- Parliamentary Elections Act 1954 https://sso.agc.gov.sg/Act/PEA1954
- Presidential Elections Act 1991 https://sso.agc.gov.sg/Act/PrEA1991

- https://www.mom.gov.sg/employment-practices/public-holidays
- https://www.mom.gov.sg/employment-practices/public-holidays-entitlement-and-pay
"""


class SG(Country):
    id = "SG"
    languages = ["en"]
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("New Year's Day") \
            .on(date(Month.JANUARY, 1)) \
            .with_flags("NF") \

        self.define_holiday() \
            .with_name("New Year's Day (in lieu)") \
            .on(first(Weekday.MONDAY).after(date(Month.JANUARY, 1))) \
            .with_flags("NF") \
            .on_condition(date(Month.JANUARY, 1).is_a(Weekday.SUNDAY))

        self.define_holiday() \
            .with_name("Chinese New Year") \
            .on(SG.chinese_new_year) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Chinese New Year (Second Day)") \
            .on(SG.chinese_new_year_day2) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Chinese New Year (in lieu)") \
            .on(SG.chinese_new_year_in_lieu) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Good Friday") \
            .on(day(2).before(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Labour Day") \
            .on(date(Month.MAY, 1)) \
            .with_flags("NF") \

        self.define_holiday() \
            .with_name("Labour Day (in lieu)") \
            .on(first(Weekday.MONDAY).after(date(Month.MAY, 1))) \
            .with_flags("NF") \
            .on_condition(date(Month.MAY, 1).is_a(Weekday.SUNDAY))

        self.define_holiday() \
            .with_name("Hari Raya Puasa") \
            .on(SG.hari_raya_puasa) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Hari Raya Puasa (in lieu)") \
            .on(SG.hari_raya_puasa_in_lieu) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Vesak Day") \
            .on(SG.vesak_day) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Vesak Day (in lieu)") \
            .on(SG.vesak_day_in_lieu) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Hari Raya Haji") \
            .on(SG.hari_raya_haji) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Hari Raya Haji (in lieu)") \
            .on(SG.hari_raya_haji_in_lieu) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("National Day") \
            .on(date(Month.AUGUST, 9)) \
            .with_flags("NF") \

        self.define_holiday() \
            .with_name("National Day (in lieu)") \
            .on(first(Weekday.MONDAY).after(date(Month.AUGUST, 9))) \
            .with_flags("NF") \
            .on_condition(date(Month.AUGUST, 9).is_a(Weekday.SUNDAY))

        self.define_holiday() \
            .with_name("Deepavali") \
            .on(SG.deepavali) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Deepavali (in lieu)") \
            .on(SG.deepavali_in_lieu) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Christmas Day") \
            .on(date(Month.DECEMBER, 25)) \
            .with_flags("NRF") \

        self.define_holiday() \
            .with_name("Christmas Day (in lieu)") \
            .on(first(Weekday.MONDAY).after(date(Month.DECEMBER, 25))) \
            .with_flags("NRF") \
            .on_condition(date(Month.DECEMBER, 25).is_a(Weekday.SUNDAY))

        """
        General Election day
        Holiday according to Section 35 of the Parliamentary Elections Act
        """
        self.define_holiday() \
            .with_name("General Election") \
            .on(SG.date_of_general_election) \
            .with_flags("NF")

        """
        Presidential Election day
        Holiday according to Section 17 of the Presidential Elections Act
        """
        self.define_holiday() \
            .with_name("Presidential Election") \
            .on(SG.date_of_presidential_election) \
            .with_flags("NF")

        """
        SG50 Public holiday
        Celebrating 50 years of independence from Malaysia
        """
        self.define_holiday() \
            .with_name("SG50 Public Holiday") \
            .on(date(Month.AUGUST, 7)) \
            .in_years([2015]) \
            .with_flags("NF")

    @staticmethod
    def date_of_general_election(year):
        dates = {
            2011: date(Month.MAY, 7),
            2015: date(Month.SEPTEMBER, 11),
            2020: date(Month.JULY, 10),
            2025: date(Month.MAY, 3),
        }
        return dates.get(year)(year) if year in dates else None

    @staticmethod
    def date_of_presidential_election(year):
        dates = {
            2011: date(Month.AUGUST, 27),
            2017: date(Month.SEPTEMBER, 13),
            2023: date(Month.SEPTEMBER, 1),
        }
        return dates.get(year)(year) if year in dates else None

    @staticmethod
    def chinese_new_year(year):
        """Return the date of Chinese New Year for the given year."""
        dates = {
            2011: date(Month.FEBRUARY, 3),
            2012: date(Month.JANUARY, 23),
            2013: date(Month.FEBRUARY, 10),
            2014: date(Month.JANUARY, 31),
            2015: date(Month.FEBRUARY, 19),
            2016: date(Month.FEBRUARY, 8),
            2017: date(Month.JANUARY, 28),
            2018: date(Month.FEBRUARY, 16),
            2019: date(Month.FEBRUARY, 5),
            2020: date(Month.JANUARY, 25),
            2021: date(Month.FEBRUARY, 12),
            2022: date(Month.FEBRUARY, 1),
            2023: date(Month.JANUARY, 22),
            2024: date(Month.FEBRUARY, 10),
            2025: date(Month.JANUARY, 29),
            2026: date(Month.FEBRUARY, 17)
        }
        return dates.get(year)(year) if year in dates else None

    @staticmethod
    def chinese_new_year_day2(year):
        """Return the date of the second day of Chinese New Year."""
        first_day = SG.chinese_new_year(year)
        return first_day.shift(days=1) if first_day is not None else None

    @staticmethod
    def chinese_new_year_in_lieu(year):
        holiday_date = SG.chinese_new_year(year)
        if holiday_date is not None and holiday_date.weekday() == Weekday.SATURDAY:
            return holiday_date.shift_to_weekday(Weekday.MONDAY)
        elif holiday_date is not None and holiday_date.weekday() == Weekday.SUNDAY:
            return holiday_date.shift_to_weekday(Weekday.TUESDAY)
        return None

    @staticmethod
    def hari_raya_puasa(year):
        """Return the date of Hari Raya Puasa for the given year."""
        dates = {
            2011: date(Month.AUGUST, 30),
            2012: date(Month.AUGUST, 19),
            2013: date(Month.AUGUST, 8),
            2014: date(Month.JULY, 28),
            2015: date(Month.JULY, 17),
            2016: date(Month.JULY, 6),
            2017: date(Month.JUNE, 25),
            2018: date(Month.JUNE, 15),
            2019: date(Month.JUNE, 5),
            2020: date(Month.MAY, 24),
            2021: date(Month.MAY, 13),
            2022: date(Month.MAY, 3),
            2023: date(Month.APRIL, 22),
            2024: date(Month.APRIL, 10),
            2025: date(Month.MARCH, 31),
            2026: date(Month.MARCH, 21)
        }
        return dates.get(year)(year) if year in dates else None

    @staticmethod
    def hari_raya_puasa_in_lieu(year):
        holiday_date = SG.hari_raya_puasa(year)
        if holiday_date is not None and holiday_date.weekday() == Weekday.SUNDAY:
            return holiday_date.shift_to_weekday(Weekday.MONDAY)
        return None

    @staticmethod
    def vesak_day(year):
        """Return the date of Vesak Day for the given year."""
        dates = {
            2011: date(Month.MAY, 17),
            2012: date(Month.MAY, 5),
            2013: date(Month.MAY, 24),
            2014: date(Month.MAY, 13),
            2015: date(Month.JUNE, 1),
            2016: date(Month.MAY, 21),
            2017: date(Month.MAY, 10),
            2018: date(Month.MAY, 29),
            2019: date(Month.MAY, 19),
            2020: date(Month.MAY, 7),
            2021: date(Month.MAY, 26),
            2022: date(Month.MAY, 15),
            2023: date(Month.JUNE, 2),
            2024: date(Month.MAY, 22),
            2025: date(Month.MAY, 12),
            2026: date(Month.MAY, 31)
        }
        return dates.get(year)(year) if year in dates else None

    @staticmethod
    def vesak_day_in_lieu(year):
        holiday_date = SG.vesak_day(year)
        if holiday_date is not None and holiday_date.weekday() == Weekday.SUNDAY:
            return holiday_date.shift_to_weekday(Weekday.MONDAY)
        return None

    @staticmethod
    def hari_raya_haji(year):
        """Return the date of Hari Raya Haji for the given year."""
        dates = {
            2011: date(Month.NOVEMBER, 6),
            2012: date(Month.OCTOBER, 26),
            2013: date(Month.OCTOBER, 15),
            2014: date(Month.OCTOBER, 5),
            2015: date(Month.SEPTEMBER, 24),
            2016: date(Month.SEPTEMBER, 12),
            2017: date(Month.SEPTEMBER, 1),
            2018: date(Month.AUGUST, 22),
            2019: date(Month.AUGUST, 11),
            2020: date(Month.JULY, 31),
            2021: date(Month.JULY, 20),
            2022: date(Month.JULY, 10),
            2023: date(Month.JUNE, 29),
            2024: date(Month.JUNE, 17),
            2025: date(Month.JUNE, 7),
            2026: date(Month.MAY, 27)
        }
        return dates.get(year)(year) if year in dates else None

    @staticmethod
    def hari_raya_haji_in_lieu(year):
        holiday_date = SG.hari_raya_haji(year)
        if holiday_date is not None and holiday_date.weekday() == Weekday.SUNDAY:
            return holiday_date.shift_to_weekday(Weekday.MONDAY)
        return None

    @staticmethod
    def deepavali(year):
        """Return the date of Deepavali for the given year."""
        dates = {
            2011: date(Month.OCTOBER, 26),
            2012: date(Month.NOVEMBER, 13),
            2013: date(Month.NOVEMBER, 2),
            2014: date(Month.OCTOBER, 22),
            2015: date(Month.NOVEMBER, 10),
            2016: date(Month.OCTOBER, 29),
            2017: date(Month.OCTOBER, 18),
            2018: date(Month.NOVEMBER, 6),
            2019: date(Month.OCTOBER, 27),
            2020: date(Month.NOVEMBER, 14),
            2021: date(Month.NOVEMBER, 4),
            2022: date(Month.OCTOBER, 24),
            2023: date(Month.NOVEMBER, 12),
            2024: date(Month.OCTOBER, 31),
            2025: date(Month.OCTOBER, 20),
            2026: date(Month.NOVEMBER, 8)
        }
        return dates.get(year)(year) if year in dates else None

    @staticmethod
    def deepavali_in_lieu(year):
        holiday_date = SG.deepavali(year)
        if holiday_date is not None and holiday_date.weekday() == Weekday.SUNDAY:
            return holiday_date.shift_to_weekday(Weekday.MONDAY)
        return None
