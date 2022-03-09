# coding=utf-8
from dateutil.easter import EASTER_WESTERN

from .holidays import Locale

"""
sources
https://www.riigiteataja.ee/akt/109032011007 (Public Holidays and Days of National Importance Act)
"""


class et_EE(Locale):
    """
    01-01: [NF] Uusaasta
    02-24: [NF] Iseseisvuspäev, Eesti Vabariigi aastapäev
    05-01: [NF] Kevadpüha
    06-23: [NF] Võidupüha
    06-24: [NF] Jaanipäev
    08-20: [NF] Taasiseseisvumispäev
    12-24: [NF] Jõululaupäev
    12-25: [NF] Esimene jõulupüha
    12-26: [NF] Teine jõulupüha
    2 days before Easter: [NRV] Suur reede
    Easter: [NRV] Ülestõusmispühade 1. püha
    49 days after Easter: [NRV] Nelipühade 1. püha
    """

    locale = "et-EE"
    easter_type = EASTER_WESTERN
