from holidata.holiday import Region
from holidata.utils import date


class ST(Region):
    def __init__(self, country):
        super().__init__("ST", country)

        self.define_holiday() \
            .with_name("Heilige drei Könige") \
            .on(date(month=1, day=6)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Reformationstag") \
            .until(2016) \
            .on(date(month=10, day=31)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Reformationstag") \
            .since(2018) \
            .on(date(month=10, day=31)) \
            .with_flags("RF")
