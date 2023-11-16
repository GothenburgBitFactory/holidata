from holidata.holidays.holidays import Region


class CM(Region):
    def __init__(self, country):
        super().__init__("CM", country)

        self.define_holiday() \
            .with_name("Lunes siguiente a la Epifanía del Señor") \
            .in_years([2013]) \
            .on("01-07") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Día de Castilla-La Mancha") \
            .except_for([2014, 2015, 2020]) \
            .on("05-31") \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Corpus Christi") \
            .in_years([2011, 2012, 2013, 2014, 2015, 2016, 2017, 2019, 2020, 2021, 2022, 2023, 2024]) \
            .on("60 days after Easter") \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("San José") \
            .in_years([2011, 2020]) \
            .on("03-19") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Jueves Santo") \
            .on("3 days before Easter") \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Lunes de Pascua") \
            .in_years([2014, 2015, 2019, 2020]) \
            .on("1 day after Easter") \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Lunes siguiente al Día de la Constitución Española") \
            .in_years([2015]) \
            .on("12-07") \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente a la Natividad del Señor") \
            .in_years([2022]) \
            .on("12-26") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("San Esteban") \
            .in_years([2016]) \
            .on("12-26") \
            .with_flags("RF")
