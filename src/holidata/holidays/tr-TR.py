# coding=utf-8
from holidata.utils import SmartDayArrow
from .holidays import Locale, Holiday

"""
sources:
law on national holidays and general holidays: https://www.mevzuat.gov.tr/mevzuat?MevzuatNo=2429&MevzuatTur=1&MevzuatTertip=5 
dates for holidays 'Ramazan Bayramı' and 'Kurban Bayramı': https://vakithesaplama.diyanet.gov.tr/dini_gunler.php
"""


class tr_TR(Locale):
    """
    01-01: [NF] Yılbaşı
    04-23: [NF] Ulusal Egemenlik ve Çocuk Bayramı
    05-01: [NF] Emek ve Dayanışma Günü
    05-19: [NF] Atatürk'ü Anma, Gençlik ve Spor Bayramı
    08-30: [NF] Zafer Bayramı
    10-29: [NF] Cumhuriyet Bayramı
    """

    locale = "tr-TR"

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

        return ramazan_bayrami_reference[year]

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

        return kurban_bayrami_reference[year]

    def holiday_demokrasi_ve_milli_birlik_gunu(self):
        """
        Democracy and National Unity Day (since 2017)
        07-15 [NF] Demokrasi ve Milli Birlik Günü
        """
        return [Holiday(
            self.locale,
            "",
            SmartDayArrow(self.year, 7, 15),
            "Demokrasi ve Milli Birlik Günü",
            "NF"
        )] if self.year >= 2017 else []

    def holiday_ramazan_bayrami(self):
        """
        Ramazan Bayramı 1.-3. Gün
        """
        reference = self.__ramazan_bayrami_reference(self.year)

        return [Holiday(
            self.locale,
            "",
            reference.shift(days=i),
            f"Ramazan Bayramı ({i}. Gün)",
            "NRV"
        ) for i in [1, 2, 3]]

    def holiday_kurban_bayrami(self):
        """
        Kurban Bayramı 1.-4. Gün
        """
        reference = self.__kurban_bayrami_reference(self.year)

        return [Holiday(
            self.locale,
            "",
            reference.shift(days=i),
            "Kurban Bayramı ({}. Gün)".format(i),
            "NRV"
        ) for i in [1, 2, 3, 4]]
