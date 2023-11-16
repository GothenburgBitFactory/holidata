from dateutil.easter import EASTER_WESTERN

from .holidays import Country


class FR(Country):
    id = "FR"
    languages = ["fr"]
    default_lang = "fr"
    easter_type = EASTER_WESTERN
