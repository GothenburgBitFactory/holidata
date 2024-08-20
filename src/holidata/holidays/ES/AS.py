from holidata.holiday import Region
from holidata.utils import day


class AS(Region):
    def __init__(self, country):
        super().__init__("AS", country)

        self.define_holiday() \
            .with_name("Lunes siguiente al Año Nuevo") \
            .in_years([2017, 2023]) \
            .on(month=1, day=2) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente a la Epifanía del Señor") \
            .in_years([2013, 2019]) \
            .on(month=1, day=7) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Lunes siguiente a la Asunción de la Virgen") \
            .in_years([2021]) \
            .on(month=8, day=16) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Día de Asturias") \
            .except_for([2019]) \
            .on(month=9, day=8) \
            .with_flags("F"),

        self.define_holiday() \
            .with_name("Lunes siguiente al Día de Asturias") \
            .in_years([2013, 2019, 2024]) \
            .on(month=9, day=9) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente a Todos los Santos") \
            .in_years([2015, 2020]) \
            .on(month=11, day=2) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente a La Inmaculada Concepción") \
            .in_years([2013, 2019, 2024]) \
            .on(month=12, day=9) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Jueves Santo") \
            .on(day(3).before(country.easter())) \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Lunes siguiente a la Fiesta del Trabajo") \
            .in_years([2011, 2016, 2022]) \
            .on(month=5, day=2) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente a la Fiesta Nacional de España") \
            .in_years([2014]) \
            .on(month=10, day=13) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente al Día de la Constitución Española") \
            .in_years([2015, 2020]) \
            .on(month=12, day=7) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente a la Natividad del Señor") \
            .in_years([2022]) \
            .on(month=12, day=26) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("San Esteban") \
            .in_years([2011, 2016]) \
            .on(month=12, day=26) \
            .with_flags("RF")
