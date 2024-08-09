from holidata.holiday import Region
from holidata.utils import day


class SL(Region):
    """
    https://recht.saarland.de/bssl/document/jlr-FeiertGSL1976V6P2
    """
    def __init__(self, country):
        super().__init__("SL", country)

        self.define_holiday() \
            .with_name("Mariä Himmelfahrt") \
            .on(month=8, day=15) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Allerheiligen") \
            .on(month=11, day=1) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Fronleichnam") \
            .on(day(60).after(country.easter())) \
            .with_flags("RV")
