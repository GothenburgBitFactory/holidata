# coding=utf-8
from dateutil.easter import EASTER_WESTERN

from holidata.utils import SmartDayArrow
from .holidays import Holiday, Locale

"""
Public Holidays Act (Act No 36 of 1994).
sources: 
https://www.gov.za/sites/default/files/gcis_document/201409/act36of1994.pdf
https://www.gov.za/sites/default/files/gcis_document/201409/act48of1995.pdf
"""


class en_ZA(Locale):
    """
    12-25: [NF] Christmas Day
    2 days before Easter: [NRV] Good Friday
    1 day after Easter: [NRV] Family Day
    """

    locale = "en-ZA"
    easter_type = EASTER_WESTERN

    def holiday_new_years_day(self):
        """01-01: [NF] New Year's Day"""
        return self.get_holidays(SmartDayArrow(self.year, 1, 1), "New Year's Day")

    def holiday_human_rights_day(self):
        """03-21: [NF] Human Rights Day"""
        return self.get_holidays(SmartDayArrow(self.year, 3, 21), "Human Rights Day")

    def holiday_freedom_day(self):
        """04-27: [NF] Freedom Day"""
        return self.get_holidays(SmartDayArrow(self.year, 4, 27), "Freedom Day")

    def holiday_workers_day(self):
        """05-01: [NF] Worker's Day"""
        return self.get_holidays(SmartDayArrow(self.year, 5, 1), "Worker's Day")

    def holiday_youth_day(self):
        """06-16: [NF] Youth Day"""
        return self.get_holidays(SmartDayArrow(self.year, 6, 16), "Youth Day")

    def holiday_national_womens_day(self):
        """08-09: [NF] National Women's Day"""
        return self.get_holidays(SmartDayArrow(self.year, 8, 9), "National Women's Day")

    def holiday_heritage_day(self):
        """09-24: [NF] Heritage Day"""
        return self.get_holidays(SmartDayArrow(self.year, 9, 24), "Heritage Day")

    def holiday_day_of_reconciliation(self):
        """12-16: [NF] Day of Reconciliation"""
        return self.get_holidays(SmartDayArrow(self.year, 12, 16), "Day of Reconciliation")

    def holiday_day_of_goodwill(self):
        """12-26: [NF] Day of Goodwill"""
        return self.get_holidays(SmartDayArrow(self.year, 12, 26), "Day of Goodwill")

    def get_holidays(self, original_date, description):
        """
        Applies section 2.1 of the Public Holidays Act (Act No 36 of 1994):
        'Whenever any public holiday falls on a Sunday, the following Monday shall be a public holiday.'
        """
        if original_date.weekday() == "sunday":
            supplement_date = original_date.shift(days=1)
            return [
                Holiday(
                    locale=self.locale,
                    region="",
                    date=original_date,
                    description=description,
                    flags="NF",
                    notes=""),
                Holiday(
                    locale=self.locale,
                    region="",
                    date=supplement_date,
                    description=description + " (Supplement)",
                    flags="NF",
                    notes="Supplement holiday")
            ]
        else:
            return [Holiday(
                locale=self.locale,
                region='',
                date=original_date,
                description=description,
                flags="NF",
                notes="")]
