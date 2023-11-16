from holidata.holidays.holidays import Region


class MD(Region):
    def __init__(self, country):
        super().__init__("MD", country)

        self.define_holiday() \
            .with_name("Lunes siguiente a la Epifanía del Señor") \
            .in_years([2013, 2019]) \
            .on("01-07") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Traslado de San José") \
            .in_years([2013]) \
            .on("03-18") \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente a San José") \
            .in_years([2017, 2023]) \
            .on("03-20") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Fiesta de la Comunidad de Madrid") \
            .except_for([2016, 2021]) \
            .on("05-02") \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente al Día de la Comunidad de Madrid") \
            .in_years([2021]) \
            .on("05-03") \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Corpus Christi") \
            .in_years([2011, 2014, 2015]) \
            .on("60 days after Easter") \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("San José") \
            .in_years([2012, 2015, 2021, 2023]) \
            .on("03-19") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Jueves Santo") \
            .on("3 days before Easter") \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Lunes siguiente a la Fiesta del Trabajo") \
            .in_years([2016]) \
            .on("05-02") \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Santiago Apóstol") \
            .in_years([2011, 2016, 2022]) \
            .on("07-25") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Santiago Apóstol / Día Nacional de Galicia") \
            .in_years([2024]) \
            .on("07-25") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Lunes siguiente a Todos los Santos") \
            .in_years([2020]) \
            .on("11-02") \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente al Día de la Constitución Española") \
            .in_years([2020]) \
            .on("12-07") \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente a La Inmaculada Concepción") \
            .in_years([2019]) \
            .on("12-09") \
            .with_flags("RF")

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
