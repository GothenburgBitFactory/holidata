from holidata.holiday import Region
from holidata.utils import day, date


class CE(Region):
    def __init__(self, country):
        super().__init__("CE", country)

        self.define_holiday() \
            .with_name("Lunes siguiente a la Epifanía del Señor") \
            .in_years([2013, 2019]) \
            .on(date(month=1, day=7)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Nuestra Señora de África") \
            .in_years([2022, 2023, 2024, 2025, 2026]) \
            .on(date(month=8, day=5)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Día de Ceuta") \
            .in_years([2016, 2017, 2019, 2020, 2021, 2022, 2023, 2026]) \
            .on(date(month=9, day=2)) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Fiesta del Sacrificio (Eidul Adha)") \
            .except_for([2011]) \
            .on(CE.day_of_eidul_adha) \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Lunes siguiente a la Fiesta del Sacrificio (Eidul Adha)") \
            .in_years([2011]) \
            .on(date(month=11, day=7)) \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Jueves Santo") \
            .on(day(3).before(country.easter())) \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Lunes siguiente a la Fiesta del Trabajo") \
            .in_years([2011]) \
            .on(date(month=5, day=2)) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente a la Fiesta Nacional de España") \
            .in_years([2014]) \
            .on(date(month=10, day=13)) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente a Todos los Santos") \
            .in_years([2015]) \
            .on(date(month=11, day=2)) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente al Día de la Constitución Española") \
            .in_years([2015, 2020]) \
            .on(date(month=12, day=7)) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Lunes siguiente a La Inmaculada Concepción") \
            .in_years([2013]) \
            .on(date(month=12, day=9)) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("San Esteban") \
            .in_years([2011, 2016]) \
            .on(date(month=12, day=26)) \
            .with_flags("RF")

    @staticmethod
    def day_of_eidul_adha(year):
        dates = {
            2012: date(10, 27),
            2013: date(10, 15),
            2014: date(10, 6),
            2015: date(9, 25),
            2016: date(9, 12),
            2017: date(9, 1),
            2018: date(8, 22),
            2019: date(8, 12),
            2020: date(7, 31),
            2021: date(7, 20),
            2022: date(7, 9),
            2023: date(6, 29),
            2024: date(6, 17),
            2025: date(6, 6),
            2026: date(5, 27),
        }

        return dates.get(year)(year) if year in dates else None
