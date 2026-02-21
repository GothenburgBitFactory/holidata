from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import Month, Weekday, date, day, first, fourth

__all__ = [
    "NZ",
]


class NZ(Country):
    id = "NZ"
    languages = ["en"]
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("New Year's Day") \
            .on(date(Month.JANUARY, 1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("New Year's Day (observed)") \
            .on(first(Weekday.MONDAY).after(date(Month.JANUARY, 1))) \
            .with_flags("NV") \
            .on_condition(date(Month.JANUARY, 1).is_one_of([Weekday.SATURDAY, Weekday.SUNDAY]))

        self.define_holiday() \
            .with_name("Day after New Year's Day") \
            .on(date(Month.JANUARY, 2)) \
            .on_condition(date(Month.JANUARY, 1).is_none_of([Weekday.FRIDAY, Weekday.SATURDAY, Weekday.SUNDAY])) \
            .with_flags("NV")

        self.define_holiday() \
            .with_name("Day after New Year's Day") \
            .on(date(Month.JANUARY, 3)) \
            .on_condition(date(Month.JANUARY, 1).is_a(Weekday.SUNDAY)) \
            .with_flags("NV")

        self.define_holiday() \
            .with_name("Day after New Year's Day") \
            .on(date(Month.JANUARY, 4)) \
            .on_condition(date(Month.JANUARY, 1).is_one_of([Weekday.FRIDAY, Weekday.SATURDAY])) \
            .with_flags("NV")

        self.define_holiday() \
            .with_name("Waitangi Day") \
            .on(date(Month.FEBRUARY, 6)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Waitangi Day (observed)") \
            .since(2017) \
            .on(first(Weekday.MONDAY).after(date(Month.FEBRUARY, 6))) \
            .with_flags("NV") \
            .on_condition(date(Month.FEBRUARY, 6).is_one_of([Weekday.SATURDAY, Weekday.SUNDAY]))

        self.define_holiday() \
            .with_name("ANZAC Day") \
            .on(date(Month.APRIL, 25)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("ANZAC Day (observed)") \
            .since(2016) \
            .on(first(Weekday.MONDAY).after(date(Month.APRIL, 25))) \
            .with_flags("NV") \
            .on_condition(date(Month.APRIL, 25).is_one_of([Weekday.SATURDAY, Weekday.SUNDAY]))

        self.define_holiday() \
            .with_name("Christmas Day") \
            .on(date(Month.DECEMBER, 25)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Christmas Day (observed)") \
            .on(first(Weekday.TUESDAY).after(date(Month.DECEMBER, 25))) \
            .with_flags("NV") \
            .on_condition(date(Month.DECEMBER, 25).is_a(Weekday.SUNDAY))

        self.define_holiday() \
            .with_name("Christmas Day (observed)") \
            .on(first(Weekday.MONDAY).after(date(Month.DECEMBER, 25))) \
            .with_flags("NV") \
            .on_condition(date(Month.DECEMBER, 25).is_a(Weekday.SATURDAY))

        self.define_holiday() \
            .with_name("Boxing Day") \
            .on(date(Month.DECEMBER, 26)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Boxing Day (observed)") \
            .on(first(Weekday.TUESDAY).after(date(Month.DECEMBER, 26))) \
            .with_flags("NV") \
            .on_condition(date(Month.DECEMBER, 26).is_a(Weekday.SUNDAY))

        self.define_holiday() \
            .with_name("Boxing Day (observed)") \
            .on(first(Weekday.MONDAY).after(date(Month.DECEMBER, 26))) \
            .with_flags("NV") \
            .on_condition(date(Month.DECEMBER, 26).is_a(Weekday.SATURDAY))

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
            .on(first(Weekday.MONDAY).of(Month.JUNE)) \
            .with_flags("NV")

        self.define_holiday() \
            .with_name("Labour Day") \
            .on(fourth(Weekday.MONDAY).of(Month.OCTOBER)) \
            .with_flags("NV")
