from holidata.holiday import Region
from holidata.utils import Month, date


class NI(Region):
    def __init__(self, country):
        super().__init__("NI", country)

        self.define_holiday() \
            .with_name("Reformationstag") \
            .since(2018) \
            .on(date(Month.OCTOBER, 31)) \
            .with_flags("RF")
