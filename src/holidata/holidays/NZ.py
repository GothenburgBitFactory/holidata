from dateutil.easter import EASTER_WESTERN

from .holidays import Country


class NZ(Country):
    id = "NZ"
    languages = ["en"]
    default_lang = "en"
    easter_type = EASTER_WESTERN
