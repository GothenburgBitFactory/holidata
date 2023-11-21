from dateutil.easter import EASTER_WESTERN

from .holidays import Country


class SK(Country):
    id = "SK"
    languages = ["sk"]
    default_lang = "sk"
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Deň vzniku Slovenskej republiky") \
            .on("01-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Zjavenie Pána / Traja králi") \
            .on("01-06") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Sviatok práce") \
            .on("05-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Deň víťazstva nad fašizmom") \
            .on("05-08") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Sviatok svätého Cyrila a Metoda") \
            .on("07-05") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Výročie SNP") \
            .on("08-29") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Deň Ústavy Slovenskej republiky") \
            .on("09-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Sedembolestná Panna Mária") \
            .on("09-15") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Sviatok všetkých svätých") \
            .on("11-01") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Deň boja za slobodu a demokraciu") \
            .on("11-17") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Štedrý deň") \
            .on("12-24") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Prvý sviatok vianočný") \
            .on("12-25") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Druhý sviatok vianočný") \
            .on("12-26") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Veľký piatok") \
            .on("2 days before Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Veľkonočný pondelok") \
            .on("1 day after Easter") \
            .with_flags("NRV")
