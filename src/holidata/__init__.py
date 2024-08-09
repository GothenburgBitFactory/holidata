from typing import Iterator

from holidata.emitters import Emitter
from holidata.holiday import Country, Holiday
from holidata.holidays import *


class Holidata:
    def __init__(self, holidays, emitter: Emitter = None):
        self.holidays = holidays
        self.emitter = emitter

    def __str__(self) -> str:
        return self.emitter.output(self.holidays)

    def formatted_as(self, format_id: str) -> 'Holidata':
        self.emitter = get_emitter_for(format_id)

        return self


class Locale:
    def __init__(self, country: Country, lang: str):
        self.country = country
        self.lang = lang

    def get_holidays_of(self, year: int) -> Iterator[Holiday]:
        return self.country.get_holidays_of(year, self.lang)

    def holidays_of(self, year: str) -> Holidata:
        return Holidata(self.country.get_holidays_of(Locale._parse_year(year), self.lang))

    @staticmethod
    def _parse_year(year: str) -> int:
        try:
            return int(year)
        except ValueError:
            raise ValueError(f"Invalid year '{year}'! Has to be an integer.")

    @property
    def id(self) -> str:
        return f"{self.lang}-{self.country.id}"


def get_country_for(identifier: str) -> Country:
    country_class = Country.get(identifier)

    if not country_class:
        raise ValueError(f"No country found for id '{identifier}'!")

    return country_class()


def get_emitter_for(identifier: str) -> Emitter:
    emitter_class = Emitter.get(identifier)

    if not emitter_class:
        raise ValueError(f"Unsupported output format '{identifier}'!")

    return emitter_class()


def for_locale(country_id: str, lang_id: str = None) -> Locale:
    country = get_country_for(country_id)
    lang_id = country.validate_language_or_get_default(lang_id)

    return Locale(country, lang_id)
