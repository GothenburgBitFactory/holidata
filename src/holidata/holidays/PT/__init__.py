from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import day, date

__all__ = [
    "PT",
]


class PT(Country):
    id = "PT"
    languages = ["pt"]
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Ano Novo") \
            .on(date(month=1, day=1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Dia da Liberdade") \
            .on(date(month=4, day=25)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Dia do Trabalhador") \
            .on(date(month=5, day=1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Dia de Portugal") \
            .on(date(month=6, day=10)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Assunção de Nossa Senhora") \
            .on(date(month=8, day=15)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Implantação da República") \
            .on(date(month=10, day=5)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Dia de Todos os Santos") \
            .on(date(month=11, day=1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Restauração da Independência") \
            .on(date(month=12, day=1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Imaculada Conceição") \
            .on(date(month=12, day=8)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Natal") \
            .on(date(month=12, day=25)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Carnaval") \
            .on(day(47).before(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Sexta-feira Santa") \
            .on(day(2).before(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Páscoa") \
            .on(self.easter()) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Corpo de Deus") \
            .on(day(60).after(self.easter())) \
            .with_flags("NRV")
