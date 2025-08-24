from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import SmartDayArrow, first, second, third, fourth, last, day

__all__ = [
    "US",
]


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
                "en": "New Year's Day (in lieu of)",
                "es": "Año Neuvo (en lugar de)",
            }) \
            .on(month=12, day=31) \
            .on_condition(US.date_is_friday(month=12, day=31)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "en": "New Year's Day (in lieu of)",
                "es": "Año Neuvo (en lugar de)",
            }) \
            .on(month=1, day=2) \
            .on_condition(US.date_is_sunday(month=1, day=1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "en": "Juneteenth National Independence Day",
                "es": "Juneteenth – Día de la Emancipación",
            }) \
            .since(2021) \
            .on(month=6, day=19) \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "en": "Juneteenth National Independence Day (in lieu of)",
                "es": "Juneteenth – Día de la Emancipación (en lugar de)",
            }) \
            .since(2021) \
            .on(month=6, day=18) \
            .on_condition(US.date_is_saturday(month=6, day=19)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "en": "Juneteenth National Independence Day (in lieu of)",
                "es": "Juneteenth – Día de la Emancipación (en lugar de)",
            }) \
            .since(2021) \
            .on(month=6, day=20) \
            .on_condition(US.date_is_sunday(month=6, day=19)) \
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
                "en": "Independence Day (in lieu of)",
                "es": "Día de la Independiencia (en lugar de)",
            }) \
            .on(month=7, day=3) \
            .on_condition(US.date_is_saturday(month=7, day=4)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "en": "Independence Day (in lieu of)",
                "es": "Día de la Independiencia (en lugar de)",
            }) \
            .on(month=7, day=5) \
            .on_condition(US.date_is_sunday(month=7, day=4)) \
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
                "en": "Veterans Day (in lieu of)",
                "es": "Día de los Veteranos (en lugar de)",
            }) \
            .on(month=11, day=10) \
            .on_condition(US.date_is_saturday(month=11, day=11)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "en": "Veterans Day (in lieu of)",
                "es": "Día de los Veteranos (en lugar de)",
            }) \
            .on(month=11, day=12) \
            .on_condition(US.date_is_sunday(month=11, day=11)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "en": "Christmas Eve",
                "es": "Nochebuena",
            }) \
            .on(month=12, day=24) \
            .on_condition(US.date_is_not_saturday(month=12, day=25)) \
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
                "en": "Christmas Day (in lieu of)",
                "es": "Navidad (en lugar de)",
            }) \
            .on(month=12, day=24) \
            .on_condition(US.date_is_saturday(month=12, day=25)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_names({
                "en": "Christmas Day (in lieu of)",
                "es": "Navidad (en lugar de)",
            }) \
            .on(month=12, day=26) \
            .on_condition(US.date_is_sunday(month=12, day=25)) \
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

    @staticmethod
    def date_is_not_saturday(month, day):
        def wrapper(year):
            return SmartDayArrow(year, month, day).weekday() != "saturday"

        return wrapper

    @staticmethod
    def date_is_friday(month, day):
        def wrapper(year):
            return SmartDayArrow(year, month, day).weekday() == "friday"

        return wrapper

    @staticmethod
    def date_is_saturday(month, day):
        def wrapper(year):
            return SmartDayArrow(year, month, day).weekday() == "saturday"

        return wrapper

    @staticmethod
    def date_is_sunday(month, day):
        def wrapper(year):
            return SmartDayArrow(year, month, day).weekday() == "sunday"

        return wrapper
