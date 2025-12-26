from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import day, date, Month

__all__ = [
    "PL",
]

"""
source: https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU20150000090/O/D20150090.pdf
source2: https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU20240001965/T/D20241965L.pdf
"""


class PL(Country):
    id = "PL"
    languages = ["pl"]
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Nowy Rok") \
            .on(date(Month.JANUARY, 1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Trzech Króli") \
            .on(date(Month.JANUARY, 6)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Święto Pracy") \
            .on(date(Month.MAY, 1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Święto Konstytucji Trzeciego Maja") \
            .on(date(Month.MAY, 3)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Wniebowzięcie Najświętszej Maryi Panny") \
            .on(date(Month.AUGUST, 15)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Wszystkich Świętych") \
            .on(date(Month.NOVEMBER, 1)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Narodowe Święto Niepodległości") \
            .on(date(Month.NOVEMBER, 11)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Wigilia") \
            .since(2025) \
            .on(date(Month.DECEMBER, 24)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Boże Narodzenie (pierwszy dzień)") \
            .on(date(Month.DECEMBER, 25)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Boże Narodzenie (drugi dzień)") \
            .on(date(Month.DECEMBER, 26)) \
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
