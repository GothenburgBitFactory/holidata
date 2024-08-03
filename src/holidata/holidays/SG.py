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

        # Special case for 2023
        self.define_holiday() \
            .with_name("Polling Day") \
            .on("2023-09-01") \
            .with_flags("NF")

    @staticmethod
    def shift_to_monday_if_weekend(holiday_date):
        """Shift the holiday to Monday if it falls on a Saturday or Sunday."""
        if holiday_date.weekday() >= 5:  # Saturday or Sunday
            return holiday_date + timedelta(days=(7 - holiday_date.weekday()))
        return holiday_date

    @staticmethod
    def new_years_day(year):
        """Return the date of New Year's Day for the given year."""
        return date(year, 1, 1)

    @staticmethod
    def chinese_new_year(year):
        """Return the date of Chinese New Year for the given year."""
        dates = {
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
        return first_day + timedelta(days=1) if first_day else None

    @staticmethod
    def good_friday(year):
        """Return the date of Good Friday for the given year."""
        dates = {
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
        return date(year, 5, 1)

    @staticmethod
    def hari_raya_puasa(year):
        """Return the date of Hari Raya Puasa for the given year."""
        dates = {
            2022: date(2022, 5, 3),
            2023: date(2023, 4, 22),
            2024: date(2024, 4, 10),
            2025: date(2025, 3, 31),
            2026: date(2026, 3, 20)
        }
        return dates.get(year)

    @staticmethod
    def vesak_day(year):
        """Return the date of Vesak Day for the given year."""
        dates = {
            2022: date(2022, 5, 15),
            2023: date(2023, 6, 2),
            2024: date(2024, 5, 22),
            2025: date(2025, 5, 12),
            2026: date(2026, 5, 31)
        }
        return SG.shift_to_monday_if_weekend(dates.get(year))

    @staticmethod
    def hari_raya_haji(year):
        """Return the date of Hari Raya Haji for the given year."""
        dates = {
            2022: date(2022, 7, 10),
            2023: date(2023, 6, 29),
            2024: date(2024, 6, 17),
            2025: date(2025, 6, 6),
            2026: date(2026, 5, 27)
        }
        return dates.get(year)

    @staticmethod
    def national_day(year):
        """Return the date of National Day for the given year."""
        holiday = date(year, 8, 9)
        if holiday.weekday() == 6:  # Sunday
            return date(year, 8, 10)  # Next Monday
        return holiday

    @staticmethod
    def deepavali(year):
        """Return the date of Deepavali for the given year."""
        dates = {
            2022: date(2022, 10, 24),
            2023: date(2023, 11, 12),
            2024: date(2024, 10, 31),
            2025: date(2025, 10, 20),
            2026: date(2026, 11, 8)
        }
        return SG.shift_to_monday_if_weekend(dates.get(year))

    @staticmethod
    def christmas_day(year):
        """Return the date of Christmas Day for the given year."""
        return date(year, 12, 25)