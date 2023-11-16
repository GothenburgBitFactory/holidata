from dateutil.easter import EASTER_WESTERN

from .holidays import Country


class SE(Country):
    id = "SE"
    languages = ["sv"]
    default_lang = "sv"
    easter_type = EASTER_WESTERN
