from dateutil.easter import EASTER_WESTERN

from holidata.utils import SmartDayArrow
from .holidays import Country


class NL(Country):
    id = "NL"
    languages = ["nl"]
    default_lang = "nl"
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Nieuwjaarsdag") \
            .on("01-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Dodenherdenking") \
            .on("05-04") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Bevrijdingsdag") \
            .on("05-05") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Sinterklaas") \
            .on("12-05") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Eerste Kerstdag") \
            .on("12-25") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Tweede Kerstdag") \
            .on("12-26") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Goede Vrijdag") \
            .on("2 days before Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Eerste Paasdag") \
            .on("Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Tweede Paasdag") \
            .on("1 day after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Hemelvaartsdag") \
            .on("39 days after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Eerste Pinksterdag") \
            .on("49 days after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Tweede Pinksterdag") \
            .on("50 days after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Koninginnedag") \
            .until(2013) \
            .on(self.koninginnedag) \
            .with_flags("NV")

        self.define_holiday() \
            .with_name("Koningsdag") \
            .since(2014) \
            .on(self.koningsdag) \
            .with_flags("NV")

        self.define_holiday() \
            .with_name("Koninkrijksdag") \
            .on(self.koninkrijksdag) \
            .with_flags("NV")

    @staticmethod
    def koninginnedag(year):
        """
        04-30 or saturday before, if it falls on sunday
        """
        date = SmartDayArrow(year, 4, 30)

        if date.weekday() == "sunday":
            date = date.shift(days=-1)

        return date

    @staticmethod
    def koningsdag(year):
        """
        04-27 or saturday before if it falls on sunday
        """
        date = SmartDayArrow(year, 4, 27)

        if date.weekday() == "sunday":
            date = date.shift(days=-1)

        return date

    @staticmethod
    def koninkrijksdag(year):
        """
        04-27 or monday after if it falls on sunday
        """
        date = SmartDayArrow(year, 12, 15)

        if date.weekday() == "sunday":
            date = date.shift(days=1)

        return date
