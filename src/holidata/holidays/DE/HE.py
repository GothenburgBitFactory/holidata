from holidata.holidays.holidays import Region


class HE(Region):
    def __init__(self, country):
        super().__init__("HE", country)

        self.define_holiday() \
            .with_name("Fronleichnam") \
            .on("60 days after Easter") \
            .with_flags("RV")
