# coding=utf-8
from dateutil.easter import EASTER_WESTERN

from .holidays import Locale


class de_CH(Locale):
    """
    01-01: [NF] Neujahrstag
    01-02: [BE,JU,TG,VD] [F] Berchtoldstag
    01-06: [SZ,TI,UR] [RF] Heilige Drei Könige
    03-19: [NW,SZ,TI,UR,VS] [RF] Josefstag
    05-01: [BL,BS,GR,NE,SH,TG,TI,ZH] [F] Tag der Arbeit
    08-01: [NF] Bundesfeier
    08-15: [AI] [RF] Mariä Himmelfahrt
    08-15: [JU,LU,NW,OW,SZ,TI,UR,VS,ZG] [RF] Mariä Himmelfahrt
    11-01: [AI,GL,JU,LU,NW,OW,SG,SZ,TI,UR,VS,ZG] [RF] Allerheiligen
    12-08: [AI] [RF] Mariä Empfängnis
    12-08: [LU,NW,OW,SZ,TI,UR,VS,ZG] [RF] Mariä Empfängnis
    12-25: [NRF] Weihnachtstag
    12-26: [AI,AR,BE,BL,BS,GL,GR,LU,SG,SH,SZ,TG,TI,UR,ZH] [RF] Stephanstag
    2 days before Easter: [AG,AI,AR,BE,BL,BS,FR,GE,GL,GR,JU,LU,NE,NW,OW,SG,SH,SO,SZ,TG,UR,VD,ZG,ZH] [RV] Karfreitag
    Easter: [NRV] Ostersonntag
    1 day after Easter: [AI,AR,BE,BL,BS,GE,GL,GR,JU,SG,SH,SZ,TG,TI,UR,VD,ZH] [RV] Ostermontag
    39 days after Easter: [NRV] Auffahrt
    49 days after Easter: [NRV] Pfingstsonntag
    50 days after Easter: [AI,AR,BE,BL,BS,GE,GL,GR,JU,SG,SH,SZ,TG,TI,UR,VD,ZH] [RV] Pfingstmontag
    60 days after Easter: [AI,JU,LU,NW,OW,SZ,TI,UR,VS,ZG] [RV] Fronleichnam
    """

    locale = "de-CH"
    easter_type = EASTER_WESTERN
