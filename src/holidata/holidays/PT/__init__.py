from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import Month, date, day

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
            .on(date(Month.JANUARY, 1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Dia da Liberdade") \
            .on(date(Month.APRIL, 25)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Dia do Trabalhador") \
            .on(date(Month.MAY, 1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Dia de Portugal") \
            .on(date(Month.JUNE, 10)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Assunção de Nossa Senhora") \
            .on(date(Month.AUGUST, 15)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Implantação da República") \
            .on(date(Month.OCTOBER, 5)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Dia de Todos os Santos") \
            .on(date(Month.NOVEMBER, 1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Restauração da Independência") \
            .on(date(Month.DECEMBER, 1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Imaculada Conceição") \
            .on(date(Month.DECEMBER, 8)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Natal") \
            .on(date(Month.DECEMBER, 25)) \
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
