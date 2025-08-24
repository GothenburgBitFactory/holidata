from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import day

__all__ = [
    "DK",
]


class DK(Country):
    id = "DK"
    languages = ["da"]
    default_lang = "da"
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Nytårsdag") \
            .on(month=1, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Grundlovsdag") \
            .on(month=6, day=5) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Juledag") \
            .on(month=12, day=25) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Anden juledag") \
            .on(month=12, day=26) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Skærtorsdag") \
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
            .with_name("Anden påskedag") \
            .on(day(1).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Store bededag") \
            .on(day(26).after(self.easter())) \
            .until(2023) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Kristi himmelfartsdag") \
            .on(day(39).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Pinsedag") \
            .on(day(49).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Anden pinsedag") \
            .on(day(50).after(self.easter())) \
            .with_flags("NRV")
