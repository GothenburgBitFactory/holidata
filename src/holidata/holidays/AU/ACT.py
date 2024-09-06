from holidata.holiday import Region
from holidata.utils import first, second, day, date


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
            .on(date(month=1, day=1)) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("New Year's Day (observed)") \
            .on(first("monday").after(date(month=1, day=1))) \
            .with_flags("V") \
            .on_condition(date(month=1, day=1).is_one_of(["saturday", "sunday"]))

        """
        Australia Day
        26 January, or, if that day falls on a Saturday or Sunday, the following Monday
        https://www.legislation.act.gov.au/View/a/1958-19/current/html/1958-19.html
        """
        self.define_holiday() \
            .with_name("Australia Day") \
            .on(date(month=1, day=26)) \
            .on_condition(date(month=1, day=26).is_none_of(["saturday", "sunday"])) \
            .with_flags("V")

        self.define_holiday() \
            .with_name("Australia Day") \
            .on(first("monday").after(date(month=1, day=26))) \
            .on_condition(date(month=1, day=26).is_one_of(["saturday", "sunday"])) \
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
            .on(date(month=4, day=25)) \
            .on_condition(date(month=4, day=25).is_not_a("sunday")) \
            .with_flags("V")

        self.define_holiday() \
            .with_name("Anzac Day") \
            .on(first("monday").after(date(month=4, day=25))) \
            .on_condition(date(month=4, day=25).is_a("sunday")) \
            .with_flags("V")

        """
        Reconciliation Day
        27 May, or, if that day is not a Monday, the following Monday
        https://www.legislation.act.gov.au/View/a/1958-19/current/html/1958-19.html
        """
        self.define_holiday() \
            .with_name("Reconciliation Day") \
            .on(first("monday").after(date(month=5, day=26), including=True)) \
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
            .on(date(month=12, day=25)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Christmas Day (observed)") \
            .on(first("monday").after(date(month=12, day=25))) \
            .with_flags("RV") \
            .on_condition(date(month=12, day=25).is_a("saturday"))

        self.define_holiday() \
            .with_name("Christmas Day (observed)") \
            .on(first("tuesday").after(date(month=12, day=25))) \
            .with_flags("RV") \
            .on_condition(date(month=12, day=25).is_a("sunday"))

        """
        Boxing Day
        26 December and, if that day falls on a Saturday, the following Monday, or, if that day falls on a Sunday, the following Tuesday
        https://www.legislation.act.gov.au/View/a/1958-19/current/html/1958-19.html
        """
        self.define_holiday() \
            .with_name("Boxing Day") \
            .on(date(month=12, day=26)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Boxing Day (observed)") \
            .on(first("monday").after(date(month=12, day=26))) \
            .with_flags("RV") \
            .on_condition(date(month=12, day=26).is_a("saturday"))

        self.define_holiday() \
            .with_name("Boxing Day (observed)") \
            .on(first("tuesday").after(date(month=12, day=26))) \
            .with_flags("RV") \
            .on_condition(date(month=12, day=26).is_a("sunday"))
