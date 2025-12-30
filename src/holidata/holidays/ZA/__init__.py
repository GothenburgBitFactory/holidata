from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import day, date

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
            .on(date(month=12, day=25)) \
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
            .on(date(month=1, day=1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("New Year's Day (Supplement)") \
            .on(date(month=1, day=2)) \
            .with_flags("NF") \
            .annotated_with("Supplement holiday") \
            .on_condition(date(month=1, day=1).is_a("sunday"))

        self.define_holiday() \
            .with_name("Human Rights Day") \
            .on(date(month=3, day=21)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Human Rights Day (Supplement)") \
            .on(date(month=3, day=22)) \
            .with_flags("NF") \
            .annotated_with("Supplement holiday") \
            .on_condition(date(month=3, day=21).is_a("sunday"))

        self.define_holiday() \
            .with_name("Freedom Day") \
            .on(date(month=4, day=27)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Freedom Day (Supplement)") \
            .on(date(month=4, day=28)) \
            .with_flags("NF") \
            .annotated_with("Supplement holiday") \
            .on_condition(date(month=4, day=27).is_a("sunday"))

        self.define_holiday() \
            .with_name("Worker's Day") \
            .on(date(month=5, day=1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Worker's Day (Supplement)") \
            .on(date(month=5, day=2)) \
            .with_flags("NF") \
            .annotated_with("Supplement holiday") \
            .on_condition(date(month=5, day=1).is_a("sunday"))

        self.define_holiday() \
            .with_name("Youth Day") \
            .on(date(month=6, day=16)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Youth Day (Supplement)") \
            .on(date(month=6, day=17)) \
            .with_flags("NF") \
            .annotated_with("Supplement holiday") \
            .on_condition(date(month=6, day=16).is_a("sunday"))

        self.define_holiday() \
            .with_name("National Women's Day") \
            .on(date(month=8, day=9)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("National Women's Day (Supplement)") \
            .on(date(month=8, day=10)) \
            .with_flags("NF") \
            .annotated_with("Supplement holiday") \
            .on_condition(date(month=8, day=9).is_a("sunday"))

        self.define_holiday() \
            .with_name("Heritage Day") \
            .on(date(month=9, day=24)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Heritage Day (Supplement)") \
            .on(date(month=9, day=25)) \
            .with_flags("NF") \
            .annotated_with("Supplement holiday") \
            .on_condition(date(month=9, day=24).is_a("sunday"))

        self.define_holiday() \
            .with_name("Day of Reconciliation") \
            .on(date(month=12, day=16)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Day of Reconciliation (Supplement)") \
            .on(date(month=12, day=17)) \
            .with_flags("NF") \
            .annotated_with("Supplement holiday") \
            .on_condition(date(month=12, day=16).is_a("sunday"))

        self.define_holiday() \
            .with_name("Day of Goodwill") \
            .on(date(month=12, day=26)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Day of Goodwill (Supplement)") \
            .on(date(month=12, day=27)) \
            .with_flags("NF") \
            .annotated_with("Supplement holiday") \
            .on_condition(date(month=12, day=26).is_a("sunday"))
