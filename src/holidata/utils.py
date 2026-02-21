"""
Provides date-handling related utils.
"""
from enum import IntEnum
from typing import Callable, Dict, List, Tuple, Union

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


class DateWrapper:
    def __init__(self, date_lookup: Union[Dict[int, Tuple[Month, int]], None] = None, default: Callable[[int], Union[Arrow, None]] = None):
        self.dates = date_lookup if date_lookup is not None else {}
        self.default_func = default

    def is_a(self, weekday: Weekday) -> Callable[[int], bool]:
        def wrapper(year):
            this = self(year)
            return this.weekday() == weekday if this is not None else False

        return wrapper

    def is_not_a(self, weekday: Weekday) -> Callable[[int], bool]:
        def wrapper(year):
            this = self(year)
            return this.weekday() != weekday if this is not None else False

        return wrapper

    def is_one_of(self, selection: List[Weekday]):
        def wrapper(year):
            this = self(year)
            return this.weekday() in selection if this is not None else False

        return wrapper

    def is_none_of(self, selection: List[Weekday]):
        def wrapper(year):
            this = self(year)
            return this.weekday() not in selection if this is not None else False

        return wrapper

    def is_equal_to(self, other):
        def wrapper(year):
            return self(year) == other(year)

        return wrapper

    def is_not_equal_to(self, other: Callable[[int], Arrow]):
        def wrapper(year):
            return self(year) != other(year)

        return wrapper

    def or_else_on(self, date_func: Callable[[int], Union[Arrow, None]]) -> 'DateWrapper':
        self.default_func = date_func

        return self

    def except_for(self, date_lookup: Dict[int, Tuple[Month, int]]):
        self.dates = date_lookup

        return self

    def __call__(self, year: int) -> Union[Arrow, None]:
        if year in self.dates:
            return Arrow(year, self.dates[year][0].value, self.dates[year][1]) if self.dates[year] is not None else None

        if self.default_func is not None:
            return self.default_func(year)

        return None


def date(month: Month, day: int) -> DateWrapper:
    return DateWrapper(default=lambda year: Arrow(year, month, day))


def dates(dates_map: Union[Dict[int, Tuple[Month, int]], None]) -> DateWrapper:
    return DateWrapper(date_lookup=dates_map)


class DayShifter:
    def __init__(self, days):
        self.day_count: int = days
        self.shift_direction: int = 0
        self.date: Callable[[int], Union[Arrow, None]] = lambda year: None

    def before(self, date_func: Callable[[int], Arrow]) -> 'DayShifter':
        self.date = date_func
        self.shift_direction = -1
        return self

    def after(self, date_func: Callable[[int], Arrow]) -> 'DayShifter':
        self.date = date_func
        self.shift_direction = 1
        return self

    def __call__(self, year: int) -> Union[Arrow, None]:
        return self.date(year).shift(days=self.day_count * self.shift_direction) if self.date is not None and self.date(year) is not None else None


def day(count: int) -> DayShifter:
    return DayShifter(count)


class WeekdayShifter:
    def __init__(self, weekday: Weekday, order: int, forward: bool):
        self.weekday = weekday
        self.order = order
        self.forward = forward
        self.including = True
        self.date = None

    def of(self, month: Month) -> 'WeekdayShifter':
        month_index = month.value

        if self.forward:
            self.date = date(month, 1)
        else:
            def wrapper(year):
                return Arrow(
                    year if month_index != 12 else year + 1,
                    (month_index % 12) + 1,
                    1).shift(days=-1)

            self.date = wrapper

        return self

    def before(self, date_func: Callable[[int], Arrow], including: bool = False) -> 'WeekdayShifter':
        self._configure_shift(date_func, False, including)
        return self

    def after(self, date_func: Callable[[int], Arrow], including: bool = False) -> 'WeekdayShifter':
        self._configure_shift(date_func, True, including)
        return self

    def _configure_shift(self, date_func: Callable[[int], Arrow], forward: bool, including: bool):
        self.date = date_func
        self.forward = forward
        self.including = including

    def _calculate_shift(self, holiday_date):
        if self.order <= 0:
            raise ValueError("Order must be greater than 0")

        # Calculate the weekday difference (positive for forward, negative for reverse)
        weekday_diff = ((self.weekday - holiday_date.weekday()) * (-1 if not self.forward else 1)) % 7

        # Adjust for the case where we're already on the target weekday but not including it
        if weekday_diff == 0 and not self.including:
            weekday_diff = 7

        # Calculate the days needed for the weeks shift of order > 1
        weeks_offset = (self.order - 1) * 7

        # Calculate total shift
        total_days = weekday_diff + weeks_offset

        # Apply the shift (negative for reverse direction)
        return total_days * (-1 if not self.forward else 1)

    def __call__(self, year: int) -> Union[Arrow, None]:
        holiday_date = self.date(year) if self.date is not None else None
        shift = self._calculate_shift(holiday_date)
        return holiday_date.shift(days=shift) if holiday_date is not None else None


def first(weekday: Weekday) -> WeekdayShifter:
    return WeekdayShifter(weekday, order=1, forward=True)


def second(weekday: Weekday) -> WeekdayShifter:
    return WeekdayShifter(weekday, order=2, forward=True)


def third(weekday: Weekday) -> WeekdayShifter:
    return WeekdayShifter(weekday, order=3, forward=True)


def fourth(weekday: Weekday) -> WeekdayShifter:
    return WeekdayShifter(weekday, order=4, forward=True)


def last(weekday: Weekday) -> WeekdayShifter:
    return WeekdayShifter(weekday, order=1, forward=False)
