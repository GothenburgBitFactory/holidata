from dateutil.easter import EASTER_WESTERN

from holidata.utils import month_reference, SmartDayArrow
from .holidays import Country


class GB(Country):
    id = "GB"
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
            .with_name("Christmas Day") \
            .on("12-25") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Christmas Day (observed)") \
            .on(self.monday_after(month=12, day=25)) \
            .with_flags("NV")  \
            .on_condition(self.date_is_on_saturday(month=12, day=25))

        self.define_holiday() \
            .with_name("Christmas Day (observed)") \
            .on(self.tuesday_after(month=12, day=25)) \
            .with_flags("NV")  \
            .on_condition(self.date_is_on_sunday(month=12, day=25))

        self.define_holiday() \
            .with_name("Boxing Day") \
            .on("12-26") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Boxing Day (observed)") \
            .on(self.monday_after(month=12, day=26)) \
            .with_flags("NV")  \
            .on_condition(self.date_is_on_saturday(month=12, day=26))

        self.define_holiday() \
            .with_name("Boxing Day (observed)") \
            .on(self.tuesday_after(month=12, day=26)) \
            .with_flags("NV")  \
            .on_condition(self.date_is_on_sunday(month=12, day=26))

        self.define_holiday() \
            .with_name("Good Friday") \
            .on("2 days before Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Easter Monday") \
            .on("1 day after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Early May Bank Holiday") \
            .on("1. monday in may") \
            .with_flags("NV")

        self.define_holiday() \
            .with_name("August Bank Holiday") \
            .on("1. last monday in august") \
            .with_flags("NV")

        self.define_holiday() \
            .with_name("Spring Bank Holiday") \
            .on(self.date_of_spring_bank_holiday) \
            .with_flags("NV")

        """
        2023-05-08: Bank holiday for the coronation of King Charles III
        """
        self.define_holiday() \
            .with_name("Coronation of King Charles III") \
            .in_years([2023]) \
            .on("05-08") \
            .with_flags("NV")

        """
        2012-06-05: Queen's Diamond Jubilee
        """
        self.define_holiday() \
            .with_name("Queen's Diamond Jubilee") \
            .in_years([2012]) \
            .on("06-05") \
            .with_flags("NV")

        """
        2022-06-03: Queen's Platinum Jubilee
        """
        self.define_holiday() \
            .with_name("Queen's Platinum Jubilee") \
            .in_years([2022]) \
            .on("06-03") \
            .with_flags("NV")

        """
        2022-09-19: State Funeral of Queen Elizabeth II
        """
        self.define_holiday() \
            .with_name("State Funeral of Queen Elizabeth II") \
            .in_years([2022]) \
            .on("09-19") \
            .with_flags("NF")

    @staticmethod
    def date_of_spring_bank_holiday(year):
        """
        1. last monday in May
        2012: Moved to June 4, because of Queen’s Diamond Jubilee
        2022: Moved to June 2, because of Queen's Platinum Jubilee
        """
        if year == 2012:
            return SmartDayArrow(year, 6, 4)
        elif year == 2022:
            return SmartDayArrow(year, 6, 2)
        else:
            return month_reference(year, "may", first=False) \
                .shift_to_weekday("monday", order=1, reverse=True, including=True)

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
    def date_is_on_weekend(month, day):
        def wrapper(year):
            return SmartDayArrow(year, month, day).weekday() in ["saturday", "sunday"]

        return wrapper

    @staticmethod
    def date_is_on_saturday(month, day):
        def wrapper(year):
            return SmartDayArrow(year, month, day).weekday() == "saturday"

        return wrapper

    @staticmethod
    def date_is_on_sunday(month, day):
        def wrapper(year):
            return SmartDayArrow(year, month, day).weekday() == "sunday"

        return wrapper
