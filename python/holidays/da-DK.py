# coding=utf-8
from dateutil.easter import EASTER_WESTERN

from .holidays import Locale


class da_DK(Locale):
    """
    01-01: [NF] Nytårsdag
    06-05: [NF] Grundlovsdag
    12-25: [NRF] Juledag
    12-26: [NRF] Anden juledag
    3 days before Easter: [NRV] Skærtorsdag
    2 days before Easter: [NRV] Langfredag
    Easter: [NRV] Påskedag
    1 day after Easter: [NRV] Anden påskedag
    26 days after Easter: [NRV] Store bededag
    39 days after Easter: [NRV] Kristi himmelfartsdag
    49 days after Easter: [NRV] Pinsedag
    50 days after Easter: [NRV] Anden pinsedag
    """

    locale = "da-DK"
    easter_type = EASTER_WESTERN
