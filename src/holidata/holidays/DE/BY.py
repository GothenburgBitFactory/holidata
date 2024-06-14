from holidata.holidays.holidays import Region


class BY(Region):
    """
    https://www.gesetze-bayern.de/Content/Document/BayFTG-9
    """
    def __init__(self, country):
        super().__init__("BY", country)

        self.define_holiday() \
            .with_name("Heilige drei Könige") \
            .on("01-06") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Mariä Himmelfahrt") \
            .on("08-15") \
            .with_flags("RF") \
            .annotated_with("In Gemeinden mit überwiegend katholischer Bevölkerung")

        self.define_holiday() \
            .with_name("Allerheiligen") \
            .on("11-01") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Fronleichnam") \
            .on("60 days after Easter") \
            .with_flags("RV")
