import pytest
from snapshottest.file import FileSnapshot
from snapshottest.formatter import Formatter

from holidata import Locale, Country, LocaleWrapper
from tests import HOLIDATA_YEAR_MAX

SNAPSHOT_FILE_PATH_PATTERN = "snapshots/snap_test_holidata/{}[{}-{}] 1.py"


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


def test_holidata_produces_holidays_for_locale_and_year(snapshot, tmpdir, locale, year):
    temp_file = tmpdir.join(f"{locale.id}.{year}.py")

    export_data = [h.as_dict() for h in locale.get_holidays_of(year)]
    export_data.sort(key=lambda x: x["date"])
    temp_file.write(Formatter().format(export_data, 0))

    try:
        snapshot.assert_match(FileSnapshot(str(temp_file)))
    except AssertionError:
        with open(temp_file, "r") as tf:
            actual = "".join(tf.readlines())

        snapshot_file = SNAPSHOT_FILE_PATH_PATTERN.format(
            "test_holidata_produces_holidays_for_locale_and_year",
            locale.id,
            year)

        with open(snapshot_file) as sf:
            expected = "".join(sf.readlines())

        assert (actual == expected)
