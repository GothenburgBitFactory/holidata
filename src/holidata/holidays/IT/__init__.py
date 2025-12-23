from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import day, first

__all__ = [
    "IT",
]

"""
sources:
- LEGGE 27 maggio   1949, n. 260 https://www.gazzettaufficiale.it/eli/gu/1949/05/31/124/sg
- LEGGE  5 marzo    1977, n.  54 https://www.gazzettaufficiale.it/eli/id/1977/03/07/077U0054/sg 
- LEGGE 20 novembre 2000, n. 336 https://www.gazzettaufficiale.it/eli/id/2000/11/22/000G0390/sg
- DECRETO DEL PRESIDENTE DELLA REPUBBLICA 28 dicembre 1985, n. 792
                                 https://www.gazzettaufficiale.it/eli/id/1985/12/31/085U0792/sg
- LEGGE  8 ottobre  2025, n. 151 https://www.gazzettaufficiale.it/eli/id/2025/10/10/25G00153/sg
"""


class IT(Country):
    id = "IT"
    languages = ["it"]
    default_lang = "it"
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Capodanno") \
            .on(month=1, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Epifania") \
            .on(month=1, day=6) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Festa della liberazione") \
            .on(month=4, day=25) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Festa del lavoro") \
            .on(month=5, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Festa della repubblica") \
            .on(month=6, day=2) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Santi Apostoli Pietro e Paolo") \
            .on(month=6, day=29) \
            .with_flags("NRF") \
            .annotated_with("Solo per il comune di Roma")

        self.define_holiday() \
            .with_name("Assunzione (ferragosto)") \
            .on(month=8, day=15) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Festa nazionale di San Francesco d'Assisi, patrono d'Italia") \
            .since(2026) \
            .on(month=10, day=4) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Ognissanti") \
            .on(month=11, day=1) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Unità nazionale") \
            .on(first("sunday").of("november")) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Immacolata concezione") \
            .on(month=12, day=8) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Natale") \
            .on(month=12, day=25) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("S.to Stefano") \
            .on(month=12, day=26) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Pasqua") \
            .on(self.easter()) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Pasquetta") \
            .on(day(1).after(self.easter())) \
            .with_flags("NRV")
