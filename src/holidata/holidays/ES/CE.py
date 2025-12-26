from holidata.holiday import Region
from holidata.utils import day, date, Month


class CE(Region):
    def __init__(self, country):
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
            .except_for([2011]) \
            .on(CE.day_of_eidul_adha) \
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

    @staticmethod
    def day_of_eidul_adha(year):
        dates = {
            2012: date(Month.OCTOBER, 27),
            2013: date(Month.OCTOBER, 15),
            2014: date(Month.OCTOBER, 6),
            2015: date(Month.SEPTEMBER, 25),
            2016: date(Month.SEPTEMBER, 12),
            2017: date(Month.SEPTEMBER, 1),
            2018: date(Month.AUGUST, 22),
            2019: date(Month.AUGUST, 12),
            2020: date(Month.JULY, 31),
            2021: date(Month.JULY, 20),
            2022: date(Month.JULY, 9),
            2023: date(Month.JUNE, 29),
            2024: date(Month.JUNE, 17),
            2025: date(Month.JUNE, 6),
            2026: date(Month.MAY, 27),
        }

        return dates.get(year)(year) if year in dates else None
