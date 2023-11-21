from dateutil.easter import EASTER_WESTERN

from holidata.utils import SmartDayArrow
from .holidays import Country

"""
source: https://almanakka.helsinki.fi/en/flag-days-and-holidays-in-finland.html
"""


class FI(Country):
    id = "FI"
    languages = ["fi", "sv"]
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_names({
                "fi": "Uudenvuodenpäivä",
                "sv": "Nyårsdagen",
            }) \
            .on("01-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "fi": "Loppiainen",
                "sv": "Trettondedagen",
            }) \
            .on("01-06") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_names({
                "fi": "Vappu",
                "sv": "Första maj",
            }) \
            .on("05-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "fi": "Itsenäisyyspäivä",
                "sv": "Självständighetsdagen",
            }) \
            .on("12-06") \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "fi": "Joulupäivä",
                "sv": "Juldagen",
            }) \
            .on("12-25") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_names({
                "fi": "Tapaninpäivä",
                "sv": "Annandag jul",
            }) \
            .on("12-26") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_names({
                "fi": "Pitkäperjantai",
                "sv": "Långfredagen",
            }) \
            .on("2 days before Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_names({
                "fi": "Pääsiäispäivä",
                "sv": "Påskdagen",
            }) \
            .on("Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_names({
                "fi": "2. pääsiäispäivä",
                "sv": "Annandag påsk",
            }) \
            .on("1 day after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_names({
                "fi": "Helatorstai",
                "sv": "Kristi himmelfärdsdag",
            }) \
            .on("39 days after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_names({
                "fi": "Helluntaipäivä",
                "sv": "Pingst",
            }) \
            .on("49 days after Easter") \
            .with_flags("NRV")

        """
        Saturday between 20 and 26 June: Midsummer Day
        """
        self.define_holiday() \
            .with_names({
                "fi": "Juhannuspäivä",
                "sv": "Midsommardagen",
            }) \
            .on(self.midsummer_day) \
            .with_flags("NRV")

        """
        Saturday between 31 October and 6 November: All Saints' Day
        """
        self.define_holiday() \
            .with_names({
                "fi": "Pyhäinpäivä",
                "sv": "Alla helgons dag",
            }) \
            .on(self.all_saints_day) \
            .with_flags("NRV")

    @staticmethod
    def midsummer_day(year):
        return SmartDayArrow(year, 6, 19).shift_to_weekday("saturday", order=1, reverse=False)

    @staticmethod
    def all_saints_day(year):
        return SmartDayArrow(year, 10, 30).shift_to_weekday("saturday", order=1, reverse=False)
