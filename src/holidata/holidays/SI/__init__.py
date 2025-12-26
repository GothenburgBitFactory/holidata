from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import day, date, Month

__all__ = [
    "SI",
]


class SI(Country):
    id = "SI"
    languages = ["sl"]
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Novo leto") \
            .on(date(Month.JANUARY, 1)) \
            .with_flags("NF")

        """
        From 1955 until May 2012, when the National Assembly of Slovenia passed the Public Finance Balance Act,
        2 January was a work-free day. It was reintroduced in 2017.
        2012<: https://www.uradni-list.si/1/objava.jsp?sop=2012-01-1700
        2016<: https://www.uradni-list.si/1/objava.jsp?sop=2016-01-3568
        """
        self.define_holiday() \
            .with_name("Novo leto") \
            .on(date(Month.JANUARY, 2)) \
            .except_for([2013, 2014, 2015, 2016]) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Prešernov dan") \
            .on(date(Month.FEBRUARY, 8)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Dan upora proti okupatorju") \
            .on(date(Month.APRIL, 27)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Praznik dela") \
            .on(date(Month.MAY, 1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Praznik dela") \
            .on(date(Month.MAY, 2)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Dan državnosti") \
            .on(date(Month.JUNE, 25)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Marijino vnebovzetje") \
            .on(date(Month.AUGUST, 15)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Dan reformacije") \
            .on(date(Month.OCTOBER, 31)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Dan spomina na mrtve") \
            .on(date(Month.NOVEMBER, 1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Božič") \
            .on(date(Month.DECEMBER, 25)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Dan samostojnosti in enotnosti") \
            .on(date(Month.DECEMBER, 26)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Velikonočna nedelja") \
            .on(self.easter()) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Velikonočni ponedeljek") \
            .on(day(1).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Binkošti") \
            .on(day(50).after(self.easter())) \
            .with_flags("NRV")
