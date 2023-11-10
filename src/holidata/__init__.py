from .emitters import Emitter
from .holidays import *


def get_country_for(identifier):
    country_class = Country.get(identifier)

    if not country_class:
        raise ValueError(f"No country found for id '{identifier}'!")

    return country_class()


def get_emitter_for(identifier):
    emitter_class = Emitter.get(identifier)

    if not emitter_class:
        raise ValueError(f"Unsupported output format '{identifier}'!")

    return emitter_class()


def for_locale(country_id, lang_id=None):
    country = get_country_for(country_id)
    lang_id = country.validate_language_or_get_default(lang_id)

    return Locale(country, lang_id)


class Holidata:
    emitter = None
    holidays = None

    def __init__(self, holidays, emitter=None):
        self.holidays = holidays
        self.emitter = emitter

    def __str__(self):
        return self.emitter.output(self.holidays)

    def formatted_as(self, format_id):
        self.emitter = get_emitter_for(format_id)

        return self


class Locale:
    def __init__(self, country, lang):
        self.country = country
        self.lang = lang

    def get_holidays_of(self, year):
        return self.country.get_holidays_of(year, self.lang)

    def holidays_of(self, year):
        return Holidata(self.country.get_holidays_of(self._parse_year(year), self.lang))

    @staticmethod
    def _parse_year(year):
        try:
            return int(year)
        except ValueError:
            raise ValueError(f"Invalid year '{year}'! Has to be an integer.")

    @property
    def id(self):
        return f"{self.lang}-{self.country.id}"
