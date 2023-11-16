from dateutil.easter import EASTER_WESTERN

from .holidays import Country


class CH(Country):
    id = "CH"
    languages = ["de"]
    default_lang = "de"
    regions = ["AG", "AI", "AR", "BE", "BL", "BS", "FR", "GE", "GL", "GR", "JU", "LU", "NE", "NW", "OW", "SG", "SH",
               "SO", "SZ", "TI", "TG", "UR", "VD", "VS", "ZG", "ZH"]
    easter_type = EASTER_WESTERN
