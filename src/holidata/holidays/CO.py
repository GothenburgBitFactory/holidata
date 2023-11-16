from dateutil.easter import EASTER_WESTERN

from holidata.utils import SmartDayArrow
from .holidays import Country


class CO(Country):
    id = "CO"
    languages = ["es"]
    default_lang = "es"
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Año Nuevo") \
            .on("01-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Día del Trabajo") \
            .on("05-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Grito de Independencia") \
            .on("07-20") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Batalla de Boyacá") \
            .on("08-07") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Inmaculada Concepción") \
            .on("12-08") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Navidad") \
            .on("12-25") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Jueves Santo") \
            .on("3 days before Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Viernes Santo") \
            .on("2 days before Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Domingo de Pascua") \
            .on("Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("La Ascensión del Señor") \
            .on("43 days after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Corpus Christi") \
            .on("64 days after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("El Sagrado Corazón de Jesús") \
            .on("71 days after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Día de los Reyes Magos") \
            .on(self.first_monday_after(1, 6)) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Día de San José") \
            .on(self.first_monday_after(3, 19)) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("San Pedro y San Pablo") \
            .on(self.first_monday_after(6, 29)) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Asunción de la Virgen") \
            .on(self.first_monday_after(8, 15)) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Día de la Raza") \
            .on(self.first_monday_after(10, 12)) \
            .with_flags("NV")

        self.define_holiday() \
            .with_name("Todos los Santos") \
            .on(self.first_monday_after(11, 1)) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Independencia de Cartagena") \
            .on(self.first_monday_after(11, 11)) \
            .with_flags("NV")

    @staticmethod
    def first_monday_after(month, day):
        def wrapper(year):
            return SmartDayArrow(year, month, day).shift_to_weekday("monday", including=True)

        return wrapper
