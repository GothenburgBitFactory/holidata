from dateutil.easter import EASTER_WESTERN

from .holidays import Country


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
            .on("01-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "de": "Tag der Arbeit",
                "fr": "Fête du Travail",
                "nl": "Dag van de arbeid",
            }) \
            .on("05-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "de": "Nationalfeiertag",
                "fr": "Fête nationale",
                "nl": "Nationale feestdag",
            }) \
            .on("07-21") \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "de": "Mariä Himmelfahrt",
                "fr": "Assomption",
                "nl": "Onze Lieve Vrouw hemelvaart",
            }) \
            .on("08-15") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_names({
                "de": "Allerheiligen",
                "fr": "Toussaint",
                "nl": "Allerheiligen",
            }) \
            .on("11-01") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_names({
                "de": "Waffenstillstand",
                "fr": "Jour de l'armistice",
                "nl": "Wapenstilstand",
            }) \
            .on("11-11") \
            .with_flags("NF")

        self.define_holiday() \
            .with_names({
                "de": "Weihnacht",
                "fr": "Noël",
                "nl": "Kerstmis",
            }) \
            .on("12-25") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_names({
                "de": "Ostern",
                "fr": "Pâques",
                "nl": "Pasen",
            }) \
            .on("Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_names({
                "de": "Ostermontag",
                "fr": "Lundi de Pâques",
                "nl": "Paasmaandag",
            }) \
            .on("1 day after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_names({
                "de": "Christi Himmelfahrt",
                "fr": "Ascension",
                "nl": "Onze Lieve Heer hemelvaart",
            }) \
            .on("39 days after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_names({
                "de": "Pfingsten",
                "fr": "Pentecôte",
                "nl": "Pinksteren",
            }) \
            .on("49 days after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_names({
                "de": "Pfingstmontag",
                "fr": "Lundi de Pentecôte",
                "nl": "Pinkstermaandag",
            }) \
            .on("50 days after Easter") \
            .with_flags("NRV")
