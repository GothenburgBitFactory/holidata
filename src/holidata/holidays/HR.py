from dateutil.easter import EASTER_WESTERN

from .holidays import Country


class HR(Country):
    id = "HR"
    languages = ["hr"]
    default_lang = "hr"
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Nova Godina") \
            .on("01-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Sveta tri kralja") \
            .on("01-06") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Praznik rada") \
            .on("05-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Dan državnosti") \
            .on("05-30") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Dan antifašističke borbe") \
            .on("06-22") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Dan pobjede i domovinske zahvalnosti i Dan hrvatskih branitelja") \
            .on("08-05") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Velika Gospa") \
            .on("08-15") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Dan svih svetih") \
            .on("11-01") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Božić") \
            .on("12-25") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Sveti Stjepan") \
            .on("12-26") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Uskrs") \
            .on("Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Uskršnji ponedjeljak") \
            .on("1 day after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Tijelovo") \
            .on("60 days after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Dan sjećanja na žrtve Domovinskog rata i Dan sjećanja na žrtvu Vukovara i Škabrnje") \
            .since(2020) \
            .on("11-18") \
            .with_flags("NF")
