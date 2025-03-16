from dateutil.easter import EASTER_WESTERN
from .holidays import Country

#
# Information taken from various government websites and official sources around 2024-08-04
#   https://www.india.gov.in/calendar
#   https://www.officeholidays.com/countries/india/
#   https://www.calendarlabs.com/holidays/india/
#
# This is a placeholder class for India holidays. More details will be added later.
#


class IN(Country):
    id = "IN"
    languages = ["hi", "en"]
    regions = ["AN", "AP", "AR", "AS", "BR", "CH", "CT", "DD", "DL", "GA", "GJ", "HR", "HP", "JK", "JH", "KA", "KL", "LA", "LD", "MH", "ML", "MN", "MP", "MZ", "NL", "OR", "PB", "PY", "RJ", "SK", "TN", "TG", "TR", "UP", "UT", "WB"]
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_names({
                "hi": "गणतंत्र दिवस",
                "en": "Republic Day",
            }) \
            .on("01-26") \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "hi": "स्वतंत्रता दिवस",
                "en": "Independence Day",
            }) \
            .on("08-15") \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "hi": "गांधी जयंती",
                "en": "Gandhi Jayanti",
            }) \
            .on("10-02") \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "hi": "दीवाली",
                "en": "Diwali",
            }) \
            .on("variable") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_names({
                "hi": "होली",
                "en": "Holi",
            }) \
            .on("variable") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_names({
                "hi": "ईद उल-फितर",
                "en": "Eid al-Fitr",
            }) \
            .on("variable") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_names({
                "hi": "ईद उल-अधा",
                "en": "Eid al-Adha",
            }) \
            .on("variable") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_names({
                "hi": "क्रिसमस",
                "en": "Christmas",
            }) \
            .on("12-25") \
            .with_flags("NRF")

        # Placeholder for additional holidays to be added later
        self.define_holiday() \
            .with_names({
                "hi": "प्लेसहोल्डर",
                "en": "Placeholder",
            }) \
            .on("02-17") \
            .with_flags("NRF")

        # More holidays and details will be added later as per the guidelines
