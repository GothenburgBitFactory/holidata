from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import day, first, fourth, date

__all__ = [
    "NZ",
]


class NZ(Country):
    id = "NZ"
    languages = ["en"]
    default_lang = "en"
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("New Year's Day") \
            .on(date(month=1, day=1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("New Year's Day (observed)") \
            .on(first("monday").after(date(month=1, day=1))) \
            .with_flags("NV") \
            .on_condition(date(month=1, day=1).is_one_of(["saturday", "sunday"]))

        self.define_holiday() \
            .with_name("Day after New Year's Day") \
            .on(date(month=1, day=2)) \
            .on_condition(date(month=1, day=1).is_none_of(["friday", "saturday", "sunday"])) \
            .with_flags("NV")

        self.define_holiday() \
            .with_name("Day after New Year's Day") \
            .on(date(month=1, day=3)) \
            .on_condition(date(month=1, day=1).is_a("sunday")) \
            .with_flags("NV")

        self.define_holiday() \
            .with_name("Day after New Year's Day") \
            .on(date(month=1, day=4)) \
            .on_condition(date(month=1, day=1).is_one_of(["friday", "saturday"])) \
            .with_flags("NV")

        self.define_holiday() \
            .with_name("Waitangi Day") \
            .on(date(month=2, day=6)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Waitangi Day (observed)") \
            .since(2017) \
            .on(first("monday").after(date(month=2, day=6))) \
            .with_flags("NV") \
            .on_condition(date(month=2, day=6).is_one_of(["saturday", "sunday"]))

        self.define_holiday() \
            .with_name("ANZAC Day") \
            .on(date(month=4, day=25)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("ANZAC Day (observed)") \
            .since(2016) \
            .on(first("monday").after(date(month=4, day=25))) \
            .with_flags("NV") \
            .on_condition(date(month=4, day=25).is_one_of(["saturday", "sunday"]))

        self.define_holiday() \
            .with_name("Christmas Day") \
            .on(date(month=12, day=25)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Christmas Day (observed)") \
            .on(first("tuesday").after(date(month=12, day=25))) \
            .with_flags("NV") \
            .on_condition(date(month=12, day=25).is_a("sunday"))

        self.define_holiday() \
            .with_name("Christmas Day (observed)") \
            .on(first("monday").after(date(month=12, day=25))) \
            .with_flags("NV") \
            .on_condition(date(month=12, day=25).is_a("saturday"))

        self.define_holiday() \
            .with_name("Boxing Day") \
            .on(date(month=12, day=26)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Boxing Day (observed)") \
            .on(first("tuesday").after(date(month=12, day=26))) \
            .with_flags("NV") \
            .on_condition(date(month=12, day=26).is_a("sunday"))

        self.define_holiday() \
            .with_name("Boxing Day (observed)") \
            .on(first("monday").after(date(month=12, day=26))) \
            .with_flags("NV") \
            .on_condition(date(month=12, day=26).is_a("saturday"))

        self.define_holiday() \
            .with_name("Good Friday") \
            .on(day(2).before(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Easter Monday") \
            .on(day(1).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Queen's Birthday") \
            .on(first("monday").of("june")) \
            .with_flags("NV")

        self.define_holiday() \
            .with_name("Labour Day") \
            .on(fourth("monday").of("october")) \
            .with_flags("NV")
