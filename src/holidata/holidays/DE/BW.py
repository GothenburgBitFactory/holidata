from holidata.holiday import Region
from holidata.utils import day


class BW(Region):
    def __init__(self, country):
        super().__init__("BW", country)

        self.define_holiday() \
            .with_name("Heilige drei Könige") \
            .on(month=1, day=6) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Allerheiligen") \
            .on(month=11, day=1) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Fronleichnam") \
            .on(day(60).after(country.easter())) \
            .with_flags("RV")
