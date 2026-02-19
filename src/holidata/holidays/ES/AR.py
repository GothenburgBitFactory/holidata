from holidata.holiday import Region
from holidata.utils import day, date, Month, dates


class AR(Region):
    def __init__(self, country):
        super().__init__("AR", country)

        self.define_holiday() \
            .with_name("Lunes siguiente al Año Nuevo") \
            .in_years([2017, 2023]) \
            .on(date(Month.JANUARY, 2)) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente a la Epifanía del Señor") \
            .in_years([2013, 2019]) \
            .on(date(Month.JANUARY, 7)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("San Jorge / Día de Aragón") \
            .on(date(Month.APRIL, 23).except_for({2017: (Month.APRIL, 24)})) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Lunes siguiente a San Jorge / Día de Aragón") \
            .in_years([2023]) \
            .on(date(Month.APRIL, 24)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Lunes siguiente a la Asunción de la Virgen") \
            .in_years([2021]) \
            .on(date(Month.AUGUST, 16)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Lunes siguiente a La Inmaculada Concepción") \
            .in_years([2013, 2019, 2024]) \
            .on(date(Month.DECEMBER, 9)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Jueves Santo") \
            .on(day(3).before(country.easter())) \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Lunes siguiente a la Fiesta del Trabajo") \
            .in_years([2011, 2016, 2022]) \
            .on(date(Month.MAY, 2)) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente a la Fiesta Nacional de España") \
            .in_years([2014, 2025]) \
            .on(date(Month.OCTOBER, 13)) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente a Todos los Santos") \
            .in_years([2015, 2020, 2026]) \
            .on(date(Month.NOVEMBER, 2)) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente al Día de la Constitución Española") \
            .in_years([2015, 2020, 2026]) \
            .on(date(Month.DECEMBER, 7)) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente a la Natividad del Señor") \
            .in_years([2022]) \
            .on(date(Month.DECEMBER, 26)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("San Esteban") \
            .in_years([2011, 2016]) \
            .on(date(Month.DECEMBER, 26)) \
            .with_flags("RF")
