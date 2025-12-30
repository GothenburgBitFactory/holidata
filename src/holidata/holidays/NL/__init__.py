from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import day, date

__all__ = [
    "NL",
]


class NL(Country):
    id = "NL"
    languages = ["nl"]
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Nieuwjaarsdag") \
            .on(date(month=1, day=1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Dodenherdenking") \
            .on(date(month=5, day=4)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Bevrijdingsdag") \
            .on(date(month=5, day=5)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Sinterklaas") \
            .on(date(month=12, day=5)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Eerste Kerstdag") \
            .on(date(month=12, day=25)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Tweede Kerstdag") \
            .on(date(month=12, day=26)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Goede Vrijdag") \
            .on(day(2).before(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Eerste Paasdag") \
            .on(self.easter()) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Tweede Paasdag") \
            .on(day(1).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Hemelvaartsdag") \
            .on(day(39).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Eerste Pinksterdag") \
            .on(day(49).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Tweede Pinksterdag") \
            .on(day(50).after(self.easter())) \
            .with_flags("NRV")

        """
        Koninginnedag
        04-30 or saturday before, if it falls on sunday
        """
        self.define_holiday() \
            .with_name("Koninginnedag") \
            .until(2013) \
            .on(date(month=4, day=29)) \
            .on_condition(date(month=4, day=30).is_a("sunday")) \
            .with_flags("NV")

        self.define_holiday() \
            .with_name("Koninginnedag") \
            .until(2013) \
            .on(date(month=4, day=30)) \
            .on_condition(date(month=4, day=30).is_not_a("sunday")) \
            .with_flags("NV")

        """
        Koningsdag
        04-27 or saturday before if it falls on sunday
        """
        self.define_holiday() \
            .with_name("Koningsdag") \
            .since(2014) \
            .on(date(month=4, day=26)) \
            .on_condition(date(month=4, day=27).is_a("sunday")) \
            .with_flags("NV")

        self.define_holiday() \
            .with_name("Koningsdag") \
            .since(2014) \
            .on(date(month=4, day=27)) \
            .on_condition(date(month=4, day=27).is_not_a("sunday")) \
            .with_flags("NV")

        """
        Koninkrijksdag
        12-15 or monday after if it falls on sunday
        """
        self.define_holiday() \
            .with_name("Koninkrijksdag") \
            .on(date(month=12, day=15)) \
            .on_condition(date(month=12, day=15).is_not_a("sunday")) \
            .with_flags("NV")

        self.define_holiday() \
            .with_name("Koninkrijksdag") \
            .on(date(month=12, day=16)) \
            .on_condition(date(month=12, day=15).is_a("sunday")) \
            .with_flags("NV")
