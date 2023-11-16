from dateutil.easter import EASTER_WESTERN

from .holidays import Country


class HU(Country):
    id = "HU"
    languages = ["hu"]
    default_lang = "hu"
    easter_type = EASTER_WESTERN
