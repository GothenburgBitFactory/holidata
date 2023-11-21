from holidata.holidays.holidays import Region


class EX(Region):
    def __init__(self, country):
        super().__init__("EX", country)

        self.define_holiday() \
            .with_name("Lunes siguiente a la Epifanía del Señor") \
            .in_years([2013, 2019]) \
            .on("01-07") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Martes de Carnaval") \
            .in_years([2023, 2024]) \
            .on("47 days before Easter") \
            .with_flags("V")

        self.define_holiday() \
            .with_name("Lunes siguiente a San José") \
            .in_years([2017]) \
            .on("03-20") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Día de Extremadura") \
            .except_for([2019, 2024]) \
            .on("09-08") \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente al Día de Extremadura") \
            .in_years([2013, 2019]) \
            .on("09-09") \
            .with_flags("F")

        self.define_holiday() \
            .with_name("San José") \
            .in_years([2021]) \
            .on("03-19") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Lunes siguiente a la Fiesta Nacional de España") \
            .in_years([2014]) \
            .on("10-13") \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente a Todos los Santos") \
            .in_years([2015, 2020]) \
            .on("11-02") \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente al Día de la Constitución Española") \
            .in_years([2015, 2020]) \
            .on("12-07") \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente a La Inmaculada Concepción") \
            .in_years([2013, 2019, 2024]) \
            .on("12-09") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Jueves Santo") \
            .on("3 days before Easter") \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Lunes siguiente a la Fiesta del Trabajo") \
            .in_years([2011, 2016, 2022]) \
            .on("05-02") \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente a la Natividad del Señor") \
            .in_years([2022]) \
            .on("12-26") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("San Esteban") \
            .in_years([2011, 2016]) \
            .on("12-26") \
            .with_flags("RF")
