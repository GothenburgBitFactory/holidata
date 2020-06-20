# coding=utf-8
from dateutil.easter import EASTER_WESTERN

from .holidays import Locale


class es_ES(Locale):
    """
    01-01: [NF] Año Nuevo
    01-06: [NRF] Día de los Reyes
    02-28: [AN] [F] Día de Andalucía
    05-01: [NF] Fiesta del Trabajo
    08-15: [NRF] Asunción de la Virgen
    10-12: [NF] Fiesta Nacional de España
    11-01: [NRF] Dia de todos los Santos
    12-06: [NF] Dia de la Constitución
    12-08: [NRF] Inmaculada Concepción
    12-24: [NRF] Noche Buena
    12-25: [NRF] Navidad
    12-31: [NF] Noche Vieja
    3 days before Easter: [AN] [RV] Jueves Santo
    2 days before Easter: [NRV] Viernes Santo
    Easter: [NRV] Pascua
    """

    locale = "es-ES"
    easter_type = EASTER_WESTERN

    def ano_nuevo_en_domingo(self):
        date = SmartDayArrow(self.year, 1, 1)
        if date.weekday() == 'sunday':
            return [Holiday(
                    locale=self.locale,
                    region="AN",
                    date=date.shift(1),
                    desctription="Lunes siguiente a Año Nuevo",
                    flags="V",
                    notes="")]
        return []

    def epifania_del_senor_en_domingo(self):
        date = SmartDayArrow(self.year, 1, 6)
        if date.weekday() == 'sunday':
            return [Holiday(
                    locale=self.locale,
                    region="AN",
                    date=date.shift(1),
                    desctription="Lunes siguiente a la Epifanía del Señor",
                    flags="RV",
                    notes="")]
        return []

    def dia_de_andalucia_en_domingo(self):
        date = SmartDayArrow(self.year, 2, 28)
        if date.weekday() == 'sunday':
            return [Holiday(
                    locale=self.locale,
                    region="AN",
                    date=date.shift(1),
                    desctription="Lunes siguiente al Día de Andalucía",
                    flags="V",
                    notes="")]
        return []

    def fiesta_del_trabajo_en_domingo(self):
        date = SmartDayArrow(self.year, 5, 1)
        if date.weekday() == 'sunday':
            return [Holiday(
                    locale=self.locale,
                    region="AN",
                    date=date.shift(1),
                    desctription="Lunes siguiente a la Fiesta del Trabajo",
                    flags="V",
                    notes="")]
        return []

    def todos_los_santos_en_domingo(self):
        date = SmartDayArrow(self.year, 11, 1)
        if date.weekday() == 'sunday':
            return [Holiday(
                    locale=self.locale,
                    region="AN",
                    date=date.shift(1),
                    desctription="Lunes siguiente a todos los Santos",
                    flags="RV",
                    notes="")]
        return []

    def constitucion_espanola_en_domingo(self):
        date = SmartDayArrow(self.year, 12, 6)
        if date.weekday() == 'sunday':
            return [Holiday(
                    locale=self.locale,
                    region="AN",
                    date=date.shift(1),
                    desctription="Lunes siguiente a la Constitución Española",
                    flags="V",
                    notes="")]
        return []

    def inmaculada_concepcion_en_domingo(self):
        date = SmartDayArrow(self.year, 12, 8)
        if date.weekday() == 'sunday':
            return [Holiday(
                    locale=self.locale,
                    region="AN",
                    date=date.shift(1),
                    desctription="Lunes siguiente a Inmaculada Concepción",
                    flags="RV",
                    notes="")]
        return []

    def navidad_en_domingo(self):
        date = SmartDayArrow(self.year, 12, 25)
        if date.weekday() == 'sunday':
            return [Holiday(
                    locale=self.locale,
                    region="AN",
                    date=date.shift(1),
                    desctription="Lunes siguiente a Navidad",
                    flags="RV",
                    notes="")]
        return []
