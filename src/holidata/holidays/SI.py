from dateutil.easter import EASTER_WESTERN

from .holidays import Country


class SI(Country):
    id = "SI"
    languages = ["sl"]
    default_lang = "sl"
    easter_type = EASTER_WESTERN
