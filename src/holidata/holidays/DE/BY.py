from holidata.holiday import Country, Region
from holidata.utils import Month, date, day


class BY(Region):
    """
    https://www.gesetze-bayern.de/Content/Document/BayFTG-9
    """
    def __init__(self, country: Country) -> None:
        super().__init__("BY", country)

        self.define_holiday() \
            .with_name("Heilige drei Könige") \
            .on(date(Month.JANUARY, 6)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Mariä Himmelfahrt") \
            .on(date(Month.AUGUST, 15)) \
            .with_flags("RF") \
            .annotated_with("In Gemeinden mit überwiegend katholischer Bevölkerung")

        self.define_holiday() \
            .with_name("Allerheiligen") \
            .on(date(Month.NOVEMBER, 1)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Fronleichnam") \
            .on(day(60).after(country.easter())) \
            .with_flags("RV")
