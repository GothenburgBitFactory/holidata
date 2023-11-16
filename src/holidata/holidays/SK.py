from dateutil.easter import EASTER_WESTERN

from .holidays import Country


class SK(Country):
    id = "SK"
    languages = ["sk"]
    default_lang = "sk"
    easter_type = EASTER_WESTERN
