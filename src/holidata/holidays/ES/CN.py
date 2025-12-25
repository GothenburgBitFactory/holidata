from holidata.holiday import Region
from holidata.utils import day


class CN(Region):
    def __init__(self, country):
        super().__init__("CN", country)

        self.define_holiday() \
            .with_name("Lunes siguiente a la Epifanía del Señor") \
            .in_years([2013, 2019]) \
            .on(month=1, day=7) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Día de Canarias") \
            .except_for([2021]) \
            .on(month=5, day=30) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Jueves Santo") \
            .on(day(3).before(country.easter())) \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Lunes de Pascua") \
            .in_years([2022]) \
            .on(day(1).after(country.easter())) \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Lunes siguiente a la Fiesta del Trabajo") \
            .in_years([2016]) \
            .on(month=5, day=2) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente a la Asunción de la Virgen") \
            .in_years([2021]) \
            .on(month=8, day=16) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Lunes siguiente a Todos los Santos") \
            .in_years([2015, 2026]) \
            .on(month=11, day=2) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente al Día de la Constitución Española") \
            .in_years([2020]) \
            .on(month=12, day=7) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente a la Natividad del Señor") \
            .in_years([2022]) \
            .on(month=12, day=26) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("San Esteban") \
            .in_years([2011]) \
            .on(month=12, day=26) \
            .with_flags("RF")
