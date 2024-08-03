from datetime import date, timedelta
from dateutil.easter import EASTER_WESTERN
from holidata.utils import month_reference
from .holidays import Country

class SG(Country):
    id = "SG"
    languages = ["en"]
    default_lang = "en"
    regions = []
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("New Year's Day") \
            .on(self.new_years_day) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Chinese New Year") \
            .on(self.chinese_new_year) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Chinese New Year (Second Day)") \
            .on(self.chinese_new_year_day2) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Good Friday") \
            .on(self.good_friday) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Labour Day") \
            .on(self.labour_day) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Hari Raya Puasa") \
            .on(self.hari_raya_puasa) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Vesak Day") \
            .on(self.vesak_day) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Hari Raya Haji") \
            .on(self.hari_raya_haji) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("National Day") \
            .on(self.national_day) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Deepavali") \
            .on(self.deepavali) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Christmas Day") \
            .on(self.christmas_day) \
            .with_flags("NRF")

    @staticmethod
    def shift_to_monday_if_weekend(holiday_date):
        """Shift the holiday to Monday if it falls on a Saturday or Sunday."""
        if holiday_date.weekday() >= 5:  # Saturday or Sunday
            return holiday_date + timedelta(days=(7 - holiday_date.weekday()))
        return holiday_date

    @staticmethod
    def new_years_day(year):
        """Return the date of New Year's Day for the given year."""
        return SG.shift_to_monday_if_weekend(date(year, 1, 1))

    @staticmethod
    def chinese_new_year(year):
        """Return the date of Chinese New Year for the given year."""
        dates = {
            2011: date(2011, 2, 3),
            2012: date(2012, 1, 23),
            2013: date(2013, 2, 10),
            2014: date(2014, 1, 31),
            2015: date(2015, 2, 19),
            2016: date(2016, 2, 8),
            2017: date(2017, 1, 28),
            2018: date(2018, 2, 16),
            2019: date(2019, 2, 5),
            2020: date(2020, 1, 25),
            2021: date(2021, 2, 12),
            2022: date(2022, 2, 1),
            2023: date(2023, 1, 22),
            2024: date(2024, 2, 10),
            2025: date(2025, 1, 29),
            2026: date(2026, 2, 17)
        }
        return dates.get(year)

    @staticmethod
    def chinese_new_year_day2(year):
        """Return the date of the second day of Chinese New Year."""
        first_day = SG.chinese_new_year(year)
        return SG.shift_to_monday_if_weekend(first_day + timedelta(days=1)) if first_day else None

    @staticmethod
    def good_friday(year):
        """Return the date of Good Friday for the given year."""
        dates = {
            2011: date(2011, 4, 22),
            2012: date(2012, 4, 6),
            2013: date(2013, 3, 29),
            2014: date(2014, 4, 18),
            2015: date(2015, 4, 3),
            2016: date(2016, 3, 25),
            2017: date(2017, 4, 14),
            2018: date(2018, 3, 30),
            2019: date(2019, 4, 19),
            2020: date(2020, 4, 10),
            2021: date(2021, 4, 2),
            2022: date(2022, 4, 15),
            2023: date(2023, 4, 7),
            2024: date(2024, 3, 29),
            2025: date(2025, 4, 18),
            2026: date(2026, 4, 3)
        }
        return dates.get(year)

    @staticmethod
    def labour_day(year):
        """Return the date of Labour Day for the given year."""
        return SG.shift_to_monday_if_weekend(date(year, 5, 1))

    @staticmethod
    def hari_raya_puasa(year):
        """Return the date of Hari Raya Puasa for the given year."""
        dates = {
            2011: date(2011, 8, 30),
            2012: date(2012, 8, 19),
            2013: date(2013, 8, 8),
            2014: date(2014, 7, 28),
            2015: date(2015, 7, 17),
            2016: date(2016, 7, 6),
            2017: date(2017, 6, 25),
            2018: date(2018, 6, 15),
            2019: date(2019, 6, 5),
            2020: date(2020, 5, 24),
            2021: date(2021, 5, 13),
            2022: date(2022, 5, 3),
            2023: date(2023, 4, 22),
            2024: date(2024, 4, 10),
            2025: date(2025, 3, 31),
            2026: date(2026, 3, 20)
        }
        holiday_date = dates.get(year)
        if holiday_date and holiday_date.weekday() == 5:  # Saturday
            return holiday_date + timedelta(days=2)  # Move to Monday
        return holiday_date

    @staticmethod
    def vesak_day(year):
        """Return the date of Vesak Day for the given year."""
        dates = {
            2011: date(2011, 5, 17),
            2012: date(2012, 5, 5),
            2013: date(2013, 5, 24),
            2014: date(2014, 5, 13),
            2015: date(2015, 6, 1),
            2016: date(2016, 5, 21),
            2017: date(2017, 5, 10),
            2018: date(2018, 5, 29),
            2019: date(2019, 5, 19),
            2020: date(2020, 5, 7),
            2021: date(2021, 5, 26),
            2022: date(2022, 5, 15),
            2023: date(2023, 6, 2),
            2024: date(2024, 5, 22),
            2025: date(2025, 5, 12),
            2026: date(2026, 5, 31)
        }
        return dates.get(year)

    @staticmethod
    def hari_raya_haji(year):
        """Return the date of Hari Raya Haji for the given year."""
        dates = {
            2023: date(2023, 6, 29),
            2024: date(2024, 6, 17),
            2025: date(2025, 6, 6),
            2026: date(2026, 5, 27)
        }
        return dates.get(year)

    @staticmethod
    def national_day(year):
        """Return the date of National Day for the given year."""
        return SG.shift_to_monday_if_weekend(date(year, 8, 9))

    @staticmethod
    def deepavali(year):
        """Return the date of Deepavali for the given year."""
        dates = {
            2023: date(2023, 11, 12),
            2024: date(2024, 10, 31),
            2025: date(2025, 10, 20),
            2026: date(2026, 11, 8)
        }
        return SG.shift_to_monday_if_weekend(dates.get(year))

    @staticmethod
    def christmas_day(year):
        """Return the date of Christmas Day for the given year."""
        return SG.shift_to_monday_if_weekend(date(year, 12, 25))

    # Add a class attribute for legal sources
    legal_sources = [
        "https://www.mom.gov.sg/employment-practices/public-holidays",
        "https://www.mom.gov.sg/employment-practices/public-holidays-entitlement-and-pay"
    ]