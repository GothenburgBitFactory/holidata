from holidata.holiday import Region
from holidata.utils import day


class TH(Region):
    """
    According to Thüringer Feier- und Gedenktagsgesetz (ThürFGtG) § 2 Abs. 1, § 2 Abs. 2 und 3 Nr. 1
    (https://landesrecht.thueringen.de/perma?d=jlr-FeiertGTHV5P2)
    the holidays are
     - Neujahrstag (New Years Day), *
     - Karfreitag (Good Friday), *
     - Ostermontag (Easter Monday), *
     - 1. Mai (May 1st), *
     - Tag Christi Himmelfahrt (Ascension), *
     - Pfingstmontag (Pentecost Monday), *
     - 20. September als Weltkindertag (Universal Children's Day),
     - 3. Oktober als Tag der Deutschen Einheit (Day of German Unity), *
     - Reformationstag (Reformation Day),
     - erster Weihnachtsfeiertag (Christmas Day), *
     - zweiter Weihnachtsfeiertag (Boxing Day), *
     - Fronleichnam (Corpus Christi, in communities with a catholic majority)

     Holidays marked with '*' are already covered by the definitions in __init__.py
    """
    def __init__(self, country):
        super().__init__("TH", country)

        self.define_holiday() \
            .with_name("Weltkindertag") \
            .since(2019) \
            .on(month=9, day=20) \
            .with_flags("F")

        self.define_holiday() \
            .with_name("Reformationstag") \
            .until(2016) \
            .on(month=10, day=31) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Reformationstag") \
            .since(2018) \
            .on(month=10, day=31) \
            .with_flags("RF")

        self.define_holiday() \
            .with_name("Fronleichnam") \
            .on(day(60).after(country.easter())) \
            .with_flags("RV") \
            .annotated_with("In Gemeinden mit überwiegend katholischer Bevölkerung")
