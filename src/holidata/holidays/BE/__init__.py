from dateutil.easter import EASTER_WESTERN

from holidata.holiday import Country
from holidata.utils import day

__all__ = [
    "BE",
]


class BE(Country):
    id = "BE"
    languages = ["de", "fr", "nl"]
    easter_type = EASTER_WESTERN

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_names({
                "de": "Neujahr",
                "fr": "Nouvel An",
                "nl": "Nieuwjaar",
            }) \
            .on(month=1, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "de": "Tag der Arbeit",
                "fr": "Fête du Travail",
                "nl": "Dag van de arbeid",
            }) \
            .on(month=5, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "de": "Nationalfeiertag",
                "fr": "Fête nationale",
                "nl": "Nationale feestdag",
            }) \
            .on(month=7, day=21) \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "de": "Mariä Himmelfahrt",
                "fr": "Assomption",
                "nl": "Onze Lieve Vrouw hemelvaart",
            }) \
            .on(month=8, day=15) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_names({
                "de": "Allerheiligen",
                "fr": "Toussaint",
                "nl": "Allerheiligen",
            }) \
            .on(month=11, day=1) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_names({
                "de": "Waffenstillstand",
                "fr": "Jour de l'armistice",
                "nl": "Wapenstilstand",
            }) \
            .on(month=11, day=11) \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "de": "Weihnacht",
                "fr": "Noël",
                "nl": "Kerstmis",
            }) \
            .on(month=12, day=25) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_names({
                "de": "Ostern",
                "fr": "Pâques",
                "nl": "Pasen",
            }) \
            .on(self.easter()) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_names({
                "de": "Ostermontag",
                "fr": "Lundi de Pâques",
                "nl": "Paasmaandag",
            }) \
            .on(day(1).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_names({
                "de": "Christi Himmelfahrt",
                "fr": "Ascension",
                "nl": "Onze Lieve Heer hemelvaart",
            }) \
            .on(day(39).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_names({
                "de": "Pfingsten",
                "fr": "Pentecôte",
                "nl": "Pinksteren",
            }) \
            .on(day(49).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_names({
                "de": "Pfingstmontag",
                "fr": "Lundi de Pentecôte",
                "nl": "Pinkstermaandag",
            }) \
            .on(day(50).after(self.easter())) \
            .with_flags("NRV")
