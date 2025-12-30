from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import day, first, last, date

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
            .on(date(month=1, day=1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("New Year's Day (observed)") \
            .on(first("monday").after(date(month=1, day=1))) \
            .with_flags("NV") \
            .on_condition(date(month=1, day=1).is_one_of(["saturday", "sunday"]))

        self.define_holiday() \
            .with_name("Christmas Day") \
            .on(date(month=12, day=25)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Christmas Day (observed)") \
            .on(first("monday").after(date(month=12, day=25))) \
            .with_flags("NV")  \
            .on_condition(date(month=12, day=25).is_a("saturday"))

        self.define_holiday() \
            .with_name("Christmas Day (observed)") \
            .on(first("tuesday").after(date(month=12, day=25))) \
            .with_flags("NV")  \
            .on_condition(date(month=12, day=25).is_a("sunday"))

        self.define_holiday() \
            .with_name("Boxing Day") \
            .on(date(month=12, day=26)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Boxing Day (observed)") \
            .on(first("monday").after(date(month=12, day=26), including=False)) \
            .with_flags("NV")  \
            .on_condition(date(month=12, day=26).is_a("saturday"))

        self.define_holiday() \
            .with_name("Boxing Day (observed)") \
            .on(first("tuesday").after(date(month=12, day=26), including=False)) \
            .with_flags("NV")  \
            .on_condition(date(month=12, day=26).is_a("sunday"))

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
            .on(first("monday").of("may")) \
            .with_flags("NV")

        self.define_holiday() \
            .with_name("August Bank Holiday") \
            .on(last("monday").of("august")) \
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
            .on(date(month=5, day=8)) \
            .with_flags("NV")

        """
        2012-06-05: Queen's Diamond Jubilee
        """
        self.define_holiday() \
            .with_name("Queen's Diamond Jubilee") \
            .in_years([2012]) \
            .on(date(month=6, day=5)) \
            .with_flags("NV")

        """
        2022-06-03: Queen's Platinum Jubilee
        """
        self.define_holiday() \
            .with_name("Queen's Platinum Jubilee") \
            .in_years([2022]) \
            .on(date(month=6, day=3)) \
            .with_flags("NV")

        """
        2022-09-19: State Funeral of Queen Elizabeth II
        """
        self.define_holiday() \
            .with_name("State Funeral of Queen Elizabeth II") \
            .in_years([2022]) \
            .on(date(month=9, day=19)) \
            .with_flags("NF")

    @staticmethod
    def date_of_spring_bank_holiday(year):
        """
        1. last monday in May
        2012: Moved to June 4, because of Queen’s Diamond Jubilee
        2022: Moved to June 2, because of Queen's Platinum Jubilee
        """
        if year == 2012:
            return date(6, 4)(year)
        elif year == 2022:
            return date(6, 2)(year)
        else:
            return last("monday").of("may")(year)
