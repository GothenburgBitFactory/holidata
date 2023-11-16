import re

import pytest

from holidata import Locale, Country, LocaleWrapper
from tests import HOLIDATA_YEAR_MAX


def create_locales():
    response = []

    for country_class in Country.plugins:
        country = country_class()

        if hasattr(country, "get_holidays_of"):
            response.extend([LocaleWrapper(country_class(), lang_id) for lang_id in country.languages])

    for locale_class in Locale.plugins:
        response.append(locale_class())

    return response


locales = create_locales()


@pytest.fixture(params=range(2011, HOLIDATA_YEAR_MAX))
def year(request):
    return request.param


@pytest.fixture(params=locales, ids=[loc.id for loc in locales])
def locale(request):
    return request.param


@pytest.fixture()
def holidays(locale, year):
    return locale.get_holidays_of(year)


@pytest.fixture(params=Country.plugins)
def country(request):
    return request.param()


def test_country_should_be_constructable(country):
    pass


def test_holiday_should_not_be_of_type_national_if_region_defined(holidays):
    for holiday in holidays:
        if holiday.region == "":
            assert "N" in holiday.flags, f"Holiday '{holiday.description}' ({holiday.date.strftime('%Y-%m-%d')}) in locale {holiday.locale} must have flag 'N': it has no regions defined"


def test_holiday_should_be_of_type_national_if_no_region_defined(holidays):
    for holiday in holidays:
        if holiday.region != "":
            assert "N" not in holiday.flags, f"Holiday '{holiday.description}' ({holiday.date.strftime('%Y-%m-%d')}) in locale {holiday.locale} must not have flag 'N': it has regions defined"


def test_holiday_should_be_of_type_either_fixed_or_variable(holidays):
    for holiday in holidays:
        date_is_fixed = "F" in holiday.flags
        date_is_variable = "V" in holiday.flags

        assert not (date_is_variable and date_is_fixed), f"Holiday '{holiday.description}' ({holiday.date.strftime('%Y-%m-%d')}) in locale {holiday.locale} must not have both flags 'F' and 'V'"
        assert (date_is_variable or date_is_fixed), f"Holiday '{holiday.description}' ({holiday.date.strftime('%Y-%m-%d')}) in locale {holiday.locale} must have either flag 'F' or 'V'"


def test_holiday_flags_should_be_in_the_correct_order(holidays):
    for holiday in holidays:
        match = re.search(r"^N?R?[FV]?$", f"{holiday.flags}")

        assert match is not None, f"Flags for holiday '{holiday.description}' ({holiday.date.strftime('%Y-%m-%d')}) in locale {holiday.locale} are not in the correct order. Flags '{holiday.flags}' should match 'N?R?[FV]?'"
