from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
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
from holidata.utils import day

__all__ = [
    "DE",
]


class DE(Country):
    id = "DE"
    languages = ["de"]
    default_lang = "de"
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
            .on(month=1, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Erster Maifeiertag") \
            .on(month=5, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Tag der Deutschen Einheit") \
            .on(month=10, day=3) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Heilig Abend") \
            .on(month=12, day=24) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Weihnachtstag") \
            .on(month=12, day=25) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Zweiter Weihnachtstag") \
            .on(month=12, day=26) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Silvester") \
            .on(month=12, day=31) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Karfreitag") \
            .on(day(2).before(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Ostern") \
            .on(self.easter()) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Ostermontag") \
            .on(day(1).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Christi Himmelfahrt") \
            .on(day(39).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Pfingstsonntag") \
            .on(day(49).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Pfingstmontag") \
            .on(day(50).after(self.easter())) \
            .with_flags("NRV")

        """
        2017-10-31: Reformationstag (national holiday because of 500th anniversary)
        """
        self.define_holiday() \
            .with_name("Reformationstag") \
            .in_years([2017]) \
            .on(month=10, day=31) \
            .with_flags("NRF")
