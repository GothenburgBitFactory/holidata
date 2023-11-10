import re

from holidata.plugin import PluginMount
from holidata.utils import SmartDayArrow, month_reference, easter


class Holiday:
    """
    A sheer container for one holiday.
    """

    def __init__(self, locale, region, date, description, flags="", notes=""):
        self.locale = locale
        self.region = region
        self.date = date
        self.description = description
        self.flags = flags
        self.notes = notes

    def as_dict(self):
        return {
            "locale": self.locale,
            "region": self.region,
            "date": self.date.strftime("%Y-%m-%d"),
            "description": self.description,
            "type": self.flags,
            "notes": self.notes
        }


class HolidayGenerator(object):
    name_dict = dict()
    default_lang = None
    country_id = None

    fixed_regex = re.compile(
        r"^\s*(?P<month>\d\d)-(?P<day>\d\d)$",
        re.UNICODE,
    )
    nth_weekday_regex = re.compile(
        r"^\s*(?P<order>\d+)\.(?P<last> last | )(?P<weekday>[a-z]+) in (?P<month>[a-zA-Z]+)$",
        re.UNICODE,
    )
    easter_shift_regex = re.compile(
        r"^\s*((?P<days>\d+) day(s)? (?P<direction>(before|after)) )?Easter$",
        re.UNICODE,
    )

    def __init__(self, country_id, default_lang, easter_type):
        self.name_dict = dict()
        self.notes = ""
        self.regions = [""]
        self.flags = ""
        self.date = None
        self.country_id = country_id
        self.default_lang = default_lang
        self.easter_type = easter_type
        self.filters = []

    def with_name(self, name, lang=None):
        lang = self.default_lang if lang is None else lang
        self.name_dict[lang] = name
        return self

    def with_names(self, name_dict):
        self.name_dict = name_dict
        return self

    def on(self, date):
        self.date = date
        return self

    def with_flags(self, flags):
        self.flags = flags
        return self

    def in_regions(self, regions):
        self.regions = regions
        return self

    def in_region(self, region):
        self.regions = [region]
        return self

    def annotated_with(self, note):
        self.notes = note
        return self

    def in_years(self, reference):
        def reference_does_contain(year):
            return year in reference

        self.filters.append(reference_does_contain)

        return self

    def since(self, reference):
        def reference_is_less_or_equal_to(year):
            return reference <= year

        self.filters.append(reference_is_less_or_equal_to)
        return self

    def until(self, reference):
        def reference_is_greater_or_equal_to(year):
            return reference >= year

        self.filters.append(reference_is_greater_or_equal_to)
        return self

    def except_for(self, reference):
        def reference_does_not_contain(year):
            return year not in reference

        self.filters.append(reference_does_not_contain)

        return self

    def on_condition(self, condition):
        self.filters.append(condition)

        return self

    def _create_date(self, date, year):
        if callable(date):
            return date(year)

        function_map = [
            (self.fixed_regex, self._date_from_fixed_reference),
            (self.nth_weekday_regex, self._date_from_weekday_reference),
            (self.easter_shift_regex, self._date_from_easter_reference),
        ]

        for reg_exp, create_date_from in function_map:
            m = reg_exp.search(date)
            if m is not None:
                return create_date_from(m, year)

        return None

    def build_for_year_and_lang(self, year, lang):
        for filter in self.filters:
            if not filter(year):
                return []

        for region in self.regions:
            yield Holiday(
                locale=f"{lang}-{self.country_id}",
                region=region,
                date=self._create_date(self.date, year),
                description=self.name_dict[lang],
                flags=self.flags,
                notes=self.notes,
            )

    @staticmethod
    def _date_from_fixed_reference(m, year):
        return SmartDayArrow(year, int(m.group("month")), int(m.group("day")))

    @staticmethod
    def _date_from_weekday_reference(m, year):
        return month_reference(
            year, m.group("month"), first=m.group("last").strip() == ""
        ).shift_to_weekday(
            m.group("weekday"),
            order=int(m.group("order")),
            reverse=m.group("last").strip() == "last",
            including=True,
        )

    def _date_from_easter_reference(self, m, year):
        if self.easter_type is None:
            raise ValueError(f"Country '{self.country_id}' does not provide its easter type! Should be one of [WESTERN|ORTHODOX].")

        return easter(year, self.easter_type).shift(
            days=int((m.group("days")) if m.group("days") is not None else 0) * (1 if m.group("direction") == "after" else -1)
        )


class Country(metaclass=PluginMount):
    """
    Represents holidays of a given country
    """
    id = None
    languages = []
    default_lang = None
    easter_type = None
    holiday_generators = []

    def __init__(self):
        self.holiday_generators = []
        self.regions = []

        if self.id is None:
            raise ValueError(f"Country '{self.__class__.__name__}' does not provide an id!")

        if not self.languages:
            raise ValueError(f"Country '{self.__class__.__name__}' does not list any languages!")

        if self.default_lang is not None and self.default_lang not in self.languages:
            raise ValueError(f"Country '{self.__class__.__name__}' does not list language '{self.default_lang}'!")

    @staticmethod
    def get(identifier):
        return Country.get_plugin(identifier, "id")

    def validate_language_or_get_default(self, lang_id):
        if lang_id is not None and lang_id.lower() not in self.languages:
            raise ValueError(
                f"Language '{lang_id}' is not defined for country '{self.id}'! Choose one of [{', '.join(self.languages)}].")
        elif lang_id is None and self.default_lang is not None:
            lang_id = self.default_lang
        elif lang_id is None:
            raise ValueError(
                f"Country '{self.id}' has no default language specified! Choose one of [{', '.join(self.languages)}].")

        return lang_id.lower()

    def define_holiday(self):
        generator = HolidayGenerator(self.id, self.default_lang, self.easter_type)
        self.holiday_generators += [generator]
        return generator

    def get_holidays_of(self, year, lang):
        for generator in self.holiday_generators:
            for holiday in generator.build_for_year_and_lang(year, lang):
                yield holiday

        for region in self.regions:
            for holiday in region.get_holidays_of(year, lang):
                yield holiday


class Region:
    def __init__(self, id, country):
        self.id = id
        self.country = country
        self.holiday_generators = []

    def define_holiday(self):
        generator = HolidayGenerator(self.country.id, self.country.default_lang, self.country.easter_type)
        generator.in_region(self.id)
        self.holiday_generators += [generator]
        return generator

    def get_holidays_of(self, year, lang):
        for generator in self.holiday_generators:
            for holiday in generator.build_for_year_and_lang(year, lang):
                yield holiday
