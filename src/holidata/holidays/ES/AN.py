from holidata.holidays.holidays import Region
from holidata.utils import SmartDayArrow


class AN(Region):
    def __init__(self, country):
        super().__init__("AN", country)

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
            .with_name("Día de Andalucía") \
            .on(self.dia_de_andalucia) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente a la Asunción de la Virgen") \
            .in_years([2021]) \
            .on("08-16") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Lunes siguiente a La Inmaculada Concepción") \
            .in_years([2013, 2019, 2024]) \
            .on("12-09") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Jueves Santo") \
            .on("3 days before Easter") \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Lunes siguiente a la Fiesta del Trabajo") \
            .in_years([2011, 2016, 2022]) \
            .on("05-02") \
            .with_flags("F")

        self.define_holiday() \
            .with_name("San Esteban") \
            .in_years([2011, 2016]) \
            .on("12-26") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Lunes siguiente a la Fiesta Nacional de España") \
            .in_years([2014]) \
            .on("10-13") \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente a Todos los Santos") \
            .in_years([2015, 2020]) \
            .on("11-02") \
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

    @staticmethod
    def dia_de_andalucia(year):
        if year == 2016:
            return SmartDayArrow(year, 2, 29)
        elif year == 2021:
            return SmartDayArrow(year, 3, 1)
        else:
            return SmartDayArrow(year, 2, 28)
