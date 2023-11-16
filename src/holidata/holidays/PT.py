from dateutil.easter import EASTER_WESTERN

from .holidays import Country


class PT(Country):
    id = "PT"
    languages = ["pt"]
    default_lang = "pt"
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Ano Novo") \
            .on("01-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Dia da Liberdade") \
            .on("04-25") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Dia do Trabalhador") \
            .on("05-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Dia de Portugal") \
            .on("06-10") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Assunção de Nossa Senhora") \
            .on("08-15") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Implantação da República") \
            .on("10-05") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Dia de Todos os Santos") \
            .on("11-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Restauração da Independência") \
            .on("12-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Imaculada Conceição") \
            .on("12-08") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Natal") \
            .on("12-25") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Carnaval") \
            .on("47 days before Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Sexta-feira Santa") \
            .on("2 days before Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Páscoa") \
            .on("Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Corpo de Deus") \
            .on("60 days after Easter") \
            .with_flags("NRV")
