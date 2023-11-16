from dateutil.easter import EASTER_WESTERN

from .holidays import Country


class CZ(Country):
    id = "CZ"
    languages = ["cs"]
    default_lang = "cs"
    easter_type = EASTER_WESTERN
