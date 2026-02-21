from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import Month, date, day

__all__ = [
    "DK",
]


class DK(Country):
    id = "DK"
    languages = ["da"]
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Nytårsdag") \
            .on(date(Month.JANUARY, 1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Grundlovsdag") \
            .on(date(Month.JUNE, 5)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Juledag") \
            .on(date(Month.DECEMBER, 25)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Anden juledag") \
            .on(date(Month.DECEMBER, 26)) \
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
