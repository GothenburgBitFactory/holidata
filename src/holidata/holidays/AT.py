from dateutil.easter import EASTER_WESTERN

from .holidays import Country


class AT(Country):
    id = "AT"
    languages = ["de"]
    default_lang = "de"
    regions = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Neujahr") \
            .on("01-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Heilige drei Könige") \
            .on("01-06") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Josef") \
            .in_regions(["2", "6", "7", "8"]) \
            .on("03-19") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Staatsfeiertag") \
            .on("05-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Florian") \
            .in_regions(["4"]) \
            .on("05-04") \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Mariä Himmelfahrt") \
            .on("08-15") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Rupert") \
            .in_regions(["5"]) \
            .on("09-24") \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Tag der Volksabstimmung") \
            .in_regions(["2"]) \
            .on("10-10") \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Nationalfeiertag") \
            .on("10-26") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Allerheiligen") \
            .on("11-01") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Martin") \
            .in_regions(["1"]) \
            .on("11-11") \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Leopold") \
            .in_regions(["9", "3"]) \
            .on("11-15") \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Mariä Empfängnis") \
            .on("12-08") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Heiliger Abend") \
            .on("12-24") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Christtag") \
            .on("12-25") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Stefanitag") \
            .on("12-26") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Silvester") \
            .on("12-31") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Karfreitag") \
            .on("2 days before Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Ostersonntag") \
            .on("Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Ostermontag") \
            .on("1 day after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Christi Himmelfahrt") \
            .on("39 days after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Pfingstsonntag") \
            .on("49 days after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Pfingstmontag") \
            .on("50 days after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Fronleichnam") \
            .on("60 days after Easter") \
            .with_flags("NRV")
