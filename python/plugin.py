"""
Provides base class for Country plugins.
"""

import json
import re
from utils import SmartDayArrow, easter, month_reference

class PluginMount(type):
    """
    Metaclass that makes a given class plugin mount (all classes inheriting
    will be referenced in the 'plugins' attribute.
    """

    def __init__(cls, name, bases, attrs):
        super(PluginMount, cls).__init__(name, bases, attrs)

        if not hasattr(cls, 'plugins'):
            cls.plugins = []
        else:
            cls.plugins.append(cls)


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


class Country(object, metaclass=PluginMount):
    """
    Represents holidays in a given country.
    """

    locale = None
    region = None

    def __init__(self, year):
        if self.locale is None:
            raise ValueError("Country {0} does not provide its locale"
                             .format(self.__class__.__name__))

        self.year = year


    @property
    def holidays(self):
        """
        Yield all the Holiday objects corresponding to the definitions in the
        self.__doc__ and also as given by the dynamic self.holiday_* methods.
        """

        # First process lines in the __doc__
        for line in self.__doc__.splitlines():
            # Skip empty lines
            if not line.strip():
                continue

            fixed_regex = re.compile(
                r'^\s*(?P<month>\d\d)-(?P<day>\d\d): '
                 '\[(?P<flags>[A-Z]*)\] (?P<description>.*)$',
                re.UNICODE
            )

            nth_weekday_regex = re.compile(
                r'^\s*(?P<order>\d+)\.(?P<last> last | )'
                 '(?P<weekday>[a-z]+) in (?P<month>[a-zA-Z]+):\s+'
                 '\[(?P<flags>[A-Z]*)\] (?P<description>.*)$',
                re.UNICODE
            )

            easter_shift_regex = re.compile(
                r'^\s*(?P<days>\d+) day(s)? (?P<direction>(before|after)) Easter:\s+'
                 '\[(?P<flags>[A-Z]*)\] (?P<description>.*)$',
                re.UNICODE
            )

            # fixed
            m = fixed_regex.search(line)
            if m is not None:
                yield Holiday(
                    SmartDayArrow(self.year, int(m.group('month')), int(m.group('day'))),
                    m.group('description'),
                    m.group('flags')
                )
                continue

            # reference points to nth day in a month
            m = nth_weekday_regex.search(line)
            if m is not None:
                yield Holiday(
                    month_reference(self.year, m.group('month'),
                                    first=m.group('last').strip() is '')
                        .shift_to_weekday(m.group('weekday'),
                                          order=int(m.group('order')),
                                          reverse=m.group('last').strip() is 'last'
                    ),
                    m.group('description'),
                    m.group('flags')
                )
                continue

            # easter reference points
            m = easter_shift_regex.search(line)
            if m is not None:
                yield Holiday(
                    easter(self.year).shift(
                        days=int(m.group('days')) *
                             (1 if m.group('direction') == 'after' else -1),
                    ),
                    m.group('description'),
                    m.group('flags')
                )
                continue

            print("Following line could not be processed: '{}'".format(line))

        # method dynamic
        yield from [
            getattr(self, method)(self.year)
            for method in dir(self)
            if method.startswith('holiday_')
        ]

    def to_json(self):
        export_data = [h.as_dict() for h in self.holidays]
        return json.dumps(export_data, ensure_ascii=False, sort_keys=True, indent=2)
