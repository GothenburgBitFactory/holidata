from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import SmartDayArrow, day

__all__ = [
    "NL",
]


class NL(Country):
    id = "NL"
    languages = ["nl"]
    default_lang = "nl"
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Nieuwjaarsdag") \
            .on(month=1, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Dodenherdenking") \
            .on(month=5, day=4) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Bevrijdingsdag") \
            .on(month=5, day=5) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Sinterklaas") \
            .on(month=12, day=5) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Eerste Kerstdag") \
            .on(month=12, day=25) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Tweede Kerstdag") \
            .on(month=12, day=26) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Goede Vrijdag") \
            .on(day(2).before(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Eerste Paasdag") \
            .on(self.easter()) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Tweede Paasdag") \
            .on(day(1).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Hemelvaartsdag") \
            .on(day(39).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Eerste Pinksterdag") \
            .on(day(49).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Tweede Pinksterdag") \
            .on(day(50).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Koninginnedag") \
            .until(2013) \
            .on(NL.koninginnedag) \
            .with_flags("NV")

        self.define_holiday() \
            .with_name("Koningsdag") \
            .since(2014) \
            .on(NL.koningsdag) \
            .with_flags("NV")

        self.define_holiday() \
            .with_name("Koninkrijksdag") \
            .on(NL.koninkrijksdag) \
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
