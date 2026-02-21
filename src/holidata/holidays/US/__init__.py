from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import Month, Weekday, date, day, first, fourth, last, second, third

__all__ = [
    "US",
]


class US(Country):
    id = "US"
    languages = ["en", "es"]
    default_lang = "en"
    easter_type = EASTER_WESTERN

    def __init__(self) -> None:
        super().__init__()

        self.define_holiday() \
            .with_names({
                "en": "New Year's Day",
                "es": "Año Neuvo",
            }) \
            .on(date(Month.JANUARY, 1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "en": "New Year's Day (in lieu of)",
                "es": "Año Neuvo (en lugar de)",
            }) \
            .on(date(Month.DECEMBER, 31)) \
            .on_condition(date(Month.DECEMBER, 31).is_a(Weekday.FRIDAY)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "en": "New Year's Day (in lieu of)",
                "es": "Año Neuvo (en lugar de)",
            }) \
            .on(date(Month.JANUARY, 2)) \
            .on_condition(date(Month.JANUARY, 1).is_a(Weekday.SUNDAY)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "en": "Juneteenth National Independence Day",
                "es": "Juneteenth – Día de la Emancipación",
            }) \
            .since(2021) \
            .on(date(Month.JUNE, 19)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "en": "Juneteenth National Independence Day (in lieu of)",
                "es": "Juneteenth – Día de la Emancipación (en lugar de)",
            }) \
            .since(2021) \
            .on(date(Month.JUNE, 18)) \
            .on_condition(date(Month.JUNE, 19).is_a(Weekday.SATURDAY)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "en": "Juneteenth National Independence Day (in lieu of)",
                "es": "Juneteenth – Día de la Emancipación (en lugar de)",
            }) \
            .since(2021) \
            .on(date(Month.JUNE, 20)) \
            .on_condition(date(Month.JUNE, 19).is_a(Weekday.SUNDAY)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "en": "Independence Day",
                "es": "Día de la Independiencia",
            }) \
            .on(date(Month.JULY, 4)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "en": "Independence Day (in lieu of)",
                "es": "Día de la Independiencia (en lugar de)",
            }) \
            .on(date(Month.JULY, 3)) \
            .on_condition(date(Month.JULY, 4).is_a(Weekday.SATURDAY)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "en": "Independence Day (in lieu of)",
                "es": "Día de la Independiencia (en lugar de)",
            }) \
            .on(date(Month.JULY, 5)) \
            .on_condition(date(Month.JULY, 4).is_a(Weekday.SUNDAY)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "en": "Veterans Day",
                "es": "Día de los Veteranos",
            }) \
            .on(date(Month.NOVEMBER, 11)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "en": "Veterans Day (in lieu of)",
                "es": "Día de los Veteranos (en lugar de)",
            }) \
            .on(date(Month.NOVEMBER, 10)) \
            .on_condition(date(Month.NOVEMBER, 11).is_a(Weekday.SATURDAY)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "en": "Veterans Day (in lieu of)",
                "es": "Día de los Veteranos (en lugar de)",
            }) \
            .on(date(Month.NOVEMBER, 12)) \
            .on_condition(date(Month.NOVEMBER, 11).is_a(Weekday.SUNDAY)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "en": "Christmas Eve",
                "es": "Nochebuena",
            }) \
            .on(date(Month.DECEMBER, 24)) \
            .on_condition(date(Month.DECEMBER, 25).is_not_a(Weekday.SATURDAY)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_names({
                "en": "Christmas Day",
                "es": "Navidad",
            }) \
            .on(date(Month.DECEMBER, 25)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_names({
                "en": "Christmas Day (in lieu of)",
                "es": "Navidad (en lugar de)",
            }) \
            .on(date(Month.DECEMBER, 24)) \
            .on_condition(date(Month.DECEMBER, 25).is_a(Weekday.SATURDAY)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_names({
                "en": "Christmas Day (in lieu of)",
                "es": "Navidad (en lugar de)",
            }) \
            .on(date(Month.DECEMBER, 26)) \
            .on_condition(date(Month.DECEMBER, 25).is_a(Weekday.SUNDAY)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_names({
                "en": "Birthday of Martin Luther King, Jr.",
                "es": "Cumpleaños de Martin Luther King, Jr.",
            }) \
            .on(third(Weekday.MONDAY).of(Month.JANUARY)) \
            .with_flags("NV")

        self.define_holiday() \
            .with_names({
                "en": "Washington's Birthday",
                "es": "Día del Presidente",
            }) \
            .on(third(Weekday.MONDAY).of(Month.FEBRUARY)) \
            .with_flags("NV")

        self.define_holiday() \
            .with_names({
                "en": "Patriots' Day",
                "es": "Día del Patriota",
                }) \
            .in_regions(["MA", "ME"]) \
            .on(third(Weekday.MONDAY).of(Month.APRIL)) \
            .with_flags("V")

        self.define_holiday() \
            .with_names({
                "en": "Memorial Day",
                "es": "Día de los Caídos",
            }) \
            .on(last(Weekday.MONDAY).of(Month.MAY)) \
            .with_flags("NV")

        self.define_holiday() \
            .with_names({
                "en": "Labor Day",
                "es": "Día del Trabajo",
            }) \
            .on(first(Weekday.MONDAY).of(Month.SEPTEMBER)) \
            .with_flags("NV")

        self.define_holiday() \
            .with_names({
                "en": "Columbus Day",
                "es": "Día de Columbus",
            }) \
            .on(second(Weekday.MONDAY).of(Month.OCTOBER)) \
            .with_flags("NV")

        self.define_holiday() \
            .with_names({
                "en": "Thanksgiving Day",
                "es": "Día de Acción de Gracias",
            }) \
            .on(fourth(Weekday.THURSDAY).of(Month.NOVEMBER)) \
            .with_flags("NV")

        self.define_holiday() \
            .with_names({
                "en": "Day after Thanksgiving",
                "es": "Día después de Acción de Gracias",
            }) \
            .on(day(1).after(fourth(Weekday.THURSDAY).of(Month.NOVEMBER))) \
            .with_flags("NV")
