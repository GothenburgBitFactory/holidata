from holidata.holiday import Region
from holidata.utils import day, second, first, date, Weekday, Month, dates


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
            .on(date(Month.JANUARY, 1)) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("New Year's Day (observed)") \
            .on(first(Weekday.MONDAY).after(date(Month.JANUARY, 1))) \
            .with_flags("V") \
            .on_condition(date(Month.JANUARY, 1).is_one_of([Weekday.SATURDAY, Weekday.SUNDAY]))

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
            .on(date(Month.JANUARY, 26)) \
            .on_condition(date(Month.JANUARY, 26).is_none_of([Weekday.SATURDAY, Weekday.SUNDAY])) \
            .with_flags("V")

        self.define_holiday() \
            .with_name("Australia Day") \
            .on(first(Weekday.MONDAY).after(date(Month.JANUARY, 26))) \
            .on_condition(date(Month.JANUARY, 26).is_one_of([Weekday.SATURDAY, Weekday.SUNDAY])) \
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
            .on(date(Month.APRIL, 25)) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Anzac Day (observed)") \
            .on(first(Weekday.MONDAY).after(date(Month.APRIL, 25))) \
            .with_flags("V") \
            .on_condition(date(Month.APRIL, 25).is_a(Weekday.SUNDAY))

        """
        Adelaide Cup Day
        Proclaimed as a replacement for the third Monday in May.
        https://www.legislation.sa.gov.au/__legislation/lz/c/a/holidays%20act%201910/current/1910.1010.auth.pdf
        """
        self.define_holiday() \
            .with_name("Adelaide Cup Day") \
            .on(dates({
                2011: (Month.MARCH, 14),  # Holidays (Adelaide Cup) Proclamation 2010
                2012: (Month.MARCH, 12),  # Holidays (Adelaide Cup) Proclamation 2011
                2013: (Month.MARCH, 11),  # Holidays (Adelaide Cup) Proclamation 2012
                2014: (Month.MARCH, 10),
                2015: (Month.MARCH, 9),
                2016: (Month.MARCH, 14),
                2017: (Month.MARCH, 13),
                2018: (Month.MARCH, 12),
                2019: (Month.MARCH, 11),
                2020: (Month.MARCH, 9),
                2021: (Month.MARCH, 8),
                2022: (Month.MARCH, 14),
                2023: (Month.MARCH, 13),
                2024: (Month.MARCH, 11),  # subject to Proclamation
                2025: (Month.MARCH, 10),  # subject to Proclamation
            })) \
            .with_flags("V")

        """
        Birthday of the Sovereign
        The second Monday in June.
        https://www.legislation.sa.gov.au/__legislation/lz/c/a/holidays%20act%201910/current/1910.1010.auth.pdf
        """
        self.define_holiday() \
            .with_name("King's Birthday") \
            .since(2023) \
            .on(second(Weekday.MONDAY).of(Month.JUNE)) \
            .with_flags("V")

        """
        National Day of Mourning for Queen Elizabeth II
        2022-09-22, as proclaimed by the Holidays (National Day of Mourning for Queen Elizabeth II) Proclamation 2022 (Gazette 16.9.2022 p 6013)
        https://www.legislation.sa.gov.au/__legislation/lz/v/p/2022/holidays%20(national%20day%20of%20mourning%20for%20queen%20elizabeth%20ii)%20proclamation%202022_16.9.2022%20p%206013/16.9.2022%20p%206013.un.pdf
        """
        self.define_holiday() \
            .with_name("National Day of Mourning for Queen Elizabeth II") \
            .in_years([2022]) \
            .on(date(Month.SEPTEMBER, 22)) \
            .with_flags("F")

        """
        Labour Day
        The first Monday in October.
        https://www.legislation.sa.gov.au/__legislation/lz/c/a/holidays%20act%201910/current/1910.1010.auth.pdf
        """
        self.define_holiday() \
            .with_name("Labour Day") \
            .on(first(Weekday.MONDAY).of(Month.OCTOBER)) \
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
            .on(date(Month.DECEMBER, 25)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Christmas Day (observed)") \
            .on(first(Weekday.MONDAY).after(date(Month.DECEMBER, 25))) \
            .with_flags("RV") \
            .on_condition(date(Month.DECEMBER, 25).is_one_of([Weekday.SATURDAY, Weekday.SUNDAY]))
