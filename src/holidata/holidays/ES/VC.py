from holidata.holiday import Region
from holidata.utils import Month, date, day


class VC(Region):
    def __init__(self, country):
        super().__init__("VC", country)

        self.define_holiday() \
            .with_name("Lunes de Fallas") \
            .in_years([2013]) \
            .on(date(Month.MARCH, 18)) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("San Juan") \
            .in_years([2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026]) \
            .on(date(Month.JUNE, 24)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Día de la Comunitat Valenciana") \
            .except_for([2011, 2016, 2022]) \
            .on(date(Month.OCTOBER, 9)) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("San José") \
            .in_years([2011, 2012, 2013, 2014, 2015, 2016, 2018, 2019, 2020, 2021, 2022, 2024, 2025, 2026]) \
            .on(date(Month.MARCH, 19)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Jueves Santo") \
            .in_years([2011, 2016, 2017, 2022, 2023]) \
            .on(day(3).before(country.easter())) \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Lunes de Pascua") \
            .except_for([2023]) \
            .on(day(1).after(country.easter())) \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Lunes siguiente a la Fiesta del Trabajo") \
            .in_years([2011]) \
            .on(date(Month.MAY, 2)) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente al Día de la Constitución Española") \
            .in_years([2015]) \
            .on(date(Month.DECEMBER, 7)) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("San Esteban") \
            .in_years([2016]) \
            .on(date(Month.DECEMBER, 26)) \
            .with_flags("RF")
