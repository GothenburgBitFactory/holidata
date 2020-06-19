# coding=utf-8
from dateutil.easter import EASTER_WESTERN

from .holidays import Locale


class en_US(Locale):
    """
    01-01: [NF] New Year's Day
    07-04: [NF] Independence Day
    11-11: [NF] Veterans Day
    12-24: [NRF] Christmas Eve
    12-25: [NRF] Christmas Day
    3. monday in January: [NV] Birthday of Martin Luther King, Jr.
    3. monday in February: [NV] Washington's Birthday
    3. monday in April: [MA,ME] [V] Patriots' Day
    1. last monday in May: [NV] Memorial Day
    1. monday in September: [NV] Labor Day
    2. monday in October: [NV] Columbus Day
    4. thursday in November: [NV] Thanksgiving Day
    4. friday in November: [NV] Day after Thanksgiving
    """

    locale = "en-US"
    easter_type = EASTER_WESTERN
