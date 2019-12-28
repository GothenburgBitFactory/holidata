# coding=utf-8
from dateutil.easter import EASTER_WESTERN

from .holidays import Locale


class sk_SK(Locale):
    """
    01-01: [NF] Deň vzniku Slovenskej republiky
    01-06: [NRF] Zjavenie Pána / Traja králi
    05-01: [NF] Sviatok práce
    05-08: [NF] Deň víťazstva nad fašizmom
    07-05: [NRF] Sviatok svätého Cyrila a Metoda
    08-29: [NF] Výročie SNP
    09-01: [NF] Deň Ústavy Slovenskej republiky
    09-15: [NRF] Sedembolestná Panna Mária
    11-01: [NRF] Sviatok všetkých svätých
    11-17: [NF] Deň boja za slobodu a demokraciu
    12-24: [NRF] Štedrý deň
    12-25: [NRF] Prvý sviatok vianočný
    12-26: [NRF] Druhý sviatok vianočný
    2 days before Easter: [NRV] Veľký piatok
    1 day after Easter: [NRV] Veľkonočný pondelok
    """

    locale = "sk-SK"
    easter_type = EASTER_WESTERN
