from holidata.holiday import Country, Region
from holidata.utils import Month, date, day


class CB(Region):
    def __init__(self, country: Country) -> None:
        super().__init__("CB", country)

        self.define_holiday() \
            .with_name("Lunes siguiente a la Epifanía del Señor") \
            .in_years([2013]) \
            .on(date(Month.JANUARY, 7)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Día de las Instituciones de Cantabria") \
            .in_years([2011, 2016, 2017, 2018, 2020, 2021, 2022, 2023, 2025, 2026]) \
            .on(date(Month.JULY, 28)) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("La Bien Aparecida") \
            .in_years([2011, 2012, 2014, 2014, 2015, 2016, 2017, 2018, 2020, 2021, 2022, 2023, 2025, 2026]) \
            .on(date(Month.SEPTEMBER, 15)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Jueves Santo") \
            .in_years([2011, 2012, 2013, 2014, 2015, 2016, 2017, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026]) \
            .on(day(3).before(country.easter())) \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Lunes de Pascua") \
            .in_years([2013, 2015, 2019, 2020, 2024]) \
            .on(day(1).after(country.easter())) \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Lunes siguiente a la Fiesta del Trabajo") \
            .in_years([2011]) \
            .on(date(Month.MAY, 2)) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Santiago Apóstol") \
            .in_years([2012, 2013, 2014, 2019]) \
            .on(date(Month.JULY, 25)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Santiago Apóstol / Día Nacional de Galicia") \
            .in_years([2024]) \
            .on(date(Month.JULY, 25)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Lunes siguiente a Todos los Santos") \
            .in_years([2015]) \
            .on(date(Month.NOVEMBER, 2)) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente al Día de la Constitución Española") \
            .in_years([2026]) \
            .on(date(Month.DECEMBER, 7)) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente a La Inmaculada Concepción") \
            .in_years([2019]) \
            .on(date(Month.DECEMBER, 9)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Lunes siguiente a la Natividad del Señor") \
            .in_years([2022]) \
            .on(date(Month.DECEMBER, 26)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("San Esteban") \
            .in_years([2016]) \
            .on(date(Month.DECEMBER, 26)) \
            .with_flags("RF")
