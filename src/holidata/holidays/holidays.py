import re

from holidata.plugin import PluginMount
from holidata.utils import SmartDayArrow, month_reference, easter


class Holiday(object):
    """
    A sheer container for one holiday.
    """

    def __init__(self, locale, region, date, description, flags="", notes=""):
        self.locale = locale
        self.region = region
        self.date = date
        self.description = description
        self.flags = flags
        self.notes = notes

    def as_dict(self):
        return {
            "locale": self.locale,
            "region": self.region,
            "date": self.date.strftime("%Y-%m-%d"),
            "description": self.description,
            "type": self.flags,
            "notes": self.notes
        }


class Country(object, metaclass=PluginMount):
    """
    Represents holidays of a given country
    """
    id = None
    languages = []
    default_lang = None
    easter_type = None

    def __init__(self):
        if self.id is None:
            raise ValueError(f"Country '{self.__class__.__name__}' does not provide its id!")

        if not self.languages:
            raise ValueError(f"Country '{self.__class__.__name__}' does not list any languages!")

        if self.default_lang is not None and self.default_lang not in self.languages:
            raise ValueError(f"Country '{self.__class__.__name__}' does not list language '{self.default_lang}'!")

    @staticmethod
    def get(identifier):
        return Country.get_plugin(identifier, "id")


class Locale(object, metaclass=PluginMount):
    """
    Represents holidays in a given locale.
    """
    locale = None
    easter_type = None

    fixed_regex = re.compile(r"^\s*(?P<month>\d\d)-(?P<day>\d\d): "
                             r"(\[(?P<regions>[^]]+)\]\s+)?"
                             r"\[(?P<flags>[A-Z]*)\] (?P<description>.*)$", re.UNICODE)
    nth_weekday_regex = re.compile(r"^\s*(?P<order>\d+)\.(?P<last> last | )"
                                   r"(?P<weekday>[a-z]+) in (?P<month>[a-zA-Z]+):\s+"
                                   r"(\[(?P<regions>[^]]+)\]\s+)?"
                                   r"\[(?P<flags>[A-Z]*)\] (?P<description>.*)$", re.UNICODE)
    easter_shift_regex = re.compile(r"^\s*((?P<days>\d+) day(s)? (?P<direction>(before|after)) )?Easter:\s+"
                                    r"(\[(?P<regions>[^]]+)\]\s+)?"
                                    r"\[(?P<flags>[A-Z]*)\] (?P<description>.*)$", re.UNICODE)

    def __init__(self, year):
        if self.locale is None:
            raise ValueError(f"Locale {self.__class__.__name__} does not provide its locale")

        self.year = year

    @staticmethod
    def get(identifier):
        return Locale.get_plugin(identifier, "locale")

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
                print(f"Following line could not be processed: '{line}'")
                continue

            for region in holidata["regions"]:
                yield Holiday(
                    locale=self.locale,
                    region=region,
                    date=holidata["date"],
                    description=holidata["description"],
                    flags=holidata["flags"],
                    notes=holidata["notes"],
                )

        # Second, call holiday functions
        for method in [getattr(self, func) for func in dir(self) if func.startswith("holiday_")]:
            holidays = method()

            for holiday in holidays:
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
                return dict(regions=([x.strip() for x in m.group("regions").split(",")] if m.group("regions") is not None else [""]),
                            date=create_date_from(m),
                            description=m.group("description"),
                            flags=m.group("flags"),
                            notes="")

        return None

    def _date_from_fixed_reference(self, m):
        return SmartDayArrow(self.year, int(m.group("month")), int(m.group("day")))

    def _date_from_weekday_reference(self, m):
        return month_reference(self.year,
                               m.group("month"),
                               first=m.group("last").strip() == "") \
            .shift_to_weekday(m.group("weekday"),
                              order=int(m.group("order")),
                              reverse=m.group("last").strip() == "last",
                              including=True)

    def _date_from_easter_reference(self, m):
        if self.easter_type is None:
            raise ValueError(f"Locale {self.__class__.__name__} does not provide its easter type (WESTERN|ORTHODOX)")

        return easter(self.year, self.easter_type) \
            .shift(days=int((m.group("days")) if m.group("days") is not None else 0) * (1 if m.group("direction") == "after" else -1))
