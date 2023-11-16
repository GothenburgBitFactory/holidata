from holidata.holidays.holidays import Region
from holidata.utils import SmartDayArrow


class RI(Region):
    def __init__(self, country):
        super().__init__("RI", country)

        self.define_holiday() \
            .with_name("Día de La Rioja") \
            .on(self.dia_de_la_rioja) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente al Día de La Rioja") \
            .in_years([2024]) \
            .on("06-10") \
            .with_flags("F")

        self.define_holiday() \
            .with_name("San José") \
            .in_years([2012]) \
            .on("03-19") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Jueves Santo") \
            .in_years([2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2024]) \
            .on("3 days before Easter") \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Lunes de Pascua") \
            .except_for([2012, 2018]) \
            .on("1 day after Easter") \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Santiago Apóstol") \
            .in_years([2011, 2016]) \
            .on("07-25") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Lunes siguiente al Día de la Constitución Española") \
            .in_years([2015, 2020]) \
            .on("12-07") \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente a La Inmaculada Concepción") \
            .in_years([2013, 2019]) \
            .on("12-09") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Lunes siguiente a la Natividad del Señor") \
            .in_years([2022]) \
            .on("12-26") \
            .with_flags("RF")

    @staticmethod
    def dia_de_la_rioja(year):
        if year in [2013, 2019]:
            return SmartDayArrow(year, 6, 10)
        else:
            return SmartDayArrow(year, 6, 9)
