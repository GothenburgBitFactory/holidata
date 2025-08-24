from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import SmartDayArrow

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
    default_lang = "tr"
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Yılbaşı") \
            .on(month=1, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Ulusal Egemenlik ve Çocuk Bayramı") \
            .on(month=4, day=23) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Emek ve Dayanışma Günü") \
            .on(month=5, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Atatürk'ü Anma, Gençlik ve Spor Bayramı") \
            .on(month=5, day=19) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Zafer Bayramı") \
            .on(month=8, day=30) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Cumhuriyet Bayramı") \
            .on(month=10, day=29) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Demokrasi ve Milli Birlik Günü") \
            .on(month=7, day=15) \
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
        ramazan_bayrami_reference = {
            2011: SmartDayArrow(2011, 8, 29),
            2012: SmartDayArrow(2012, 8, 18),
            2013: SmartDayArrow(2013, 8,  7),
            2014: SmartDayArrow(2014, 7, 27),
            2015: SmartDayArrow(2015, 7, 16),
            2016: SmartDayArrow(2016, 7,  4),
            2017: SmartDayArrow(2017, 6, 24),
            2018: SmartDayArrow(2018, 6, 14),
            2019: SmartDayArrow(2019, 6,  4),
            2020: SmartDayArrow(2020, 5, 23),
            2021: SmartDayArrow(2021, 5, 12),
            2022: SmartDayArrow(2022, 5,  1),
            2023: SmartDayArrow(2023, 4, 20),
            2024: SmartDayArrow(2024, 4,  9),
            2025: SmartDayArrow(2025, 3, 29),
            2026: SmartDayArrow(2026, 3, 19),
            2027: SmartDayArrow(2027, 3,  8),
        }

        return ramazan_bayrami_reference.get(year)

    @staticmethod
    def __kurban_bayrami_reference(year):
        kurban_bayrami_reference = {
            2011: SmartDayArrow(2011, 11,  5),
            2012: SmartDayArrow(2012, 10, 24),
            2013: SmartDayArrow(2013, 10, 14),
            2014: SmartDayArrow(2014, 10,  3),
            2015: SmartDayArrow(2015,  9, 23),
            2016: SmartDayArrow(2016,  9, 11),
            2017: SmartDayArrow(2017,  8, 31),
            2018: SmartDayArrow(2018,  8, 20),
            2019: SmartDayArrow(2019,  8, 10),
            2020: SmartDayArrow(2020,  7, 30),
            2021: SmartDayArrow(2021,  7, 19),
            2022: SmartDayArrow(2022,  7,  8),
            2023: SmartDayArrow(2023,  6, 27),
            2024: SmartDayArrow(2024,  6, 15),
            2025: SmartDayArrow(2025,  6,  5),
            2026: SmartDayArrow(2026,  5, 26),
            2027: SmartDayArrow(2027,  5, 15),
        }

        return kurban_bayrami_reference.get(year)
