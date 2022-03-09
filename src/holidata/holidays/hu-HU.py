# coding=utf-8
from dateutil.easter import EASTER_WESTERN

from holidata.utils import easter, SmartDayArrow
from .holidays import Locale, Holiday

"""
sources:
- Hungarian Constitution - Article J (1)
  https://www.keh.hu/magyarorszag_alaptorvenye/1515-Magyarorszag_Alaptorvenye
- 2017. évi XIII. törvény egyes törvényeknek a nagypéntek munkaszüneti nappá történő nyilvánításával összefüggő módosításáról
  https://mkogy.jogtar.hu/jogszabaly?docid=A1700013.TV
"""


class hu_HU(Locale):
    """
    01-01: [NF] Újév
    03-15: [NF] Az 1848-as forradalom ünnepe
    05-01: [NF] A munka ünnepe
    08-20: [NF] Az államalapítás ünnepe
    10-23: [NF] Az 1956-os forradalom ünnepe
    11-01: [NRF] Mindenszentek
    12-25: [NRF] Karácsony
    12-26: [NRF] Karácsony
    Easter: [NRV] Húsvét
    1 day after Easter: [NRV] Húsvéthétfő
    49 days after Easter: [NRV] Pünkösd
    50 days after Easter: [NRV] Pünkösdhétfő
    """

    locale = "hu-HU"
    easter_type = EASTER_WESTERN

    def holiday_nagypentek(self):
        """
        2 days before Easter: [NRV] Nagypéntek (since 2017)
        """
        if self.year >= 2017:
            return [Holiday(
                self.locale,
                "",
                easter(self.year, self.easter_type).shift(days=-2),
                "Nagypéntek",
                "NRV"
            )]
        else:
            return []

    def holiday_munkaszuneti_nap(self):
        """
        Non-Working days (Munkaszüneti nap)
        When a public holiday falls on a Tuesday or a Thursday, a special decree swaps the preceding Monday or the
        following Friday (respectively) with a not too distant Saturday
        2015: 28/2014. (IX.   24.) NGM rendelet a 2015. évi munkaszüneti napok körüli munkarendről
        2016:  8/2015. (VI.   29.) NGM rendelet a 2016. évi munkaszüneti napok körüli munkarendről
        2018:  9/2017. (V.    19.) NGM rendelet a 2018. évi munkaszüneti napok körüli munkarendről
        2019:  6/2018. (VIII. 23.) PM  rendelet a 2019. évi munkaszüneti napok körüli munkarendről
        2020:  7/2019. (VI.   25.) PM  rendelet a 2020. évi munkaszüneti napok körüli munkarendről
        2021: 14/2020. (V.    13.) ITM rendelet a 2021. évi munkaszüneti napok körüli munkarendről
        2022: 23/2021. (VI.    1.) ITM rendelet a 2022. évi munkaszüneti napok körüli munkarendről
        """
        if self.year == 2015:
            """
            01-02, swapped with 01-10
            08-21, swapped with 08-08
            12-24, swapped with 12-12
            """
            return [
                Holiday(
                    locale=self.locale,
                    region="",
                    date=SmartDayArrow(self.year, 1, 2),
                    description="Munkaszüneti nap",
                    flags="NF",
                    notes="2015-01-10 munkanap"
                ),
                Holiday(
                    locale=self.locale,
                    region="",
                    date=SmartDayArrow(self.year, 8, 21),
                    description="Munkaszüneti nap",
                    flags="NF",
                    notes="2015-08-08 munkanap"
                ),
                Holiday(
                    locale=self.locale,
                    region="",
                    date=SmartDayArrow(self.year, 12, 24),
                    description="Munkaszüneti nap",
                    flags="NF",
                    notes="2015-12-12 munkanap"
                )]
        if self.year == 2016:
            """
            03-14, swapped with 03-05
            10-31, swapped with 10-15
            """
            return [
                Holiday(
                    locale=self.locale,
                    region="",
                    date=SmartDayArrow(self.year, 3, 14),
                    description="Munkaszüneti nap",
                    flags="NF",
                    notes="2016-03-05 munkanap"
                ),
                Holiday(
                    locale=self.locale,
                    region="",
                    date=SmartDayArrow(self.year, 10, 31),
                    description="Munkaszüneti nap",
                    flags="NF",
                    notes="2016-10-15 munkanap"
                )]
        if self.year == 2018:
            """
            03-16, swapped with 03-10
            04-30, swapped with 04-21
            10-22, swapped with 10-13
            11-02, swapped with 11-10
            12-24, swapped with 12-01
            12-31, swapped with 12-15
            """
            return [
                Holiday(
                    locale=self.locale,
                    region="",
                    date=SmartDayArrow(self.year, 3, 16),
                    description="Munkaszüneti nap",
                    flags="NF",
                    notes="2018-03-10 munkanap"
                ),
                Holiday(
                    locale=self.locale,
                    region="",
                    date=SmartDayArrow(self.year, 4, 30),
                    description="Munkaszüneti nap",
                    flags="NF",
                    notes="2018-04-21 munkanap"
                ),
                Holiday(
                    locale=self.locale,
                    region="",
                    date=SmartDayArrow(self.year, 10, 22),
                    description="Munkaszüneti nap",
                    flags="NF",
                    notes="2018-10-13 munkanap"
                ),
                Holiday(
                    locale=self.locale,
                    region="",
                    date=SmartDayArrow(self.year, 11, 2),
                    description="Munkaszüneti nap",
                    flags="NF",
                    notes="2018-11-10 munkanap"
                ),
                Holiday(
                    locale=self.locale,
                    region="",
                    date=SmartDayArrow(self.year, 12, 24),
                    description="Munkaszüneti nap",
                    flags="NF",
                    notes="2018-12-01 munkanap"
                ),
                Holiday(
                    locale=self.locale,
                    region="",
                    date=SmartDayArrow(self.year, 12, 31),
                    description="Munkaszüneti nap",
                    flags="NF",
                    notes="2018-12-15 munkanap"
                )]
        if self.year == 2019:
            """
            08-19, swapped with 08-10
            12-24, swapped with 12-07
            12-27, swapped with 12-14
            """
            return [
                Holiday(
                    locale=self.locale,
                    region="",
                    date=SmartDayArrow(self.year, 8, 19),
                    description="Munkaszüneti nap",
                    flags="NF",
                    notes="2019-08-10 munkanap"
                ),
                Holiday(
                    locale=self.locale,
                    region="",
                    date=SmartDayArrow(self.year, 12, 24),
                    description="Munkaszüneti nap",
                    flags="NF",
                    notes="2019-12-07 munkanap"
                ),
                Holiday(
                    locale=self.locale,
                    region="",
                    date=SmartDayArrow(self.year, 12, 27),
                    description="Munkaszüneti nap",
                    flags="NF",
                    notes="2019-12-14 munkanap"
                )]
        if self.year == 2020:
            """
            08-21, swapped with 08-29
            12-24, swapped with 12-12
            """
            return [
                Holiday(
                    locale=self.locale,
                    region="",
                    date=SmartDayArrow(self.year, 8, 21),
                    description="Munkaszüneti nap",
                    flags="NF",
                    notes="2020-08-29 munkanap"),
                Holiday(
                    locale=self.locale,
                    region="",
                    date=SmartDayArrow(self.year, 12, 24),
                    description="Munkaszüneti nap",
                    flags="NF",
                    notes="2020-12-12 munkanap"
                )]
        if self.year == 2021:
            """
            12-24, swapped with 12-11
            """
            return [
                Holiday(
                    locale=self.locale,
                    region="",
                    date=SmartDayArrow(self.year, 12, 24),
                    description="Munkaszüneti nap",
                    flags="NF",
                    notes="2021-12-11 munkanap"
                )]
        if self.year == 2022:
            """
            03-14, swapped with 03-26
            10-31, swapped with 10-15
            """
            return [
                Holiday(
                    locale=self.locale,
                    region="",
                    date=SmartDayArrow(self.year, 3, 14),
                    description="Munkaszüneti nap",
                    flags="NF",
                    notes="2022-03-26 munkanap"),
                Holiday(
                    locale=self.locale,
                    region="",
                    date=SmartDayArrow(self.year, 10, 31),
                    description="Munkaszüneti nap",
                    flags="NF",
                    notes="2022-10-15 munkanap"
                )]

        return []
