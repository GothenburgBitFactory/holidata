from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import day, first, last, date, Weekday, Month

__all__ = [
    "GB",
]


class GB(Country):
    id = "GB"
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
            .with_name("Christmas Day") \
            .on(date(Month.DECEMBER, 25)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Christmas Day (observed)") \
            .on(first(Weekday.MONDAY).after(date(Month.DECEMBER, 25))) \
            .with_flags("NV")  \
            .on_condition(date(Month.DECEMBER, 25).is_a(Weekday.SATURDAY))

        self.define_holiday() \
            .with_name("Christmas Day (observed)") \
            .on(first(Weekday.TUESDAY).after(date(Month.DECEMBER, 25))) \
            .with_flags("NV")  \
            .on_condition(date(Month.DECEMBER, 25).is_a(Weekday.SUNDAY))

        self.define_holiday() \
            .with_name("Boxing Day") \
            .on(date(Month.DECEMBER, 26)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Boxing Day (observed)") \
            .on(first(Weekday.MONDAY).after(date(Month.DECEMBER, 26), including=False)) \
            .with_flags("NV")  \
            .on_condition(date(Month.DECEMBER, 26).is_a(Weekday.SATURDAY))

        self.define_holiday() \
            .with_name("Boxing Day (observed)") \
            .on(first(Weekday.TUESDAY).after(date(Month.DECEMBER, 26), including=False)) \
            .with_flags("NV")  \
            .on_condition(date(Month.DECEMBER, 26).is_a(Weekday.SUNDAY))

        self.define_holiday() \
            .with_name("Good Friday") \
            .on(day(2).before(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Easter Monday") \
            .on(day(1).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Early May Bank Holiday") \
            .on(first(Weekday.MONDAY).of(Month.MAY)) \
            .with_flags("NV")

        self.define_holiday() \
            .with_name("August Bank Holiday") \
            .on(last(Weekday.MONDAY).of(Month.AUGUST)) \
            .with_flags("NV")

        self.define_holiday() \
            .with_name("Spring Bank Holiday") \
            .on(GB.date_of_spring_bank_holiday) \
            .with_flags("NV")

        """
        2023-05-08: Bank holiday for the coronation of King Charles III
        """
        self.define_holiday() \
            .with_name("Coronation of King Charles III") \
            .in_years([2023]) \
            .on(date(Month.MAY, 8)) \
            .with_flags("NV")

        """
        2012-06-05: Queen's Diamond Jubilee
        """
        self.define_holiday() \
            .with_name("Queen's Diamond Jubilee") \
            .in_years([2012]) \
            .on(date(Month.JUNE, 5)) \
            .with_flags("NV")

        """
        2022-06-03: Queen's Platinum Jubilee
        """
        self.define_holiday() \
            .with_name("Queen's Platinum Jubilee") \
            .in_years([2022]) \
            .on(date(Month.JUNE, 3)) \
            .with_flags("NV")

        """
        2022-09-19: State Funeral of Queen Elizabeth II
        """
        self.define_holiday() \
            .with_name("State Funeral of Queen Elizabeth II") \
            .in_years([2022]) \
            .on(date(Month.SEPTEMBER, 19)) \
            .with_flags("NF")

    @staticmethod
    def date_of_spring_bank_holiday(year):
        """
        1. last monday in May
        2012: Moved to June 4, because of Queen’s Diamond Jubilee
        2022: Moved to June 2, because of Queen's Platinum Jubilee
        """
        if year == 2012:
            return date(Month.JUNE, 4)(year)
        elif year == 2022:
            return date(Month.JUNE, 2)(year)
        else:
            return last(Weekday.MONDAY).of(Month.MAY)(year)
