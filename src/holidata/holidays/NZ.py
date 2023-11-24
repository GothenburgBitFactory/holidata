from dateutil.easter import EASTER_WESTERN

from holidata.utils import SmartDayArrow
from .holidays import Country


class NZ(Country):
    id = "NZ"
    languages = ["en"]
    default_lang = "en"
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("New Year's Day") \
            .on("01-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("New Year's Day (observed)") \
            .on(self.monday_after(month=1, day=1)) \
            .with_flags("NV") \
            .on_condition(self.date_is_on_weekend(month=1, day=1))

        self.define_holiday() \
            .with_name("Day after New Year's Day") \
            .on(self.day_after_new_years_day) \
            .with_flags("NV")

        self.define_holiday() \
            .with_name("Waitangi Day") \
            .on("02-06") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Waitangi Day (observed)") \
            .since(2017) \
            .on(self.monday_after(month=2, day=6)) \
            .with_flags("NV") \
            .on_condition(self.date_is_on_weekend(month=2, day=6))

        self.define_holiday() \
            .with_name("ANZAC Day") \
            .on("04-25") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("ANZAC Day (observed)") \
            .since(2016) \
            .on(self.monday_after(month=4, day=25)) \
            .with_flags("NV") \
            .on_condition(self.date_is_on_weekend(month=4, day=25))

        self.define_holiday() \
            .with_name("Christmas Day") \
            .on("12-25") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Christmas Day (observed)") \
            .on(self.tuesday_after(month=12, day=25)) \
            .with_flags("NV") \
            .on_condition(self.date_is_sunday(month=12, day=25))

        self.define_holiday() \
            .with_name("Christmas Day (observed)") \
            .on(self.monday_after(month=12, day=25)) \
            .with_flags("NV") \
            .on_condition(self.date_is_saturday(month=12, day=25))

        self.define_holiday() \
            .with_name("Boxing Day") \
            .on("12-26") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Boxing Day (observed)") \
            .on(self.tuesday_after(month=12, day=26)) \
            .with_flags("NV") \
            .on_condition(self.date_is_sunday(month=12, day=26))

        self.define_holiday() \
            .with_name("Boxing Day (observed)") \
            .on(self.monday_after(month=12, day=26)) \
            .with_flags("NV") \
            .on_condition(self.date_is_saturday(month=12, day=26))

        self.define_holiday() \
            .with_name("Good Friday") \
            .on("2 days before Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Easter Monday") \
            .on("1 day after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Queen's Birthday") \
            .on("1. monday in june") \
            .with_flags("NV")

        self.define_holiday() \
            .with_name("Labour Day") \
            .on("4. monday in october") \
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
    def monday_after(month, day):
        def wrapper(year):
            return SmartDayArrow(year, month, day).shift_to_weekday("monday", including=True)

        return wrapper

    @staticmethod
    def tuesday_after(month, day):
        def wrapper(year):
            return SmartDayArrow(year, month, day).shift_to_weekday("tuesday", including=True)

        return wrapper

    @staticmethod
    def day_after_new_years_day(year):
        date = SmartDayArrow(year, 1, 2)

        if date.weekday() in ["sunday", "monday"]:
            return date.shift_to_weekday("tuesday", including=True)

        elif date.weekday() == "saturday":
            return date.shift_to_weekday("monday", including=True)

        return date
