from holidata.holiday import Region
from holidata.utils import SmartDayArrow, day, first


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
            .on(month=1, day=1) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("New Year's Day (observed)") \
            .on(first("monday").after(month=1, day=1)) \
            .with_flags("V") \
            .on_condition(self.date_is_on_weekend(month=1, day=1))

        """
        Australia Day
        26th January or, when that day falls on a Saturday or Sunday, the first Monday following the 26th January
        https://www.legislation.wa.gov.au/legislation/statutes.nsf/RedirectURL?OpenAgent&query=mrdoc_19831.pdf
        """
        self.define_holiday() \
            .with_name("Australia Day") \
            .on(self.mon_to_fri_on_or_following(month=1, day=26)) \
            .with_flags("V")

        """
        Labour Day
        Monday on or first Monday following the 1st March
        https://www.legislation.wa.gov.au/legislation/statutes.nsf/RedirectURL?OpenAgent&query=mrdoc_19831.pdf
        """
        self.define_holiday() \
            .with_name("Labour Day") \
            .on(self.monday_on_or_first_monday_following(month=3, day=1)) \
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
            .on(month=4, day=25) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Anzac Day (supplement)") \
            .on(first("monday").after(month=4, day=25)) \
            .with_flags("F") \
            .on_condition(self.date_is_on_weekend(month=4, day=25))

        """
        Western Australia Day/Foundation Day
        Monday on or first Monday following the 1st June
        https://www.legislation.wa.gov.au/legislation/statutes.nsf/RedirectURL?OpenAgent&query=mrdoc_19831.pdf
        """
        self.define_holiday() \
            .with_name("Western Australia Day") \
            .on(self.monday_on_or_first_monday_following(month=6, day=1)) \
            .with_flags("V")

        """
        Birthday of the Sovereign
        day to be appointed for each year by proclamation published in the Government Gazette at least 3 weeks before the day so appointed
        https://www.legislation.wa.gov.au/legislation/statutes.nsf/RedirectURL?OpenAgent&query=mrdoc_19831.pdf
        """
        self.define_holiday() \
            .with_name("Queen's Birthday") \
            .until(2022) \
            .on(self.birthday_of_the_sovereign) \
            .with_flags("V")

        self.define_holiday() \
            .with_name("King's Birthday") \
            .since(2023) \
            .on(self.birthday_of_the_sovereign) \
            .with_flags("V")

        """
        National Day of Mourning for Queen Elizabeth II
        2022-09-22
        https://www.legislation.wa.gov.au/legislation/prod/gazettestore.nsf/FileURL/gg2022_138.pdf/$FILE/Gg2022_138.pdf?OpenElement
        """
        self.define_holiday() \
            .with_name("National Day of Mourning for Queen Elizabeth II") \
            .in_years([2022]) \
            .on(month=9, day=22) \
            .with_flags("F")

        """
        Christmas Day
        25th December
        When Christmas Day falls on a Saturday or Sunday the next following Monday is also a public holiday and bank holiday
        https://www.legislation.wa.gov.au/legislation/statutes.nsf/RedirectURL?OpenAgent&query=mrdoc_19831.pdf
        """
        self.define_holiday() \
            .with_name("Christmas Day") \
            .on(month=12, day=25) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Christmas Day (observed)") \
            .on(first("monday").after(month=12, day=25)) \
            .with_flags("RV") \
            .on_condition(self.date_is_on_weekend(month=12, day=25))

        """
        Boxing Day
        26th December
        When Boxing Day falls on a Saturday the next following Monday is also a public holiday and bank holiday
        When Boxing Day falls on a Sunday or Monday the next following Tuesday is also a public holiday and bank holiday
        https://www.legislation.wa.gov.au/legislation/statutes.nsf/RedirectURL?OpenAgent&query=mrdoc_19831.pdf
        """
        self.define_holiday() \
            .with_name("Boxing Day") \
            .on(month=12, day=26) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Boxing Day (observed)") \
            .on(first("monday").after(month=12, day=26)) \
            .with_flags("RV") \
            .on_condition(self.date_is_saturday(month=12, day=26))

        self.define_holiday() \
            .with_name("Boxing Day (observed)") \
            .on(first("tuesday").after(month=12, day=26)) \
            .with_flags("RV") \
            .on_condition(self.date_is_sunday_or_monday(month=12, day=26))

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
    def date_is_sunday_or_monday(month, day):
        def wrapper(year):
            return SmartDayArrow(year, month, day).weekday() in ["sunday", "monday"]

        return wrapper

    @staticmethod
    def monday_on_or_first_monday_following(month, day):
        def wrapper(year):
            return SmartDayArrow(year, month, day).shift_to_weekday("monday", including=True)

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
    def birthday_of_the_sovereign(year):
        """
        Dates proclaimed in the Government Gazettes
        https://www.legislation.wa.gov.au/legislation/statutes.nsf/gazettes.html
        """
        date = {
            2011: {"month": 10, "day": 28},  # 2010 234-6261
            2012: {"month": 10, "day":  1},  # 2008 229-5633
            2013: {"month":  9, "day": 30},  # 2008 229-5633
            2014: {"month":  9, "day": 29},  # 2012  61-1687
            2015: {"month":  9, "day": 28},  # 2012  61-1687
            2016: {"month":  9, "day": 26},  # 2014  74-1595
            2017: {"month":  9, "day": 25},  # 2014  74-1595
            2018: {"month":  9, "day": 24},  # 2016  73-1379
            2019: {"month":  9, "day": 30},  # 2016  73-1379
            2020: {"month":  9, "day": 28},  # 2018  53-1287
            2021: {"month":  9, "day": 27},  # 2018  53-1287
            2022: {"month":  9, "day": 26},  # 2020 151-2919
            2023: {"month":  9, "day": 25},  # 2020 151-2919
            2024: {"month":  9, "day": 23},  # 2022  69-3009
            2025: {"month":  9, "day": 29},  # 2022  69-3009
        }

        return SmartDayArrow(year, **date.get(year)) if date.get(year) is not None else None
