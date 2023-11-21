from dateutil.easter import EASTER_WESTERN

from .holidays import Country


class DK(Country):
    id = "DK"
    languages = ["da"]
    default_lang = "da"
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Nytårsdag") \
            .on("01-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Grundlovsdag") \
            .on("06-05") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Juledag") \
            .on("12-25") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Anden juledag") \
            .on("12-26") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Skærtorsdag") \
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
            .with_name("Anden påskedag") \
            .on("1 day after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Store bededag") \
            .on("26 days after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Kristi himmelfartsdag") \
            .on("39 days after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Pinsedag") \
            .on("49 days after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Anden pinsedag") \
            .on("50 days after Easter") \
            .with_flags("NRV")
