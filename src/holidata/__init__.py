from .holidays import *
from .emitters import Emitter


def get_country_for(identifier):
    country_class = Country.get(identifier)

    if not country_class:
        raise ValueError(f"No plugin found for country id '{identifier}'!")

    return country_class()


def get_locale_for(identifier):
    locale_class = Locale.get(identifier)

    if not locale_class:
        raise ValueError(f"No plugin found for locale '{identifier}'!")

    return locale_class()


def get_emitter_for(identifier):
    emitter_class = Emitter.get(identifier)

    if not emitter_class:
        raise ValueError(f"Unsupported output format '{identifier}'!")

    return emitter_class()


def create_locale_for(country_id=None, lang_id=None):
    country = get_country_for(country_id)
    lang_id = country.validate_language_or_get_default(lang_id)

    return get_locale_for(f"{lang_id}-{country_id}")


def parse_year(year):
    try:
        return int(year)
    except ValueError:
        raise ValueError(f"Invalid year '{year}'! Has to be an integer.")


class Holidata:
    emitter = None
    holidays = None

    def __init__(self, country=None, language=None, year=None):
        year = parse_year(year)
        locale = create_locale_for(country_id=country, lang_id=language)
        self.holidays = locale.get_holidays_of(year)

    def __str__(self):
        return self.emitter.output(self.holidays)

    def formatted_as(self, format_id):
        self.emitter = get_emitter_for(format_id)

        return self
