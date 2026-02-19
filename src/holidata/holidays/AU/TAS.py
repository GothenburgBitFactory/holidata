from holidata.holiday import Region
from holidata.utils import second, day, first, date, Weekday, Month


class TAS(Region):
    def __init__(self, country):
        super().__init__("TAS", country)

        """
        New Year's Day (1 January), unless that day falls on a Saturday or Sunday, in which case the Monday following New Year's Day
        https://www.legislation.tas.gov.au/view/html/inforce/current/act-2000-096
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
        Australia Day (26 January), unless that day falls on a Saturday or Sunday, in which case the following Monday
        https://www.legislation.tas.gov.au/view/html/inforce/current/act-2000-096
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

        self.define_holiday() \
            .with_name("Royal Hobart Regatta") \
            .on(second(Weekday.MONDAY).of(Month.FEBRUARY)) \
            .with_flags("V")

        """
        the second Monday in March, known as Eight Hours Day or Labour Day
        https://www.legislation.tas.gov.au/view/html/inforce/current/act-2000-096
        """
        self.define_holiday() \
            .with_name("Labour Day") \
            .on(second(Weekday.MONDAY).of(Month.MARCH)) \
            .with_flags("V")

        """
        Good Friday
        https://www.legislation.tas.gov.au/view/html/inforce/current/act-2000-096
        """
        self.define_holiday() \
            .with_name("Good Friday") \
            .on(day(2).before(country.easter())) \
            .with_flags("RV")

        """
        Easter Monday
        https://www.legislation.tas.gov.au/view/html/inforce/current/act-2000-096
        """
        self.define_holiday() \
            .with_name("Easter Monday") \
            .on(day(1).after(country.easter())) \
            .with_flags("RV")

        """
        Anzac Day
        25 April
        https://www.legislation.tas.gov.au/view/html/inforce/current/act-2000-096
        """
        self.define_holiday() \
            .with_name("Anzac Day") \
            .on(date(Month.APRIL, 25)) \
            .with_flags("F")

        """
        Birthday of the Sovereign
        the second Monday in June
        https://www.legislation.tas.gov.au/view/html/inforce/current/act-2000-096
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
        Christmas Day (25 December); if Christmas Day falls on a Saturday, the Monday following Christmas Day; if Christmas Day falls on a Sunday, the Tuesday following Christmas Day
        https://www.legislation.tas.gov.au/view/html/inforce/current/act-2000-096
        """
        self.define_holiday() \
            .with_name("Christmas Day") \
            .on(date(Month.DECEMBER, 25)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Christmas Day (observed)") \
            .on(first(Weekday.MONDAY).after(date(Month.DECEMBER, 25), including=False)) \
            .with_flags("RV") \
            .on_condition(date(Month.DECEMBER, 25).is_one_of([Weekday.SATURDAY, Weekday.SUNDAY]))

        """
        Boxing Day (26 December), unless that day falls on a Saturday or Sunday, in which case – the Monday following Boxing Day, if that day falls on a Saturday; or the Tuesday following Boxing Day, if that day falls on a Sunday.
        https://www.legislation.tas.gov.au/view/html/inforce/current/act-2000-096
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
            .on_condition(date(Month.DECEMBER, 26).is_one_of([Weekday.SUNDAY, Weekday.MONDAY]))
