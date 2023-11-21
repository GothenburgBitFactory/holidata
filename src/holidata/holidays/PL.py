from dateutil.easter import EASTER_WESTERN

from .holidays import Country

"""
source: http://prawo.sejm.gov.pl/isap.nsf/download.xsp/WDU20150000090/O/D20150090.pdf
"""


class PL(Country):
    id = "PL"
    languages = ["pl"]
    default_lang = "pl"
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Nowy Rok") \
            .on("01-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Trzech Króli") \
            .on("01-06") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Święto Pracy") \
            .on("05-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Święto Konstytucji Trzeciego Maja") \
            .on("05-03") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Wniebowzięcie Najświętszej Maryi Panny") \
            .on("08-15") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Wszystkich Świętych") \
            .on("11-01") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Narodowe Święto Niepodległości") \
            .on("11-11") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Boże Narodzenie (pierwszy dzień)") \
            .on("12-25") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Boże Narodzenie (drugi dzień)") \
            .on("12-26") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Wielkanoc") \
            .on("Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Poniedziałek Wielkanocny") \
            .on("1 day after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Zielone Świątki") \
            .on("49 days after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Boże Ciało") \
            .on("60 days after Easter") \
            .with_flags("NRV")
