from holidata.holidays.holidays import Region
from holidata.utils import SmartDayArrow


class ML(Region):
    def __init__(self, country):
        super().__init__("ML", country)

        self.define_holiday() \
            .with_name("Lunes siguiente al Año Nuevo") \
            .in_years([2017]) \
            .on("01-02") \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente a la Epifanía del Señor") \
            .in_years([2013, 2019]) \
            .on("01-07") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Estatuto de Autonomía de la Ciudad de Melilla") \
            .in_years([2020, 2021]) \
            .on("03-13") \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Fiesta del Eid Fitr") \
            .in_years([2022, 2023]) \
            .on(self.day_of_eid_fitr) \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Fiesta del Sacrificio (Aid Al Adha)") \
            .in_years([2022, 2023, 2024]) \
            .on(self.holiday_aid_al_adha) \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Fiesta del Sacrificio (Aid El Kebir)") \
            .until(2021) \
            .on(self.holiday_aid_el_kebir) \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("San José") \
            .in_years([2011, 2012, 2013, 2014, 2015, 2016]) \
            .on("03-19") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Jueves Santo") \
            .on("3 days before Easter") \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Lunes siguiente al Día de la Constitución Española") \
            .in_years([2015, 2020]) \
            .on("12-07") \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente a La Inmaculada Concepción") \
            .in_years([2019, 2024]) \
            .on("12-09") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Lunes siguiente a la Natividad del Señor") \
            .in_years([2022]) \
            .on("12-26") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("San Esteban") \
            .in_years([2011, 2016]) \
            .on("12-26") \
            .with_flags("RF")

    @staticmethod
    def holiday_aid_el_kebir(year):
        dates = {
            2011: SmartDayArrow(year, 11, 7),
            2012: SmartDayArrow(year, 10, 26),
            2013: SmartDayArrow(year, 10, 15),
            2014: SmartDayArrow(year, 10, 4),
            2015: SmartDayArrow(year, 9, 25),
            2016: SmartDayArrow(year, 9, 12),
            2017: SmartDayArrow(year, 9, 1),
            2018: SmartDayArrow(year, 8, 22),
            2019: SmartDayArrow(year, 8, 12),
            2020: SmartDayArrow(year, 7, 31),
            2021: SmartDayArrow(year, 7, 21),
        }
        return dates[year]

    @staticmethod
    def holiday_aid_al_adha(year):
        dates = {
            2022: SmartDayArrow(year, 7, 11),
            2023: SmartDayArrow(year, 6, 29),
            2024: SmartDayArrow(year, 6, 17),
        }
        return dates[year]

    @staticmethod
    def day_of_eid_fitr(year):
        dates = {
            2022: SmartDayArrow(year, 5, 3),
            2023: SmartDayArrow(year, 4, 21),
        }
        return dates[year]
