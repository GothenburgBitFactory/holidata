from dateutil.easter import EASTER_ORTHODOX

from .holidays import Country


class RU(Country):
    id = "RU"
    languages = ["ru"]
    default_lang = "ru"
    easter_type = EASTER_ORTHODOX

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Новый Год") \
            .on("01-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Рождество Христово") \
            .on("01-07") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("День защитника Отечества") \
            .on("02-23") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Международный женский день") \
            .on("03-08") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Праздник весны и труда") \
            .on("05-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("День Победы") \
            .on("05-09") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("День России") \
            .on("06-12") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("День народного единства") \
            .on("11-04") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Пасха") \
            .on("Easter") \
            .with_flags("NRV")
