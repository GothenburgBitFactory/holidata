from dateutil.easter import EASTER_WESTERN

from .holidays import Country


class FI(Country):
    id = "FI"
    languages = ["fi", "sv"]
    easter_type = EASTER_WESTERN
