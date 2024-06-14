from holidata.holidays.holidays import Region


class SL(Region):
    """
    https://recht.saarland.de/bssl/document/jlr-FeiertGSL1976V6P2
    """
    def __init__(self, country):
        super().__init__("SL", country)

        self.define_holiday() \
            .with_name("Mariä Himmelfahrt") \
            .on("08-15") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Allerheiligen") \
            .on("11-01") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Fronleichnam") \
            .on("60 days after Easter") \
            .with_flags("RV")
