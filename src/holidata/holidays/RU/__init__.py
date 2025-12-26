from dateutil.easter import EASTER_ORTHODOX

from holidata.holiday import Country
from holidata.utils import date, Month

__all__ = [
    "RU",
]


class RU(Country):
    id = "RU"
    languages = ["ru"]
    easter_type = EASTER_ORTHODOX

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Новый Год") \
            .on(date(Month.JANUARY, 1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Рождество Христово") \
            .on(date(Month.JANUARY, 7)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("День защитника Отечества") \
            .on(date(Month.FEBRUARY, 23)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Международный женский день") \
            .on(date(Month.MARCH, 8)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Праздник весны и труда") \
            .on(date(Month.MAY, 1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("День Победы") \
            .on(date(Month.MAY, 9)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("День России") \
            .on(date(Month.JUNE, 12)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("День народного единства") \
            .on(date(Month.NOVEMBER, 4)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Пасха") \
            .on(self.easter()) \
            .with_flags("NRV")
