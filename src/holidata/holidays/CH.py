from dateutil.easter import EASTER_WESTERN

from .holidays import Country


class CH(Country):
    id = "CH"
    languages = ["de"]
    default_lang = "de"
    regions = ["AG", "AI", "AR", "BE", "BL", "BS", "FR", "GE", "GL", "GR", "JU", "LU", "NE", "NW", "OW", "SG", "SH",
               "SO", "SZ", "TI", "TG", "UR", "VD", "VS", "ZG", "ZH"]
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Neujahrstag") \
            .on("01-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Berchtoldstag") \
            .in_regions(["BE", "JU", "TG", "VD"]) \
            .on("01-02") \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Heilige Drei Könige") \
            .in_regions(["SZ", "TI", "UR"]) \
            .on("01-06") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Josefstag") \
            .in_regions(["NW", "SZ", "TI", "UR", "VS"]) \
            .on("03-19") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Tag der Arbeit") \
            .in_regions(["BL", "BS", "GR", "NE", "SH", "TG", "TI", "ZH"]) \
            .on("05-01") \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Bundesfeier") \
            .on("08-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Mariä Himmelfahrt") \
            .in_regions(["AI"]) \
            .on("08-15") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Mariä Himmelfahrt") \
            .in_regions(["JU", "LU", "NW", "OW", "SZ", "TI", "UR", "VS", "ZG"]) \
            .on("08-15") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Allerheiligen") \
            .in_regions(["AI", "GL", "JU", "LU", "NW", "OW", "SG", "SZ", "TI", "UR", "VS", "ZG"]) \
            .on("11-01") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Mariä Empfängnis") \
            .in_regions(["AI"]) \
            .on("12-08") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Mariä Empfängnis") \
            .in_regions(["LU", "NW", "OW", "SZ", "TI", "UR", "VS", "ZG"]) \
            .on("12-08") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Weihnachtstag") \
            .on("12-25") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Stephanstag") \
            .in_regions(["AI", "AR", "BE", "BL", "BS", "GL", "GR", "LU", "SG", "SH", "SZ", "TG", "TI", "UR", "ZH"]) \
            .on("12-26") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Karfreitag") \
            .in_regions(["AG", "AI", "AR", "BE", "BL", "BS", "FR", "GE", "GL", "GR", "JU", "LU", "NE", "NW", "OW", "SG", "SH", "SO", "SZ", "TG", "UR", "VD", "ZG", "ZH"]) \
            .on("2 days before Easter") \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Ostersonntag") \
            .on("Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Ostermontag") \
            .in_regions(["AI", "AR", "BE", "BL", "BS", "GE", "GL", "GR", "JU", "SG", "SH", "SZ", "TG", "TI", "UR", "VD", "ZH"]) \
            .on("1 day after Easter") \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Auffahrt") \
            .on("39 days after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Pfingstsonntag") \
            .on("49 days after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Pfingstmontag") \
            .in_regions(["AI", "AR", "BE", "BL", "BS", "GE", "GL", "GR", "JU", "SG", "SH", "SZ", "TG", "TI", "UR", "VD", "ZH"]) \
            .on("50 days after Easter") \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Fronleichnam") \
            .in_regions(["AI", "JU", "LU", "NW", "OW", "SZ", "TI", "UR", "VS", "ZG"]) \
            .on("60 days after Easter") \
            .with_flags("RV")
