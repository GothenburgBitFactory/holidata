from holidata.holidays.holidays import Region
from holidata.utils import SmartDayArrow


class CE(Region):
    def __init__(self, country):
        super().__init__("CE", country)

        self.define_holiday() \
            .with_name("Lunes siguiente a la Epifanía del Señor") \
            .in_years([2013, 2019]) \
            .on("01-07") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Nuestra Señora de África") \
            .in_years([2022, 2023, 2024]) \
            .on("08-05") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Día de Ceuta") \
            .in_years([2016, 2017, 2019, 2020, 2021, 2022, 2023]) \
            .on("09-02") \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Fiesta del Sacrificio (Eidul Adha)") \
            .except_for([2011]) \
            .on(self.day_of_eidul_adha) \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Lunes siguiente a la Fiesta del Sacrificio (Eidul Adha)") \
            .in_years([2011]) \
            .on("11-07") \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Jueves Santo") \
            .on("3 days before Easter") \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Lunes siguiente a la Fiesta del Trabajo") \
            .in_years([2011]) \
            .on("05-02") \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente a la Fiesta Nacional de España") \
            .in_years([2014]) \
            .on("10-13") \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente a Todos los Santos") \
            .in_years([2015]) \
            .on("11-02") \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente al Día de la Constitución Española") \
            .in_years([2015, 2020]) \
            .on("12-07") \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente a La Inmaculada Concepción") \
            .in_years([2013]) \
            .on("12-09") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("San Esteban") \
            .in_years([2011, 2016]) \
            .on("12-26") \
            .with_flags("RF")

    @staticmethod
    def day_of_eidul_adha(year):
        dates = {
            2012: SmartDayArrow(year, 10, 27),
            2013: SmartDayArrow(year, 10, 15),
            2014: SmartDayArrow(year, 10, 6),
            2015: SmartDayArrow(year, 9, 25),
            2016: SmartDayArrow(year, 9, 12),
            2017: SmartDayArrow(year, 9, 1),
            2018: SmartDayArrow(year, 8, 22),
            2019: SmartDayArrow(year, 8, 12),
            2020: SmartDayArrow(year, 7, 31),
            2021: SmartDayArrow(year, 7, 20),
            2022: SmartDayArrow(year, 7, 9),
            2023: SmartDayArrow(year, 6, 29),
            2024: SmartDayArrow(year, 6, 17),
        }

        return dates[year]
