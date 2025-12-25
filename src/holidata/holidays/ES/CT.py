from holidata.holiday import Region
from holidata.utils import day


class CT(Region):
    def __init__(self, country):
        super().__init__("CT", country)

        self.define_holiday() \
            .with_name("San Juan") \
            .in_years([2011, 2013, 2014, 2015, 2016, 2017, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026]) \
            .on(month=6, day=24) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Fiesta Nacional de Cataluña") \
            .except_for([2011, 2016, 2022]) \
            .on(month=9, day=11) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes de Pascua Granada") \
            .in_years([2011, 2016, 2022]) \
            .on(day(50).after(country.easter())) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes de Pascua") \
            .except_for([2018]) \
            .on(day(1).after(country.easter())) \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("San Esteban") \
            .except_for([2018, 2021]) \
            .on(month=12, day=26) \
            .with_flags("RF")
