"""
Provides date-handling related utils.
"""
from enum import IntEnum
from typing import Callable, List, Union

from arrow import Arrow


class Weekday(IntEnum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


class Month(IntEnum):
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12


class SmartDayArrow(Arrow):
    """
    A wrapper around Arrow datetime reference that provides additional convenience methods.
    """

    def shift_to_weekday(self, day: Weekday, order: int = 1, reverse: bool = False, including: bool = False) -> 'SmartDayArrow':
        """
        Shifts to {order}. weekday in the given direction, i.e. 2. monday before this date would be:

        >>> arrow.shift_to_weekday(Weekday.MONDAY, order=2, reverse=True)
        """
        if order <= 0:
            raise ValueError("Order must be greater than 0")

        result = self

        if including and result.weekday() == day:
            if order == 1:
                return result
            else:
                order = order - 1

        while order > 0:
            result = result.shift(days=1 if not reverse else -1)
            if day == result.weekday():
                order = order - 1

        return result


class SmartDayArrowWrapper:
    def __init__(self, month: int, day: int):
        self.month = month
        self.day = day

    def is_a(self, weekday: Weekday) -> Callable[[int], bool]:
        def wrapper(year):
            return self(year).weekday() == weekday

        return wrapper

    def is_not_a(self, weekday: Weekday) -> Callable[[int], bool]:
        def wrapper(year):
            return self(year).weekday() != weekday

        return wrapper

    def is_one_of(self, selection: List[Weekday]):
        def wrapper(year):
            return self(year).weekday() in selection

        return wrapper

    def is_none_of(self, selection: List[Weekday]):
        def wrapper(year):
            return self(year).weekday() not in selection

        return wrapper

    def is_equal_to(self, other):
        def wrapper(year):
            return self(year) == other(year)

        return wrapper

    def is_not_equal_to(self, other: Callable[[int], SmartDayArrow]):
        def wrapper(year):
            return self(year) != other(year)

        return wrapper

    def __call__(self, year: int) -> SmartDayArrow:
        return SmartDayArrow(year, self.month, self.day)


def date(month: int, day: int) -> SmartDayArrowWrapper:
    return SmartDayArrowWrapper(month, day)


class SmartDayArrowDayShifter:
    def __init__(self, days):
        self.day_count: int = days
        self.shift_direction: int = 0
        self.date: Callable[[int], Union[SmartDayArrow, None]] = lambda year: None

    def before(self, date_func: Callable[[int], SmartDayArrow]) -> 'SmartDayArrowDayShifter':
        self.date = date_func
        self.shift_direction = -1
        return self

    def after(self, date_func: Callable[[int], SmartDayArrow]) -> 'SmartDayArrowDayShifter':
        self.date = date_func
        self.shift_direction = 1
        return self

    def __call__(self, year: int) -> SmartDayArrow:
        return self.date(year).shift(days=self.day_count * self.shift_direction) if self.date is not None else None


def day(count: int) -> SmartDayArrowDayShifter:
    return SmartDayArrowDayShifter(count)


class SmartDayArrowWeekdayShifter:
    def __init__(self, weekday: Weekday, order: int, forward: bool):
        self.weekday = weekday
        self.order = order
        self.forward = forward
        self.including = True
        self.date = None

    def of(self, month: Month) -> 'SmartDayArrowWeekdayShifter':
        month_index = month.value

        if self.forward:
            self.date = date(month, 1)
        else:
            def wrapper(year):
                return SmartDayArrow(
                    year if month_index != 12 else year + 1,
                    (month_index % 12) + 1,
                    1).shift(days=-1)

            self.date = wrapper

        return self

    def before(self, date_func: Callable[[int], SmartDayArrow], including: bool = False) -> 'SmartDayArrowWeekdayShifter':
        self._configure_shift(date_func, False, including)
        return self

    def after(self, date_func: Callable[[int], SmartDayArrow], including: bool = False) -> 'SmartDayArrowWeekdayShifter':
        self._configure_shift(date_func, True, including)
        return self

    def _configure_shift(self, date_func: Callable[[int], SmartDayArrow], forward: bool, including: bool):
        self.date = date_func
        self.forward = forward
        self.including = including

    def __call__(self, year: int) -> SmartDayArrow:
        return self.date(year).shift_to_weekday(
            self.weekday,
            order=self.order,
            reverse=not self.forward,
            including=self.including,
        )


def first(weekday: Weekday) -> SmartDayArrowWeekdayShifter:
    return SmartDayArrowWeekdayShifter(weekday, order=1, forward=True)


def second(weekday: Weekday) -> SmartDayArrowWeekdayShifter:
    return SmartDayArrowWeekdayShifter(weekday, order=2, forward=True)


def third(weekday: Weekday) -> SmartDayArrowWeekdayShifter:
    return SmartDayArrowWeekdayShifter(weekday, order=3, forward=True)


def fourth(weekday: Weekday) -> SmartDayArrowWeekdayShifter:
    return SmartDayArrowWeekdayShifter(weekday, order=4, forward=True)


def last(weekday: Weekday) -> SmartDayArrowWeekdayShifter:
    return SmartDayArrowWeekdayShifter(weekday, order=1, forward=False)
