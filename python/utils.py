"""
Provides date-handling related utils.
"""

from arrow import Arrow


class SmartDayArrow(Arrow):
    """
    A wrapper around Arrow datetime reference that provides additional
    convenience methods.
    """

    def weekday(self):
        """
        Provide a more readable weekday representation.
        """

        weekdays = [
            'monday',
            'tuesday',
            'wednesday',
            'thursday',
            'friday',
            'saturday',
            'sunday',
        ]

        return weekdays[Arrow.weekday(self)]

    def shift_to_weekday(self, day, order=1, reverse=False, including=False):
        """
        Shifts to {order}. weekday in the given direction, i.e.
        2. monday before this date woud be:

        >>> arrow.shift_to_weekday('monday', order=2, reverse=True)
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


def paschal_full_moon_date(year):
    """
    Returns Paschal Full Moon date, used to compute easter things.
    """

    pfmd = SmartDayArrow(year, 3, 1)

    PFMd_shift = 44 - (((year % 19) * 11) % 30)

    if year % 19 in (5, 16):
        PFMd_shift += 29
    if year % 19 == 8:
        PFMd_shift += 30

    return pfmd.shift(days=PFMd_shift)


def easter(year):
    pfmd = paschal_full_moon_date(year)
    return pfmd.shift_to_weekday('sunday')


def month_reference(year, month, first=True):
    months = [
        'january',
        'february',
        'march',
        'april',
        'may',
        'june',
        'july',
        'august',
        'september',
        'october',
        'november',
        'december',
    ]

    month = months.index(month.lower()) + 1

    if first:
        return SmartDayArrow(year, month, 1)
    else:
        return SmartDayArrow(
            year if month != 12 else year+1,
            month+1 if month != 12 else 1,
            1).shift(days=-1)
