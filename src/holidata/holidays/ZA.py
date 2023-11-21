from dateutil.easter import EASTER_WESTERN

from holidata.utils import SmartDayArrow
from .holidays import Country


class ZA(Country):
    id = "ZA"
    languages = ["en"]
    default_lang = "en"
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Christmas Day") \
            .on("12-25") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Good Friday") \
            .on("2 days before Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Family Day") \
            .on("1 day after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("New Year's Day") \
            .on("01-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("New Year's Day (Supplement)") \
            .on("01-02") \
            .with_flags("NF") \
            .annotated_with("Supplement holiday") \
            .on_condition(self.date_is_on_sunday(month=1, day=1))

        self.define_holiday() \
            .with_name("Human Rights Day") \
            .on("03-21") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Human Rights Day (Supplement)") \
            .on("03-22") \
            .with_flags("NF") \
            .annotated_with("Supplement holiday") \
            .on_condition(self.date_is_on_sunday(month=3, day=21))

        self.define_holiday() \
            .with_name("Freedom Day") \
            .on("04-27") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Freedom Day (Supplement)") \
            .on("04-28") \
            .with_flags("NF") \
            .annotated_with("Supplement holiday") \
            .on_condition(self.date_is_on_sunday(month=4, day=27))

        self.define_holiday() \
            .with_name("Worker's Day") \
            .on("05-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Worker's Day (Supplement)") \
            .on("05-02") \
            .with_flags("NF") \
            .annotated_with("Supplement holiday") \
            .on_condition(self.date_is_on_sunday(month=5, day=1))

        self.define_holiday() \
            .with_name("Youth Day") \
            .on("06-16") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Youth Day (Supplement)") \
            .on("06-17") \
            .with_flags("NF") \
            .annotated_with("Supplement holiday") \
            .on_condition(self.date_is_on_sunday(month=6, day=16))

        self.define_holiday() \
            .with_name("National Women's Day") \
            .on("08-09") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("National Women's Day (Supplement)") \
            .on("08-10") \
            .with_flags("NF") \
            .annotated_with("Supplement holiday") \
            .on_condition(self.date_is_on_sunday(month=8, day=9))

        self.define_holiday() \
            .with_name("Heritage Day") \
            .on("09-24") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Heritage Day (Supplement)") \
            .on("09-25") \
            .with_flags("NF") \
            .annotated_with("Supplement holiday") \
            .on_condition(self.date_is_on_sunday(month=9, day=24))

        self.define_holiday() \
            .with_name("Day of Reconciliation") \
            .on("12-16") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Day of Reconciliation (Supplement)") \
            .on("12-17") \
            .with_flags("NF") \
            .annotated_with("Supplement holiday") \
            .on_condition(self.date_is_on_sunday(month=12, day=16))

        self.define_holiday() \
            .with_name("Day of Goodwill") \
            .on("12-26") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Day of Goodwill (Supplement)") \
            .on("12-27") \
            .with_flags("NF") \
            .annotated_with("Supplement holiday") \
            .on_condition(self.date_is_on_sunday(month=12, day=26))

    @staticmethod
    def date_is_on_sunday(month, day):
        def wrapper(year):
            return SmartDayArrow(year, month, day).weekday() == "sunday"

        return wrapper
