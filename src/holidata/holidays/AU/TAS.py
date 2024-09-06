from holidata.holiday import Region
from holidata.utils import second, day, first, date


class TAS(Region):
    def __init__(self, country):
        super().__init__("TAS", country)

        """
        New Year's Day (1 January), unless that day falls on a Saturday or Sunday, in which case the Monday following New Year's Day
        https://www.legislation.tas.gov.au/view/html/inforce/current/act-2000-096
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
        Australia Day (26 January), unless that day falls on a Saturday or Sunday, in which case the following Monday
        https://www.legislation.tas.gov.au/view/html/inforce/current/act-2000-096
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

        self.define_holiday() \
            .with_name("Royal Hobart Regatta") \
            .in_regions(["TAS"]) \
            .on(second("monday").of("february")) \
            .with_flags("V")

        """
        the second Monday in March, known as Eight Hours Day or Labour Day
        https://www.legislation.tas.gov.au/view/html/inforce/current/act-2000-096
        """
        self.define_holiday() \
            .with_name("Labour Day") \
            .on(second("monday").of("march")) \
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
            .on(date(month=4, day=25)) \
            .with_flags("F")

        """
        Birthday of the Sovereign
        the second Monday in June
        https://www.legislation.tas.gov.au/view/html/inforce/current/act-2000-096
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
        Christmas Day (25 December); if Christmas Day falls on a Saturday, the Monday following Christmas Day; if Christmas Day falls on a Sunday, the Tuesday following Christmas Day
        https://www.legislation.tas.gov.au/view/html/inforce/current/act-2000-096
        """
        self.define_holiday() \
            .with_name("Christmas Day") \
            .on(date(month=12, day=25)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Christmas Day (observed)") \
            .on(first("monday").after(date(month=12, day=25), including=False)) \
            .with_flags("RV") \
            .on_condition(date(month=12, day=25).is_one_of(["saturday", "sunday"]))

        """
        Boxing Day (26 December), unless that day falls on a Saturday or Sunday, in which case – the Monday following Boxing Day, if that day falls on a Saturday; or the Tuesday following Boxing Day, if that day falls on a Sunday.
        https://www.legislation.tas.gov.au/view/html/inforce/current/act-2000-096
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
            .on_condition(date(month=12, day=26).is_one_of(["sunday", "monday"]))
