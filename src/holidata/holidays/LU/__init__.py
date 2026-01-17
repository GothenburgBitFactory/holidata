from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country

__all__ = [
    "LU",
]

from holidata.utils import Month, date, day

"""
source: Code du Travail - Art. L. 232-2
<2019: https://data.legilux.public.lu/eli/etat/leg/code/travail/20181101
>2019: https://data.legilux.public.lu/eli/etat/leg/code/travail/20260101
"""


class LU(Country):
    id = "LU"
    languages = ["de", "en", "fr", "lb"]
    default_lang = "lb"
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_names({
                "de": "Neujahr",
                "en": "New Year",
                "fr": "Nouvel An",
                "lb": "Neijoerschdag",
            }) \
            .on(date(Month.JANUARY, 1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "de": "1. Mai",
                "en": "Mayday",
                "fr": "Premier Mai",
                "lb": "Éischte Mee",
            }) \
            .on(date(Month.MAY, 1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "de": "Europatag",
                "en": "Europe Day",
                "fr": "Journée de l'Europe",
                "lb": "Europadag",
            }) \
            .since(2019) \
            .on(date(Month.MAY, 9)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "de": "Nationalfeiertag",
                "en": "National Day",
                "fr": "Fête nationale",
                "lb": "Nationalfeierdag",
            }) \
            .on(date(Month.JUNE, 23)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "de": "Mariä Himmelfahrt",
                "en": "Assumption",
                "fr": "Assomption",
                "lb": "Léiffrawëschdag",
            }) \
            .on(date(Month.AUGUST, 15)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_names({
                "de": "Allerheiligen",
                "en": "All Saints",
                "fr": "Toussaint",
                "lb": "Allerhellegen",
            }) \
            .on(date(Month.NOVEMBER, 1)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_names({
                "de": "Weihnachten",
                "en": "Christmas",
                "fr": "Noël",
                "lb": "Chrëschtdag",
            }) \
            .on(date(Month.DECEMBER, 25)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_names({
                "de": "2. Weihnachtsfeiertag",
                "en": "Boxing Day",
                "fr": "Saint Étienne",
                "lb": "Stiefesdag",
            }) \
            .on(date(Month.DECEMBER, 26)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_names({
                "de": "Ostern",
                "en": "Easter",
                "fr": "Pâques",
                "lb": "Ouschteren",
            }) \
            .on(self.easter()) \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "de": "Ostermontag",
                "en": "Easter Monday",
                "fr": "Lundi de Pâques",
                "lb": "Ouschterméindeg",
            }) \
            .on(day(1).after(self.easter())) \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "de": "Christi Himmelfahrt",
                "en": "Ascension Day",
                "fr": "Ascension",
                "lb": "Christi Himmelfaart",
            }) \
            .on(day(39).after(self.easter())) \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "de": "Pfingsten",
                "en": "Pentecost",
                "fr": "Pentecôte",
                "lb": "Péngschten",
            }) \
            .on(day(49).after(self.easter())) \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "de": "Pfingstmontag",
                "en": "Whit Monday",
                "fr": "Lundi de Pentecôte",
                "lb": "Péngschtméindeg",
            }) \
            .on(day(50).after(self.easter())) \
            .with_flags("NF")
