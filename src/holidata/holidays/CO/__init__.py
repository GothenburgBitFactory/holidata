from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import day, first, date, Weekday, Month

__all__ = [
    "CO",
]


class CO(Country):
    id = "CO"
    languages = ["es"]
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Año Nuevo") \
            .on(date(Month.JANUARY, 1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Día del Trabajo") \
            .on(date(Month.MAY, 1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Grito de Independencia") \
            .on(date(Month.JULY, 20)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Batalla de Boyacá") \
            .on(date(Month.AUGUST, 7)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Inmaculada Concepción") \
            .on(date(Month.DECEMBER, 8)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Navidad") \
            .on(date(Month.DECEMBER, 25)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Jueves Santo") \
            .on(day(3).before(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Viernes Santo") \
            .on(day(2).before(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Domingo de Pascua") \
            .on(self.easter()) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("La Ascensión del Señor") \
            .on(day(43).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Corpus Christi") \
            .on(day(64).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("El Sagrado Corazón de Jesús") \
            .on(day(71).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Día de los Reyes Magos") \
            .on(first(Weekday.MONDAY).after(date(Month.JANUARY, 6), including=True)) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Día de San José") \
            .on(first(Weekday.MONDAY).after(date(Month.MARCH, 19), including=True)) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("San Pedro y San Pablo") \
            .on(first(Weekday.MONDAY).after(date(Month.JUNE, 29), including=True)) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Asunción de la Virgen") \
            .on(first(Weekday.MONDAY).after(date(Month.AUGUST, 15), including=True)) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Día de la Raza") \
            .on(first(Weekday.MONDAY).after(date(Month.OCTOBER, 12), including=True)) \
            .with_flags("NV")

        self.define_holiday() \
            .with_name("Todos los Santos") \
            .on(first(Weekday.MONDAY).after(date(Month.NOVEMBER, 1), including=True)) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Independencia de Cartagena") \
            .on(first(Weekday.MONDAY).after(date(Month.NOVEMBER, 11), including=True)) \
            .with_flags("NV")
