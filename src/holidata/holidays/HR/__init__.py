from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import Month, date, day

__all__ = [
    "HR",
]


class HR(Country):
    id = "HR"
    languages = ["hr"]
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Nova Godina") \
            .on(date(Month.JANUARY, 1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Sveta tri kralja") \
            .on(date(Month.JANUARY, 6)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Praznik rada") \
            .on(date(Month.MAY, 1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Dan državnosti") \
            .on(date(Month.MAY, 30)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Dan antifašističke borbe") \
            .on(date(Month.JUNE, 22)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Dan pobjede i domovinske zahvalnosti i Dan hrvatskih branitelja") \
            .on(date(Month.AUGUST, 5)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Velika Gospa") \
            .on(date(Month.AUGUST, 15)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Dan svih svetih") \
            .on(date(Month.NOVEMBER, 1)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Božić") \
            .on(date(Month.DECEMBER, 25)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Sveti Stjepan") \
            .on(date(Month.DECEMBER, 26)) \
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
            .on(date(Month.NOVEMBER, 18)) \
            .with_flags("NF")
