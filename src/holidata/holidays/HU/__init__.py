from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import day

__all__ = [
    "HU",
]

"""
sources:
- Hungarian Constitution - Article J (1)
  https://www.keh.hu/magyarorszag_alaptorvenye/1515-Magyarorszag_Alaptorvenye
- 2017. évi XIII. törvény egyes törvényeknek a nagypéntek munkaszüneti nappá történő nyilvánításával összefüggő módosításáról
  https://mkogy.jogtar.hu/jogszabaly?docid=A1700013.TV
"""


class HU(Country):
    id = "HU"
    languages = ["hu"]
    default_lang = "hu"
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Újév") \
            .on(month=1, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Az 1848-as forradalom ünnepe") \
            .on(month=3, day=15) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("A munka ünnepe") \
            .on(month=5, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Az államalapítás ünnepe") \
            .on(month=8, day=20) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Az 1956-os forradalom ünnepe") \
            .on(month=10, day=23) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Mindenszentek") \
            .on(month=11, day=1) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Karácsony") \
            .on(month=12, day=25) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Karácsony") \
            .on(month=12, day=26) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Húsvét") \
            .on(self.easter()) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Húsvéthétfő") \
            .on(day(1).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Pünkösd") \
            .on(day(49).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Pünkösdhétfő") \
            .on(day(50).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Nagypéntek") \
            .since(2017) \
            .on(day(2).before(self.easter())) \
            .with_flags("NRV")

        for year, listing in HU.holiday_munkaszuneti_nap().items():
            for date, note in listing:
                self.define_holiday() \
                    .with_name("Munkaszüneti nap") \
                    .in_years([year]) \
                    .on(**date) \
                    .with_flags("NF") \
                    .annotated_with(note)

    @staticmethod
    def holiday_munkaszuneti_nap():
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
        2024: 15/2023. (VII.  13.) GFM rendelet a 2024. évi munkaszüneti napok körüli munkarendről
        2025: 11/2024. (IV.    8.) NGM rendelet a 2025. évi munkaszüneti napok körüli munkarendről
        2026: 10/2025. (IV.   30.) NGM rendelet a 2026. évi munkaszüneti napok körüli munkarendről
        """
        return {
            2015: [
                ({"month": 1, "day": 2}, "2015-01-10 munkanap"),
                ({"month": 8, "day": 21}, "2015-08-08 munkanap"),
                ({"month": 12, "day": 24}, "2015-12-12 munkanap"),
            ],
            2016: [
                ({"month": 3, "day": 14}, "2016-03-05 munkanap"),
                ({"month": 10, "day": 31}, "2016-10-15 munkanap"),
            ],
            2018: [
                ({"month": 3, "day": 16}, "2018-03-10 munkanap"),
                ({"month": 4, "day": 30}, "2018-04-21 munkanap"),
                ({"month": 10, "day": 22}, "2018-10-13 munkanap"),
                ({"month": 11, "day": 2}, "2018-11-10 munkanap"),
                ({"month": 12, "day": 24}, "2018-12-01 munkanap"),
                ({"month": 12, "day": 31}, "2018-12-15 munkanap"),
            ],
            2019: [
                ({"month": 8, "day": 19}, "2019-08-10 munkanap"),
                ({"month": 12, "day": 24}, "2019-12-07 munkanap"),
                ({"month": 12, "day": 27}, "2019-12-14 munkanap"),
            ],
            2020: [
                ({"month": 8, "day": 21}, "2020-08-29 munkanap"),
                ({"month": 12, "day": 24}, "2020-12-12 munkanap"),
            ],
            2021: [
                ({"month": 12, "day": 24}, "2021-12-11 munkanap")
            ],
            2022: [
                ({"month": 3, "day": 14}, "2022-03-26 munkanap"),
                ({"month": 10, "day": 31}, "2022-10-15 munkanap"),
            ],
            2024: [
                ({"month": 8, "day": 19}, "2024-08-03 munkanap"),
                ({"month": 12, "day": 24}, "2024-12-07 munkanap"),
                ({"month": 12, "day": 27}, "2024-12-14 munkanap"),
            ],
            2025: [
                ({"month": 5, "day": 2}, "2025-05-17 munkanap"),
                ({"month": 10, "day": 24}, "2025-10-18 munkanap"),
                ({"month": 12, "day": 24}, "2025-12-13 munkanap"),
            ],
            2026: [
                ({"month": 1, "day": 2}, "2026-01-10 munkanap"),
                ({"month": 8, "day": 21}, "2026-08-08 munkanap"),
                ({"month": 12, "day": 24}, "2026-12-12 munkanap"),
            ]
        }
