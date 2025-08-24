from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import SmartDayArrow, day

__all__ = [
    "ZA",
]


class ZA(Country):
    id = "ZA"
    languages = ["en"]
    default_lang = "en"
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Christmas Day") \
            .on(month=12, day=25) \
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
            .on(month=1, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("New Year's Day (Supplement)") \
            .on(month=1, day=2) \
            .with_flags("NF") \
            .annotated_with("Supplement holiday") \
            .on_condition(ZA.date_is_on_sunday(month=1, day=1))

        self.define_holiday() \
            .with_name("Human Rights Day") \
            .on(month=3, day=21) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Human Rights Day (Supplement)") \
            .on(month=3, day=22) \
            .with_flags("NF") \
            .annotated_with("Supplement holiday") \
            .on_condition(ZA.date_is_on_sunday(month=3, day=21))

        self.define_holiday() \
            .with_name("Freedom Day") \
            .on(month=4, day=27) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Freedom Day (Supplement)") \
            .on(month=4, day=28) \
            .with_flags("NF") \
            .annotated_with("Supplement holiday") \
            .on_condition(ZA.date_is_on_sunday(month=4, day=27))

        self.define_holiday() \
            .with_name("Worker's Day") \
            .on(month=5, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Worker's Day (Supplement)") \
            .on(month=5, day=2) \
            .with_flags("NF") \
            .annotated_with("Supplement holiday") \
            .on_condition(ZA.date_is_on_sunday(month=5, day=1))

        self.define_holiday() \
            .with_name("Youth Day") \
            .on(month=6, day=16) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Youth Day (Supplement)") \
            .on(month=6, day=17) \
            .with_flags("NF") \
            .annotated_with("Supplement holiday") \
            .on_condition(ZA.date_is_on_sunday(month=6, day=16))

        self.define_holiday() \
            .with_name("National Women's Day") \
            .on(month=8, day=9) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("National Women's Day (Supplement)") \
            .on(month=8, day=10) \
            .with_flags("NF") \
            .annotated_with("Supplement holiday") \
            .on_condition(ZA.date_is_on_sunday(month=8, day=9))

        self.define_holiday() \
            .with_name("Heritage Day") \
            .on(month=9, day=24) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Heritage Day (Supplement)") \
            .on(month=9, day=25) \
            .with_flags("NF") \
            .annotated_with("Supplement holiday") \
            .on_condition(ZA.date_is_on_sunday(month=9, day=24))

        self.define_holiday() \
            .with_name("Day of Reconciliation") \
            .on(month=12, day=16) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Day of Reconciliation (Supplement)") \
            .on(month=12, day=17) \
            .with_flags("NF") \
            .annotated_with("Supplement holiday") \
            .on_condition(ZA.date_is_on_sunday(month=12, day=16))

        self.define_holiday() \
            .with_name("Day of Goodwill") \
            .on(month=12, day=26) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Day of Goodwill (Supplement)") \
            .on(month=12, day=27) \
            .with_flags("NF") \
            .annotated_with("Supplement holiday") \
            .on_condition(ZA.date_is_on_sunday(month=12, day=26))

    @staticmethod
    def date_is_on_sunday(month, day):
        def wrapper(year):
            return SmartDayArrow(year, month, day).weekday() == "sunday"

        return wrapper
