from holidata.holiday import Region
from holidata.utils import SmartDayArrow, first, second, day


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
            .on(month=1, day=1) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("New Year's Day (observed)") \
            .on(first("monday").after(month=1, day=1)) \
            .with_flags("V") \
            .on_condition(ACT.date_is_on_weekend(month=1, day=1))

        """
        Australia Day
        26 January, or, if that day falls on a Saturday or Sunday, the following Monday
        https://www.legislation.act.gov.au/View/a/1958-19/current/html/1958-19.html
        """
        self.define_holiday() \
            .with_name("Australia Day") \
            .on(self.mon_to_fri_on_or_following(month=1, day=26)) \
            .with_flags("V")

        """
        Canberra Day
        the 2nd Monday in March;
        https://www.legislation.act.gov.au/View/a/1958-19/current/html/1958-19.html
        """
        self.define_holiday() \
            .with_name("Canberra Day") \
            .on(second("monday").of("march")) \
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
            .on(self.mon_to_sat_on_or_following(month=4, day=25)) \
            .with_flags("V")

        """
        Reconciliation Day
        27 May, or, if that day is not a Monday, the following Monday
        https://www.legislation.act.gov.au/View/a/1958-19/current/html/1958-19.html
        """
        self.define_holiday() \
            .with_name("Reconciliation Day") \
            .on(first("monday").after(month=5, day=26, including=True)) \
            .with_flags("V")

        """
        Birthday of the Sovereign
        the 2nd Monday in June
        https://www.legislation.act.gov.au/View/a/1958-19/current/html/1958-19.html
        """
        self.define_holiday() \
            .with_name("Queen's Birthday") \
            .until(2022) \
            .on(second("monday").of("june")) \
            .with_flags("V")

        self.define_holiday() \
            .with_name("King's Birthday") \
            .since(2023) \
            .on(second("monday").of("june")) \
            .with_flags("V")

        """
        Bank Holiday
        the 1st Monday in August
        https://www.legislation.act.gov.au/View/a/1958-19/current/html/1958-19.html
        """
        self.define_holiday() \
            .with_name("Bank Holiday") \
            .on(first("monday").of("august")) \
            .with_flags("V")

        """
        Labour Day
        the 1st Monday in October
        https://www.legislation.act.gov.au/View/a/1958-19/current/html/1958-19.html
        """
        self.define_holiday() \
            .with_name("Labour Day") \
            .on(first("monday").of("october")) \
            .with_flags("V")

        """
        Christmas Day
        25 December, and, if that day falls on a Saturday, the following Monday, or if that day falls on a Sunday, the following Tuesday
        https://www.legislation.act.gov.au/View/a/1958-19/current/html/1958-19.html
        """
        self.define_holiday() \
            .with_name("Christmas Day") \
            .on(month=12, day=25) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Christmas Day (observed)") \
            .on(first("monday").after(month=12, day=25)) \
            .with_flags("RV") \
            .on_condition(ACT.date_is_saturday(month=12, day=25))

        self.define_holiday() \
            .with_name("Christmas Day (observed)") \
            .on(first("tuesday").after(month=12, day=25)) \
            .with_flags("RV") \
            .on_condition(ACT.date_is_sunday(month=12, day=25))

        """
        Boxing Day
        26 December and, if that day falls on a Saturday, the following Monday, or, if that day falls on a Sunday, the following Tuesday
        https://www.legislation.act.gov.au/View/a/1958-19/current/html/1958-19.html
        """
        self.define_holiday() \
            .with_name("Boxing Day") \
            .on(month=12, day=26) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Boxing Day (observed)") \
            .on(first("monday").after(month=12, day=26)) \
            .with_flags("RV") \
            .on_condition(ACT.date_is_saturday(month=12, day=26))

        self.define_holiday() \
            .with_name("Boxing Day (observed)") \
            .on(first("tuesday").after(month=12, day=26)) \
            .with_flags("RV") \
            .on_condition(ACT.date_is_sunday(month=12, day=26))

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
    def mon_to_sat_on_or_following(month, day):
        def wrapper(year):
            date = SmartDayArrow(year, month, day)

            if date.weekday() == "sunday":
                date.shift_to_weekday("monday", including=True)

            return date

        return wrapper
