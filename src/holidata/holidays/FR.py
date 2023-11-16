from dateutil.easter import EASTER_WESTERN

from .holidays import Country


class FR(Country):
    id = "FR"
    languages = ["fr"]
    default_lang = "fr"
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Jour de l'an") \
            .on("01-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Fête du premier mai") \
            .on("05-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Armistice 1945") \
            .on("05-08") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Fête nationale") \
            .on("07-14") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Assomption") \
            .on("08-15") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Toussaint") \
            .on("11-01") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Armistice 1918") \
            .on("11-11") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Noël") \
            .on("12-25") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Lundi de Pâques") \
            .on("1 day after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Ascension") \
            .on("39 days after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Pentecôte") \
            .on("49 days after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Lundi de Pentecôte") \
            .on("50 days after Easter") \
            .with_flags("NRV")
