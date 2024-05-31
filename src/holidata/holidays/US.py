from dateutil.easter import EASTER_WESTERN

from holidata.utils import month_reference
from .holidays import Country


class US(Country):
    id = "US"
    languages = ["en", "es"]
    default_lang = "en"
    regions = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
               "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND",
               "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY", "DC",
               "AS", "GU", "MP", "PR", "UM", "VI"]
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_names({
                "en": "New Year's Day",
                "es": "Año Neuvo",
            }) \
            .on("01-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "en": "Independence Day",
                "es": "Día de la Independiencia",
            }) \
            .on("07-04") \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "en": "Veterans Day",
                "es": "Día de los Veteranos",
            }) \
            .on("11-11") \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "en": "Christmas Eve",
                "es": "Nochebuena",
            }) \
            .on("12-24") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_names({
                "en": "Christmas Day",
                "es": "Navidad",
            }) \
            .on("12-25") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_names({
                "en": "Birthday of Martin Luther King, Jr.",
                "es": "Cumpleaños de Martin Luther King, Jr.",
            }) \
            .on("3. monday in January") \
            .with_flags("NV")

        self.define_holiday() \
            .with_names({
                "en": "Washington's Birthday",
                "es": "Día del Presidente",
            }) \
            .on("3. monday in February") \
            .with_flags("NV")

        self.define_holiday() \
            .with_names({
                "en": "Patriots' Day",
                "es": "Día del Patriota",
                }) \
            .in_regions(["MA", "ME"]) \
            .on("3. monday in April") \
            .with_flags("V")

        self.define_holiday() \
            .with_names({
                "en": "Memorial Day",
                "es": "Día de los Caídos",
            }) \
            .on("1. last monday in May") \
            .with_flags("NV")

        self.define_holiday() \
            .with_names({
                "en": "Labor Day",
                "es": "Día del Trabajo",
            }) \
            .on("1. monday in September") \
            .with_flags("NV")

        self.define_holiday() \
            .with_names({
                "en": "Columbus Day",
                "es": "Día de Columbus",
            }) \
            .on("2. monday in October") \
            .with_flags("NV")

        self.define_holiday() \
            .with_names({
                "en": "Thanksgiving Day",
                "es": "Día de Acción de Gracias",
            }) \
            .on("4. thursday in November") \
            .with_flags("NV")

        self.define_holiday() \
            .with_names({
                "en": "Day after Thanksgiving",
                "es": "Día después de Acción de Gracias",
            }) \
            .on(self.day_after_thanksgiving) \
            .with_flags("NV")

    @staticmethod
    def day_after_thanksgiving(year):
        date = month_reference(year, "november").shift_to_weekday(
            "thursday",
            order=4,
            reverse=False,
            including=True,
        )

        return date.shift(days=1)

