from dateutil.easter import EASTER_WESTERN

from .holidays import Country


class HR(Country):
    id = "HR"
    languages = ["hr"]
    default_lang = "hr"
    easter_type = EASTER_WESTERN
