"""
Provides base class for Locale plugins.
"""

import csv
import io
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

    def __init__(self, locale, region, date, description, flags="", notes="", postpone=False):
        self.locale = locale
        self.region = region
        self.date = date
        self.description = description
        self.flags = flags
        self.notes = notes

        if postpone:
            self.postpone()

    def postpone(self):
        if self.date.weekday() in ['saturday', 'sunday']:
            self.date = self.date.shift_to_weekday('monday', including=True)

    def as_dict(self):
        return {
            'locale': self.locale,
            'region': self.region,
            'date': self.date.strftime('%Y-%m-%d'),
            'description': self.description,
            'type': self.flags,
            'notes': self.notes
        }
