from dateutil.easter import EASTER_WESTERN

from holidata.utils import SmartDayArrow
from .holidays import Country


class DE(Country):
    id = "DE"
    languages = ["de"]
    default_lang = "de"
    regions = ["BB", "BE", "BH", "BW", "BY", "HE", "HH", "MV", "NI", "NW", "RP", "SH", "SL", "SN", "ST", "TH"]
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()
        self.default_lang = "de"

        self.define_holiday() \
            .with_name("Neujahr") \
            .on("01-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Heilige drei Könige") \
            .in_regions(["BW", "BY", "ST"]) \
            .on("01-06") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Erster Maifeiertag") \
            .on("05-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Mariä Himmelfahrt") \
            .in_region("SL") \
            .on("08-15") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Tag der Deutschen Einheit") \
            .on("10-03") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Allerheiligen") \
            .in_regions(["BW", "BY", "NW", "RP", "SL"]) \
            .on("11-01") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Heilig Abend") \
            .on("12-24") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Weihnachtstag") \
            .on("12-25") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Zweiter Weihnachtstag") \
            .on("12-26") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Silvester") \
            .on("12-31") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Karfreitag") \
            .on("2 days before Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Ostern") \
            .on("Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Ostermontag") \
            .on("1 day after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Christi Himmelfahrt") \
            .on("39 days after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Pfingstsonntag") \
            .on("49 days after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Pfingstmontag") \
            .on("50 days after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Fronleichnam") \
            .in_regions(["BW", "BY", "HE", "NW", "RP", "SL"]) \
            .on("60 days after Easter") \
            .with_flags("RV")

        """
        11 days before 4. sunday before 12-25: Buß- und Bettag
        """
        self.define_holiday() \
            .with_name("Buß- und Bettag") \
            .in_region("SN") \
            .on(self.buss_und_bettag) \
            .with_flags("RV")

        """
        2020-05-08: 75. Jahrestag der Befreiung vom Nationalsozialismus und der Beendigung des Zweiten Weltkrieges in Europa
        Introduced 2019 for Berlin
        https://gesetze.berlin.de/perma?d=jlr-FeiertGBEV6P1
        """
        self.define_holiday() \
            .with_name("75. Jahrestag der Befreiung vom Nationalsozialismus und der Beendigung des Zweiten Weltkrieges in Europa") \
            .in_region("BE") \
            .in_years([2020]) \
            .on("05-08") \
            .with_flags("F")

        """
        03-08: Frauentag
        Introduced 2019 for Berlin
        https://gesetze.berlin.de/perma?d=jlr-FeiertGBEV6P1
        """
        self.define_holiday() \
            .with_name("Internationaler Frauentag") \
            .in_region("BE") \
            .since(2019) \
            .on("03-08") \
            .with_flags("F")

        """
        before 2018: 10-31: [BB, MV, SN, ST, TH] [RF] Reformationstag
        since 2018:  10-31: [BB, BH, HH, MV, NI, SH, SN, ST, TH] [RF] Reformationstag
        2017:        10-31: [NRF] Reformationstag (national holiday because of 500th anniversary)

        """
        self.define_holiday() \
            .with_name("Reformationstag") \
            .in_years([2017]) \
            .on("10-31") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Reformationstag") \
            .in_regions(["BB", "MV", "SN", "ST", "TH"]) \
            .until(2016) \
            .on("10-31") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Reformationstag") \
            .in_regions(["BB", "BH", "HH", "MV", "NI", "SH", "SN", "ST", "TH"]) \
            .since(2018) \
            .on("10-31") \
            .with_flags("RF")

    @staticmethod
    def buss_und_bettag(year):
        return SmartDayArrow(year, 12, 25).shift_to_weekday("sunday", order=4, reverse=True).shift(days=-11)
