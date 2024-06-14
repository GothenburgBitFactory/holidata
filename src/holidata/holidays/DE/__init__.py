from dateutil.easter import EASTER_WESTERN

from holidata.holidays.DE.BB import BB
from holidata.holidays.DE.BE import BE
from holidata.holidays.DE.BW import BW
from holidata.holidays.DE.BY import BY
from holidata.holidays.DE.HB import HB
from holidata.holidays.DE.HE import HE
from holidata.holidays.DE.HH import HH
from holidata.holidays.DE.MV import MV
from holidata.holidays.DE.NI import NI
from holidata.holidays.DE.NW import NW
from holidata.holidays.DE.RP import RP
from holidata.holidays.DE.SH import SH
from holidata.holidays.DE.SL import SL
from holidata.holidays.DE.SN import SN
from holidata.holidays.DE.ST import ST
from holidata.holidays.DE.TH import TH
from holidata.holidays.holidays import Country

__all__ = [
    "DE",
]


class DE(Country):
    id = "DE"
    languages = ["de"]
    default_lang = "de"
    regions = ["BB", "BE", "BW", "BY", "HB", "HE", "HH", "MV", "NI", "NW", "RP", "SH", "SL", "SN", "ST", "TH"]
    easter_type = EASTER_WESTERN

    """
    https://www.bmi.bund.de/DE/themen/verfassung/staatliche-symbole/nationale-feiertage/nationale-feiertage-node.html
    """
    def __init__(self):
        super().__init__()

        self.regions = [
            BB(self),
            BE(self),
            BW(self),
            BY(self),
            HB(self),
            HE(self),
            HH(self),
            MV(self),
            NI(self),
            NW(self),
            RP(self),
            SH(self),
            SL(self),
            SN(self),
            ST(self),
            TH(self),
        ]

        self.define_holiday() \
            .with_name("Neujahr") \
            .on("01-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Erster Maifeiertag") \
            .on("05-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Tag der Deutschen Einheit") \
            .on("10-03") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Heilig Abend") \
            .on("12-24") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Weihnachtstag") \
            .on("12-25") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Zweiter Weihnachtstag") \
            .on("12-26") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Silvester") \
            .on("12-31") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Karfreitag") \
            .on("2 days before Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Ostern") \
            .on("Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Ostermontag") \
            .on("1 day after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Christi Himmelfahrt") \
            .on("39 days after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Pfingstsonntag") \
            .on("49 days after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Pfingstmontag") \
            .on("50 days after Easter") \
            .with_flags("NRV")

        """
        2017-10-31: Reformationstag (national holiday because of 500th anniversary)
        """
        self.define_holiday() \
            .with_name("Reformationstag") \
            .in_years([2017]) \
            .on("10-31") \
            .with_flags("NRF")
