from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import day

__all__ = [
    "HR",
]


class HR(Country):
    id = "HR"
    languages = ["hr"]
    default_lang = "hr"
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Nova Godina") \
            .on(month=1, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Sveta tri kralja") \
            .on(month=1, day=6) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Praznik rada") \
            .on(month=5, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Dan državnosti") \
            .on(month=5, day=30) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Dan antifašističke borbe") \
            .on(month=6, day=22) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Dan pobjede i domovinske zahvalnosti i Dan hrvatskih branitelja") \
            .on(month=8, day=5) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Velika Gospa") \
            .on(month=8, day=15) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Dan svih svetih") \
            .on(month=11, day=1) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Božić") \
            .on(month=12, day=25) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Sveti Stjepan") \
            .on(month=12, day=26) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Uskrs") \
            .on(self.easter()) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Uskršnji ponedjeljak") \
            .on(day(1).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Tijelovo") \
            .on(day(60).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Dan sjećanja na žrtve Domovinskog rata i Dan sjećanja na žrtvu Vukovara i Škabrnje") \
            .since(2020) \
            .on(month=11, day=18) \
            .with_flags("NF")
