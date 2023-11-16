from dateutil.easter import EASTER_ORTHODOX

from .holidays import Country


class GR(Country):
    id = "GR"
    languages = ["el"]
    default_lang = "el"
    easter_type = EASTER_ORTHODOX
