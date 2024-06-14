from holidata.holidays.holidays import Region


class RP(Region):
    def __init__(self, country):
        super().__init__("RP", country)

        self.define_holiday() \
            .with_name("Allerheiligen") \
            .on("11-01") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Fronleichnam") \
            .on("60 days after Easter") \
            .with_flags("RV")
