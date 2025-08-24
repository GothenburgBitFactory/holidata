from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import day, first, third, second

__all__ = [
    "CA",
]


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


class CA(Country):
    id = "CA"
    languages = ["en", "fr"]
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_names({
                "en": "New Year's Day",
                "fr": "Jour de l'An",
            }) \
            .on(month=1, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "en": "National Holiday",
                "fr": "Fête Nationale",
            }) \
            .in_regions(["QC"]) \
            .on(month=6, day=24) \
            .with_flags("F")

        self.define_holiday() \
            .with_names({
                "en": "Canada Day",
                "fr": "Fête du Canada",
            }) \
            .on(month=7, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "en": "Remembrance Day",
                "fr": "Jour du Souvenir",
            }) \
            .in_regions(["AB", "BC", "NB", "NL", "NT"]) \
            .on(month=11, day=11) \
            .with_flags("F")

        self.define_holiday() \
            .with_names({
                "en": "Christmas Day",
                "fr": "Jour de Noël",
            }) \
            .on(month=12, day=25) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_names({
                "en": "Boxing Day",
                "fr": "Lendemain de Noël",
            }) \
            .on(month=12, day=26) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_names({
                "en": "Good Friday",
                "fr": "Vendredi Saint",
            }) \
            .on(day(2).before(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_names({
                "en": "Easter Monday",
                "fr": "Lundi de Pâques",
            }) \
            .in_regions(["AB", "PE", "QC"]) \
            .on(day(1).after(self.easter())) \
            .with_flags("RV")

        self.define_holiday() \
            .with_names({
                "en": "Family Day",
                "fr": "Fête de la Famille",
            }) \
            .in_regions(["AB", "ON", "SK", "NB"]) \
            .on(third("monday").of("february")) \
            .with_flags("V")

        self.define_holiday() \
            .with_names({
                "en": "Louis Riel Day",
                "fr": "Journée Louis Riel",
            }) \
            .in_regions(["MB"]) \
            .on(third("monday").of("february")) \
            .with_flags("V")

        self.define_holiday() \
            .with_names({
                "en": "Islander Day",
                "fr": "Fête des Insulaires",
            }) \
            .in_regions(["PE"]) \
            .on(third("monday").of("february")) \
            .with_flags("V")

        self.define_holiday() \
            .with_names({
                "en": "August Civic Holiday",
                "fr": "Premier lundi d'août",
            }) \
            .in_regions(["NT", "NU"]) \
            .on(first("monday").of("august")) \
            .with_flags("V")

        self.define_holiday() \
            .with_names({
                "en": "Saskatchewan Day",
                "fr": "Fête de la Saskatchewan",
            }) \
            .in_regions(["SK"]) \
            .on(first("monday").of("august")) \
            .with_flags("V")

        self.define_holiday() \
            .with_names({
                "en": "Heritage Day",
                "fr": "Fête du Patrimoine",
            }) \
            .in_regions(["AB"]) \
            .on(first("monday").of("august")) \
            .with_flags("V")

        self.define_holiday() \
            .with_names({
                "en": "Heritage Day",
                "fr": "Jour de la Fondation",
            }) \
            .in_regions(["NS"]) \
            .on(first("monday").of("august")) \
            .with_flags("V")

        self.define_holiday() \
            .with_names({
                "en": "New Brunswick Day",
                "fr": "Jour du Nouveau-Brunswick",
            }) \
            .in_regions(["NB"]) \
            .on(first("monday").of("august")) \
            .with_flags("V")

        self.define_holiday() \
            .with_names({
                "en": "Labour Day",
                "fr": "Fête du Travail",
            }) \
            .on(first("monday").of("september")) \
            .with_flags("NV")

        self.define_holiday() \
            .with_names({
                "en": "Thanksgiving Day",
                "fr": "Jour de l'Action de grâce",
            }) \
            .in_regions(["AB", "BC", "MB", "NL", "ON", "QC", "SK", "NT", "NU", "YT"]) \
            .on(second("monday").of("october")) \
            .with_flags("V")

        self.define_holiday() \
            .with_names({
                "en": "National Patriots' Day",
                "fr": "Journée Nationale des Patriotes",
            }) \
            .in_regions(["QC"]) \
            .on(first("monday").before(month=5, day=25)) \
            .with_flags("V")

        self.define_holiday() \
            .with_names({
                "en": "Victoria Day",
                "fr": "Fête de la Reine Victoria",
            }) \
            .in_regions(["AB", "BC", "MB", "NS", "ON", "SK", "NT", "NU", "YT"]) \
            .on(first("monday").before(month=5, day=25)) \
            .with_flags("V")
