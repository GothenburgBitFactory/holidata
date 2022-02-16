from holidata.holiday import Region
from holidata.utils import SmartDayArrow, second, day, first, last


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
            .on(month=1, day=1) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("New Year's Day (observed)") \
            .on(first("monday").after(month=1, day=1)) \
            .with_flags("V") \
            .on_condition(self.date_is_on_weekend(month=1, day=1))

        """
        Australia Day
        26 January, or the Monday after Australia Day when Australia Day is a Saturday or Sunday
        2009: https://content.legislation.vic.gov.au/sites/default/files/ccbe13db-9862-3b4f-b16c-8f9a552d2dbc_93-119a024.pdf
        2011: https://content.legislation.vic.gov.au/sites/default/files/68a646e7-a547-39aa-adac-b2d5e4bfa756_93-119aa025%20authorised.pdf
        2019: https://content.legislation.vic.gov.au/sites/default/files/ad24ad2c-06f2-3ae3-b0ce-1fcd9b5f61a0_93-119aa026%20authorised.pdf        
        """
        self.define_holiday() \
            .with_name("Australia Day") \
            .on(VIC.mon_to_fri_on_or_following(month=1, day=26)) \
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
            .on(second("monday").of("march")) \
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
            .on(month=4, day=25) \
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
            .on(second("monday").of("june")) \
            .with_flags("V")

        self.define_holiday() \
            .with_name("King's Birthday") \
            .since(2023) \
            .on(second("monday").of("june")) \
            .with_flags("V")

        """
        Grand Final Eve
        the Friday before the Australian Football League Grand Final
        2019: https://content.legislation.vic.gov.au/sites/default/files/ad24ad2c-06f2-3ae3-b0ce-1fcd9b5f61a0_93-119aa026%20authorised.pdf
        """
        self.define_holiday() \
            .with_name("Grand Final Eve") \
            .since(2019) \
            .on(VIC.friday_before_afl_grand_final) \
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
            .on(first("tuesday").of("november")) \
            .with_flags("V")

        """
        25 December (Christmas Day) or the Monday after Christmas Day when Christmas Day is a Saturday or the Tuesday after Christmas Day when Christmas Day is a Sunday
        2009: https://content.legislation.vic.gov.au/sites/default/files/ccbe13db-9862-3b4f-b16c-8f9a552d2dbc_93-119a024.pdf
        2011: https://content.legislation.vic.gov.au/sites/default/files/68a646e7-a547-39aa-adac-b2d5e4bfa756_93-119aa025%20authorised.pdf
        2019: https://content.legislation.vic.gov.au/sites/default/files/ad24ad2c-06f2-3ae3-b0ce-1fcd9b5f61a0_93-119aa026%20authorised.pdf
        """
        self.define_holiday() \
            .with_name("Christmas Day") \
            .on(month=12, day=25) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Christmas Day (observed)") \
            .on(first("monday").after(month=12, day=25)) \
            .with_flags("RF") \
            .on_condition(self.date_is_saturday(month=12, day=25))

        self.define_holiday() \
            .with_name("Christmas Day (observed)") \
            .on(first("tuesday").after(month=12, day=25)) \
            .with_flags("RF") \
            .on_condition(self.date_is_sunday(month=12, day=25))

        """
        26 December (Boxing Day)
        the Monday after 26 December (Boxing Day) when Boxing Day is a Saturday or the Tuesday after Boxing Day when Boxing Day is a Sunday
        2009: https://content.legislation.vic.gov.au/sites/default/files/ccbe13db-9862-3b4f-b16c-8f9a552d2dbc_93-119a024.pdf
        2011: https://content.legislation.vic.gov.au/sites/default/files/68a646e7-a547-39aa-adac-b2d5e4bfa756_93-119aa025%20authorised.pdf
        2019: https://content.legislation.vic.gov.au/sites/default/files/ad24ad2c-06f2-3ae3-b0ce-1fcd9b5f61a0_93-119aa026%20authorised.pdf
        """
        self.define_holiday() \
            .with_name("Boxing Day") \
            .on(month=12, day=26) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Boxing Day (observed)") \
            .on(first("monday").after(month=12, day=26)) \
            .with_flags("RF") \
            .on_condition(self.date_is_saturday(month=12, day=26))

        self.define_holiday() \
            .with_name("Boxing Day (observed)") \
            .on(first("tuesday").after(month=12, day=26)) \
            .with_flags("RF") \
            .on_condition(self.date_is_sunday(month=12, day=26))

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
    def friday_before_afl_grand_final(year):
        """
        Usually, the Friday before last Saturday in September
        """
        exception = {
                2011: {"month":  9, "day": 31},  # MCG was occupied by the International Cricket Council (ICC)
                2015: {"month": 10, "day":  2},  # Due to scheduling of the 2015 Rugby World Cup
                2016: {"month":  9, "day": 31},
                2020: {"month": 10, "day": 23},  # Adaption due to the COVID-19 pandemic
        }

        if year in exception:
            return SmartDayArrow(year, **exception[year])

        return first("friday").before(last("saturday").of("september"))(year)

    @staticmethod
    def mon_to_fri_on_or_following(month, day):
        def wrapper(year):
            date = SmartDayArrow(year, month, day)

            if date.weekday() in ["saturday", "sunday"]:
                date.shift_to_weekday("monday", including=True)

            return date

        return wrapper
