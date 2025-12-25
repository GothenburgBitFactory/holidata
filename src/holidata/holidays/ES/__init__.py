from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.holidays.ES.AN import AN
from holidata.holidays.ES.AR import AR
from holidata.holidays.ES.AS import AS
from holidata.holidays.ES.CB import CB
from holidata.holidays.ES.CE import CE
from holidata.holidays.ES.CL import CL
from holidata.holidays.ES.CM import CM
from holidata.holidays.ES.CN import CN
from holidata.holidays.ES.CT import CT
from holidata.holidays.ES.EX import EX
from holidata.holidays.ES.GA import GA
from holidata.holidays.ES.IB import IB
from holidata.holidays.ES.MC import MC
from holidata.holidays.ES.MD import MD
from holidata.holidays.ES.ML import ML
from holidata.holidays.ES.NC import NC
from holidata.holidays.ES.PV import PV
from holidata.holidays.ES.RI import RI
from holidata.holidays.ES.VC import VC
from holidata.utils import day

__all__ = [
    "ES"
]

"""
Information taken from government websites around 2020-06
    https://administracion.gob.es/pag_Home/atencionCiudadana/calendarios/laboral.html
    http://www.seg-social.es/wps/portal/wss/internet/CalendarioLaboral

    2011: https://www.boe.es/eli/es/res/2010/10/07/(1)
          https://www.boe.es/eli/es/res/2010/11/24/(1)
    2012: https://www.boe.es/eli/es/res/2011/10/06/(1)
    2013: https://www.boe.es/eli/es/res/2012/10/30/(1)
          https://www.boe.es/eli/es/res/2012/11/12/(2)
    2014: https://www.boe.es/eli/es/res/2013/11/08/(3)
          https://www.boe.es/eli/es/res/2013/11/21/(1)
    2015: https://www.boe.es/eli/es/res/2014/10/17/(3)
    2016: https://www.boe.es/eli/es/res/2015/10/19/(1)
    2017: https://www.boe.es/eli/es/res/2016/10/04/(1)
    2018: https://www.boe.es/eli/es/res/2017/10/09/(1)
          https://www.boe.es/eli/es/res/2017/10/09/(1)/corrigendum/20171019
          https://www.boe.es/eli/es/res/2017/10/09/(1)/corrigendum/20171025
    2019: https://www.boe.es/eli/es/res/2018/10/16/(1)
    2020: https://www.boe.es/eli/es/res/2019/10/03/(1)
    2021: https://www.boe.es/eli/es/res/2020/10/28/(1)
    2022: https://www.boe.es/eli/es/res/2021/10/14/(3)
    2023: https://www.boe.es/eli/es/res/2022/10/07/(2)
    2024: https://www.boe.es/eli/es/res/2023/10/23/(1)
    2025: https://www.boe.es/eli/es/res/2024/10/15/(1)
    2026: https://www.boe.es/eli/es/res/2025/10/17/(2)

Regional governments
    [AN] https://www.juntadeandalucia.es/temas/trabajar/relaciones/calendario.html

Also those sites for some information
    https://es.wikipedia.org/wiki/Calendario_laboral
"""


class ES(Country):
    id = "ES"
    languages = ["es"]
    default_lang = "es"
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.regions = [
            AN(self),
            AR(self),
            AS(self),
            CB(self),
            CE(self),
            CL(self),
            CM(self),
            CN(self),
            CT(self),
            EX(self),
            GA(self),
            IB(self),
            MC(self),
            MD(self),
            ML(self),
            NC(self),
            PV(self),
            RI(self),
            VC(self),
        ]

        self.define_holiday() \
            .with_name("Año Nuevo") \
            .on(month=1, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Epifanía del Señor") \
            .on(month=1, day=6) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Fiesta del Trabajo") \
            .on(month=5, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Asunción de la Virgen") \
            .on(month=8, day=15) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Fiesta Nacional de España") \
            .on(month=10, day=12) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Todos los Santos") \
            .on(month=11, day=1) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Día de la Constitución Española") \
            .on(month=12, day=6) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Inmaculada Concepción") \
            .on(month=12, day=8) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Natividad del Señor") \
            .on(month=12, day=25) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Viernes Santo") \
            .on(day(2).before(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Pascua") \
            .on(self.easter()) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Lunes siguiente al Año Nuevo") \
            .in_years([2012]) \
            .on(month=1, day=2) \
            .with_flags("NF")
