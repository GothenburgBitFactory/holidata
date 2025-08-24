from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import SmartDayArrow, day, first, fourth

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
            .on(month=1, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("New Year's Day (observed)") \
            .on(first("monday").after(month=1, day=1)) \
            .with_flags("NV") \
            .on_condition(NZ.date_is_on_weekend(month=1, day=1))

        self.define_holiday() \
            .with_name("Day after New Year's Day") \
            .on(NZ.day_after_new_years_day) \
            .with_flags("NV")

        self.define_holiday() \
            .with_name("Waitangi Day") \
            .on(month=2, day=6) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Waitangi Day (observed)") \
            .since(2017) \
            .on(first("monday").after(month=2, day=6)) \
            .with_flags("NV") \
            .on_condition(NZ.date_is_on_weekend(month=2, day=6))

        self.define_holiday() \
            .with_name("ANZAC Day") \
            .on(month=4, day=25) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("ANZAC Day (observed)") \
            .since(2016) \
            .on(first("monday").after(month=4, day=25)) \
            .with_flags("NV") \
            .on_condition(NZ.date_is_on_weekend(month=4, day=25))

        self.define_holiday() \
            .with_name("Christmas Day") \
            .on(month=12, day=25) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Christmas Day (observed)") \
            .on(first("tuesday").after(month=12, day=25)) \
            .with_flags("NV") \
            .on_condition(NZ.date_is_sunday(month=12, day=25))

        self.define_holiday() \
            .with_name("Christmas Day (observed)") \
            .on(first("monday").after(month=12, day=25)) \
            .with_flags("NV") \
            .on_condition(NZ.date_is_saturday(month=12, day=25))

        self.define_holiday() \
            .with_name("Boxing Day") \
            .on(month=12, day=26) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Boxing Day (observed)") \
            .on(first("tuesday").after(month=12, day=26)) \
            .with_flags("NV") \
            .on_condition(NZ.date_is_sunday(month=12, day=26))

        self.define_holiday() \
            .with_name("Boxing Day (observed)") \
            .on(first("monday").after(month=12, day=26)) \
            .with_flags("NV") \
            .on_condition(NZ.date_is_saturday(month=12, day=26))

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

    @staticmethod
    def date_is_on_weekend(month, day):
        def wrapper(year):
            return SmartDayArrow(year, month, day).weekday() in ["saturday", "sunday"]

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

    @staticmethod
    def day_after_new_years_day(year):
        date = SmartDayArrow(year, 1, 2)

        if date.weekday() in ["sunday", "monday"]:
            return date.shift_to_weekday("tuesday", including=True)

        elif date.weekday() == "saturday":
            return date.shift_to_weekday("monday", including=True)

        return date
