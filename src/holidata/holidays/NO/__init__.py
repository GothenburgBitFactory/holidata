from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import day

__all__ = [
    "NO",
]


class NO(Country):
    id = "NO"
    languages = ["nb"]
    default_lang = "nb"
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Nyttårsdag") \
            .on(month=1, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Offentlig Høytidsdag") \
            .on(month=5, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Frigjøringsdag 1945") \
            .on(month=5, day=8) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Grunnlovsdag") \
            .on(month=5, day=17) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Julaften") \
            .on(month=12, day=24) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Juledag") \
            .on(month=12, day=25) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Juledag") \
            .on(month=12, day=26) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Nyttårsaften") \
            .on(month=12, day=31) \
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
