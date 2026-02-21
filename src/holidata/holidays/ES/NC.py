from holidata.holiday import Region
from holidata.utils import Month, date, day


class NC(Region):
    def __init__(self, country):
        super().__init__("NC", country)

        self.define_holiday() \
            .with_name("Lunes siguiente a la Epifanía del Señor") \
            .in_years([2013, 2019]) \
            .on(date(Month.JANUARY, 7)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("San José") \
            .in_years([2012, 2014, 2015, 2019, 2020, 2021, 2026]) \
            .on(date(Month.MARCH, 19)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Santiago Apóstol / Día Nacional de Galicia") \
            .in_years([2023, 2024, 2025]) \
            .on(date(Month.JULY, 25)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Jueves Santo") \
            .on(day(3).before(country.easter())) \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Lunes de Pascua") \
            .on(day(1).after(country.easter())) \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Santiago Apóstol") \
            .in_years([2011, 2013, 2015, 2016, 2017, 2022]) \
            .on(date(Month.JULY, 25)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Lunes siguiente a Todos los Santos") \
            .in_years([2026]) \
            .on(date(Month.NOVEMBER, 2)) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente al Día de la Constitución Española") \
            .in_years([2020]) \
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
