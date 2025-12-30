from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import day, date, first

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
            .on(date(month=1, day=1)) \
            .with_flags("NF") \

        self.define_holiday() \
            .with_name("New Year's Day (in lieu)") \
            .on(first("monday").after(date(month=1, day=1))) \
            .with_flags("NF") \
            .on_condition(date(month=1, day=1).is_a("sunday"))

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
            .on(date(month=5, day=1)) \
            .with_flags("NF") \

        self.define_holiday() \
            .with_name("Labour Day (in lieu)") \
            .on(first("monday").after(date(month=5, day=1))) \
            .with_flags("NF") \
            .on_condition(date(month=5, day=1).is_a("sunday"))

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
            .on(date(month=8, day=9)) \
            .with_flags("NF") \

        self.define_holiday() \
            .with_name("National Day (in lieu)") \
            .on(first("monday").after(date(month=8, day=9))) \
            .with_flags("NF") \
            .on_condition(date(month=8, day=9).is_a("sunday"))

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
            .on(date(month=12, day=25)) \
            .with_flags("NRF") \

        self.define_holiday() \
            .with_name("Christmas Day (in lieu)") \
            .on(first("monday").after(date(month=12, day=25))) \
            .with_flags("NRF") \
            .on_condition(date(month=12, day=25).is_a("sunday"))

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
            .on(date(month=8, day=7)) \
            .in_years([2015]) \
            .with_flags("NF")

    @staticmethod
    def date_of_general_election(year):
        dates = {
            2011: date(month=5, day=7),
            2015: date(month=9, day=11),
            2020: date(month=7, day=10),
            2025: date(month=5, day=3),
        }
        return dates.get(year)(year) if year in dates else None

    @staticmethod
    def date_of_presidential_election(year):
        dates = {
            2011: date(month=8, day=27),
            2017: date(month=9, day=13),
            2023: date(month=9, day=1),
        }
        return dates.get(year)(year) if year in dates else None

    @staticmethod
    def chinese_new_year(year):
        """Return the date of Chinese New Year for the given year."""
        dates = {
            2011: date(2, 3),
            2012: date(1, 23),
            2013: date(2, 10),
            2014: date(1, 31),
            2015: date(2, 19),
            2016: date(2, 8),
            2017: date(1, 28),
            2018: date(2, 16),
            2019: date(2, 5),
            2020: date(1, 25),
            2021: date(2, 12),
            2022: date(2, 1),
            2023: date(1, 22),
            2024: date(2, 10),
            2025: date(1, 29),
            2026: date(2, 17)
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
        if holiday_date is not None and holiday_date.weekday() == "saturday":
            return holiday_date.shift_to_weekday("monday")
        elif holiday_date is not None and holiday_date.weekday() == "sunday":
            return holiday_date.shift_to_weekday("tuesday")
        return None

    @staticmethod
    def hari_raya_puasa(year):
        """Return the date of Hari Raya Puasa for the given year."""
        dates = {
            2011: date(8, 30),
            2012: date(8, 19),
            2013: date(8, 8),
            2014: date(7, 28),
            2015: date(7, 17),
            2016: date(7, 6),
            2017: date(6, 25),
            2018: date(6, 15),
            2019: date(6, 5),
            2020: date(5, 24),
            2021: date(5, 13),
            2022: date(5, 3),
            2023: date(4, 22),
            2024: date(4, 10),
            2025: date(3, 31),
            2026: date(3, 21)
        }
        return dates.get(year)(year) if year in dates else None

    @staticmethod
    def hari_raya_puasa_in_lieu(year):
        holiday_date = SG.hari_raya_puasa(year)
        if holiday_date is not None and holiday_date.weekday() == "sunday":
            return holiday_date.shift_to_weekday("monday")
        return None

    @staticmethod
    def vesak_day(year):
        """Return the date of Vesak Day for the given year."""
        dates = {
            2011: date(5, 17),
            2012: date(5, 5),
            2013: date(5, 24),
            2014: date(5, 13),
            2015: date(6, 1),
            2016: date(5, 21),
            2017: date(5, 10),
            2018: date(5, 29),
            2019: date(5, 19),
            2020: date(5, 7),
            2021: date(5, 26),
            2022: date(5, 15),
            2023: date(6, 2),
            2024: date(5, 22),
            2025: date(5, 12),
            2026: date(5, 31)
        }
        return dates.get(year)(year) if year in dates else None

    @staticmethod
    def vesak_day_in_lieu(year):
        holiday_date = SG.vesak_day(year)
        if holiday_date is not None and holiday_date.weekday() == "sunday":
            return holiday_date.shift_to_weekday("monday")
        return None

    @staticmethod
    def hari_raya_haji(year):
        """Return the date of Hari Raya Haji for the given year."""
        dates = {
            2011: date(11, 6),
            2012: date(10, 26),
            2013: date(10, 15),
            2014: date(10, 5),
            2015: date(9, 24),
            2016: date(9, 12),
            2017: date(9, 1),
            2018: date(8, 22),
            2019: date(8, 11),
            2020: date(7, 31),
            2021: date(7, 20),
            2022: date(7, 10),
            2023: date(6, 29),
            2024: date(6, 17),
            2025: date(6, 7),
            2026: date(5, 27)
        }
        return dates.get(year)(year) if year in dates else None

    @staticmethod
    def hari_raya_haji_in_lieu(year):
        holiday_date = SG.hari_raya_haji(year)
        if holiday_date is not None and holiday_date.weekday() == "sunday":
            return holiday_date.shift_to_weekday("monday")
        return None

    @staticmethod
    def deepavali(year):
        """Return the date of Deepavali for the given year."""
        dates = {
            2011: date(10, 26),
            2012: date(11, 13),
            2013: date(11, 2),
            2014: date(10, 22),
            2015: date(11, 10),
            2016: date(10, 29),
            2017: date(10, 18),
            2018: date(11, 6),
            2019: date(10, 27),
            2020: date(11, 14),
            2021: date(11, 4),
            2022: date(10, 24),
            2023: date(11, 12),
            2024: date(10, 31),
            2025: date(10, 20),
            2026: date(11, 8)
        }
        return dates.get(year)(year) if year in dates else None

    @staticmethod
    def deepavali_in_lieu(year):
        holiday_date = SG.deepavali(year)
        if holiday_date is not None and holiday_date.weekday() == "sunday":
            return holiday_date.shift_to_weekday("monday")
        return None
