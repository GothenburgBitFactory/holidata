from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import date, Month

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

    def __init__(self):
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
    def ramazan_bayrami_day(ordinal):
        def ramazan_bayrami_reference_shifted(year):
            reference = TR.__ramazan_bayrami_reference(year)
            return reference.shift(days=ordinal) if reference is not None else None

        return ramazan_bayrami_reference_shifted

    @staticmethod
    def kurban_bayrami_day(ordinal):
        def kurban_bayrami_reference_shifted(year):
            reference = TR.__kurban_bayrami_reference(year)
            return reference.shift(days=ordinal) if reference is not None else None

        return kurban_bayrami_reference_shifted

    @staticmethod
    def __ramazan_bayrami_reference(year):
        dates = {
            2011: date(Month.AUGUST, 29),
            2012: date(Month.AUGUST, 18),
            2013: date(Month.AUGUST, 7),
            2014: date(Month.JULY, 27),
            2015: date(Month.JULY, 16),
            2016: date(Month.JULY, 4),
            2017: date(Month.JUNE, 24),
            2018: date(Month.JUNE, 14),
            2019: date(Month.JUNE, 4),
            2020: date(Month.MAY, 23),
            2021: date(Month.MAY, 12),
            2022: date(Month.MAY, 1),
            2023: date(Month.APRIL, 20),
            2024: date(Month.APRIL, 9),
            2025: date(Month.MARCH, 29),
            2026: date(Month.MARCH, 19),
            2027: date(Month.MARCH, 8),
        }

        return dates.get(year)(year) if year in dates else None

    @staticmethod
    def __kurban_bayrami_reference(year):
        dates = {
            2011: date(Month.NOVEMBER, 5),
            2012: date(Month.OCTOBER, 24),
            2013: date(Month.OCTOBER, 14),
            2014: date(Month.OCTOBER, 3),
            2015: date(Month.SEPTEMBER, 23),
            2016: date(Month.SEPTEMBER, 11),
            2017: date(Month.AUGUST, 31),
            2018: date(Month.AUGUST, 20),
            2019: date(Month.AUGUST, 10),
            2020: date(Month.JULY, 30),
            2021: date(Month.JULY, 19),
            2022: date(Month.JULY, 8),
            2023: date(Month.JUNE, 27),
            2024: date(Month.JUNE, 15),
            2025: date(Month.JUNE, 5),
            2026: date(Month.MAY, 26),
            2027: date(Month.MAY, 15),
        }

        return dates.get(year)(year) if year in dates else None
