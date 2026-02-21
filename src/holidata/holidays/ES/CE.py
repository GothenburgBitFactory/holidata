from holidata.holiday import Country, Region
from holidata.utils import Month, date, dates, day


class CE(Region):
    def __init__(self, country: Country) -> None:
        super().__init__("CE", country)

        self.define_holiday() \
            .with_name("Lunes siguiente a la Epifanía del Señor") \
            .in_years([2013, 2019]) \
            .on(date(Month.JANUARY, 7)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Nuestra Señora de África") \
            .in_years([2022, 2023, 2024, 2025, 2026]) \
            .on(date(Month.AUGUST, 5)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Día de Ceuta") \
            .in_years([2016, 2017, 2019, 2020, 2021, 2022, 2023, 2026]) \
            .on(date(Month.SEPTEMBER, 2)) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Fiesta del Sacrificio (Eidul Adha)") \
            .on(dates({
                2012: (Month.OCTOBER, 27),
                2013: (Month.OCTOBER, 15),
                2014: (Month.OCTOBER, 6),
                2015: (Month.SEPTEMBER, 25),
                2016: (Month.SEPTEMBER, 12),
                2017: (Month.SEPTEMBER, 1),
                2018: (Month.AUGUST, 22),
                2019: (Month.AUGUST, 12),
                2020: (Month.JULY, 31),
                2021: (Month.JULY, 20),
                2022: (Month.JULY, 9),
                2023: (Month.JUNE, 29),
                2024: (Month.JUNE, 17),
                2025: (Month.JUNE, 6),
                2026: (Month.MAY, 27),
            })) \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Lunes siguiente a la Fiesta del Sacrificio (Eidul Adha)") \
            .in_years([2011]) \
            .on(date(Month.NOVEMBER, 7)) \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Jueves Santo") \
            .on(day(3).before(country.easter())) \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Lunes siguiente a la Fiesta del Trabajo") \
            .in_years([2011]) \
            .on(date(Month.MAY, 2)) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente a la Fiesta Nacional de España") \
            .in_years([2014]) \
            .on(date(Month.OCTOBER, 13)) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente a Todos los Santos") \
            .in_years([2015]) \
            .on(date(Month.NOVEMBER, 2)) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente al Día de la Constitución Española") \
            .in_years([2015, 2020]) \
            .on(date(Month.DECEMBER, 7)) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente a La Inmaculada Concepción") \
            .in_years([2013]) \
            .on(date(Month.DECEMBER, 9)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("San Esteban") \
            .in_years([2011, 2016]) \
            .on(date(Month.DECEMBER, 26)) \
            .with_flags("RF")
