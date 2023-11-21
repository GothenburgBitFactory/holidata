from dateutil.easter import EASTER_WESTERN

from .holidays import Country

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
            .on("01-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Den obnovy samostatného českého státu") \
            .on("01-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Svátek práce") \
            .on("05-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Den vítězství") \
            .on("05-08") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Den slovanských věrozvěstů Cyrila a Metoděje") \
            .on("07-05") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Den upálení mistra Jana Husa") \
            .on("07-06") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Den české státnosti") \
            .on("09-28") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Den vzniku samostatného československého státu") \
            .on("10-28") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Štědrý den") \
            .on("12-24") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("1. svátek vánoční") \
            .on("12-25") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("2. svátek vánoční") \
            .on("12-26") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Velikonoční pondělí") \
            .on("1 day after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Velký pátek") \
            .on("2 days before Easter") \
            .since(2016) \
            .with_flags("NRV")

        """
        Until 2018, replaced by "Den boje za svobodu a demokracii a Mezinárodní den studentstva" on 2019-04-01"
        """
        self.define_holiday() \
            .with_name("Den boje za svobodu a demokracii") \
            .on("11-17") \
            .until(2018) \
            .with_flags("NF")

        """
        Since 2019, replaces "Den boje za svobodu a demokracii"
        """
        self.define_holiday() \
            .with_name("Den boje za svobodu a demokracii a Mezinárodní den studentstva") \
            .on("11-17") \
            .since(2019) \
            .with_flags("NF")
