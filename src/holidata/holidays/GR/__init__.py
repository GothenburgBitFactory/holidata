from dateutil.easter import EASTER_ORTHODOX

from holidata.holiday import Country
from holidata.utils import day, date, Month

__all__ = [
    "GR",
]


class GR(Country):
    id = "GR"
    languages = ["el"]
    easter_type = EASTER_ORTHODOX

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Πρωτοχρονιά") \
            .on(date(Month.JANUARY, 1)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Θεοφάνεια") \
            .on(date(Month.JANUARY, 6)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Ευαγγελισμός της Θεοτόκου και Εθνική Ημέρα Ανεξαρτησίας της Ελλάδας") \
            .on(date(Month.MARCH, 25)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Κοίμηση της Θεοτόκου") \
            .on(date(Month.AUGUST, 15)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Ημέρα του ΌΧΙ") \
            .on(date(Month.OCTOBER, 28)) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Χριστούγεννα") \
            .on(date(Month.DECEMBER, 25)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Επόμενη ημέρα Χριστουγέννων") \
            .on(date(Month.DECEMBER, 26)) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Καθαρά Δευτέρα") \
            .on(day(48).before(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Μεγάλη Παρασκευή") \
            .on(day(2).before(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Μεγάλο Σάββατο") \
            .on(day(1).before(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Πάσχα") \
            .on(self.easter()) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Δευτέρα του Πάσχα") \
            .on(day(1).after(self.easter())) \
            .with_flags("NRV")

        self.define_holiday() \
            .with_name("Δευτέρα του Αγίου Πνεύματος") \
            .on(day(50).after(self.easter())) \
            .with_flags("NRV")

        """
        May day
        Postponed if it collides with Easter
        """
        self.define_holiday() \
            .with_name("Πρωτομαγιά") \
            .on(date(Month.MAY, 1)) \
            .on_condition(date(Month.MAY, 1).is_not_equal_to(self.easter())) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Πρωτομαγιά") \
            .on(date(Month.MAY, 2)) \
            .on_condition(date(Month.APRIL, 30).is_equal_to(self.easter())) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Πρωτομαγιά") \
            .on(date(Month.MAY, 3)) \
            .on_condition(date(Month.MAY, 1).is_equal_to(self.easter())) \
            .with_flags("NF")
