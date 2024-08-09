import datetime
from dataclasses import dataclass
from typing import Iterator, Callable, Union, Dict, List

import dateutil

from holidata.plugin import PluginMount
from holidata.utils import SmartDayArrow, date


@dataclass
class Holiday:
    """
    A sheer container for one holiday.
    """
    locale: str
    region: str
    date: datetime.date
    description: str
    flags: str = ""
    notes: str = ""

    def as_dict(self) -> dict:
        return {
            "locale": self.locale,
            "region": self.region,
            "date": self.date.strftime("%Y-%m-%d"),
            "description": self.description,
            "type": self.flags,
            "notes": self.notes
        }


class HolidayGenerator:
    def __init__(self, country_id: str, default_lang: str):
        self.name_dict: Dict[str, str] = {}
        self.notes: str = ""
        self.regions: List[str] = [""]
        self.flags: str = ""
        self.date: callable = None
        self.country_id: str = country_id
        self.default_lang: str = default_lang
        self.filters: List[callable] = []

    def with_name(self, name: str, lang: str = None) -> 'HolidayGenerator':
        lang = self.default_lang if lang is None else lang
        self.name_dict[lang] = name
        return self

    def with_names(self, name_dict: Dict[str, str]) -> 'HolidayGenerator':
        self.name_dict = name_dict
        return self

    def on(self, date_func: callable = None, month: int = None, day: int = None) -> 'HolidayGenerator':
        if month is not None and day is not None:
            self.date = date(month, day)
        elif callable(date_func):
            self.date = date_func
        else:
            raise ValueError("Invalid reference date")

        return self

    def with_flags(self, flags: str) -> 'HolidayGenerator':
        self.flags = flags
        return self

    def in_regions(self, regions: List[str]) -> 'HolidayGenerator':
        self.regions = regions
        return self

    def in_region(self, region: str) -> 'HolidayGenerator':
        self.regions = [region]
        return self

    def annotated_with(self, note: str) -> 'HolidayGenerator':
        self.notes = note
        return self

    def in_years(self, reference: List[int]) -> 'HolidayGenerator':
        def reference_does_contain(year: int) -> bool:
            return year in reference

        self.filters.append(reference_does_contain)
        return self

    def since(self, reference: int) -> 'HolidayGenerator':
        def reference_is_less_or_equal_to(year: int) -> bool:
            return reference <= year

        self.filters.append(reference_is_less_or_equal_to)
        return self

    def until(self, reference: int) -> 'HolidayGenerator':
        def reference_is_greater_or_equal_to(year: int) -> bool:
            return reference >= year

        self.filters.append(reference_is_greater_or_equal_to)
        return self

    def except_for(self, reference: List[int]) -> 'HolidayGenerator':
        def reference_does_not_contain(year: int) -> bool:
            return year not in reference

        self.filters.append(reference_does_not_contain)
        return self

    def on_condition(self, condition: callable) -> 'HolidayGenerator':
        self.filters.append(condition)
        return self

    def build_for_year_and_lang(self, year: int, lang: str) -> Iterator[Holiday]:
        for filter in self.filters:
            if not filter(year):
                return []

        for region in self.regions:
            date = self.date(year)
            if date is None:
                continue
            yield Holiday(
                locale=f"{lang}-{self.country_id}",
                region=region,
                date=date,
                description=self.name_dict[lang],
                flags=self.flags,
                notes=self.notes,
            )


class Country(metaclass=PluginMount):
    """
    Represents holidays of a given country
    """
    id: str
    languages: List[str]
    default_lang: Union[str, None] = None
    easter_type: str
    holiday_generators: list
    regions: list

    def __init__(self):
        if not self.id:
            raise ValueError(f"Country '{self.__class__.__name__}' does not provide an id!")
        if not self.languages:
            raise ValueError(f"Country '{self.__class__.__name__}' does not list any languages!")
        if self.default_lang is not None and self.default_lang not in self.languages:
            raise ValueError(f"Country '{self.__class__.__name__}' does not list language '{self.default_lang}'!")

        self.holiday_generators = []
        self.regions = []

    @staticmethod
    def get(identifier):
        return Country.get_plugin(identifier, "id")

    def validate_language_or_get_default(self, lang_id: str) -> str:
        if lang_id and lang_id.lower() not in self.languages:
            raise ValueError(
                f"Language '{lang_id}' is not defined for country '{self.id}'! Choose one of [{', '.join(self.languages)}].")
        elif lang_id is None and self.default_lang:
            lang_id = self.default_lang
        elif lang_id is None:
            raise ValueError(
                f"Country '{self.id}' has no default language specified! Choose one of [{', '.join(self.languages)}].")

        return lang_id.lower()

    def define_holiday(self) -> HolidayGenerator:
        generator = HolidayGenerator(self.id, self.default_lang)
        self.holiday_generators.append(generator)
        return generator

    def get_holidays_of(self, year: int, lang: str) -> Iterator[Holiday]:
        for generator in self.holiday_generators:
            yield from generator.build_for_year_and_lang(year, lang)
        for region in self.regions:
            yield from region.get_holidays_of(year, lang)

    def easter(self) -> Callable[[int], SmartDayArrow]:
        def wrapper(year: int) -> SmartDayArrow:
            date = dateutil.easter.easter(year, self.easter_type)
            return SmartDayArrow(date.year, date.month, date.day)

        return wrapper


class Region:
    def __init__(self, id: str, country: Country):
        self.id: str = id
        self.country: Country = country
        self.holiday_generators: List[HolidayGenerator] = []

    def define_holiday(self) -> HolidayGenerator:
        generator = HolidayGenerator(self.country.id, self.country.default_lang)
        generator.in_region(self.id)
        self.holiday_generators.append(generator)
        return generator

    def get_holidays_of(self, year: int, lang: str) -> Iterator[Holiday]:
        for generator in self.holiday_generators:
            yield from generator.build_for_year_and_lang(year, lang)
