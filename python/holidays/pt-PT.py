# coding=utf-8
from dateutil.easter import EASTER_WESTERN

from .holidays import Locale


class pt_PT(Locale):
    """
    01-01: [NF] Ano Novo
    04-25: [NF] Dia da Liberdade
    05-01: [NF] Dia do Trabalhador
    06-10: [NF] Dia de Portugal
    08-15: [NF] Assunção de Nossa Senhora
    10-05: [NF] Implantação da República
    11-01: [NF] Dia de Todos os Santos
    12-01: [NF] Restauração da Independência
    12-08: [NF] Imaculada Conceição
    12-25: [NF] Natal
    47 days before Easter: [NRV] Carnaval
    2 days before Easter: [NRV] Sexta-feira Santa
    Easter: [NRV] Páscoa
    60 days after Easter: [NRV] Corpo de Deus
    """

    locale = "pt-PT"
    easter_type = EASTER_WESTERN
