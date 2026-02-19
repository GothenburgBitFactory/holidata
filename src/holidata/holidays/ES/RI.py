from holidata.holiday import Region
from holidata.utils import day, date, Month, dates


class RI(Region):
    def __init__(self, country):
        super().__init__("RI", country)

        self.define_holiday() \
            .with_name("Día de La Rioja") \
            .on(date(Month.JUNE, 9).except_for({
                2013: (Month.JUNE, 10),
                2019: (Month.JUNE, 10),
            })) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente al Día de La Rioja") \
            .in_years([2024]) \
            .on(date(Month.JUNE, 10)) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("San José") \
            .in_years([2012]) \
            .on(date(Month.MARCH, 19)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Jueves Santo") \
            .in_years([2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2024, 2025, 2026]) \
            .on(day(3).before(country.easter())) \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Lunes de Pascua") \
            .except_for([2012, 2018]) \
            .on(day(1).after(country.easter())) \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Santiago Apóstol") \
            .in_years([2011, 2016]) \
            .on(date(Month.JULY, 25)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Lunes siguiente al Día de la Constitución Española") \
            .in_years([2015, 2020, 2026]) \
            .on(date(Month.DECEMBER, 7)) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente a La Inmaculada Concepción") \
            .in_years([2013, 2019]) \
            .on(date(Month.DECEMBER, 9)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Lunes siguiente a la Natividad del Señor") \
            .in_years([2022]) \
            .on(date(Month.DECEMBER, 26)) \
            .with_flags("RF")
