from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import day, first

__all__ = [
    "CO",
]


class CO(Country):
    id = "CO"
    languages = ["es"]
    default_lang = "es"
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Año Nuevo") \
            .on(month=1, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Día del Trabajo") \
            .on(month=5, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Grito de Independencia") \
            .on(month=7, day=20) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Batalla de Boyacá") \
            .on(month=8, day=7) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Inmaculada Concepción") \
            .on(month=12, day=8) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Navidad") \
            .on(month=12, day=25) \
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
            .on(first("monday").after(month=1, day=6, including=True)) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Día de San José") \
            .on(first("monday").after(month=3, day=19, including=True)) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("San Pedro y San Pablo") \
            .on(first("monday").after(month=6, day=29, including=True)) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Asunción de la Virgen") \
            .on(first("monday").after(month=8, day=15, including=True)) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Día de la Raza") \
            .on(first("monday").after(month=10, day=12, including=True)) \
            .with_flags("NV")

        self.define_holiday() \
            .with_name("Todos los Santos") \
            .on(first("monday").after(month=11, day=1, including=True)) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Independencia de Cartagena") \
            .on(first("monday").after(month=11, day=11, including=True)) \
            .with_flags("NV")
