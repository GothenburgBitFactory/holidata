from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import day, first, date, Weekday, Month

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
            .on(date(Month.JANUARY, 1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Trettondedag jul") \
            .on(date(Month.JANUARY, 6)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Första maj") \
            .on(date(Month.MAY, 1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Nationaldagen") \
            .on(date(Month.JUNE, 6)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Julafton") \
            .on(date(Month.DECEMBER, 24)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Juldagen") \
            .on(date(Month.DECEMBER, 25)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Annandag jul") \
            .on(date(Month.DECEMBER, 26)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Nyårsafton") \
            .on(date(Month.DECEMBER, 31)) \
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
            .on(day(1).before(first(Weekday.SATURDAY).after(date(Month.JUNE, 19)))) \
            .with_flags("NV")

        self.define_holiday() \
            .with_name("Midsommardagen") \
            .on(first(Weekday.SATURDAY).after(date(Month.JUNE, 19))) \
            .with_flags("NV")

        self.define_holiday() \
            .with_name("Alla helgons dag") \
            .on(first(Weekday.SATURDAY).after(date(Month.OCTOBER, 30))) \
            .with_flags("NRV")
