from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import day, first

__all__ = [
    "IS",
]


class IS(Country):
    id = "IS"
    languages = ["is"]
    default_lang = "is"
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Nýársdagur") \
            .on(month=1, day=1) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Verkalýðsdagurinn") \
            .on(month=5, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Þjóðhátíðardagurinn") \
            .on(month=6, day=17) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Jóladagur") \
            .on(month=12, day=25) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Annar dagur jóla") \
            .on(month=12, day=26) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Skírdagur") \
            .on(day(3).before(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Föstudagurinn langi") \
            .on(day(2).before(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Páskadagur") \
            .on(self.easter()) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Annar dagur páska") \
            .on(day(1).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Uppstigningardagur") \
            .on(day(39).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Hvítasunnudagur") \
            .on(day(49).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Annar dagur hvítasunnu") \
            .on(day(50).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Frídagur verslunarmanna") \
            .on(first("monday").of("august")) \
            .with_flags("NV")

        self.define_holiday() \
            .with_name("Sumardagurinn fyrsti") \
            .on(first("thursday").after(month=4, day=18)) \
            .with_flags("NV")

        """ 
        Both, Christmas Eve (_aðfangadagur jóla_) and New Year's Eve (_gamlársdagur_) are public holidays in Iceland from 13:00 only.
        They're included as full-day holidays, but with an explanatory note.
        """
        self.define_holiday() \
            .with_name("Aðfangadagur jóla") \
            .on(month=12, day=24) \
            .with_flags("NRF") \
            .annotated_with("Holiday from 13:00")

        self.define_holiday() \
            .with_name("Gamlársdagur") \
            .on(month=12, day=31) \
            .with_flags("NF") \
            .annotated_with("Holiday from 13:00")
