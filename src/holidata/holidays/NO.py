from dateutil.easter import EASTER_WESTERN

from .holidays import Country


class NO(Country):
    id = "NO"
    languages = "nb"
    default_lang = "nb"
    easter_type = EASTER_WESTERN
