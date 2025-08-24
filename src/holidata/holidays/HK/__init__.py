from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country

__all__ = [
    "HK",
]


class HK(Country):
    id = "HK"
    languages = ["en", "zh"]
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()
