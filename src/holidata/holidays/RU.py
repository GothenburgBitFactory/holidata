from dateutil.easter import EASTER_ORTHODOX

from .holidays import Country


class RU(Country):
    id = "RU"
    languages = ["ru"]
    default_lang = "ru"
    easter_type = EASTER_ORTHODOX
