#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Holidata - generate holidata files.

Usage:
  holidata.py (--year=<value>) (--locale=<value>)

Options:
    --year=<value>       Specify which year to generate data for.
    --locale=<value>     Specify the locale for which data should be generated.

Dependencies:
    pip3 install arrow docopt
"""

import sys
import json
import re

from arrow import Arrow
from docopt import docopt


class SmartDayArrow(Arrow):

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
    months = ['january', 'february', 'march', 'april', 'may', 'june',
              'july', 'august', 'september', 'october', 'november', 'december']
    month = months.index(month.lower()) + 1

    if first:
        return SmartDayArrow(year, month, 1)
    else:
        return SmartDayArrow(
            year if month != 12 else year+1,
            month+1 if month != 12 else 1,
            1).shift(days=-1)


class PluginMount(type):

    def __init__(cls, name, bases, attrs):
        super(PluginMount, cls).__init__(name, bases, attrs)

        if not hasattr(cls, 'plugins'):
            cls.plugins = []
        else:
            cls.plugins.append(cls)


class Country(object, metaclass=PluginMount):

    locale = None
    region = None

    def __init__(self, year):
        if self.locale is None:
            raise ValueError("Country {0} does not provide its locale"
                             .format(self.__class__.__name__))

        self.year = year


    @property
    def holidays(self):
        fixed_regex = re.compile(
            r'^\s*(?P<month>\d\d)-(?P<day>\d\d): '
             '\[(?P<flags>[A-Z]*)\] (?P<description>.*)$',
            re.MULTILINE | re.UNICODE
        )

        nth_weekday_regex = re.compile(
            r'^\s*(?P<order>\d+)\.(?P<last> last | )(?P<weekday>[a-z]+) in (?P<month>[a-zA-Z]+):\s+'
             '\[(?P<flags>[A-Z]*)\] (?P<description>.*)$',
            re.MULTILINE | re.UNICODE
        )

        easter_shift_regex = re.compile(
            r'^\s*(?P<days>\d+) day(s)? (?P<direction>before|after) Easter: \s+'
             '\[(?P<flags>[A-Z]*)\] (?P<description>.*)$',
            re.MULTILINE | re.UNICODE
        )

        # fixed
        yield from [
            Holiday(
                SmartDayArrow(self.year, int(m.group('month')), int(m.group('day'))),
                m.group('description'),
                m.group('flags')
            )
            for m in fixed_regex.finditer(self.__doc__)
        ]

        # reference points to nth day in a month
        yield from [
            Holiday(
                month_reference(self.year, m.group('month'), first=m.group('last').strip() is '')
                    .shift_to_weekday(m.group('weekday'),
                                      order=int(m.group('order')),
                                      reverse=m.group('last').strip() is 'last'
                ),
                m.group('description'),
                m.group('flags')
            )
            for m in nth_weekday_regex.finditer(self.__doc__)
        ]

        # easter reference points
        yield from [
            Holiday(
                easter(self.year).shift(
                    days=int(m.group('days')) * (1 if m.group('direction') == 'after' else -1),
                ),
                m.group('description'),
                m.group('flags')
            )
            for m in easter_shift_regex.finditer(self.__doc__)
        ]

        # method dynamic
        yield from [
            getattr(self, method)(self.year)
            for method in dir(self)
            if method.startswith('holiday_')
        ]

    def to_json(self):
        export_data = [h.as_dict() for h in self.holidays]
        return json.dumps(export_data, ensure_ascii=False, sort_keys=True, indent=2)


class Holiday(object):
    """
    A sheer container for one holiday.
    """

    def __init__(self, date, description, flags="", notes=""):
        self.date = date
        self.description = description
        self.flags = flags
        self.notes = notes

    def as_dict(self):
        return {
            'date': self.date.strftime('%Y-%m-%d'),
            'description': self.description,
            'type': self.flags,
            'notes': self.notes
        }


class Slovakia(Country):
    u"""
    01-01: [NF] Deň vzniku Slovenskej republiky
    01-06: [NRF] Zjavenie Pána / Traja králi
    05-01: [NF] Sviatok práce
    05-08: [NF] Deň víťazstva nad fašizmom
    07-05: [NRF] Sviatok svätého Cyrila a Metoda
    08-29: [NF] Výročie SNP
    09-01: [NF] Deň Ústavy Slovenskej republiky
    09-15: [NRF] Sedembolestná Panna Mária
    11-01: [NRF] Sviatok všetkých svätých
    11-17: [NF] Deň boja za slobodu a demokraciu
    12-24: [NRF] Štedrý deň
    12.25: [NRF] Prvý sviatok vianočný
    12-26: [NRF] Druhý sviatok vianočný
    1 days after Easter:  [NRV] Veľký piatok
    2 days before Easter: [NRV] Veľkonočný pondelok
    """

    locale = "sk-SK"


class USA(Country):
    u"""
    01-01: [NF] New Year's Day
    07-04: [NF] Independence Day
    11-11: [NF] Veterans Day
    11-24: [NV] Thanksgiving Day
    12-25: [NRF] Christmas Day
    3. monday in January:    [V] Birthday of Martin Luther King, Jr.
    3. monday in February:   [NV] Washington's Birthday
    3. monday in April:      [NV] Patriot's day
    1. last monday in May:   [NV] Memorial day
    1. monday in September:  [NV] Labor Day
    2. monday in October:    [NV] Columbus Day
    4. thursday in November: [NV] Thanksgiving Day
    """

    locale = "en-US"


if __name__ == '__main__':
    args = docopt(__doc__)
    class_candidates = [cls for cls in Country.plugins if cls.locale == args['--locale']]

    if class_candidates:
        country = class_candidates[0](int(args['--year']))
        print(country.to_json())
    else:
        sys.exit("No plugin fonud for locale: {}".format(args['--locale']))
