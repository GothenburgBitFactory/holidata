from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import Month, Weekday, date, dates, day, first

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
            .on(SG.chinese_new_year()) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Chinese New Year (Second Day)") \
            .on(day(1).after(SG.chinese_new_year())) \
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
            .on(SG.hari_raya_puasa()) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Hari Raya Puasa (in lieu)") \
            .on(first(Weekday.MONDAY).after(SG.hari_raya_puasa())) \
            .with_flags("NRV") \
            .on_condition(SG.hari_raya_puasa().is_a(Weekday.SUNDAY))

        self.define_holiday() \
            .with_name("Vesak Day") \
            .on(SG.vesak_day()) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Vesak Day (in lieu)") \
            .on(first(Weekday.MONDAY).after(SG.vesak_day())) \
            .with_flags("NRV") \
            .on_condition(SG.vesak_day().is_a(Weekday.SUNDAY))

        self.define_holiday() \
            .with_name("Hari Raya Haji") \
            .on(SG.hari_raya_haji()) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Hari Raya Haji (in lieu)") \
            .on(day(1).after(SG.hari_raya_haji())) \
            .with_flags("NRV") \
            .on_condition(SG.hari_raya_haji().is_a(Weekday.SUNDAY))

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
            .on(SG.deepavali()) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Deepavali (in lieu)") \
            .on(day(1).after(SG.deepavali())) \
            .with_flags("NRV") \
            .on_condition(SG.deepavali().is_a(Weekday.SUNDAY))

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
            .on(dates({
                2011: (Month.MAY, 7),
                2015: (Month.SEPTEMBER, 11),
                2020: (Month.JULY, 10),
                2025: (Month.MAY, 3),
            })) \
            .with_flags("NF")

        """
        Presidential Election day
        Holiday according to Section 17 of the Presidential Elections Act
        """
        self.define_holiday() \
            .with_name("Presidential Election") \
            .on(dates({
                2011: (Month.AUGUST, 27),
                2017: (Month.SEPTEMBER, 13),
                2023: (Month.SEPTEMBER, 1),
            })) \
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
    def chinese_new_year():
        """Return the date of Chinese New Year for the given year."""
        return dates({
            2011: (Month.FEBRUARY, 3),
            2012: (Month.JANUARY, 23),
            2013: (Month.FEBRUARY, 10),
            2014: (Month.JANUARY, 31),
            2015: (Month.FEBRUARY, 19),
            2016: (Month.FEBRUARY, 8),
            2017: (Month.JANUARY, 28),
            2018: (Month.FEBRUARY, 16),
            2019: (Month.FEBRUARY, 5),
            2020: (Month.JANUARY, 25),
            2021: (Month.FEBRUARY, 12),
            2022: (Month.FEBRUARY, 1),
            2023: (Month.JANUARY, 22),
            2024: (Month.FEBRUARY, 10),
            2025: (Month.JANUARY, 29),
            2026: (Month.FEBRUARY, 17)
        })

    @staticmethod
    def chinese_new_year_in_lieu(year):
        holiday_date = SG.chinese_new_year()(year)
        if holiday_date is not None and holiday_date.weekday() == Weekday.SATURDAY:
            return first(Weekday.MONDAY).after(SG.chinese_new_year())(year)
        elif holiday_date is not None and holiday_date.weekday() == Weekday.SUNDAY:
            return first(Weekday.TUESDAY).after(SG.chinese_new_year())(year)
        return None

    @staticmethod
    def hari_raya_puasa():
        """Return the date of Hari Raya Puasa for the given year."""
        return dates({
            2011: (Month.AUGUST, 30),
            2012: (Month.AUGUST, 19),
            2013: (Month.AUGUST, 8),
            2014: (Month.JULY, 28),
            2015: (Month.JULY, 17),
            2016: (Month.JULY, 6),
            2017: (Month.JUNE, 25),
            2018: (Month.JUNE, 15),
            2019: (Month.JUNE, 5),
            2020: (Month.MAY, 24),
            2021: (Month.MAY, 13),
            2022: (Month.MAY, 3),
            2023: (Month.APRIL, 22),
            2024: (Month.APRIL, 10),
            2025: (Month.MARCH, 31),
            2026: (Month.MARCH, 21)
        })

    @staticmethod
    def vesak_day():
        """Return the date of Vesak Day for the given year."""
        return dates({
            2011: (Month.MAY, 17),
            2012: (Month.MAY, 5),
            2013: (Month.MAY, 24),
            2014: (Month.MAY, 13),
            2015: (Month.JUNE, 1),
            2016: (Month.MAY, 21),
            2017: (Month.MAY, 10),
            2018: (Month.MAY, 29),
            2019: (Month.MAY, 19),
            2020: (Month.MAY, 7),
            2021: (Month.MAY, 26),
            2022: (Month.MAY, 15),
            2023: (Month.JUNE, 2),
            2024: (Month.MAY, 22),
            2025: (Month.MAY, 12),
            2026: (Month.MAY, 31)
        })

    @staticmethod
    def hari_raya_haji():
        """Return the date of Hari Raya Haji for the given year."""
        return dates({
            2011: (Month.NOVEMBER, 6),
            2012: (Month.OCTOBER, 26),
            2013: (Month.OCTOBER, 15),
            2014: (Month.OCTOBER, 5),
            2015: (Month.SEPTEMBER, 24),
            2016: (Month.SEPTEMBER, 12),
            2017: (Month.SEPTEMBER, 1),
            2018: (Month.AUGUST, 22),
            2019: (Month.AUGUST, 11),
            2020: (Month.JULY, 31),
            2021: (Month.JULY, 20),
            2022: (Month.JULY, 10),
            2023: (Month.JUNE, 29),
            2024: (Month.JUNE, 17),
            2025: (Month.JUNE, 7),
            2026: (Month.MAY, 27)
        })

    @staticmethod
    def deepavali():
        """Return the date of Deepavali for the given year."""
        return dates({
            2011: (Month.OCTOBER, 26),
            2012: (Month.NOVEMBER, 13),
            2013: (Month.NOVEMBER, 2),
            2014: (Month.OCTOBER, 22),
            2015: (Month.NOVEMBER, 10),
            2016: (Month.OCTOBER, 29),
            2017: (Month.OCTOBER, 18),
            2018: (Month.NOVEMBER, 6),
            2019: (Month.OCTOBER, 27),
            2020: (Month.NOVEMBER, 14),
            2021: (Month.NOVEMBER, 4),
            2022: (Month.OCTOBER, 24),
            2023: (Month.NOVEMBER, 12),
            2024: (Month.OCTOBER, 31),
            2025: (Month.OCTOBER, 20),
            2026: (Month.NOVEMBER, 8)
        })
