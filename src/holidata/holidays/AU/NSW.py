from holidata.holiday import Region
from holidata.utils import day, second, first, date


class NSW(Region):
    def __init__(self, country):
        super().__init__("NSW", country)

        """
        New Year's Day
        Public holiday on 1 January.
        When 1 January is a Saturday or Sunday, there is to be an additional public holiday on the following Monday.
        https://legislation.nsw.gov.au/view/html/inforce/2011-12-31/act-2010-115
        https://legislation.nsw.gov.au/view/html/inforce/2012-07-06/act-2010-115
        https://legislation.nsw.gov.au/view/html/inforce/2023-01-13/act-2010-115
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
        Public holiday on 26 January.
        When 26 January is a Saturday or Sunday, there is to be no public holiday on that day and instead the following Monday is to be a public holiday.
        https://legislation.nsw.gov.au/view/html/inforce/2011-12-31/act-2010-115
        https://legislation.nsw.gov.au/view/html/inforce/2012-07-06/act-2010-115
        https://legislation.nsw.gov.au/view/html/inforce/2023-01-13/act-2010-115
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
        Public holiday on the Friday publicly observed as Good Friday.
        https://legislation.nsw.gov.au/view/html/inforce/2011-12-31/act-2010-115
        https://legislation.nsw.gov.au/view/html/inforce/2012-07-06/act-2010-115
        https://legislation.nsw.gov.au/view/html/inforce/2023-01-13/act-2010-115
        """
        self.define_holiday() \
            .with_name("Good Friday") \
            .on(day(2).before(country.easter())) \
            .with_flags("RV")

        """
        Easter Saturday
        Public holiday on the day after Good Friday.
        https://legislation.nsw.gov.au/view/html/inforce/2011-12-31/act-2010-115
        https://legislation.nsw.gov.au/view/html/inforce/2012-07-06/act-2010-115
        https://legislation.nsw.gov.au/view/html/inforce/2023-01-13/act-2010-115
        """
        self.define_holiday() \
            .with_name("Easter Saturday") \
            .on(day(1).before(country.easter())) \
            .with_flags("RV")

        """
        Easter Sunday
        Public holiday on the Sunday following Good Friday.
        https://legislation.nsw.gov.au/view/html/inforce/2011-12-31/act-2010-115
        https://legislation.nsw.gov.au/view/html/inforce/2012-07-06/act-2010-115
        https://legislation.nsw.gov.au/view/html/inforce/2023-01-13/act-2010-115
        """
        self.define_holiday() \
            .with_name("Easter") \
            .on(country.easter()) \
            .with_flags("RV")

        """
        Easter Monday
        Public holiday on the Monday following Good Friday.
        https://legislation.nsw.gov.au/view/html/inforce/2011-12-31/act-2010-115
        https://legislation.nsw.gov.au/view/html/inforce/2012-07-06/act-2010-115
        https://legislation.nsw.gov.au/view/html/inforce/2023-01-13/act-2010-115
        """
        self.define_holiday() \
            .with_name("Easter Monday") \
            .on(day(1).after(country.easter())) \
            .with_flags("RV")

        """
        Anzac Day
        Public holiday on 25 April.
        https://legislation.nsw.gov.au/view/html/inforce/2011-12-31/act-2010-115
        https://legislation.nsw.gov.au/view/html/inforce/2012-07-06/act-2010-115
        https://legislation.nsw.gov.au/view/html/inforce/2023-01-13/act-2010-115
        """
        self.define_holiday() \
            .with_name("Anzac Day") \
            .on(date(month=4, day=25)) \
            .with_flags("F")

        """
        Queen's Birthday
        Public holiday on the second Monday in June.
        https://legislation.nsw.gov.au/view/html/inforce/2011-12-31/act-2010-115
        https://legislation.nsw.gov.au/view/html/inforce/2012-07-06/act-2010-115
        """
        self.define_holiday() \
            .with_name("Queen's Birthday") \
            .until(2022) \
            .on(second("monday").of("june")) \
            .with_flags("V")

        """
        King's Birthday
        Public holiday on the second Monday in June.
        https://legislation.nsw.gov.au/view/html/inforce/2023-01-13/act-2010-115
        """
        self.define_holiday() \
            .with_name("King's Birthday") \
            .since(2023) \
            .on(second("monday").of("june")) \
            .with_flags("V")

        """
        Labour Day
        Public holiday on the first Monday in October.
        https://legislation.nsw.gov.au/view/html/inforce/2011-12-31/act-2010-115
        https://legislation.nsw.gov.au/view/html/inforce/2012-07-06/act-2010-115
        https://legislation.nsw.gov.au/view/html/inforce/2023-01-13/act-2010-115
        """
        self.define_holiday() \
            .with_name("Labour Day") \
            .on(first("monday").of("october")) \
            .with_flags("V")

        """
        Christmas Day
        Public holiday on 25 December.
        When 25 December is a Saturday, there is to be an additional public holiday on the following Monday.
        When 25 December is a Sunday, there is to be an additional public holiday on the following Tuesday.
        https://legislation.nsw.gov.au/view/html/inforce/2011-12-31/act-2010-115
        https://legislation.nsw.gov.au/view/html/inforce/2012-07-06/act-2010-115
        https://legislation.nsw.gov.au/view/html/inforce/2023-01-13/act-2010-115
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
        Public holiday on 26 December.
        When 26 December is a Saturday, there is to be an additional public holiday on the following Monday.
        When 26 December is a Sunday, there is to be an additional public holiday on the following Tuesday.
        https://legislation.nsw.gov.au/view/html/inforce/2011-12-31/act-2010-115
        https://legislation.nsw.gov.au/view/html/inforce/2012-07-06/act-2010-115
        https://legislation.nsw.gov.au/view/html/inforce/2023-01-13/act-2010-115
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
