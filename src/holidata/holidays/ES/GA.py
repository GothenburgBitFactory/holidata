from holidata.holiday import Region
from holidata.utils import day


class GA(Region):
    def __init__(self, country):
        super().__init__("GA", country)

        self.define_holiday() \
            .with_name("San Juan") \
            .in_years([2013, 2016, 2020, 2022, 2026]) \
            .on(month=6, day=24) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("San José") \
            .in_years([2011, 2019, 2020, 2021, 2026]) \
            .on(month=3, day=19) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Día siguiente a San José") \
            .in_years([2015]) \
            .on(month=3, day=20) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Día de las Letras Gallegas") \
            .except_for([2015, 2020]) \
            .on(month=5, day=17) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Santiago Apóstol / Día Nacional de Galicia") \
            .except_for([2021]) \
            .on(month=7, day=25) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Lunes siguiente a Todos los Santos") \
            .in_years([2015]) \
            .on(month=11, day=2) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Jueves Santo") \
            .on(day(3).before(country.easter())) \
            .with_flags("RV")
