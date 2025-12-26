from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import day, date, Month

__all__ = [
    "NO",
]


class NO(Country):
    id = "NO"
    languages = ["nb"]
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Nyttårsdag") \
            .on(date(Month.JANUARY, 1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Offentlig Høytidsdag") \
            .on(date(Month.MAY, 1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Frigjøringsdag 1945") \
            .on(date(Month.MAY, 8)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Grunnlovsdag") \
            .on(date(Month.MAY, 17)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Julaften") \
            .on(date(Month.DECEMBER, 24)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Juledag") \
            .on(date(Month.DECEMBER, 25)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Juledag") \
            .on(date(Month.DECEMBER, 26)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Nyttårsaften") \
            .on(date(Month.DECEMBER, 31)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Fastelavn") \
            .on(day(49).before(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Palmesøndag") \
            .on(day(7).before(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Skjærtorsdag") \
            .on(day(3).before(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Langfredag") \
            .on(day(2).before(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Påskedag") \
            .on(self.easter()) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Påskedag") \
            .on(day(1).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Kristi Himmelfartsdag") \
            .on(day(39).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Pinsedag") \
            .on(day(49).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Pinsedag") \
            .on(day(50).after(self.easter())) \
            .with_flags("NRV")
