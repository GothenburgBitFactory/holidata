from holidata.holidays.holidays import Region


class NI(Region):
    def __init__(self, country):
        super().__init__("NI", country)

        self.define_holiday() \
            .with_name("Reformationstag") \
            .since(2018) \
            .on("10-31") \
            .with_flags("RF")
