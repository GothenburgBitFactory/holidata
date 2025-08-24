from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import day

__all__ = [
    "CZ",
]


"""
source: https://www.zakonyprolidi.cz/cs/2000-245, §1 and §2.
        https://www.zakonyprolidi.cz/cs/2000-245/zneni-20200201 (>2020-02-01)
        https://www.zakonyprolidi.cz/cs/2000-245/zneni-20190401 (>2019-04-01)
        https://www.zakonyprolidi.cz/cs/2000-245/zneni-0 (>2000-08-09)
"""


class CZ(Country):
    id = "CZ"
    languages = ["cs"]
    default_lang = "cs"
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Nový rok") \
            .on(month=1, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Den obnovy samostatného českého státu") \
            .on(month=1, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Svátek práce") \
            .on(month=5, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Den vítězství") \
            .on(month=5, day=8) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Den slovanských věrozvěstů Cyrila a Metoděje") \
            .on(month=7, day=5) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Den upálení mistra Jana Husa") \
            .on(month=7, day=6) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Den české státnosti") \
            .on(month=9, day=28) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Den vzniku samostatného československého státu") \
            .on(month=10, day=28) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Štědrý den") \
            .on(month=12, day=24) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("1. svátek vánoční") \
            .on(month=12, day=25) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("2. svátek vánoční") \
            .on(month=12, day=26) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Velikonoční pondělí") \
            .on(day(1).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Velký pátek") \
            .on(day(2).before(self.easter())) \
            .since(2016) \
            .with_flags("NRV")

        """
        Until 2018, replaced by "Den boje za svobodu a demokracii a Mezinárodní den studentstva" on 2019-04-01"
        """
        self.define_holiday() \
            .with_name("Den boje za svobodu a demokracii") \
            .on(month=11, day=17) \
            .until(2018) \
            .with_flags("NF")

        """
        Since 2019, replaces "Den boje za svobodu a demokracii"
        """
        self.define_holiday() \
            .with_name("Den boje za svobodu a demokracii a Mezinárodní den studentstva") \
            .on(month=11, day=17) \
            .since(2019) \
            .with_flags("NF")
