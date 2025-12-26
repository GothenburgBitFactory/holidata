from holidata.holiday import Region
from holidata.utils import day, date, Month


class RP(Region):
    def __init__(self, country):
        super().__init__("RP", country)

        self.define_holiday() \
            .with_name("Allerheiligen") \
            .on(date(Month.NOVEMBER, 1)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Fronleichnam") \
            .on(day(60).after(country.easter())) \
            .with_flags("RV")
