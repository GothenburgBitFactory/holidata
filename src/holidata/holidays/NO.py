from dateutil.easter import EASTER_WESTERN

from .holidays import Country


class NO(Country):
    id = "NO"
    languages = ["nb"]
    default_lang = "nb"
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Nyttårsdag") \
            .on("01-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Offentlig Høytidsdag") \
            .on("05-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Frigjøringsdag 1945") \
            .on("05-08") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Grunnlovsdag") \
            .on("05-17") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Julaften") \
            .on("12-24") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Juledag") \
            .on("12-25") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Juledag") \
            .on("12-26") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Nyttårsaften") \
            .on("12-31") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Fastelavn") \
            .on("49 days before Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Palmesøndag") \
            .on("7 days before Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Skjærtorsdag") \
            .on("3 days before Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Langfredag") \
            .on("2 days before Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Påskedag") \
            .on("Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Påskedag") \
            .on("1 day after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Kristi Himmelfartsdag") \
            .on("39 days after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Pinsedag") \
            .on("49 days after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Pinsedag") \
            .on("50 days after Easter") \
            .with_flags("NRV")
