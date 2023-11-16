from dateutil.easter import EASTER_WESTERN

from .holidays import Country


class CA(Country):
    id = "CA"
    languages = ["en", "fr"]
    regions = ["AB", "BC", "MB", "NB", "NL", "NS", "ON", "PE", "QC", "SK", "NT", "NU", "YT"]
    easter_type = EASTER_WESTERN
