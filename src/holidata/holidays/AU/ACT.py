from holidata.holiday import Region
from holidata.utils import Month, Weekday, date, day, first, second


class ACT(Region):
    def __init__(self, country):
        super().__init__("ACT", country)

        """
        New Year's Day
        1 January, and, if that day falls on a Saturday or Sunday, the following Monday
        https://www.legislation.act.gov.au/View/a/1958-19/current/html/1958-19.html
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
        26 January, or, if that day falls on a Saturday or Sunday, the following Monday
        https://www.legislation.act.gov.au/View/a/1958-19/current/html/1958-19.html
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
        Canberra Day
        the 2nd Monday in March;
        https://www.legislation.act.gov.au/View/a/1958-19/current/html/1958-19.html
        """
        self.define_holiday() \
            .with_name("Canberra Day") \
            .on(second(Weekday.MONDAY).of(Month.MARCH)) \
            .with_flags("V")

        """
        Good Friday
        https://www.legislation.act.gov.au/View/a/1958-19/current/html/1958-19.html
        """
        self.define_holiday() \
            .with_name("Good Friday") \
            .on(day(2).before(country.easter())) \
            .with_flags("RV")

        """
        the Saturday following Good Friday
        https://www.legislation.act.gov.au/View/a/1958-19/current/html/1958-19.html
        """
        self.define_holiday() \
            .with_name("Easter Saturday") \
            .on(day(1).before(country.easter())) \
            .with_flags("RV")

        """
        Easter Sunday
        https://www.legislation.act.gov.au/View/a/1958-19/current/html/1958-19.html
        """
        self.define_holiday() \
            .with_name("Easter") \
            .on(country.easter()) \
            .with_flags("RV")

        """
        the Monday following Good Friday
        https://www.legislation.act.gov.au/View/a/1958-19/current/html/1958-19.html
        """
        self.define_holiday() \
            .with_name("Easter Monday") \
            .on(day(1).after(country.easter())) \
            .with_flags("RV")

        """
        Anzac Day
        25 April, or, if that day falls on a Sunday, the following Monday
        https://www.legislation.act.gov.au/View/a/1958-19/current/html/1958-19.html
        """
        self.define_holiday() \
            .with_name("Anzac Day") \
            .on(date(Month.APRIL, 25)) \
            .on_condition(date(Month.APRIL, 25).is_not_a(Weekday.SUNDAY)) \
            .with_flags("V")

        self.define_holiday() \
            .with_name("Anzac Day") \
            .on(first(Weekday.MONDAY).after(date(Month.APRIL, 25))) \
            .on_condition(date(Month.APRIL, 25).is_a(Weekday.SUNDAY)) \
            .with_flags("V")

        """
        Reconciliation Day
        27 May, or, if that day is not a Monday, the following Monday
        https://www.legislation.act.gov.au/View/a/1958-19/current/html/1958-19.html
        """
        self.define_holiday() \
            .with_name("Reconciliation Day") \
            .on(first(Weekday.MONDAY).after(date(Month.MAY, 26), including=True)) \
            .with_flags("V")

        """
        Birthday of the Sovereign
        the 2nd Monday in June
        https://www.legislation.act.gov.au/View/a/1958-19/current/html/1958-19.html
        """
        self.define_holiday() \
            .with_name("Queen's Birthday") \
            .until(2022) \
            .on(second(Weekday.MONDAY).of(Month.JUNE)) \
            .with_flags("V")

        self.define_holiday() \
            .with_name("King's Birthday") \
            .since(2023) \
            .on(second(Weekday.MONDAY).of(Month.JUNE)) \
            .with_flags("V")

        """
        Bank Holiday
        the 1st Monday in August
        https://www.legislation.act.gov.au/View/a/1958-19/current/html/1958-19.html
        """
        self.define_holiday() \
            .with_name("Bank Holiday") \
            .on(first(Weekday.MONDAY).of(Month.AUGUST)) \
            .with_flags("V")

        """
        Labour Day
        the 1st Monday in October
        https://www.legislation.act.gov.au/View/a/1958-19/current/html/1958-19.html
        """
        self.define_holiday() \
            .with_name("Labour Day") \
            .on(first(Weekday.MONDAY).of(Month.OCTOBER)) \
            .with_flags("V")

        """
        Christmas Day
        25 December, and, if that day falls on a Saturday, the following Monday, or if that day falls on a Sunday, the following Tuesday
        https://www.legislation.act.gov.au/View/a/1958-19/current/html/1958-19.html
        """
        self.define_holiday() \
            .with_name("Christmas Day") \
            .on(date(Month.DECEMBER, 25)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Christmas Day (observed)") \
            .on(first(Weekday.MONDAY).after(date(Month.DECEMBER, 25))) \
            .with_flags("RV") \
            .on_condition(date(Month.DECEMBER, 25).is_a(Weekday.SATURDAY))

        self.define_holiday() \
            .with_name("Christmas Day (observed)") \
            .on(first(Weekday.TUESDAY).after(date(Month.DECEMBER, 25))) \
            .with_flags("RV") \
            .on_condition(date(Month.DECEMBER, 25).is_a(Weekday.SUNDAY))

        """
        Boxing Day
        26 December and, if that day falls on a Saturday, the following Monday, or, if that day falls on a Sunday, the following Tuesday
        https://www.legislation.act.gov.au/View/a/1958-19/current/html/1958-19.html
        """
        self.define_holiday() \
            .with_name("Boxing Day") \
            .on(date(Month.DECEMBER, 26)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Boxing Day (observed)") \
            .on(first(Weekday.MONDAY).after(date(Month.DECEMBER, 26))) \
            .with_flags("RV") \
            .on_condition(date(Month.DECEMBER, 26).is_a(Weekday.SATURDAY))

        self.define_holiday() \
            .with_name("Boxing Day (observed)") \
            .on(first(Weekday.TUESDAY).after(date(Month.DECEMBER, 26))) \
            .with_flags("RV") \
            .on_condition(date(Month.DECEMBER, 26).is_a(Weekday.SUNDAY))
