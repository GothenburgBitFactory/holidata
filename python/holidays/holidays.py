import csv
import io
import json
import re

from plugin import PluginMount, Holiday
from utils import SmartDayArrow, month_reference, easter


class Locale(object, metaclass=PluginMount):
    """
    Represents holidays in a given locale.
    """

    locale = None

    postpone = False

    def __init__(self, year):
        if self.locale is None:
            raise ValueError("Locale {0} does not provide its locale"
                             .format(self.__class__.__name__))

        self.year = year

    @property
    def holidays(self):
        """
        Yield all the Holiday objects corresponding to the definitions in the
        self.__doc__ and also as given by the dynamic self.holiday_* methods.
        """

        fixed_regex = re.compile(
            r'^\s*(?P<month>\d\d)-(?P<day>\d\d): '
            r'(\[(?P<regions>[^]]+)\]\s+)?'
            r'\[(?P<flags>[A-Z]*)\] (?P<description>.*)$',
            re.UNICODE
        )

        nth_weekday_regex = re.compile(
            r'^\s*(?P<order>\d+)\.(?P<last> last | )'
            r'(?P<weekday>[a-z]+) in (?P<month>[a-zA-Z]+):\s+'
            r'(\[(?P<regions>[^]]+)\]\s+)?'
            r'\[(?P<flags>[A-Z]*)\] (?P<description>.*)$',
            re.UNICODE
        )

        easter_shift_regex = re.compile(
            r'^\s*(?P<days>\d+) day(s)? (?P<direction>(before|after)) Easter:\s+'
            r'(\[(?P<regions>[^]]+)\]\s+)?'
            r'\[(?P<flags>[A-Z]*)\] (?P<description>.*)$',
            re.UNICODE
        )

        # First process lines in the __doc__
        for line in self.__doc__.splitlines():
            # Skip empty lines
            if not line.strip():
                continue

            # fixed
            m = fixed_regex.search(line)
            if m is not None:
                regions = m.group('regions').split(',') if m.group('regions') is not None else [""]

                for region in regions:
                    yield Holiday(
                        self.locale,
                        region,
                        SmartDayArrow(self.year, int(m.group('month')), int(m.group('day'))),
                        m.group('description'),
                        m.group('flags'),
                        postpone=self.postpone
                    )
                continue

            # reference points to nth day in a month
            m = nth_weekday_regex.search(line)
            if m is not None:
                regions = m.group('regions').split(',') if m.group('regions') is not None else [""]

                for region in regions:
                    yield Holiday(
                        self.locale,
                        region,
                        month_reference(self.year, m.group('month'),
                                        first=m.group('last').strip() is '')
                            .shift_to_weekday(m.group('weekday'),
                                              order=int(m.group('order')),
                                              reverse=m.group('last').strip() == 'last',
                                              including=True
                                              ),
                        m.group('description'),
                        m.group('flags'),
                        postpone=self.postpone
                    )
                continue

            # easter reference points
            m = easter_shift_regex.search(line)
            if m is not None:
                regions = m.group('regions').split(',') if m.group('regions') is not None else [""]

                for region in regions:
                    yield Holiday(
                        self.locale,
                        region,
                        easter(self.year).shift(
                            days=int(m.group('days')) *
                                 (1 if m.group('direction') == 'after' else -1),
                        ),
                        m.group('description'),
                        m.group('flags'),
                        postpone=self.postpone
                    )
                continue

            print("Following line could not be processed: '{}'".format(line))

        # method dynamic
        dynamic_methods = [
            getattr(self, method)
            for method in dir(self)
            if method.startswith('holiday_')
        ]

        for method in dynamic_methods:
            holiday = method(self.year)

            # Handle postponing if the class attribute for postponing is set
            if self.postpone:
                holiday.postpone()

            yield holiday

    def to_json(self):
        export_data = [h.as_dict() for h in self.holidays]
        export_data.sort(key=lambda x: x['date'])
        return json.dumps(export_data, ensure_ascii=False, sort_keys=True, indent=2)

    def to_csv(self):
        export_data = [h.as_dict() for h in self.holidays]
        export_data.sort(key=lambda x: x['date'])
        result = io.StringIO()

        writer = csv.DictWriter(result,
                                ["locale", "region", "date", "description", "type", "notes"],
                                quoting=csv.QUOTE_ALL,
                                lineterminator='\n')
        writer.writeheader()
        writer.writerows(export_data)

        return result.getvalue()
