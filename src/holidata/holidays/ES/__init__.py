from dateutil.easter import EASTER_WESTERN

from holidata.holidays.holidays import Country

__all__ = [
    "ES",
    "es-ES",
]


class ES(Country):
    id = "ES"
    languages = ["es"]
    default_lang = "es"
    easter_type = EASTER_WESTERN
