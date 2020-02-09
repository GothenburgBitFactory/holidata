from datetime import datetime

from snapshottest.file import FileSnapshot

from holidata import Locale
import pytest


@pytest.fixture(params=range(2011, datetime.now().year + 1))
def year(request):
    return request.param


@pytest.fixture(params=Locale.plugins)
def locale(request, year):
    return request.param(year)


def test_holidata_produces_holidays_for_locale_and_year(snapshot, tmpdir, locale):
    temp_file = tmpdir.join('{}.{}.py'.format(locale.locale, locale.year))

    export_data = [h.as_dict() for h in locale.holidays]
    export_data.sort(key=lambda x: x['date'])
    temp_file.write(export_data)

    snapshot.assert_match(FileSnapshot(str(temp_file)))
