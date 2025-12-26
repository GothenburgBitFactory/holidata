from holidata.holiday import Region
from holidata.utils import day, date, Month


class ML(Region):
    def __init__(self, country):
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
            .in_years([2022, 2023, 2025, 2026]) \
            .on(ML.day_of_eid_fitr) \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Fiesta del Sacrificio (Aid Al Adha)") \
            .in_years([2022, 2023, 2024, 2025, 2026]) \
            .on(ML.holiday_aid_al_adha) \
            .with_flags("RV")

        self.define_holiday() \
            .with_name("Fiesta del Sacrificio (Aid El Kebir)") \
            .until(2021) \
            .on(ML.holiday_aid_el_kebir) \
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

    @staticmethod
    def holiday_aid_el_kebir(year):
        dates = {
            2011: date(Month.NOVEMBER, 7),
            2012: date(Month.OCTOBER, 26),
            2013: date(Month.OCTOBER, 15),
            2014: date(Month.OCTOBER, 4),
            2015: date(Month.SEPTEMBER, 25),
            2016: date(Month.SEPTEMBER, 12),
            2017: date(Month.SEPTEMBER, 1),
            2018: date(Month.AUGUST, 22),
            2019: date(Month.AUGUST, 12),
            2020: date(Month.JULY, 31),
            2021: date(Month.JULY, 21),
        }
        return dates.get(year)(year) if year in dates else None

    @staticmethod
    def holiday_aid_al_adha(year):
        dates = {
            2022: date(Month.JULY, 11),
            2023: date(Month.JUNE, 29),
            2024: date(Month.JUNE, 17),
            2025: date(Month.JUNE, 6),
            2026: date(Month.MAY, 27),
        }
        return dates.get(year)(year) if year in dates else None

    @staticmethod
    def day_of_eid_fitr(year):
        dates = {
            2022: date(Month.MAY, 3),
            2023: date(Month.APRIL, 21),
            2025: date(Month.MARCH, 31),
            2026: date(Month.MARCH, 20),
        }
        return dates.get(year)(year) if year in dates else None
