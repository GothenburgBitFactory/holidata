from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import day, date, Month

__all__ = [
    "AT",
]


class AT(Country):
    id = "AT"
    languages = ["de"]
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Neujahr") \
            .on(date(Month.JANUARY, 1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Heilige drei Könige") \
            .on(date(Month.JANUARY, 6)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Josef") \
            .in_regions(["2", "6", "7", "8"]) \
            .on(date(Month.MARCH, 19)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Staatsfeiertag") \
            .on(date(Month.MAY, 1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Florian") \
            .in_regions(["4"]) \
            .on(date(Month.MAY, 4)) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Mariä Himmelfahrt") \
            .on(date(Month.AUGUST, 15)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Rupert") \
            .in_regions(["5"]) \
            .on(date(Month.SEPTEMBER, 24)) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Tag der Volksabstimmung") \
            .in_regions(["2"]) \
            .on(date(Month.OCTOBER, 10)) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Nationalfeiertag") \
            .on(date(Month.OCTOBER, 26)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Allerheiligen") \
            .on(date(Month.NOVEMBER, 1)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Martin") \
            .in_regions(["1"]) \
            .on(date(Month.NOVEMBER, 11)) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Leopold") \
            .in_regions(["9", "3"]) \
            .on(date(Month.NOVEMBER, 15)) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Mariä Empfängnis") \
            .on(date(Month.DECEMBER, 8)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Heiliger Abend") \
            .on(date(Month.DECEMBER, 24)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Christtag") \
            .on(date(Month.DECEMBER, 25)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Stefanitag") \
            .on(date(Month.DECEMBER, 26)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Silvester") \
            .on(date(Month.DECEMBER, 31)) \
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
