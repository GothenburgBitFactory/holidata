from holidata.holiday import Region
from holidata.utils import Month, Weekday, date, day, first, second


class QLD(Region):
    def __init__(self, country):
        super().__init__("QLD", country)

        """
        New Year's Day
        Public holiday on 1 January.
        When 1 January is a Saturday or Sunday, there is to be an additional public holiday on the following Monday.
        https://www.legislation.qld.gov.au/view/html/2010-12-10/act-1983-018
        https://www.legislation.qld.gov.au/view/html/2011-12-06/act-1983-018
        """
        self.define_holiday() \
            .with_name("New Year's Day") \
            .on(date(Month.JANUARY, 1)) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("New Year's Day (observed)") \
            .since(2012) \
            .on(first(Weekday.MONDAY).after(date(Month.JANUARY, 1))) \
            .with_flags("V") \
            .on_condition(date(Month.JANUARY, 1).is_one_of([Weekday.SATURDAY, Weekday.SUNDAY]))

        """
        Australia Day
        Public holiday on 26 January.
        When 26 January is a Saturday or Sunday, there is to be no public holiday on that day and instead the following Monday is to be a public holiday.
        https://www.legislation.qld.gov.au/view/html/2010-12-10/act-1983-018
        https://www.legislation.qld.gov.au/view/html/2011-12-06/act-1983-018
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
        Good Friday
        Public holiday on the Friday publicly observed as Good Friday.
        https://www.legislation.qld.gov.au/view/html/2010-12-10/act-1983-018
        """
        self.define_holiday() \
            .with_name("Good Friday") \
            .on(day(2).before(country.easter())) \
            .with_flags("RV")

        """
        Easter Saturday
        Public holiday on the day after Good Friday.
        https://www.legislation.qld.gov.au/view/html/2010-12-10/act-1983-018
        """
        self.define_holiday() \
            .with_name("Easter Saturday") \
            .on(day(1).before(country.easter())) \
            .with_flags("RV")

        """
        Easter Sunday
        Public holiday on the Sunday following Good Friday.
        https://www.legislation.qld.gov.au/view/html/2017-03-01/act-1983-018
        """
        self.define_holiday() \
            .with_name("Easter") \
            .since(2017) \
            .on(country.easter()) \
            .with_flags("RV")

        """
        Easter Monday
        Public holiday on the Monday following Good Friday.
        https://www.legislation.qld.gov.au/view/html/2010-12-10/act-1983-018
        """
        self.define_holiday() \
            .with_name("Easter Monday") \
            .on(day(1).after(country.easter())) \
            .with_flags("RV")

        """
        Anzac Day
        Public holiday on 25 April.
        25 April (Anzac Day) A public holiday is to be observed on—
        (a) 25 April; or
        (b) if 25 April is a Sunday—the following Monday.
        https://www.legislation.qld.gov.au/view/html/2010-12-10/act-1983-018
        https://www.legislation.qld.gov.au/view/html/2011-12-06/act-1983-018
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
        Labour Day
        https://www.legislation.qld.gov.au/view/html/2010-12-10/act-1983-018
        """
        self.define_holiday() \
            .with_name("Labour Day") \
            .until(2011) \
            .on(date(Month.MAY, 1)) \
            .with_flags("F")

        """
        A public holiday is to be observed on—
        (a) 1 May; or
        (b) if 1 May is a day other than a Monday—the following Monday.
        https://www.legislation.qld.gov.au/view/html/2011-12-06/act-1983-018
        """
        self.define_holiday() \
            .with_name("Labour Day") \
            .since(2012) \
            .until(2012) \
            .on(first(Weekday.MONDAY).of(Month.MAY)) \
            .with_flags("V")

        """
        A public holiday is to be observed on the first Monday in October.
        https://www.legislation.qld.gov.au/view/html/2012-11-08/act-1983-018
        """
        self.define_holiday() \
            .with_name("Labour Day") \
            .since(2013) \
            .until(2015) \
            .on(first(Weekday.MONDAY).of(Month.OCTOBER)) \
            .with_flags("V")

        """
        A public holiday is to be observed on the first Monday in May.
        https://www.legislation.qld.gov.au/view/html/2015-10-22/act-1983-018
        """
        self.define_holiday() \
            .with_name("Labour Day") \
            .since(2016) \
            .on(first(Weekday.MONDAY).of(Month.MAY)) \
            .with_flags("V")

        """
        Birthday of the Sovereign
        https://www.legislation.qld.gov.au/view/html/2010-12-10/act-1983-018
        """
        self.define_holiday() \
            .with_name("Queen's Birthday") \
            .until(2011) \
            .on(second(Weekday.MONDAY).of(Month.JUNE)) \
            .with_flags("V")

        """
        https://www.legislation.qld.gov.au/view/html/2011-12-06/act-1983-018
        """
        self.define_holiday() \
            .with_name("Queen's Birthday") \
            .since(2012) \
            .until(2012) \
            .on(first(Weekday.MONDAY).of(Month.OCTOBER)) \
            .with_flags("V")

        """
        https://www.legislation.qld.gov.au/view/html/2012-11-08/act-1983-018
        """
        self.define_holiday() \
            .with_name("Queen's Birthday") \
            .since(2013) \
            .until(2015) \
            .on(second(Weekday.MONDAY).of(Month.JUNE)) \
            .with_flags("V")

        """
        https://www.legislation.qld.gov.au/view/html/2015-10-22/act-1983-018
        """
        self.define_holiday() \
            .with_name("Queen's Birthday") \
            .since(2016) \
            .until(2021) \
            .on(first(Weekday.MONDAY).of(Month.OCTOBER)) \
            .with_flags("V")

        self.define_holiday() \
            .with_name("King's Birthday") \
            .since(2022) \
            .on(first(Weekday.MONDAY).of(Month.OCTOBER)) \
            .with_flags("V")

        """
        Queen's Diamond Jubilee
        https://www.legislation.qld.gov.au/view/html/2011-12-06/act-1983-018
        """
        self.define_holiday() \
            .with_name("Queen's Diamond Jubilee") \
            .in_years([2012]) \
            .on(date(Month.JUNE, 11)) \
            .with_flags("F")

        """
        National Day of Mourning for Her Majesty The Queen
        https://www.legislation.qld.gov.au/view/html/2022-09-15/act-1983-018
        """
        self.define_holiday() \
            .with_name("National Day of Mourning for Her Majesty The Queen") \
            .in_years([2022]) \
            .on(date(Month.SEPTEMBER, 22)) \
            .with_flags("F")

        """
        Christmas Day
        Public holiday on 25 December.
        https://www.legislation.qld.gov.au/view/html/2010-12-10/act-1983-018
        https://www.legislation.qld.gov.au/view/html/2011-12-06/act-1983-018
        """
        self.define_holiday() \
            .with_name("Christmas Day") \
            .on(date(Month.DECEMBER, 25)) \
            .with_flags("RF")

        """
        27 December
        A public holiday is to be observed on 27 December only if 25 December is a Saturday or Sunday.
        """
        self.define_holiday() \
            .with_name("Christmas Day (observed)") \
            .on(date(Month.DECEMBER, 27)) \
            .with_flags("RF") \
            .on_condition(date(Month.DECEMBER, 25).is_one_of([Weekday.SATURDAY, Weekday.SUNDAY]))

        """
        Boxing Day
        Public holiday on 26 December.
        https://www.legislation.qld.gov.au/view/html/2010-12-10/act-1983-018
        https://www.legislation.qld.gov.au/view/html/2011-12-06/act-1983-018
        """
        self.define_holiday() \
            .with_name("Boxing Day") \
            .on(date(Month.DECEMBER, 26)) \
            .with_flags("RF")

        """
        28 December 
        A public holiday is to be observed on 28 December only if 26 December is a Saturday or Sunday.
        """
        self.define_holiday() \
            .with_name("Boxing Day (observed)") \
            .on(date(Month.DECEMBER, 28)) \
            .with_flags("RF") \
            .on_condition(date(Month.DECEMBER, 26).is_one_of([Weekday.SATURDAY, Weekday.SUNDAY]))
