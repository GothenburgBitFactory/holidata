from holidata.holiday import Region
from holidata.utils import SmartDayArrow, day, second, first


class SA(Region):
    def __init__(self, country):
        super().__init__("SA", country)

        """
        1 January.
        (a) when a day mentioned in Part 2 of Schedule 2 falls on a Saturday, the
        following Monday will be a public holiday instead of that day and that day
        and the following Monday will be bank holidays; and
        (b) when a day mentioned in Part 2 of Schedule 2 falls on a Sunday, that day and
        the following Monday will be public holidays and bank holidays.
        https://www.legislation.sa.gov.au/__legislation/lz/c/a/holidays%20act%201910/current/1910.1010.auth.pdf
        """
        self.define_holiday() \
            .with_name("New Year's Day") \
            .on(month=1, day=1) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("New Year's Day (observed)") \
            .on(first("monday").after(month=1, day=1)) \
            .with_flags("V") \
            .on_condition(self.date_is_on_weekend(month=1, day=1))

        """
        Australia Day
        26 January.
        (a) when a day mentioned in Part 2 of Schedule 2 falls on a Saturday, the
        following Monday will be a public holiday instead of that day and that day
        and the following Monday will be bank holidays; and
        (b) when a day mentioned in Part 2 of Schedule 2 falls on a Sunday, that day and
        the following Monday will be public holidays and bank holidays.
        https://www.legislation.sa.gov.au/__legislation/lz/c/a/holidays%20act%201910/current/1910.1010.auth.pdf
        """
        self.define_holiday() \
            .with_name("Australia Day") \
            .on(self.mon_to_fri_on_or_following(month=1, day=26)) \
            .with_flags("V")

        """
        Good Friday.
        https://www.legislation.sa.gov.au/__legislation/lz/c/a/holidays%20act%201910/current/1910.1010.auth.pdf
        """
        self.define_holiday() \
            .with_name("Good Friday") \
            .on(day(2).before(country.easter())) \
            .with_flags("RV")

        """
        The day after Good Friday.
        https://www.legislation.sa.gov.au/__legislation/lz/c/a/holidays%20act%201910/current/1910.1010.auth.pdf
        """
        self.define_holiday() \
            .with_name("Easter Saturday") \
            .on(day(1).before(country.easter())) \
            .with_flags("RV")

        """
        Easter Sunday
        https://www.legislation.sa.gov.au/__legislation/lz/c/a/holidays%20act%201910/current/1910.1010.auth.pdf
        """
        self.define_holiday() \
            .with_name("Easter") \
            .on(country.easter()) \
            .with_flags("RV")

        """
        Easter Monday.
        https://www.legislation.sa.gov.au/__legislation/lz/c/a/holidays%20act%201910/current/1910.1010.auth.pdf
        """
        self.define_holiday() \
            .with_name("Easter Monday") \
            .on(day(1).after(country.easter())) \
            .with_flags("RV")

        """
        Anzac Day
        In addition to the days mentioned in Schedule 2, 25 April will be a public holiday and
        bank holiday but when that day falls on a Sunday, that day and the following Monday
        will be public holidays and bank holidays.
        https://www.legislation.sa.gov.au/__legislation/lz/c/a/holidays%20act%201910/current/1910.1010.auth.pdf
        """
        self.define_holiday() \
            .with_name("Anzac Day") \
            .on(month=4, day=25) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Anzac Day (observed)") \
            .on(first("monday").after(month=4, day=25)) \
            .with_flags("V") \
            .on_condition(self.date_is_sunday(month=4, day=25))

        """
        Adelaide Cup Day
        Proclaimed as a replacement for the third Monday in May.
        https://www.legislation.sa.gov.au/__legislation/lz/c/a/holidays%20act%201910/current/1910.1010.auth.pdf
        """
        self.define_holiday() \
            .with_name("Adelaide Cup Day") \
            .on(self.date_as_declared_by_the_holidays_adelaide_cup_proclamation) \
            .with_flags("V")

        """
        Birthday of the Sovereign
        The second Monday in June.
        https://www.legislation.sa.gov.au/__legislation/lz/c/a/holidays%20act%201910/current/1910.1010.auth.pdf
        """
        self.define_holiday() \
            .with_name("King's Birthday") \
            .since(2023) \
            .on(second("monday").of("june")) \
            .with_flags("V")

        """
        National Day of Mourning for Queen Elizabeth II
        2022-09-22, as proclaimed by the Holidays (National Day of Mourning for Queen Elizabeth II) Proclamation 2022 (Gazette 16.9.2022 p 6013)
        https://www.legislation.sa.gov.au/__legislation/lz/v/p/2022/holidays%20(national%20day%20of%20mourning%20for%20queen%20elizabeth%20ii)%20proclamation%202022_16.9.2022%20p%206013/16.9.2022%20p%206013.un.pdf
        """
        self.define_holiday() \
            .with_name("National Day of Mourning for Queen Elizabeth II") \
            .in_years([2022]) \
            .on(month=9, day=22) \
            .with_flags("F")

        """
        Labour Day
        The first Monday in October.
        https://www.legislation.sa.gov.au/__legislation/lz/c/a/holidays%20act%201910/current/1910.1010.auth.pdf
        """
        self.define_holiday() \
            .with_name("Labour Day") \
            .on(first("monday").of("october")) \
            .with_flags("V")

        """
        Christmas Day.
        (a) when a day mentioned in Part 2 of Schedule 2 falls on a Saturday, the
        following Monday will be a public holiday instead of that day and that day
        and the following Monday will be bank holidays; and
        (b) when a day mentioned in Part 2 of Schedule 2 falls on a Sunday, that day and
        the following Monday will be public holidays and bank holidays. 
        https://www.legislation.sa.gov.au/__legislation/lz/c/a/holidays%20act%201910/current/1910.1010.auth.pdf
        """
        self.define_holiday() \
            .with_name("Christmas Day") \
            .on(month=12, day=25) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Christmas Day (observed)") \
            .on(first("monday").after(month=12, day=25)) \
            .with_flags("RV") \
            .on_condition(self.date_is_on_weekend(month=12, day=25))

    @staticmethod
    def date_is_on_weekend(month, day):
        def wrapper(year):
            return SmartDayArrow(year, month, day).weekday() in ["saturday", "sunday"]

        return wrapper

    @staticmethod
    def date_is_saturday(month, day):
        def wrapper(year):
            return SmartDayArrow(year, month, day).weekday() == "saturday"

        return wrapper

    @staticmethod
    def date_is_sunday(month, day):
        def wrapper(year):
            return SmartDayArrow(year, month, day).weekday() == "sunday"

        return wrapper

    @staticmethod
    def mon_to_fri_on_or_following(month, day):
        def wrapper(year):
            date = SmartDayArrow(year, month, day)

            if date.weekday() in ["saturday", "sunday"]:
                date.shift_to_weekday("monday", including=True)

            return date

        return wrapper

    @staticmethod
    def date_as_declared_by_the_holidays_adelaide_cup_proclamation(year):
        substitution_date = {
            2011: {"month": 3, "day": 14},  # Holidays (Adelaide Cup) Proclamation 2010
            2012: {"month": 3, "day": 12},  # Holidays (Adelaide Cup) Proclamation 2011
            2013: {"month": 3, "day": 11},  # Holidays (Adelaide Cup) Proclamation 2012
            2014: {"month": 3, "day": 10},
            2015: {"month": 3, "day":  9},
            2016: {"month": 3, "day": 14},
            2017: {"month": 3, "day": 13},
            2018: {"month": 3, "day": 12},
            2019: {"month": 3, "day": 11},
            2020: {"month": 3, "day":  9},
            2021: {"month": 3, "day":  8},
            2022: {"month": 3, "day": 14},
            2023: {"month": 3, "day": 13},
            2024: {"month": 3, "day": 11},  # subject to Proclamation
            2025: {"month": 3, "day": 10},  # subject to Proclamation
        }

        return SmartDayArrow(year, **substitution_date.get(year)) if substitution_date.get(year) is not None else None
