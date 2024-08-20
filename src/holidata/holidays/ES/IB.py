from holidata.holiday import Region
from holidata.utils import day


class IB(Region):
    def __init__(self, country):
        super().__init__("IB", country)

        self.define_holiday() \
            .with_name("Día de las Illes Balears") \
            .in_years([2011, 2012, 2013, 2014, 2016, 2017, 2018, 2019, 2021, 2022, 2023, 2024]) \
            .on(month=3, day=1) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Jueves Santo") \
            .on(day(3).before(country.easter())) \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Lunes de Pascua") \
            .except_for([2014]) \
            .on(day(1).after(country.easter())) \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Lunes siguiente a Todos los Santos") \
            .in_years([2015]) \
            .on(month=11, day=2) \
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
            .in_years([2011, 2013, 2014, 2016, 2019, 2020]) \
            .on(month=12, day=26) \
            .with_flags("RF")
