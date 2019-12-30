from dateutil.easter import EASTER_WESTERN

from holidata.utils import SmartDayArrow
from .holidays import Holiday, Locale


class is_IS(Locale):
    """
    01-01: [NRF] Nýársdagur
    05-01: [NF] Verkalýðsdagurinn
    06-17: [NF] Þjóðhátíðardagurinn
    12-25: [NRF] Jóladagur
    12-26: [NRF] Annar dagur jóla
    3 days before Easter: [NRV] Skírdagur
    2 days before Easter: [NRV] Föstudagurinn langi
    Easter: [NRV] Páskadagur
    1 day after Easter: [NRV] Annar dagur páska
    39 days after Easter: [NRV] Uppstigningardagur
    49 days after Easter: [NRV] Hvítasunnudagur
    50 days after Easter: [NRV] Annar dagur hvítasunnu
    1. monday in August: [NV] Frídagur verslunarmanna
    """

    locale = "is-IS"
    easter_type = EASTER_WESTERN

    def holiday_first_day_of_summer(self):
        """
        Calculate sumardagurinn fyrsti (first day of summer).

        The holiday falls on the first Thursday after the 18th of April.
        """
        return [
            Holiday(
                locale=self.locale,
                region="",
                date=SmartDayArrow(self.year, 4, 18).shift_to_weekday("thursday"),
                description="Sumardagurinn fyrsti",
                flags="NV",
                notes="",
            )
        ]

    def holiday_half_days(self):
        """
        Define half-day holidays.

        Both Christmas Eve (_aðfangadagur jóla_) and New Year's Eve
        (_gamlársdagur_) are public holidays in Iceland from 13:00 only.
        They're included as full-day holidays, but with an explanatory
        note.

        12-24: [NRF] Aðfangadagur jóla
        12-31: [NF] Gamlársdagur
        """
        return [
            Holiday(
                locale=self.locale,
                region="",
                date=SmartDayArrow(self.year, 12, 24),
                description="Aðfangadagur jóla",
                flags="NRF",
                notes="Holiday from 13:00",
            ),
            Holiday(
                locale=self.locale,
                region="",
                date=SmartDayArrow(self.year, 12, 31),
                description="Gamlársdagur",
                flags="NF",
                notes="Holiday from 13:00",
            ),
        ]
