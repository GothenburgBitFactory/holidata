import json
import pytest

from holidata.emitters import JsonEmitter
from holidata.holidays import Locale

def test_JsonEmitter_produces_valid_json_for_every_locale():
    for locale in Locale.plugins:
        output = JsonEmitter().output(locale(year=2020))
        assert json.loads(output)

