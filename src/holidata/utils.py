"""
Provides date-handling related utils.
"""
from typing import Callable

from arrow import Arrow

WEEKDAYS = [
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday"
]

MONTHS = [
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december"
]


class SmartDayArrow(Arrow):
    """
    A wrapper around Arrow datetime reference that provides additional convenience methods.
    """

    def weekday(self) -> str:
        """
        Provide a more readable weekday representation.
        """

        return WEEKDAYS[super().weekday()]

    def shift_to_weekday(self, day: str, order: int = 1, reverse: bool = False, including: bool = False) -> 'SmartDayArrow':
        """
        Shifts to {order}. weekday in the given direction, i.e. 2. monday before this date would be:

        >>> arrow.shift_to_weekday("monday", order=2, reverse=True)
        """

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


def date(month: int, day: int) -> Callable[[int], SmartDayArrow]:
    def wrapper(year: int):
        return SmartDayArrow(year, month, day)

    return wrapper


class SmartDayArrowDayShifter:
    def __init__(self, days):
        self.day_count: int = days
        self.shift_direction: int = 0
        self.date: callable = None

    def before(self, date: callable) -> 'SmartDayArrowDayShifter':
        self.date = date
        self.shift_direction = -1
        return self

    def after(self, date: callable) -> 'SmartDayArrowDayShifter':
        self.date = date
        self.shift_direction = 1
        return self

    def __call__(self, year: int) -> SmartDayArrow:
        return self.date(year).shift(days=self.day_count * self.shift_direction)


def day(count: int) -> SmartDayArrowDayShifter:
    return SmartDayArrowDayShifter(count)


class SmartDayArrowWeekdayShifter:
    def __init__(self, weekday: str, order: int, forward: bool):
        self.weekday = weekday
        self.order = order
        self.forward = forward
        self.including = True
        self.date = None

    def of(self, month: str) -> 'SmartDayArrowWeekdayShifter':
        month_index = MONTHS.index(month.lower()) + 1

        if self.forward:
            self.date = date(month_index, 1)
        else:
            def wrapper(year):
                return SmartDayArrow(
                    year if month_index != 12 else year + 1,
                    (month_index % 12) + 1,
                    1).shift(days=-1)

            self.date = wrapper

        return self

    def before(self, date: callable = None, month: int = None, day: int = None, including: bool = False) -> 'SmartDayArrowWeekdayShifter':
        self._configure_shift(date, month, day, False, including)
        return self

    def after(self, date: callable = None, month: int = None, day: int = None, including: bool = False) -> 'SmartDayArrowWeekdayShifter':
        self._configure_shift(date, month, day, True, including)
        return self

    def _configure_shift(self, date_func: callable, month: int, day: int, forward: bool, including: bool):
        if month is not None and day is not None:
            self.date = date(month, day)
        elif callable(date_func):
            self.date = date_func
        else:
            raise ValueError("Invalid reference date")

        self.forward = forward
        self.including = including

    def __call__(self, year: int) -> SmartDayArrow:
        return self.date(year).shift_to_weekday(
            self.weekday,
            order=self.order,
            reverse=not self.forward,
            including=self.including,
        )


def first(weekday: str) -> SmartDayArrowWeekdayShifter:
    return SmartDayArrowWeekdayShifter(weekday, order=1, forward=True)


def second(weekday: str) -> SmartDayArrowWeekdayShifter:
    return SmartDayArrowWeekdayShifter(weekday, order=2, forward=True)


def third(weekday: str) -> SmartDayArrowWeekdayShifter:
    return SmartDayArrowWeekdayShifter(weekday, order=3, forward=True)


def fourth(weekday: str) -> SmartDayArrowWeekdayShifter:
    return SmartDayArrowWeekdayShifter(weekday, order=4, forward=True)


def last(weekday: str) -> SmartDayArrowWeekdayShifter:
    return SmartDayArrowWeekdayShifter(weekday, order=1, forward=False)
