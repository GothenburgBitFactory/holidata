from holidata.holidays.holidays import Region


class BW(Region):
    def __init__(self, country):
        super().__init__("BW", country)

        self.define_holiday() \
            .with_name("Heilige drei Könige") \
            .on("01-06") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Allerheiligen") \
            .on("11-01") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Fronleichnam") \
            .on("60 days after Easter") \
            .with_flags("RV")
