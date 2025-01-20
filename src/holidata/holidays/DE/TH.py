from holidata.holiday import Region
from holidata.utils import day


class TH(Region):
    def __init__(self, country):
        super().__init__("TH", country)

        self.define_holiday() \
            .with_name("Weltkindertag") \
            .since(2019) \
            .on(month=9, day=20) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Reformationstag") \
            .until(2016) \
            .on(month=10, day=31) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Reformationstag") \
            .since(2018) \
            .on(month=10, day=31) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Fronleichnam") \
            .on(day(60).after(country.easter())) \
            .with_flags("RV") \
            .annotated_with("In Gemeinden mit überwiegend katholischer Bevölkerung")
