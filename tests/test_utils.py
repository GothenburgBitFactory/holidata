from arrow import Arrow

from holidata.utils import (
    DateWrapper,
    DayShifter,
    Month,
    Weekday,
    WeekdayShifter,
    date,
    day,
    first,
    fourth,
    last,
    second,
    third,
)


class TestWeekdayEnum:
    def test_weekday_enum_values(self):
        assert Weekday.MONDAY == 0
        assert Weekday.TUESDAY == 1
        assert Weekday.WEDNESDAY == 2
        assert Weekday.THURSDAY == 3
        assert Weekday.FRIDAY == 4
        assert Weekday.SATURDAY == 5
        assert Weekday.SUNDAY == 6


class TestMonthEnum:
    def test_month_enum_values(self):
        assert Month.JANUARY == 1
        assert Month.FEBRUARY == 2
        assert Month.MARCH == 3
        assert Month.APRIL == 4
        assert Month.MAY == 5
        assert Month.JUNE == 6
        assert Month.JULY == 7
        assert Month.AUGUST == 8
        assert Month.SEPTEMBER == 9
        assert Month.OCTOBER == 10
        assert Month.NOVEMBER == 11
        assert Month.DECEMBER == 12


class TestDateWrapper:
    def test_wrapper_creation(self):
        wrapper = DateWrapper(default=lambda year: Arrow(year, Month.JANUARY, 1))
        assert wrapper.default_func is not None

    def test_wrapper_callable(self):
        wrapper = DateWrapper(default=lambda year: Arrow(year, Month.JANUARY, 1))
        result = wrapper(2023)
        assert isinstance(result, Arrow)
        assert result.year == 2023
        assert result.month == 1
        assert result.day == 1

    def test_is_a_method(self):
        wrapper = DateWrapper(default=lambda year: Arrow(year, Month.JANUARY, 2))  # 2023-01-02 is a Monday)
        predicate = wrapper.is_a(Weekday.MONDAY)
        assert predicate(2023) is True

        predicate = wrapper.is_a(Weekday.TUESDAY)
        assert predicate(2023) is False

    def test_is_not_a_method(self):
        wrapper = DateWrapper(default=lambda year: Arrow(year, Month.JANUARY, 2))  # 2023-01-02 is a Monday)
        predicate = wrapper.is_not_a(Weekday.TUESDAY)
        assert predicate(2023) is True

        predicate = wrapper.is_not_a(Weekday.MONDAY)
        assert predicate(2023) is False

    def test_is_one_of_method(self):
        wrapper = DateWrapper(default=lambda year: Arrow(year, Month.JANUARY, 2))  # 2023-01-02 is a Monday)
        predicate = wrapper.is_one_of([Weekday.MONDAY, Weekday.TUESDAY])
        assert predicate(2023) is True

        predicate = wrapper.is_one_of([Weekday.TUESDAY, Weekday.WEDNESDAY])
        assert predicate(2023) is False

    def test_is_none_of_method(self):
        wrapper = DateWrapper(default=lambda year: Arrow(year, Month.JANUARY, 2))  # 2023-01-02 is a Monday)
        predicate = wrapper.is_none_of([Weekday.TUESDAY, Weekday.WEDNESDAY])
        assert predicate(2023) is True

        predicate = wrapper.is_none_of([Weekday.MONDAY, Weekday.TUESDAY])
        assert predicate(2023) is False

    def test_is_equal_to_method(self):
        wrapper1 = DateWrapper(default=lambda year: Arrow(year, Month.JANUARY, 2))
        wrapper2 = DateWrapper(default=lambda year: Arrow(year, Month.JANUARY, 2))
        wrapper3 = DateWrapper(default=lambda year: Arrow(year, Month.JANUARY, 3))

        predicate = wrapper1.is_equal_to(wrapper2)
        assert predicate(2023) is True

        predicate = wrapper1.is_equal_to(wrapper3)
        assert predicate(2023) is False

    def test_is_not_equal_to_method(self):
        wrapper1 = DateWrapper(default=lambda year: Arrow(year, Month.JANUARY, 2))
        wrapper2 = DateWrapper(default=lambda year: Arrow(year, Month.JANUARY, 2))
        wrapper3 = DateWrapper(default=lambda year: Arrow(year, Month.JANUARY, 3))

        predicate = wrapper1.is_not_equal_to(wrapper3)
        assert predicate(2023) is True

        predicate = wrapper1.is_not_equal_to(wrapper2)
        assert predicate(2023) is False


class TestDateFunction:
    def test_date_function_creates_wrapper(self):
        wrapper = date(Month.JANUARY, 1)
        assert isinstance(wrapper, DateWrapper)
        assert wrapper.default_func is not None


class TestDayFunctionAndShifter:
    def test_day_function_creates_shifter(self):
        shifter = day(5)
        assert isinstance(shifter, DayShifter)
        assert shifter.day_count == 5

    def test_day_shifter_before(self):
        def base_date_func(year):
            return Arrow(year, Month.JANUARY, 10)

        shifter = day(3).before(base_date_func)
        result = shifter(2023)
        assert result.year == 2023
        assert result.month == 1
        assert result.day == 7  # 10 - 3 = 7

    def test_day_shifter_after(self):
        def base_date_func(year):
            return Arrow(year, Month.JANUARY, 10)

        shifter = day(3).after(base_date_func)
        result = shifter(2023)
        assert result.year == 2023
        assert result.month == 1
        assert result.day == 13  # 10 + 3 = 13


class TestWeekdayShifter:
    def test_first_weekday_shifter(self):
        shifter = first(Weekday.MONDAY)
        assert isinstance(shifter, WeekdayShifter)
        assert shifter.weekday == Weekday.MONDAY
        assert shifter.order == 1
        assert shifter.forward is True

    def test_second_weekday_shifter(self):
        shifter = second(Weekday.TUESDAY)
        assert isinstance(shifter, WeekdayShifter)
        assert shifter.weekday == Weekday.TUESDAY
        assert shifter.order == 2
        assert shifter.forward is True

    def test_third_weekday_shifter(self):
        shifter = third(Weekday.WEDNESDAY)
        assert isinstance(shifter, WeekdayShifter)
        assert shifter.weekday == Weekday.WEDNESDAY
        assert shifter.order == 3
        assert shifter.forward is True

    def test_fourth_weekday_shifter(self):
        shifter = fourth(Weekday.THURSDAY)
        assert isinstance(shifter, WeekdayShifter)
        assert shifter.weekday == Weekday.THURSDAY
        assert shifter.order == 4
        assert shifter.forward is True

    def test_last_weekday_shifter(self):
        shifter = last(Weekday.FRIDAY)
        assert isinstance(shifter, WeekdayShifter)
        assert shifter.weekday == Weekday.FRIDAY
        assert shifter.order == 1
        assert shifter.forward is False

    def test_weekday_shifter_of_method(self):
        shifter = first(Weekday.MONDAY).of(Month.JANUARY)
        result = shifter(2023)
        # First Monday of January 2023 is 2023-01-02
        assert result.year == 2023
        assert result.month == 1
        assert result.day == 2
        assert result.weekday() == Weekday.MONDAY

    def test_weekday_shifter_before_method(self):
        def base_date_func(year):
            return Arrow(year, Month.JANUARY, 15)

        shifter = first(Weekday.MONDAY).before(base_date_func)
        result = shifter(2023)
        # First Monday before 2023-01-15 is 2023-01-09
        assert result.year == 2023
        assert result.month == 1
        assert result.day == 9
        assert result.weekday() == Weekday.MONDAY

    def test_weekday_shifter_after_method(self):
        def base_date_func(year):
            return Arrow(year, Month.JANUARY, 15)

        shifter = first(Weekday.MONDAY).after(base_date_func)
        result = shifter(2023)
        # First Monday after 2023-01-15 is 2023-01-16
        assert result.year == 2023
        assert result.month == 1
        assert result.day == 16
        assert result.weekday() == Weekday.MONDAY
