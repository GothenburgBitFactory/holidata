# coding=utf-8
from dateutil.easter import EASTER_WESTERN

from holidata.utils import easter, SmartDayArrow
from .holidays import Locale, Holiday

"""
source: https://www.zakonyprolidi.cz/cs/2000-245, §1 and §2.
        https://www.zakonyprolidi.cz/cs/2000-245/zneni-20200201 (>2020-02-01)
        https://www.zakonyprolidi.cz/cs/2000-245/zneni-20190401 (>2019-04-01)
        https://www.zakonyprolidi.cz/cs/2000-245/zneni-0 (>2000-08-09)
"""


class cs_CZ(Locale):
    """
    01-01: [NF] Nový rok
    01-01: [NF] Den obnovy samostatného českého státu
    05-01: [NF] Svátek práce
    05-08: [NF] Den vítězství
    07-05: [NRF] Den slovanských věrozvěstů Cyrila a Metoděje
    07-06: [NRF] Den upálení mistra Jana Husa
    09-28: [NRF] Den české státnosti
    10-28: [NF] Den vzniku samostatného československého státu
    12-24: [NRF] Štědrý den
    12-25: [NRF] 1. svátek vánoční
    12-26: [NRF] 2. svátek vánoční
    1 day after Easter: [NRV] Velikonoční pondělí
    """

    locale = "cs-CZ"
    easter_type = EASTER_WESTERN

    def holiday_velky_patek(self):
        """
        2 days before Easter: [NRV] Velký pátek
        since 2016
        """
        if self.year >= 2016:
            return [Holiday(
                self.locale,
                "",
                easter(self.year, self.easter_type).shift(days=-2),
                "Velký pátek",
                "NRV"
            )]

        return []

    def holiday_den_boje_za_svobodu_a_demokracii_a_mezinarodni_den_studentstva(self):
        """
        11-17: [NF]
        before 2019-04-01: Den boje za svobodu a demokracii
        before 2019-04-01: Den boje za svobodu a demokracii a Mezinárodní den studentstva
        """
        if self.year < 2019:
            name = "Den boje za svobodu a demokracii"
        else:
            name = "Den boje za svobodu a demokracii a Mezinárodní den studentstva"

        return [Holiday(
            self.locale,
            "",
            SmartDayArrow(self.year, 11, 17),
            name,
            "NF"
        )]
