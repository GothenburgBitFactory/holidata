from holidata.holiday import Country, Region
from holidata.utils import Month, date, day


class EX(Region):
    def __init__(self, country: Country) -> None:
        super().__init__("EX", country)

        self.define_holiday() \
            .with_name("Lunes siguiente a la Epifanía del Señor") \
            .in_years([2013, 2019]) \
            .on(date(Month.JANUARY, 7)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Martes de Carnaval") \
            .in_years([2023, 2024]) \
            .on(day(47).before(country.easter())) \
            .with_flags("V")

        self.define_holiday() \
            .with_name("Lunes siguiente a San José") \
            .in_years([2017]) \
            .on(date(Month.MARCH, 20)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Día de Extremadura") \
            .except_for([2019, 2024]) \
            .on(date(Month.SEPTEMBER, 8)) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente al Día de Extremadura") \
            .in_years([2013, 2019]) \
            .on(date(Month.SEPTEMBER, 9)) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("San José") \
            .in_years([2021]) \
            .on(date(Month.MARCH, 19)) \
            .with_flags("RF")

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
            .with_name("Lunes siguiente a la Natividad del Señor") \
            .in_years([2022]) \
            .on(date(Month.DECEMBER, 26)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("San Esteban") \
            .in_years([2011, 2016]) \
            .on(date(Month.DECEMBER, 26)) \
            .with_flags("RF")
