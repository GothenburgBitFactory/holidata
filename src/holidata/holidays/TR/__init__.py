from typing import Callable, Union

from arrow import Arrow
from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import Month, date, dates, day

__all__ = [
    "TR",
]

"""
sources:
law on national holidays and general holidays: https://www.mevzuat.gov.tr/mevzuat?MevzuatNo=2429&MevzuatTur=1&MevzuatTertip=5 
dates for holidays 'Ramazan Bayramı' and 'Kurban Bayramı': https://vakithesaplama.diyanet.gov.tr/dini_gunler.php
"""


class TR(Country):
    id = "TR"
    languages = ["tr"]
    easter_type = EASTER_WESTERN

    def __init__(self) -> None:
        super().__init__()

        self.define_holiday() \
            .with_name("Yılbaşı") \
            .on(date(Month.JANUARY, 1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Ulusal Egemenlik ve Çocuk Bayramı") \
            .on(date(Month.APRIL, 23)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Emek ve Dayanışma Günü") \
            .on(date(Month.MAY, 1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Atatürk'ü Anma, Gençlik ve Spor Bayramı") \
            .on(date(Month.MAY, 19)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Zafer Bayramı") \
            .on(date(Month.AUGUST, 30)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Cumhuriyet Bayramı") \
            .on(date(Month.OCTOBER, 29)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Demokrasi ve Milli Birlik Günü") \
            .on(date(Month.JULY, 15)) \
            .since(2017) \
            .with_flags("NF")

        """
        Ramazan Bayramı 1.-3. Gün
        """
        for i in [1, 2, 3]:
            self.define_holiday() \
                .with_name(f"Ramazan Bayramı ({i}. Gün)") \
                .on(TR.ramazan_bayrami_day(i)) \
                .with_flags("NRV")

        """
        Kurban Bayramı 1.-4. Gün
        """
        for i in [1, 2, 3, 4]:
            self.define_holiday() \
                .with_name(f"Kurban Bayramı ({i}. Gün)") \
                .on(TR.kurban_bayrami_day(i)) \
                .with_flags("NRV")

    @staticmethod
    def ramazan_bayrami_day(ordinal: int) -> Callable[[int], Union[Arrow, None]]:
        def ramazan_bayrami_reference_shifted(year: int) -> Union[Arrow, None]:
            reference = TR.__ramazan_bayrami_reference()
            return day(ordinal).after(reference)(year) if reference is not None else None

        return ramazan_bayrami_reference_shifted

    @staticmethod
    def kurban_bayrami_day(ordinal: int) -> Callable[[int], Union[Arrow, None]]:
        def kurban_bayrami_reference_shifted(year: int) -> Union[Arrow, None]:
            reference = TR.__kurban_bayrami_reference()
            return day(ordinal).after(reference)(year) if reference is not None else None

        return kurban_bayrami_reference_shifted

    @staticmethod
    def __ramazan_bayrami_reference():
        return dates({
            2011: (Month.AUGUST, 29),
            2012: (Month.AUGUST, 18),
            2013: (Month.AUGUST, 7),
            2014: (Month.JULY, 27),
            2015: (Month.JULY, 16),
            2016: (Month.JULY, 4),
            2017: (Month.JUNE, 24),
            2018: (Month.JUNE, 14),
            2019: (Month.JUNE, 4),
            2020: (Month.MAY, 23),
            2021: (Month.MAY, 12),
            2022: (Month.MAY, 1),
            2023: (Month.APRIL, 20),
            2024: (Month.APRIL, 9),
            2025: (Month.MARCH, 29),
            2026: (Month.MARCH, 19),
            2027: (Month.MARCH, 8),
        })

    @staticmethod
    def __kurban_bayrami_reference():
        return dates({
            2011: (Month.NOVEMBER, 5),
            2012: (Month.OCTOBER, 24),
            2013: (Month.OCTOBER, 14),
            2014: (Month.OCTOBER, 3),
            2015: (Month.SEPTEMBER, 23),
            2016: (Month.SEPTEMBER, 11),
            2017: (Month.AUGUST, 31),
            2018: (Month.AUGUST, 20),
            2019: (Month.AUGUST, 10),
            2020: (Month.JULY, 30),
            2021: (Month.JULY, 19),
            2022: (Month.JULY, 8),
            2023: (Month.JUNE, 27),
            2024: (Month.JUNE, 15),
            2025: (Month.JUNE, 5),
            2026: (Month.MAY, 26),
            2027: (Month.MAY, 15),
        })
