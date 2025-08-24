from dateutil.easter import EASTER_ORTHODOX

from holidata.holiday import Country
from holidata.utils import SmartDayArrow, day

__all__ = [
    "GR",
]


class GR(Country):
    id = "GR"
    languages = ["el"]
    default_lang = "el"
    easter_type = EASTER_ORTHODOX

    def __init__(self):
        super().__init__()

        self.define_holiday() \
            .with_name("Πρωτοχρονιά") \
            .on(month=1, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Θεοφάνεια") \
            .on(month=1, day=6) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Ευαγγελισμός της Θεοτόκου και Εθνική Ημέρα Ανεξαρτησίας της Ελλάδας") \
            .on(month=3, day=25) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Κοίμηση της Θεοτόκου") \
            .on(month=8, day=15) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Ημέρα του ΌΧΙ") \
            .on(month=10, day=28) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Χριστούγεννα") \
            .on(month=12, day=25) \
            .with_flags("NRF")

        self.define_holiday() \
            .with_name("Επόμενη ημέρα Χριστουγέννων") \
            .on(month=12, day=26) \
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

        self.define_holiday() \
            .with_name("Πρωτομαγιά") \
            .on(self.date_for_may_day) \
            .with_flags("NF")

    def date_for_may_day(self, year):
        """
        Postponed if it collides with Easter
        """
        date = SmartDayArrow(year, 5, 1)
        easter_date = self.easter()(year)

        if date == easter_date:
            date = date.shift(days=2)
        elif date == easter_date.shift(days=1):
            date = date.shift(days=1)

        return date
