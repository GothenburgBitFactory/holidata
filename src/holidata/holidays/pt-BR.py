# coding=utf-8
from dateutil.easter import EASTER_WESTERN

from .holidays import Locale


# Information gathered from Brazilian legislation.

# National holidays:
# Law 10.607/2002: http://www.planalto.gov.br/ccivil_03/leis/2002/l10607.htm
# Law 6.802/1980:  http://www.planalto.gov.br/ccivil_03/leis/l6802.htm

# State holidays
# AC: State laws 1.538/2004, 1.411/2001, 14/1964, 1.526/2004, and 57/1965
# AL: State laws 5.508/1993, 5.509/1993, 5.724/1995, and Decree 68.782 (30/dec/2019)
# AP: State law 667/2002 and Art. 355 of the Constitution of the Federative Republic of Brazil
# AM: State laws 25/1977 and 84/2010
# BA: Art. 6 of the Constitution of the Federative Republic of Brazil
# CE: State laws 9.093/1995, 9.093/1995 and Art. 18 of the Constitution of the State of Ceará
# DF: District law 963/1995
# ES: State law 11.010/2019
# GO: State law 20.756/2020
# MA: State law 2.457/1964
# MT: State law 7.879/2002
# MS: State law 10/1979
# MG: Art. 256 of the Constitution of the State of Minas Gerais
# PA: State law 5.999/1996
# PB: State law 3.489/1967
# PR: State law 4.658/1962
# PE: State law 13.835/2009
# PI: State law 176/1937
# RJ: State laws 5.243/2008, 5.198/2008, and 4.007/2002
# RN: State laws 7.831/2000 and 8.913/2006
# RS: Art. 6 of the Constitution of the State of Rio Grande do Sul and Decree 36.180 (18/set/1995)
# RO: State laws 2.291/2010 and 1.026/2001
# RR: Art. 9 of the Constitution of the State of Roraima
# SC: State laws 12.906/2004 and 10.306/1996
# SP: State law 9.497/1997
# SE: Art. 269 of the Constitution of the State of Sergipe
# TO: State laws 98/1989, 960/1998, 627/1993


class pt_BR(Locale):
    """
    01-01: [NF] Confraternização Universal
    01-04: [RO] [F] Criação do Estado de Rondônia
    01-23: [AC] [RF] Dia do Evangélico no Acre
    03-06: [PE] [F] Revolução Pernambucana de 1817
    03-08: [AC] [F] Dia Internacional da Mulher
    03-18: [TO] [F] Autonomia do Estado de Tocantins
    03-19: [AP, CE] [RF] Dia de São José
    03-25: [CE] [F] Abolição da Escravidão no Ceará
    04-21: [DF] [F] Fundação de Brasília
    04-21: [MG] [F] Execução de Tiradentes
    04-21: [NF] Tiradentes
    04-23: [RJ] [RF] Dia de São Jorge
    05-01: [NF] Dia Internacional do Trabalhador
    06-15: [AC] [F] Aniversário do Estado do Acre
    06-18: [RO] [RF] Dia do Evangélico em Rondônia
    06-24: [AL, PE] [RF] São João
    06-29: [AL] [RF] São Pedro
    07-02: [BA] [F] Independência da Bahia
    07-08: [SE] [F] Emancipação Política de Sergipe
    07-09: [SP] [F] Revolução Constitucionalista de 1932
    07-26: [GO] [F] Fundação da Cidade de Goiás
    07-28: [MA] [F] Adesão do Maranhão à Independência do Brasil
    08-05: [PB] [F] Fundação do Estado da Paraíba
    08-07: [RN] [F] Dia do Rio Grande do Norte
    08-11: [SC] [F] Dia de Santa Catarina
    08-15: [CE] [RF] Dia de Nossa Senhora da Assunção
    08-15: [PA] [F] Adesão do Pará à Independência do Brasil
    09-05: [AC] [F] Dia da Amazônia
    09-05: [AM] [F] Elevação do Amazonas à Categoria de Província
    09-07: [NF] Independência do Brasil
    09-08: [TO] [F] Nossa Senhora da Natividade
    09-13: [AP] [F] Criação do Território Federal do Amapá
    09-16: [AL] [F] Emancipação Política do Alagoas
    09-20: [RS] [F] Dia do Gaúcho
    10-03: [RN] [F] Mártires de Cunhaú e Uruaçu
    10-05: [RR] [F] Criação dos Estado de Roraima
    10-05: [TO] [F] Criação dos Estado de Tocantins
    10-11: [MS] [F] Criação do Estado do Mato Grosso do Sul
    10-12: [NRF] Nossa Senhora Aparecida
    10-19: [PI] [F] Dia do Piauí
    10-24: [GO] [F] Pedra Fundamental de Goiânia
    11-02: [NRF] Finados
    11-15: [NF] Proclamação da República
    11-17: [AC] [F] Assinatura do Tratado de Petrópolis
    11-20: [AL] [F] Morte de Zumbi dos Palmares
    11-20: [AM, MT, RJ] [F] Dia da Consciência Negra
    11-25: [SC] [RF] Dia de Santa Catarina de Alexandria
    11-30: [DF] [RF] Dia do Evangélico do Distrito Federal
    12-08: [AM] [RF] Nossa Senhora da Conceição
    12-19: [PR] [F] Emancipação Política do Estado do Paraná
    12-25: [NRF] Natal
    47 days before Easter: [NRV] Carnaval
    Easter: [NRV] Páscoa
    """

    locale = "pt-BR"
    easter_type = EASTER_WESTERN
