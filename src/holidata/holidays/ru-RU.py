# coding=utf-8
from dateutil.easter import EASTER_ORTHODOX

from .holidays import Locale


class ru_RU(Locale):
    """
    01-01: [NF] Новый Год
    01-07: [NRF] Рождество Христово
    02-23: [NF] День защитника Отечества
    03-08: [NF] Международный женский день
    05-01: [NF] Праздник весны и труда
    05-09: [NF] День Победы
    06-12: [NF] День России
    11-04: [NF] День народного единства
    Easter: [NRV] Пасха
    """

    locale = "ru-RU"
    easter_type = EASTER_ORTHODOX
