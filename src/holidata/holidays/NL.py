from dateutil.easter import EASTER_WESTERN

from .holidays import Country


class NL(Country):
    id = "NL"
    languages = ["nl"]
    default_lang = "nl"
    easter_type = EASTER_WESTERN
