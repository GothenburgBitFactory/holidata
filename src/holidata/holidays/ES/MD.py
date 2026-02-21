from holidata.holiday import Region
from holidata.utils import Month, date, day


class MD(Region):
    def __init__(self, country):
        super().__init__("MD", country)

        self.define_holiday() \
            .with_name("Lunes siguiente a la Epifanía del Señor") \
            .in_years([2013, 2019]) \
            .on(date(Month.JANUARY, 7)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Traslado de San José") \
            .in_years([2013]) \
            .on(date(Month.MARCH, 18)) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente a San José") \
            .in_years([2017, 2023]) \
            .on(date(Month.MARCH, 20)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Fiesta de la Comunidad de Madrid") \
            .except_for([2016, 2021]) \
            .on(date(Month.MAY, 2)) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente al Día de la Comunidad de Madrid") \
            .in_years([2021]) \
            .on(date(Month.MAY, 3)) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Corpus Christi") \
            .in_years([2011, 2014, 2015]) \
            .on(day(60).after(country.easter())) \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("San José") \
            .in_years([2012, 2015, 2021, 2023]) \
            .on(date(Month.MARCH, 19)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Jueves Santo") \
            .on(day(3).before(country.easter())) \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Lunes siguiente a la Fiesta del Trabajo") \
            .in_years([2016]) \
            .on(date(Month.MAY, 2)) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Santiago Apóstol") \
            .in_years([2011, 2016, 2022]) \
            .on(date(Month.JULY, 25)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Santiago Apóstol / Día Nacional de Galicia") \
            .in_years([2024, 2025]) \
            .on(date(Month.JULY, 25)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Lunes siguiente a Todos los Santos") \
            .in_years([2020, 2026]) \
            .on(date(Month.NOVEMBER, 2)) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente al Día de la Constitución Española") \
            .in_years([2020, 2026]) \
            .on(date(Month.DECEMBER, 7)) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente a La Inmaculada Concepción") \
            .in_years([2019]) \
            .on(date(Month.DECEMBER, 9)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Lunes siguiente a la Natividad del Señor") \
            .in_years([2022]) \
            .on(date(Month.DECEMBER, 26)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("San Esteban") \
            .in_years([2016]) \
            .on(date(Month.DECEMBER, 26)) \
            .with_flags("RF")
