import pytest
from syrupy import snapshot
from syrupy.extensions.json import JSONSnapshotExtension

from holidata import Locale, Country
from tests import HOLIDATA_YEAR_MAX


def create_locales():
    response = []

    for country_class in Country.plugins:
        response.extend([Locale(country_class(), lang_id) for lang_id in country_class.languages])

    return response


locales = create_locales()


@pytest.fixture
def snapshot_json(snapshot):
    return snapshot.with_defaults(extension_class=JSONSnapshotExtension)


@pytest.fixture(params=range(2011, HOLIDATA_YEAR_MAX))
def year(request):
    return request.param


@pytest.fixture(params=locales, ids=[loc.id for loc in locales])
def locale(request):
    return request.param


def test_holidata_produces_holidays_for_locale_and_year(snapshot_json, locale, year):
    export_data = [h.as_dict() for h in locale.get_holidays_of(year)]
    export_data.sort(key=lambda x: (x["date"], x["description"], x["region"]))

    assert export_data == snapshot_json


def test_holidata_can_produce_holidays_out_of_range(locale):
    [h.as_dict() for h in locale.get_holidays_of(HOLIDATA_YEAR_MAX)]
