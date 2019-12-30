# coding=utf-8
from dateutil.easter import EASTER_ORTHODOX

from holidata.utils import SmartDayArrow, easter
from .holidays import Holiday, Locale


class el_GR(Locale):
    """
    01-01: [NF] Πρωτοχρονιά
    01-06: [NRF] Θεοφάνεια
    03-25: [NF] Ευαγγελισμός της Θεοτόκου και Εθνική Ημέρα Ανεξαρτησίας της Ελλάδας
    08-15: [NRF] Κοίμηση της Θεοτόκου
    10-28: [NF] Ημέρα του ΌΧΙ
    12-25: [NRF] Χριστούγεννα
    12-26: [NRF] Επόμενη ημέρα Χριστουγέννων
    48 days before Easter: [NRV] Καθαρά Δευτέρα
    2 days before Easter: [NRV] Μεγάλη Παρασκευή
    1 day before Easter: [NRV] Μεγάλο Σάββατο
    Easter: [NRV] Πάσχα
    1 day after Easter: [NRV] Δευτέρα του Πάσχα
    50 days after Easter: [NRV] Δευτέρα του Αγίου Πνεύματος
    """

    locale = "el-GR"
    easter_type = EASTER_ORTHODOX

    def holiday_may_day(self):
        """
        05-01: [NF] Πρωτομαγιά
        Postponed if it collides with Easter
        """
        date = SmartDayArrow(self.year, 5, 1)
        easter_date = easter(self.year, self.easter_type)

        if date == easter_date:
            date = date.shift(days=2)
        elif date == easter_date.shift(days=1):
            date = date.shift(days=1)

        return [Holiday(
            self.locale,
            "",
            date,
            "Πρωτομαγιά",
            "NF"
        )]
