from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import Month, date, day

__all__ = [
    "FR",
]


class FR(Country):
    id = "FR"
    languages = ["fr"]
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Jour de l'an") \
            .on(date(Month.JANUARY, 1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Fête du premier mai") \
            .on(date(Month.MAY, 1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Armistice 1945") \
            .on(date(Month.MAY, 8)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Fête nationale") \
            .on(date(Month.JULY, 14)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Assomption") \
            .on(date(Month.AUGUST, 15)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Toussaint") \
            .on(date(Month.NOVEMBER, 1)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Armistice 1918") \
            .on(date(Month.NOVEMBER, 11)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Noël") \
            .on(date(Month.DECEMBER, 25)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Lundi de Pâques") \
            .on(day(1).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Ascension") \
            .on(day(39).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Pentecôte") \
            .on(day(49).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Lundi de Pentecôte") \
            .on(day(50).after(self.easter())) \
            .with_flags("NRV")
