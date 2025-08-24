from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import day

__all__ = [
    "PL",
]

"""
source: http://prawo.sejm.gov.pl/isap.nsf/download.xsp/WDU20150000090/O/D20150090.pdf
"""


class PL(Country):
    id = "PL"
    languages = ["pl"]
    default_lang = "pl"
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Nowy Rok") \
            .on(month=1, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Trzech Króli") \
            .on(month=1, day=6) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Święto Pracy") \
            .on(month=5, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Święto Konstytucji Trzeciego Maja") \
            .on(month=5, day=3) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Wniebowzięcie Najświętszej Maryi Panny") \
            .on(month=8, day=15) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Wszystkich Świętych") \
            .on(month=11, day=1) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Narodowe Święto Niepodległości") \
            .on(month=11, day=11) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Boże Narodzenie (pierwszy dzień)") \
            .on(month=12, day=25) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Boże Narodzenie (drugi dzień)") \
            .on(month=12, day=26) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Wielkanoc") \
            .on(self.easter()) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Poniedziałek Wielkanocny") \
            .on(day(1).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Zielone Świątki") \
            .on(day(49).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Boże Ciało") \
            .on(day(60).after(self.easter())) \
            .with_flags("NRV")
