from dateutil.easter import EASTER_WESTERN

from .holidays import Country


class GB(Country):
    id = "GB"
    languages = ["en"]
    default_lang = "en"
    easter_type = EASTER_WESTERN
