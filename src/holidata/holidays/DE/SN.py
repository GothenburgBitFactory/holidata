from holidata.holiday import Region
from holidata.utils import day, fourth


class SN(Region):
    def __init__(self, country):
        super().__init__("SN", country)

        """
        11 days before 4. sunday before 12-25: Buß- und Bettag
        """
        self.define_holiday() \
            .with_name("Buß- und Bettag") \
            .on(day(11).before(fourth("sunday").before(month=12, day=25))) \
            .with_flags("RV")

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
