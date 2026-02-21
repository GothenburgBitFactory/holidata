from holidata.holiday import Country, Region
from holidata.utils import Month, date


class BB(Region):
    """

    """
    def __init__(self, country: Country) -> None:
        super().__init__("BB", country)

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
