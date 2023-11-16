from holidata.holidays.holidays import Region


class GA(Region):
    def __init__(self, country):
        super().__init__("GA", country)

        self.define_holiday() \
            .with_name("San Juan") \
            .in_years([2013, 2016, 2020, 2022]) \
            .on("06-24") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("San José") \
            .in_years([2011, 2019, 2020, 2021]) \
            .on("03-19") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Día siguiente a San José") \
            .in_years([2015]) \
            .on("03-20") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Día de las Letras Gallegas") \
            .except_for([2015, 2020]) \
            .on("05-17") \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Santiago Apóstol / Día Nacional de Galicia") \
            .except_for([2021]) \
            .on("07-25") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Lunes siguiente a Todos los Santos") \
            .in_years([2015]) \
            .on("11-02") \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Jueves Santo") \
            .on("3 days before Easter") \
            .with_flags("RV")
