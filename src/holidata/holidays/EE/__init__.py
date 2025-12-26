from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import day, date, Month

__all__ = [
    "EE",
]

"""
sources
https://www.riigiteataja.ee/akt/109032011007 (Public Holidays and Days of National Importance Act)
"""


class EE(Country):
    id = "EE"
    languages = ["et"]
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Uusaasta") \
            .on(date(Month.JANUARY, 1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Iseseisvuspäev, Eesti Vabariigi aastapäev") \
            .on(date(Month.FEBRUARY, 24)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Kevadpüha") \
            .on(date(Month.MAY, 1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Võidupüha") \
            .on(date(Month.JUNE, 23)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Jaanipäev") \
            .on(date(Month.JUNE, 24)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Taasiseseisvumispäev") \
            .on(date(Month.AUGUST, 20)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Jõululaupäev") \
            .on(date(Month.DECEMBER, 24)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Esimene jõulupüha") \
            .on(date(Month.DECEMBER, 25)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Teine jõulupüha") \
            .on(date(Month.DECEMBER, 26)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Suur reede") \
            .on(day(2).before(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Ülestõusmispühade 1. püha") \
            .on(self.easter()) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Nelipühade 1. püha") \
            .on(day(49).after(self.easter())) \
            .with_flags("NRV")
