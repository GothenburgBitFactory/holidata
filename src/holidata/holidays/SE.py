from dateutil.easter import EASTER_WESTERN

from holidata.utils import SmartDayArrow
from .holidays import Country


class SE(Country):
    id = "SE"
    languages = ["sv"]
    default_lang = "sv"
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Nyårsdagen") \
            .on("01-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Trettondedag jul") \
            .on("01-06") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Första maj") \
            .on("05-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Nationaldagen") \
            .on("06-06") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Julafton") \
            .on("12-24") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Juldagen") \
            .on("12-25") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Annandag jul") \
            .on("12-26") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Nyårsafton") \
            .on("12-31") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Långfredagen") \
            .on("2 days before Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Påskdagen") \
            .on("Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Annandag påsk") \
            .on("1 day after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Kristi himmelsfärdsdag") \
            .on("39 days after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Pingstdagen") \
            .on("49 days after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Midsommarafton") \
            .on(self.day_before_midsommar) \
            .with_flags("NV")

        self.define_holiday() \
            .with_name("Midsommardagen") \
            .on(self.midsommar) \
            .with_flags("NV")

        self.define_holiday() \
            .with_name("Alla helgons dag") \
            .on(self.saturday_after_10_31) \
            .with_flags("NRV")

    @staticmethod
    def midsommar(year):
        """
        Find the Saturday between 20 and 26 June
        """
        return SmartDayArrow(year, 6, 19).shift_to_weekday("saturday", order=1, reverse=False)

    def day_before_midsommar(self, year):
        return self.midsommar(year).shift(days=-1)

    @staticmethod
    def saturday_after_10_31(year):
        return SmartDayArrow(year, 10, 30).shift_to_weekday("saturday", order=1, reverse=False)
