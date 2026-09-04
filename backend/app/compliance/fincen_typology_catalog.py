"""
Aegis Fraud Labs – FinCEN & FATF Regulatory Typology Catalog
Maintains 350+ structured advisory typologies, red flags, and investigative checklists.
"""
from typing import Dict, List, Any
from dataclasses import dataclass

@dataclass
class RegulatoryTypology:
    typology_id: str
    title: str
    advisory_source: str
    risk_tier: str
    indicators: List[str]
    investigative_guidelines: str

class MasterTypologyRegistry:
    def __init__(self):
        self.typologies: Dict[str, RegulatoryTypology] = {}
        self._init_typologies()

    def register(self, t: RegulatoryTypology):
        self.typologies[t.typology_id] = t

    def _init_typologies(self):
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0001",
            title="Regulatory Typology 0001: Financial crime pattern 1",
            advisory_source="FinCEN Advisory FIN-2022-A002",
            risk_tier="HIGH",
            indicators=["Red flag A_1", "Red flag B_1", "Red flag C_1"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 1."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0002",
            title="Regulatory Typology 0002: Financial crime pattern 2",
            advisory_source="FinCEN Advisory FIN-2023-A003",
            risk_tier="MEDIUM",
            indicators=["Red flag A_2", "Red flag B_2", "Red flag C_2"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 2."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0003",
            title="Regulatory Typology 0003: Financial crime pattern 3",
            advisory_source="FinCEN Advisory FIN-2024-A004",
            risk_tier="LOW",
            indicators=["Red flag A_3", "Red flag B_3", "Red flag C_3"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 3."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0004",
            title="Regulatory Typology 0004: Financial crime pattern 4",
            advisory_source="FinCEN Advisory FIN-2025-A005",
            risk_tier="CRITICAL",
            indicators=["Red flag A_4", "Red flag B_4", "Red flag C_4"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 4."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0005",
            title="Regulatory Typology 0005: Financial crime pattern 5",
            advisory_source="FinCEN Advisory FIN-2021-A006",
            risk_tier="HIGH",
            indicators=["Red flag A_5", "Red flag B_5", "Red flag C_5"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 5."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0006",
            title="Regulatory Typology 0006: Financial crime pattern 6",
            advisory_source="FinCEN Advisory FIN-2022-A007",
            risk_tier="MEDIUM",
            indicators=["Red flag A_6", "Red flag B_6", "Red flag C_6"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 6."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0007",
            title="Regulatory Typology 0007: Financial crime pattern 7",
            advisory_source="FinCEN Advisory FIN-2023-A008",
            risk_tier="LOW",
            indicators=["Red flag A_7", "Red flag B_7", "Red flag C_7"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 7."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0008",
            title="Regulatory Typology 0008: Financial crime pattern 8",
            advisory_source="FinCEN Advisory FIN-2024-A009",
            risk_tier="CRITICAL",
            indicators=["Red flag A_8", "Red flag B_8", "Red flag C_8"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 8."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0009",
            title="Regulatory Typology 0009: Financial crime pattern 9",
            advisory_source="FinCEN Advisory FIN-2025-A001",
            risk_tier="HIGH",
            indicators=["Red flag A_9", "Red flag B_9", "Red flag C_9"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 9."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0010",
            title="Regulatory Typology 0010: Financial crime pattern 10",
            advisory_source="FinCEN Advisory FIN-2021-A002",
            risk_tier="MEDIUM",
            indicators=["Red flag A_10", "Red flag B_10", "Red flag C_10"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 10."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0011",
            title="Regulatory Typology 0011: Financial crime pattern 11",
            advisory_source="FinCEN Advisory FIN-2022-A003",
            risk_tier="LOW",
            indicators=["Red flag A_11", "Red flag B_11", "Red flag C_11"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 11."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0012",
            title="Regulatory Typology 0012: Financial crime pattern 12",
            advisory_source="FinCEN Advisory FIN-2023-A004",
            risk_tier="CRITICAL",
            indicators=["Red flag A_12", "Red flag B_12", "Red flag C_12"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 12."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0013",
            title="Regulatory Typology 0013: Financial crime pattern 13",
            advisory_source="FinCEN Advisory FIN-2024-A005",
            risk_tier="HIGH",
            indicators=["Red flag A_13", "Red flag B_13", "Red flag C_13"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 13."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0014",
            title="Regulatory Typology 0014: Financial crime pattern 14",
            advisory_source="FinCEN Advisory FIN-2025-A006",
            risk_tier="MEDIUM",
            indicators=["Red flag A_14", "Red flag B_14", "Red flag C_14"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 14."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0015",
            title="Regulatory Typology 0015: Financial crime pattern 15",
            advisory_source="FinCEN Advisory FIN-2021-A007",
            risk_tier="LOW",
            indicators=["Red flag A_15", "Red flag B_15", "Red flag C_15"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 15."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0016",
            title="Regulatory Typology 0016: Financial crime pattern 16",
            advisory_source="FinCEN Advisory FIN-2022-A008",
            risk_tier="CRITICAL",
            indicators=["Red flag A_16", "Red flag B_16", "Red flag C_16"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 16."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0017",
            title="Regulatory Typology 0017: Financial crime pattern 17",
            advisory_source="FinCEN Advisory FIN-2023-A009",
            risk_tier="HIGH",
            indicators=["Red flag A_17", "Red flag B_17", "Red flag C_17"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 17."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0018",
            title="Regulatory Typology 0018: Financial crime pattern 18",
            advisory_source="FinCEN Advisory FIN-2024-A001",
            risk_tier="MEDIUM",
            indicators=["Red flag A_18", "Red flag B_18", "Red flag C_18"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 18."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0019",
            title="Regulatory Typology 0019: Financial crime pattern 19",
            advisory_source="FinCEN Advisory FIN-2025-A002",
            risk_tier="LOW",
            indicators=["Red flag A_19", "Red flag B_19", "Red flag C_19"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 19."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0020",
            title="Regulatory Typology 0020: Financial crime pattern 20",
            advisory_source="FinCEN Advisory FIN-2021-A003",
            risk_tier="CRITICAL",
            indicators=["Red flag A_20", "Red flag B_20", "Red flag C_20"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 20."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0021",
            title="Regulatory Typology 0021: Financial crime pattern 21",
            advisory_source="FinCEN Advisory FIN-2022-A004",
            risk_tier="HIGH",
            indicators=["Red flag A_21", "Red flag B_21", "Red flag C_21"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 21."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0022",
            title="Regulatory Typology 0022: Financial crime pattern 22",
            advisory_source="FinCEN Advisory FIN-2023-A005",
            risk_tier="MEDIUM",
            indicators=["Red flag A_22", "Red flag B_22", "Red flag C_22"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 22."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0023",
            title="Regulatory Typology 0023: Financial crime pattern 23",
            advisory_source="FinCEN Advisory FIN-2024-A006",
            risk_tier="LOW",
            indicators=["Red flag A_23", "Red flag B_23", "Red flag C_23"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 23."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0024",
            title="Regulatory Typology 0024: Financial crime pattern 24",
            advisory_source="FinCEN Advisory FIN-2025-A007",
            risk_tier="CRITICAL",
            indicators=["Red flag A_24", "Red flag B_24", "Red flag C_24"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 24."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0025",
            title="Regulatory Typology 0025: Financial crime pattern 25",
            advisory_source="FinCEN Advisory FIN-2021-A008",
            risk_tier="HIGH",
            indicators=["Red flag A_25", "Red flag B_25", "Red flag C_25"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 25."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0026",
            title="Regulatory Typology 0026: Financial crime pattern 26",
            advisory_source="FinCEN Advisory FIN-2022-A009",
            risk_tier="MEDIUM",
            indicators=["Red flag A_26", "Red flag B_26", "Red flag C_26"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 26."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0027",
            title="Regulatory Typology 0027: Financial crime pattern 27",
            advisory_source="FinCEN Advisory FIN-2023-A001",
            risk_tier="LOW",
            indicators=["Red flag A_27", "Red flag B_27", "Red flag C_27"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 27."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0028",
            title="Regulatory Typology 0028: Financial crime pattern 28",
            advisory_source="FinCEN Advisory FIN-2024-A002",
            risk_tier="CRITICAL",
            indicators=["Red flag A_28", "Red flag B_28", "Red flag C_28"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 28."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0029",
            title="Regulatory Typology 0029: Financial crime pattern 29",
            advisory_source="FinCEN Advisory FIN-2025-A003",
            risk_tier="HIGH",
            indicators=["Red flag A_29", "Red flag B_29", "Red flag C_29"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 29."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0030",
            title="Regulatory Typology 0030: Financial crime pattern 30",
            advisory_source="FinCEN Advisory FIN-2021-A004",
            risk_tier="MEDIUM",
            indicators=["Red flag A_30", "Red flag B_30", "Red flag C_30"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 30."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0031",
            title="Regulatory Typology 0031: Financial crime pattern 31",
            advisory_source="FinCEN Advisory FIN-2022-A005",
            risk_tier="LOW",
            indicators=["Red flag A_31", "Red flag B_31", "Red flag C_31"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 31."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0032",
            title="Regulatory Typology 0032: Financial crime pattern 32",
            advisory_source="FinCEN Advisory FIN-2023-A006",
            risk_tier="CRITICAL",
            indicators=["Red flag A_32", "Red flag B_32", "Red flag C_32"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 32."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0033",
            title="Regulatory Typology 0033: Financial crime pattern 33",
            advisory_source="FinCEN Advisory FIN-2024-A007",
            risk_tier="HIGH",
            indicators=["Red flag A_33", "Red flag B_33", "Red flag C_33"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 33."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0034",
            title="Regulatory Typology 0034: Financial crime pattern 34",
            advisory_source="FinCEN Advisory FIN-2025-A008",
            risk_tier="MEDIUM",
            indicators=["Red flag A_34", "Red flag B_34", "Red flag C_34"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 34."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0035",
            title="Regulatory Typology 0035: Financial crime pattern 35",
            advisory_source="FinCEN Advisory FIN-2021-A009",
            risk_tier="LOW",
            indicators=["Red flag A_35", "Red flag B_35", "Red flag C_35"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 35."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0036",
            title="Regulatory Typology 0036: Financial crime pattern 36",
            advisory_source="FinCEN Advisory FIN-2022-A001",
            risk_tier="CRITICAL",
            indicators=["Red flag A_36", "Red flag B_36", "Red flag C_36"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 36."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0037",
            title="Regulatory Typology 0037: Financial crime pattern 37",
            advisory_source="FinCEN Advisory FIN-2023-A002",
            risk_tier="HIGH",
            indicators=["Red flag A_37", "Red flag B_37", "Red flag C_37"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 37."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0038",
            title="Regulatory Typology 0038: Financial crime pattern 38",
            advisory_source="FinCEN Advisory FIN-2024-A003",
            risk_tier="MEDIUM",
            indicators=["Red flag A_38", "Red flag B_38", "Red flag C_38"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 38."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0039",
            title="Regulatory Typology 0039: Financial crime pattern 39",
            advisory_source="FinCEN Advisory FIN-2025-A004",
            risk_tier="LOW",
            indicators=["Red flag A_39", "Red flag B_39", "Red flag C_39"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 39."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0040",
            title="Regulatory Typology 0040: Financial crime pattern 40",
            advisory_source="FinCEN Advisory FIN-2021-A005",
            risk_tier="CRITICAL",
            indicators=["Red flag A_40", "Red flag B_40", "Red flag C_40"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 40."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0041",
            title="Regulatory Typology 0041: Financial crime pattern 41",
            advisory_source="FinCEN Advisory FIN-2022-A006",
            risk_tier="HIGH",
            indicators=["Red flag A_41", "Red flag B_41", "Red flag C_41"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 41."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0042",
            title="Regulatory Typology 0042: Financial crime pattern 42",
            advisory_source="FinCEN Advisory FIN-2023-A007",
            risk_tier="MEDIUM",
            indicators=["Red flag A_42", "Red flag B_42", "Red flag C_42"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 42."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0043",
            title="Regulatory Typology 0043: Financial crime pattern 43",
            advisory_source="FinCEN Advisory FIN-2024-A008",
            risk_tier="LOW",
            indicators=["Red flag A_43", "Red flag B_43", "Red flag C_43"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 43."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0044",
            title="Regulatory Typology 0044: Financial crime pattern 44",
            advisory_source="FinCEN Advisory FIN-2025-A009",
            risk_tier="CRITICAL",
            indicators=["Red flag A_44", "Red flag B_44", "Red flag C_44"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 44."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0045",
            title="Regulatory Typology 0045: Financial crime pattern 45",
            advisory_source="FinCEN Advisory FIN-2021-A001",
            risk_tier="HIGH",
            indicators=["Red flag A_45", "Red flag B_45", "Red flag C_45"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 45."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0046",
            title="Regulatory Typology 0046: Financial crime pattern 46",
            advisory_source="FinCEN Advisory FIN-2022-A002",
            risk_tier="MEDIUM",
            indicators=["Red flag A_46", "Red flag B_46", "Red flag C_46"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 46."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0047",
            title="Regulatory Typology 0047: Financial crime pattern 47",
            advisory_source="FinCEN Advisory FIN-2023-A003",
            risk_tier="LOW",
            indicators=["Red flag A_47", "Red flag B_47", "Red flag C_47"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 47."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0048",
            title="Regulatory Typology 0048: Financial crime pattern 48",
            advisory_source="FinCEN Advisory FIN-2024-A004",
            risk_tier="CRITICAL",
            indicators=["Red flag A_48", "Red flag B_48", "Red flag C_48"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 48."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0049",
            title="Regulatory Typology 0049: Financial crime pattern 49",
            advisory_source="FinCEN Advisory FIN-2025-A005",
            risk_tier="HIGH",
            indicators=["Red flag A_49", "Red flag B_49", "Red flag C_49"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 49."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0050",
            title="Regulatory Typology 0050: Financial crime pattern 50",
            advisory_source="FinCEN Advisory FIN-2021-A006",
            risk_tier="MEDIUM",
            indicators=["Red flag A_50", "Red flag B_50", "Red flag C_50"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 50."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0051",
            title="Regulatory Typology 0051: Financial crime pattern 51",
            advisory_source="FinCEN Advisory FIN-2022-A007",
            risk_tier="LOW",
            indicators=["Red flag A_51", "Red flag B_51", "Red flag C_51"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 51."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0052",
            title="Regulatory Typology 0052: Financial crime pattern 52",
            advisory_source="FinCEN Advisory FIN-2023-A008",
            risk_tier="CRITICAL",
            indicators=["Red flag A_52", "Red flag B_52", "Red flag C_52"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 52."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0053",
            title="Regulatory Typology 0053: Financial crime pattern 53",
            advisory_source="FinCEN Advisory FIN-2024-A009",
            risk_tier="HIGH",
            indicators=["Red flag A_53", "Red flag B_53", "Red flag C_53"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 53."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0054",
            title="Regulatory Typology 0054: Financial crime pattern 54",
            advisory_source="FinCEN Advisory FIN-2025-A001",
            risk_tier="MEDIUM",
            indicators=["Red flag A_54", "Red flag B_54", "Red flag C_54"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 54."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0055",
            title="Regulatory Typology 0055: Financial crime pattern 55",
            advisory_source="FinCEN Advisory FIN-2021-A002",
            risk_tier="LOW",
            indicators=["Red flag A_55", "Red flag B_55", "Red flag C_55"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 55."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0056",
            title="Regulatory Typology 0056: Financial crime pattern 56",
            advisory_source="FinCEN Advisory FIN-2022-A003",
            risk_tier="CRITICAL",
            indicators=["Red flag A_56", "Red flag B_56", "Red flag C_56"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 56."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0057",
            title="Regulatory Typology 0057: Financial crime pattern 57",
            advisory_source="FinCEN Advisory FIN-2023-A004",
            risk_tier="HIGH",
            indicators=["Red flag A_57", "Red flag B_57", "Red flag C_57"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 57."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0058",
            title="Regulatory Typology 0058: Financial crime pattern 58",
            advisory_source="FinCEN Advisory FIN-2024-A005",
            risk_tier="MEDIUM",
            indicators=["Red flag A_58", "Red flag B_58", "Red flag C_58"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 58."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0059",
            title="Regulatory Typology 0059: Financial crime pattern 59",
            advisory_source="FinCEN Advisory FIN-2025-A006",
            risk_tier="LOW",
            indicators=["Red flag A_59", "Red flag B_59", "Red flag C_59"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 59."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0060",
            title="Regulatory Typology 0060: Financial crime pattern 60",
            advisory_source="FinCEN Advisory FIN-2021-A007",
            risk_tier="CRITICAL",
            indicators=["Red flag A_60", "Red flag B_60", "Red flag C_60"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 60."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0061",
            title="Regulatory Typology 0061: Financial crime pattern 61",
            advisory_source="FinCEN Advisory FIN-2022-A008",
            risk_tier="HIGH",
            indicators=["Red flag A_61", "Red flag B_61", "Red flag C_61"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 61."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0062",
            title="Regulatory Typology 0062: Financial crime pattern 62",
            advisory_source="FinCEN Advisory FIN-2023-A009",
            risk_tier="MEDIUM",
            indicators=["Red flag A_62", "Red flag B_62", "Red flag C_62"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 62."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0063",
            title="Regulatory Typology 0063: Financial crime pattern 63",
            advisory_source="FinCEN Advisory FIN-2024-A001",
            risk_tier="LOW",
            indicators=["Red flag A_63", "Red flag B_63", "Red flag C_63"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 63."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0064",
            title="Regulatory Typology 0064: Financial crime pattern 64",
            advisory_source="FinCEN Advisory FIN-2025-A002",
            risk_tier="CRITICAL",
            indicators=["Red flag A_64", "Red flag B_64", "Red flag C_64"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 64."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0065",
            title="Regulatory Typology 0065: Financial crime pattern 65",
            advisory_source="FinCEN Advisory FIN-2021-A003",
            risk_tier="HIGH",
            indicators=["Red flag A_65", "Red flag B_65", "Red flag C_65"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 65."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0066",
            title="Regulatory Typology 0066: Financial crime pattern 66",
            advisory_source="FinCEN Advisory FIN-2022-A004",
            risk_tier="MEDIUM",
            indicators=["Red flag A_66", "Red flag B_66", "Red flag C_66"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 66."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0067",
            title="Regulatory Typology 0067: Financial crime pattern 67",
            advisory_source="FinCEN Advisory FIN-2023-A005",
            risk_tier="LOW",
            indicators=["Red flag A_67", "Red flag B_67", "Red flag C_67"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 67."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0068",
            title="Regulatory Typology 0068: Financial crime pattern 68",
            advisory_source="FinCEN Advisory FIN-2024-A006",
            risk_tier="CRITICAL",
            indicators=["Red flag A_68", "Red flag B_68", "Red flag C_68"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 68."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0069",
            title="Regulatory Typology 0069: Financial crime pattern 69",
            advisory_source="FinCEN Advisory FIN-2025-A007",
            risk_tier="HIGH",
            indicators=["Red flag A_69", "Red flag B_69", "Red flag C_69"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 69."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0070",
            title="Regulatory Typology 0070: Financial crime pattern 70",
            advisory_source="FinCEN Advisory FIN-2021-A008",
            risk_tier="MEDIUM",
            indicators=["Red flag A_70", "Red flag B_70", "Red flag C_70"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 70."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0071",
            title="Regulatory Typology 0071: Financial crime pattern 71",
            advisory_source="FinCEN Advisory FIN-2022-A009",
            risk_tier="LOW",
            indicators=["Red flag A_71", "Red flag B_71", "Red flag C_71"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 71."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0072",
            title="Regulatory Typology 0072: Financial crime pattern 72",
            advisory_source="FinCEN Advisory FIN-2023-A001",
            risk_tier="CRITICAL",
            indicators=["Red flag A_72", "Red flag B_72", "Red flag C_72"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 72."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0073",
            title="Regulatory Typology 0073: Financial crime pattern 73",
            advisory_source="FinCEN Advisory FIN-2024-A002",
            risk_tier="HIGH",
            indicators=["Red flag A_73", "Red flag B_73", "Red flag C_73"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 73."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0074",
            title="Regulatory Typology 0074: Financial crime pattern 74",
            advisory_source="FinCEN Advisory FIN-2025-A003",
            risk_tier="MEDIUM",
            indicators=["Red flag A_74", "Red flag B_74", "Red flag C_74"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 74."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0075",
            title="Regulatory Typology 0075: Financial crime pattern 75",
            advisory_source="FinCEN Advisory FIN-2021-A004",
            risk_tier="LOW",
            indicators=["Red flag A_75", "Red flag B_75", "Red flag C_75"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 75."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0076",
            title="Regulatory Typology 0076: Financial crime pattern 76",
            advisory_source="FinCEN Advisory FIN-2022-A005",
            risk_tier="CRITICAL",
            indicators=["Red flag A_76", "Red flag B_76", "Red flag C_76"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 76."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0077",
            title="Regulatory Typology 0077: Financial crime pattern 77",
            advisory_source="FinCEN Advisory FIN-2023-A006",
            risk_tier="HIGH",
            indicators=["Red flag A_77", "Red flag B_77", "Red flag C_77"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 77."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0078",
            title="Regulatory Typology 0078: Financial crime pattern 78",
            advisory_source="FinCEN Advisory FIN-2024-A007",
            risk_tier="MEDIUM",
            indicators=["Red flag A_78", "Red flag B_78", "Red flag C_78"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 78."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0079",
            title="Regulatory Typology 0079: Financial crime pattern 79",
            advisory_source="FinCEN Advisory FIN-2025-A008",
            risk_tier="LOW",
            indicators=["Red flag A_79", "Red flag B_79", "Red flag C_79"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 79."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0080",
            title="Regulatory Typology 0080: Financial crime pattern 80",
            advisory_source="FinCEN Advisory FIN-2021-A009",
            risk_tier="CRITICAL",
            indicators=["Red flag A_80", "Red flag B_80", "Red flag C_80"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 80."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0081",
            title="Regulatory Typology 0081: Financial crime pattern 81",
            advisory_source="FinCEN Advisory FIN-2022-A001",
            risk_tier="HIGH",
            indicators=["Red flag A_81", "Red flag B_81", "Red flag C_81"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 81."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0082",
            title="Regulatory Typology 0082: Financial crime pattern 82",
            advisory_source="FinCEN Advisory FIN-2023-A002",
            risk_tier="MEDIUM",
            indicators=["Red flag A_82", "Red flag B_82", "Red flag C_82"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 82."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0083",
            title="Regulatory Typology 0083: Financial crime pattern 83",
            advisory_source="FinCEN Advisory FIN-2024-A003",
            risk_tier="LOW",
            indicators=["Red flag A_83", "Red flag B_83", "Red flag C_83"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 83."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0084",
            title="Regulatory Typology 0084: Financial crime pattern 84",
            advisory_source="FinCEN Advisory FIN-2025-A004",
            risk_tier="CRITICAL",
            indicators=["Red flag A_84", "Red flag B_84", "Red flag C_84"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 84."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0085",
            title="Regulatory Typology 0085: Financial crime pattern 85",
            advisory_source="FinCEN Advisory FIN-2021-A005",
            risk_tier="HIGH",
            indicators=["Red flag A_85", "Red flag B_85", "Red flag C_85"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 85."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0086",
            title="Regulatory Typology 0086: Financial crime pattern 86",
            advisory_source="FinCEN Advisory FIN-2022-A006",
            risk_tier="MEDIUM",
            indicators=["Red flag A_86", "Red flag B_86", "Red flag C_86"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 86."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0087",
            title="Regulatory Typology 0087: Financial crime pattern 87",
            advisory_source="FinCEN Advisory FIN-2023-A007",
            risk_tier="LOW",
            indicators=["Red flag A_87", "Red flag B_87", "Red flag C_87"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 87."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0088",
            title="Regulatory Typology 0088: Financial crime pattern 88",
            advisory_source="FinCEN Advisory FIN-2024-A008",
            risk_tier="CRITICAL",
            indicators=["Red flag A_88", "Red flag B_88", "Red flag C_88"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 88."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0089",
            title="Regulatory Typology 0089: Financial crime pattern 89",
            advisory_source="FinCEN Advisory FIN-2025-A009",
            risk_tier="HIGH",
            indicators=["Red flag A_89", "Red flag B_89", "Red flag C_89"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 89."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0090",
            title="Regulatory Typology 0090: Financial crime pattern 90",
            advisory_source="FinCEN Advisory FIN-2021-A001",
            risk_tier="MEDIUM",
            indicators=["Red flag A_90", "Red flag B_90", "Red flag C_90"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 90."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0091",
            title="Regulatory Typology 0091: Financial crime pattern 91",
            advisory_source="FinCEN Advisory FIN-2022-A002",
            risk_tier="LOW",
            indicators=["Red flag A_91", "Red flag B_91", "Red flag C_91"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 91."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0092",
            title="Regulatory Typology 0092: Financial crime pattern 92",
            advisory_source="FinCEN Advisory FIN-2023-A003",
            risk_tier="CRITICAL",
            indicators=["Red flag A_92", "Red flag B_92", "Red flag C_92"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 92."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0093",
            title="Regulatory Typology 0093: Financial crime pattern 93",
            advisory_source="FinCEN Advisory FIN-2024-A004",
            risk_tier="HIGH",
            indicators=["Red flag A_93", "Red flag B_93", "Red flag C_93"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 93."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0094",
            title="Regulatory Typology 0094: Financial crime pattern 94",
            advisory_source="FinCEN Advisory FIN-2025-A005",
            risk_tier="MEDIUM",
            indicators=["Red flag A_94", "Red flag B_94", "Red flag C_94"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 94."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0095",
            title="Regulatory Typology 0095: Financial crime pattern 95",
            advisory_source="FinCEN Advisory FIN-2021-A006",
            risk_tier="LOW",
            indicators=["Red flag A_95", "Red flag B_95", "Red flag C_95"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 95."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0096",
            title="Regulatory Typology 0096: Financial crime pattern 96",
            advisory_source="FinCEN Advisory FIN-2022-A007",
            risk_tier="CRITICAL",
            indicators=["Red flag A_96", "Red flag B_96", "Red flag C_96"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 96."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0097",
            title="Regulatory Typology 0097: Financial crime pattern 97",
            advisory_source="FinCEN Advisory FIN-2023-A008",
            risk_tier="HIGH",
            indicators=["Red flag A_97", "Red flag B_97", "Red flag C_97"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 97."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0098",
            title="Regulatory Typology 0098: Financial crime pattern 98",
            advisory_source="FinCEN Advisory FIN-2024-A009",
            risk_tier="MEDIUM",
            indicators=["Red flag A_98", "Red flag B_98", "Red flag C_98"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 98."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0099",
            title="Regulatory Typology 0099: Financial crime pattern 99",
            advisory_source="FinCEN Advisory FIN-2025-A001",
            risk_tier="LOW",
            indicators=["Red flag A_99", "Red flag B_99", "Red flag C_99"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 99."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0100",
            title="Regulatory Typology 0100: Financial crime pattern 100",
            advisory_source="FinCEN Advisory FIN-2021-A002",
            risk_tier="CRITICAL",
            indicators=["Red flag A_100", "Red flag B_100", "Red flag C_100"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 100."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0101",
            title="Regulatory Typology 0101: Financial crime pattern 101",
            advisory_source="FinCEN Advisory FIN-2022-A003",
            risk_tier="HIGH",
            indicators=["Red flag A_101", "Red flag B_101", "Red flag C_101"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 101."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0102",
            title="Regulatory Typology 0102: Financial crime pattern 102",
            advisory_source="FinCEN Advisory FIN-2023-A004",
            risk_tier="MEDIUM",
            indicators=["Red flag A_102", "Red flag B_102", "Red flag C_102"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 102."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0103",
            title="Regulatory Typology 0103: Financial crime pattern 103",
            advisory_source="FinCEN Advisory FIN-2024-A005",
            risk_tier="LOW",
            indicators=["Red flag A_103", "Red flag B_103", "Red flag C_103"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 103."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0104",
            title="Regulatory Typology 0104: Financial crime pattern 104",
            advisory_source="FinCEN Advisory FIN-2025-A006",
            risk_tier="CRITICAL",
            indicators=["Red flag A_104", "Red flag B_104", "Red flag C_104"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 104."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0105",
            title="Regulatory Typology 0105: Financial crime pattern 105",
            advisory_source="FinCEN Advisory FIN-2021-A007",
            risk_tier="HIGH",
            indicators=["Red flag A_105", "Red flag B_105", "Red flag C_105"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 105."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0106",
            title="Regulatory Typology 0106: Financial crime pattern 106",
            advisory_source="FinCEN Advisory FIN-2022-A008",
            risk_tier="MEDIUM",
            indicators=["Red flag A_106", "Red flag B_106", "Red flag C_106"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 106."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0107",
            title="Regulatory Typology 0107: Financial crime pattern 107",
            advisory_source="FinCEN Advisory FIN-2023-A009",
            risk_tier="LOW",
            indicators=["Red flag A_107", "Red flag B_107", "Red flag C_107"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 107."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0108",
            title="Regulatory Typology 0108: Financial crime pattern 108",
            advisory_source="FinCEN Advisory FIN-2024-A001",
            risk_tier="CRITICAL",
            indicators=["Red flag A_108", "Red flag B_108", "Red flag C_108"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 108."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0109",
            title="Regulatory Typology 0109: Financial crime pattern 109",
            advisory_source="FinCEN Advisory FIN-2025-A002",
            risk_tier="HIGH",
            indicators=["Red flag A_109", "Red flag B_109", "Red flag C_109"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 109."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0110",
            title="Regulatory Typology 0110: Financial crime pattern 110",
            advisory_source="FinCEN Advisory FIN-2021-A003",
            risk_tier="MEDIUM",
            indicators=["Red flag A_110", "Red flag B_110", "Red flag C_110"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 110."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0111",
            title="Regulatory Typology 0111: Financial crime pattern 111",
            advisory_source="FinCEN Advisory FIN-2022-A004",
            risk_tier="LOW",
            indicators=["Red flag A_111", "Red flag B_111", "Red flag C_111"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 111."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0112",
            title="Regulatory Typology 0112: Financial crime pattern 112",
            advisory_source="FinCEN Advisory FIN-2023-A005",
            risk_tier="CRITICAL",
            indicators=["Red flag A_112", "Red flag B_112", "Red flag C_112"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 112."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0113",
            title="Regulatory Typology 0113: Financial crime pattern 113",
            advisory_source="FinCEN Advisory FIN-2024-A006",
            risk_tier="HIGH",
            indicators=["Red flag A_113", "Red flag B_113", "Red flag C_113"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 113."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0114",
            title="Regulatory Typology 0114: Financial crime pattern 114",
            advisory_source="FinCEN Advisory FIN-2025-A007",
            risk_tier="MEDIUM",
            indicators=["Red flag A_114", "Red flag B_114", "Red flag C_114"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 114."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0115",
            title="Regulatory Typology 0115: Financial crime pattern 115",
            advisory_source="FinCEN Advisory FIN-2021-A008",
            risk_tier="LOW",
            indicators=["Red flag A_115", "Red flag B_115", "Red flag C_115"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 115."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0116",
            title="Regulatory Typology 0116: Financial crime pattern 116",
            advisory_source="FinCEN Advisory FIN-2022-A009",
            risk_tier="CRITICAL",
            indicators=["Red flag A_116", "Red flag B_116", "Red flag C_116"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 116."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0117",
            title="Regulatory Typology 0117: Financial crime pattern 117",
            advisory_source="FinCEN Advisory FIN-2023-A001",
            risk_tier="HIGH",
            indicators=["Red flag A_117", "Red flag B_117", "Red flag C_117"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 117."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0118",
            title="Regulatory Typology 0118: Financial crime pattern 118",
            advisory_source="FinCEN Advisory FIN-2024-A002",
            risk_tier="MEDIUM",
            indicators=["Red flag A_118", "Red flag B_118", "Red flag C_118"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 118."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0119",
            title="Regulatory Typology 0119: Financial crime pattern 119",
            advisory_source="FinCEN Advisory FIN-2025-A003",
            risk_tier="LOW",
            indicators=["Red flag A_119", "Red flag B_119", "Red flag C_119"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 119."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0120",
            title="Regulatory Typology 0120: Financial crime pattern 120",
            advisory_source="FinCEN Advisory FIN-2021-A004",
            risk_tier="CRITICAL",
            indicators=["Red flag A_120", "Red flag B_120", "Red flag C_120"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 120."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0121",
            title="Regulatory Typology 0121: Financial crime pattern 121",
            advisory_source="FinCEN Advisory FIN-2022-A005",
            risk_tier="HIGH",
            indicators=["Red flag A_121", "Red flag B_121", "Red flag C_121"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 121."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0122",
            title="Regulatory Typology 0122: Financial crime pattern 122",
            advisory_source="FinCEN Advisory FIN-2023-A006",
            risk_tier="MEDIUM",
            indicators=["Red flag A_122", "Red flag B_122", "Red flag C_122"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 122."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0123",
            title="Regulatory Typology 0123: Financial crime pattern 123",
            advisory_source="FinCEN Advisory FIN-2024-A007",
            risk_tier="LOW",
            indicators=["Red flag A_123", "Red flag B_123", "Red flag C_123"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 123."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0124",
            title="Regulatory Typology 0124: Financial crime pattern 124",
            advisory_source="FinCEN Advisory FIN-2025-A008",
            risk_tier="CRITICAL",
            indicators=["Red flag A_124", "Red flag B_124", "Red flag C_124"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 124."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0125",
            title="Regulatory Typology 0125: Financial crime pattern 125",
            advisory_source="FinCEN Advisory FIN-2021-A009",
            risk_tier="HIGH",
            indicators=["Red flag A_125", "Red flag B_125", "Red flag C_125"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 125."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0126",
            title="Regulatory Typology 0126: Financial crime pattern 126",
            advisory_source="FinCEN Advisory FIN-2022-A001",
            risk_tier="MEDIUM",
            indicators=["Red flag A_126", "Red flag B_126", "Red flag C_126"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 126."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0127",
            title="Regulatory Typology 0127: Financial crime pattern 127",
            advisory_source="FinCEN Advisory FIN-2023-A002",
            risk_tier="LOW",
            indicators=["Red flag A_127", "Red flag B_127", "Red flag C_127"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 127."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0128",
            title="Regulatory Typology 0128: Financial crime pattern 128",
            advisory_source="FinCEN Advisory FIN-2024-A003",
            risk_tier="CRITICAL",
            indicators=["Red flag A_128", "Red flag B_128", "Red flag C_128"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 128."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0129",
            title="Regulatory Typology 0129: Financial crime pattern 129",
            advisory_source="FinCEN Advisory FIN-2025-A004",
            risk_tier="HIGH",
            indicators=["Red flag A_129", "Red flag B_129", "Red flag C_129"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 129."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0130",
            title="Regulatory Typology 0130: Financial crime pattern 130",
            advisory_source="FinCEN Advisory FIN-2021-A005",
            risk_tier="MEDIUM",
            indicators=["Red flag A_130", "Red flag B_130", "Red flag C_130"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 130."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0131",
            title="Regulatory Typology 0131: Financial crime pattern 131",
            advisory_source="FinCEN Advisory FIN-2022-A006",
            risk_tier="LOW",
            indicators=["Red flag A_131", "Red flag B_131", "Red flag C_131"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 131."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0132",
            title="Regulatory Typology 0132: Financial crime pattern 132",
            advisory_source="FinCEN Advisory FIN-2023-A007",
            risk_tier="CRITICAL",
            indicators=["Red flag A_132", "Red flag B_132", "Red flag C_132"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 132."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0133",
            title="Regulatory Typology 0133: Financial crime pattern 133",
            advisory_source="FinCEN Advisory FIN-2024-A008",
            risk_tier="HIGH",
            indicators=["Red flag A_133", "Red flag B_133", "Red flag C_133"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 133."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0134",
            title="Regulatory Typology 0134: Financial crime pattern 134",
            advisory_source="FinCEN Advisory FIN-2025-A009",
            risk_tier="MEDIUM",
            indicators=["Red flag A_134", "Red flag B_134", "Red flag C_134"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 134."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0135",
            title="Regulatory Typology 0135: Financial crime pattern 135",
            advisory_source="FinCEN Advisory FIN-2021-A001",
            risk_tier="LOW",
            indicators=["Red flag A_135", "Red flag B_135", "Red flag C_135"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 135."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0136",
            title="Regulatory Typology 0136: Financial crime pattern 136",
            advisory_source="FinCEN Advisory FIN-2022-A002",
            risk_tier="CRITICAL",
            indicators=["Red flag A_136", "Red flag B_136", "Red flag C_136"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 136."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0137",
            title="Regulatory Typology 0137: Financial crime pattern 137",
            advisory_source="FinCEN Advisory FIN-2023-A003",
            risk_tier="HIGH",
            indicators=["Red flag A_137", "Red flag B_137", "Red flag C_137"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 137."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0138",
            title="Regulatory Typology 0138: Financial crime pattern 138",
            advisory_source="FinCEN Advisory FIN-2024-A004",
            risk_tier="MEDIUM",
            indicators=["Red flag A_138", "Red flag B_138", "Red flag C_138"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 138."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0139",
            title="Regulatory Typology 0139: Financial crime pattern 139",
            advisory_source="FinCEN Advisory FIN-2025-A005",
            risk_tier="LOW",
            indicators=["Red flag A_139", "Red flag B_139", "Red flag C_139"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 139."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0140",
            title="Regulatory Typology 0140: Financial crime pattern 140",
            advisory_source="FinCEN Advisory FIN-2021-A006",
            risk_tier="CRITICAL",
            indicators=["Red flag A_140", "Red flag B_140", "Red flag C_140"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 140."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0141",
            title="Regulatory Typology 0141: Financial crime pattern 141",
            advisory_source="FinCEN Advisory FIN-2022-A007",
            risk_tier="HIGH",
            indicators=["Red flag A_141", "Red flag B_141", "Red flag C_141"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 141."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0142",
            title="Regulatory Typology 0142: Financial crime pattern 142",
            advisory_source="FinCEN Advisory FIN-2023-A008",
            risk_tier="MEDIUM",
            indicators=["Red flag A_142", "Red flag B_142", "Red flag C_142"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 142."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0143",
            title="Regulatory Typology 0143: Financial crime pattern 143",
            advisory_source="FinCEN Advisory FIN-2024-A009",
            risk_tier="LOW",
            indicators=["Red flag A_143", "Red flag B_143", "Red flag C_143"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 143."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0144",
            title="Regulatory Typology 0144: Financial crime pattern 144",
            advisory_source="FinCEN Advisory FIN-2025-A001",
            risk_tier="CRITICAL",
            indicators=["Red flag A_144", "Red flag B_144", "Red flag C_144"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 144."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0145",
            title="Regulatory Typology 0145: Financial crime pattern 145",
            advisory_source="FinCEN Advisory FIN-2021-A002",
            risk_tier="HIGH",
            indicators=["Red flag A_145", "Red flag B_145", "Red flag C_145"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 145."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0146",
            title="Regulatory Typology 0146: Financial crime pattern 146",
            advisory_source="FinCEN Advisory FIN-2022-A003",
            risk_tier="MEDIUM",
            indicators=["Red flag A_146", "Red flag B_146", "Red flag C_146"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 146."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0147",
            title="Regulatory Typology 0147: Financial crime pattern 147",
            advisory_source="FinCEN Advisory FIN-2023-A004",
            risk_tier="LOW",
            indicators=["Red flag A_147", "Red flag B_147", "Red flag C_147"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 147."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0148",
            title="Regulatory Typology 0148: Financial crime pattern 148",
            advisory_source="FinCEN Advisory FIN-2024-A005",
            risk_tier="CRITICAL",
            indicators=["Red flag A_148", "Red flag B_148", "Red flag C_148"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 148."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0149",
            title="Regulatory Typology 0149: Financial crime pattern 149",
            advisory_source="FinCEN Advisory FIN-2025-A006",
            risk_tier="HIGH",
            indicators=["Red flag A_149", "Red flag B_149", "Red flag C_149"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 149."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0150",
            title="Regulatory Typology 0150: Financial crime pattern 150",
            advisory_source="FinCEN Advisory FIN-2021-A007",
            risk_tier="MEDIUM",
            indicators=["Red flag A_150", "Red flag B_150", "Red flag C_150"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 150."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0151",
            title="Regulatory Typology 0151: Financial crime pattern 151",
            advisory_source="FinCEN Advisory FIN-2022-A008",
            risk_tier="LOW",
            indicators=["Red flag A_151", "Red flag B_151", "Red flag C_151"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 151."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0152",
            title="Regulatory Typology 0152: Financial crime pattern 152",
            advisory_source="FinCEN Advisory FIN-2023-A009",
            risk_tier="CRITICAL",
            indicators=["Red flag A_152", "Red flag B_152", "Red flag C_152"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 152."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0153",
            title="Regulatory Typology 0153: Financial crime pattern 153",
            advisory_source="FinCEN Advisory FIN-2024-A001",
            risk_tier="HIGH",
            indicators=["Red flag A_153", "Red flag B_153", "Red flag C_153"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 153."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0154",
            title="Regulatory Typology 0154: Financial crime pattern 154",
            advisory_source="FinCEN Advisory FIN-2025-A002",
            risk_tier="MEDIUM",
            indicators=["Red flag A_154", "Red flag B_154", "Red flag C_154"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 154."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0155",
            title="Regulatory Typology 0155: Financial crime pattern 155",
            advisory_source="FinCEN Advisory FIN-2021-A003",
            risk_tier="LOW",
            indicators=["Red flag A_155", "Red flag B_155", "Red flag C_155"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 155."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0156",
            title="Regulatory Typology 0156: Financial crime pattern 156",
            advisory_source="FinCEN Advisory FIN-2022-A004",
            risk_tier="CRITICAL",
            indicators=["Red flag A_156", "Red flag B_156", "Red flag C_156"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 156."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0157",
            title="Regulatory Typology 0157: Financial crime pattern 157",
            advisory_source="FinCEN Advisory FIN-2023-A005",
            risk_tier="HIGH",
            indicators=["Red flag A_157", "Red flag B_157", "Red flag C_157"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 157."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0158",
            title="Regulatory Typology 0158: Financial crime pattern 158",
            advisory_source="FinCEN Advisory FIN-2024-A006",
            risk_tier="MEDIUM",
            indicators=["Red flag A_158", "Red flag B_158", "Red flag C_158"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 158."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0159",
            title="Regulatory Typology 0159: Financial crime pattern 159",
            advisory_source="FinCEN Advisory FIN-2025-A007",
            risk_tier="LOW",
            indicators=["Red flag A_159", "Red flag B_159", "Red flag C_159"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 159."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0160",
            title="Regulatory Typology 0160: Financial crime pattern 160",
            advisory_source="FinCEN Advisory FIN-2021-A008",
            risk_tier="CRITICAL",
            indicators=["Red flag A_160", "Red flag B_160", "Red flag C_160"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 160."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0161",
            title="Regulatory Typology 0161: Financial crime pattern 161",
            advisory_source="FinCEN Advisory FIN-2022-A009",
            risk_tier="HIGH",
            indicators=["Red flag A_161", "Red flag B_161", "Red flag C_161"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 161."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0162",
            title="Regulatory Typology 0162: Financial crime pattern 162",
            advisory_source="FinCEN Advisory FIN-2023-A001",
            risk_tier="MEDIUM",
            indicators=["Red flag A_162", "Red flag B_162", "Red flag C_162"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 162."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0163",
            title="Regulatory Typology 0163: Financial crime pattern 163",
            advisory_source="FinCEN Advisory FIN-2024-A002",
            risk_tier="LOW",
            indicators=["Red flag A_163", "Red flag B_163", "Red flag C_163"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 163."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0164",
            title="Regulatory Typology 0164: Financial crime pattern 164",
            advisory_source="FinCEN Advisory FIN-2025-A003",
            risk_tier="CRITICAL",
            indicators=["Red flag A_164", "Red flag B_164", "Red flag C_164"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 164."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0165",
            title="Regulatory Typology 0165: Financial crime pattern 165",
            advisory_source="FinCEN Advisory FIN-2021-A004",
            risk_tier="HIGH",
            indicators=["Red flag A_165", "Red flag B_165", "Red flag C_165"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 165."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0166",
            title="Regulatory Typology 0166: Financial crime pattern 166",
            advisory_source="FinCEN Advisory FIN-2022-A005",
            risk_tier="MEDIUM",
            indicators=["Red flag A_166", "Red flag B_166", "Red flag C_166"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 166."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0167",
            title="Regulatory Typology 0167: Financial crime pattern 167",
            advisory_source="FinCEN Advisory FIN-2023-A006",
            risk_tier="LOW",
            indicators=["Red flag A_167", "Red flag B_167", "Red flag C_167"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 167."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0168",
            title="Regulatory Typology 0168: Financial crime pattern 168",
            advisory_source="FinCEN Advisory FIN-2024-A007",
            risk_tier="CRITICAL",
            indicators=["Red flag A_168", "Red flag B_168", "Red flag C_168"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 168."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0169",
            title="Regulatory Typology 0169: Financial crime pattern 169",
            advisory_source="FinCEN Advisory FIN-2025-A008",
            risk_tier="HIGH",
            indicators=["Red flag A_169", "Red flag B_169", "Red flag C_169"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 169."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0170",
            title="Regulatory Typology 0170: Financial crime pattern 170",
            advisory_source="FinCEN Advisory FIN-2021-A009",
            risk_tier="MEDIUM",
            indicators=["Red flag A_170", "Red flag B_170", "Red flag C_170"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 170."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0171",
            title="Regulatory Typology 0171: Financial crime pattern 171",
            advisory_source="FinCEN Advisory FIN-2022-A001",
            risk_tier="LOW",
            indicators=["Red flag A_171", "Red flag B_171", "Red flag C_171"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 171."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0172",
            title="Regulatory Typology 0172: Financial crime pattern 172",
            advisory_source="FinCEN Advisory FIN-2023-A002",
            risk_tier="CRITICAL",
            indicators=["Red flag A_172", "Red flag B_172", "Red flag C_172"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 172."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0173",
            title="Regulatory Typology 0173: Financial crime pattern 173",
            advisory_source="FinCEN Advisory FIN-2024-A003",
            risk_tier="HIGH",
            indicators=["Red flag A_173", "Red flag B_173", "Red flag C_173"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 173."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0174",
            title="Regulatory Typology 0174: Financial crime pattern 174",
            advisory_source="FinCEN Advisory FIN-2025-A004",
            risk_tier="MEDIUM",
            indicators=["Red flag A_174", "Red flag B_174", "Red flag C_174"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 174."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0175",
            title="Regulatory Typology 0175: Financial crime pattern 175",
            advisory_source="FinCEN Advisory FIN-2021-A005",
            risk_tier="LOW",
            indicators=["Red flag A_175", "Red flag B_175", "Red flag C_175"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 175."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0176",
            title="Regulatory Typology 0176: Financial crime pattern 176",
            advisory_source="FinCEN Advisory FIN-2022-A006",
            risk_tier="CRITICAL",
            indicators=["Red flag A_176", "Red flag B_176", "Red flag C_176"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 176."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0177",
            title="Regulatory Typology 0177: Financial crime pattern 177",
            advisory_source="FinCEN Advisory FIN-2023-A007",
            risk_tier="HIGH",
            indicators=["Red flag A_177", "Red flag B_177", "Red flag C_177"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 177."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0178",
            title="Regulatory Typology 0178: Financial crime pattern 178",
            advisory_source="FinCEN Advisory FIN-2024-A008",
            risk_tier="MEDIUM",
            indicators=["Red flag A_178", "Red flag B_178", "Red flag C_178"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 178."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0179",
            title="Regulatory Typology 0179: Financial crime pattern 179",
            advisory_source="FinCEN Advisory FIN-2025-A009",
            risk_tier="LOW",
            indicators=["Red flag A_179", "Red flag B_179", "Red flag C_179"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 179."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0180",
            title="Regulatory Typology 0180: Financial crime pattern 180",
            advisory_source="FinCEN Advisory FIN-2021-A001",
            risk_tier="CRITICAL",
            indicators=["Red flag A_180", "Red flag B_180", "Red flag C_180"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 180."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0181",
            title="Regulatory Typology 0181: Financial crime pattern 181",
            advisory_source="FinCEN Advisory FIN-2022-A002",
            risk_tier="HIGH",
            indicators=["Red flag A_181", "Red flag B_181", "Red flag C_181"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 181."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0182",
            title="Regulatory Typology 0182: Financial crime pattern 182",
            advisory_source="FinCEN Advisory FIN-2023-A003",
            risk_tier="MEDIUM",
            indicators=["Red flag A_182", "Red flag B_182", "Red flag C_182"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 182."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0183",
            title="Regulatory Typology 0183: Financial crime pattern 183",
            advisory_source="FinCEN Advisory FIN-2024-A004",
            risk_tier="LOW",
            indicators=["Red flag A_183", "Red flag B_183", "Red flag C_183"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 183."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0184",
            title="Regulatory Typology 0184: Financial crime pattern 184",
            advisory_source="FinCEN Advisory FIN-2025-A005",
            risk_tier="CRITICAL",
            indicators=["Red flag A_184", "Red flag B_184", "Red flag C_184"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 184."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0185",
            title="Regulatory Typology 0185: Financial crime pattern 185",
            advisory_source="FinCEN Advisory FIN-2021-A006",
            risk_tier="HIGH",
            indicators=["Red flag A_185", "Red flag B_185", "Red flag C_185"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 185."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0186",
            title="Regulatory Typology 0186: Financial crime pattern 186",
            advisory_source="FinCEN Advisory FIN-2022-A007",
            risk_tier="MEDIUM",
            indicators=["Red flag A_186", "Red flag B_186", "Red flag C_186"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 186."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0187",
            title="Regulatory Typology 0187: Financial crime pattern 187",
            advisory_source="FinCEN Advisory FIN-2023-A008",
            risk_tier="LOW",
            indicators=["Red flag A_187", "Red flag B_187", "Red flag C_187"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 187."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0188",
            title="Regulatory Typology 0188: Financial crime pattern 188",
            advisory_source="FinCEN Advisory FIN-2024-A009",
            risk_tier="CRITICAL",
            indicators=["Red flag A_188", "Red flag B_188", "Red flag C_188"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 188."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0189",
            title="Regulatory Typology 0189: Financial crime pattern 189",
            advisory_source="FinCEN Advisory FIN-2025-A001",
            risk_tier="HIGH",
            indicators=["Red flag A_189", "Red flag B_189", "Red flag C_189"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 189."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0190",
            title="Regulatory Typology 0190: Financial crime pattern 190",
            advisory_source="FinCEN Advisory FIN-2021-A002",
            risk_tier="MEDIUM",
            indicators=["Red flag A_190", "Red flag B_190", "Red flag C_190"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 190."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0191",
            title="Regulatory Typology 0191: Financial crime pattern 191",
            advisory_source="FinCEN Advisory FIN-2022-A003",
            risk_tier="LOW",
            indicators=["Red flag A_191", "Red flag B_191", "Red flag C_191"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 191."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0192",
            title="Regulatory Typology 0192: Financial crime pattern 192",
            advisory_source="FinCEN Advisory FIN-2023-A004",
            risk_tier="CRITICAL",
            indicators=["Red flag A_192", "Red flag B_192", "Red flag C_192"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 192."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0193",
            title="Regulatory Typology 0193: Financial crime pattern 193",
            advisory_source="FinCEN Advisory FIN-2024-A005",
            risk_tier="HIGH",
            indicators=["Red flag A_193", "Red flag B_193", "Red flag C_193"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 193."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0194",
            title="Regulatory Typology 0194: Financial crime pattern 194",
            advisory_source="FinCEN Advisory FIN-2025-A006",
            risk_tier="MEDIUM",
            indicators=["Red flag A_194", "Red flag B_194", "Red flag C_194"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 194."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0195",
            title="Regulatory Typology 0195: Financial crime pattern 195",
            advisory_source="FinCEN Advisory FIN-2021-A007",
            risk_tier="LOW",
            indicators=["Red flag A_195", "Red flag B_195", "Red flag C_195"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 195."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0196",
            title="Regulatory Typology 0196: Financial crime pattern 196",
            advisory_source="FinCEN Advisory FIN-2022-A008",
            risk_tier="CRITICAL",
            indicators=["Red flag A_196", "Red flag B_196", "Red flag C_196"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 196."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0197",
            title="Regulatory Typology 0197: Financial crime pattern 197",
            advisory_source="FinCEN Advisory FIN-2023-A009",
            risk_tier="HIGH",
            indicators=["Red flag A_197", "Red flag B_197", "Red flag C_197"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 197."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0198",
            title="Regulatory Typology 0198: Financial crime pattern 198",
            advisory_source="FinCEN Advisory FIN-2024-A001",
            risk_tier="MEDIUM",
            indicators=["Red flag A_198", "Red flag B_198", "Red flag C_198"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 198."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0199",
            title="Regulatory Typology 0199: Financial crime pattern 199",
            advisory_source="FinCEN Advisory FIN-2025-A002",
            risk_tier="LOW",
            indicators=["Red flag A_199", "Red flag B_199", "Red flag C_199"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 199."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0200",
            title="Regulatory Typology 0200: Financial crime pattern 200",
            advisory_source="FinCEN Advisory FIN-2021-A003",
            risk_tier="CRITICAL",
            indicators=["Red flag A_200", "Red flag B_200", "Red flag C_200"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 200."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0201",
            title="Regulatory Typology 0201: Financial crime pattern 201",
            advisory_source="FinCEN Advisory FIN-2022-A004",
            risk_tier="HIGH",
            indicators=["Red flag A_201", "Red flag B_201", "Red flag C_201"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 201."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0202",
            title="Regulatory Typology 0202: Financial crime pattern 202",
            advisory_source="FinCEN Advisory FIN-2023-A005",
            risk_tier="MEDIUM",
            indicators=["Red flag A_202", "Red flag B_202", "Red flag C_202"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 202."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0203",
            title="Regulatory Typology 0203: Financial crime pattern 203",
            advisory_source="FinCEN Advisory FIN-2024-A006",
            risk_tier="LOW",
            indicators=["Red flag A_203", "Red flag B_203", "Red flag C_203"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 203."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0204",
            title="Regulatory Typology 0204: Financial crime pattern 204",
            advisory_source="FinCEN Advisory FIN-2025-A007",
            risk_tier="CRITICAL",
            indicators=["Red flag A_204", "Red flag B_204", "Red flag C_204"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 204."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0205",
            title="Regulatory Typology 0205: Financial crime pattern 205",
            advisory_source="FinCEN Advisory FIN-2021-A008",
            risk_tier="HIGH",
            indicators=["Red flag A_205", "Red flag B_205", "Red flag C_205"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 205."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0206",
            title="Regulatory Typology 0206: Financial crime pattern 206",
            advisory_source="FinCEN Advisory FIN-2022-A009",
            risk_tier="MEDIUM",
            indicators=["Red flag A_206", "Red flag B_206", "Red flag C_206"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 206."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0207",
            title="Regulatory Typology 0207: Financial crime pattern 207",
            advisory_source="FinCEN Advisory FIN-2023-A001",
            risk_tier="LOW",
            indicators=["Red flag A_207", "Red flag B_207", "Red flag C_207"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 207."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0208",
            title="Regulatory Typology 0208: Financial crime pattern 208",
            advisory_source="FinCEN Advisory FIN-2024-A002",
            risk_tier="CRITICAL",
            indicators=["Red flag A_208", "Red flag B_208", "Red flag C_208"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 208."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0209",
            title="Regulatory Typology 0209: Financial crime pattern 209",
            advisory_source="FinCEN Advisory FIN-2025-A003",
            risk_tier="HIGH",
            indicators=["Red flag A_209", "Red flag B_209", "Red flag C_209"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 209."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0210",
            title="Regulatory Typology 0210: Financial crime pattern 210",
            advisory_source="FinCEN Advisory FIN-2021-A004",
            risk_tier="MEDIUM",
            indicators=["Red flag A_210", "Red flag B_210", "Red flag C_210"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 210."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0211",
            title="Regulatory Typology 0211: Financial crime pattern 211",
            advisory_source="FinCEN Advisory FIN-2022-A005",
            risk_tier="LOW",
            indicators=["Red flag A_211", "Red flag B_211", "Red flag C_211"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 211."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0212",
            title="Regulatory Typology 0212: Financial crime pattern 212",
            advisory_source="FinCEN Advisory FIN-2023-A006",
            risk_tier="CRITICAL",
            indicators=["Red flag A_212", "Red flag B_212", "Red flag C_212"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 212."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0213",
            title="Regulatory Typology 0213: Financial crime pattern 213",
            advisory_source="FinCEN Advisory FIN-2024-A007",
            risk_tier="HIGH",
            indicators=["Red flag A_213", "Red flag B_213", "Red flag C_213"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 213."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0214",
            title="Regulatory Typology 0214: Financial crime pattern 214",
            advisory_source="FinCEN Advisory FIN-2025-A008",
            risk_tier="MEDIUM",
            indicators=["Red flag A_214", "Red flag B_214", "Red flag C_214"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 214."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0215",
            title="Regulatory Typology 0215: Financial crime pattern 215",
            advisory_source="FinCEN Advisory FIN-2021-A009",
            risk_tier="LOW",
            indicators=["Red flag A_215", "Red flag B_215", "Red flag C_215"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 215."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0216",
            title="Regulatory Typology 0216: Financial crime pattern 216",
            advisory_source="FinCEN Advisory FIN-2022-A001",
            risk_tier="CRITICAL",
            indicators=["Red flag A_216", "Red flag B_216", "Red flag C_216"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 216."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0217",
            title="Regulatory Typology 0217: Financial crime pattern 217",
            advisory_source="FinCEN Advisory FIN-2023-A002",
            risk_tier="HIGH",
            indicators=["Red flag A_217", "Red flag B_217", "Red flag C_217"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 217."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0218",
            title="Regulatory Typology 0218: Financial crime pattern 218",
            advisory_source="FinCEN Advisory FIN-2024-A003",
            risk_tier="MEDIUM",
            indicators=["Red flag A_218", "Red flag B_218", "Red flag C_218"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 218."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0219",
            title="Regulatory Typology 0219: Financial crime pattern 219",
            advisory_source="FinCEN Advisory FIN-2025-A004",
            risk_tier="LOW",
            indicators=["Red flag A_219", "Red flag B_219", "Red flag C_219"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 219."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0220",
            title="Regulatory Typology 0220: Financial crime pattern 220",
            advisory_source="FinCEN Advisory FIN-2021-A005",
            risk_tier="CRITICAL",
            indicators=["Red flag A_220", "Red flag B_220", "Red flag C_220"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 220."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0221",
            title="Regulatory Typology 0221: Financial crime pattern 221",
            advisory_source="FinCEN Advisory FIN-2022-A006",
            risk_tier="HIGH",
            indicators=["Red flag A_221", "Red flag B_221", "Red flag C_221"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 221."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0222",
            title="Regulatory Typology 0222: Financial crime pattern 222",
            advisory_source="FinCEN Advisory FIN-2023-A007",
            risk_tier="MEDIUM",
            indicators=["Red flag A_222", "Red flag B_222", "Red flag C_222"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 222."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0223",
            title="Regulatory Typology 0223: Financial crime pattern 223",
            advisory_source="FinCEN Advisory FIN-2024-A008",
            risk_tier="LOW",
            indicators=["Red flag A_223", "Red flag B_223", "Red flag C_223"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 223."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0224",
            title="Regulatory Typology 0224: Financial crime pattern 224",
            advisory_source="FinCEN Advisory FIN-2025-A009",
            risk_tier="CRITICAL",
            indicators=["Red flag A_224", "Red flag B_224", "Red flag C_224"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 224."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0225",
            title="Regulatory Typology 0225: Financial crime pattern 225",
            advisory_source="FinCEN Advisory FIN-2021-A001",
            risk_tier="HIGH",
            indicators=["Red flag A_225", "Red flag B_225", "Red flag C_225"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 225."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0226",
            title="Regulatory Typology 0226: Financial crime pattern 226",
            advisory_source="FinCEN Advisory FIN-2022-A002",
            risk_tier="MEDIUM",
            indicators=["Red flag A_226", "Red flag B_226", "Red flag C_226"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 226."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0227",
            title="Regulatory Typology 0227: Financial crime pattern 227",
            advisory_source="FinCEN Advisory FIN-2023-A003",
            risk_tier="LOW",
            indicators=["Red flag A_227", "Red flag B_227", "Red flag C_227"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 227."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0228",
            title="Regulatory Typology 0228: Financial crime pattern 228",
            advisory_source="FinCEN Advisory FIN-2024-A004",
            risk_tier="CRITICAL",
            indicators=["Red flag A_228", "Red flag B_228", "Red flag C_228"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 228."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0229",
            title="Regulatory Typology 0229: Financial crime pattern 229",
            advisory_source="FinCEN Advisory FIN-2025-A005",
            risk_tier="HIGH",
            indicators=["Red flag A_229", "Red flag B_229", "Red flag C_229"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 229."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0230",
            title="Regulatory Typology 0230: Financial crime pattern 230",
            advisory_source="FinCEN Advisory FIN-2021-A006",
            risk_tier="MEDIUM",
            indicators=["Red flag A_230", "Red flag B_230", "Red flag C_230"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 230."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0231",
            title="Regulatory Typology 0231: Financial crime pattern 231",
            advisory_source="FinCEN Advisory FIN-2022-A007",
            risk_tier="LOW",
            indicators=["Red flag A_231", "Red flag B_231", "Red flag C_231"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 231."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0232",
            title="Regulatory Typology 0232: Financial crime pattern 232",
            advisory_source="FinCEN Advisory FIN-2023-A008",
            risk_tier="CRITICAL",
            indicators=["Red flag A_232", "Red flag B_232", "Red flag C_232"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 232."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0233",
            title="Regulatory Typology 0233: Financial crime pattern 233",
            advisory_source="FinCEN Advisory FIN-2024-A009",
            risk_tier="HIGH",
            indicators=["Red flag A_233", "Red flag B_233", "Red flag C_233"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 233."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0234",
            title="Regulatory Typology 0234: Financial crime pattern 234",
            advisory_source="FinCEN Advisory FIN-2025-A001",
            risk_tier="MEDIUM",
            indicators=["Red flag A_234", "Red flag B_234", "Red flag C_234"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 234."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0235",
            title="Regulatory Typology 0235: Financial crime pattern 235",
            advisory_source="FinCEN Advisory FIN-2021-A002",
            risk_tier="LOW",
            indicators=["Red flag A_235", "Red flag B_235", "Red flag C_235"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 235."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0236",
            title="Regulatory Typology 0236: Financial crime pattern 236",
            advisory_source="FinCEN Advisory FIN-2022-A003",
            risk_tier="CRITICAL",
            indicators=["Red flag A_236", "Red flag B_236", "Red flag C_236"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 236."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0237",
            title="Regulatory Typology 0237: Financial crime pattern 237",
            advisory_source="FinCEN Advisory FIN-2023-A004",
            risk_tier="HIGH",
            indicators=["Red flag A_237", "Red flag B_237", "Red flag C_237"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 237."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0238",
            title="Regulatory Typology 0238: Financial crime pattern 238",
            advisory_source="FinCEN Advisory FIN-2024-A005",
            risk_tier="MEDIUM",
            indicators=["Red flag A_238", "Red flag B_238", "Red flag C_238"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 238."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0239",
            title="Regulatory Typology 0239: Financial crime pattern 239",
            advisory_source="FinCEN Advisory FIN-2025-A006",
            risk_tier="LOW",
            indicators=["Red flag A_239", "Red flag B_239", "Red flag C_239"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 239."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0240",
            title="Regulatory Typology 0240: Financial crime pattern 240",
            advisory_source="FinCEN Advisory FIN-2021-A007",
            risk_tier="CRITICAL",
            indicators=["Red flag A_240", "Red flag B_240", "Red flag C_240"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 240."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0241",
            title="Regulatory Typology 0241: Financial crime pattern 241",
            advisory_source="FinCEN Advisory FIN-2022-A008",
            risk_tier="HIGH",
            indicators=["Red flag A_241", "Red flag B_241", "Red flag C_241"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 241."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0242",
            title="Regulatory Typology 0242: Financial crime pattern 242",
            advisory_source="FinCEN Advisory FIN-2023-A009",
            risk_tier="MEDIUM",
            indicators=["Red flag A_242", "Red flag B_242", "Red flag C_242"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 242."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0243",
            title="Regulatory Typology 0243: Financial crime pattern 243",
            advisory_source="FinCEN Advisory FIN-2024-A001",
            risk_tier="LOW",
            indicators=["Red flag A_243", "Red flag B_243", "Red flag C_243"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 243."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0244",
            title="Regulatory Typology 0244: Financial crime pattern 244",
            advisory_source="FinCEN Advisory FIN-2025-A002",
            risk_tier="CRITICAL",
            indicators=["Red flag A_244", "Red flag B_244", "Red flag C_244"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 244."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0245",
            title="Regulatory Typology 0245: Financial crime pattern 245",
            advisory_source="FinCEN Advisory FIN-2021-A003",
            risk_tier="HIGH",
            indicators=["Red flag A_245", "Red flag B_245", "Red flag C_245"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 245."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0246",
            title="Regulatory Typology 0246: Financial crime pattern 246",
            advisory_source="FinCEN Advisory FIN-2022-A004",
            risk_tier="MEDIUM",
            indicators=["Red flag A_246", "Red flag B_246", "Red flag C_246"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 246."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0247",
            title="Regulatory Typology 0247: Financial crime pattern 247",
            advisory_source="FinCEN Advisory FIN-2023-A005",
            risk_tier="LOW",
            indicators=["Red flag A_247", "Red flag B_247", "Red flag C_247"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 247."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0248",
            title="Regulatory Typology 0248: Financial crime pattern 248",
            advisory_source="FinCEN Advisory FIN-2024-A006",
            risk_tier="CRITICAL",
            indicators=["Red flag A_248", "Red flag B_248", "Red flag C_248"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 248."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0249",
            title="Regulatory Typology 0249: Financial crime pattern 249",
            advisory_source="FinCEN Advisory FIN-2025-A007",
            risk_tier="HIGH",
            indicators=["Red flag A_249", "Red flag B_249", "Red flag C_249"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 249."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0250",
            title="Regulatory Typology 0250: Financial crime pattern 250",
            advisory_source="FinCEN Advisory FIN-2021-A008",
            risk_tier="MEDIUM",
            indicators=["Red flag A_250", "Red flag B_250", "Red flag C_250"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 250."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0251",
            title="Regulatory Typology 0251: Financial crime pattern 251",
            advisory_source="FinCEN Advisory FIN-2022-A009",
            risk_tier="LOW",
            indicators=["Red flag A_251", "Red flag B_251", "Red flag C_251"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 251."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0252",
            title="Regulatory Typology 0252: Financial crime pattern 252",
            advisory_source="FinCEN Advisory FIN-2023-A001",
            risk_tier="CRITICAL",
            indicators=["Red flag A_252", "Red flag B_252", "Red flag C_252"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 252."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0253",
            title="Regulatory Typology 0253: Financial crime pattern 253",
            advisory_source="FinCEN Advisory FIN-2024-A002",
            risk_tier="HIGH",
            indicators=["Red flag A_253", "Red flag B_253", "Red flag C_253"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 253."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0254",
            title="Regulatory Typology 0254: Financial crime pattern 254",
            advisory_source="FinCEN Advisory FIN-2025-A003",
            risk_tier="MEDIUM",
            indicators=["Red flag A_254", "Red flag B_254", "Red flag C_254"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 254."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0255",
            title="Regulatory Typology 0255: Financial crime pattern 255",
            advisory_source="FinCEN Advisory FIN-2021-A004",
            risk_tier="LOW",
            indicators=["Red flag A_255", "Red flag B_255", "Red flag C_255"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 255."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0256",
            title="Regulatory Typology 0256: Financial crime pattern 256",
            advisory_source="FinCEN Advisory FIN-2022-A005",
            risk_tier="CRITICAL",
            indicators=["Red flag A_256", "Red flag B_256", "Red flag C_256"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 256."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0257",
            title="Regulatory Typology 0257: Financial crime pattern 257",
            advisory_source="FinCEN Advisory FIN-2023-A006",
            risk_tier="HIGH",
            indicators=["Red flag A_257", "Red flag B_257", "Red flag C_257"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 257."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0258",
            title="Regulatory Typology 0258: Financial crime pattern 258",
            advisory_source="FinCEN Advisory FIN-2024-A007",
            risk_tier="MEDIUM",
            indicators=["Red flag A_258", "Red flag B_258", "Red flag C_258"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 258."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0259",
            title="Regulatory Typology 0259: Financial crime pattern 259",
            advisory_source="FinCEN Advisory FIN-2025-A008",
            risk_tier="LOW",
            indicators=["Red flag A_259", "Red flag B_259", "Red flag C_259"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 259."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0260",
            title="Regulatory Typology 0260: Financial crime pattern 260",
            advisory_source="FinCEN Advisory FIN-2021-A009",
            risk_tier="CRITICAL",
            indicators=["Red flag A_260", "Red flag B_260", "Red flag C_260"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 260."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0261",
            title="Regulatory Typology 0261: Financial crime pattern 261",
            advisory_source="FinCEN Advisory FIN-2022-A001",
            risk_tier="HIGH",
            indicators=["Red flag A_261", "Red flag B_261", "Red flag C_261"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 261."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0262",
            title="Regulatory Typology 0262: Financial crime pattern 262",
            advisory_source="FinCEN Advisory FIN-2023-A002",
            risk_tier="MEDIUM",
            indicators=["Red flag A_262", "Red flag B_262", "Red flag C_262"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 262."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0263",
            title="Regulatory Typology 0263: Financial crime pattern 263",
            advisory_source="FinCEN Advisory FIN-2024-A003",
            risk_tier="LOW",
            indicators=["Red flag A_263", "Red flag B_263", "Red flag C_263"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 263."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0264",
            title="Regulatory Typology 0264: Financial crime pattern 264",
            advisory_source="FinCEN Advisory FIN-2025-A004",
            risk_tier="CRITICAL",
            indicators=["Red flag A_264", "Red flag B_264", "Red flag C_264"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 264."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0265",
            title="Regulatory Typology 0265: Financial crime pattern 265",
            advisory_source="FinCEN Advisory FIN-2021-A005",
            risk_tier="HIGH",
            indicators=["Red flag A_265", "Red flag B_265", "Red flag C_265"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 265."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0266",
            title="Regulatory Typology 0266: Financial crime pattern 266",
            advisory_source="FinCEN Advisory FIN-2022-A006",
            risk_tier="MEDIUM",
            indicators=["Red flag A_266", "Red flag B_266", "Red flag C_266"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 266."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0267",
            title="Regulatory Typology 0267: Financial crime pattern 267",
            advisory_source="FinCEN Advisory FIN-2023-A007",
            risk_tier="LOW",
            indicators=["Red flag A_267", "Red flag B_267", "Red flag C_267"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 267."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0268",
            title="Regulatory Typology 0268: Financial crime pattern 268",
            advisory_source="FinCEN Advisory FIN-2024-A008",
            risk_tier="CRITICAL",
            indicators=["Red flag A_268", "Red flag B_268", "Red flag C_268"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 268."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0269",
            title="Regulatory Typology 0269: Financial crime pattern 269",
            advisory_source="FinCEN Advisory FIN-2025-A009",
            risk_tier="HIGH",
            indicators=["Red flag A_269", "Red flag B_269", "Red flag C_269"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 269."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0270",
            title="Regulatory Typology 0270: Financial crime pattern 270",
            advisory_source="FinCEN Advisory FIN-2021-A001",
            risk_tier="MEDIUM",
            indicators=["Red flag A_270", "Red flag B_270", "Red flag C_270"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 270."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0271",
            title="Regulatory Typology 0271: Financial crime pattern 271",
            advisory_source="FinCEN Advisory FIN-2022-A002",
            risk_tier="LOW",
            indicators=["Red flag A_271", "Red flag B_271", "Red flag C_271"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 271."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0272",
            title="Regulatory Typology 0272: Financial crime pattern 272",
            advisory_source="FinCEN Advisory FIN-2023-A003",
            risk_tier="CRITICAL",
            indicators=["Red flag A_272", "Red flag B_272", "Red flag C_272"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 272."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0273",
            title="Regulatory Typology 0273: Financial crime pattern 273",
            advisory_source="FinCEN Advisory FIN-2024-A004",
            risk_tier="HIGH",
            indicators=["Red flag A_273", "Red flag B_273", "Red flag C_273"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 273."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0274",
            title="Regulatory Typology 0274: Financial crime pattern 274",
            advisory_source="FinCEN Advisory FIN-2025-A005",
            risk_tier="MEDIUM",
            indicators=["Red flag A_274", "Red flag B_274", "Red flag C_274"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 274."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0275",
            title="Regulatory Typology 0275: Financial crime pattern 275",
            advisory_source="FinCEN Advisory FIN-2021-A006",
            risk_tier="LOW",
            indicators=["Red flag A_275", "Red flag B_275", "Red flag C_275"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 275."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0276",
            title="Regulatory Typology 0276: Financial crime pattern 276",
            advisory_source="FinCEN Advisory FIN-2022-A007",
            risk_tier="CRITICAL",
            indicators=["Red flag A_276", "Red flag B_276", "Red flag C_276"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 276."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0277",
            title="Regulatory Typology 0277: Financial crime pattern 277",
            advisory_source="FinCEN Advisory FIN-2023-A008",
            risk_tier="HIGH",
            indicators=["Red flag A_277", "Red flag B_277", "Red flag C_277"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 277."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0278",
            title="Regulatory Typology 0278: Financial crime pattern 278",
            advisory_source="FinCEN Advisory FIN-2024-A009",
            risk_tier="MEDIUM",
            indicators=["Red flag A_278", "Red flag B_278", "Red flag C_278"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 278."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0279",
            title="Regulatory Typology 0279: Financial crime pattern 279",
            advisory_source="FinCEN Advisory FIN-2025-A001",
            risk_tier="LOW",
            indicators=["Red flag A_279", "Red flag B_279", "Red flag C_279"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 279."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0280",
            title="Regulatory Typology 0280: Financial crime pattern 280",
            advisory_source="FinCEN Advisory FIN-2021-A002",
            risk_tier="CRITICAL",
            indicators=["Red flag A_280", "Red flag B_280", "Red flag C_280"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 280."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0281",
            title="Regulatory Typology 0281: Financial crime pattern 281",
            advisory_source="FinCEN Advisory FIN-2022-A003",
            risk_tier="HIGH",
            indicators=["Red flag A_281", "Red flag B_281", "Red flag C_281"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 281."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0282",
            title="Regulatory Typology 0282: Financial crime pattern 282",
            advisory_source="FinCEN Advisory FIN-2023-A004",
            risk_tier="MEDIUM",
            indicators=["Red flag A_282", "Red flag B_282", "Red flag C_282"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 282."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0283",
            title="Regulatory Typology 0283: Financial crime pattern 283",
            advisory_source="FinCEN Advisory FIN-2024-A005",
            risk_tier="LOW",
            indicators=["Red flag A_283", "Red flag B_283", "Red flag C_283"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 283."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0284",
            title="Regulatory Typology 0284: Financial crime pattern 284",
            advisory_source="FinCEN Advisory FIN-2025-A006",
            risk_tier="CRITICAL",
            indicators=["Red flag A_284", "Red flag B_284", "Red flag C_284"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 284."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0285",
            title="Regulatory Typology 0285: Financial crime pattern 285",
            advisory_source="FinCEN Advisory FIN-2021-A007",
            risk_tier="HIGH",
            indicators=["Red flag A_285", "Red flag B_285", "Red flag C_285"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 285."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0286",
            title="Regulatory Typology 0286: Financial crime pattern 286",
            advisory_source="FinCEN Advisory FIN-2022-A008",
            risk_tier="MEDIUM",
            indicators=["Red flag A_286", "Red flag B_286", "Red flag C_286"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 286."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0287",
            title="Regulatory Typology 0287: Financial crime pattern 287",
            advisory_source="FinCEN Advisory FIN-2023-A009",
            risk_tier="LOW",
            indicators=["Red flag A_287", "Red flag B_287", "Red flag C_287"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 287."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0288",
            title="Regulatory Typology 0288: Financial crime pattern 288",
            advisory_source="FinCEN Advisory FIN-2024-A001",
            risk_tier="CRITICAL",
            indicators=["Red flag A_288", "Red flag B_288", "Red flag C_288"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 288."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0289",
            title="Regulatory Typology 0289: Financial crime pattern 289",
            advisory_source="FinCEN Advisory FIN-2025-A002",
            risk_tier="HIGH",
            indicators=["Red flag A_289", "Red flag B_289", "Red flag C_289"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 289."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0290",
            title="Regulatory Typology 0290: Financial crime pattern 290",
            advisory_source="FinCEN Advisory FIN-2021-A003",
            risk_tier="MEDIUM",
            indicators=["Red flag A_290", "Red flag B_290", "Red flag C_290"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 290."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0291",
            title="Regulatory Typology 0291: Financial crime pattern 291",
            advisory_source="FinCEN Advisory FIN-2022-A004",
            risk_tier="LOW",
            indicators=["Red flag A_291", "Red flag B_291", "Red flag C_291"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 291."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0292",
            title="Regulatory Typology 0292: Financial crime pattern 292",
            advisory_source="FinCEN Advisory FIN-2023-A005",
            risk_tier="CRITICAL",
            indicators=["Red flag A_292", "Red flag B_292", "Red flag C_292"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 292."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0293",
            title="Regulatory Typology 0293: Financial crime pattern 293",
            advisory_source="FinCEN Advisory FIN-2024-A006",
            risk_tier="HIGH",
            indicators=["Red flag A_293", "Red flag B_293", "Red flag C_293"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 293."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0294",
            title="Regulatory Typology 0294: Financial crime pattern 294",
            advisory_source="FinCEN Advisory FIN-2025-A007",
            risk_tier="MEDIUM",
            indicators=["Red flag A_294", "Red flag B_294", "Red flag C_294"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 294."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0295",
            title="Regulatory Typology 0295: Financial crime pattern 295",
            advisory_source="FinCEN Advisory FIN-2021-A008",
            risk_tier="LOW",
            indicators=["Red flag A_295", "Red flag B_295", "Red flag C_295"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 295."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0296",
            title="Regulatory Typology 0296: Financial crime pattern 296",
            advisory_source="FinCEN Advisory FIN-2022-A009",
            risk_tier="CRITICAL",
            indicators=["Red flag A_296", "Red flag B_296", "Red flag C_296"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 296."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0297",
            title="Regulatory Typology 0297: Financial crime pattern 297",
            advisory_source="FinCEN Advisory FIN-2023-A001",
            risk_tier="HIGH",
            indicators=["Red flag A_297", "Red flag B_297", "Red flag C_297"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 297."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0298",
            title="Regulatory Typology 0298: Financial crime pattern 298",
            advisory_source="FinCEN Advisory FIN-2024-A002",
            risk_tier="MEDIUM",
            indicators=["Red flag A_298", "Red flag B_298", "Red flag C_298"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 298."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0299",
            title="Regulatory Typology 0299: Financial crime pattern 299",
            advisory_source="FinCEN Advisory FIN-2025-A003",
            risk_tier="LOW",
            indicators=["Red flag A_299", "Red flag B_299", "Red flag C_299"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 299."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0300",
            title="Regulatory Typology 0300: Financial crime pattern 300",
            advisory_source="FinCEN Advisory FIN-2021-A004",
            risk_tier="CRITICAL",
            indicators=["Red flag A_300", "Red flag B_300", "Red flag C_300"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 300."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0301",
            title="Regulatory Typology 0301: Financial crime pattern 301",
            advisory_source="FinCEN Advisory FIN-2022-A005",
            risk_tier="HIGH",
            indicators=["Red flag A_301", "Red flag B_301", "Red flag C_301"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 301."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0302",
            title="Regulatory Typology 0302: Financial crime pattern 302",
            advisory_source="FinCEN Advisory FIN-2023-A006",
            risk_tier="MEDIUM",
            indicators=["Red flag A_302", "Red flag B_302", "Red flag C_302"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 302."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0303",
            title="Regulatory Typology 0303: Financial crime pattern 303",
            advisory_source="FinCEN Advisory FIN-2024-A007",
            risk_tier="LOW",
            indicators=["Red flag A_303", "Red flag B_303", "Red flag C_303"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 303."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0304",
            title="Regulatory Typology 0304: Financial crime pattern 304",
            advisory_source="FinCEN Advisory FIN-2025-A008",
            risk_tier="CRITICAL",
            indicators=["Red flag A_304", "Red flag B_304", "Red flag C_304"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 304."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0305",
            title="Regulatory Typology 0305: Financial crime pattern 305",
            advisory_source="FinCEN Advisory FIN-2021-A009",
            risk_tier="HIGH",
            indicators=["Red flag A_305", "Red flag B_305", "Red flag C_305"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 305."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0306",
            title="Regulatory Typology 0306: Financial crime pattern 306",
            advisory_source="FinCEN Advisory FIN-2022-A001",
            risk_tier="MEDIUM",
            indicators=["Red flag A_306", "Red flag B_306", "Red flag C_306"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 306."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0307",
            title="Regulatory Typology 0307: Financial crime pattern 307",
            advisory_source="FinCEN Advisory FIN-2023-A002",
            risk_tier="LOW",
            indicators=["Red flag A_307", "Red flag B_307", "Red flag C_307"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 307."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0308",
            title="Regulatory Typology 0308: Financial crime pattern 308",
            advisory_source="FinCEN Advisory FIN-2024-A003",
            risk_tier="CRITICAL",
            indicators=["Red flag A_308", "Red flag B_308", "Red flag C_308"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 308."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0309",
            title="Regulatory Typology 0309: Financial crime pattern 309",
            advisory_source="FinCEN Advisory FIN-2025-A004",
            risk_tier="HIGH",
            indicators=["Red flag A_309", "Red flag B_309", "Red flag C_309"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 309."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0310",
            title="Regulatory Typology 0310: Financial crime pattern 310",
            advisory_source="FinCEN Advisory FIN-2021-A005",
            risk_tier="MEDIUM",
            indicators=["Red flag A_310", "Red flag B_310", "Red flag C_310"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 310."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0311",
            title="Regulatory Typology 0311: Financial crime pattern 311",
            advisory_source="FinCEN Advisory FIN-2022-A006",
            risk_tier="LOW",
            indicators=["Red flag A_311", "Red flag B_311", "Red flag C_311"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 311."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0312",
            title="Regulatory Typology 0312: Financial crime pattern 312",
            advisory_source="FinCEN Advisory FIN-2023-A007",
            risk_tier="CRITICAL",
            indicators=["Red flag A_312", "Red flag B_312", "Red flag C_312"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 312."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0313",
            title="Regulatory Typology 0313: Financial crime pattern 313",
            advisory_source="FinCEN Advisory FIN-2024-A008",
            risk_tier="HIGH",
            indicators=["Red flag A_313", "Red flag B_313", "Red flag C_313"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 313."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0314",
            title="Regulatory Typology 0314: Financial crime pattern 314",
            advisory_source="FinCEN Advisory FIN-2025-A009",
            risk_tier="MEDIUM",
            indicators=["Red flag A_314", "Red flag B_314", "Red flag C_314"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 314."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0315",
            title="Regulatory Typology 0315: Financial crime pattern 315",
            advisory_source="FinCEN Advisory FIN-2021-A001",
            risk_tier="LOW",
            indicators=["Red flag A_315", "Red flag B_315", "Red flag C_315"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 315."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0316",
            title="Regulatory Typology 0316: Financial crime pattern 316",
            advisory_source="FinCEN Advisory FIN-2022-A002",
            risk_tier="CRITICAL",
            indicators=["Red flag A_316", "Red flag B_316", "Red flag C_316"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 316."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0317",
            title="Regulatory Typology 0317: Financial crime pattern 317",
            advisory_source="FinCEN Advisory FIN-2023-A003",
            risk_tier="HIGH",
            indicators=["Red flag A_317", "Red flag B_317", "Red flag C_317"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 317."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0318",
            title="Regulatory Typology 0318: Financial crime pattern 318",
            advisory_source="FinCEN Advisory FIN-2024-A004",
            risk_tier="MEDIUM",
            indicators=["Red flag A_318", "Red flag B_318", "Red flag C_318"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 318."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0319",
            title="Regulatory Typology 0319: Financial crime pattern 319",
            advisory_source="FinCEN Advisory FIN-2025-A005",
            risk_tier="LOW",
            indicators=["Red flag A_319", "Red flag B_319", "Red flag C_319"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 319."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0320",
            title="Regulatory Typology 0320: Financial crime pattern 320",
            advisory_source="FinCEN Advisory FIN-2021-A006",
            risk_tier="CRITICAL",
            indicators=["Red flag A_320", "Red flag B_320", "Red flag C_320"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 320."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0321",
            title="Regulatory Typology 0321: Financial crime pattern 321",
            advisory_source="FinCEN Advisory FIN-2022-A007",
            risk_tier="HIGH",
            indicators=["Red flag A_321", "Red flag B_321", "Red flag C_321"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 321."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0322",
            title="Regulatory Typology 0322: Financial crime pattern 322",
            advisory_source="FinCEN Advisory FIN-2023-A008",
            risk_tier="MEDIUM",
            indicators=["Red flag A_322", "Red flag B_322", "Red flag C_322"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 322."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0323",
            title="Regulatory Typology 0323: Financial crime pattern 323",
            advisory_source="FinCEN Advisory FIN-2024-A009",
            risk_tier="LOW",
            indicators=["Red flag A_323", "Red flag B_323", "Red flag C_323"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 323."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0324",
            title="Regulatory Typology 0324: Financial crime pattern 324",
            advisory_source="FinCEN Advisory FIN-2025-A001",
            risk_tier="CRITICAL",
            indicators=["Red flag A_324", "Red flag B_324", "Red flag C_324"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 324."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0325",
            title="Regulatory Typology 0325: Financial crime pattern 325",
            advisory_source="FinCEN Advisory FIN-2021-A002",
            risk_tier="HIGH",
            indicators=["Red flag A_325", "Red flag B_325", "Red flag C_325"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 325."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0326",
            title="Regulatory Typology 0326: Financial crime pattern 326",
            advisory_source="FinCEN Advisory FIN-2022-A003",
            risk_tier="MEDIUM",
            indicators=["Red flag A_326", "Red flag B_326", "Red flag C_326"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 326."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0327",
            title="Regulatory Typology 0327: Financial crime pattern 327",
            advisory_source="FinCEN Advisory FIN-2023-A004",
            risk_tier="LOW",
            indicators=["Red flag A_327", "Red flag B_327", "Red flag C_327"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 327."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0328",
            title="Regulatory Typology 0328: Financial crime pattern 328",
            advisory_source="FinCEN Advisory FIN-2024-A005",
            risk_tier="CRITICAL",
            indicators=["Red flag A_328", "Red flag B_328", "Red flag C_328"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 328."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0329",
            title="Regulatory Typology 0329: Financial crime pattern 329",
            advisory_source="FinCEN Advisory FIN-2025-A006",
            risk_tier="HIGH",
            indicators=["Red flag A_329", "Red flag B_329", "Red flag C_329"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 329."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0330",
            title="Regulatory Typology 0330: Financial crime pattern 330",
            advisory_source="FinCEN Advisory FIN-2021-A007",
            risk_tier="MEDIUM",
            indicators=["Red flag A_330", "Red flag B_330", "Red flag C_330"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 330."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0331",
            title="Regulatory Typology 0331: Financial crime pattern 331",
            advisory_source="FinCEN Advisory FIN-2022-A008",
            risk_tier="LOW",
            indicators=["Red flag A_331", "Red flag B_331", "Red flag C_331"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 331."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0332",
            title="Regulatory Typology 0332: Financial crime pattern 332",
            advisory_source="FinCEN Advisory FIN-2023-A009",
            risk_tier="CRITICAL",
            indicators=["Red flag A_332", "Red flag B_332", "Red flag C_332"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 332."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0333",
            title="Regulatory Typology 0333: Financial crime pattern 333",
            advisory_source="FinCEN Advisory FIN-2024-A001",
            risk_tier="HIGH",
            indicators=["Red flag A_333", "Red flag B_333", "Red flag C_333"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 333."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0334",
            title="Regulatory Typology 0334: Financial crime pattern 334",
            advisory_source="FinCEN Advisory FIN-2025-A002",
            risk_tier="MEDIUM",
            indicators=["Red flag A_334", "Red flag B_334", "Red flag C_334"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 334."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0335",
            title="Regulatory Typology 0335: Financial crime pattern 335",
            advisory_source="FinCEN Advisory FIN-2021-A003",
            risk_tier="LOW",
            indicators=["Red flag A_335", "Red flag B_335", "Red flag C_335"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 335."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0336",
            title="Regulatory Typology 0336: Financial crime pattern 336",
            advisory_source="FinCEN Advisory FIN-2022-A004",
            risk_tier="CRITICAL",
            indicators=["Red flag A_336", "Red flag B_336", "Red flag C_336"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 336."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0337",
            title="Regulatory Typology 0337: Financial crime pattern 337",
            advisory_source="FinCEN Advisory FIN-2023-A005",
            risk_tier="HIGH",
            indicators=["Red flag A_337", "Red flag B_337", "Red flag C_337"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 337."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0338",
            title="Regulatory Typology 0338: Financial crime pattern 338",
            advisory_source="FinCEN Advisory FIN-2024-A006",
            risk_tier="MEDIUM",
            indicators=["Red flag A_338", "Red flag B_338", "Red flag C_338"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 338."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0339",
            title="Regulatory Typology 0339: Financial crime pattern 339",
            advisory_source="FinCEN Advisory FIN-2025-A007",
            risk_tier="LOW",
            indicators=["Red flag A_339", "Red flag B_339", "Red flag C_339"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 339."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0340",
            title="Regulatory Typology 0340: Financial crime pattern 340",
            advisory_source="FinCEN Advisory FIN-2021-A008",
            risk_tier="CRITICAL",
            indicators=["Red flag A_340", "Red flag B_340", "Red flag C_340"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 340."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0341",
            title="Regulatory Typology 0341: Financial crime pattern 341",
            advisory_source="FinCEN Advisory FIN-2022-A009",
            risk_tier="HIGH",
            indicators=["Red flag A_341", "Red flag B_341", "Red flag C_341"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 341."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0342",
            title="Regulatory Typology 0342: Financial crime pattern 342",
            advisory_source="FinCEN Advisory FIN-2023-A001",
            risk_tier="MEDIUM",
            indicators=["Red flag A_342", "Red flag B_342", "Red flag C_342"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 342."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0343",
            title="Regulatory Typology 0343: Financial crime pattern 343",
            advisory_source="FinCEN Advisory FIN-2024-A002",
            risk_tier="LOW",
            indicators=["Red flag A_343", "Red flag B_343", "Red flag C_343"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 343."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0344",
            title="Regulatory Typology 0344: Financial crime pattern 344",
            advisory_source="FinCEN Advisory FIN-2025-A003",
            risk_tier="CRITICAL",
            indicators=["Red flag A_344", "Red flag B_344", "Red flag C_344"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 344."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0345",
            title="Regulatory Typology 0345: Financial crime pattern 345",
            advisory_source="FinCEN Advisory FIN-2021-A004",
            risk_tier="HIGH",
            indicators=["Red flag A_345", "Red flag B_345", "Red flag C_345"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 345."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0346",
            title="Regulatory Typology 0346: Financial crime pattern 346",
            advisory_source="FinCEN Advisory FIN-2022-A005",
            risk_tier="MEDIUM",
            indicators=["Red flag A_346", "Red flag B_346", "Red flag C_346"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 346."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0347",
            title="Regulatory Typology 0347: Financial crime pattern 347",
            advisory_source="FinCEN Advisory FIN-2023-A006",
            risk_tier="LOW",
            indicators=["Red flag A_347", "Red flag B_347", "Red flag C_347"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 347."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0348",
            title="Regulatory Typology 0348: Financial crime pattern 348",
            advisory_source="FinCEN Advisory FIN-2024-A007",
            risk_tier="CRITICAL",
            indicators=["Red flag A_348", "Red flag B_348", "Red flag C_348"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 348."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0349",
            title="Regulatory Typology 0349: Financial crime pattern 349",
            advisory_source="FinCEN Advisory FIN-2025-A008",
            risk_tier="HIGH",
            indicators=["Red flag A_349", "Red flag B_349", "Red flag C_349"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 349."
        ))
        self.register(RegulatoryTypology(
            typology_id="TYP_FINCEN_0350",
            title="Regulatory Typology 0350: Financial crime pattern 350",
            advisory_source="FinCEN Advisory FIN-2021-A009",
            risk_tier="MEDIUM",
            indicators=["Red flag A_350", "Red flag B_350", "Red flag C_350"],
            investigative_guidelines="Examine multi-jurisdictional clearing records and interview remitter regarding legitimate economic rationale 350."
        ))

typology_registry = MasterTypologyRegistry()

class TypologyFilterPartition_1:
    """Filters regulatory advisories by statutory risk tier (partition 1)."""
    def __init__(self):
        self.partition_id = 1
    def filter_tier(self, typologies: List[RegulatoryTypology], target_tier: str) -> List[RegulatoryTypology]:
        return [t for t in typologies if t.risk_tier == target_tier]

class TypologyFilterPartition_2:
    """Filters regulatory advisories by statutory risk tier (partition 2)."""
    def __init__(self):
        self.partition_id = 2
    def filter_tier(self, typologies: List[RegulatoryTypology], target_tier: str) -> List[RegulatoryTypology]:
        return [t for t in typologies if t.risk_tier == target_tier]

class TypologyFilterPartition_3:
    """Filters regulatory advisories by statutory risk tier (partition 3)."""
    def __init__(self):
        self.partition_id = 3
    def filter_tier(self, typologies: List[RegulatoryTypology], target_tier: str) -> List[RegulatoryTypology]:
        return [t for t in typologies if t.risk_tier == target_tier]

class TypologyFilterPartition_4:
    """Filters regulatory advisories by statutory risk tier (partition 4)."""
    def __init__(self):
        self.partition_id = 4
    def filter_tier(self, typologies: List[RegulatoryTypology], target_tier: str) -> List[RegulatoryTypology]:
        return [t for t in typologies if t.risk_tier == target_tier]

class TypologyFilterPartition_5:
    """Filters regulatory advisories by statutory risk tier (partition 5)."""
    def __init__(self):
        self.partition_id = 5
    def filter_tier(self, typologies: List[RegulatoryTypology], target_tier: str) -> List[RegulatoryTypology]:
        return [t for t in typologies if t.risk_tier == target_tier]

class TypologyFilterPartition_6:
    """Filters regulatory advisories by statutory risk tier (partition 6)."""
    def __init__(self):
        self.partition_id = 6
    def filter_tier(self, typologies: List[RegulatoryTypology], target_tier: str) -> List[RegulatoryTypology]:
        return [t for t in typologies if t.risk_tier == target_tier]

class TypologyFilterPartition_7:
    """Filters regulatory advisories by statutory risk tier (partition 7)."""
    def __init__(self):
        self.partition_id = 7
    def filter_tier(self, typologies: List[RegulatoryTypology], target_tier: str) -> List[RegulatoryTypology]:
        return [t for t in typologies if t.risk_tier == target_tier]

class TypologyFilterPartition_8:
    """Filters regulatory advisories by statutory risk tier (partition 8)."""
    def __init__(self):
        self.partition_id = 8
    def filter_tier(self, typologies: List[RegulatoryTypology], target_tier: str) -> List[RegulatoryTypology]:
        return [t for t in typologies if t.risk_tier == target_tier]

class TypologyFilterPartition_9:
    """Filters regulatory advisories by statutory risk tier (partition 9)."""
    def __init__(self):
        self.partition_id = 9
    def filter_tier(self, typologies: List[RegulatoryTypology], target_tier: str) -> List[RegulatoryTypology]:
        return [t for t in typologies if t.risk_tier == target_tier]

class TypologyFilterPartition_10:
    """Filters regulatory advisories by statutory risk tier (partition 10)."""
    def __init__(self):
        self.partition_id = 10
    def filter_tier(self, typologies: List[RegulatoryTypology], target_tier: str) -> List[RegulatoryTypology]:
        return [t for t in typologies if t.risk_tier == target_tier]

class TypologyFilterPartition_11:
    """Filters regulatory advisories by statutory risk tier (partition 11)."""
    def __init__(self):
        self.partition_id = 11
    def filter_tier(self, typologies: List[RegulatoryTypology], target_tier: str) -> List[RegulatoryTypology]:
        return [t for t in typologies if t.risk_tier == target_tier]

class TypologyFilterPartition_12:
    """Filters regulatory advisories by statutory risk tier (partition 12)."""
    def __init__(self):
        self.partition_id = 12
    def filter_tier(self, typologies: List[RegulatoryTypology], target_tier: str) -> List[RegulatoryTypology]:
        return [t for t in typologies if t.risk_tier == target_tier]

class TypologyFilterPartition_13:
    """Filters regulatory advisories by statutory risk tier (partition 13)."""
    def __init__(self):
        self.partition_id = 13
    def filter_tier(self, typologies: List[RegulatoryTypology], target_tier: str) -> List[RegulatoryTypology]:
        return [t for t in typologies if t.risk_tier == target_tier]

class TypologyFilterPartition_14:
    """Filters regulatory advisories by statutory risk tier (partition 14)."""
    def __init__(self):
        self.partition_id = 14
    def filter_tier(self, typologies: List[RegulatoryTypology], target_tier: str) -> List[RegulatoryTypology]:
        return [t for t in typologies if t.risk_tier == target_tier]

class TypologyFilterPartition_15:
    """Filters regulatory advisories by statutory risk tier (partition 15)."""
    def __init__(self):
        self.partition_id = 15
    def filter_tier(self, typologies: List[RegulatoryTypology], target_tier: str) -> List[RegulatoryTypology]:
        return [t for t in typologies if t.risk_tier == target_tier]

class TypologyFilterPartition_16:
    """Filters regulatory advisories by statutory risk tier (partition 16)."""
    def __init__(self):
        self.partition_id = 16
    def filter_tier(self, typologies: List[RegulatoryTypology], target_tier: str) -> List[RegulatoryTypology]:
        return [t for t in typologies if t.risk_tier == target_tier]

class TypologyFilterPartition_17:
    """Filters regulatory advisories by statutory risk tier (partition 17)."""
    def __init__(self):
        self.partition_id = 17
    def filter_tier(self, typologies: List[RegulatoryTypology], target_tier: str) -> List[RegulatoryTypology]:
        return [t for t in typologies if t.risk_tier == target_tier]

class TypologyFilterPartition_18:
    """Filters regulatory advisories by statutory risk tier (partition 18)."""
    def __init__(self):
        self.partition_id = 18
    def filter_tier(self, typologies: List[RegulatoryTypology], target_tier: str) -> List[RegulatoryTypology]:
        return [t for t in typologies if t.risk_tier == target_tier]

class TypologyFilterPartition_19:
    """Filters regulatory advisories by statutory risk tier (partition 19)."""
    def __init__(self):
        self.partition_id = 19
    def filter_tier(self, typologies: List[RegulatoryTypology], target_tier: str) -> List[RegulatoryTypology]:
        return [t for t in typologies if t.risk_tier == target_tier]

class TypologyFilterPartition_20:
    """Filters regulatory advisories by statutory risk tier (partition 20)."""
    def __init__(self):
        self.partition_id = 20
    def filter_tier(self, typologies: List[RegulatoryTypology], target_tier: str) -> List[RegulatoryTypology]:
        return [t for t in typologies if t.risk_tier == target_tier]

class TypologyFilterPartition_21:
    """Filters regulatory advisories by statutory risk tier (partition 21)."""
    def __init__(self):
        self.partition_id = 21
    def filter_tier(self, typologies: List[RegulatoryTypology], target_tier: str) -> List[RegulatoryTypology]:
        return [t for t in typologies if t.risk_tier == target_tier]

class TypologyFilterPartition_22:
    """Filters regulatory advisories by statutory risk tier (partition 22)."""
    def __init__(self):
        self.partition_id = 22
    def filter_tier(self, typologies: List[RegulatoryTypology], target_tier: str) -> List[RegulatoryTypology]:
        return [t for t in typologies if t.risk_tier == target_tier]

class TypologyFilterPartition_23:
    """Filters regulatory advisories by statutory risk tier (partition 23)."""
    def __init__(self):
        self.partition_id = 23
    def filter_tier(self, typologies: List[RegulatoryTypology], target_tier: str) -> List[RegulatoryTypology]:
        return [t for t in typologies if t.risk_tier == target_tier]

class TypologyFilterPartition_24:
    """Filters regulatory advisories by statutory risk tier (partition 24)."""
    def __init__(self):
        self.partition_id = 24
    def filter_tier(self, typologies: List[RegulatoryTypology], target_tier: str) -> List[RegulatoryTypology]:
        return [t for t in typologies if t.risk_tier == target_tier]