from holidata.holiday import Country, Region
from holidata.utils import Month, date, dates, day


class ML(Region):
    def __init__(self, country: Country) -> None:
        super().__init__("ML", country)

        self.define_holiday() \
            .with_name("Lunes siguiente al Año Nuevo") \
            .in_years([2017]) \
            .on(date(Month.JANUARY, 2)) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente a la Epifanía del Señor") \
            .in_years([2013, 2019]) \
            .on(date(Month.JANUARY, 7)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Estatuto de Autonomía de la Ciudad de Melilla") \
            .in_years([2020, 2021]) \
            .on(date(Month.MARCH, 13)) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Fiesta del Eid Fitr") \
            .on(dates({
                2022: (Month.MAY, 3),
                2023: (Month.APRIL, 21),
                2025: (Month.MARCH, 31),
                2026: (Month.MARCH, 20),
            })) \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Fiesta del Sacrificio (Aid Al Adha)") \
            .on(dates({
                2022: (Month.JULY, 11),
                2023: (Month.JUNE, 29),
                2024: (Month.JUNE, 17),
                2025: (Month.JUNE, 6),
                2026: (Month.MAY, 27),
            })) \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Fiesta del Sacrificio (Aid El Kebir)") \
            .on(dates({
                2011: (Month.NOVEMBER, 7),
                2012: (Month.OCTOBER, 26),
                2013: (Month.OCTOBER, 15),
                2014: (Month.OCTOBER, 4),
                2015: (Month.SEPTEMBER, 25),
                2016: (Month.SEPTEMBER, 12),
                2017: (Month.SEPTEMBER, 1),
                2018: (Month.AUGUST, 22),
                2019: (Month.AUGUST, 12),
                2020: (Month.JULY, 31),
                2021: (Month.JULY, 21),
            })) \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("San José") \
            .in_years([2011, 2012, 2013, 2014, 2015, 2016]) \
            .on(date(Month.MARCH, 19)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Jueves Santo") \
            .on(day(3).before(country.easter())) \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Lunes siguiente al Día de la Constitución Española") \
            .in_years([2015, 2020, 2026]) \
            .on(date(Month.DECEMBER, 7)) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente a La Inmaculada Concepción") \
            .in_years([2019, 2024]) \
            .on(date(Month.DECEMBER, 9)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Lunes siguiente a la Natividad del Señor") \
            .in_years([2022]) \
            .on(date(Month.DECEMBER, 26)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("San Esteban") \
            .in_years([2011, 2016]) \
            .on(date(Month.DECEMBER, 26)) \
            .with_flags("RF")
