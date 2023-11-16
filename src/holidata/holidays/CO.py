from dateutil.easter import EASTER_WESTERN

from .holidays import Country


class CO(Country):
    id = "CO"
    languages = ["es"]
    default_lang = "es"
    easter_type = EASTER_WESTERN
