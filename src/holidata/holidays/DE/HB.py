from holidata.holiday import Region
from holidata.utils import date


class HB(Region):
    def __init__(self, country):
        super().__init__("HB", country)

        self.define_holiday() \
            .with_name("Reformationstag") \
            .since(2018) \
            .on(date(month=10, day=31)) \
            .with_flags("RF")
