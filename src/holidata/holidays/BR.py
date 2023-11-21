from dateutil.easter import EASTER_WESTERN

from .holidays import Country

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
    regions = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE",
               "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()
        
        self.define_holiday() \
            .with_name("Confraternização Universal") \
            .on("01-01") \
            .with_flags("NF")
        
        self.define_holiday() \
            .with_name("Criação do Estado de Rondônia") \
            .in_regions(["RO"]) \
            .on("01-04") \
            .with_flags("F")
        
        self.define_holiday() \
            .with_name("Dia do Evangélico no Acre") \
            .in_regions(["AC"]) \
            .on("01-23") \
            .with_flags("RF")
        
        self.define_holiday() \
            .with_name("Revolução Pernambucana de 1817") \
            .in_regions(["PE"]) \
            .on("03-06") \
            .with_flags("F")
        
        self.define_holiday() \
            .with_name("Dia Internacional da Mulher") \
            .in_regions(["AC"]) \
            .on("03-08") \
            .with_flags("F")
        
        self.define_holiday() \
            .with_name("Autonomia do Estado de Tocantins") \
            .in_regions(["TO"]) \
            .on("03-18") \
            .with_flags("F")
        
        self.define_holiday() \
            .with_name("Dia de São José") \
            .in_regions(["AP", "CE"]) \
            .on("03-19") \
            .with_flags("RF")
        
        self.define_holiday() \
            .with_name("Abolição da Escravidão no Ceará") \
            .in_regions(["CE"]) \
            .on("03-25") \
            .with_flags("F")
        
        self.define_holiday() \
            .with_name("Fundação de Brasília") \
            .in_regions(["DF"]) \
            .on("04-21") \
            .with_flags("F")
        
        self.define_holiday() \
            .with_name("Execução de Tiradentes") \
            .in_regions(["MG"]) \
            .on("04-21") \
            .with_flags("F")
        
        self.define_holiday() \
            .with_name("Tiradentes") \
            .on("04-21") \
            .with_flags("NF")
        
        self.define_holiday() \
            .with_name("Dia de São Jorge") \
            .in_regions(["RJ"]) \
            .on("04-23") \
            .with_flags("RF")
        
        self.define_holiday() \
            .with_name("Dia Internacional do Trabalhador") \
            .on("05-01") \
            .with_flags("NF")
        
        self.define_holiday() \
            .with_name("Aniversário do Estado do Acre") \
            .in_regions(["AC"]) \
            .on("06-15") \
            .with_flags("F")
        
        self.define_holiday() \
            .with_name("Dia do Evangélico em Rondônia") \
            .in_regions(["RO"]) \
            .on("06-18") \
            .with_flags("RF")
        
        self.define_holiday() \
            .with_name("São João") \
            .in_regions(["AL", "PE"]) \
            .on("06-24") \
            .with_flags("RF")
        
        self.define_holiday() \
            .with_name("São Pedro") \
            .in_regions(["AL"]) \
            .on("06-29") \
            .with_flags("RF")
        
        self.define_holiday() \
            .with_name("Independência da Bahia") \
            .in_regions(["BA"]) \
            .on("07-02") \
            .with_flags("F")
        
        self.define_holiday() \
            .with_name("Emancipação Política de Sergipe") \
            .in_regions(["SE"]) \
            .on("07-08") \
            .with_flags("F")
        
        self.define_holiday() \
            .with_name("Revolução Constitucionalista de 1932") \
            .in_regions(["SP"]) \
            .on("07-09") \
            .with_flags("F")
        
        self.define_holiday() \
            .with_name("Fundação da Cidade de Goiás") \
            .in_regions(["GO"]) \
            .on("07-26") \
            .with_flags("F")
        
        self.define_holiday() \
            .with_name("Adesão do Maranhão à Independência do Brasil") \
            .in_regions(["MA"]) \
            .on("07-28") \
            .with_flags("F")
        
        self.define_holiday() \
            .with_name("Fundação do Estado da Paraíba") \
            .in_regions(["PB"]) \
            .on("08-05") \
            .with_flags("F")
        
        self.define_holiday() \
            .with_name("Dia do Rio Grande do Norte") \
            .in_regions(["RN"]) \
            .on("08-07") \
            .with_flags("F")
        
        self.define_holiday() \
            .with_name("Dia de Santa Catarina") \
            .in_regions(["SC"]) \
            .on("08-11") \
            .with_flags("F")
        
        self.define_holiday() \
            .with_name("Dia de Nossa Senhora da Assunção") \
            .in_regions(["CE"]) \
            .on("08-15") \
            .with_flags("RF")
        
        self.define_holiday() \
            .with_name("Adesão do Pará à Independência do Brasil") \
            .in_regions(["PA"]) \
            .on("08-15") \
            .with_flags("F")
        
        self.define_holiday() \
            .with_name("Dia da Amazônia") \
            .in_regions(["AC"]) \
            .on("09-05") \
            .with_flags("F")
        
        self.define_holiday() \
            .with_name("Elevação do Amazonas à Categoria de Província") \
            .in_regions(["AM"]) \
            .on("09-05") \
            .with_flags("F")
        
        self.define_holiday() \
            .with_name("Independência do Brasil") \
            .on("09-07") \
            .with_flags("NF")
        
        self.define_holiday() \
            .with_name("Nossa Senhora da Natividade") \
            .in_regions(["TO"]) \
            .on("09-08") \
            .with_flags("F")
        
        self.define_holiday() \
            .with_name("Criação do Território Federal do Amapá") \
            .in_regions(["AP"]) \
            .on("09-13") \
            .with_flags("F")
        
        self.define_holiday() \
            .with_name("Emancipação Política do Alagoas") \
            .in_regions(["AL"]) \
            .on("09-16") \
            .with_flags("F")
        
        self.define_holiday() \
            .with_name("Dia do Gaúcho") \
            .in_regions(["RS"]) \
            .on("09-20") \
            .with_flags("F")
        
        self.define_holiday() \
            .with_name("Mártires de Cunhaú e Uruaçu") \
            .in_regions(["RN"]) \
            .on("10-03") \
            .with_flags("F")
        
        self.define_holiday() \
            .with_name("Criação dos Estado de Roraima") \
            .in_regions(["RR"]) \
            .on("10-05") \
            .with_flags("F")
        
        self.define_holiday() \
            .with_name("Criação dos Estado de Tocantins") \
            .in_regions(["TO"]) \
            .on("10-05") \
            .with_flags("F")
        
        self.define_holiday() \
            .with_name("Criação do Estado do Mato Grosso do Sul") \
            .in_regions(["MS"]) \
            .on("10-11") \
            .with_flags("F")
        
        self.define_holiday() \
            .with_name("Nossa Senhora Aparecida") \
            .on("10-12") \
            .with_flags("NRF")
        
        self.define_holiday() \
            .with_name("Dia do Piauí") \
            .in_regions(["PI"]) \
            .on("10-19") \
            .with_flags("F")
        
        self.define_holiday() \
            .with_name("Pedra Fundamental de Goiânia") \
            .in_regions(["GO"]) \
            .on("10-24") \
            .with_flags("F")
        
        self.define_holiday() \
            .with_name("Finados") \
            .on("11-02") \
            .with_flags("NRF")
        
        self.define_holiday() \
            .with_name("Proclamação da República") \
            .on("11-15") \
            .with_flags("NF")
        
        self.define_holiday() \
            .with_name("Assinatura do Tratado de Petrópolis") \
            .in_regions(["AC"]) \
            .on("11-17") \
            .with_flags("F")
        
        self.define_holiday() \
            .with_name("Morte de Zumbi dos Palmares") \
            .in_regions(["AL"]) \
            .on("11-20") \
            .with_flags("F")
        
        self.define_holiday() \
            .with_name("Dia da Consciência Negra") \
            .in_regions(["AM", "MT", "RJ"]) \
            .on("11-20") \
            .with_flags("F")
        
        self.define_holiday() \
            .with_name("Dia de Santa Catarina de Alexandria") \
            .in_regions(["SC"]) \
            .on("11-25") \
            .with_flags("RF")
        
        self.define_holiday() \
            .with_name("Dia do Evangélico do Distrito Federal") \
            .in_regions(["DF"]) \
            .on("11-30") \
            .with_flags("RF")
        
        self.define_holiday() \
            .with_name("Nossa Senhora da Conceição") \
            .in_regions(["AM"]) \
            .on("12-08") \
            .with_flags("RF")
        
        self.define_holiday() \
            .with_name("Emancipação Política do Estado do Paraná") \
            .in_regions(["PR"]) \
            .on("12-19") \
            .with_flags("F")
        
        self.define_holiday() \
            .with_name("Natal") \
            .on("12-25") \
            .with_flags("NRF")
        
        self.define_holiday() \
            .with_name("Carnaval") \
            .on("47 days before Easter") \
            .with_flags("NRV")
        
        self.define_holiday() \
            .with_name("Páscoa") \
            .on("Easter") \
            .with_flags("NRV")
