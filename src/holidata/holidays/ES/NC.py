from holidata.holidays.holidays import Region


class NC(Region):
    def __init__(self, country):
        super().__init__("NC", country)

        self.define_holiday() \
            .with_name("Lunes siguiente a la Epifanía del Señor") \
            .in_years([2013, 2019]) \
            .on("01-07") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("San José") \
            .in_years([2012, 2014, 2015, 2019, 2020, 2021]) \
            .on("03-19") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Santiago Apóstol / Día Nacional de Galicia") \
            .in_years([2023, 2024]) \
            .on("07-25") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Jueves Santo") \
            .on("3 days before Easter") \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Lunes de Pascua") \
            .on("1 day after Easter") \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Santiago Apóstol") \
            .in_years([2011, 2013, 2015, 2016, 2017, 2022]) \
            .on("07-25") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Lunes siguiente al Día de la Constitución Española") \
            .in_years([2020]) \
            .on("12-07") \
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
