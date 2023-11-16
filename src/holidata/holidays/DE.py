from dateutil.easter import EASTER_WESTERN

from .holidays import Country


class DE(Country):
    id = "DE"
    languages = ["de"]
    default_lang = "de"
    regions = ["BB", "BE", "BH", "BW", "BY", "HE", "HH", "MV", "NI", "NW", "RP", "SH", "SL", "SN", "ST", "TH"]
    easter_type = EASTER_WESTERN
