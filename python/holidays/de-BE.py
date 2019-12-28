# coding=utf-8
from dateutil.easter import EASTER_WESTERN

from .holidays import Locale


class de_BE(Locale):
    """
    01-01: [NF] Neujahr
    05-01: [NF] Tag der Arbeit
    07-21: [NF] Nationalfeiertag
    08-15: [NRF] Mariä Himmelfahrt
    11-01: [NRF] Allerheiligen
    11-11: [NF] Waffenstillstand
    12-25: [NRF] Weihnacht
    Easter: [NRV] Ostern
    1 day after Easter: [NRV] Ostermontag
    39 days after Easter: [NRV] Christi Himmelfahrt
    49 days after Easter: [NRV] Pfingsten
    50 days after Easter: [NRV] Pfingstmontag
    """

    locale = "de-BE"
    easter_type = EASTER_WESTERN
