from holidata.holiday import Region
from holidata.utils import second, day, first, last, date, Weekday, Month, dates


class VIC(Region):
    def __init__(self, country):
        super().__init__("VIC", country)

        """
        New Year's Day
        1 January, and the Monday after 1 January (New Year's Day) when New Year's Day is a Saturday or Sunday
        2009: https://content.legislation.vic.gov.au/sites/default/files/ccbe13db-9862-3b4f-b16c-8f9a552d2dbc_93-119a024.pdf
        2011: https://content.legislation.vic.gov.au/sites/default/files/68a646e7-a547-39aa-adac-b2d5e4bfa756_93-119aa025%20authorised.pdf
        2019: https://content.legislation.vic.gov.au/sites/default/files/ad24ad2c-06f2-3ae3-b0ce-1fcd9b5f61a0_93-119aa026%20authorised.pdf
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
        26 January, or the Monday after Australia Day when Australia Day is a Saturday or Sunday
        2009: https://content.legislation.vic.gov.au/sites/default/files/ccbe13db-9862-3b4f-b16c-8f9a552d2dbc_93-119a024.pdf
        2011: https://content.legislation.vic.gov.au/sites/default/files/68a646e7-a547-39aa-adac-b2d5e4bfa756_93-119aa025%20authorised.pdf
        2019: https://content.legislation.vic.gov.au/sites/default/files/ad24ad2c-06f2-3ae3-b0ce-1fcd9b5f61a0_93-119aa026%20authorised.pdf        
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
        Labour Day
        the second Monday in March
        2009: https://content.legislation.vic.gov.au/sites/default/files/ccbe13db-9862-3b4f-b16c-8f9a552d2dbc_93-119a024.pdf
        2011: https://content.legislation.vic.gov.au/sites/default/files/68a646e7-a547-39aa-adac-b2d5e4bfa756_93-119aa025%20authorised.pdf
        2019: https://content.legislation.vic.gov.au/sites/default/files/ad24ad2c-06f2-3ae3-b0ce-1fcd9b5f61a0_93-119aa026%20authorised.pdf
        """
        self.define_holiday() \
            .with_name("Labour Day") \
            .on(second(Weekday.MONDAY).of(Month.MARCH)) \
            .with_flags("V")

        """
        Good Friday
        2009: https://content.legislation.vic.gov.au/sites/default/files/ccbe13db-9862-3b4f-b16c-8f9a552d2dbc_93-119a024.pdf
        2011: https://content.legislation.vic.gov.au/sites/default/files/68a646e7-a547-39aa-adac-b2d5e4bfa756_93-119aa025%20authorised.pdf
        2019: https://content.legislation.vic.gov.au/sites/default/files/ad24ad2c-06f2-3ae3-b0ce-1fcd9b5f61a0_93-119aa026%20authorised.pdf
        """
        self.define_holiday() \
            .with_name("Good Friday") \
            .on(day(2).before(country.easter())) \
            .with_flags("RV")

        """
        the Saturday before Easter Sunday
        2009: https://content.legislation.vic.gov.au/sites/default/files/ccbe13db-9862-3b4f-b16c-8f9a552d2dbc_93-119a024.pdf
        2011: https://content.legislation.vic.gov.au/sites/default/files/68a646e7-a547-39aa-adac-b2d5e4bfa756_93-119aa025%20authorised.pdf
        2019: https://content.legislation.vic.gov.au/sites/default/files/ad24ad2c-06f2-3ae3-b0ce-1fcd9b5f61a0_93-119aa026%20authorised.pdf
        """
        self.define_holiday() \
            .with_name("Easter Saturday") \
            .on(day(1).before(country.easter())) \
            .with_flags("RV")

        """
        Easter Sunday
        2019: https://content.legislation.vic.gov.au/sites/default/files/ad24ad2c-06f2-3ae3-b0ce-1fcd9b5f61a0_93-119aa026%20authorised.pdf
        """
        self.define_holiday() \
            .with_name("Easter") \
            .since(2019) \
            .on(country.easter()) \
            .with_flags("RV")

        """
        Easter Monday
        2009: https://content.legislation.vic.gov.au/sites/default/files/ccbe13db-9862-3b4f-b16c-8f9a552d2dbc_93-119a024.pdf
        2011: https://content.legislation.vic.gov.au/sites/default/files/68a646e7-a547-39aa-adac-b2d5e4bfa756_93-119aa025%20authorised.pdf
        2019: https://content.legislation.vic.gov.au/sites/default/files/ad24ad2c-06f2-3ae3-b0ce-1fcd9b5f61a0_93-119aa026%20authorised.pdf
        """
        self.define_holiday() \
            .with_name("Easter Monday") \
            .on(day(1).after(country.easter())) \
            .with_flags("RV")

        """
        Anzac Day
        25 April
        2009: https://content.legislation.vic.gov.au/sites/default/files/ccbe13db-9862-3b4f-b16c-8f9a552d2dbc_93-119a024.pdf
        2011: https://content.legislation.vic.gov.au/sites/default/files/68a646e7-a547-39aa-adac-b2d5e4bfa756_93-119aa025%20authorised.pdf
        2019: https://content.legislation.vic.gov.au/sites/default/files/ad24ad2c-06f2-3ae3-b0ce-1fcd9b5f61a0_93-119aa026%20authorised.pdf
        """
        self.define_holiday() \
            .with_name("Anzac Day") \
            .on(date(Month.APRIL, 25)) \
            .with_flags("F")

        """
        Birthday of the Sovereign
        the second Monday in June
        2009: https://content.legislation.vic.gov.au/sites/default/files/ccbe13db-9862-3b4f-b16c-8f9a552d2dbc_93-119a024.pdf
        2011: https://content.legislation.vic.gov.au/sites/default/files/68a646e7-a547-39aa-adac-b2d5e4bfa756_93-119aa025%20authorised.pdf
        2019: https://content.legislation.vic.gov.au/sites/default/files/ad24ad2c-06f2-3ae3-b0ce-1fcd9b5f61a0_93-119aa026%20authorised.pdf
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
        Grand Final Eve
        the Friday before the Australian Football League Grand Final
        Usually, the Friday before last Saturday in September
        2016: https://www.gazette.vic.gov.au/gazette/Gazettes2016/GG2016G036.pdf
        2017: https://www.gazette.vic.gov.au/gazette/Gazettes2017/GG2017G032.pdf
        2018: https://www.gazette.vic.gov.au/gazette/Gazettes2018/GG2018G039.pdf
        2019: https://content.legislation.vic.gov.au/sites/default/files/ad24ad2c-06f2-3ae3-b0ce-1fcd9b5f61a0_93-119aa026%20authorised.pdf
        """
        self.define_holiday() \
            .with_name("Grand Final Eve") \
            .since(2016) \
            .on(dates({
                2016: (Month.SEPTEMBER, 30),
                2020: (Month.OCTOBER, 23),  # Adaption due to the COVID-19 pandemic
            }).or_else_on(first(Weekday.FRIDAY).before(last(Weekday.SATURDAY).of(Month.SEPTEMBER)))) \
            .with_flags("V")

        """
        Melbourne Cup Day
        the first Tuesday in November
        2009: https://content.legislation.vic.gov.au/sites/default/files/ccbe13db-9862-3b4f-b16c-8f9a552d2dbc_93-119a024.pdf
        2011: https://content.legislation.vic.gov.au/sites/default/files/68a646e7-a547-39aa-adac-b2d5e4bfa756_93-119aa025%20authorised.pdf
        2019: https://content.legislation.vic.gov.au/sites/default/files/ad24ad2c-06f2-3ae3-b0ce-1fcd9b5f61a0_93-119aa026%20authorised.pdf
        """
        self.define_holiday() \
            .with_name("Melbourne Cup Day") \
            .on(first(Weekday.TUESDAY).of(Month.NOVEMBER)) \
            .with_flags("V")

        """
        25 December (Christmas Day) or the Monday after Christmas Day when Christmas Day is a Saturday or the Tuesday after Christmas Day when Christmas Day is a Sunday
        2009: https://content.legislation.vic.gov.au/sites/default/files/ccbe13db-9862-3b4f-b16c-8f9a552d2dbc_93-119a024.pdf
        2011: https://content.legislation.vic.gov.au/sites/default/files/68a646e7-a547-39aa-adac-b2d5e4bfa756_93-119aa025%20authorised.pdf
        2019: https://content.legislation.vic.gov.au/sites/default/files/ad24ad2c-06f2-3ae3-b0ce-1fcd9b5f61a0_93-119aa026%20authorised.pdf
        """
        self.define_holiday() \
            .with_name("Christmas Day") \
            .on(date(Month.DECEMBER, 25)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Christmas Day (observed)") \
            .on(first(Weekday.MONDAY).after(date(Month.DECEMBER, 25))) \
            .with_flags("RF") \
            .on_condition(date(Month.DECEMBER, 25).is_a(Weekday.SATURDAY))

        self.define_holiday() \
            .with_name("Christmas Day (observed)") \
            .on(first(Weekday.TUESDAY).after(date(Month.DECEMBER, 25))) \
            .with_flags("RF") \
            .on_condition(date(Month.DECEMBER, 25).is_a(Weekday.SUNDAY))

        """
        26 December (Boxing Day)
        the Monday after 26 December (Boxing Day) when Boxing Day is a Saturday or the Tuesday after Boxing Day when Boxing Day is a Sunday
        2009: https://content.legislation.vic.gov.au/sites/default/files/ccbe13db-9862-3b4f-b16c-8f9a552d2dbc_93-119a024.pdf
        2011: https://content.legislation.vic.gov.au/sites/default/files/68a646e7-a547-39aa-adac-b2d5e4bfa756_93-119aa025%20authorised.pdf
        2019: https://content.legislation.vic.gov.au/sites/default/files/ad24ad2c-06f2-3ae3-b0ce-1fcd9b5f61a0_93-119aa026%20authorised.pdf
        """
        self.define_holiday() \
            .with_name("Boxing Day") \
            .on(date(Month.DECEMBER, 26)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Boxing Day (observed)") \
            .on(first(Weekday.MONDAY).after(date(Month.DECEMBER, 26))) \
            .with_flags("RF") \
            .on_condition(date(Month.DECEMBER, 26).is_a(Weekday.SATURDAY))

        self.define_holiday() \
            .with_name("Boxing Day (observed)") \
            .on(first(Weekday.TUESDAY).after(date(Month.DECEMBER, 26))) \
            .with_flags("RF") \
            .on_condition(date(Month.DECEMBER, 26).is_a(Weekday.SUNDAY))
