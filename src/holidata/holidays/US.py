from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import first, third, last, second, fourth, day


class US(Country):
    id = "US"
    languages = ["en", "es"]
    default_lang = "en"
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_names({
                "en": "New Year's Day",
                "es": "Año Neuvo",
            }) \
            .on(month=1, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "en": "Independence Day",
                "es": "Día de la Independiencia",
            }) \
            .on(month=7, day=4) \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "en": "Veterans Day",
                "es": "Día de los Veteranos",
            }) \
            .on(month=11, day=11) \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "en": "Christmas Eve",
                "es": "Nochebuena",
            }) \
            .on(month=12, day=24) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_names({
                "en": "Christmas Day",
                "es": "Navidad",
            }) \
            .on(month=12, day=25) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_names({
                "en": "Birthday of Martin Luther King, Jr.",
                "es": "Cumpleaños de Martin Luther King, Jr.",
            }) \
            .on(third("monday").of("January")) \
            .with_flags("NV")

        self.define_holiday() \
            .with_names({
                "en": "Washington's Birthday",
                "es": "Día del Presidente",
            }) \
            .on(third("monday").of("february")) \
            .with_flags("NV")

        self.define_holiday() \
            .with_names({
                "en": "Patriots' Day",
                "es": "Día del Patriota",
                }) \
            .in_regions(["MA", "ME"]) \
            .on(third("monday").of("april")) \
            .with_flags("V")

        self.define_holiday() \
            .with_names({
                "en": "Memorial Day",
                "es": "Día de los Caídos",
            }) \
            .on(last("monday").of("may")) \
            .with_flags("NV")

        self.define_holiday() \
            .with_names({
                "en": "Labor Day",
                "es": "Día del Trabajo",
            }) \
            .on(first("monday").of("september")) \
            .with_flags("NV")

        self.define_holiday() \
            .with_names({
                "en": "Columbus Day",
                "es": "Día de Columbus",
            }) \
            .on(second("monday").of("october")) \
            .with_flags("NV")

        self.define_holiday() \
            .with_names({
                "en": "Thanksgiving Day",
                "es": "Día de Acción de Gracias",
            }) \
            .on(fourth("thursday").of("november")) \
            .with_flags("NV")

        self.define_holiday() \
            .with_names({
                "en": "Day after Thanksgiving",
                "es": "Día después de Acción de Gracias",
            }) \
            .on(day(1).after(fourth("thursday").of("november"))) \
            .with_flags("NV")
