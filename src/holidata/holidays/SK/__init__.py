from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import day

__all__ = [
    "SK",
]


class SK(Country):
    id = "SK"
    languages = ["sk"]
    default_lang = "sk"
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Deň vzniku Slovenskej republiky") \
            .on(month=1, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Zjavenie Pána / Traja králi") \
            .on(month=1, day=6) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Sviatok práce") \
            .on(month=5, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Deň víťazstva nad fašizmom") \
            .on(month=5, day=8) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Sviatok svätého Cyrila a Metoda") \
            .on(month=7, day=5) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Výročie SNP") \
            .on(month=8, day=29) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Deň Ústavy Slovenskej republiky") \
            .on(month=9, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Sedembolestná Panna Mária") \
            .on(month=9, day=15) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Sviatok všetkých svätých") \
            .on(month=11, day=1) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Deň boja za slobodu a demokraciu") \
            .on(month=11, day=17) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Štedrý deň") \
            .on(month=12, day=24) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Prvý sviatok vianočný") \
            .on(month=12, day=25) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Druhý sviatok vianočný") \
            .on(month=12, day=26) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Veľký piatok") \
            .on(day(2).before(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Veľkonočný pondelok") \
            .on(day(1).after(self.easter())) \
            .with_flags("NRV")
