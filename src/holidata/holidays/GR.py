from dateutil.easter import EASTER_ORTHODOX

from .holidays import Country
from holidata.utils import SmartDayArrow, easter


class GR(Country):
    id = "GR"
    languages = ["el"]
    default_lang = "el"
    easter_type = EASTER_ORTHODOX

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Πρωτοχρονιά") \
            .on("01-01") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Θεοφάνεια") \
            .on("01-06") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Ευαγγελισμός της Θεοτόκου και Εθνική Ημέρα Ανεξαρτησίας της Ελλάδας") \
            .on("03-25") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Κοίμηση της Θεοτόκου") \
            .on("08-15") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Ημέρα του ΌΧΙ") \
            .on("10-28") \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Χριστούγεννα") \
            .on("12-25") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Επόμενη ημέρα Χριστουγέννων") \
            .on("12-26") \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Καθαρά Δευτέρα") \
            .on("48 days before Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Μεγάλη Παρασκευή") \
            .on("2 days before Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Μεγάλο Σάββατο") \
            .on("1 day before Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Πάσχα") \
            .on("Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Δευτέρα του Πάσχα") \
            .on("1 day after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Δευτέρα του Αγίου Πνεύματος") \
            .on("50 days after Easter") \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Πρωτομαγιά") \
            .on(self.date_for_may_day) \
            .with_flags("NF")

    def date_for_may_day(self, year):
        """
        Postponed if it collides with Easter
        """
        date = SmartDayArrow(year, 5, 1)
        easter_date = easter(year, self.easter_type)

        if date == easter_date:
            date = date.shift(days=2)
        elif date == easter_date.shift(days=1):
            date = date.shift(days=1)

        return date
