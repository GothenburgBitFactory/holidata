from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.holidays.AU.ACT import ACT
from holidata.holidays.AU.NSW import NSW
from holidata.holidays.AU.NT import NT
from holidata.holidays.AU.QLD import QLD
from holidata.holidays.AU.SA import SA
from holidata.holidays.AU.TAS import TAS
from holidata.holidays.AU.VIC import VIC
from holidata.holidays.AU.WA import WA

__all__ = [
    "AU"
]


class AU(Country):
    id = "AU"
    languages = ["en"]
    default_lang = "en"
    regions = ["ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"]
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.regions = [
            ACT(self),
            NSW(self),
            NT(self),
            QLD(self),
            SA(self),
            TAS(self),
            VIC(self),
            WA(self),
        ]
