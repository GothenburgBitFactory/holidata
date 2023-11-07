# coding=utf-8
from dateutil.easter import EASTER_WESTERN

from holidata.utils import SmartDayArrow
from .holidays import Holiday, Locale


#
# Information taken from various government websites around 2020-04-16
#   https://www.canada.ca/fr/emploi-developpement-social/services/normes-travail/rapports/jours-feries.html
#   http://www4.gouv.qc.ca/FR/Portail/Citoyens/Evenements/travailleur-avec-salaire/Pages/jours-feries-chomes-payes.aspx
#   https://www.ontario.ca/document/your-guide-employment-standards-act-0/public-holidays#section-2
#   https://www.cfib-fcei.ca/en/tools-resources/paying-employees-public-holidays-newfoundland-labrador
#   https://www.princeedwardisland.ca/en/information/economic-growth-tourism-and-culture/paid-holidays
#   https://www2.gnb.ca/content/dam/gnb/Departments/petl-epft/PDF/es/FactSheets/PublicHolidaysVacation.pdf
#
# Also those sites for some information
#   https://www.officeholidays.com/holidays/canada/canada-remembrance-day
#   https://www.timeanddate.com/holidays/canada/family-day
#   https://fr.wikipedia.org/wiki/F%C3%AAtes_et_jours_f%C3%A9ri%C3%A9s_au_Canada
#
# I have not checked every province and territory website, but the wikipedia
# summary has been true for everything that I have checked, although it seems
# to be considering more holidays than the bare minimum and also counts holidays
# that are not mandated but usually observed (e.g. St-Patrick's Day in NL which
# is not statutory, but is given to government employees).
#


class en_CA(Locale):
    """
    01-01: [NF] New Year's Day
    06-24: [QC] [F] National Holiday
    07-01: [NF] Canada Day
    11-11: [AB,BC,NB,NL,NT] [F] Remembrance Day
    12-25: [NRF] Christmas Day
    12-26: [NRF] Boxing Day
    2 days before Easter: [NRV] Good Friday
    1 day after Easter: [AB,PE,QC] [RV] Easter Monday
    3. monday in February: [AB,ON,SK,NB] [V] Family Day
    3. monday in February: [MB] [V] Louis Riel Day
    3. monday in February: [PE] [V] Islander Day
    1. monday in August: [NT,NU] [V] August Civic Holiday
    1. monday in August: [SK] [V] Saskatchewan Day
    1. monday in August: [AB,NS] [V] Heritage Day
    1. monday in August: [NB] [V] New Brunswick Day
    1. monday in September: [NV] Labour Day
    2. monday in October: [AB,BC,MB,NL,ON,QC,SK,NT,NU,YT] [V] Thanksgiving Day
    """

    locale = "en-CA"
    easter_type = EASTER_WESTERN

    def holiday_patriot_s_day(self):
        return [Holiday(
            locale=self.locale,
            region="QC",
            date=SmartDayArrow(self.year, 5, 25).shift_to_weekday(
                "monday", order=1, reverse=True, including=False),
            description="National Patriots' Day",
            flags="V",
            notes="")]

    def holiday_victoria_day(self):
        return [Holiday(
            locale=self.locale,
            region=region,
            date=SmartDayArrow(self.year, 5, 25).shift_to_weekday(
                "monday", order=1, reverse=True, including=False),
            description="Victoria Day",
            flags="V",
            notes=""
        ) for region in ["AB", "BC", "MB", "NS", "ON", "SK", "NT", "NU", "YT"]
        ]
