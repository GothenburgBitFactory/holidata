from holidata.holiday import Region
from holidata.utils import day, date


class BY(Region):
    """
    https://www.gesetze-bayern.de/Content/Document/BayFTG-9
    """
    def __init__(self, country):
        super().__init__("BY", country)

        self.define_holiday() \
            .with_name("Heilige drei Könige") \
            .on(date(month=1, day=6)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Mariä Himmelfahrt") \
            .on(date(month=8, day=15)) \
            .with_flags("RF") \
            .annotated_with("In Gemeinden mit überwiegend katholischer Bevölkerung")

        self.define_holiday() \
            .with_name("Allerheiligen") \
            .on(date(month=11, day=1)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Fronleichnam") \
            .on(day(60).after(country.easter())) \
            .with_flags("RV")
