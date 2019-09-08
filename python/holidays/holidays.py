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

    fixed_regex = re.compile(r'^\s*(?P<month>\d\d)-(?P<day>\d\d): '
                             r'(\[(?P<regions>[^]]+)\]\s+)?'
                             r'\[(?P<flags>[A-Z]*)\] (?P<description>.*)$', re.UNICODE)
    nth_weekday_regex = re.compile(r'^\s*(?P<order>\d+)\.(?P<last> last | )'
                                   r'(?P<weekday>[a-z]+) in (?P<month>[a-zA-Z]+):\s+'
                                   r'(\[(?P<regions>[^]]+)\]\s+)?'
                                   r'\[(?P<flags>[A-Z]*)\] (?P<description>.*)$', re.UNICODE)
    easter_shift_regex = re.compile(r'^\s*(?P<days>\d+) day(s)? (?P<direction>(before|after)) Easter:\s+'
                                    r'(\[(?P<regions>[^]]+)\]\s+)?'
                                    r'\[(?P<flags>[A-Z]*)\] (?P<description>.*)$', re.UNICODE)

    def __init__(self, year):
        if self.locale is None:
            raise ValueError("Locale {0} does not provide its locale".format(self.__class__.__name__))

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

            holidata = self._parse_holidata(line)

            if holidata is None:
                print("Following line could not be processed: '{}'".format(line))
                continue

            for region in holidata['regions']:
                yield Holiday(
                    locale=self.locale,
                    region=region,
                    date=holidata['date'],
                    description=holidata['description'],
                    flags=holidata['flags'],
                    notes=holidata['notes'],
                    postpone=self.postpone,
                )

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

    def _parse_holidata(self, line):
        function_map = [
            (self.fixed_regex, self._date_from_fixed_reference),
            (self.nth_weekday_regex, self._date_from_weekday_reference),
            (self.easter_shift_regex, self._date_from_easter_reference),
        ]

        for reg_exp, create_date_from in function_map:
            m = reg_exp.search(line)
            if m is not None:
                return dict(regions=(m.group('regions').split(',') if m.group('regions') is not None else [""]),
                            date=create_date_from(m),
                            description=m.group('description'),
                            flags=m.group('flags'), notes="")

        return None

    def _date_from_fixed_reference(self, m):
        return SmartDayArrow(self.year, int(m.group('month')), int(m.group('day')))

    def _date_from_weekday_reference(self, m):
        return month_reference(self.year,
                               m.group('month'),
                               first=m.group('last').strip() is '') \
            .shift_to_weekday(m.group('weekday'),
                              order=int(m.group('order')),
                              reverse=m.group('last').strip() == 'last',
                              including=True)

    def _date_from_easter_reference(self, m):
        return easter(self.year) \
            .shift(days=int(m.group('days')) * (1 if m.group('direction') == 'after' else -1))

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
