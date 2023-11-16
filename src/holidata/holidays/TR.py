from dateutil.easter import EASTER_WESTERN

from .holidays import Country


class TR(Country):
    id = "TR"
    languages = ["tr"]
    default_lang = "tr"
    easter_type = EASTER_WESTERN
