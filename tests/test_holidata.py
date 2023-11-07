import pytest
from snapshottest.file import FileSnapshot
from snapshottest.formatter import Formatter

from holidata import Locale
from tests import HOLIDATA_YEAR_MAX

SNAPSHOT_FILE_PATH_PATTERN = "snapshots/snap_test_holidata/{}[{}-{}] 1.py"


@pytest.fixture(params=range(2011, HOLIDATA_YEAR_MAX))
def year(request):
    return request.param


@pytest.fixture(params=Locale.plugins)
def locale(request, year):
    return request.param(year)


def test_holidata_produces_holidays_for_locale_and_year(snapshot, tmpdir, locale):
    temp_file = tmpdir.join(f"{locale.locale}.{locale.year}.py")

    export_data = [h.as_dict() for h in locale.holidays]
    export_data.sort(key=lambda x: x["date"])
    temp_file.write(Formatter().format(export_data, 0))

    try:
        snapshot.assert_match(FileSnapshot(str(temp_file)))
    except AssertionError:
        with open(temp_file, "r") as tf:
            actual = "".join(tf.readlines())

        snapshot_file = SNAPSHOT_FILE_PATH_PATTERN.format(
            "test_holidata_produces_holidays_for_locale_and_year",
            locale.__class__.__name__,
            locale.year)

        with open(snapshot_file) as sf:
            expected = "".join(sf.readlines())

        assert (actual == expected)
