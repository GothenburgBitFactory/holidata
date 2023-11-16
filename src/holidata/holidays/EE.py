from dateutil.easter import EASTER_WESTERN

from .holidays import Country


class EE(Country):
    id = "EE"
    languages = ["et"]
    default_lang = "et"
    easter_type = EASTER_WESTERN
