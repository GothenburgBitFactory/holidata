from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import day, first, date

__all__ = [
    "SE",
]


class SE(Country):
    id = "SE"
    languages = ["sv"]
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Nyårsdagen") \
            .on(date(month=1, day=1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Trettondedag jul") \
            .on(date(month=1, day=6)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Första maj") \
            .on(date(month=5, day=1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Nationaldagen") \
            .on(date(month=6, day=6)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Julafton") \
            .on(date(month=12, day=24)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Juldagen") \
            .on(date(month=12, day=25)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Annandag jul") \
            .on(date(month=12, day=26)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Nyårsafton") \
            .on(date(month=12, day=31)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Långfredagen") \
            .on(day(2).before(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Påskdagen") \
            .on(self.easter()) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Annandag påsk") \
            .on(day(1).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Kristi himmelsfärdsdag") \
            .on(day(39).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Pingstdagen") \
            .on(day(49).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Midsommarafton") \
            .on(day(1).before(first("saturday").after(date(month=6, day=19)))) \
            .with_flags("NV")

        self.define_holiday() \
            .with_name("Midsommardagen") \
            .on(first("saturday").after(date(month=6, day=19))) \
            .with_flags("NV")

        self.define_holiday() \
            .with_name("Alla helgons dag") \
            .on(first("saturday").after(date(month=10, day=30))) \
            .with_flags("NRV")
