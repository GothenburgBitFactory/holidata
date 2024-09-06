from holidata.holiday import Region
from holidata.utils import date


class SH(Region):
    def __init__(self, country):
        super().__init__("SH", country)

        self.define_holiday() \
            .with_name("Reformationstag") \
            .since(2018) \
            .on(date(month=10, day=31)) \
            .with_flags("RF")
