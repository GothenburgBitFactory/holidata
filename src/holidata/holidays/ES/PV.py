from holidata.holiday import Region
from holidata.utils import day


class PV(Region):
    def __init__(self, country):
        super().__init__("PV", country)

        self.define_holiday() \
            .with_name("V Centenario Vuelta al Mundo") \
            .in_years([2022]) \
            .on(month=9, day=6) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("80º aniversario del primer Gobierno Vasco") \
            .in_years([2016]) \
            .on(month=10, day=7) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Día del País Vasco-Euskadiko Eguna") \
            .in_years([2011, 2012, 2013, 2014]) \
            .on(month=10, day=25) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("San José") \
            .in_years([2015, 2019, 2020, 2021, 2026]) \
            .on(month=3, day=19) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Jueves Santo") \
            .on(day(3).before(country.easter())) \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Lunes de Pascua") \
            .except_for([2012]) \
            .on(day(1).after(country.easter())) \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Santiago Apóstol") \
            .in_years([2011, 2013, 2015, 2016, 2017, 2019, 2020, 2022]) \
            .on(month=7, day=25) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Santiago Apóstol / Día Nacional de Galicia") \
            .in_years([2023, 2024, 2025, 2026]) \
            .on(month=7, day=25) \
            .with_flags("RF")

