from holidata.holidays.holidays import Region
from holidata.utils import SmartDayArrow


class SN(Region):
    def __init__(self, country):
        super().__init__("SN", country)

        """
        11 days before 4. sunday before 12-25: Buß- und Bettag
        """
        self.define_holiday() \
            .with_name("Buß- und Bettag") \
            .on(self.buss_und_bettag) \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Reformationstag") \
            .until(2016) \
            .on("10-31") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Reformationstag") \
            .since(2018) \
            .on("10-31") \
            .with_flags("RF")


    @staticmethod
    def buss_und_bettag(year):
        return SmartDayArrow(year, 12, 25).shift_to_weekday("sunday", order=4, reverse=True).shift(days=-11)
