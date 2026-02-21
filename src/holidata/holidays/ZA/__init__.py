from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import Month, Weekday, date, day

__all__ = [
    "ZA",
]


class ZA(Country):
    id = "ZA"
    languages = ["en"]
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Christmas Day") \
            .on(date(Month.DECEMBER, 25)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Good Friday") \
            .on(day(2).before(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Family Day") \
            .on(day(1).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("New Year's Day") \
            .on(date(Month.JANUARY, 1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("New Year's Day (Supplement)") \
            .on(date(Month.JANUARY, 2)) \
            .with_flags("NF") \
            .annotated_with("Supplement holiday") \
            .on_condition(date(Month.JANUARY, 1).is_a(Weekday.SUNDAY))

        self.define_holiday() \
            .with_name("Human Rights Day") \
            .on(date(Month.MARCH, 21)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Human Rights Day (Supplement)") \
            .on(date(Month.MARCH, 22)) \
            .with_flags("NF") \
            .annotated_with("Supplement holiday") \
            .on_condition(date(Month.MARCH, 21).is_a(Weekday.SUNDAY))

        self.define_holiday() \
            .with_name("Freedom Day") \
            .on(date(Month.APRIL, 27)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Freedom Day (Supplement)") \
            .on(date(Month.APRIL, 28)) \
            .with_flags("NF") \
            .annotated_with("Supplement holiday") \
            .on_condition(date(Month.APRIL, 27).is_a(Weekday.SUNDAY))

        self.define_holiday() \
            .with_name("Worker's Day") \
            .on(date(Month.MAY, 1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Worker's Day (Supplement)") \
            .on(date(Month.MAY, 2)) \
            .with_flags("NF") \
            .annotated_with("Supplement holiday") \
            .on_condition(date(Month.MAY, 1).is_a(Weekday.SUNDAY))

        self.define_holiday() \
            .with_name("Youth Day") \
            .on(date(Month.JUNE, 16)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Youth Day (Supplement)") \
            .on(date(Month.JUNE, 17)) \
            .with_flags("NF") \
            .annotated_with("Supplement holiday") \
            .on_condition(date(Month.JUNE, 16).is_a(Weekday.SUNDAY))

        self.define_holiday() \
            .with_name("National Women's Day") \
            .on(date(Month.AUGUST, 9)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("National Women's Day (Supplement)") \
            .on(date(Month.AUGUST, 10)) \
            .with_flags("NF") \
            .annotated_with("Supplement holiday") \
            .on_condition(date(Month.AUGUST, 9).is_a(Weekday.SUNDAY))

        self.define_holiday() \
            .with_name("Heritage Day") \
            .on(date(Month.SEPTEMBER, 24)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Heritage Day (Supplement)") \
            .on(date(Month.SEPTEMBER, 25)) \
            .with_flags("NF") \
            .annotated_with("Supplement holiday") \
            .on_condition(date(Month.SEPTEMBER, 24).is_a(Weekday.SUNDAY))

        self.define_holiday() \
            .with_name("Day of Reconciliation") \
            .on(date(Month.DECEMBER, 16)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Day of Reconciliation (Supplement)") \
            .on(date(Month.DECEMBER, 17)) \
            .with_flags("NF") \
            .annotated_with("Supplement holiday") \
            .on_condition(date(Month.DECEMBER, 16).is_a(Weekday.SUNDAY))

        self.define_holiday() \
            .with_name("Day of Goodwill") \
            .on(date(Month.DECEMBER, 26)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Day of Goodwill (Supplement)") \
            .on(date(Month.DECEMBER, 27)) \
            .with_flags("NF") \
            .annotated_with("Supplement holiday") \
            .on_condition(date(Month.DECEMBER, 26).is_a(Weekday.SUNDAY))
