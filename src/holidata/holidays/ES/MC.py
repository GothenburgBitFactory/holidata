from holidata.holidays.holidays import Region
from holidata.utils import SmartDayArrow


class MC(Region):
    def __init__(self, country):
        super().__init__("MC", country)

        self.define_holiday() \
            .with_name("Lunes siguiente al Año Nuevo") \
            .in_years([2017, 2023]) \
            .on("01-02") \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente a la Epifanía del Señor") \
            .in_years([2013, 2019]) \
            .on("01-07") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Día de la Región de Murcia") \
            .except_for([2013, 2024]) \
            .on(self.dia_de_la_region_de_murcia) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("San José") \
            .in_years([2011, 2012, 2013, 2014, 2015, 2016, 2018, 2019, 2020, 2021, 2024]) \
            .on("03-19") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Lunes siguiente a La Inmaculada Concepción") \
            .in_years([2013, 2024]) \
            .on("12-09") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Jueves Santo") \
            .on("3 days before Easter") \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Lunes de Pascua") \
            .in_years([2023]) \
            .on("1 day after Easter") \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Lunes siguiente a la Fiesta del Trabajo") \
            .in_years([2011, 2022]) \
            .on("05-02") \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente al Día de la Constitución Española") \
            .in_years([2015, 2020]) \
            .on("12-07") \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente a la Natividad del Señor") \
            .in_years([2022]) \
            .on("12-26") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("San Esteban") \
            .in_years([2016]) \
            .on("12-26") \
            .with_flags("RF")

    @staticmethod
    def dia_de_la_region_de_murcia(year):
        if year == 2019:
            return SmartDayArrow(year, 6, 10)
        else:
            return SmartDayArrow(year, 6, 9)
