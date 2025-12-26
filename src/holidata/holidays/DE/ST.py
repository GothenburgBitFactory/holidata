from holidata.holiday import Region
from holidata.utils import date, Month


class ST(Region):
    def __init__(self, country):
        super().__init__("ST", country)

        self.define_holiday() \
            .with_name("Heilige drei Könige") \
            .on(date(Month.JANUARY, 6)) \
            .with_flags("RF")

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
