from dateutil.easter import EASTER_WESTERN

from .holidays import Country


class PT(Country):
    id = "PT"
    languages = ["pt"]
    default_lang = "pt"
    easter_type = EASTER_WESTERN
