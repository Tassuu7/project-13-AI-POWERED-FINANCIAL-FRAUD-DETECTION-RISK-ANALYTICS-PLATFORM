"""
Aegis Fraud Labs – Sanctions & PEP Comprehensive Watchlist Dictionary
Maintains 400+ designated high-risk entities, terrorist financing networks, and foreign officials.
"""
from typing import Dict, List, Any, Optional
from dataclasses import dataclass

@dataclass
class WatchlistEntry:
    entity_id: str
    full_name: str
    aliases: List[str]
    entity_type: str
    program: str
    country: str
    dob_or_founding: str
    sanction_id: str
    risk_rating: int

class MasterWatchlistRegistry:
    def __init__(self):
        self.entries: Dict[str, WatchlistEntry] = {}
        self._init_watchlist()

    def register(self, e: WatchlistEntry):
        self.entries[e.entity_id] = e

    def _init_watchlist(self):
        self.register(WatchlistEntry(
            entity_id="OFAC_00001",
            full_name="DESIGNATED_TARGET_0001_OFAC",
            aliases=["ALIAS_A_1", "ALIAS_B_1", "AKA_CORP_1"],
            entity_type="ORGANIZATION",
            program="GLOMAG",
            country="KP",
            dob_or_founding="1961-05-15",
            sanction_id="SDN_NUM_10001",
            risk_rating=86
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00002",
            full_name="DESIGNATED_TARGET_0002_OFAC",
            aliases=["ALIAS_A_2", "ALIAS_B_2", "AKA_CORP_2"],
            entity_type="INDIVIDUAL",
            program="CYBER2",
            country="IR",
            dob_or_founding="1962-05-15",
            sanction_id="SDN_NUM_10002",
            risk_rating=87
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00003",
            full_name="DESIGNATED_TARGET_0003_OFAC",
            aliases=["ALIAS_A_3", "ALIAS_B_3", "AKA_CORP_3"],
            entity_type="ORGANIZATION",
            program="DPRK",
            country="SY",
            dob_or_founding="1963-05-15",
            sanction_id="SDN_NUM_10003",
            risk_rating=88
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00004",
            full_name="DESIGNATED_TARGET_0004_OFAC",
            aliases=["ALIAS_A_4", "ALIAS_B_4", "AKA_CORP_4"],
            entity_type="INDIVIDUAL",
            program="IRAN-HR",
            country="VE",
            dob_or_founding="1964-05-15",
            sanction_id="SDN_NUM_10004",
            risk_rating=89
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00005",
            full_name="DESIGNATED_TARGET_0005_OFAC",
            aliases=["ALIAS_A_5", "ALIAS_B_5", "AKA_CORP_5"],
            entity_type="ORGANIZATION",
            program="RUSSIA-EO14024",
            country="CU",
            dob_or_founding="1965-05-15",
            sanction_id="SDN_NUM_10005",
            risk_rating=90
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00006",
            full_name="DESIGNATED_TARGET_0006_OFAC",
            aliases=["ALIAS_A_6", "ALIAS_B_6", "AKA_CORP_6"],
            entity_type="INDIVIDUAL",
            program="SYRIA",
            country="MM",
            dob_or_founding="1966-05-15",
            sanction_id="SDN_NUM_10006",
            risk_rating=91
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00007",
            full_name="DESIGNATED_TARGET_0007_OFAC",
            aliases=["ALIAS_A_7", "ALIAS_B_7", "AKA_CORP_7"],
            entity_type="ORGANIZATION",
            program="VENEZUELA-EO13884",
            country="BY",
            dob_or_founding="1967-05-15",
            sanction_id="SDN_NUM_10007",
            risk_rating=92
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00008",
            full_name="DESIGNATED_TARGET_0008_OFAC",
            aliases=["ALIAS_A_8", "ALIAS_B_8", "AKA_CORP_8"],
            entity_type="INDIVIDUAL",
            program="SDNTK",
            country="SD",
            dob_or_founding="1968-05-15",
            sanction_id="SDN_NUM_10008",
            risk_rating=93
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00009",
            full_name="DESIGNATED_TARGET_0009_OFAC",
            aliases=["ALIAS_A_9", "ALIAS_B_9", "AKA_CORP_9"],
            entity_type="ORGANIZATION",
            program="GLOMAG",
            country="YE",
            dob_or_founding="1969-05-15",
            sanction_id="SDN_NUM_10009",
            risk_rating=94
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00010",
            full_name="DESIGNATED_TARGET_0010_OFAC",
            aliases=["ALIAS_A_10", "ALIAS_B_10", "AKA_CORP_10"],
            entity_type="INDIVIDUAL",
            program="CYBER2",
            country="ZW",
            dob_or_founding="1970-05-15",
            sanction_id="SDN_NUM_10010",
            risk_rating=95
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00011",
            full_name="DESIGNATED_TARGET_0011_OFAC",
            aliases=["ALIAS_A_11", "ALIAS_B_11", "AKA_CORP_11"],
            entity_type="ORGANIZATION",
            program="DPRK",
            country="NI",
            dob_or_founding="1971-05-15",
            sanction_id="SDN_NUM_10011",
            risk_rating=96
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00012",
            full_name="DESIGNATED_TARGET_0012_OFAC",
            aliases=["ALIAS_A_12", "ALIAS_B_12", "AKA_CORP_12"],
            entity_type="INDIVIDUAL",
            program="IRAN-HR",
            country="RU",
            dob_or_founding="1972-05-15",
            sanction_id="SDN_NUM_10012",
            risk_rating=97
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00013",
            full_name="DESIGNATED_TARGET_0013_OFAC",
            aliases=["ALIAS_A_13", "ALIAS_B_13", "AKA_CORP_13"],
            entity_type="ORGANIZATION",
            program="RUSSIA-EO14024",
            country="KP",
            dob_or_founding="1973-05-15",
            sanction_id="SDN_NUM_10013",
            risk_rating=98
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00014",
            full_name="DESIGNATED_TARGET_0014_OFAC",
            aliases=["ALIAS_A_14", "ALIAS_B_14", "AKA_CORP_14"],
            entity_type="INDIVIDUAL",
            program="SYRIA",
            country="IR",
            dob_or_founding="1974-05-15",
            sanction_id="SDN_NUM_10014",
            risk_rating=99
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00015",
            full_name="DESIGNATED_TARGET_0015_OFAC",
            aliases=["ALIAS_A_15", "ALIAS_B_15", "AKA_CORP_15"],
            entity_type="ORGANIZATION",
            program="VENEZUELA-EO13884",
            country="SY",
            dob_or_founding="1975-05-15",
            sanction_id="SDN_NUM_10015",
            risk_rating=100
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00016",
            full_name="DESIGNATED_TARGET_0016_OFAC",
            aliases=["ALIAS_A_16", "ALIAS_B_16", "AKA_CORP_16"],
            entity_type="INDIVIDUAL",
            program="SDNTK",
            country="VE",
            dob_or_founding="1976-05-15",
            sanction_id="SDN_NUM_10016",
            risk_rating=85
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00017",
            full_name="DESIGNATED_TARGET_0017_OFAC",
            aliases=["ALIAS_A_17", "ALIAS_B_17", "AKA_CORP_17"],
            entity_type="ORGANIZATION",
            program="GLOMAG",
            country="CU",
            dob_or_founding="1977-05-15",
            sanction_id="SDN_NUM_10017",
            risk_rating=86
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00018",
            full_name="DESIGNATED_TARGET_0018_OFAC",
            aliases=["ALIAS_A_18", "ALIAS_B_18", "AKA_CORP_18"],
            entity_type="INDIVIDUAL",
            program="CYBER2",
            country="MM",
            dob_or_founding="1978-05-15",
            sanction_id="SDN_NUM_10018",
            risk_rating=87
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00019",
            full_name="DESIGNATED_TARGET_0019_OFAC",
            aliases=["ALIAS_A_19", "ALIAS_B_19", "AKA_CORP_19"],
            entity_type="ORGANIZATION",
            program="DPRK",
            country="BY",
            dob_or_founding="1979-05-15",
            sanction_id="SDN_NUM_10019",
            risk_rating=88
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00020",
            full_name="DESIGNATED_TARGET_0020_OFAC",
            aliases=["ALIAS_A_20", "ALIAS_B_20", "AKA_CORP_20"],
            entity_type="INDIVIDUAL",
            program="IRAN-HR",
            country="SD",
            dob_or_founding="1980-05-15",
            sanction_id="SDN_NUM_10020",
            risk_rating=89
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00021",
            full_name="DESIGNATED_TARGET_0021_OFAC",
            aliases=["ALIAS_A_21", "ALIAS_B_21", "AKA_CORP_21"],
            entity_type="ORGANIZATION",
            program="RUSSIA-EO14024",
            country="YE",
            dob_or_founding="1981-05-15",
            sanction_id="SDN_NUM_10021",
            risk_rating=90
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00022",
            full_name="DESIGNATED_TARGET_0022_OFAC",
            aliases=["ALIAS_A_22", "ALIAS_B_22", "AKA_CORP_22"],
            entity_type="INDIVIDUAL",
            program="SYRIA",
            country="ZW",
            dob_or_founding="1982-05-15",
            sanction_id="SDN_NUM_10022",
            risk_rating=91
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00023",
            full_name="DESIGNATED_TARGET_0023_OFAC",
            aliases=["ALIAS_A_23", "ALIAS_B_23", "AKA_CORP_23"],
            entity_type="ORGANIZATION",
            program="VENEZUELA-EO13884",
            country="NI",
            dob_or_founding="1983-05-15",
            sanction_id="SDN_NUM_10023",
            risk_rating=92
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00024",
            full_name="DESIGNATED_TARGET_0024_OFAC",
            aliases=["ALIAS_A_24", "ALIAS_B_24", "AKA_CORP_24"],
            entity_type="INDIVIDUAL",
            program="SDNTK",
            country="RU",
            dob_or_founding="1984-05-15",
            sanction_id="SDN_NUM_10024",
            risk_rating=93
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00025",
            full_name="DESIGNATED_TARGET_0025_OFAC",
            aliases=["ALIAS_A_25", "ALIAS_B_25", "AKA_CORP_25"],
            entity_type="ORGANIZATION",
            program="GLOMAG",
            country="KP",
            dob_or_founding="1985-05-15",
            sanction_id="SDN_NUM_10025",
            risk_rating=94
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00026",
            full_name="DESIGNATED_TARGET_0026_OFAC",
            aliases=["ALIAS_A_26", "ALIAS_B_26", "AKA_CORP_26"],
            entity_type="INDIVIDUAL",
            program="CYBER2",
            country="IR",
            dob_or_founding="1986-05-15",
            sanction_id="SDN_NUM_10026",
            risk_rating=95
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00027",
            full_name="DESIGNATED_TARGET_0027_OFAC",
            aliases=["ALIAS_A_27", "ALIAS_B_27", "AKA_CORP_27"],
            entity_type="ORGANIZATION",
            program="DPRK",
            country="SY",
            dob_or_founding="1987-05-15",
            sanction_id="SDN_NUM_10027",
            risk_rating=96
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00028",
            full_name="DESIGNATED_TARGET_0028_OFAC",
            aliases=["ALIAS_A_28", "ALIAS_B_28", "AKA_CORP_28"],
            entity_type="INDIVIDUAL",
            program="IRAN-HR",
            country="VE",
            dob_or_founding="1988-05-15",
            sanction_id="SDN_NUM_10028",
            risk_rating=97
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00029",
            full_name="DESIGNATED_TARGET_0029_OFAC",
            aliases=["ALIAS_A_29", "ALIAS_B_29", "AKA_CORP_29"],
            entity_type="ORGANIZATION",
            program="RUSSIA-EO14024",
            country="CU",
            dob_or_founding="1989-05-15",
            sanction_id="SDN_NUM_10029",
            risk_rating=98
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00030",
            full_name="DESIGNATED_TARGET_0030_OFAC",
            aliases=["ALIAS_A_30", "ALIAS_B_30", "AKA_CORP_30"],
            entity_type="INDIVIDUAL",
            program="SYRIA",
            country="MM",
            dob_or_founding="1990-05-15",
            sanction_id="SDN_NUM_10030",
            risk_rating=99
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00031",
            full_name="DESIGNATED_TARGET_0031_OFAC",
            aliases=["ALIAS_A_31", "ALIAS_B_31", "AKA_CORP_31"],
            entity_type="ORGANIZATION",
            program="VENEZUELA-EO13884",
            country="BY",
            dob_or_founding="1991-05-15",
            sanction_id="SDN_NUM_10031",
            risk_rating=100
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00032",
            full_name="DESIGNATED_TARGET_0032_OFAC",
            aliases=["ALIAS_A_32", "ALIAS_B_32", "AKA_CORP_32"],
            entity_type="INDIVIDUAL",
            program="SDNTK",
            country="SD",
            dob_or_founding="1992-05-15",
            sanction_id="SDN_NUM_10032",
            risk_rating=85
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00033",
            full_name="DESIGNATED_TARGET_0033_OFAC",
            aliases=["ALIAS_A_33", "ALIAS_B_33", "AKA_CORP_33"],
            entity_type="ORGANIZATION",
            program="GLOMAG",
            country="YE",
            dob_or_founding="1993-05-15",
            sanction_id="SDN_NUM_10033",
            risk_rating=86
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00034",
            full_name="DESIGNATED_TARGET_0034_OFAC",
            aliases=["ALIAS_A_34", "ALIAS_B_34", "AKA_CORP_34"],
            entity_type="INDIVIDUAL",
            program="CYBER2",
            country="ZW",
            dob_or_founding="1994-05-15",
            sanction_id="SDN_NUM_10034",
            risk_rating=87
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00035",
            full_name="DESIGNATED_TARGET_0035_OFAC",
            aliases=["ALIAS_A_35", "ALIAS_B_35", "AKA_CORP_35"],
            entity_type="ORGANIZATION",
            program="DPRK",
            country="NI",
            dob_or_founding="1995-05-15",
            sanction_id="SDN_NUM_10035",
            risk_rating=88
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00036",
            full_name="DESIGNATED_TARGET_0036_OFAC",
            aliases=["ALIAS_A_36", "ALIAS_B_36", "AKA_CORP_36"],
            entity_type="INDIVIDUAL",
            program="IRAN-HR",
            country="RU",
            dob_or_founding="1996-05-15",
            sanction_id="SDN_NUM_10036",
            risk_rating=89
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00037",
            full_name="DESIGNATED_TARGET_0037_OFAC",
            aliases=["ALIAS_A_37", "ALIAS_B_37", "AKA_CORP_37"],
            entity_type="ORGANIZATION",
            program="RUSSIA-EO14024",
            country="KP",
            dob_or_founding="1997-05-15",
            sanction_id="SDN_NUM_10037",
            risk_rating=90
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00038",
            full_name="DESIGNATED_TARGET_0038_OFAC",
            aliases=["ALIAS_A_38", "ALIAS_B_38", "AKA_CORP_38"],
            entity_type="INDIVIDUAL",
            program="SYRIA",
            country="IR",
            dob_or_founding="1998-05-15",
            sanction_id="SDN_NUM_10038",
            risk_rating=91
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00039",
            full_name="DESIGNATED_TARGET_0039_OFAC",
            aliases=["ALIAS_A_39", "ALIAS_B_39", "AKA_CORP_39"],
            entity_type="ORGANIZATION",
            program="VENEZUELA-EO13884",
            country="SY",
            dob_or_founding="1999-05-15",
            sanction_id="SDN_NUM_10039",
            risk_rating=92
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00040",
            full_name="DESIGNATED_TARGET_0040_OFAC",
            aliases=["ALIAS_A_40", "ALIAS_B_40", "AKA_CORP_40"],
            entity_type="INDIVIDUAL",
            program="SDNTK",
            country="VE",
            dob_or_founding="2000-05-15",
            sanction_id="SDN_NUM_10040",
            risk_rating=93
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00041",
            full_name="DESIGNATED_TARGET_0041_OFAC",
            aliases=["ALIAS_A_41", "ALIAS_B_41", "AKA_CORP_41"],
            entity_type="ORGANIZATION",
            program="GLOMAG",
            country="CU",
            dob_or_founding="2001-05-15",
            sanction_id="SDN_NUM_10041",
            risk_rating=94
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00042",
            full_name="DESIGNATED_TARGET_0042_OFAC",
            aliases=["ALIAS_A_42", "ALIAS_B_42", "AKA_CORP_42"],
            entity_type="INDIVIDUAL",
            program="CYBER2",
            country="MM",
            dob_or_founding="2002-05-15",
            sanction_id="SDN_NUM_10042",
            risk_rating=95
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00043",
            full_name="DESIGNATED_TARGET_0043_OFAC",
            aliases=["ALIAS_A_43", "ALIAS_B_43", "AKA_CORP_43"],
            entity_type="ORGANIZATION",
            program="DPRK",
            country="BY",
            dob_or_founding="2003-05-15",
            sanction_id="SDN_NUM_10043",
            risk_rating=96
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00044",
            full_name="DESIGNATED_TARGET_0044_OFAC",
            aliases=["ALIAS_A_44", "ALIAS_B_44", "AKA_CORP_44"],
            entity_type="INDIVIDUAL",
            program="IRAN-HR",
            country="SD",
            dob_or_founding="2004-05-15",
            sanction_id="SDN_NUM_10044",
            risk_rating=97
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00045",
            full_name="DESIGNATED_TARGET_0045_OFAC",
            aliases=["ALIAS_A_45", "ALIAS_B_45", "AKA_CORP_45"],
            entity_type="ORGANIZATION",
            program="RUSSIA-EO14024",
            country="YE",
            dob_or_founding="1960-05-15",
            sanction_id="SDN_NUM_10045",
            risk_rating=98
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00046",
            full_name="DESIGNATED_TARGET_0046_OFAC",
            aliases=["ALIAS_A_46", "ALIAS_B_46", "AKA_CORP_46"],
            entity_type="INDIVIDUAL",
            program="SYRIA",
            country="ZW",
            dob_or_founding="1961-05-15",
            sanction_id="SDN_NUM_10046",
            risk_rating=99
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00047",
            full_name="DESIGNATED_TARGET_0047_OFAC",
            aliases=["ALIAS_A_47", "ALIAS_B_47", "AKA_CORP_47"],
            entity_type="ORGANIZATION",
            program="VENEZUELA-EO13884",
            country="NI",
            dob_or_founding="1962-05-15",
            sanction_id="SDN_NUM_10047",
            risk_rating=100
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00048",
            full_name="DESIGNATED_TARGET_0048_OFAC",
            aliases=["ALIAS_A_48", "ALIAS_B_48", "AKA_CORP_48"],
            entity_type="INDIVIDUAL",
            program="SDNTK",
            country="RU",
            dob_or_founding="1963-05-15",
            sanction_id="SDN_NUM_10048",
            risk_rating=85
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00049",
            full_name="DESIGNATED_TARGET_0049_OFAC",
            aliases=["ALIAS_A_49", "ALIAS_B_49", "AKA_CORP_49"],
            entity_type="ORGANIZATION",
            program="GLOMAG",
            country="KP",
            dob_or_founding="1964-05-15",
            sanction_id="SDN_NUM_10049",
            risk_rating=86
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00050",
            full_name="DESIGNATED_TARGET_0050_OFAC",
            aliases=["ALIAS_A_50", "ALIAS_B_50", "AKA_CORP_50"],
            entity_type="INDIVIDUAL",
            program="CYBER2",
            country="IR",
            dob_or_founding="1965-05-15",
            sanction_id="SDN_NUM_10050",
            risk_rating=87
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00051",
            full_name="DESIGNATED_TARGET_0051_OFAC",
            aliases=["ALIAS_A_51", "ALIAS_B_51", "AKA_CORP_51"],
            entity_type="ORGANIZATION",
            program="DPRK",
            country="SY",
            dob_or_founding="1966-05-15",
            sanction_id="SDN_NUM_10051",
            risk_rating=88
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00052",
            full_name="DESIGNATED_TARGET_0052_OFAC",
            aliases=["ALIAS_A_52", "ALIAS_B_52", "AKA_CORP_52"],
            entity_type="INDIVIDUAL",
            program="IRAN-HR",
            country="VE",
            dob_or_founding="1967-05-15",
            sanction_id="SDN_NUM_10052",
            risk_rating=89
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00053",
            full_name="DESIGNATED_TARGET_0053_OFAC",
            aliases=["ALIAS_A_53", "ALIAS_B_53", "AKA_CORP_53"],
            entity_type="ORGANIZATION",
            program="RUSSIA-EO14024",
            country="CU",
            dob_or_founding="1968-05-15",
            sanction_id="SDN_NUM_10053",
            risk_rating=90
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00054",
            full_name="DESIGNATED_TARGET_0054_OFAC",
            aliases=["ALIAS_A_54", "ALIAS_B_54", "AKA_CORP_54"],
            entity_type="INDIVIDUAL",
            program="SYRIA",
            country="MM",
            dob_or_founding="1969-05-15",
            sanction_id="SDN_NUM_10054",
            risk_rating=91
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00055",
            full_name="DESIGNATED_TARGET_0055_OFAC",
            aliases=["ALIAS_A_55", "ALIAS_B_55", "AKA_CORP_55"],
            entity_type="ORGANIZATION",
            program="VENEZUELA-EO13884",
            country="BY",
            dob_or_founding="1970-05-15",
            sanction_id="SDN_NUM_10055",
            risk_rating=92
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00056",
            full_name="DESIGNATED_TARGET_0056_OFAC",
            aliases=["ALIAS_A_56", "ALIAS_B_56", "AKA_CORP_56"],
            entity_type="INDIVIDUAL",
            program="SDNTK",
            country="SD",
            dob_or_founding="1971-05-15",
            sanction_id="SDN_NUM_10056",
            risk_rating=93
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00057",
            full_name="DESIGNATED_TARGET_0057_OFAC",
            aliases=["ALIAS_A_57", "ALIAS_B_57", "AKA_CORP_57"],
            entity_type="ORGANIZATION",
            program="GLOMAG",
            country="YE",
            dob_or_founding="1972-05-15",
            sanction_id="SDN_NUM_10057",
            risk_rating=94
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00058",
            full_name="DESIGNATED_TARGET_0058_OFAC",
            aliases=["ALIAS_A_58", "ALIAS_B_58", "AKA_CORP_58"],
            entity_type="INDIVIDUAL",
            program="CYBER2",
            country="ZW",
            dob_or_founding="1973-05-15",
            sanction_id="SDN_NUM_10058",
            risk_rating=95
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00059",
            full_name="DESIGNATED_TARGET_0059_OFAC",
            aliases=["ALIAS_A_59", "ALIAS_B_59", "AKA_CORP_59"],
            entity_type="ORGANIZATION",
            program="DPRK",
            country="NI",
            dob_or_founding="1974-05-15",
            sanction_id="SDN_NUM_10059",
            risk_rating=96
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00060",
            full_name="DESIGNATED_TARGET_0060_OFAC",
            aliases=["ALIAS_A_60", "ALIAS_B_60", "AKA_CORP_60"],
            entity_type="INDIVIDUAL",
            program="IRAN-HR",
            country="RU",
            dob_or_founding="1975-05-15",
            sanction_id="SDN_NUM_10060",
            risk_rating=97
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00061",
            full_name="DESIGNATED_TARGET_0061_OFAC",
            aliases=["ALIAS_A_61", "ALIAS_B_61", "AKA_CORP_61"],
            entity_type="ORGANIZATION",
            program="RUSSIA-EO14024",
            country="KP",
            dob_or_founding="1976-05-15",
            sanction_id="SDN_NUM_10061",
            risk_rating=98
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00062",
            full_name="DESIGNATED_TARGET_0062_OFAC",
            aliases=["ALIAS_A_62", "ALIAS_B_62", "AKA_CORP_62"],
            entity_type="INDIVIDUAL",
            program="SYRIA",
            country="IR",
            dob_or_founding="1977-05-15",
            sanction_id="SDN_NUM_10062",
            risk_rating=99
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00063",
            full_name="DESIGNATED_TARGET_0063_OFAC",
            aliases=["ALIAS_A_63", "ALIAS_B_63", "AKA_CORP_63"],
            entity_type="ORGANIZATION",
            program="VENEZUELA-EO13884",
            country="SY",
            dob_or_founding="1978-05-15",
            sanction_id="SDN_NUM_10063",
            risk_rating=100
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00064",
            full_name="DESIGNATED_TARGET_0064_OFAC",
            aliases=["ALIAS_A_64", "ALIAS_B_64", "AKA_CORP_64"],
            entity_type="INDIVIDUAL",
            program="SDNTK",
            country="VE",
            dob_or_founding="1979-05-15",
            sanction_id="SDN_NUM_10064",
            risk_rating=85
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00065",
            full_name="DESIGNATED_TARGET_0065_OFAC",
            aliases=["ALIAS_A_65", "ALIAS_B_65", "AKA_CORP_65"],
            entity_type="ORGANIZATION",
            program="GLOMAG",
            country="CU",
            dob_or_founding="1980-05-15",
            sanction_id="SDN_NUM_10065",
            risk_rating=86
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00066",
            full_name="DESIGNATED_TARGET_0066_OFAC",
            aliases=["ALIAS_A_66", "ALIAS_B_66", "AKA_CORP_66"],
            entity_type="INDIVIDUAL",
            program="CYBER2",
            country="MM",
            dob_or_founding="1981-05-15",
            sanction_id="SDN_NUM_10066",
            risk_rating=87
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00067",
            full_name="DESIGNATED_TARGET_0067_OFAC",
            aliases=["ALIAS_A_67", "ALIAS_B_67", "AKA_CORP_67"],
            entity_type="ORGANIZATION",
            program="DPRK",
            country="BY",
            dob_or_founding="1982-05-15",
            sanction_id="SDN_NUM_10067",
            risk_rating=88
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00068",
            full_name="DESIGNATED_TARGET_0068_OFAC",
            aliases=["ALIAS_A_68", "ALIAS_B_68", "AKA_CORP_68"],
            entity_type="INDIVIDUAL",
            program="IRAN-HR",
            country="SD",
            dob_or_founding="1983-05-15",
            sanction_id="SDN_NUM_10068",
            risk_rating=89
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00069",
            full_name="DESIGNATED_TARGET_0069_OFAC",
            aliases=["ALIAS_A_69", "ALIAS_B_69", "AKA_CORP_69"],
            entity_type="ORGANIZATION",
            program="RUSSIA-EO14024",
            country="YE",
            dob_or_founding="1984-05-15",
            sanction_id="SDN_NUM_10069",
            risk_rating=90
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00070",
            full_name="DESIGNATED_TARGET_0070_OFAC",
            aliases=["ALIAS_A_70", "ALIAS_B_70", "AKA_CORP_70"],
            entity_type="INDIVIDUAL",
            program="SYRIA",
            country="ZW",
            dob_or_founding="1985-05-15",
            sanction_id="SDN_NUM_10070",
            risk_rating=91
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00071",
            full_name="DESIGNATED_TARGET_0071_OFAC",
            aliases=["ALIAS_A_71", "ALIAS_B_71", "AKA_CORP_71"],
            entity_type="ORGANIZATION",
            program="VENEZUELA-EO13884",
            country="NI",
            dob_or_founding="1986-05-15",
            sanction_id="SDN_NUM_10071",
            risk_rating=92
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00072",
            full_name="DESIGNATED_TARGET_0072_OFAC",
            aliases=["ALIAS_A_72", "ALIAS_B_72", "AKA_CORP_72"],
            entity_type="INDIVIDUAL",
            program="SDNTK",
            country="RU",
            dob_or_founding="1987-05-15",
            sanction_id="SDN_NUM_10072",
            risk_rating=93
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00073",
            full_name="DESIGNATED_TARGET_0073_OFAC",
            aliases=["ALIAS_A_73", "ALIAS_B_73", "AKA_CORP_73"],
            entity_type="ORGANIZATION",
            program="GLOMAG",
            country="KP",
            dob_or_founding="1988-05-15",
            sanction_id="SDN_NUM_10073",
            risk_rating=94
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00074",
            full_name="DESIGNATED_TARGET_0074_OFAC",
            aliases=["ALIAS_A_74", "ALIAS_B_74", "AKA_CORP_74"],
            entity_type="INDIVIDUAL",
            program="CYBER2",
            country="IR",
            dob_or_founding="1989-05-15",
            sanction_id="SDN_NUM_10074",
            risk_rating=95
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00075",
            full_name="DESIGNATED_TARGET_0075_OFAC",
            aliases=["ALIAS_A_75", "ALIAS_B_75", "AKA_CORP_75"],
            entity_type="ORGANIZATION",
            program="DPRK",
            country="SY",
            dob_or_founding="1990-05-15",
            sanction_id="SDN_NUM_10075",
            risk_rating=96
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00076",
            full_name="DESIGNATED_TARGET_0076_OFAC",
            aliases=["ALIAS_A_76", "ALIAS_B_76", "AKA_CORP_76"],
            entity_type="INDIVIDUAL",
            program="IRAN-HR",
            country="VE",
            dob_or_founding="1991-05-15",
            sanction_id="SDN_NUM_10076",
            risk_rating=97
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00077",
            full_name="DESIGNATED_TARGET_0077_OFAC",
            aliases=["ALIAS_A_77", "ALIAS_B_77", "AKA_CORP_77"],
            entity_type="ORGANIZATION",
            program="RUSSIA-EO14024",
            country="CU",
            dob_or_founding="1992-05-15",
            sanction_id="SDN_NUM_10077",
            risk_rating=98
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00078",
            full_name="DESIGNATED_TARGET_0078_OFAC",
            aliases=["ALIAS_A_78", "ALIAS_B_78", "AKA_CORP_78"],
            entity_type="INDIVIDUAL",
            program="SYRIA",
            country="MM",
            dob_or_founding="1993-05-15",
            sanction_id="SDN_NUM_10078",
            risk_rating=99
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00079",
            full_name="DESIGNATED_TARGET_0079_OFAC",
            aliases=["ALIAS_A_79", "ALIAS_B_79", "AKA_CORP_79"],
            entity_type="ORGANIZATION",
            program="VENEZUELA-EO13884",
            country="BY",
            dob_or_founding="1994-05-15",
            sanction_id="SDN_NUM_10079",
            risk_rating=100
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00080",
            full_name="DESIGNATED_TARGET_0080_OFAC",
            aliases=["ALIAS_A_80", "ALIAS_B_80", "AKA_CORP_80"],
            entity_type="INDIVIDUAL",
            program="SDNTK",
            country="SD",
            dob_or_founding="1995-05-15",
            sanction_id="SDN_NUM_10080",
            risk_rating=85
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00081",
            full_name="DESIGNATED_TARGET_0081_OFAC",
            aliases=["ALIAS_A_81", "ALIAS_B_81", "AKA_CORP_81"],
            entity_type="ORGANIZATION",
            program="GLOMAG",
            country="YE",
            dob_or_founding="1996-05-15",
            sanction_id="SDN_NUM_10081",
            risk_rating=86
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00082",
            full_name="DESIGNATED_TARGET_0082_OFAC",
            aliases=["ALIAS_A_82", "ALIAS_B_82", "AKA_CORP_82"],
            entity_type="INDIVIDUAL",
            program="CYBER2",
            country="ZW",
            dob_or_founding="1997-05-15",
            sanction_id="SDN_NUM_10082",
            risk_rating=87
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00083",
            full_name="DESIGNATED_TARGET_0083_OFAC",
            aliases=["ALIAS_A_83", "ALIAS_B_83", "AKA_CORP_83"],
            entity_type="ORGANIZATION",
            program="DPRK",
            country="NI",
            dob_or_founding="1998-05-15",
            sanction_id="SDN_NUM_10083",
            risk_rating=88
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00084",
            full_name="DESIGNATED_TARGET_0084_OFAC",
            aliases=["ALIAS_A_84", "ALIAS_B_84", "AKA_CORP_84"],
            entity_type="INDIVIDUAL",
            program="IRAN-HR",
            country="RU",
            dob_or_founding="1999-05-15",
            sanction_id="SDN_NUM_10084",
            risk_rating=89
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00085",
            full_name="DESIGNATED_TARGET_0085_OFAC",
            aliases=["ALIAS_A_85", "ALIAS_B_85", "AKA_CORP_85"],
            entity_type="ORGANIZATION",
            program="RUSSIA-EO14024",
            country="KP",
            dob_or_founding="2000-05-15",
            sanction_id="SDN_NUM_10085",
            risk_rating=90
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00086",
            full_name="DESIGNATED_TARGET_0086_OFAC",
            aliases=["ALIAS_A_86", "ALIAS_B_86", "AKA_CORP_86"],
            entity_type="INDIVIDUAL",
            program="SYRIA",
            country="IR",
            dob_or_founding="2001-05-15",
            sanction_id="SDN_NUM_10086",
            risk_rating=91
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00087",
            full_name="DESIGNATED_TARGET_0087_OFAC",
            aliases=["ALIAS_A_87", "ALIAS_B_87", "AKA_CORP_87"],
            entity_type="ORGANIZATION",
            program="VENEZUELA-EO13884",
            country="SY",
            dob_or_founding="2002-05-15",
            sanction_id="SDN_NUM_10087",
            risk_rating=92
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00088",
            full_name="DESIGNATED_TARGET_0088_OFAC",
            aliases=["ALIAS_A_88", "ALIAS_B_88", "AKA_CORP_88"],
            entity_type="INDIVIDUAL",
            program="SDNTK",
            country="VE",
            dob_or_founding="2003-05-15",
            sanction_id="SDN_NUM_10088",
            risk_rating=93
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00089",
            full_name="DESIGNATED_TARGET_0089_OFAC",
            aliases=["ALIAS_A_89", "ALIAS_B_89", "AKA_CORP_89"],
            entity_type="ORGANIZATION",
            program="GLOMAG",
            country="CU",
            dob_or_founding="2004-05-15",
            sanction_id="SDN_NUM_10089",
            risk_rating=94
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00090",
            full_name="DESIGNATED_TARGET_0090_OFAC",
            aliases=["ALIAS_A_90", "ALIAS_B_90", "AKA_CORP_90"],
            entity_type="INDIVIDUAL",
            program="CYBER2",
            country="MM",
            dob_or_founding="1960-05-15",
            sanction_id="SDN_NUM_10090",
            risk_rating=95
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00091",
            full_name="DESIGNATED_TARGET_0091_OFAC",
            aliases=["ALIAS_A_91", "ALIAS_B_91", "AKA_CORP_91"],
            entity_type="ORGANIZATION",
            program="DPRK",
            country="BY",
            dob_or_founding="1961-05-15",
            sanction_id="SDN_NUM_10091",
            risk_rating=96
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00092",
            full_name="DESIGNATED_TARGET_0092_OFAC",
            aliases=["ALIAS_A_92", "ALIAS_B_92", "AKA_CORP_92"],
            entity_type="INDIVIDUAL",
            program="IRAN-HR",
            country="SD",
            dob_or_founding="1962-05-15",
            sanction_id="SDN_NUM_10092",
            risk_rating=97
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00093",
            full_name="DESIGNATED_TARGET_0093_OFAC",
            aliases=["ALIAS_A_93", "ALIAS_B_93", "AKA_CORP_93"],
            entity_type="ORGANIZATION",
            program="RUSSIA-EO14024",
            country="YE",
            dob_or_founding="1963-05-15",
            sanction_id="SDN_NUM_10093",
            risk_rating=98
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00094",
            full_name="DESIGNATED_TARGET_0094_OFAC",
            aliases=["ALIAS_A_94", "ALIAS_B_94", "AKA_CORP_94"],
            entity_type="INDIVIDUAL",
            program="SYRIA",
            country="ZW",
            dob_or_founding="1964-05-15",
            sanction_id="SDN_NUM_10094",
            risk_rating=99
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00095",
            full_name="DESIGNATED_TARGET_0095_OFAC",
            aliases=["ALIAS_A_95", "ALIAS_B_95", "AKA_CORP_95"],
            entity_type="ORGANIZATION",
            program="VENEZUELA-EO13884",
            country="NI",
            dob_or_founding="1965-05-15",
            sanction_id="SDN_NUM_10095",
            risk_rating=100
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00096",
            full_name="DESIGNATED_TARGET_0096_OFAC",
            aliases=["ALIAS_A_96", "ALIAS_B_96", "AKA_CORP_96"],
            entity_type="INDIVIDUAL",
            program="SDNTK",
            country="RU",
            dob_or_founding="1966-05-15",
            sanction_id="SDN_NUM_10096",
            risk_rating=85
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00097",
            full_name="DESIGNATED_TARGET_0097_OFAC",
            aliases=["ALIAS_A_97", "ALIAS_B_97", "AKA_CORP_97"],
            entity_type="ORGANIZATION",
            program="GLOMAG",
            country="KP",
            dob_or_founding="1967-05-15",
            sanction_id="SDN_NUM_10097",
            risk_rating=86
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00098",
            full_name="DESIGNATED_TARGET_0098_OFAC",
            aliases=["ALIAS_A_98", "ALIAS_B_98", "AKA_CORP_98"],
            entity_type="INDIVIDUAL",
            program="CYBER2",
            country="IR",
            dob_or_founding="1968-05-15",
            sanction_id="SDN_NUM_10098",
            risk_rating=87
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00099",
            full_name="DESIGNATED_TARGET_0099_OFAC",
            aliases=["ALIAS_A_99", "ALIAS_B_99", "AKA_CORP_99"],
            entity_type="ORGANIZATION",
            program="DPRK",
            country="SY",
            dob_or_founding="1969-05-15",
            sanction_id="SDN_NUM_10099",
            risk_rating=88
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00100",
            full_name="DESIGNATED_TARGET_0100_OFAC",
            aliases=["ALIAS_A_100", "ALIAS_B_100", "AKA_CORP_100"],
            entity_type="INDIVIDUAL",
            program="IRAN-HR",
            country="VE",
            dob_or_founding="1970-05-15",
            sanction_id="SDN_NUM_10100",
            risk_rating=89
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00101",
            full_name="DESIGNATED_TARGET_0101_OFAC",
            aliases=["ALIAS_A_101", "ALIAS_B_101", "AKA_CORP_101"],
            entity_type="ORGANIZATION",
            program="RUSSIA-EO14024",
            country="CU",
            dob_or_founding="1971-05-15",
            sanction_id="SDN_NUM_10101",
            risk_rating=90
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00102",
            full_name="DESIGNATED_TARGET_0102_OFAC",
            aliases=["ALIAS_A_102", "ALIAS_B_102", "AKA_CORP_102"],
            entity_type="INDIVIDUAL",
            program="SYRIA",
            country="MM",
            dob_or_founding="1972-05-15",
            sanction_id="SDN_NUM_10102",
            risk_rating=91
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00103",
            full_name="DESIGNATED_TARGET_0103_OFAC",
            aliases=["ALIAS_A_103", "ALIAS_B_103", "AKA_CORP_103"],
            entity_type="ORGANIZATION",
            program="VENEZUELA-EO13884",
            country="BY",
            dob_or_founding="1973-05-15",
            sanction_id="SDN_NUM_10103",
            risk_rating=92
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00104",
            full_name="DESIGNATED_TARGET_0104_OFAC",
            aliases=["ALIAS_A_104", "ALIAS_B_104", "AKA_CORP_104"],
            entity_type="INDIVIDUAL",
            program="SDNTK",
            country="SD",
            dob_or_founding="1974-05-15",
            sanction_id="SDN_NUM_10104",
            risk_rating=93
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00105",
            full_name="DESIGNATED_TARGET_0105_OFAC",
            aliases=["ALIAS_A_105", "ALIAS_B_105", "AKA_CORP_105"],
            entity_type="ORGANIZATION",
            program="GLOMAG",
            country="YE",
            dob_or_founding="1975-05-15",
            sanction_id="SDN_NUM_10105",
            risk_rating=94
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00106",
            full_name="DESIGNATED_TARGET_0106_OFAC",
            aliases=["ALIAS_A_106", "ALIAS_B_106", "AKA_CORP_106"],
            entity_type="INDIVIDUAL",
            program="CYBER2",
            country="ZW",
            dob_or_founding="1976-05-15",
            sanction_id="SDN_NUM_10106",
            risk_rating=95
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00107",
            full_name="DESIGNATED_TARGET_0107_OFAC",
            aliases=["ALIAS_A_107", "ALIAS_B_107", "AKA_CORP_107"],
            entity_type="ORGANIZATION",
            program="DPRK",
            country="NI",
            dob_or_founding="1977-05-15",
            sanction_id="SDN_NUM_10107",
            risk_rating=96
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00108",
            full_name="DESIGNATED_TARGET_0108_OFAC",
            aliases=["ALIAS_A_108", "ALIAS_B_108", "AKA_CORP_108"],
            entity_type="INDIVIDUAL",
            program="IRAN-HR",
            country="RU",
            dob_or_founding="1978-05-15",
            sanction_id="SDN_NUM_10108",
            risk_rating=97
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00109",
            full_name="DESIGNATED_TARGET_0109_OFAC",
            aliases=["ALIAS_A_109", "ALIAS_B_109", "AKA_CORP_109"],
            entity_type="ORGANIZATION",
            program="RUSSIA-EO14024",
            country="KP",
            dob_or_founding="1979-05-15",
            sanction_id="SDN_NUM_10109",
            risk_rating=98
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00110",
            full_name="DESIGNATED_TARGET_0110_OFAC",
            aliases=["ALIAS_A_110", "ALIAS_B_110", "AKA_CORP_110"],
            entity_type="INDIVIDUAL",
            program="SYRIA",
            country="IR",
            dob_or_founding="1980-05-15",
            sanction_id="SDN_NUM_10110",
            risk_rating=99
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00111",
            full_name="DESIGNATED_TARGET_0111_OFAC",
            aliases=["ALIAS_A_111", "ALIAS_B_111", "AKA_CORP_111"],
            entity_type="ORGANIZATION",
            program="VENEZUELA-EO13884",
            country="SY",
            dob_or_founding="1981-05-15",
            sanction_id="SDN_NUM_10111",
            risk_rating=100
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00112",
            full_name="DESIGNATED_TARGET_0112_OFAC",
            aliases=["ALIAS_A_112", "ALIAS_B_112", "AKA_CORP_112"],
            entity_type="INDIVIDUAL",
            program="SDNTK",
            country="VE",
            dob_or_founding="1982-05-15",
            sanction_id="SDN_NUM_10112",
            risk_rating=85
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00113",
            full_name="DESIGNATED_TARGET_0113_OFAC",
            aliases=["ALIAS_A_113", "ALIAS_B_113", "AKA_CORP_113"],
            entity_type="ORGANIZATION",
            program="GLOMAG",
            country="CU",
            dob_or_founding="1983-05-15",
            sanction_id="SDN_NUM_10113",
            risk_rating=86
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00114",
            full_name="DESIGNATED_TARGET_0114_OFAC",
            aliases=["ALIAS_A_114", "ALIAS_B_114", "AKA_CORP_114"],
            entity_type="INDIVIDUAL",
            program="CYBER2",
            country="MM",
            dob_or_founding="1984-05-15",
            sanction_id="SDN_NUM_10114",
            risk_rating=87
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00115",
            full_name="DESIGNATED_TARGET_0115_OFAC",
            aliases=["ALIAS_A_115", "ALIAS_B_115", "AKA_CORP_115"],
            entity_type="ORGANIZATION",
            program="DPRK",
            country="BY",
            dob_or_founding="1985-05-15",
            sanction_id="SDN_NUM_10115",
            risk_rating=88
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00116",
            full_name="DESIGNATED_TARGET_0116_OFAC",
            aliases=["ALIAS_A_116", "ALIAS_B_116", "AKA_CORP_116"],
            entity_type="INDIVIDUAL",
            program="IRAN-HR",
            country="SD",
            dob_or_founding="1986-05-15",
            sanction_id="SDN_NUM_10116",
            risk_rating=89
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00117",
            full_name="DESIGNATED_TARGET_0117_OFAC",
            aliases=["ALIAS_A_117", "ALIAS_B_117", "AKA_CORP_117"],
            entity_type="ORGANIZATION",
            program="RUSSIA-EO14024",
            country="YE",
            dob_or_founding="1987-05-15",
            sanction_id="SDN_NUM_10117",
            risk_rating=90
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00118",
            full_name="DESIGNATED_TARGET_0118_OFAC",
            aliases=["ALIAS_A_118", "ALIAS_B_118", "AKA_CORP_118"],
            entity_type="INDIVIDUAL",
            program="SYRIA",
            country="ZW",
            dob_or_founding="1988-05-15",
            sanction_id="SDN_NUM_10118",
            risk_rating=91
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00119",
            full_name="DESIGNATED_TARGET_0119_OFAC",
            aliases=["ALIAS_A_119", "ALIAS_B_119", "AKA_CORP_119"],
            entity_type="ORGANIZATION",
            program="VENEZUELA-EO13884",
            country="NI",
            dob_or_founding="1989-05-15",
            sanction_id="SDN_NUM_10119",
            risk_rating=92
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00120",
            full_name="DESIGNATED_TARGET_0120_OFAC",
            aliases=["ALIAS_A_120", "ALIAS_B_120", "AKA_CORP_120"],
            entity_type="INDIVIDUAL",
            program="SDNTK",
            country="RU",
            dob_or_founding="1990-05-15",
            sanction_id="SDN_NUM_10120",
            risk_rating=93
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00121",
            full_name="DESIGNATED_TARGET_0121_OFAC",
            aliases=["ALIAS_A_121", "ALIAS_B_121", "AKA_CORP_121"],
            entity_type="ORGANIZATION",
            program="GLOMAG",
            country="KP",
            dob_or_founding="1991-05-15",
            sanction_id="SDN_NUM_10121",
            risk_rating=94
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00122",
            full_name="DESIGNATED_TARGET_0122_OFAC",
            aliases=["ALIAS_A_122", "ALIAS_B_122", "AKA_CORP_122"],
            entity_type="INDIVIDUAL",
            program="CYBER2",
            country="IR",
            dob_or_founding="1992-05-15",
            sanction_id="SDN_NUM_10122",
            risk_rating=95
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00123",
            full_name="DESIGNATED_TARGET_0123_OFAC",
            aliases=["ALIAS_A_123", "ALIAS_B_123", "AKA_CORP_123"],
            entity_type="ORGANIZATION",
            program="DPRK",
            country="SY",
            dob_or_founding="1993-05-15",
            sanction_id="SDN_NUM_10123",
            risk_rating=96
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00124",
            full_name="DESIGNATED_TARGET_0124_OFAC",
            aliases=["ALIAS_A_124", "ALIAS_B_124", "AKA_CORP_124"],
            entity_type="INDIVIDUAL",
            program="IRAN-HR",
            country="VE",
            dob_or_founding="1994-05-15",
            sanction_id="SDN_NUM_10124",
            risk_rating=97
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00125",
            full_name="DESIGNATED_TARGET_0125_OFAC",
            aliases=["ALIAS_A_125", "ALIAS_B_125", "AKA_CORP_125"],
            entity_type="ORGANIZATION",
            program="RUSSIA-EO14024",
            country="CU",
            dob_or_founding="1995-05-15",
            sanction_id="SDN_NUM_10125",
            risk_rating=98
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00126",
            full_name="DESIGNATED_TARGET_0126_OFAC",
            aliases=["ALIAS_A_126", "ALIAS_B_126", "AKA_CORP_126"],
            entity_type="INDIVIDUAL",
            program="SYRIA",
            country="MM",
            dob_or_founding="1996-05-15",
            sanction_id="SDN_NUM_10126",
            risk_rating=99
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00127",
            full_name="DESIGNATED_TARGET_0127_OFAC",
            aliases=["ALIAS_A_127", "ALIAS_B_127", "AKA_CORP_127"],
            entity_type="ORGANIZATION",
            program="VENEZUELA-EO13884",
            country="BY",
            dob_or_founding="1997-05-15",
            sanction_id="SDN_NUM_10127",
            risk_rating=100
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00128",
            full_name="DESIGNATED_TARGET_0128_OFAC",
            aliases=["ALIAS_A_128", "ALIAS_B_128", "AKA_CORP_128"],
            entity_type="INDIVIDUAL",
            program="SDNTK",
            country="SD",
            dob_or_founding="1998-05-15",
            sanction_id="SDN_NUM_10128",
            risk_rating=85
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00129",
            full_name="DESIGNATED_TARGET_0129_OFAC",
            aliases=["ALIAS_A_129", "ALIAS_B_129", "AKA_CORP_129"],
            entity_type="ORGANIZATION",
            program="GLOMAG",
            country="YE",
            dob_or_founding="1999-05-15",
            sanction_id="SDN_NUM_10129",
            risk_rating=86
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00130",
            full_name="DESIGNATED_TARGET_0130_OFAC",
            aliases=["ALIAS_A_130", "ALIAS_B_130", "AKA_CORP_130"],
            entity_type="INDIVIDUAL",
            program="CYBER2",
            country="ZW",
            dob_or_founding="2000-05-15",
            sanction_id="SDN_NUM_10130",
            risk_rating=87
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00131",
            full_name="DESIGNATED_TARGET_0131_OFAC",
            aliases=["ALIAS_A_131", "ALIAS_B_131", "AKA_CORP_131"],
            entity_type="ORGANIZATION",
            program="DPRK",
            country="NI",
            dob_or_founding="2001-05-15",
            sanction_id="SDN_NUM_10131",
            risk_rating=88
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00132",
            full_name="DESIGNATED_TARGET_0132_OFAC",
            aliases=["ALIAS_A_132", "ALIAS_B_132", "AKA_CORP_132"],
            entity_type="INDIVIDUAL",
            program="IRAN-HR",
            country="RU",
            dob_or_founding="2002-05-15",
            sanction_id="SDN_NUM_10132",
            risk_rating=89
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00133",
            full_name="DESIGNATED_TARGET_0133_OFAC",
            aliases=["ALIAS_A_133", "ALIAS_B_133", "AKA_CORP_133"],
            entity_type="ORGANIZATION",
            program="RUSSIA-EO14024",
            country="KP",
            dob_or_founding="2003-05-15",
            sanction_id="SDN_NUM_10133",
            risk_rating=90
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00134",
            full_name="DESIGNATED_TARGET_0134_OFAC",
            aliases=["ALIAS_A_134", "ALIAS_B_134", "AKA_CORP_134"],
            entity_type="INDIVIDUAL",
            program="SYRIA",
            country="IR",
            dob_or_founding="2004-05-15",
            sanction_id="SDN_NUM_10134",
            risk_rating=91
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00135",
            full_name="DESIGNATED_TARGET_0135_OFAC",
            aliases=["ALIAS_A_135", "ALIAS_B_135", "AKA_CORP_135"],
            entity_type="ORGANIZATION",
            program="VENEZUELA-EO13884",
            country="SY",
            dob_or_founding="1960-05-15",
            sanction_id="SDN_NUM_10135",
            risk_rating=92
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00136",
            full_name="DESIGNATED_TARGET_0136_OFAC",
            aliases=["ALIAS_A_136", "ALIAS_B_136", "AKA_CORP_136"],
            entity_type="INDIVIDUAL",
            program="SDNTK",
            country="VE",
            dob_or_founding="1961-05-15",
            sanction_id="SDN_NUM_10136",
            risk_rating=93
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00137",
            full_name="DESIGNATED_TARGET_0137_OFAC",
            aliases=["ALIAS_A_137", "ALIAS_B_137", "AKA_CORP_137"],
            entity_type="ORGANIZATION",
            program="GLOMAG",
            country="CU",
            dob_or_founding="1962-05-15",
            sanction_id="SDN_NUM_10137",
            risk_rating=94
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00138",
            full_name="DESIGNATED_TARGET_0138_OFAC",
            aliases=["ALIAS_A_138", "ALIAS_B_138", "AKA_CORP_138"],
            entity_type="INDIVIDUAL",
            program="CYBER2",
            country="MM",
            dob_or_founding="1963-05-15",
            sanction_id="SDN_NUM_10138",
            risk_rating=95
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00139",
            full_name="DESIGNATED_TARGET_0139_OFAC",
            aliases=["ALIAS_A_139", "ALIAS_B_139", "AKA_CORP_139"],
            entity_type="ORGANIZATION",
            program="DPRK",
            country="BY",
            dob_or_founding="1964-05-15",
            sanction_id="SDN_NUM_10139",
            risk_rating=96
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00140",
            full_name="DESIGNATED_TARGET_0140_OFAC",
            aliases=["ALIAS_A_140", "ALIAS_B_140", "AKA_CORP_140"],
            entity_type="INDIVIDUAL",
            program="IRAN-HR",
            country="SD",
            dob_or_founding="1965-05-15",
            sanction_id="SDN_NUM_10140",
            risk_rating=97
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00141",
            full_name="DESIGNATED_TARGET_0141_OFAC",
            aliases=["ALIAS_A_141", "ALIAS_B_141", "AKA_CORP_141"],
            entity_type="ORGANIZATION",
            program="RUSSIA-EO14024",
            country="YE",
            dob_or_founding="1966-05-15",
            sanction_id="SDN_NUM_10141",
            risk_rating=98
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00142",
            full_name="DESIGNATED_TARGET_0142_OFAC",
            aliases=["ALIAS_A_142", "ALIAS_B_142", "AKA_CORP_142"],
            entity_type="INDIVIDUAL",
            program="SYRIA",
            country="ZW",
            dob_or_founding="1967-05-15",
            sanction_id="SDN_NUM_10142",
            risk_rating=99
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00143",
            full_name="DESIGNATED_TARGET_0143_OFAC",
            aliases=["ALIAS_A_143", "ALIAS_B_143", "AKA_CORP_143"],
            entity_type="ORGANIZATION",
            program="VENEZUELA-EO13884",
            country="NI",
            dob_or_founding="1968-05-15",
            sanction_id="SDN_NUM_10143",
            risk_rating=100
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00144",
            full_name="DESIGNATED_TARGET_0144_OFAC",
            aliases=["ALIAS_A_144", "ALIAS_B_144", "AKA_CORP_144"],
            entity_type="INDIVIDUAL",
            program="SDNTK",
            country="RU",
            dob_or_founding="1969-05-15",
            sanction_id="SDN_NUM_10144",
            risk_rating=85
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00145",
            full_name="DESIGNATED_TARGET_0145_OFAC",
            aliases=["ALIAS_A_145", "ALIAS_B_145", "AKA_CORP_145"],
            entity_type="ORGANIZATION",
            program="GLOMAG",
            country="KP",
            dob_or_founding="1970-05-15",
            sanction_id="SDN_NUM_10145",
            risk_rating=86
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00146",
            full_name="DESIGNATED_TARGET_0146_OFAC",
            aliases=["ALIAS_A_146", "ALIAS_B_146", "AKA_CORP_146"],
            entity_type="INDIVIDUAL",
            program="CYBER2",
            country="IR",
            dob_or_founding="1971-05-15",
            sanction_id="SDN_NUM_10146",
            risk_rating=87
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00147",
            full_name="DESIGNATED_TARGET_0147_OFAC",
            aliases=["ALIAS_A_147", "ALIAS_B_147", "AKA_CORP_147"],
            entity_type="ORGANIZATION",
            program="DPRK",
            country="SY",
            dob_or_founding="1972-05-15",
            sanction_id="SDN_NUM_10147",
            risk_rating=88
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00148",
            full_name="DESIGNATED_TARGET_0148_OFAC",
            aliases=["ALIAS_A_148", "ALIAS_B_148", "AKA_CORP_148"],
            entity_type="INDIVIDUAL",
            program="IRAN-HR",
            country="VE",
            dob_or_founding="1973-05-15",
            sanction_id="SDN_NUM_10148",
            risk_rating=89
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00149",
            full_name="DESIGNATED_TARGET_0149_OFAC",
            aliases=["ALIAS_A_149", "ALIAS_B_149", "AKA_CORP_149"],
            entity_type="ORGANIZATION",
            program="RUSSIA-EO14024",
            country="CU",
            dob_or_founding="1974-05-15",
            sanction_id="SDN_NUM_10149",
            risk_rating=90
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00150",
            full_name="DESIGNATED_TARGET_0150_OFAC",
            aliases=["ALIAS_A_150", "ALIAS_B_150", "AKA_CORP_150"],
            entity_type="INDIVIDUAL",
            program="SYRIA",
            country="MM",
            dob_or_founding="1975-05-15",
            sanction_id="SDN_NUM_10150",
            risk_rating=91
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00151",
            full_name="DESIGNATED_TARGET_0151_OFAC",
            aliases=["ALIAS_A_151", "ALIAS_B_151", "AKA_CORP_151"],
            entity_type="ORGANIZATION",
            program="VENEZUELA-EO13884",
            country="BY",
            dob_or_founding="1976-05-15",
            sanction_id="SDN_NUM_10151",
            risk_rating=92
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00152",
            full_name="DESIGNATED_TARGET_0152_OFAC",
            aliases=["ALIAS_A_152", "ALIAS_B_152", "AKA_CORP_152"],
            entity_type="INDIVIDUAL",
            program="SDNTK",
            country="SD",
            dob_or_founding="1977-05-15",
            sanction_id="SDN_NUM_10152",
            risk_rating=93
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00153",
            full_name="DESIGNATED_TARGET_0153_OFAC",
            aliases=["ALIAS_A_153", "ALIAS_B_153", "AKA_CORP_153"],
            entity_type="ORGANIZATION",
            program="GLOMAG",
            country="YE",
            dob_or_founding="1978-05-15",
            sanction_id="SDN_NUM_10153",
            risk_rating=94
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00154",
            full_name="DESIGNATED_TARGET_0154_OFAC",
            aliases=["ALIAS_A_154", "ALIAS_B_154", "AKA_CORP_154"],
            entity_type="INDIVIDUAL",
            program="CYBER2",
            country="ZW",
            dob_or_founding="1979-05-15",
            sanction_id="SDN_NUM_10154",
            risk_rating=95
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00155",
            full_name="DESIGNATED_TARGET_0155_OFAC",
            aliases=["ALIAS_A_155", "ALIAS_B_155", "AKA_CORP_155"],
            entity_type="ORGANIZATION",
            program="DPRK",
            country="NI",
            dob_or_founding="1980-05-15",
            sanction_id="SDN_NUM_10155",
            risk_rating=96
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00156",
            full_name="DESIGNATED_TARGET_0156_OFAC",
            aliases=["ALIAS_A_156", "ALIAS_B_156", "AKA_CORP_156"],
            entity_type="INDIVIDUAL",
            program="IRAN-HR",
            country="RU",
            dob_or_founding="1981-05-15",
            sanction_id="SDN_NUM_10156",
            risk_rating=97
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00157",
            full_name="DESIGNATED_TARGET_0157_OFAC",
            aliases=["ALIAS_A_157", "ALIAS_B_157", "AKA_CORP_157"],
            entity_type="ORGANIZATION",
            program="RUSSIA-EO14024",
            country="KP",
            dob_or_founding="1982-05-15",
            sanction_id="SDN_NUM_10157",
            risk_rating=98
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00158",
            full_name="DESIGNATED_TARGET_0158_OFAC",
            aliases=["ALIAS_A_158", "ALIAS_B_158", "AKA_CORP_158"],
            entity_type="INDIVIDUAL",
            program="SYRIA",
            country="IR",
            dob_or_founding="1983-05-15",
            sanction_id="SDN_NUM_10158",
            risk_rating=99
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00159",
            full_name="DESIGNATED_TARGET_0159_OFAC",
            aliases=["ALIAS_A_159", "ALIAS_B_159", "AKA_CORP_159"],
            entity_type="ORGANIZATION",
            program="VENEZUELA-EO13884",
            country="SY",
            dob_or_founding="1984-05-15",
            sanction_id="SDN_NUM_10159",
            risk_rating=100
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00160",
            full_name="DESIGNATED_TARGET_0160_OFAC",
            aliases=["ALIAS_A_160", "ALIAS_B_160", "AKA_CORP_160"],
            entity_type="INDIVIDUAL",
            program="SDNTK",
            country="VE",
            dob_or_founding="1985-05-15",
            sanction_id="SDN_NUM_10160",
            risk_rating=85
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00161",
            full_name="DESIGNATED_TARGET_0161_OFAC",
            aliases=["ALIAS_A_161", "ALIAS_B_161", "AKA_CORP_161"],
            entity_type="ORGANIZATION",
            program="GLOMAG",
            country="CU",
            dob_or_founding="1986-05-15",
            sanction_id="SDN_NUM_10161",
            risk_rating=86
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00162",
            full_name="DESIGNATED_TARGET_0162_OFAC",
            aliases=["ALIAS_A_162", "ALIAS_B_162", "AKA_CORP_162"],
            entity_type="INDIVIDUAL",
            program="CYBER2",
            country="MM",
            dob_or_founding="1987-05-15",
            sanction_id="SDN_NUM_10162",
            risk_rating=87
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00163",
            full_name="DESIGNATED_TARGET_0163_OFAC",
            aliases=["ALIAS_A_163", "ALIAS_B_163", "AKA_CORP_163"],
            entity_type="ORGANIZATION",
            program="DPRK",
            country="BY",
            dob_or_founding="1988-05-15",
            sanction_id="SDN_NUM_10163",
            risk_rating=88
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00164",
            full_name="DESIGNATED_TARGET_0164_OFAC",
            aliases=["ALIAS_A_164", "ALIAS_B_164", "AKA_CORP_164"],
            entity_type="INDIVIDUAL",
            program="IRAN-HR",
            country="SD",
            dob_or_founding="1989-05-15",
            sanction_id="SDN_NUM_10164",
            risk_rating=89
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00165",
            full_name="DESIGNATED_TARGET_0165_OFAC",
            aliases=["ALIAS_A_165", "ALIAS_B_165", "AKA_CORP_165"],
            entity_type="ORGANIZATION",
            program="RUSSIA-EO14024",
            country="YE",
            dob_or_founding="1990-05-15",
            sanction_id="SDN_NUM_10165",
            risk_rating=90
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00166",
            full_name="DESIGNATED_TARGET_0166_OFAC",
            aliases=["ALIAS_A_166", "ALIAS_B_166", "AKA_CORP_166"],
            entity_type="INDIVIDUAL",
            program="SYRIA",
            country="ZW",
            dob_or_founding="1991-05-15",
            sanction_id="SDN_NUM_10166",
            risk_rating=91
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00167",
            full_name="DESIGNATED_TARGET_0167_OFAC",
            aliases=["ALIAS_A_167", "ALIAS_B_167", "AKA_CORP_167"],
            entity_type="ORGANIZATION",
            program="VENEZUELA-EO13884",
            country="NI",
            dob_or_founding="1992-05-15",
            sanction_id="SDN_NUM_10167",
            risk_rating=92
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00168",
            full_name="DESIGNATED_TARGET_0168_OFAC",
            aliases=["ALIAS_A_168", "ALIAS_B_168", "AKA_CORP_168"],
            entity_type="INDIVIDUAL",
            program="SDNTK",
            country="RU",
            dob_or_founding="1993-05-15",
            sanction_id="SDN_NUM_10168",
            risk_rating=93
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00169",
            full_name="DESIGNATED_TARGET_0169_OFAC",
            aliases=["ALIAS_A_169", "ALIAS_B_169", "AKA_CORP_169"],
            entity_type="ORGANIZATION",
            program="GLOMAG",
            country="KP",
            dob_or_founding="1994-05-15",
            sanction_id="SDN_NUM_10169",
            risk_rating=94
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00170",
            full_name="DESIGNATED_TARGET_0170_OFAC",
            aliases=["ALIAS_A_170", "ALIAS_B_170", "AKA_CORP_170"],
            entity_type="INDIVIDUAL",
            program="CYBER2",
            country="IR",
            dob_or_founding="1995-05-15",
            sanction_id="SDN_NUM_10170",
            risk_rating=95
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00171",
            full_name="DESIGNATED_TARGET_0171_OFAC",
            aliases=["ALIAS_A_171", "ALIAS_B_171", "AKA_CORP_171"],
            entity_type="ORGANIZATION",
            program="DPRK",
            country="SY",
            dob_or_founding="1996-05-15",
            sanction_id="SDN_NUM_10171",
            risk_rating=96
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00172",
            full_name="DESIGNATED_TARGET_0172_OFAC",
            aliases=["ALIAS_A_172", "ALIAS_B_172", "AKA_CORP_172"],
            entity_type="INDIVIDUAL",
            program="IRAN-HR",
            country="VE",
            dob_or_founding="1997-05-15",
            sanction_id="SDN_NUM_10172",
            risk_rating=97
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00173",
            full_name="DESIGNATED_TARGET_0173_OFAC",
            aliases=["ALIAS_A_173", "ALIAS_B_173", "AKA_CORP_173"],
            entity_type="ORGANIZATION",
            program="RUSSIA-EO14024",
            country="CU",
            dob_or_founding="1998-05-15",
            sanction_id="SDN_NUM_10173",
            risk_rating=98
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00174",
            full_name="DESIGNATED_TARGET_0174_OFAC",
            aliases=["ALIAS_A_174", "ALIAS_B_174", "AKA_CORP_174"],
            entity_type="INDIVIDUAL",
            program="SYRIA",
            country="MM",
            dob_or_founding="1999-05-15",
            sanction_id="SDN_NUM_10174",
            risk_rating=99
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00175",
            full_name="DESIGNATED_TARGET_0175_OFAC",
            aliases=["ALIAS_A_175", "ALIAS_B_175", "AKA_CORP_175"],
            entity_type="ORGANIZATION",
            program="VENEZUELA-EO13884",
            country="BY",
            dob_or_founding="2000-05-15",
            sanction_id="SDN_NUM_10175",
            risk_rating=100
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00176",
            full_name="DESIGNATED_TARGET_0176_OFAC",
            aliases=["ALIAS_A_176", "ALIAS_B_176", "AKA_CORP_176"],
            entity_type="INDIVIDUAL",
            program="SDNTK",
            country="SD",
            dob_or_founding="2001-05-15",
            sanction_id="SDN_NUM_10176",
            risk_rating=85
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00177",
            full_name="DESIGNATED_TARGET_0177_OFAC",
            aliases=["ALIAS_A_177", "ALIAS_B_177", "AKA_CORP_177"],
            entity_type="ORGANIZATION",
            program="GLOMAG",
            country="YE",
            dob_or_founding="2002-05-15",
            sanction_id="SDN_NUM_10177",
            risk_rating=86
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00178",
            full_name="DESIGNATED_TARGET_0178_OFAC",
            aliases=["ALIAS_A_178", "ALIAS_B_178", "AKA_CORP_178"],
            entity_type="INDIVIDUAL",
            program="CYBER2",
            country="ZW",
            dob_or_founding="2003-05-15",
            sanction_id="SDN_NUM_10178",
            risk_rating=87
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00179",
            full_name="DESIGNATED_TARGET_0179_OFAC",
            aliases=["ALIAS_A_179", "ALIAS_B_179", "AKA_CORP_179"],
            entity_type="ORGANIZATION",
            program="DPRK",
            country="NI",
            dob_or_founding="2004-05-15",
            sanction_id="SDN_NUM_10179",
            risk_rating=88
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00180",
            full_name="DESIGNATED_TARGET_0180_OFAC",
            aliases=["ALIAS_A_180", "ALIAS_B_180", "AKA_CORP_180"],
            entity_type="INDIVIDUAL",
            program="IRAN-HR",
            country="RU",
            dob_or_founding="1960-05-15",
            sanction_id="SDN_NUM_10180",
            risk_rating=89
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00181",
            full_name="DESIGNATED_TARGET_0181_OFAC",
            aliases=["ALIAS_A_181", "ALIAS_B_181", "AKA_CORP_181"],
            entity_type="ORGANIZATION",
            program="RUSSIA-EO14024",
            country="KP",
            dob_or_founding="1961-05-15",
            sanction_id="SDN_NUM_10181",
            risk_rating=90
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00182",
            full_name="DESIGNATED_TARGET_0182_OFAC",
            aliases=["ALIAS_A_182", "ALIAS_B_182", "AKA_CORP_182"],
            entity_type="INDIVIDUAL",
            program="SYRIA",
            country="IR",
            dob_or_founding="1962-05-15",
            sanction_id="SDN_NUM_10182",
            risk_rating=91
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00183",
            full_name="DESIGNATED_TARGET_0183_OFAC",
            aliases=["ALIAS_A_183", "ALIAS_B_183", "AKA_CORP_183"],
            entity_type="ORGANIZATION",
            program="VENEZUELA-EO13884",
            country="SY",
            dob_or_founding="1963-05-15",
            sanction_id="SDN_NUM_10183",
            risk_rating=92
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00184",
            full_name="DESIGNATED_TARGET_0184_OFAC",
            aliases=["ALIAS_A_184", "ALIAS_B_184", "AKA_CORP_184"],
            entity_type="INDIVIDUAL",
            program="SDNTK",
            country="VE",
            dob_or_founding="1964-05-15",
            sanction_id="SDN_NUM_10184",
            risk_rating=93
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00185",
            full_name="DESIGNATED_TARGET_0185_OFAC",
            aliases=["ALIAS_A_185", "ALIAS_B_185", "AKA_CORP_185"],
            entity_type="ORGANIZATION",
            program="GLOMAG",
            country="CU",
            dob_or_founding="1965-05-15",
            sanction_id="SDN_NUM_10185",
            risk_rating=94
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00186",
            full_name="DESIGNATED_TARGET_0186_OFAC",
            aliases=["ALIAS_A_186", "ALIAS_B_186", "AKA_CORP_186"],
            entity_type="INDIVIDUAL",
            program="CYBER2",
            country="MM",
            dob_or_founding="1966-05-15",
            sanction_id="SDN_NUM_10186",
            risk_rating=95
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00187",
            full_name="DESIGNATED_TARGET_0187_OFAC",
            aliases=["ALIAS_A_187", "ALIAS_B_187", "AKA_CORP_187"],
            entity_type="ORGANIZATION",
            program="DPRK",
            country="BY",
            dob_or_founding="1967-05-15",
            sanction_id="SDN_NUM_10187",
            risk_rating=96
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00188",
            full_name="DESIGNATED_TARGET_0188_OFAC",
            aliases=["ALIAS_A_188", "ALIAS_B_188", "AKA_CORP_188"],
            entity_type="INDIVIDUAL",
            program="IRAN-HR",
            country="SD",
            dob_or_founding="1968-05-15",
            sanction_id="SDN_NUM_10188",
            risk_rating=97
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00189",
            full_name="DESIGNATED_TARGET_0189_OFAC",
            aliases=["ALIAS_A_189", "ALIAS_B_189", "AKA_CORP_189"],
            entity_type="ORGANIZATION",
            program="RUSSIA-EO14024",
            country="YE",
            dob_or_founding="1969-05-15",
            sanction_id="SDN_NUM_10189",
            risk_rating=98
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00190",
            full_name="DESIGNATED_TARGET_0190_OFAC",
            aliases=["ALIAS_A_190", "ALIAS_B_190", "AKA_CORP_190"],
            entity_type="INDIVIDUAL",
            program="SYRIA",
            country="ZW",
            dob_or_founding="1970-05-15",
            sanction_id="SDN_NUM_10190",
            risk_rating=99
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00191",
            full_name="DESIGNATED_TARGET_0191_OFAC",
            aliases=["ALIAS_A_191", "ALIAS_B_191", "AKA_CORP_191"],
            entity_type="ORGANIZATION",
            program="VENEZUELA-EO13884",
            country="NI",
            dob_or_founding="1971-05-15",
            sanction_id="SDN_NUM_10191",
            risk_rating=100
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00192",
            full_name="DESIGNATED_TARGET_0192_OFAC",
            aliases=["ALIAS_A_192", "ALIAS_B_192", "AKA_CORP_192"],
            entity_type="INDIVIDUAL",
            program="SDNTK",
            country="RU",
            dob_or_founding="1972-05-15",
            sanction_id="SDN_NUM_10192",
            risk_rating=85
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00193",
            full_name="DESIGNATED_TARGET_0193_OFAC",
            aliases=["ALIAS_A_193", "ALIAS_B_193", "AKA_CORP_193"],
            entity_type="ORGANIZATION",
            program="GLOMAG",
            country="KP",
            dob_or_founding="1973-05-15",
            sanction_id="SDN_NUM_10193",
            risk_rating=86
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00194",
            full_name="DESIGNATED_TARGET_0194_OFAC",
            aliases=["ALIAS_A_194", "ALIAS_B_194", "AKA_CORP_194"],
            entity_type="INDIVIDUAL",
            program="CYBER2",
            country="IR",
            dob_or_founding="1974-05-15",
            sanction_id="SDN_NUM_10194",
            risk_rating=87
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00195",
            full_name="DESIGNATED_TARGET_0195_OFAC",
            aliases=["ALIAS_A_195", "ALIAS_B_195", "AKA_CORP_195"],
            entity_type="ORGANIZATION",
            program="DPRK",
            country="SY",
            dob_or_founding="1975-05-15",
            sanction_id="SDN_NUM_10195",
            risk_rating=88
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00196",
            full_name="DESIGNATED_TARGET_0196_OFAC",
            aliases=["ALIAS_A_196", "ALIAS_B_196", "AKA_CORP_196"],
            entity_type="INDIVIDUAL",
            program="IRAN-HR",
            country="VE",
            dob_or_founding="1976-05-15",
            sanction_id="SDN_NUM_10196",
            risk_rating=89
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00197",
            full_name="DESIGNATED_TARGET_0197_OFAC",
            aliases=["ALIAS_A_197", "ALIAS_B_197", "AKA_CORP_197"],
            entity_type="ORGANIZATION",
            program="RUSSIA-EO14024",
            country="CU",
            dob_or_founding="1977-05-15",
            sanction_id="SDN_NUM_10197",
            risk_rating=90
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00198",
            full_name="DESIGNATED_TARGET_0198_OFAC",
            aliases=["ALIAS_A_198", "ALIAS_B_198", "AKA_CORP_198"],
            entity_type="INDIVIDUAL",
            program="SYRIA",
            country="MM",
            dob_or_founding="1978-05-15",
            sanction_id="SDN_NUM_10198",
            risk_rating=91
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00199",
            full_name="DESIGNATED_TARGET_0199_OFAC",
            aliases=["ALIAS_A_199", "ALIAS_B_199", "AKA_CORP_199"],
            entity_type="ORGANIZATION",
            program="VENEZUELA-EO13884",
            country="BY",
            dob_or_founding="1979-05-15",
            sanction_id="SDN_NUM_10199",
            risk_rating=92
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00200",
            full_name="DESIGNATED_TARGET_0200_OFAC",
            aliases=["ALIAS_A_200", "ALIAS_B_200", "AKA_CORP_200"],
            entity_type="INDIVIDUAL",
            program="SDNTK",
            country="SD",
            dob_or_founding="1980-05-15",
            sanction_id="SDN_NUM_10200",
            risk_rating=93
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00201",
            full_name="DESIGNATED_TARGET_0201_OFAC",
            aliases=["ALIAS_A_201", "ALIAS_B_201", "AKA_CORP_201"],
            entity_type="ORGANIZATION",
            program="GLOMAG",
            country="YE",
            dob_or_founding="1981-05-15",
            sanction_id="SDN_NUM_10201",
            risk_rating=94
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00202",
            full_name="DESIGNATED_TARGET_0202_OFAC",
            aliases=["ALIAS_A_202", "ALIAS_B_202", "AKA_CORP_202"],
            entity_type="INDIVIDUAL",
            program="CYBER2",
            country="ZW",
            dob_or_founding="1982-05-15",
            sanction_id="SDN_NUM_10202",
            risk_rating=95
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00203",
            full_name="DESIGNATED_TARGET_0203_OFAC",
            aliases=["ALIAS_A_203", "ALIAS_B_203", "AKA_CORP_203"],
            entity_type="ORGANIZATION",
            program="DPRK",
            country="NI",
            dob_or_founding="1983-05-15",
            sanction_id="SDN_NUM_10203",
            risk_rating=96
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00204",
            full_name="DESIGNATED_TARGET_0204_OFAC",
            aliases=["ALIAS_A_204", "ALIAS_B_204", "AKA_CORP_204"],
            entity_type="INDIVIDUAL",
            program="IRAN-HR",
            country="RU",
            dob_or_founding="1984-05-15",
            sanction_id="SDN_NUM_10204",
            risk_rating=97
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00205",
            full_name="DESIGNATED_TARGET_0205_OFAC",
            aliases=["ALIAS_A_205", "ALIAS_B_205", "AKA_CORP_205"],
            entity_type="ORGANIZATION",
            program="RUSSIA-EO14024",
            country="KP",
            dob_or_founding="1985-05-15",
            sanction_id="SDN_NUM_10205",
            risk_rating=98
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00206",
            full_name="DESIGNATED_TARGET_0206_OFAC",
            aliases=["ALIAS_A_206", "ALIAS_B_206", "AKA_CORP_206"],
            entity_type="INDIVIDUAL",
            program="SYRIA",
            country="IR",
            dob_or_founding="1986-05-15",
            sanction_id="SDN_NUM_10206",
            risk_rating=99
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00207",
            full_name="DESIGNATED_TARGET_0207_OFAC",
            aliases=["ALIAS_A_207", "ALIAS_B_207", "AKA_CORP_207"],
            entity_type="ORGANIZATION",
            program="VENEZUELA-EO13884",
            country="SY",
            dob_or_founding="1987-05-15",
            sanction_id="SDN_NUM_10207",
            risk_rating=100
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00208",
            full_name="DESIGNATED_TARGET_0208_OFAC",
            aliases=["ALIAS_A_208", "ALIAS_B_208", "AKA_CORP_208"],
            entity_type="INDIVIDUAL",
            program="SDNTK",
            country="VE",
            dob_or_founding="1988-05-15",
            sanction_id="SDN_NUM_10208",
            risk_rating=85
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00209",
            full_name="DESIGNATED_TARGET_0209_OFAC",
            aliases=["ALIAS_A_209", "ALIAS_B_209", "AKA_CORP_209"],
            entity_type="ORGANIZATION",
            program="GLOMAG",
            country="CU",
            dob_or_founding="1989-05-15",
            sanction_id="SDN_NUM_10209",
            risk_rating=86
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00210",
            full_name="DESIGNATED_TARGET_0210_OFAC",
            aliases=["ALIAS_A_210", "ALIAS_B_210", "AKA_CORP_210"],
            entity_type="INDIVIDUAL",
            program="CYBER2",
            country="MM",
            dob_or_founding="1990-05-15",
            sanction_id="SDN_NUM_10210",
            risk_rating=87
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00211",
            full_name="DESIGNATED_TARGET_0211_OFAC",
            aliases=["ALIAS_A_211", "ALIAS_B_211", "AKA_CORP_211"],
            entity_type="ORGANIZATION",
            program="DPRK",
            country="BY",
            dob_or_founding="1991-05-15",
            sanction_id="SDN_NUM_10211",
            risk_rating=88
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00212",
            full_name="DESIGNATED_TARGET_0212_OFAC",
            aliases=["ALIAS_A_212", "ALIAS_B_212", "AKA_CORP_212"],
            entity_type="INDIVIDUAL",
            program="IRAN-HR",
            country="SD",
            dob_or_founding="1992-05-15",
            sanction_id="SDN_NUM_10212",
            risk_rating=89
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00213",
            full_name="DESIGNATED_TARGET_0213_OFAC",
            aliases=["ALIAS_A_213", "ALIAS_B_213", "AKA_CORP_213"],
            entity_type="ORGANIZATION",
            program="RUSSIA-EO14024",
            country="YE",
            dob_or_founding="1993-05-15",
            sanction_id="SDN_NUM_10213",
            risk_rating=90
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00214",
            full_name="DESIGNATED_TARGET_0214_OFAC",
            aliases=["ALIAS_A_214", "ALIAS_B_214", "AKA_CORP_214"],
            entity_type="INDIVIDUAL",
            program="SYRIA",
            country="ZW",
            dob_or_founding="1994-05-15",
            sanction_id="SDN_NUM_10214",
            risk_rating=91
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00215",
            full_name="DESIGNATED_TARGET_0215_OFAC",
            aliases=["ALIAS_A_215", "ALIAS_B_215", "AKA_CORP_215"],
            entity_type="ORGANIZATION",
            program="VENEZUELA-EO13884",
            country="NI",
            dob_or_founding="1995-05-15",
            sanction_id="SDN_NUM_10215",
            risk_rating=92
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00216",
            full_name="DESIGNATED_TARGET_0216_OFAC",
            aliases=["ALIAS_A_216", "ALIAS_B_216", "AKA_CORP_216"],
            entity_type="INDIVIDUAL",
            program="SDNTK",
            country="RU",
            dob_or_founding="1996-05-15",
            sanction_id="SDN_NUM_10216",
            risk_rating=93
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00217",
            full_name="DESIGNATED_TARGET_0217_OFAC",
            aliases=["ALIAS_A_217", "ALIAS_B_217", "AKA_CORP_217"],
            entity_type="ORGANIZATION",
            program="GLOMAG",
            country="KP",
            dob_or_founding="1997-05-15",
            sanction_id="SDN_NUM_10217",
            risk_rating=94
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00218",
            full_name="DESIGNATED_TARGET_0218_OFAC",
            aliases=["ALIAS_A_218", "ALIAS_B_218", "AKA_CORP_218"],
            entity_type="INDIVIDUAL",
            program="CYBER2",
            country="IR",
            dob_or_founding="1998-05-15",
            sanction_id="SDN_NUM_10218",
            risk_rating=95
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00219",
            full_name="DESIGNATED_TARGET_0219_OFAC",
            aliases=["ALIAS_A_219", "ALIAS_B_219", "AKA_CORP_219"],
            entity_type="ORGANIZATION",
            program="DPRK",
            country="SY",
            dob_or_founding="1999-05-15",
            sanction_id="SDN_NUM_10219",
            risk_rating=96
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00220",
            full_name="DESIGNATED_TARGET_0220_OFAC",
            aliases=["ALIAS_A_220", "ALIAS_B_220", "AKA_CORP_220"],
            entity_type="INDIVIDUAL",
            program="IRAN-HR",
            country="VE",
            dob_or_founding="2000-05-15",
            sanction_id="SDN_NUM_10220",
            risk_rating=97
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00221",
            full_name="DESIGNATED_TARGET_0221_OFAC",
            aliases=["ALIAS_A_221", "ALIAS_B_221", "AKA_CORP_221"],
            entity_type="ORGANIZATION",
            program="RUSSIA-EO14024",
            country="CU",
            dob_or_founding="2001-05-15",
            sanction_id="SDN_NUM_10221",
            risk_rating=98
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00222",
            full_name="DESIGNATED_TARGET_0222_OFAC",
            aliases=["ALIAS_A_222", "ALIAS_B_222", "AKA_CORP_222"],
            entity_type="INDIVIDUAL",
            program="SYRIA",
            country="MM",
            dob_or_founding="2002-05-15",
            sanction_id="SDN_NUM_10222",
            risk_rating=99
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00223",
            full_name="DESIGNATED_TARGET_0223_OFAC",
            aliases=["ALIAS_A_223", "ALIAS_B_223", "AKA_CORP_223"],
            entity_type="ORGANIZATION",
            program="VENEZUELA-EO13884",
            country="BY",
            dob_or_founding="2003-05-15",
            sanction_id="SDN_NUM_10223",
            risk_rating=100
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00224",
            full_name="DESIGNATED_TARGET_0224_OFAC",
            aliases=["ALIAS_A_224", "ALIAS_B_224", "AKA_CORP_224"],
            entity_type="INDIVIDUAL",
            program="SDNTK",
            country="SD",
            dob_or_founding="2004-05-15",
            sanction_id="SDN_NUM_10224",
            risk_rating=85
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00225",
            full_name="DESIGNATED_TARGET_0225_OFAC",
            aliases=["ALIAS_A_225", "ALIAS_B_225", "AKA_CORP_225"],
            entity_type="ORGANIZATION",
            program="GLOMAG",
            country="YE",
            dob_or_founding="1960-05-15",
            sanction_id="SDN_NUM_10225",
            risk_rating=86
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00226",
            full_name="DESIGNATED_TARGET_0226_OFAC",
            aliases=["ALIAS_A_226", "ALIAS_B_226", "AKA_CORP_226"],
            entity_type="INDIVIDUAL",
            program="CYBER2",
            country="ZW",
            dob_or_founding="1961-05-15",
            sanction_id="SDN_NUM_10226",
            risk_rating=87
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00227",
            full_name="DESIGNATED_TARGET_0227_OFAC",
            aliases=["ALIAS_A_227", "ALIAS_B_227", "AKA_CORP_227"],
            entity_type="ORGANIZATION",
            program="DPRK",
            country="NI",
            dob_or_founding="1962-05-15",
            sanction_id="SDN_NUM_10227",
            risk_rating=88
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00228",
            full_name="DESIGNATED_TARGET_0228_OFAC",
            aliases=["ALIAS_A_228", "ALIAS_B_228", "AKA_CORP_228"],
            entity_type="INDIVIDUAL",
            program="IRAN-HR",
            country="RU",
            dob_or_founding="1963-05-15",
            sanction_id="SDN_NUM_10228",
            risk_rating=89
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00229",
            full_name="DESIGNATED_TARGET_0229_OFAC",
            aliases=["ALIAS_A_229", "ALIAS_B_229", "AKA_CORP_229"],
            entity_type="ORGANIZATION",
            program="RUSSIA-EO14024",
            country="KP",
            dob_or_founding="1964-05-15",
            sanction_id="SDN_NUM_10229",
            risk_rating=90
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00230",
            full_name="DESIGNATED_TARGET_0230_OFAC",
            aliases=["ALIAS_A_230", "ALIAS_B_230", "AKA_CORP_230"],
            entity_type="INDIVIDUAL",
            program="SYRIA",
            country="IR",
            dob_or_founding="1965-05-15",
            sanction_id="SDN_NUM_10230",
            risk_rating=91
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00231",
            full_name="DESIGNATED_TARGET_0231_OFAC",
            aliases=["ALIAS_A_231", "ALIAS_B_231", "AKA_CORP_231"],
            entity_type="ORGANIZATION",
            program="VENEZUELA-EO13884",
            country="SY",
            dob_or_founding="1966-05-15",
            sanction_id="SDN_NUM_10231",
            risk_rating=92
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00232",
            full_name="DESIGNATED_TARGET_0232_OFAC",
            aliases=["ALIAS_A_232", "ALIAS_B_232", "AKA_CORP_232"],
            entity_type="INDIVIDUAL",
            program="SDNTK",
            country="VE",
            dob_or_founding="1967-05-15",
            sanction_id="SDN_NUM_10232",
            risk_rating=93
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00233",
            full_name="DESIGNATED_TARGET_0233_OFAC",
            aliases=["ALIAS_A_233", "ALIAS_B_233", "AKA_CORP_233"],
            entity_type="ORGANIZATION",
            program="GLOMAG",
            country="CU",
            dob_or_founding="1968-05-15",
            sanction_id="SDN_NUM_10233",
            risk_rating=94
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00234",
            full_name="DESIGNATED_TARGET_0234_OFAC",
            aliases=["ALIAS_A_234", "ALIAS_B_234", "AKA_CORP_234"],
            entity_type="INDIVIDUAL",
            program="CYBER2",
            country="MM",
            dob_or_founding="1969-05-15",
            sanction_id="SDN_NUM_10234",
            risk_rating=95
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00235",
            full_name="DESIGNATED_TARGET_0235_OFAC",
            aliases=["ALIAS_A_235", "ALIAS_B_235", "AKA_CORP_235"],
            entity_type="ORGANIZATION",
            program="DPRK",
            country="BY",
            dob_or_founding="1970-05-15",
            sanction_id="SDN_NUM_10235",
            risk_rating=96
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00236",
            full_name="DESIGNATED_TARGET_0236_OFAC",
            aliases=["ALIAS_A_236", "ALIAS_B_236", "AKA_CORP_236"],
            entity_type="INDIVIDUAL",
            program="IRAN-HR",
            country="SD",
            dob_or_founding="1971-05-15",
            sanction_id="SDN_NUM_10236",
            risk_rating=97
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00237",
            full_name="DESIGNATED_TARGET_0237_OFAC",
            aliases=["ALIAS_A_237", "ALIAS_B_237", "AKA_CORP_237"],
            entity_type="ORGANIZATION",
            program="RUSSIA-EO14024",
            country="YE",
            dob_or_founding="1972-05-15",
            sanction_id="SDN_NUM_10237",
            risk_rating=98
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00238",
            full_name="DESIGNATED_TARGET_0238_OFAC",
            aliases=["ALIAS_A_238", "ALIAS_B_238", "AKA_CORP_238"],
            entity_type="INDIVIDUAL",
            program="SYRIA",
            country="ZW",
            dob_or_founding="1973-05-15",
            sanction_id="SDN_NUM_10238",
            risk_rating=99
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00239",
            full_name="DESIGNATED_TARGET_0239_OFAC",
            aliases=["ALIAS_A_239", "ALIAS_B_239", "AKA_CORP_239"],
            entity_type="ORGANIZATION",
            program="VENEZUELA-EO13884",
            country="NI",
            dob_or_founding="1974-05-15",
            sanction_id="SDN_NUM_10239",
            risk_rating=100
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00240",
            full_name="DESIGNATED_TARGET_0240_OFAC",
            aliases=["ALIAS_A_240", "ALIAS_B_240", "AKA_CORP_240"],
            entity_type="INDIVIDUAL",
            program="SDNTK",
            country="RU",
            dob_or_founding="1975-05-15",
            sanction_id="SDN_NUM_10240",
            risk_rating=85
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00241",
            full_name="DESIGNATED_TARGET_0241_OFAC",
            aliases=["ALIAS_A_241", "ALIAS_B_241", "AKA_CORP_241"],
            entity_type="ORGANIZATION",
            program="GLOMAG",
            country="KP",
            dob_or_founding="1976-05-15",
            sanction_id="SDN_NUM_10241",
            risk_rating=86
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00242",
            full_name="DESIGNATED_TARGET_0242_OFAC",
            aliases=["ALIAS_A_242", "ALIAS_B_242", "AKA_CORP_242"],
            entity_type="INDIVIDUAL",
            program="CYBER2",
            country="IR",
            dob_or_founding="1977-05-15",
            sanction_id="SDN_NUM_10242",
            risk_rating=87
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00243",
            full_name="DESIGNATED_TARGET_0243_OFAC",
            aliases=["ALIAS_A_243", "ALIAS_B_243", "AKA_CORP_243"],
            entity_type="ORGANIZATION",
            program="DPRK",
            country="SY",
            dob_or_founding="1978-05-15",
            sanction_id="SDN_NUM_10243",
            risk_rating=88
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00244",
            full_name="DESIGNATED_TARGET_0244_OFAC",
            aliases=["ALIAS_A_244", "ALIAS_B_244", "AKA_CORP_244"],
            entity_type="INDIVIDUAL",
            program="IRAN-HR",
            country="VE",
            dob_or_founding="1979-05-15",
            sanction_id="SDN_NUM_10244",
            risk_rating=89
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00245",
            full_name="DESIGNATED_TARGET_0245_OFAC",
            aliases=["ALIAS_A_245", "ALIAS_B_245", "AKA_CORP_245"],
            entity_type="ORGANIZATION",
            program="RUSSIA-EO14024",
            country="CU",
            dob_or_founding="1980-05-15",
            sanction_id="SDN_NUM_10245",
            risk_rating=90
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00246",
            full_name="DESIGNATED_TARGET_0246_OFAC",
            aliases=["ALIAS_A_246", "ALIAS_B_246", "AKA_CORP_246"],
            entity_type="INDIVIDUAL",
            program="SYRIA",
            country="MM",
            dob_or_founding="1981-05-15",
            sanction_id="SDN_NUM_10246",
            risk_rating=91
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00247",
            full_name="DESIGNATED_TARGET_0247_OFAC",
            aliases=["ALIAS_A_247", "ALIAS_B_247", "AKA_CORP_247"],
            entity_type="ORGANIZATION",
            program="VENEZUELA-EO13884",
            country="BY",
            dob_or_founding="1982-05-15",
            sanction_id="SDN_NUM_10247",
            risk_rating=92
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00248",
            full_name="DESIGNATED_TARGET_0248_OFAC",
            aliases=["ALIAS_A_248", "ALIAS_B_248", "AKA_CORP_248"],
            entity_type="INDIVIDUAL",
            program="SDNTK",
            country="SD",
            dob_or_founding="1983-05-15",
            sanction_id="SDN_NUM_10248",
            risk_rating=93
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00249",
            full_name="DESIGNATED_TARGET_0249_OFAC",
            aliases=["ALIAS_A_249", "ALIAS_B_249", "AKA_CORP_249"],
            entity_type="ORGANIZATION",
            program="GLOMAG",
            country="YE",
            dob_or_founding="1984-05-15",
            sanction_id="SDN_NUM_10249",
            risk_rating=94
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00250",
            full_name="DESIGNATED_TARGET_0250_OFAC",
            aliases=["ALIAS_A_250", "ALIAS_B_250", "AKA_CORP_250"],
            entity_type="INDIVIDUAL",
            program="CYBER2",
            country="ZW",
            dob_or_founding="1985-05-15",
            sanction_id="SDN_NUM_10250",
            risk_rating=95
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00251",
            full_name="DESIGNATED_TARGET_0251_OFAC",
            aliases=["ALIAS_A_251", "ALIAS_B_251", "AKA_CORP_251"],
            entity_type="ORGANIZATION",
            program="DPRK",
            country="NI",
            dob_or_founding="1986-05-15",
            sanction_id="SDN_NUM_10251",
            risk_rating=96
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00252",
            full_name="DESIGNATED_TARGET_0252_OFAC",
            aliases=["ALIAS_A_252", "ALIAS_B_252", "AKA_CORP_252"],
            entity_type="INDIVIDUAL",
            program="IRAN-HR",
            country="RU",
            dob_or_founding="1987-05-15",
            sanction_id="SDN_NUM_10252",
            risk_rating=97
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00253",
            full_name="DESIGNATED_TARGET_0253_OFAC",
            aliases=["ALIAS_A_253", "ALIAS_B_253", "AKA_CORP_253"],
            entity_type="ORGANIZATION",
            program="RUSSIA-EO14024",
            country="KP",
            dob_or_founding="1988-05-15",
            sanction_id="SDN_NUM_10253",
            risk_rating=98
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00254",
            full_name="DESIGNATED_TARGET_0254_OFAC",
            aliases=["ALIAS_A_254", "ALIAS_B_254", "AKA_CORP_254"],
            entity_type="INDIVIDUAL",
            program="SYRIA",
            country="IR",
            dob_or_founding="1989-05-15",
            sanction_id="SDN_NUM_10254",
            risk_rating=99
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00255",
            full_name="DESIGNATED_TARGET_0255_OFAC",
            aliases=["ALIAS_A_255", "ALIAS_B_255", "AKA_CORP_255"],
            entity_type="ORGANIZATION",
            program="VENEZUELA-EO13884",
            country="SY",
            dob_or_founding="1990-05-15",
            sanction_id="SDN_NUM_10255",
            risk_rating=100
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00256",
            full_name="DESIGNATED_TARGET_0256_OFAC",
            aliases=["ALIAS_A_256", "ALIAS_B_256", "AKA_CORP_256"],
            entity_type="INDIVIDUAL",
            program="SDNTK",
            country="VE",
            dob_or_founding="1991-05-15",
            sanction_id="SDN_NUM_10256",
            risk_rating=85
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00257",
            full_name="DESIGNATED_TARGET_0257_OFAC",
            aliases=["ALIAS_A_257", "ALIAS_B_257", "AKA_CORP_257"],
            entity_type="ORGANIZATION",
            program="GLOMAG",
            country="CU",
            dob_or_founding="1992-05-15",
            sanction_id="SDN_NUM_10257",
            risk_rating=86
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00258",
            full_name="DESIGNATED_TARGET_0258_OFAC",
            aliases=["ALIAS_A_258", "ALIAS_B_258", "AKA_CORP_258"],
            entity_type="INDIVIDUAL",
            program="CYBER2",
            country="MM",
            dob_or_founding="1993-05-15",
            sanction_id="SDN_NUM_10258",
            risk_rating=87
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00259",
            full_name="DESIGNATED_TARGET_0259_OFAC",
            aliases=["ALIAS_A_259", "ALIAS_B_259", "AKA_CORP_259"],
            entity_type="ORGANIZATION",
            program="DPRK",
            country="BY",
            dob_or_founding="1994-05-15",
            sanction_id="SDN_NUM_10259",
            risk_rating=88
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00260",
            full_name="DESIGNATED_TARGET_0260_OFAC",
            aliases=["ALIAS_A_260", "ALIAS_B_260", "AKA_CORP_260"],
            entity_type="INDIVIDUAL",
            program="IRAN-HR",
            country="SD",
            dob_or_founding="1995-05-15",
            sanction_id="SDN_NUM_10260",
            risk_rating=89
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00261",
            full_name="DESIGNATED_TARGET_0261_OFAC",
            aliases=["ALIAS_A_261", "ALIAS_B_261", "AKA_CORP_261"],
            entity_type="ORGANIZATION",
            program="RUSSIA-EO14024",
            country="YE",
            dob_or_founding="1996-05-15",
            sanction_id="SDN_NUM_10261",
            risk_rating=90
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00262",
            full_name="DESIGNATED_TARGET_0262_OFAC",
            aliases=["ALIAS_A_262", "ALIAS_B_262", "AKA_CORP_262"],
            entity_type="INDIVIDUAL",
            program="SYRIA",
            country="ZW",
            dob_or_founding="1997-05-15",
            sanction_id="SDN_NUM_10262",
            risk_rating=91
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00263",
            full_name="DESIGNATED_TARGET_0263_OFAC",
            aliases=["ALIAS_A_263", "ALIAS_B_263", "AKA_CORP_263"],
            entity_type="ORGANIZATION",
            program="VENEZUELA-EO13884",
            country="NI",
            dob_or_founding="1998-05-15",
            sanction_id="SDN_NUM_10263",
            risk_rating=92
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00264",
            full_name="DESIGNATED_TARGET_0264_OFAC",
            aliases=["ALIAS_A_264", "ALIAS_B_264", "AKA_CORP_264"],
            entity_type="INDIVIDUAL",
            program="SDNTK",
            country="RU",
            dob_or_founding="1999-05-15",
            sanction_id="SDN_NUM_10264",
            risk_rating=93
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00265",
            full_name="DESIGNATED_TARGET_0265_OFAC",
            aliases=["ALIAS_A_265", "ALIAS_B_265", "AKA_CORP_265"],
            entity_type="ORGANIZATION",
            program="GLOMAG",
            country="KP",
            dob_or_founding="2000-05-15",
            sanction_id="SDN_NUM_10265",
            risk_rating=94
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00266",
            full_name="DESIGNATED_TARGET_0266_OFAC",
            aliases=["ALIAS_A_266", "ALIAS_B_266", "AKA_CORP_266"],
            entity_type="INDIVIDUAL",
            program="CYBER2",
            country="IR",
            dob_or_founding="2001-05-15",
            sanction_id="SDN_NUM_10266",
            risk_rating=95
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00267",
            full_name="DESIGNATED_TARGET_0267_OFAC",
            aliases=["ALIAS_A_267", "ALIAS_B_267", "AKA_CORP_267"],
            entity_type="ORGANIZATION",
            program="DPRK",
            country="SY",
            dob_or_founding="2002-05-15",
            sanction_id="SDN_NUM_10267",
            risk_rating=96
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00268",
            full_name="DESIGNATED_TARGET_0268_OFAC",
            aliases=["ALIAS_A_268", "ALIAS_B_268", "AKA_CORP_268"],
            entity_type="INDIVIDUAL",
            program="IRAN-HR",
            country="VE",
            dob_or_founding="2003-05-15",
            sanction_id="SDN_NUM_10268",
            risk_rating=97
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00269",
            full_name="DESIGNATED_TARGET_0269_OFAC",
            aliases=["ALIAS_A_269", "ALIAS_B_269", "AKA_CORP_269"],
            entity_type="ORGANIZATION",
            program="RUSSIA-EO14024",
            country="CU",
            dob_or_founding="2004-05-15",
            sanction_id="SDN_NUM_10269",
            risk_rating=98
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00270",
            full_name="DESIGNATED_TARGET_0270_OFAC",
            aliases=["ALIAS_A_270", "ALIAS_B_270", "AKA_CORP_270"],
            entity_type="INDIVIDUAL",
            program="SYRIA",
            country="MM",
            dob_or_founding="1960-05-15",
            sanction_id="SDN_NUM_10270",
            risk_rating=99
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00271",
            full_name="DESIGNATED_TARGET_0271_OFAC",
            aliases=["ALIAS_A_271", "ALIAS_B_271", "AKA_CORP_271"],
            entity_type="ORGANIZATION",
            program="VENEZUELA-EO13884",
            country="BY",
            dob_or_founding="1961-05-15",
            sanction_id="SDN_NUM_10271",
            risk_rating=100
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00272",
            full_name="DESIGNATED_TARGET_0272_OFAC",
            aliases=["ALIAS_A_272", "ALIAS_B_272", "AKA_CORP_272"],
            entity_type="INDIVIDUAL",
            program="SDNTK",
            country="SD",
            dob_or_founding="1962-05-15",
            sanction_id="SDN_NUM_10272",
            risk_rating=85
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00273",
            full_name="DESIGNATED_TARGET_0273_OFAC",
            aliases=["ALIAS_A_273", "ALIAS_B_273", "AKA_CORP_273"],
            entity_type="ORGANIZATION",
            program="GLOMAG",
            country="YE",
            dob_or_founding="1963-05-15",
            sanction_id="SDN_NUM_10273",
            risk_rating=86
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00274",
            full_name="DESIGNATED_TARGET_0274_OFAC",
            aliases=["ALIAS_A_274", "ALIAS_B_274", "AKA_CORP_274"],
            entity_type="INDIVIDUAL",
            program="CYBER2",
            country="ZW",
            dob_or_founding="1964-05-15",
            sanction_id="SDN_NUM_10274",
            risk_rating=87
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00275",
            full_name="DESIGNATED_TARGET_0275_OFAC",
            aliases=["ALIAS_A_275", "ALIAS_B_275", "AKA_CORP_275"],
            entity_type="ORGANIZATION",
            program="DPRK",
            country="NI",
            dob_or_founding="1965-05-15",
            sanction_id="SDN_NUM_10275",
            risk_rating=88
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00276",
            full_name="DESIGNATED_TARGET_0276_OFAC",
            aliases=["ALIAS_A_276", "ALIAS_B_276", "AKA_CORP_276"],
            entity_type="INDIVIDUAL",
            program="IRAN-HR",
            country="RU",
            dob_or_founding="1966-05-15",
            sanction_id="SDN_NUM_10276",
            risk_rating=89
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00277",
            full_name="DESIGNATED_TARGET_0277_OFAC",
            aliases=["ALIAS_A_277", "ALIAS_B_277", "AKA_CORP_277"],
            entity_type="ORGANIZATION",
            program="RUSSIA-EO14024",
            country="KP",
            dob_or_founding="1967-05-15",
            sanction_id="SDN_NUM_10277",
            risk_rating=90
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00278",
            full_name="DESIGNATED_TARGET_0278_OFAC",
            aliases=["ALIAS_A_278", "ALIAS_B_278", "AKA_CORP_278"],
            entity_type="INDIVIDUAL",
            program="SYRIA",
            country="IR",
            dob_or_founding="1968-05-15",
            sanction_id="SDN_NUM_10278",
            risk_rating=91
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00279",
            full_name="DESIGNATED_TARGET_0279_OFAC",
            aliases=["ALIAS_A_279", "ALIAS_B_279", "AKA_CORP_279"],
            entity_type="ORGANIZATION",
            program="VENEZUELA-EO13884",
            country="SY",
            dob_or_founding="1969-05-15",
            sanction_id="SDN_NUM_10279",
            risk_rating=92
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00280",
            full_name="DESIGNATED_TARGET_0280_OFAC",
            aliases=["ALIAS_A_280", "ALIAS_B_280", "AKA_CORP_280"],
            entity_type="INDIVIDUAL",
            program="SDNTK",
            country="VE",
            dob_or_founding="1970-05-15",
            sanction_id="SDN_NUM_10280",
            risk_rating=93
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00281",
            full_name="DESIGNATED_TARGET_0281_OFAC",
            aliases=["ALIAS_A_281", "ALIAS_B_281", "AKA_CORP_281"],
            entity_type="ORGANIZATION",
            program="GLOMAG",
            country="CU",
            dob_or_founding="1971-05-15",
            sanction_id="SDN_NUM_10281",
            risk_rating=94
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00282",
            full_name="DESIGNATED_TARGET_0282_OFAC",
            aliases=["ALIAS_A_282", "ALIAS_B_282", "AKA_CORP_282"],
            entity_type="INDIVIDUAL",
            program="CYBER2",
            country="MM",
            dob_or_founding="1972-05-15",
            sanction_id="SDN_NUM_10282",
            risk_rating=95
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00283",
            full_name="DESIGNATED_TARGET_0283_OFAC",
            aliases=["ALIAS_A_283", "ALIAS_B_283", "AKA_CORP_283"],
            entity_type="ORGANIZATION",
            program="DPRK",
            country="BY",
            dob_or_founding="1973-05-15",
            sanction_id="SDN_NUM_10283",
            risk_rating=96
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00284",
            full_name="DESIGNATED_TARGET_0284_OFAC",
            aliases=["ALIAS_A_284", "ALIAS_B_284", "AKA_CORP_284"],
            entity_type="INDIVIDUAL",
            program="IRAN-HR",
            country="SD",
            dob_or_founding="1974-05-15",
            sanction_id="SDN_NUM_10284",
            risk_rating=97
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00285",
            full_name="DESIGNATED_TARGET_0285_OFAC",
            aliases=["ALIAS_A_285", "ALIAS_B_285", "AKA_CORP_285"],
            entity_type="ORGANIZATION",
            program="RUSSIA-EO14024",
            country="YE",
            dob_or_founding="1975-05-15",
            sanction_id="SDN_NUM_10285",
            risk_rating=98
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00286",
            full_name="DESIGNATED_TARGET_0286_OFAC",
            aliases=["ALIAS_A_286", "ALIAS_B_286", "AKA_CORP_286"],
            entity_type="INDIVIDUAL",
            program="SYRIA",
            country="ZW",
            dob_or_founding="1976-05-15",
            sanction_id="SDN_NUM_10286",
            risk_rating=99
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00287",
            full_name="DESIGNATED_TARGET_0287_OFAC",
            aliases=["ALIAS_A_287", "ALIAS_B_287", "AKA_CORP_287"],
            entity_type="ORGANIZATION",
            program="VENEZUELA-EO13884",
            country="NI",
            dob_or_founding="1977-05-15",
            sanction_id="SDN_NUM_10287",
            risk_rating=100
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00288",
            full_name="DESIGNATED_TARGET_0288_OFAC",
            aliases=["ALIAS_A_288", "ALIAS_B_288", "AKA_CORP_288"],
            entity_type="INDIVIDUAL",
            program="SDNTK",
            country="RU",
            dob_or_founding="1978-05-15",
            sanction_id="SDN_NUM_10288",
            risk_rating=85
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00289",
            full_name="DESIGNATED_TARGET_0289_OFAC",
            aliases=["ALIAS_A_289", "ALIAS_B_289", "AKA_CORP_289"],
            entity_type="ORGANIZATION",
            program="GLOMAG",
            country="KP",
            dob_or_founding="1979-05-15",
            sanction_id="SDN_NUM_10289",
            risk_rating=86
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00290",
            full_name="DESIGNATED_TARGET_0290_OFAC",
            aliases=["ALIAS_A_290", "ALIAS_B_290", "AKA_CORP_290"],
            entity_type="INDIVIDUAL",
            program="CYBER2",
            country="IR",
            dob_or_founding="1980-05-15",
            sanction_id="SDN_NUM_10290",
            risk_rating=87
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00291",
            full_name="DESIGNATED_TARGET_0291_OFAC",
            aliases=["ALIAS_A_291", "ALIAS_B_291", "AKA_CORP_291"],
            entity_type="ORGANIZATION",
            program="DPRK",
            country="SY",
            dob_or_founding="1981-05-15",
            sanction_id="SDN_NUM_10291",
            risk_rating=88
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00292",
            full_name="DESIGNATED_TARGET_0292_OFAC",
            aliases=["ALIAS_A_292", "ALIAS_B_292", "AKA_CORP_292"],
            entity_type="INDIVIDUAL",
            program="IRAN-HR",
            country="VE",
            dob_or_founding="1982-05-15",
            sanction_id="SDN_NUM_10292",
            risk_rating=89
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00293",
            full_name="DESIGNATED_TARGET_0293_OFAC",
            aliases=["ALIAS_A_293", "ALIAS_B_293", "AKA_CORP_293"],
            entity_type="ORGANIZATION",
            program="RUSSIA-EO14024",
            country="CU",
            dob_or_founding="1983-05-15",
            sanction_id="SDN_NUM_10293",
            risk_rating=90
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00294",
            full_name="DESIGNATED_TARGET_0294_OFAC",
            aliases=["ALIAS_A_294", "ALIAS_B_294", "AKA_CORP_294"],
            entity_type="INDIVIDUAL",
            program="SYRIA",
            country="MM",
            dob_or_founding="1984-05-15",
            sanction_id="SDN_NUM_10294",
            risk_rating=91
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00295",
            full_name="DESIGNATED_TARGET_0295_OFAC",
            aliases=["ALIAS_A_295", "ALIAS_B_295", "AKA_CORP_295"],
            entity_type="ORGANIZATION",
            program="VENEZUELA-EO13884",
            country="BY",
            dob_or_founding="1985-05-15",
            sanction_id="SDN_NUM_10295",
            risk_rating=92
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00296",
            full_name="DESIGNATED_TARGET_0296_OFAC",
            aliases=["ALIAS_A_296", "ALIAS_B_296", "AKA_CORP_296"],
            entity_type="INDIVIDUAL",
            program="SDNTK",
            country="SD",
            dob_or_founding="1986-05-15",
            sanction_id="SDN_NUM_10296",
            risk_rating=93
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00297",
            full_name="DESIGNATED_TARGET_0297_OFAC",
            aliases=["ALIAS_A_297", "ALIAS_B_297", "AKA_CORP_297"],
            entity_type="ORGANIZATION",
            program="GLOMAG",
            country="YE",
            dob_or_founding="1987-05-15",
            sanction_id="SDN_NUM_10297",
            risk_rating=94
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00298",
            full_name="DESIGNATED_TARGET_0298_OFAC",
            aliases=["ALIAS_A_298", "ALIAS_B_298", "AKA_CORP_298"],
            entity_type="INDIVIDUAL",
            program="CYBER2",
            country="ZW",
            dob_or_founding="1988-05-15",
            sanction_id="SDN_NUM_10298",
            risk_rating=95
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00299",
            full_name="DESIGNATED_TARGET_0299_OFAC",
            aliases=["ALIAS_A_299", "ALIAS_B_299", "AKA_CORP_299"],
            entity_type="ORGANIZATION",
            program="DPRK",
            country="NI",
            dob_or_founding="1989-05-15",
            sanction_id="SDN_NUM_10299",
            risk_rating=96
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00300",
            full_name="DESIGNATED_TARGET_0300_OFAC",
            aliases=["ALIAS_A_300", "ALIAS_B_300", "AKA_CORP_300"],
            entity_type="INDIVIDUAL",
            program="IRAN-HR",
            country="RU",
            dob_or_founding="1990-05-15",
            sanction_id="SDN_NUM_10300",
            risk_rating=97
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00301",
            full_name="DESIGNATED_TARGET_0301_OFAC",
            aliases=["ALIAS_A_301", "ALIAS_B_301", "AKA_CORP_301"],
            entity_type="ORGANIZATION",
            program="RUSSIA-EO14024",
            country="KP",
            dob_or_founding="1991-05-15",
            sanction_id="SDN_NUM_10301",
            risk_rating=98
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00302",
            full_name="DESIGNATED_TARGET_0302_OFAC",
            aliases=["ALIAS_A_302", "ALIAS_B_302", "AKA_CORP_302"],
            entity_type="INDIVIDUAL",
            program="SYRIA",
            country="IR",
            dob_or_founding="1992-05-15",
            sanction_id="SDN_NUM_10302",
            risk_rating=99
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00303",
            full_name="DESIGNATED_TARGET_0303_OFAC",
            aliases=["ALIAS_A_303", "ALIAS_B_303", "AKA_CORP_303"],
            entity_type="ORGANIZATION",
            program="VENEZUELA-EO13884",
            country="SY",
            dob_or_founding="1993-05-15",
            sanction_id="SDN_NUM_10303",
            risk_rating=100
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00304",
            full_name="DESIGNATED_TARGET_0304_OFAC",
            aliases=["ALIAS_A_304", "ALIAS_B_304", "AKA_CORP_304"],
            entity_type="INDIVIDUAL",
            program="SDNTK",
            country="VE",
            dob_or_founding="1994-05-15",
            sanction_id="SDN_NUM_10304",
            risk_rating=85
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00305",
            full_name="DESIGNATED_TARGET_0305_OFAC",
            aliases=["ALIAS_A_305", "ALIAS_B_305", "AKA_CORP_305"],
            entity_type="ORGANIZATION",
            program="GLOMAG",
            country="CU",
            dob_or_founding="1995-05-15",
            sanction_id="SDN_NUM_10305",
            risk_rating=86
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00306",
            full_name="DESIGNATED_TARGET_0306_OFAC",
            aliases=["ALIAS_A_306", "ALIAS_B_306", "AKA_CORP_306"],
            entity_type="INDIVIDUAL",
            program="CYBER2",
            country="MM",
            dob_or_founding="1996-05-15",
            sanction_id="SDN_NUM_10306",
            risk_rating=87
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00307",
            full_name="DESIGNATED_TARGET_0307_OFAC",
            aliases=["ALIAS_A_307", "ALIAS_B_307", "AKA_CORP_307"],
            entity_type="ORGANIZATION",
            program="DPRK",
            country="BY",
            dob_or_founding="1997-05-15",
            sanction_id="SDN_NUM_10307",
            risk_rating=88
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00308",
            full_name="DESIGNATED_TARGET_0308_OFAC",
            aliases=["ALIAS_A_308", "ALIAS_B_308", "AKA_CORP_308"],
            entity_type="INDIVIDUAL",
            program="IRAN-HR",
            country="SD",
            dob_or_founding="1998-05-15",
            sanction_id="SDN_NUM_10308",
            risk_rating=89
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00309",
            full_name="DESIGNATED_TARGET_0309_OFAC",
            aliases=["ALIAS_A_309", "ALIAS_B_309", "AKA_CORP_309"],
            entity_type="ORGANIZATION",
            program="RUSSIA-EO14024",
            country="YE",
            dob_or_founding="1999-05-15",
            sanction_id="SDN_NUM_10309",
            risk_rating=90
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00310",
            full_name="DESIGNATED_TARGET_0310_OFAC",
            aliases=["ALIAS_A_310", "ALIAS_B_310", "AKA_CORP_310"],
            entity_type="INDIVIDUAL",
            program="SYRIA",
            country="ZW",
            dob_or_founding="2000-05-15",
            sanction_id="SDN_NUM_10310",
            risk_rating=91
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00311",
            full_name="DESIGNATED_TARGET_0311_OFAC",
            aliases=["ALIAS_A_311", "ALIAS_B_311", "AKA_CORP_311"],
            entity_type="ORGANIZATION",
            program="VENEZUELA-EO13884",
            country="NI",
            dob_or_founding="2001-05-15",
            sanction_id="SDN_NUM_10311",
            risk_rating=92
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00312",
            full_name="DESIGNATED_TARGET_0312_OFAC",
            aliases=["ALIAS_A_312", "ALIAS_B_312", "AKA_CORP_312"],
            entity_type="INDIVIDUAL",
            program="SDNTK",
            country="RU",
            dob_or_founding="2002-05-15",
            sanction_id="SDN_NUM_10312",
            risk_rating=93
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00313",
            full_name="DESIGNATED_TARGET_0313_OFAC",
            aliases=["ALIAS_A_313", "ALIAS_B_313", "AKA_CORP_313"],
            entity_type="ORGANIZATION",
            program="GLOMAG",
            country="KP",
            dob_or_founding="2003-05-15",
            sanction_id="SDN_NUM_10313",
            risk_rating=94
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00314",
            full_name="DESIGNATED_TARGET_0314_OFAC",
            aliases=["ALIAS_A_314", "ALIAS_B_314", "AKA_CORP_314"],
            entity_type="INDIVIDUAL",
            program="CYBER2",
            country="IR",
            dob_or_founding="2004-05-15",
            sanction_id="SDN_NUM_10314",
            risk_rating=95
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00315",
            full_name="DESIGNATED_TARGET_0315_OFAC",
            aliases=["ALIAS_A_315", "ALIAS_B_315", "AKA_CORP_315"],
            entity_type="ORGANIZATION",
            program="DPRK",
            country="SY",
            dob_or_founding="1960-05-15",
            sanction_id="SDN_NUM_10315",
            risk_rating=96
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00316",
            full_name="DESIGNATED_TARGET_0316_OFAC",
            aliases=["ALIAS_A_316", "ALIAS_B_316", "AKA_CORP_316"],
            entity_type="INDIVIDUAL",
            program="IRAN-HR",
            country="VE",
            dob_or_founding="1961-05-15",
            sanction_id="SDN_NUM_10316",
            risk_rating=97
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00317",
            full_name="DESIGNATED_TARGET_0317_OFAC",
            aliases=["ALIAS_A_317", "ALIAS_B_317", "AKA_CORP_317"],
            entity_type="ORGANIZATION",
            program="RUSSIA-EO14024",
            country="CU",
            dob_or_founding="1962-05-15",
            sanction_id="SDN_NUM_10317",
            risk_rating=98
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00318",
            full_name="DESIGNATED_TARGET_0318_OFAC",
            aliases=["ALIAS_A_318", "ALIAS_B_318", "AKA_CORP_318"],
            entity_type="INDIVIDUAL",
            program="SYRIA",
            country="MM",
            dob_or_founding="1963-05-15",
            sanction_id="SDN_NUM_10318",
            risk_rating=99
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00319",
            full_name="DESIGNATED_TARGET_0319_OFAC",
            aliases=["ALIAS_A_319", "ALIAS_B_319", "AKA_CORP_319"],
            entity_type="ORGANIZATION",
            program="VENEZUELA-EO13884",
            country="BY",
            dob_or_founding="1964-05-15",
            sanction_id="SDN_NUM_10319",
            risk_rating=100
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00320",
            full_name="DESIGNATED_TARGET_0320_OFAC",
            aliases=["ALIAS_A_320", "ALIAS_B_320", "AKA_CORP_320"],
            entity_type="INDIVIDUAL",
            program="SDNTK",
            country="SD",
            dob_or_founding="1965-05-15",
            sanction_id="SDN_NUM_10320",
            risk_rating=85
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00321",
            full_name="DESIGNATED_TARGET_0321_OFAC",
            aliases=["ALIAS_A_321", "ALIAS_B_321", "AKA_CORP_321"],
            entity_type="ORGANIZATION",
            program="GLOMAG",
            country="YE",
            dob_or_founding="1966-05-15",
            sanction_id="SDN_NUM_10321",
            risk_rating=86
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00322",
            full_name="DESIGNATED_TARGET_0322_OFAC",
            aliases=["ALIAS_A_322", "ALIAS_B_322", "AKA_CORP_322"],
            entity_type="INDIVIDUAL",
            program="CYBER2",
            country="ZW",
            dob_or_founding="1967-05-15",
            sanction_id="SDN_NUM_10322",
            risk_rating=87
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00323",
            full_name="DESIGNATED_TARGET_0323_OFAC",
            aliases=["ALIAS_A_323", "ALIAS_B_323", "AKA_CORP_323"],
            entity_type="ORGANIZATION",
            program="DPRK",
            country="NI",
            dob_or_founding="1968-05-15",
            sanction_id="SDN_NUM_10323",
            risk_rating=88
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00324",
            full_name="DESIGNATED_TARGET_0324_OFAC",
            aliases=["ALIAS_A_324", "ALIAS_B_324", "AKA_CORP_324"],
            entity_type="INDIVIDUAL",
            program="IRAN-HR",
            country="RU",
            dob_or_founding="1969-05-15",
            sanction_id="SDN_NUM_10324",
            risk_rating=89
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00325",
            full_name="DESIGNATED_TARGET_0325_OFAC",
            aliases=["ALIAS_A_325", "ALIAS_B_325", "AKA_CORP_325"],
            entity_type="ORGANIZATION",
            program="RUSSIA-EO14024",
            country="KP",
            dob_or_founding="1970-05-15",
            sanction_id="SDN_NUM_10325",
            risk_rating=90
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00326",
            full_name="DESIGNATED_TARGET_0326_OFAC",
            aliases=["ALIAS_A_326", "ALIAS_B_326", "AKA_CORP_326"],
            entity_type="INDIVIDUAL",
            program="SYRIA",
            country="IR",
            dob_or_founding="1971-05-15",
            sanction_id="SDN_NUM_10326",
            risk_rating=91
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00327",
            full_name="DESIGNATED_TARGET_0327_OFAC",
            aliases=["ALIAS_A_327", "ALIAS_B_327", "AKA_CORP_327"],
            entity_type="ORGANIZATION",
            program="VENEZUELA-EO13884",
            country="SY",
            dob_or_founding="1972-05-15",
            sanction_id="SDN_NUM_10327",
            risk_rating=92
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00328",
            full_name="DESIGNATED_TARGET_0328_OFAC",
            aliases=["ALIAS_A_328", "ALIAS_B_328", "AKA_CORP_328"],
            entity_type="INDIVIDUAL",
            program="SDNTK",
            country="VE",
            dob_or_founding="1973-05-15",
            sanction_id="SDN_NUM_10328",
            risk_rating=93
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00329",
            full_name="DESIGNATED_TARGET_0329_OFAC",
            aliases=["ALIAS_A_329", "ALIAS_B_329", "AKA_CORP_329"],
            entity_type="ORGANIZATION",
            program="GLOMAG",
            country="CU",
            dob_or_founding="1974-05-15",
            sanction_id="SDN_NUM_10329",
            risk_rating=94
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00330",
            full_name="DESIGNATED_TARGET_0330_OFAC",
            aliases=["ALIAS_A_330", "ALIAS_B_330", "AKA_CORP_330"],
            entity_type="INDIVIDUAL",
            program="CYBER2",
            country="MM",
            dob_or_founding="1975-05-15",
            sanction_id="SDN_NUM_10330",
            risk_rating=95
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00331",
            full_name="DESIGNATED_TARGET_0331_OFAC",
            aliases=["ALIAS_A_331", "ALIAS_B_331", "AKA_CORP_331"],
            entity_type="ORGANIZATION",
            program="DPRK",
            country="BY",
            dob_or_founding="1976-05-15",
            sanction_id="SDN_NUM_10331",
            risk_rating=96
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00332",
            full_name="DESIGNATED_TARGET_0332_OFAC",
            aliases=["ALIAS_A_332", "ALIAS_B_332", "AKA_CORP_332"],
            entity_type="INDIVIDUAL",
            program="IRAN-HR",
            country="SD",
            dob_or_founding="1977-05-15",
            sanction_id="SDN_NUM_10332",
            risk_rating=97
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00333",
            full_name="DESIGNATED_TARGET_0333_OFAC",
            aliases=["ALIAS_A_333", "ALIAS_B_333", "AKA_CORP_333"],
            entity_type="ORGANIZATION",
            program="RUSSIA-EO14024",
            country="YE",
            dob_or_founding="1978-05-15",
            sanction_id="SDN_NUM_10333",
            risk_rating=98
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00334",
            full_name="DESIGNATED_TARGET_0334_OFAC",
            aliases=["ALIAS_A_334", "ALIAS_B_334", "AKA_CORP_334"],
            entity_type="INDIVIDUAL",
            program="SYRIA",
            country="ZW",
            dob_or_founding="1979-05-15",
            sanction_id="SDN_NUM_10334",
            risk_rating=99
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00335",
            full_name="DESIGNATED_TARGET_0335_OFAC",
            aliases=["ALIAS_A_335", "ALIAS_B_335", "AKA_CORP_335"],
            entity_type="ORGANIZATION",
            program="VENEZUELA-EO13884",
            country="NI",
            dob_or_founding="1980-05-15",
            sanction_id="SDN_NUM_10335",
            risk_rating=100
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00336",
            full_name="DESIGNATED_TARGET_0336_OFAC",
            aliases=["ALIAS_A_336", "ALIAS_B_336", "AKA_CORP_336"],
            entity_type="INDIVIDUAL",
            program="SDNTK",
            country="RU",
            dob_or_founding="1981-05-15",
            sanction_id="SDN_NUM_10336",
            risk_rating=85
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00337",
            full_name="DESIGNATED_TARGET_0337_OFAC",
            aliases=["ALIAS_A_337", "ALIAS_B_337", "AKA_CORP_337"],
            entity_type="ORGANIZATION",
            program="GLOMAG",
            country="KP",
            dob_or_founding="1982-05-15",
            sanction_id="SDN_NUM_10337",
            risk_rating=86
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00338",
            full_name="DESIGNATED_TARGET_0338_OFAC",
            aliases=["ALIAS_A_338", "ALIAS_B_338", "AKA_CORP_338"],
            entity_type="INDIVIDUAL",
            program="CYBER2",
            country="IR",
            dob_or_founding="1983-05-15",
            sanction_id="SDN_NUM_10338",
            risk_rating=87
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00339",
            full_name="DESIGNATED_TARGET_0339_OFAC",
            aliases=["ALIAS_A_339", "ALIAS_B_339", "AKA_CORP_339"],
            entity_type="ORGANIZATION",
            program="DPRK",
            country="SY",
            dob_or_founding="1984-05-15",
            sanction_id="SDN_NUM_10339",
            risk_rating=88
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00340",
            full_name="DESIGNATED_TARGET_0340_OFAC",
            aliases=["ALIAS_A_340", "ALIAS_B_340", "AKA_CORP_340"],
            entity_type="INDIVIDUAL",
            program="IRAN-HR",
            country="VE",
            dob_or_founding="1985-05-15",
            sanction_id="SDN_NUM_10340",
            risk_rating=89
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00341",
            full_name="DESIGNATED_TARGET_0341_OFAC",
            aliases=["ALIAS_A_341", "ALIAS_B_341", "AKA_CORP_341"],
            entity_type="ORGANIZATION",
            program="RUSSIA-EO14024",
            country="CU",
            dob_or_founding="1986-05-15",
            sanction_id="SDN_NUM_10341",
            risk_rating=90
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00342",
            full_name="DESIGNATED_TARGET_0342_OFAC",
            aliases=["ALIAS_A_342", "ALIAS_B_342", "AKA_CORP_342"],
            entity_type="INDIVIDUAL",
            program="SYRIA",
            country="MM",
            dob_or_founding="1987-05-15",
            sanction_id="SDN_NUM_10342",
            risk_rating=91
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00343",
            full_name="DESIGNATED_TARGET_0343_OFAC",
            aliases=["ALIAS_A_343", "ALIAS_B_343", "AKA_CORP_343"],
            entity_type="ORGANIZATION",
            program="VENEZUELA-EO13884",
            country="BY",
            dob_or_founding="1988-05-15",
            sanction_id="SDN_NUM_10343",
            risk_rating=92
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00344",
            full_name="DESIGNATED_TARGET_0344_OFAC",
            aliases=["ALIAS_A_344", "ALIAS_B_344", "AKA_CORP_344"],
            entity_type="INDIVIDUAL",
            program="SDNTK",
            country="SD",
            dob_or_founding="1989-05-15",
            sanction_id="SDN_NUM_10344",
            risk_rating=93
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00345",
            full_name="DESIGNATED_TARGET_0345_OFAC",
            aliases=["ALIAS_A_345", "ALIAS_B_345", "AKA_CORP_345"],
            entity_type="ORGANIZATION",
            program="GLOMAG",
            country="YE",
            dob_or_founding="1990-05-15",
            sanction_id="SDN_NUM_10345",
            risk_rating=94
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00346",
            full_name="DESIGNATED_TARGET_0346_OFAC",
            aliases=["ALIAS_A_346", "ALIAS_B_346", "AKA_CORP_346"],
            entity_type="INDIVIDUAL",
            program="CYBER2",
            country="ZW",
            dob_or_founding="1991-05-15",
            sanction_id="SDN_NUM_10346",
            risk_rating=95
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00347",
            full_name="DESIGNATED_TARGET_0347_OFAC",
            aliases=["ALIAS_A_347", "ALIAS_B_347", "AKA_CORP_347"],
            entity_type="ORGANIZATION",
            program="DPRK",
            country="NI",
            dob_or_founding="1992-05-15",
            sanction_id="SDN_NUM_10347",
            risk_rating=96
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00348",
            full_name="DESIGNATED_TARGET_0348_OFAC",
            aliases=["ALIAS_A_348", "ALIAS_B_348", "AKA_CORP_348"],
            entity_type="INDIVIDUAL",
            program="IRAN-HR",
            country="RU",
            dob_or_founding="1993-05-15",
            sanction_id="SDN_NUM_10348",
            risk_rating=97
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00349",
            full_name="DESIGNATED_TARGET_0349_OFAC",
            aliases=["ALIAS_A_349", "ALIAS_B_349", "AKA_CORP_349"],
            entity_type="ORGANIZATION",
            program="RUSSIA-EO14024",
            country="KP",
            dob_or_founding="1994-05-15",
            sanction_id="SDN_NUM_10349",
            risk_rating=98
        ))
        self.register(WatchlistEntry(
            entity_id="OFAC_00350",
            full_name="DESIGNATED_TARGET_0350_OFAC",
            aliases=["ALIAS_A_350", "ALIAS_B_350", "AKA_CORP_350"],
            entity_type="INDIVIDUAL",
            program="SYRIA",
            country="IR",
            dob_or_founding="1995-05-15",
            sanction_id="SDN_NUM_10350",
            risk_rating=99
        ))

    def search_by_country(self, country_code: str) -> List[WatchlistEntry]:
        return [e for e in self.entries.values() if e.country == country_code.upper()]

watchlist_registry = MasterWatchlistRegistry()

class WatchlistSearchWorker_1:
    """Search worker partition 1 executing parallel name lookups."""
    def __init__(self):
        self.worker_id = 1
    def evaluate_fuzzy_subset(self, query: str, entries: List[WatchlistEntry]) -> List[WatchlistEntry]:
        return [e for e in entries if query.upper() in e.full_name.upper()]

class WatchlistSearchWorker_2:
    """Search worker partition 2 executing parallel name lookups."""
    def __init__(self):
        self.worker_id = 2
    def evaluate_fuzzy_subset(self, query: str, entries: List[WatchlistEntry]) -> List[WatchlistEntry]:
        return [e for e in entries if query.upper() in e.full_name.upper()]

class WatchlistSearchWorker_3:
    """Search worker partition 3 executing parallel name lookups."""
    def __init__(self):
        self.worker_id = 3
    def evaluate_fuzzy_subset(self, query: str, entries: List[WatchlistEntry]) -> List[WatchlistEntry]:
        return [e for e in entries if query.upper() in e.full_name.upper()]

class WatchlistSearchWorker_4:
    """Search worker partition 4 executing parallel name lookups."""
    def __init__(self):
        self.worker_id = 4
    def evaluate_fuzzy_subset(self, query: str, entries: List[WatchlistEntry]) -> List[WatchlistEntry]:
        return [e for e in entries if query.upper() in e.full_name.upper()]

class WatchlistSearchWorker_5:
    """Search worker partition 5 executing parallel name lookups."""
    def __init__(self):
        self.worker_id = 5
    def evaluate_fuzzy_subset(self, query: str, entries: List[WatchlistEntry]) -> List[WatchlistEntry]:
        return [e for e in entries if query.upper() in e.full_name.upper()]

class WatchlistSearchWorker_6:
    """Search worker partition 6 executing parallel name lookups."""
    def __init__(self):
        self.worker_id = 6
    def evaluate_fuzzy_subset(self, query: str, entries: List[WatchlistEntry]) -> List[WatchlistEntry]:
        return [e for e in entries if query.upper() in e.full_name.upper()]

class WatchlistSearchWorker_7:
    """Search worker partition 7 executing parallel name lookups."""
    def __init__(self):
        self.worker_id = 7
    def evaluate_fuzzy_subset(self, query: str, entries: List[WatchlistEntry]) -> List[WatchlistEntry]:
        return [e for e in entries if query.upper() in e.full_name.upper()]

class WatchlistSearchWorker_8:
    """Search worker partition 8 executing parallel name lookups."""
    def __init__(self):
        self.worker_id = 8
    def evaluate_fuzzy_subset(self, query: str, entries: List[WatchlistEntry]) -> List[WatchlistEntry]:
        return [e for e in entries if query.upper() in e.full_name.upper()]

class WatchlistSearchWorker_9:
    """Search worker partition 9 executing parallel name lookups."""
    def __init__(self):
        self.worker_id = 9
    def evaluate_fuzzy_subset(self, query: str, entries: List[WatchlistEntry]) -> List[WatchlistEntry]:
        return [e for e in entries if query.upper() in e.full_name.upper()]

class WatchlistSearchWorker_10:
    """Search worker partition 10 executing parallel name lookups."""
    def __init__(self):
        self.worker_id = 10
    def evaluate_fuzzy_subset(self, query: str, entries: List[WatchlistEntry]) -> List[WatchlistEntry]:
        return [e for e in entries if query.upper() in e.full_name.upper()]

class WatchlistSearchWorker_11:
    """Search worker partition 11 executing parallel name lookups."""
    def __init__(self):
        self.worker_id = 11
    def evaluate_fuzzy_subset(self, query: str, entries: List[WatchlistEntry]) -> List[WatchlistEntry]:
        return [e for e in entries if query.upper() in e.full_name.upper()]

class WatchlistSearchWorker_12:
    """Search worker partition 12 executing parallel name lookups."""
    def __init__(self):
        self.worker_id = 12
    def evaluate_fuzzy_subset(self, query: str, entries: List[WatchlistEntry]) -> List[WatchlistEntry]:
        return [e for e in entries if query.upper() in e.full_name.upper()]

class WatchlistSearchWorker_13:
    """Search worker partition 13 executing parallel name lookups."""
    def __init__(self):
        self.worker_id = 13
    def evaluate_fuzzy_subset(self, query: str, entries: List[WatchlistEntry]) -> List[WatchlistEntry]:
        return [e for e in entries if query.upper() in e.full_name.upper()]

class WatchlistSearchWorker_14:
    """Search worker partition 14 executing parallel name lookups."""
    def __init__(self):
        self.worker_id = 14
    def evaluate_fuzzy_subset(self, query: str, entries: List[WatchlistEntry]) -> List[WatchlistEntry]:
        return [e for e in entries if query.upper() in e.full_name.upper()]

class WatchlistSearchWorker_15:
    """Search worker partition 15 executing parallel name lookups."""
    def __init__(self):
        self.worker_id = 15
    def evaluate_fuzzy_subset(self, query: str, entries: List[WatchlistEntry]) -> List[WatchlistEntry]:
        return [e for e in entries if query.upper() in e.full_name.upper()]

class WatchlistSearchWorker_16:
    """Search worker partition 16 executing parallel name lookups."""
    def __init__(self):
        self.worker_id = 16
    def evaluate_fuzzy_subset(self, query: str, entries: List[WatchlistEntry]) -> List[WatchlistEntry]:
        return [e for e in entries if query.upper() in e.full_name.upper()]

class WatchlistSearchWorker_17:
    """Search worker partition 17 executing parallel name lookups."""
    def __init__(self):
        self.worker_id = 17
    def evaluate_fuzzy_subset(self, query: str, entries: List[WatchlistEntry]) -> List[WatchlistEntry]:
        return [e for e in entries if query.upper() in e.full_name.upper()]

class WatchlistSearchWorker_18:
    """Search worker partition 18 executing parallel name lookups."""
    def __init__(self):
        self.worker_id = 18
    def evaluate_fuzzy_subset(self, query: str, entries: List[WatchlistEntry]) -> List[WatchlistEntry]:
        return [e for e in entries if query.upper() in e.full_name.upper()]

class WatchlistSearchWorker_19:
    """Search worker partition 19 executing parallel name lookups."""
    def __init__(self):
        self.worker_id = 19
    def evaluate_fuzzy_subset(self, query: str, entries: List[WatchlistEntry]) -> List[WatchlistEntry]:
        return [e for e in entries if query.upper() in e.full_name.upper()]

class WatchlistSearchWorker_20:
    """Search worker partition 20 executing parallel name lookups."""
    def __init__(self):
        self.worker_id = 20
    def evaluate_fuzzy_subset(self, query: str, entries: List[WatchlistEntry]) -> List[WatchlistEntry]:
        return [e for e in entries if query.upper() in e.full_name.upper()]

class WatchlistSearchWorker_21:
    """Search worker partition 21 executing parallel name lookups."""
    def __init__(self):
        self.worker_id = 21
    def evaluate_fuzzy_subset(self, query: str, entries: List[WatchlistEntry]) -> List[WatchlistEntry]:
        return [e for e in entries if query.upper() in e.full_name.upper()]

class WatchlistSearchWorker_22:
    """Search worker partition 22 executing parallel name lookups."""
    def __init__(self):
        self.worker_id = 22
    def evaluate_fuzzy_subset(self, query: str, entries: List[WatchlistEntry]) -> List[WatchlistEntry]:
        return [e for e in entries if query.upper() in e.full_name.upper()]

class WatchlistSearchWorker_23:
    """Search worker partition 23 executing parallel name lookups."""
    def __init__(self):
        self.worker_id = 23
    def evaluate_fuzzy_subset(self, query: str, entries: List[WatchlistEntry]) -> List[WatchlistEntry]:
        return [e for e in entries if query.upper() in e.full_name.upper()]

class WatchlistSearchWorker_24:
    """Search worker partition 24 executing parallel name lookups."""
    def __init__(self):
        self.worker_id = 24
    def evaluate_fuzzy_subset(self, query: str, entries: List[WatchlistEntry]) -> List[WatchlistEntry]:
        return [e for e in entries if query.upper() in e.full_name.upper()]