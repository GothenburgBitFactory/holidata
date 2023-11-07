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
#   https://www.gov.mb.ca/labour/standards/doc,gen-holidays-after-april-30-07,factsheet.html#q12
#   https://www.saskatchewan.ca/business/employment-standards/vacations-holidays-leaves-and-absences/public-statutory-holidays/list-of-saskatchewan-public-holidays
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


class fr_CA(Locale):
    """
    01-01: [NF] Jour de l'An
    06-24: [QC] [F] Fête Nationale
    07-01: [NF] Fête du Canada
    11-11: [AB,BC,NB,NL,NT] [F] Jour du Souvenir
    12-25: [NRF] Jour de Noël
    12-26: [NRF] Lendemain de Noël
    2 days before Easter: [NRV] Vendredi Saint
    1 day after Easter: [AB,PE,QC] [RV] Lundi de Pâques
    3. monday in February: [AB,ON,SK,NB] [V] Fête de la Famille
    3. monday in February: [MB] [V] Journée Louis Riel
    3. monday in February: [PE] [V] Fête des Insulaires
    1. monday in August: [NT,NU] [V] Premier lundi d'août
    1. monday in August: [AB] [V] Fête du Patrimoine
    1. monday in August: [SK] [V] Fête de la Saskatchewan
    1. monday in August: [NS] [V] Jour de la Fondation
    1. monday in August: [NB] [V] Jour du Nouveau-Brunswick
    1. monday in September: [NV] Fête du Travail
    2. monday in October: [AB,BC,MB,NL,ON,QC,SK,NT,NU,YT] [V] Jour de l'Action de grâce
    """

    locale = "fr-CA"
    easter_type = EASTER_WESTERN

    def holiday_journee_nationale_des_patriotes(self):
        return [Holiday(
            locale=self.locale,
            region="QC",
            date=SmartDayArrow(self.year, 5, 25).shift_to_weekday(
                "monday", order=1, reverse=True, including=False),
            description="Journée Nationale des Patriotes",
            flags="V",
            notes="")]

    def holiday_fete_de_la_reine_victoria(self):
        return [Holiday(
            locale=self.locale,
            region=region,
            date=SmartDayArrow(self.year, 5, 25).shift_to_weekday(
                "monday", order=1, reverse=True, including=False),
            description="Fête de la Reine Victoria",
            flags="V",
            notes=""
        ) for region in ["AB", "BC", "MB", "NS", "ON", "SK", "NT", "NU", "YT"]
        ]
