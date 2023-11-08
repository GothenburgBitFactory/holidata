# coding=utf-8
from dateutil.easter import EASTER_WESTERN

from holidata.utils import SmartDayArrow, easter
from .holidays import Locale, Holiday

"""
Information taken from government websites around 2020-06
    https://administracion.gob.es/pag_Home/atencionCiudadana/calendarios/laboral.html
    http://www.seg-social.es/wps/portal/wss/internet/CalendarioLaboral

    2011: https://www.boe.es/eli/es/res/2010/10/07/(1)
          https://www.boe.es/eli/es/res/2010/11/24/(1)
    2012: https://www.boe.es/eli/es/res/2011/10/06/(1)
    2013: https://www.boe.es/eli/es/res/2012/10/30/(1)
          https://www.boe.es/eli/es/res/2012/11/12/(2)
    2014: https://www.boe.es/eli/es/res/2013/11/08/(3)
          https://www.boe.es/eli/es/res/2013/11/21/(1)
    2015: https://www.boe.es/eli/es/res/2014/10/17/(3)
    2016: https://www.boe.es/eli/es/res/2015/10/19/(1)
    2017: https://www.boe.es/eli/es/res/2016/10/04/(1)
    2018: https://www.boe.es/eli/es/res/2017/10/09/(1)
          https://www.boe.es/eli/es/res/2017/10/09/(1)/corrigendum/20171019
          https://www.boe.es/eli/es/res/2017/10/09/(1)/corrigendum/20171025
    2019: https://www.boe.es/eli/es/res/2018/10/16/(1)
    2020: https://www.boe.es/eli/es/res/2019/10/03/(1)
    2021: https://www.boe.es/eli/es/res/2020/10/28/(1)
    2022: https://www.boe.es/eli/es/res/2021/10/14/(3)
    2023: https://www.boe.es/eli/es/res/2022/10/07/(2)
    2024: https://www.boe.es/eli/es/res/2023/10/23/(1)

Regional governments
    [AN] https://www.juntadeandalucia.es/temas/trabajar/relaciones/calendario.html

Also those sites for some information
    https://es.wikipedia.org/wiki/Calendario_laboral
"""


class es_ES(Locale):
    """
    01-01: [NF] Año Nuevo
    01-06: [NRF] Epifanía del Señor
    05-01: [NF] Fiesta del Trabajo
    08-15: [NRF] Asunción de la Virgen
    10-12: [NF] Fiesta Nacional de España
    11-01: [NRF] Todos los Santos
    12-06: [NF] Día de la Constitución Española
    12-08: [NRF] Inmaculada Concepción
    12-25: [NRF] Natividad del Señor
    2 days before Easter: [NRV] Viernes Santo
    Easter: [NRV] Pascua
    """

    locale = "es-ES"
    easter_type = EASTER_WESTERN

    def holiday_lunes_siguiente_al_ano_nuevo(self):
        if self.year == 2012:
            regions = [""]
        elif self.year == 2017:
            regions = ["AN", "AR", "AS", "CL", "MC", "ML"]
        elif self.year == 2023:
            regions = ["AN", "AR", "AS", "CL", "MC"]
        else:
            return []

        return [Holiday(
            self.locale,
            region,
            SmartDayArrow(self.year, 1, 1).shift_to_weekday("monday", including=True),
            "Lunes siguiente al Año Nuevo",
            "NF" if regions == [""] else "F"
        ) for region in regions]

    def holiday_lunes_siguiente_a_la_epifania_del_senor(self):
        if self.year == 2013:
            regions = ["AN", "AR", "AS", "CB", "CE", "CL", "CM", "CN", "EX", "MC", "MD", "ML", "NC"]
        elif self.year == 2019:
            regions = ["AN", "AR", "AS", "CE", "CL", "CN", "EX", "MC", "MD", "ML", "NC"]
        else:
            return []

        return [Holiday(
            self.locale,
            region,
            SmartDayArrow(self.year, 1, 6).shift_to_weekday("monday", including=True),
            "Lunes siguiente a la Epifanía del Señor",
            "NRF" if regions == [""] else "RF"
        ) for region in regions]

    def holiday_martes_de_carnaval(self):
        if self.year in [2023, 2024]:
            return [Holiday(
                self.locale,
                "EX",
                easter(self.year, self.easter_type).shift(days=-47),
                "Martes de Carnaval",
                "V"
            )]
        else:
            return []

    def holiday_dia_de_andalucia(self):
        if self.year == 2016:
            date = SmartDayArrow(self.year, 2, 29)
        elif self.year == 2021:
            date = SmartDayArrow(self.year, 3, 1)
        else:
            date = SmartDayArrow(self.year, 2, 28)

        return [Holiday(
            self.locale,
            "AN",
            date,
            "Día de Andalucía",
            "F"
        )]

    def holiday_dia_de_las_illes_balears(self):
        if self.year in [2011, 2012, 2013, 2014, 2016, 2017, 2018, 2019, 2021, 2022, 2023, 2024]:
            return [Holiday(
                self.locale,
                "IB",
                SmartDayArrow(self.year, 3, 1),
                "Día de las Illes Balears",
                "F"
            )]
        else:
            return []

    def holiday_estatuto_de_autonomia_de_la_ciudad_de_melilla(self):
        if self.year in [2020, 2021]:
            return [Holiday(
                self.locale,
                "ML",
                SmartDayArrow(self.year, 3, 13),
                "Estatuto de Autonomía de la Ciudad de Melilla",
                "F"
            )]
        else:
            return []

    def holiday_san_jose(self):
        if self.year == 2011:
            regions = ["CM", "GA", "MC", "ML", "VC"]
        elif self.year == 2012:
            regions = ["CL", "MC", "MD", "ML", "NC", "RI", "VC"]
        elif self.year == 2013:
            regions = ["MC", "ML", "VC"]
        elif self.year == 2014:
            regions = ["MC", "ML", "NC", "VC"]
        elif self.year == 2015:
            regions = ["MC", "MD", "ML", "NC", "PV", "VC"]
        elif self.year in [2016]:
            regions = ["MC", "ML", "VC"]
        elif self.year == 2018:
            regions = ["MC", "VC"]
        elif self.year == 2019:
            regions = ["GA", "MC", "NC", "PV", "VC"]
        elif self.year == 2020:
            regions = ["CM", "GA", "MC", "NC", "PV", "VC"]
        elif self.year == 2021:
            regions = ["EX", "GA", "MC", "MD", "NC", "PV", "VC"]
        elif self.year == 2022:
            regions = ["VC"]
        elif self.year == 2023:
            regions = ["MD"]
        elif self.year == 2024:
            regions = ["MC", "VC"]
        else:
            return []

        return [Holiday(
            self.locale,
            region,
            SmartDayArrow(self.year, 3, 19),
            "San José",
            "NRF" if regions == [""] else "RF"
        ) for region in regions]

    def holiday_lunes_de_fallas(self):
        if self.year == 2013:
            return [Holiday(
                self.locale,
                "VC",
                SmartDayArrow(self.year, 3, 18),
                "Lunes de Fallas",
                "F"
            )]
        else:
            return []

    def holiday_traslado_de_san_jose(self):
        if self.year == 2013:
            return [Holiday(
                self.locale,
                "MD",
                SmartDayArrow(self.year, 3, 18),
                "Traslado de San José",
                "F"
            )]
        else:
            return []

    def holiday_dia_siguente_a_san_jose(self):
        if self.year == 2015:
            return [Holiday(
                self.locale,
                "GA",
                SmartDayArrow(self.year, 3, 20),
                "Día siguiente a San José",
                "RF"
            )]
        else:
            return []

    def holiday_lunes_siguiente_a_san_jose(self):
        if self.year in [2017]:
            regions = ["EX", "MD"]
        elif self.year == 2023:
            regions = ["MD"]
        else:
            return []

        return [Holiday(
            self.locale,
            region,
            SmartDayArrow(self.year, 3, 19).shift_to_weekday("monday", True),
            "Lunes siguiente a San José",
            "NRF" if regions == [""] else "RF"
        ) for region in regions]

    def holiday_san_jorge__dia_de_aragon(self):
        if self.year == 2017:
            date = SmartDayArrow(self.year, 4, 24)
        else:
            date = SmartDayArrow(self.year, 4, 23)

        return [Holiday(
            self.locale,
            "AR",
            date,
            "San Jorge / Día de Aragón",
            "RF"
        )]

    def holiday_lunes_siguiente_a_san_jorge__dia_de_aragon(self):
        if self.year == 2023:
            date = SmartDayArrow(self.year, 4, 24)
        else:
            return []

        return [Holiday(
            self.locale,
            "AR",
            date,
            "Lunes siguiente a San Jorge / Día de Aragón",
            "RF"
        )]

    def holiday_fiesta_de_castilla_y_leon(self):
        if self.year == 2017:
            date = SmartDayArrow(self.year, 4, 24)
        else:
            date = SmartDayArrow(self.year, 4, 23)

        return [Holiday(
            self.locale,
            "CL",
            date,
            "Fiesta de Castilla y León",
            "F"
        )]

    def holiday_lunes_siguiente_a_la_fiesta_del_trabajo(self):
        if self.year == 2011:
            regions = ["AN", "AR", "AS", "CB", "CE", "EX", "MC", "VC"]
        elif self.year == 2016:
            regions = ["AN", "AR", "AS", "CL", "CN", "EX", "MD"]
        elif self.year == 2022:
            regions = ["AN", "AR", "AS", "CL", "EX", "MC"]
        else:
            return []

        return [Holiday(
            self.locale,
            region,
            SmartDayArrow(self.year, 5, 1).shift_to_weekday("monday", including=True),
            "Lunes siguiente a la Fiesta del Trabajo",
            "NF" if regions == [""] else "F"
        ) for region in regions]

    def holiday_fiesta_de_la_comunidad_de_madrid(self):
        if self.year in [2016, 2021]:
            return []
        else:
            return [Holiday(
                self.locale,
                "MD",
                SmartDayArrow(self.year, 5, 2),
                "Fiesta de la Comunidad de Madrid",
                "F"
            )]

    def holiday_lunes_siguiente_al_dia_de_la_comunidad_de_madrid(self):
        if self.year in [2021]:
            return [Holiday(
                self.locale,
                "MD",
                SmartDayArrow(self.year, 5, 2).shift_to_weekday("monday", including=True),
                "Lunes siguiente al Día de la Comunidad de Madrid",
                "F"
            )]
        else:
            return []

    def holiday_dia_de_las_letras_gallegas(self):
        if self.year in [2015, 2020]:
            return []
        else:
            return [Holiday(
                self.locale,
                "GA",
                SmartDayArrow(self.year, 5, 17),
                "Día de las Letras Gallegas",
                "F"
            )]

    def holiday_dia_de_canarias(self):
        if self.year in [2021]:
            return []
        else:
            return [Holiday(
                self.locale,
                "CN",
                SmartDayArrow(self.year, 5, 30),
                "Día de Canarias",
                "F"
            )]

    def holiday_dia_de_castilla_la_mancha(self):
        if self.year in [2014, 2015, 2020]:
            return []
        else:
            return [Holiday(
                self.locale,
                "CM",
                SmartDayArrow(self.year, 5, 31),
                "Día de Castilla-La Mancha",
                "F"
            )]

    def holiday_dia_de_la_region_de_murcia(self):
        if self.year in [2013, 2024]:
            return []
        elif self.year == 2019:
            date = SmartDayArrow(self.year, 6, 10)
        else:
            date = SmartDayArrow(self.year, 6, 9)

        return [Holiday(
            self.locale,
            "MC",
            date,
            "Día de la Región de Murcia",
            "F"
        )]

    def holiday_dia_de_la_rioja(self):
        if self.year in [2013, 2019]:
            date = SmartDayArrow(self.year, 6, 10)
        else:
            date = SmartDayArrow(self.year, 6, 9)

        if date is not None:
            return [Holiday(
                self.locale,
                "RI",
                date,
                "Día de La Rioja",
                "F"
            )]
        else:
            return []

    def holiday_lunes_siguiente_al_dia_de_la_rioja(self):
        if self.year == 2024:

            return [Holiday(
                self.locale,
                "RI",
                SmartDayArrow(self.year, 6, 10),
                "Lunes siguiente al Día de La Rioja",
                "F"
            )]
        else:
            return []

    def holiday_san_juan(self):
        if self.year == 2011:
            regions = ["CT"]
        elif self.year == 2013:
            regions = ["CT", "GA"]
        elif self.year == 2014:
            regions = ["CT"]
        elif self.year == 2015:
            regions = ["CT"]
        elif self.year == 2016:
            regions = ["CT", "GA"]
        elif self.year == 2017:
            regions = ["CT"]
        elif self.year == 2019:
            regions = ["CT", "VC"]
        elif self.year == 2020:
            regions = ["CT", "GA", "VC"]
        elif self.year == 2021:
            regions = ["CT", "VC"]
        elif self.year == 2022:
            regions = ["CT", "GA", "VC"]
        elif self.year == 2023:
            regions = ["CT", "VC"]
        elif self.year == 2024:
            regions = ["CT", "VC"]
        else:
            return []

        return [Holiday(
            self.locale,
            region,
            SmartDayArrow(self.year, 6, 24),
            "San Juan",
            "NRF" if regions == [""] else "RF"
        ) for region in regions]

    def holiday_santiago_apostol__dia_nacional_de_galicia(self):
        if self.year == 2021:
            return []
        elif self.year == 2023:
            regions = ["CL", "GA", "NC", "PV"]
        elif self.year == 2024:
            regions = ["CB", "GA", "MD", "NC", "PV"]
        else:
            regions = ["GA"]

        return [Holiday(
            self.locale,
            region,
            SmartDayArrow(self.year, 7, 25),
            "Santiago Apóstol / Día Nacional de Galicia",
            "RF"
        ) for region in regions]

    def holiday_santiago_apostol(self):
        if self.year == 2011:
            regions = ["CL", "MD", "NC", "PV", "RI"]
        elif self.year == 2012:
            regions = ["CB"]
        elif self.year == 2013:
            regions = ["CB", "NC", "PV"]
        elif self.year == 2014:
            regions = ["CB"]
        elif self.year == 2015:
            regions = ["NC", "PV"]
        elif self.year == 2016:
            regions = ["MD", "NC", "PV", "RI"]
        elif self.year == 2017:
            regions = ["NC", "PV"]
        elif self.year == 2019:
            regions = ["CB", "PV"]
        elif self.year == 2020:
            regions = ["PV"]
        elif self.year == 2022:
            regions = ["MD", "NC", "PV"]
        else:
            return []

        return [Holiday(
            self.locale,
            region,
            SmartDayArrow(self.year, 7, 25),
            "Santiago Apóstol",
            "NRF" if regions == [""] else "RF"
        ) for region in regions]

    def holiday_dia_de_las_instituciones_de_cantabria(self):
        if self.year in [2011, 2016, 2017, 2018, 2020, 2021, 2022, 2023]:
            return [Holiday(
                self.locale,
                "CB",
                SmartDayArrow(self.year, 7, 28),
                "Día de las Instituciones de Cantabria",
                "F"
            )]
        else:
            return []

    def holiday_nuestra_senora_de_africa(self):
        if self.year in [2022, 2023, 2024]:
            return [Holiday(
                self.locale,
                "CE",
                SmartDayArrow(self.year, 8, 5),
                "Nuestra Señora de África",
                "RF"
            )]
        else:
            return []

    def holiday_lunes_siguiente_a_la_asuncion_de_la_virgen(self):
        if self.year == 2021:
            regions = ["AN", "AR", "AS", "CL", "CN"]
        else:
            return []

        return [Holiday(
            self.locale,
            region,
            SmartDayArrow(self.year, 8, 15).shift_to_weekday("monday", including=True),
            "Lunes siguiente a la Asunción de la Virgen",
            "RF"
        ) for region in regions]

    def holiday_dia_de_ceuta(self):
        if self.year in [2016, 2017, 2019, 2020, 2021, 2022, 2023]:
            return [Holiday(
                self.locale,
                "CE",
                SmartDayArrow(self.year, 9, 2),
                "Día de Ceuta",
                "F"
            )]
        else:
            return []

    def holiday_v_centenario_vuelta_al_mundo(self):
        if self.year == 2022:
            return [Holiday(
                self.locale,
                "PV",
                SmartDayArrow(self.year, 9, 6),
                "V Centenario Vuelta al Mundo",
                "F"
            )]
        else:
            return []

    def holiday_dia_de_asturias(self):
        if self.year in [2019]:
            return []
        else:
            return [Holiday(
                self.locale,
                "AS",
                SmartDayArrow(self.year, 9, 8),
                "Día de Asturias",
                "F"
            )]

    def holiday_lunes_siguiente_al_dia_de_asturias(self):
        if self.year in [2013, 2019, 2024]:
            return [Holiday(
                self.locale,
                "AS",
                SmartDayArrow(self.year, 9, 8).shift_to_weekday("monday", including=True),
                "Lunes siguiente al Día de Asturias",
                "F"
            )]
        else:
            return []

    def holiday_dia_de_extremadura(self):
        if self.year in [2019, 2024]:
            return []
        else:
            return [Holiday(
                self.locale,
                "EX",
                SmartDayArrow(self.year, 9, 8),
                "Día de Extremadura",
                "F"
            )]

    def holiday_lunes_siguiente_al_dia_de_extremadura(self):
        if self.year in [2013, 2019]:
            return [Holiday(
                self.locale,
                "EX",
                SmartDayArrow(self.year, 9, 8).shift_to_weekday("monday", including=True),
                "Lunes siguiente al Día de Extremadura",
                "F"
            )]
        else:
            return []

    def holiday_fiesta_nacional_de_cataluna(self):
        if self.year in [2011, 2016, 2022]:
            return []
        else:
            return [Holiday(
                self.locale,
                "CT",
                SmartDayArrow(self.year, 9, 11),
                "Fiesta Nacional de Cataluña",
                "F"
            )]

    def holiday_la_bien_aparecida(self):
        if self.year in [2011, 2012, 2014, 2014, 2015, 2016, 2017, 2018, 2020, 2021, 2022, 2023]:
            return [Holiday(
                self.locale,
                "CB",
                SmartDayArrow(self.year, 9, 15),
                "La Bien Aparecida",
                "RF")]
        else:
            return []

    def holiday_80_aniversario_del_primer_gobierno_vasco(self):
        if self.year in [2016]:
            return [Holiday(
                self.locale,
                "PV",
                SmartDayArrow(self.year, 10, 7),
                "80º aniversario del primer Gobierno Vasco",
                "F"
            )]
        else:
            return []

    def holiday_dia_de_la_comunitat_valenciana(self):
        if self.year in [2011, 2016, 2022]:
            return []
        else:
            return [Holiday(
                self.locale,
                "VC",
                SmartDayArrow(self.year, 10, 9),
                "Día de la Comunitat Valenciana",
                "F"
            )]

    def holiday_lunes_siguiente_a_la_fiesta_nacional_de_espana(self):
        if self.year == 2014:
            regions = ["AN", "AR", "AS", "CE", "CL", "EX"]
        else:
            return []

        return [Holiday(
            self.locale,
            region,
            SmartDayArrow(self.year, 10, 12).shift_to_weekday("monday", including=True),
            "Lunes siguiente a la Fiesta Nacional de España",
            "F"
        ) for region in regions]

    def holiday_dia_del_pais_vasco_euskadiko_eguna(self):
        if self.year in [2011, 2012, 2013, 2014]:
            return [Holiday(
                self.locale,
                "PV",
                SmartDayArrow(self.year, 10, 25),
                "Día del País Vasco-Euskadiko Eguna",
                "F"
            )]
        else:
            return []

    def holiday_lunes_siguiente_a_todos_los_santos(self):
        if self.year == 2015:
            regions = ["AN", "AR", "AS", "CB", "CE", "CL", "CN", "EX", "GA", "IB"]
        elif self.year == 2020:
            regions = ["AN", "AR", "AS", "CL", "EX", "MD"]
        else:
            return []

        return [Holiday(
            self.locale,
            region,
            SmartDayArrow(self.year, 11, 1).shift_to_weekday("monday", including=True),
            "Lunes siguiente a Todos los Santos",
            "F"
        ) for region in regions]

    def holiday_lunes_siguiente_al_dia_de_la_constitucion_espanola(self):
        if self.year == 2015:
            regions = ["AN", "AR", "AS", "CE", "CL", "CM", "EX", "IB", "MC", "ML", "RI", "VC"]
        elif self.year == 2020:
            regions = ["AN", "AR", "AS", "CE", "CL", "CN", "EX", "IB", "MC", "MD", "ML", "NC", "RI"]
        else:
            return []

        return [Holiday(
            self.locale,
            region,
            SmartDayArrow(self.year, 12, 6).shift_to_weekday("monday", including=True),
            "Lunes siguiente al Día de la Constitución Española",
            "F"
        ) for region in regions]

    def holiday_lunes_siguiente_a_la_inmaculada_concepcion(self):
        if self.year == 2013:
            regions = ["AN", "AR", "AS", "CE", "CL", "EX", "MC", "RI"]
        elif self.year == 2019:
            regions = ["AN", "AR", "AS", "CB", "CL", "EX", "MD", "ML", "RI"]
        elif self.year == 2024:
            regions = ["AN", "AR", "AS", "CL", "EX", "MC", "ML"]
        else:
            return []

        return [Holiday(
            self.locale,
            region,
            SmartDayArrow(self.year, 12, 8).shift_to_weekday("monday", including=True),
            "Lunes siguiente a La Inmaculada Concepción",
            "RF"
        ) for region in regions]

    def holiday_lunes_siguiente_a_la_natividad_del_senor(self):
        if self.year == 2022:
            regions = ["AN", "AR", "AS", "CB", "CL", "CM", "CN", "EX", "IB", "MC", "MD", "ML", "NC", "RI"]
        else:
            return []

        return [Holiday(
            self.locale,
            region,
            SmartDayArrow(self.year, 12, 26),
            "Lunes siguiente a la Natividad del Señor",
            "RF"
        ) for region in regions]

    def holiday_san_esteban(self):
        if self.year == 2011:
            regions = ["AN", "AR", "AS", "CE", "CL", "CN", "CT", "EX", "IB", "ML", "NC"]
        elif self.year == 2012:
            regions = ["CT"]
        elif self.year == 2013:
            regions = ["CT", "IB"]
        elif self.year == 2014:
            regions = ["CT", "IB"]
        elif self.year == 2015:
            regions = ["CT"]
        elif self.year == 2016:
            regions = ["AN", "AR", "AS", "CB", "CE", "CL", "CM", "CT", "EX", "IB", "MC", "MD", "ML", "NC", "VC"]
        elif self.year == 2017:
            regions = ["CT"]
        elif self.year == 2018:
            regions = ["CL"]
        elif self.year == 2019:
            regions = ["CT", "IB"]
        elif self.year == 2020:
            regions = ["CT", "IB"]
        elif self.year == 2022:
            regions = ["CT"]
        elif self.year == 2023:
            regions = ["CT"]
        elif self.year == 2024:
            regions = ["CT"]
        else:
            return []

        return [Holiday(
            self.locale,
            region,
            SmartDayArrow(self.year, 12, 26),
            "San Esteban",
            "NRF" if regions == [""] else "RF"
        ) for region in regions]

    def holiday_jueves_santo(self):
        if self.year in [2011, 2016, 2017, 2022]:
            regions = ["AN", "AR", "AS", "CB", "CE", "CL", "CM", "CN", "EX", "GA", "IB", "MC", "MD", "ML", "NC", "PV", "RI", "VC"]
        elif self.year in [2012, 2013, 2014, 2015, 2019, 2020, 2021, 2024]:
            regions = ["AN", "AR", "AS", "CB", "CE", "CL", "CM", "CN", "EX", "GA", "IB", "MC", "MD", "ML", "NC", "PV", "RI"]
        elif self.year in [2018]:
            regions = ["AN", "AR", "AS", "CE", "CL", "CM", "CN", "EX", "GA", "IB", "MC", "MD", "ML", "NC", "PV", "RI"]
        elif self.year in [2023]:
            regions = ["AN", "AR", "AS", "CB", "CE", "CL", "CM", "CN", "EX", "GA", "IB", "MC", "MD", "ML", "NC", "PV", "VC"]
        else:
            return []

        return [Holiday(
            self.locale,
            region,
            easter(self.year, self.easter_type).shift(days=-3),
            "Jueves Santo",
            "NRV" if regions == [""] else "RV"
        ) for region in regions]

    def holiday_lunes_de_pascua(self):
        if self.year == 2011:
            regions = ["CT", "IB", "NC", "PV", "RI", "VC"]
        elif self.year == 2012:
            regions = ["CT", "IB", "NC", "VC"]
        elif self.year == 2013:
            regions = ["CB", "CT", "IB", "NC", "PV", "RI", "VC"]
        elif self.year == 2014:
            regions = ["CM", "CT", "NC", "PV", "RI", "VC"]
        elif self.year == 2015:
            regions = ["CB", "CM", "CT", "IB", "NC", "PV", "RI", "VC"]
        elif self.year == 2016:
            regions = ["CT", "IB", "NC", "PV", "RI", "VC"]
        elif self.year == 2017:
            regions = ["CT", "IB", "NC", "PV", "RI", "VC"]
        elif self.year == 2018:
            regions = ["CL", "IB", "NC", "PV", "VC"]
        elif self.year == 2019:
            regions = ["CB", "CM", "CT", "IB", "NC", "PV", "RI", "VC"]
        elif self.year == 2020:
            regions = ["CB", "CM", "CT", "IB", "NC", "PV", "RI", "VC"]
        elif self.year == 2021:
            regions = ["CT", "IB", "NC", "PV", "RI", "VC"]
        elif self.year == 2022:
            regions = ["CN", "CT", "IB", "NC", "PV", "RI", "VC"]
        elif self.year == 2023:
            regions = ["CT", "IB", "MC", "NC", "PV", "RI"]
        elif self.year == 2024:
            regions = ["CB", "CT", "IB", "NC", "PV", "RI", "VC"]
        else:
            return []

        return [Holiday(
            self.locale,
            region,
            easter(self.year, self.easter_type).shift_to_weekday("monday", including=True),
            "Lunes de Pascua",
            "NRV" if regions == [""] else "RV"
        ) for region in regions]

    def holiday_lunes_de_pascua_granada(self):
        if self.year == 2011:
            date = SmartDayArrow(self.year, 6, 13)
        elif self.year == 2016:
            date = SmartDayArrow(self.year, 5, 16)
        elif self.year == 2022:
            date = SmartDayArrow(self.year, 6, 6)
        else:
            return []

        return [Holiday(
            self.locale,
            "CT",
            date,
            "Lunes de Pascua Granada",
            "F"
        )]

    def holiday_corpus_christi(self):
        if self.year in [2012, 2013, 2016, 2017, 2019, 2020, 2021, 2022, 2023, 2024]:
            regions = ["CM"]
        elif self.year in [2011, 2014, 2015]:
            regions = ["CM", "MD"]
        else:
            return []

        return [Holiday(
            self.locale,
            region,
            easter(self.year, self.easter_type).shift(days=60),
            "Corpus Christi",
            "RV"
        ) for region in regions]

    def holiday_eid_fitr(self):
        if self.year == 2022:
            date = SmartDayArrow(self.year, 5, 3)
        elif self.year == 2023:
            date = SmartDayArrow(self.year, 4, 21)
        else:
            return []

        return [Holiday(
            self.locale,
            "ML",
            date,
            "Fiesta del Eid Fitr",
            "RV"
        )]

    def holiday_eidul_adha(self):
        if self.year == 2012:
            date = SmartDayArrow(self.year, 10, 27)
        elif self.year == 2013:
            date = SmartDayArrow(self.year, 10, 15)
        elif self.year == 2014:
            date = SmartDayArrow(self.year, 10, 6)
        elif self.year == 2015:
            date = SmartDayArrow(self.year, 9, 25)
        elif self.year == 2016:
            date = SmartDayArrow(self.year, 9, 12)
        elif self.year == 2017:
            date = SmartDayArrow(self.year, 9, 1)
        elif self.year == 2018:
            date = SmartDayArrow(self.year, 8, 22)
        elif self.year == 2019:
            date = SmartDayArrow(self.year, 8, 12)
        elif self.year == 2020:
            date = SmartDayArrow(self.year, 7, 31)
        elif self.year == 2021:
            date = SmartDayArrow(self.year, 7, 20)
        elif self.year == 2022:
            date = SmartDayArrow(self.year, 7, 9)
        elif self.year == 2023:
            date = SmartDayArrow(self.year, 6, 29)
        elif self.year == 2024:
            date = SmartDayArrow(self.year, 6, 17)
        else:
            return []

        return [Holiday(
            self.locale,
            "CE",
            date,
            "Fiesta del Sacrificio (Eidul Adha)",
            "RV"
        )]

    def holiday_aid_al_adha(self):
        if self.year == 2022:
            date = SmartDayArrow(self.year, 7, 11)
        elif self.year == 2023:
            date = SmartDayArrow(self.year, 6, 29)
        elif self.year == 2024:
            date = SmartDayArrow(self.year, 6, 17)
        else:
            return []

        return [Holiday(
            self.locale,
            "ML",
            date,
            "Fiesta del Sacrificio (Aid Al Adha)",
            "RV"
        )]

    def holiday_lunes_siguiente_al_eidul_adha(self):
        if self.year == 2011:
            date = SmartDayArrow(self.year, 11, 7)
        else:
            return []

        return [Holiday(
            self.locale,
            "CE",
            date,
            "Lunes siguiente a la Fiesta del Sacrificio (Eidul Adha)",
            "RV"
        )]

    def holiday_aid_el_kebir(self):
        if self.year == 2011:
            date = SmartDayArrow(self.year, 11, 7)
        elif self.year == 2012:
            date = SmartDayArrow(self.year, 10, 26)
        elif self.year == 2013:
            date = SmartDayArrow(self.year, 10, 15)
        elif self.year == 2014:
            date = SmartDayArrow(self.year, 10, 4)
        elif self.year == 2015:
            date = SmartDayArrow(self.year, 9, 25)
        elif self.year == 2016:
            date = SmartDayArrow(self.year, 9, 12)
        elif self.year == 2017:
            date = SmartDayArrow(self.year, 9, 1)
        elif self.year == 2018:
            date = SmartDayArrow(self.year, 8, 22)
        elif self.year == 2019:
            date = SmartDayArrow(self.year, 8, 12)
        elif self.year == 2020:
            date = SmartDayArrow(self.year, 7, 31)
        elif self.year == 2021:
            date = SmartDayArrow(self.year, 7, 21)
        else:
            return []

        return [Holiday(
            self.locale,
            "ML",
            date,
            "Fiesta del Sacrificio (Aid El Kebir)",
            "RV"
        )]
