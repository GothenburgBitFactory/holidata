from holidata.holiday import Region
from holidata.utils import day, first, date, Weekday, Month, dates


class WA(Region):
    def __init__(self, country):
        super().__init__("WA", country)

        """
        New Year's Day
        1st January
        When New Year's Day falls on a Saturday or Sunday the next following Monday is also a public holiday and bank holiday.
        https://www.legislation.wa.gov.au/legislation/statutes.nsf/RedirectURL?OpenAgent&query=mrdoc_19831.pdf
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
        26th January or, when that day falls on a Saturday or Sunday, the first Monday following the 26th January
        https://www.legislation.wa.gov.au/legislation/statutes.nsf/RedirectURL?OpenAgent&query=mrdoc_19831.pdf
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
        Monday on or first Monday following the 1st March
        https://www.legislation.wa.gov.au/legislation/statutes.nsf/RedirectURL?OpenAgent&query=mrdoc_19831.pdf
        """
        self.define_holiday() \
            .with_name("Labour Day") \
            .on(first(Weekday.MONDAY).of(Month.MARCH)) \
            .with_flags("V")

        """
        Good Friday
        https://www.legislation.wa.gov.au/legislation/statutes.nsf/RedirectURL?OpenAgent&query=mrdoc_19831.pdf
        """
        self.define_holiday() \
            .with_name("Good Friday") \
            .on(day(2).before(country.easter())) \
            .with_flags("RV")

        """
        Easter Sunday
        https://www.legislation.wa.gov.au/legislation/statutes.nsf/RedirectURL?OpenAgent&query=mrdoc_44571.pdf
        """
        self.define_holiday() \
            .with_name("Easter") \
            .since(2022) \
            .on(country.easter()) \
            .with_flags("RV")

        """
        Easter Monday
        https://www.legislation.wa.gov.au/legislation/statutes.nsf/RedirectURL?OpenAgent&query=mrdoc_19831.pdf
        """
        self.define_holiday() \
            .with_name("Easter Monday") \
            .on(day(1).after(country.easter())) \
            .with_flags("RV")

        """
        Anzac Day
        25th April
        When Anzac Day falls on a Saturday or Sunday the next following Monday is also a public holiday and bank holiday
        https://www.legislation.wa.gov.au/legislation/statutes.nsf/RedirectURL?OpenAgent&query=mrdoc_19831.pdf
        """
        self.define_holiday() \
            .with_name("Anzac Day") \
            .on(date(Month.APRIL, 25)) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Anzac Day (supplement)") \
            .on(first(Weekday.MONDAY).after(date(Month.APRIL, 25))) \
            .with_flags("F") \
            .on_condition(date(Month.APRIL, 25).is_one_of([Weekday.SATURDAY, Weekday.SUNDAY]))

        """
        Western Australia Day/Foundation Day
        Monday on or first Monday following the 1st June
        https://www.legislation.wa.gov.au/legislation/statutes.nsf/RedirectURL?OpenAgent&query=mrdoc_19831.pdf
        """
        self.define_holiday() \
            .with_name("Western Australia Day") \
            .on(first(Weekday.MONDAY).of(Month.JUNE)) \
            .with_flags("V")

        """
        Birthday of the Sovereign
        Dates proclaimed in the Government Gazettes https://www.legislation.wa.gov.au/legislation/statutes.nsf/gazettes.html
        day to be appointed for each year by proclamation published in the Government Gazette at least 3 weeks before the day so appointed
        https://www.legislation.wa.gov.au/legislation/statutes.nsf/RedirectURL?OpenAgent&query=mrdoc_19831.pdf
        """
        self.define_holiday() \
            .with_name("Queen's Birthday") \
            .on(dates({
                2011: (Month.OCTOBER, 28),    # 2010 234-6261
                2012: (Month.OCTOBER, 1),     # 2008 229-5633
                2013: (Month.SEPTEMBER, 30),  # 2008 229-5633
                2014: (Month.SEPTEMBER, 29),  # 2012  61-1687
                2015: (Month.SEPTEMBER, 28),  # 2012  61-1687
                2016: (Month.SEPTEMBER, 26),  # 2014  74-1595
                2017: (Month.SEPTEMBER, 25),  # 2014  74-1595
                2018: (Month.SEPTEMBER, 24),  # 2016  73-1379
                2019: (Month.SEPTEMBER, 30),  # 2016  73-1379
                2020: (Month.SEPTEMBER, 28),  # 2018  53-1287
                2021: (Month.SEPTEMBER, 27),  # 2018  53-1287
                2022: (Month.SEPTEMBER, 26),  # 2020 151-2919
            }))\
            .with_flags("V")

        self.define_holiday() \
            .with_name("King's Birthday") \
            .on(dates({
                2023: (Month.SEPTEMBER, 25),  # 2020 151-2919
                2024: (Month.SEPTEMBER, 23),  # 2022  69-3009
                2025: (Month.SEPTEMBER, 29),  # 2022  69-3009
            })) \
            .with_flags("V")

        """
        National Day of Mourning for Queen Elizabeth II
        2022-09-22
        https://www.legislation.wa.gov.au/legislation/prod/gazettestore.nsf/FileURL/gg2022_138.pdf/$FILE/Gg2022_138.pdf?OpenElement
        """
        self.define_holiday() \
            .with_name("National Day of Mourning for Queen Elizabeth II") \
            .in_years([2022]) \
            .on(date(Month.SEPTEMBER, 22)) \
            .with_flags("F")

        """
        Christmas Day
        25th December
        When Christmas Day falls on a Saturday or Sunday the next following Monday is also a public holiday and bank holiday
        https://www.legislation.wa.gov.au/legislation/statutes.nsf/RedirectURL?OpenAgent&query=mrdoc_19831.pdf
        """
        self.define_holiday() \
            .with_name("Christmas Day") \
            .on(date(Month.DECEMBER, 25)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Christmas Day (observed)") \
            .on(first(Weekday.MONDAY).after(date(Month.DECEMBER, 25))) \
            .with_flags("RV") \
            .on_condition(date(Month.DECEMBER, 25).is_one_of([Weekday.SATURDAY, Weekday.SUNDAY]))

        """
        Boxing Day
        26th December
        When Boxing Day falls on a Saturday the next following Monday is also a public holiday and bank holiday
        When Boxing Day falls on a Sunday or Monday the next following Tuesday is also a public holiday and bank holiday
        https://www.legislation.wa.gov.au/legislation/statutes.nsf/RedirectURL?OpenAgent&query=mrdoc_19831.pdf
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
