from dateutil.easter import EASTER_WESTERN

from .holidays import Country


class BE(Country):
    id = "BE"
    languages = ["de", "fr", "nl"]
    easter_type = EASTER_WESTERN
