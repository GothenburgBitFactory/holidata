from holidata.holidays.holidays import Region


class VC(Region):
    def __init__(self, country):
        super().__init__("VC", country)

        self.define_holiday() \
            .with_name("Lunes de Fallas") \
            .in_years([2013]) \
            .on("03-18") \
            .with_flags("F")

        self.define_holiday() \
            .with_name("San Juan") \
            .in_years([2019, 2020, 2021, 2022, 2023, 2024]) \
            .on("06-24") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Día de la Comunitat Valenciana") \
            .except_for([2011, 2016, 2022]) \
            .on("10-09") \
            .with_flags("F")

        self.define_holiday() \
            .with_name("San José") \
            .in_years([2011, 2012, 2013, 2014, 2015, 2016, 2018, 2019, 2020, 2021, 2022, 2024]) \
            .on("03-19") \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Jueves Santo") \
            .in_years([2011, 2016, 2017, 2022, 2023]) \
            .on("3 days before Easter") \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Lunes de Pascua") \
            .except_for([2023]) \
            .on("1 day after Easter") \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Lunes siguiente a la Fiesta del Trabajo") \
            .in_years([2011]) \
            .on("05-02") \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente al Día de la Constitución Española") \
            .in_years([2015]) \
            .on("12-07") \
            .with_flags("F")

        self.define_holiday() \
            .with_name("San Esteban") \
            .in_years([2016]) \
            .on("12-26") \
            .with_flags("RF")
