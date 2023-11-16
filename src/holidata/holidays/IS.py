from dateutil.easter import EASTER_WESTERN

from .holidays import Country


class IS(Country):
    id = "IS"
    languages = ["is"]
    default_lang = "is"
    easter_type = EASTER_WESTERN
