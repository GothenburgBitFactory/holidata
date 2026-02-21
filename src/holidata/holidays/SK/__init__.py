from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import Month, date, day

__all__ = [
    "SK",
]


class SK(Country):
    id = "SK"
    languages = ["sk"]
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Deň vzniku Slovenskej republiky") \
            .on(date(Month.JANUARY, 1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Zjavenie Pána / Traja králi") \
            .on(date(Month.JANUARY, 6)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Sviatok práce") \
            .on(date(Month.MAY, 1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Deň víťazstva nad fašizmom") \
            .on(date(Month.MAY, 8)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Sviatok svätého Cyrila a Metoda") \
            .on(date(Month.JULY, 5)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Výročie SNP") \
            .on(date(Month.AUGUST, 29)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Deň Ústavy Slovenskej republiky") \
            .on(date(Month.SEPTEMBER, 1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Sedembolestná Panna Mária") \
            .on(date(Month.SEPTEMBER, 15)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Sviatok všetkých svätých") \
            .on(date(Month.NOVEMBER, 1)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Deň boja za slobodu a demokraciu") \
            .on(date(Month.NOVEMBER, 17)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Štedrý deň") \
            .on(date(Month.DECEMBER, 24)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Prvý sviatok vianočný") \
            .on(date(Month.DECEMBER, 25)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Druhý sviatok vianočný") \
            .on(date(Month.DECEMBER, 26)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Veľký piatok") \
            .on(day(2).before(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Veľkonočný pondelok") \
            .on(day(1).after(self.easter())) \
            .with_flags("NRV")
