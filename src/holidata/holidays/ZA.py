from dateutil.easter import EASTER_WESTERN

from .holidays import Country


class ZA(Country):
    id = "ZA"
    languages = ["en"]
    easter_type = EASTER_WESTERN
