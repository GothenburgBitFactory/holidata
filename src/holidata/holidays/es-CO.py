# coding=utf-8
from dateutil.easter import EASTER_WESTERN

from holidata.utils import SmartDayArrow
from .holidays import Holiday, Locale

"""
LEY 51 DE 1983
http://www.suin-juriscol.gov.co/viewDocument.asp?id=1605519
"""


class es_CO(Locale):
    """
    01-01: [NF] Año Nuevo
    05-01: [NF] Día del Trabajo
    07-20: [NF] Grito de Independencia
    08-07: [NF] Batalla de Boyacá
    12-08: [NRF] Inmaculada Concepción
    12-25: [NRF] Navidad
    3 days before Easter: [NRV] Jueves Santo
    2 days before Easter: [NRV] Viernes Santo
    Easter: [NRV] Domingo de Pascua
    43 days after Easter: [NRV] La Ascensión del Señor
    64 days after Easter: [NRV] Corpus Christi
    71 days after Easter: [NRV] El Sagrado Corazón de Jesús
    """

    locale = "es-CO"
    easter_type = EASTER_WESTERN

    def holiday_reyes(self):
        """First Monday after January 6."""
        return [Holiday(
            self.locale,
            "",
            SmartDayArrow(self.year, 1, 6).shift_to_weekday("monday", including=True),
            "Día de los Reyes Magos",
            "NRV"
        )]

    def holiday_san_jose(self):
        """First Monday after March 19."""
        return [Holiday(
            self.locale,
            "",
            SmartDayArrow(self.year, 3, 19).shift_to_weekday("monday", including=True),
            "Día de San José",
            "NRV"
        )]

    def holiday_san_pedro_san_pablo(self):
        """First Monday after June 29."""
        return [Holiday(
            self.locale,
            "",
            SmartDayArrow(self.year, 6, 29).shift_to_weekday("monday", including=True),
            "San Pedro y San Pablo",
            "NRV"
        )]

    def holiday_asuncion(self):
        """First Monday after August 15."""
        return [Holiday(
            self.locale,
            "",
            SmartDayArrow(self.year, 8, 15).shift_to_weekday("monday", including=True),
            "Asunción de la Virgen",
            "NRV"
        )]

    def holiday_dia_raza(self):
        """First Monday after October 12."""
        return [Holiday(
            self.locale,
            "",
            SmartDayArrow(self.year, 10, 12).shift_to_weekday("monday", including=True),
            "Día de la Raza",
            "NV"
        )]

    def holiday_todos_santos(self):
        """First Monday after November 1."""
        return [Holiday(
            self.locale,
            "",
            SmartDayArrow(self.year, 11, 1).shift_to_weekday("monday", including=True),
            "Todos los Santos",
            "NRV"
        )]

    def holiday_independencia_cartagena(self):
        """First Monday after November 11."""
        return [Holiday(
            self.locale,
            "",
            SmartDayArrow(self.year, 11, 11).shift_to_weekday("monday", including=True),
            "Independencia de Cartagena",
            "NV"
        )]

