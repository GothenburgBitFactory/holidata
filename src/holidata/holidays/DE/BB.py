from holidata.holidays.holidays import Region


class BB(Region):
    """

    """
    def __init__(self, country):
        super().__init__("BB", country)

        self.define_holiday() \
            .with_name("Reformationstag") \
            .until(2016) \
            .on("10-31") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Reformationstag") \
            .since(2018) \
            .on("10-31") \
            .with_flags("RF")
