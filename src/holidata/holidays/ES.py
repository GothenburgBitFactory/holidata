from dateutil.easter import EASTER_WESTERN

from .holidays import Country


class ES(Country):
    id = "ES"
    languages = ["es"]
    default_lang = "es"
    easter_type = EASTER_WESTERN
