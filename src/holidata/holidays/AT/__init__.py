from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import day

__all__ = [
    "AT",
]


class AT(Country):
    id = "AT"
    languages = ["de"]
    default_lang = "de"
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Neujahr") \
            .on(month=1, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Heilige drei Könige") \
            .on(month=1, day=6) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Josef") \
            .in_regions(["2", "6", "7", "8"]) \
            .on(month=3, day=19) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Staatsfeiertag") \
            .on(month=5, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Florian") \
            .in_regions(["4"]) \
            .on(month=5, day=4) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Mariä Himmelfahrt") \
            .on(month=8, day=15) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Rupert") \
            .in_regions(["5"]) \
            .on(month=9, day=24) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Tag der Volksabstimmung") \
            .in_regions(["2"]) \
            .on(month=10, day=10) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Nationalfeiertag") \
            .on(month=10, day=26) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Allerheiligen") \
            .on(month=11, day=1) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Martin") \
            .in_regions(["1"]) \
            .on(month=11, day=11) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Leopold") \
            .in_regions(["9", "3"]) \
            .on(month=11, day=15) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Mariä Empfängnis") \
            .on(month=12, day=8) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Heiliger Abend") \
            .on(month=12, day=24) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Christtag") \
            .on(month=12, day=25) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Stefanitag") \
            .on(month=12, day=26) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Silvester") \
            .on(month=12, day=31) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Karfreitag") \
            .on(day(2).before(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Ostersonntag") \
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

        self.define_holiday() \
            .with_name("Fronleichnam") \
            .on(day(60).after(self.easter())) \
            .with_flags("NRV")
