from holidata.holiday import Region
from holidata.utils import Month, date


class MV(Region):
    def __init__(self, country):
        super().__init__("MV", country)

        self.define_holiday() \
            .with_name("Reformationstag") \
            .until(2016) \
            .on(date(Month.OCTOBER, 31)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Reformationstag") \
            .since(2018) \
            .on(date(Month.OCTOBER, 31)) \
            .with_flags("RF")
