from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import day

__all__ = [
    "FR",
]


class FR(Country):
    id = "FR"
    languages = ["fr"]
    default_lang = "fr"
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Jour de l'an") \
            .on(month=1, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Fête du premier mai") \
            .on(month=5, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Armistice 1945") \
            .on(month=5, day=8) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Fête nationale") \
            .on(month=7, day=14) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Assomption") \
            .on(month=8, day=15) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Toussaint") \
            .on(month=11, day=1) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Armistice 1918") \
            .on(month=11, day=11) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Noël") \
            .on(month=12, day=25) \
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
