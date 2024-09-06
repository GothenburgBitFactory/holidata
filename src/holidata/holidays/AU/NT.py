from holidata.holiday import Region
from holidata.utils import day, first, second, date


class NT(Region):
    def __init__(self, country):
        super().__init__("NT", country)

        """
        New Year's Day
        1 January, and, if that day falls on a Saturday or Sunday, the following Monday
        https://legislation.nt.gov.au/Legislation/PUBLIC-HOLIDAYS-ACT-1981
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
        26 January, or, if that day falls on a Saturday or a Sunday, the following Monday
        https://legislation.nt.gov.au/Legislation/PUBLIC-HOLIDAYS-ACT-1981
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
        Good Friday
        https://legislation.nt.gov.au/Legislation/PUBLIC-HOLIDAYS-ACT-1981
        """
        self.define_holiday() \
            .with_name("Good Friday") \
            .on(day(2).before(country.easter())) \
            .with_flags("RV")

        """
        The Saturday following Good Friday
        https://legislation.nt.gov.au/Legislation/PUBLIC-HOLIDAYS-ACT-1981
        """
        self.define_holiday() \
            .with_name("Easter Saturday") \
            .on(day(1).before(country.easter())) \
            .with_flags("RV")

        """
        The Sunday following Good Friday
        https://legislation.nt.gov.au/Legislation/PUBLIC-HOLIDAYS-ACT-1981
        """
        self.define_holiday() \
            .with_name("Easter") \
            .on(country.easter()) \
            .with_flags("RV")

        """
        The Monday following Good Friday
        https://legislation.nt.gov.au/Legislation/PUBLIC-HOLIDAYS-ACT-1981
        """
        self.define_holiday() \
            .with_name("Easter Monday") \
            .on(day(1).after(country.easter())) \
            .with_flags("RV")

        """
        Anzac Day
        25 April, or, if that day falls on a Sunday, the following Monday
        https://legislation.nt.gov.au/Legislation/PUBLIC-HOLIDAYS-ACT-1981
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
        May Day
        The first Monday in May
        https://legislation.nt.gov.au/Legislation/PUBLIC-HOLIDAYS-ACT-1981
        """
        self.define_holiday() \
            .with_name("May Day") \
            .on(first("monday").of("may")) \
            .with_flags("V")

        """
        Birthday of the Sovereign
        The second Monday in June
        https://legislation.nt.gov.au/Legislation/PUBLIC-HOLIDAYS-ACT-1981
        """
        self.define_holiday() \
            .with_name("King's Birthday") \
            .since(2023) \
            .on(second("monday").of("june")) \
            .with_flags("V")

        """
        Picnic Day
        The first Monday in August
        https://legislation.nt.gov.au/Legislation/PUBLIC-HOLIDAYS-ACT-1981
        """
        self.define_holiday() \
            .with_name("Picnic Day") \
            .on(first("monday").of("august")) \
            .with_flags("V")

        """
        24 December (Christmas Eve) from 7.00 pm to midnight
        https://legislation.nt.gov.au/Legislation/PUBLIC-HOLIDAYS-ACT-1981
        """
        """
        Christmas Day
        25 December, and, if that day falls on a Saturday or Sunday, the following Monday
        https://legislation.nt.gov.au/Legislation/PUBLIC-HOLIDAYS-ACT-1981
        """
        self.define_holiday() \
            .with_name("Christmas Day") \
            .on(date(month=12, day=25)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Christmas Day (observed)") \
            .on(first("monday").after(date(month=12, day=25))) \
            .with_flags("RV") \
            .on_condition(date(month=12, day=25).is_one_of(["saturday", "sunday"]))

        """
        Boxing Day
        26 December and, if that day falls on a Saturday, the following Monday, or, if that day falls on a Sunday or Monday, the following Tuesday
        https://legislation.nt.gov.au/Legislation/PUBLIC-HOLIDAYS-ACT-1981
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

        """
        New Year's Eve
        31 December from 7.00 pm to midnight
        https://legislation.nt.gov.au/Legislation/PUBLIC-HOLIDAYS-ACT-1981
        """
