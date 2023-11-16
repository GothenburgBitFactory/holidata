from dateutil.easter import EASTER_WESTERN

from .holidays import Country


class DK(Country):
    id = "DK"
    languages = ["da"]
    default_lang = "da"
    easter_type = EASTER_WESTERN
