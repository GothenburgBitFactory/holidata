from holidata.holiday import Region
from holidata.utils import day


class HE(Region):
    def __init__(self, country):
        super().__init__("HE", country)

        self.define_holiday() \
            .with_name("Fronleichnam") \
            .on(day(60).after(country.easter())) \
            .with_flags("RV")
