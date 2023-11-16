from dateutil.easter import EASTER_WESTERN

from .holidays import Country


class PL(Country):
    id = "PL"
    languages = ["pl"]
    default_lang = "pl"
    easter_type = EASTER_WESTERN
