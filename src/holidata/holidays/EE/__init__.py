from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import day, date

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
    default_lang = "et"
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Uusaasta") \
            .on(date(month=1, day=1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Iseseisvuspäev, Eesti Vabariigi aastapäev") \
            .on(date(month=2, day=24)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Kevadpüha") \
            .on(date(month=5, day=1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Võidupüha") \
            .on(date(month=6, day=23)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Jaanipäev") \
            .on(date(month=6, day=24)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Taasiseseisvumispäev") \
            .on(date(month=8, day=20)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Jõululaupäev") \
            .on(date(month=12, day=24)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Esimene jõulupüha") \
            .on(date(month=12, day=25)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Teine jõulupüha") \
            .on(date(month=12, day=26)) \
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
