from holidata.holidays.holidays import Region


class CB(Region):
    def __init__(self, country):
        super().__init__("CB", country)

        self.define_holiday() \
            .with_name("Lunes siguiente a la Epifanía del Señor") \
            .in_years([2013]) \
            .on("01-07") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Día de las Instituciones de Cantabria") \
            .in_years([2011, 2016, 2017, 2018, 2020, 2021, 2022, 2023]) \
            .on("07-28") \
            .with_flags("F")

        self.define_holiday() \
            .with_name("La Bien Aparecida") \
            .in_years([2011, 2012, 2014, 2014, 2015, 2016, 2017, 2018, 2020, 2021, 2022, 2023]) \
            .on("09-15") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Jueves Santo") \
            .in_years([2011, 2012, 2013, 2014, 2015, 2016, 2017, 2019, 2020, 2021, 2022, 2023, 2024]) \
            .on("3 days before Easter") \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Lunes de Pascua") \
            .in_years([2013, 2015, 2019, 2020, 2024]) \
            .on("1 day after Easter") \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Lunes siguiente a la Fiesta del Trabajo") \
            .in_years([2011]) \
            .on("05-02") \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Santiago Apóstol") \
            .in_years([2012, 2013, 2014, 2019]) \
            .on("07-25") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Santiago Apóstol / Día Nacional de Galicia") \
            .in_years([2024]) \
            .on("07-25") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Lunes siguiente a Todos los Santos") \
            .in_years([2015]) \
            .on("11-02") \
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
