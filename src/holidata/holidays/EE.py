from dateutil.easter import EASTER_WESTERN

from .holidays import Country

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
            .on("01-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Iseseisvuspäev, Eesti Vabariigi aastapäev") \
            .on("02-24") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Kevadpüha") \
            .on("05-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Võidupüha") \
            .on("06-23") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Jaanipäev") \
            .on("06-24") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Taasiseseisvumispäev") \
            .on("08-20") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Jõululaupäev") \
            .on("12-24") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Esimene jõulupüha") \
            .on("12-25") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Teine jõulupüha") \
            .on("12-26") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Suur reede") \
            .on("2 days before Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Ülestõusmispühade 1. püha") \
            .on("Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Nelipühade 1. püha") \
            .on("49 days after Easter") \
            .with_flags("NRV")
