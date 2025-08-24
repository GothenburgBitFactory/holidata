from dateutil.easter import EASTER_ORTHODOX

from holidata.holiday import Country

__all__ = [
    "RU",
]


class RU(Country):
    id = "RU"
    languages = ["ru"]
    default_lang = "ru"
    easter_type = EASTER_ORTHODOX

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Новый Год") \
            .on(month=1, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Рождество Христово") \
            .on(month=1, day=7) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("День защитника Отечества") \
            .on(month=2, day=23) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Международный женский день") \
            .on(month=3, day=8) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Праздник весны и труда") \
            .on(month=5, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("День Победы") \
            .on(month=5, day=9) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("День России") \
            .on(month=6, day=12) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("День народного единства") \
            .on(month=11, day=4) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Пасха") \
            .on(self.easter()) \
            .with_flags("NRV")
