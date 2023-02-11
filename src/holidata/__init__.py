from .holidays import *
from .emitters import Emitter

def get_country_for(identifier):
    country_class = Country.get(identifier)

    if not country_class:
        raise ValueError("No plugin found for country id '{}'!".format(identifier))

    return country_class()


def get_locale_class_for(identifier):
    locale_class = Locale.get(identifier)

    if not locale_class:
        raise ValueError("No plugin found for locale: {}!".format(identifier))

    return locale_class


def create_locale_for(country_id=None, lang_id=None, year=None):
    country_class = get_country_for(country_id)

    if lang_id is not None and lang_id.lower() not in country_class.languages:
        raise ValueError("Language '{}' is not defined for country '{}'!".format(lang_id, country_class.id))
    elif lang_id is None and country_class.default_lang is not None:
        lang_id = country_class.default_lang
    elif lang_id is None:
        raise ValueError("Country '{}' has no default language specified! Please choose one of [{}].".format(country_id, ", ".join(country_class.languages)))

    locale_class = get_locale_class_for("{}-{}".format(lang_id, country_id))

    return locale_class(year)


def create_emitter_for(identifier):
    emitter_class = Emitter.get(identifier)

    if not emitter_class:
        raise ValueError("Unsupported output format: '{}'!".format(identifier))

    return emitter_class()


def parse_year(year):
    try:
        return int(year)
    except:
        raise ValueError(f"Invalid year '{year}'! Has to be an integer.")


class Holidata:
    locale = None
    emitter = None

    def __init__(self, country=None, language=None, year=None, output=None):
        self.locale = create_locale_for(country_id=country, lang_id=language, year=parse_year(year))
        self.emitter = create_emitter_for(output)

    def __str__(self):
        return self.emitter.output(self.locale)
