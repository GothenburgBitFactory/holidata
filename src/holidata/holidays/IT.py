from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import day


class IT(Country):
    id = "IT"
    languages = ["it"]
    default_lang = "it"
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Capodanno") \
            .on(month=1, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Epifania") \
            .on(month=1, day=6) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Festa della liberazione") \
            .on(month=4, day=25) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Festa del lavoro") \
            .on(month=5, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Festa della repubblica") \
            .on(month=6, day=2) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Assunzione (ferragosto)") \
            .on(month=8, day=15) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Ognissanti") \
            .on(month=11, day=1) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Immacolata concezione") \
            .on(month=12, day=8) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Natale") \
            .on(month=12, day=25) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("S.to Stefano") \
            .on(month=12, day=26) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Pasqua") \
            .on(self.easter()) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Pasquetta") \
            .on(day(1).after(self.easter())) \
            .with_flags("NRV")
