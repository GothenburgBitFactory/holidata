from dateutil.easter import EASTER_WESTERN

from .holidays import Country


class SI(Country):
    id = "SI"
    languages = ["sl"]
    default_lang = "sl"
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Novo leto") \
            .on("01-01") \
            .with_flags("NF")

        """
        From 1955 until May 2012, when the National Assembly of Slovenia passed the Public Finance Balance Act,
        2 January was a work-free day. It was reintroduced in 2017.
        2012<: https://www.uradni-list.si/1/objava.jsp?sop=2012-01-1700
        2016<: https://www.uradni-list.si/1/objava.jsp?sop=2016-01-3568
        """
        self.define_holiday() \
            .with_name("Novo leto") \
            .on("01-02") \
            .except_for([2013, 2014, 2015, 2016]) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Prešernov dan") \
            .on("02-08") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Dan upora proti okupatorju") \
            .on("04-27") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Praznik dela") \
            .on("05-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Praznik dela") \
            .on("05-02") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Dan državnosti") \
            .on("06-25") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Marijino vnebovzetje") \
            .on("08-15") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Dan reformacije") \
            .on("10-31") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Dan spomina na mrtve") \
            .on("11-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Božič") \
            .on("12-25") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Dan samostojnosti in enotnosti") \
            .on("12-26") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Velikonočna nedelja") \
            .on("Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Velikonočni ponedeljek") \
            .on("1 day after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Binkošti") \
            .on("50 days after Easter") \
            .with_flags("NRV")
