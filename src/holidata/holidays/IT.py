from dateutil.easter import EASTER_WESTERN

from .holidays import Country


class IT(Country):
    id = "IT"
    languages = ["it"]
    default_lang = "it"
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Capodanno") \
            .on("01-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Epifania") \
            .on("01-06") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Festa della liberazione") \
            .on("04-25") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Festa del lavoro") \
            .on("05-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Festa della repubblica") \
            .on("06-02") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Assunzione (ferragosto)") \
            .on("08-15") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Ognissanti") \
            .on("11-01") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Immacolata concezione") \
            .on("12-08") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Natale") \
            .on("12-25") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("S.to Stefano") \
            .on("12-26") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Pasqua") \
            .on("Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Pasquetta") \
            .on("1 day after Easter") \
            .with_flags("NRV")
