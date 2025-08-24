from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import day

__all__ = [
    "CH",
]


class CH(Country):
    id = "CH"
    languages = ["de"]
    default_lang = "de"
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Neujahrstag") \
            .on(month=1, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Berchtoldstag") \
            .in_regions(["BE", "JU", "TG", "VD"]) \
            .on(month=1, day=2) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Heilige Drei Könige") \
            .in_regions(["SZ", "TI", "UR"]) \
            .on(month=1, day=6) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Josefstag") \
            .in_regions(["NW", "SZ", "TI", "UR", "VS"]) \
            .on(month=3, day=19) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Tag der Arbeit") \
            .in_regions(["BL", "BS", "GR", "NE", "SH", "TG", "TI", "ZH"]) \
            .on(month=5, day=1) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Bundesfeier") \
            .on(month=8, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Mariä Himmelfahrt") \
            .in_regions(["AI"]) \
            .on(month=8, day=15) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Mariä Himmelfahrt") \
            .in_regions(["JU", "LU", "NW", "OW", "SZ", "TI", "UR", "VS", "ZG"]) \
            .on(month=8, day=15) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Allerheiligen") \
            .in_regions(["AI", "GL", "JU", "LU", "NW", "OW", "SG", "SZ", "TI", "UR", "VS", "ZG"]) \
            .on(month=11, day=1) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Mariä Empfängnis") \
            .in_regions(["AI"]) \
            .on(month=12, day=8) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Mariä Empfängnis") \
            .in_regions(["LU", "NW", "OW", "SZ", "TI", "UR", "VS", "ZG"]) \
            .on(month=12, day=8) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Weihnachtstag") \
            .on(month=12, day=25) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Stephanstag") \
            .in_regions(["AI", "AR", "BE", "BL", "BS", "GL", "GR", "LU", "SG", "SH", "SZ", "TG", "TI", "UR", "ZH"]) \
            .on(month=12, day=26) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Karfreitag") \
            .in_regions(["AG", "AI", "AR", "BE", "BL", "BS", "FR", "GE", "GL", "GR", "JU", "LU", "NE", "NW", "OW", "SG", "SH", "SO", "SZ", "TG", "UR", "VD", "ZG", "ZH"]) \
            .on(day(2).before(self.easter())) \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Ostersonntag") \
            .on(self.easter()) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Ostermontag") \
            .in_regions(["AI", "AR", "BE", "BL", "BS", "GE", "GL", "GR", "JU", "SG", "SH", "SZ", "TG", "TI", "UR", "VD", "ZH"]) \
            .on(day(1).after(self.easter())) \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Auffahrt") \
            .on(day(39).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Pfingstsonntag") \
            .on(day(49).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Pfingstmontag") \
            .in_regions(["AI", "AR", "BE", "BL", "BS", "GE", "GL", "GR", "JU", "SG", "SH", "SZ", "TG", "TI", "UR", "VD", "ZH"]) \
            .on(day(50).after(self.easter())) \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Fronleichnam") \
            .in_regions(["AI", "JU", "LU", "NW", "OW", "SZ", "TI", "UR", "VS", "ZG"]) \
            .on(day(60).after(self.easter())) \
            .with_flags("RV")
