from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import day, first

__all__ = [
    "FI",
]

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
            .on(month=1, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "fi": "Loppiainen",
                "sv": "Trettondedagen",
            }) \
            .on(month=1, day=6) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_names({
                "fi": "Vappu",
                "sv": "Första maj",
            }) \
            .on(month=5, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "fi": "Itsenäisyyspäivä",
                "sv": "Självständighetsdagen",
            }) \
            .on(month=12, day=6) \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "fi": "Joulupäivä",
                "sv": "Juldagen",
            }) \
            .on(month=12, day=25) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_names({
                "fi": "Tapaninpäivä",
                "sv": "Annandag jul",
            }) \
            .on(month=12, day=26) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_names({
                "fi": "Pitkäperjantai",
                "sv": "Långfredagen",
            }) \
            .on(day(2).before(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_names({
                "fi": "Pääsiäispäivä",
                "sv": "Påskdagen",
            }) \
            .on(self.easter()) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_names({
                "fi": "2. pääsiäispäivä",
                "sv": "Annandag påsk",
            }) \
            .on(day(1).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_names({
                "fi": "Helatorstai",
                "sv": "Kristi himmelfärdsdag",
            }) \
            .on(day(39).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_names({
                "fi": "Helluntaipäivä",
                "sv": "Pingst",
            }) \
            .on(day(49).after(self.easter())) \
            .with_flags("NRV")

        """
        Saturday between 20 and 26 June: Midsummer Day
        """
        self.define_holiday() \
            .with_names({
                "fi": "Juhannuspäivä",
                "sv": "Midsommardagen",
            }) \
            .on(first("saturday").after(month=6, day=19)) \
            .with_flags("NRV")

        """
        Saturday between 31 October and 6 November: All Saints' Day
        """
        self.define_holiday() \
            .with_names({
                "fi": "Pyhäinpäivä",
                "sv": "Alla helgons dag",
            }) \
            .on(first("saturday").after(month=10, day=30)) \
            .with_flags("NRV")
