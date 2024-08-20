from holidata.holiday import Region


class TH(Region):
    def __init__(self, country):
        super().__init__("TH", country)

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
