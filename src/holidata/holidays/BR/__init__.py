from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import day

__all__ = [
    "BR",
]


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


class BR(Country):
    id = "BR"
    languages = ["pt"]
    default_lang = "pt"
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Confraternização Universal") \
            .on(month=1, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Criação do Estado de Rondônia") \
            .in_regions(["RO"]) \
            .on(month=1, day=4) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Dia do Evangélico no Acre") \
            .in_regions(["AC"]) \
            .on(month=1, day=23) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Revolução Pernambucana de 1817") \
            .in_regions(["PE"]) \
            .on(month=3, day=6) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Dia Internacional da Mulher") \
            .in_regions(["AC"]) \
            .on(month=3, day=8) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Autonomia do Estado de Tocantins") \
            .in_regions(["TO"]) \
            .on(month=3, day=18) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Dia de São José") \
            .in_regions(["AP", "CE"]) \
            .on(month=3, day=19) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Abolição da Escravidão no Ceará") \
            .in_regions(["CE"]) \
            .on(month=3, day=25) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Fundação de Brasília") \
            .in_regions(["DF"]) \
            .on(month=4, day=21) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Execução de Tiradentes") \
            .in_regions(["MG"]) \
            .on(month=4, day=21) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Tiradentes") \
            .on(month=4, day=21) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Dia de São Jorge") \
            .in_regions(["RJ"]) \
            .on(month=4, day=23) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Dia Internacional do Trabalhador") \
            .on(month=5, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Aniversário do Estado do Acre") \
            .in_regions(["AC"]) \
            .on(month=6, day=15) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Dia do Evangélico em Rondônia") \
            .in_regions(["RO"]) \
            .on(month=6, day=18) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("São João") \
            .in_regions(["AL", "PE"]) \
            .on(month=6, day=24) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("São Pedro") \
            .in_regions(["AL"]) \
            .on(month=6, day=29) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Independência da Bahia") \
            .in_regions(["BA"]) \
            .on(month=7, day=2) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Emancipação Política de Sergipe") \
            .in_regions(["SE"]) \
            .on(month=7, day=8) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Revolução Constitucionalista de 1932") \
            .in_regions(["SP"]) \
            .on(month=7, day=9) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Fundação da Cidade de Goiás") \
            .in_regions(["GO"]) \
            .on(month=7, day=26) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Adesão do Maranhão à Independência do Brasil") \
            .in_regions(["MA"]) \
            .on(month=7, day=28) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Fundação do Estado da Paraíba") \
            .in_regions(["PB"]) \
            .on(month=8, day=5) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Dia do Rio Grande do Norte") \
            .in_regions(["RN"]) \
            .on(month=8, day=7) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Dia de Santa Catarina") \
            .in_regions(["SC"]) \
            .on(month=8, day=11) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Dia de Nossa Senhora da Assunção") \
            .in_regions(["CE"]) \
            .on(month=8, day=15) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Adesão do Pará à Independência do Brasil") \
            .in_regions(["PA"]) \
            .on(month=8, day=15) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Dia da Amazônia") \
            .in_regions(["AC"]) \
            .on(month=9, day=5) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Elevação do Amazonas à Categoria de Província") \
            .in_regions(["AM"]) \
            .on(month=9, day=5) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Independência do Brasil") \
            .on(month=9, day=7) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Nossa Senhora da Natividade") \
            .in_regions(["TO"]) \
            .on(month=9, day=8) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Criação do Território Federal do Amapá") \
            .in_regions(["AP"]) \
            .on(month=9, day=13) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Emancipação Política do Alagoas") \
            .in_regions(["AL"]) \
            .on(month=9, day=16) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Dia do Gaúcho") \
            .in_regions(["RS"]) \
            .on(month=9, day=20) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Mártires de Cunhaú e Uruaçu") \
            .in_regions(["RN"]) \
            .on(month=10, day=3) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Criação dos Estado de Roraima") \
            .in_regions(["RR"]) \
            .on(month=10, day=5) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Criação dos Estado de Tocantins") \
            .in_regions(["TO"]) \
            .on(month=10, day=5) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Criação do Estado do Mato Grosso do Sul") \
            .in_regions(["MS"]) \
            .on(month=10, day=11) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Nossa Senhora Aparecida") \
            .on(month=10, day=12) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Dia do Piauí") \
            .in_regions(["PI"]) \
            .on(month=10, day=19) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Pedra Fundamental de Goiânia") \
            .in_regions(["GO"]) \
            .on(month=10, day=24) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Finados") \
            .on(month=11, day=2) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Proclamação da República") \
            .on(month=11, day=15) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Assinatura do Tratado de Petrópolis") \
            .in_regions(["AC"]) \
            .on(month=11, day=17) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Morte de Zumbi dos Palmares") \
            .in_regions(["AL"]) \
            .on(month=11, day=20) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Dia da Consciência Negra") \
            .in_regions(["AM", "MT", "RJ"]) \
            .on(month=11, day=20) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Dia de Santa Catarina de Alexandria") \
            .in_regions(["SC"]) \
            .on(month=11, day=25) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Dia do Evangélico do Distrito Federal") \
            .in_regions(["DF"]) \
            .on(month=11, day=30) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Nossa Senhora da Conceição") \
            .in_regions(["AM"]) \
            .on(month=12, day=8) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Emancipação Política do Estado do Paraná") \
            .in_regions(["PR"]) \
            .on(month=12, day=19) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Natal") \
            .on(month=12, day=25) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Carnaval") \
            .on(day(47).before(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Páscoa") \
            .on(self.easter()) \
            .with_flags("NRV")
