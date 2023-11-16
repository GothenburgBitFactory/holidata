from dateutil.easter import EASTER_WESTERN

from holidata.utils import SmartDayArrow
from .holidays import Country


class IS(Country):
    id = "IS"
    languages = ["is"]
    default_lang = "is"
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Nýársdagur") \
            .on("01-01") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Verkalýðsdagurinn") \
            .on("05-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Þjóðhátíðardagurinn") \
            .on("06-17") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Jóladagur") \
            .on("12-25") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Annar dagur jóla") \
            .on("12-26") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Skírdagur") \
            .on("3 days before Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Föstudagurinn langi") \
            .on("2 days before Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Páskadagur") \
            .on("Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Annar dagur páska") \
            .on("1 day after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Uppstigningardagur") \
            .on("39 days after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Hvítasunnudagur") \
            .on("49 days after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Annar dagur hvítasunnu") \
            .on("50 days after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Frídagur verslunarmanna") \
            .on("1. monday in August") \
            .with_flags("NV")

        self.define_holiday() \
            .with_name("Sumardagurinn fyrsti") \
            .on(self.first_thursday_after_04_18) \
            .with_flags("NV")

        """ 
        Both, Christmas Eve (_aðfangadagur jóla_) and New Year's Eve (_gamlársdagur_) are public holidays in Iceland from 13:00 only.
        They're included as full-day holidays, but with an explanatory note.
        """
        self.define_holiday() \
            .with_name("Aðfangadagur jóla") \
            .on("12-24") \
            .with_flags("NRF") \
            .annotated_with("Holiday from 13:00")

        self.define_holiday() \
            .with_name("Gamlársdagur") \
            .on("12-31") \
            .with_flags("NF") \
            .annotated_with("Holiday from 13:00")

    @staticmethod
    def first_thursday_after_04_18(year):
        return SmartDayArrow(year, 4, 18).shift_to_weekday("thursday")
