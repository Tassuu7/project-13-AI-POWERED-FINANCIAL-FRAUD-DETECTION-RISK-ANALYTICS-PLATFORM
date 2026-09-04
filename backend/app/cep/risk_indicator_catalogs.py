"""
Aegis Fraud Labs – Master Financial Fraud Indicator & Typology Matrix
Defines 300+ granular behavioral, transactional, and cyber indicators across all payment rails.
"""
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
from enum import Enum

class IndicatorRail(Enum):
    ACH = "ACH"
    WIRE = "WIRE"
    CARD_POS = "CARD_POS"
    CARD_CNP = "CARD_CNP"
    UPI = "UPI"
    CRYPTO = "CRYPTO"
    ATM = "ATM"
    INTERNAL_BOOK = "INTERNAL_BOOK"

@dataclass
class FraudIndicator:
    indicator_id: str
    name: str
    rail: IndicatorRail
    risk_points: int
    detection_method: str
    regulatory_reference: str
    mitigation_action: str

class MasterIndicatorCatalog:
    def __init__(self):
        self.indicators: Dict[str, FraudIndicator] = {}
        self._init_indicators()

    def register(self, ind: FraudIndicator):
        self.indicators[ind.indicator_id] = ind

    def _init_indicators(self):
        self.register(FraudIndicator(
            indicator_id="IND_0001",
            name="Indicator 0001: Anomaly signature for WIRE",
            rail=IndicatorRail.WIRE,
            risk_points=21,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 101",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0002",
            name="Indicator 0002: Anomaly signature for CARD_POS",
            rail=IndicatorRail.CARD_POS,
            risk_points=22,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 102",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0003",
            name="Indicator 0003: Anomaly signature for CARD_CNP",
            rail=IndicatorRail.CARD_CNP,
            risk_points=23,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 103",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0004",
            name="Indicator 0004: Anomaly signature for UPI",
            rail=IndicatorRail.UPI,
            risk_points=24,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 104",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0005",
            name="Indicator 0005: Anomaly signature for CRYPTO",
            rail=IndicatorRail.CRYPTO,
            risk_points=25,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 105",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0006",
            name="Indicator 0006: Anomaly signature for ATM",
            rail=IndicatorRail.ATM,
            risk_points=26,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 106",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0007",
            name="Indicator 0007: Anomaly signature for INTERNAL_BOOK",
            rail=IndicatorRail.INTERNAL_BOOK,
            risk_points=27,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 107",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0008",
            name="Indicator 0008: Anomaly signature for ACH",
            rail=IndicatorRail.ACH,
            risk_points=28,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 108",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0009",
            name="Indicator 0009: Anomaly signature for WIRE",
            rail=IndicatorRail.WIRE,
            risk_points=29,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 109",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0010",
            name="Indicator 0010: Anomaly signature for CARD_POS",
            rail=IndicatorRail.CARD_POS,
            risk_points=30,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 110",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0011",
            name="Indicator 0011: Anomaly signature for CARD_CNP",
            rail=IndicatorRail.CARD_CNP,
            risk_points=31,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 111",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0012",
            name="Indicator 0012: Anomaly signature for UPI",
            rail=IndicatorRail.UPI,
            risk_points=32,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 112",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0013",
            name="Indicator 0013: Anomaly signature for CRYPTO",
            rail=IndicatorRail.CRYPTO,
            risk_points=33,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 113",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0014",
            name="Indicator 0014: Anomaly signature for ATM",
            rail=IndicatorRail.ATM,
            risk_points=34,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 114",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0015",
            name="Indicator 0015: Anomaly signature for INTERNAL_BOOK",
            rail=IndicatorRail.INTERNAL_BOOK,
            risk_points=35,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 115",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0016",
            name="Indicator 0016: Anomaly signature for ACH",
            rail=IndicatorRail.ACH,
            risk_points=36,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 116",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0017",
            name="Indicator 0017: Anomaly signature for WIRE",
            rail=IndicatorRail.WIRE,
            risk_points=37,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 117",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0018",
            name="Indicator 0018: Anomaly signature for CARD_POS",
            rail=IndicatorRail.CARD_POS,
            risk_points=38,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 118",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0019",
            name="Indicator 0019: Anomaly signature for CARD_CNP",
            rail=IndicatorRail.CARD_CNP,
            risk_points=39,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 119",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0020",
            name="Indicator 0020: Anomaly signature for UPI",
            rail=IndicatorRail.UPI,
            risk_points=40,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 120",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0021",
            name="Indicator 0021: Anomaly signature for CRYPTO",
            rail=IndicatorRail.CRYPTO,
            risk_points=41,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 121",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0022",
            name="Indicator 0022: Anomaly signature for ATM",
            rail=IndicatorRail.ATM,
            risk_points=42,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 122",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0023",
            name="Indicator 0023: Anomaly signature for INTERNAL_BOOK",
            rail=IndicatorRail.INTERNAL_BOOK,
            risk_points=43,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 123",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0024",
            name="Indicator 0024: Anomaly signature for ACH",
            rail=IndicatorRail.ACH,
            risk_points=44,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 124",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0025",
            name="Indicator 0025: Anomaly signature for WIRE",
            rail=IndicatorRail.WIRE,
            risk_points=45,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 125",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0026",
            name="Indicator 0026: Anomaly signature for CARD_POS",
            rail=IndicatorRail.CARD_POS,
            risk_points=46,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 126",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0027",
            name="Indicator 0027: Anomaly signature for CARD_CNP",
            rail=IndicatorRail.CARD_CNP,
            risk_points=47,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 127",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0028",
            name="Indicator 0028: Anomaly signature for UPI",
            rail=IndicatorRail.UPI,
            risk_points=48,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 128",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0029",
            name="Indicator 0029: Anomaly signature for CRYPTO",
            rail=IndicatorRail.CRYPTO,
            risk_points=49,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 129",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0030",
            name="Indicator 0030: Anomaly signature for ATM",
            rail=IndicatorRail.ATM,
            risk_points=50,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 130",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0031",
            name="Indicator 0031: Anomaly signature for INTERNAL_BOOK",
            rail=IndicatorRail.INTERNAL_BOOK,
            risk_points=51,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 131",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0032",
            name="Indicator 0032: Anomaly signature for ACH",
            rail=IndicatorRail.ACH,
            risk_points=52,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 132",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0033",
            name="Indicator 0033: Anomaly signature for WIRE",
            rail=IndicatorRail.WIRE,
            risk_points=53,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 133",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0034",
            name="Indicator 0034: Anomaly signature for CARD_POS",
            rail=IndicatorRail.CARD_POS,
            risk_points=54,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 134",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0035",
            name="Indicator 0035: Anomaly signature for CARD_CNP",
            rail=IndicatorRail.CARD_CNP,
            risk_points=55,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 135",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0036",
            name="Indicator 0036: Anomaly signature for UPI",
            rail=IndicatorRail.UPI,
            risk_points=56,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 136",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0037",
            name="Indicator 0037: Anomaly signature for CRYPTO",
            rail=IndicatorRail.CRYPTO,
            risk_points=57,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 137",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0038",
            name="Indicator 0038: Anomaly signature for ATM",
            rail=IndicatorRail.ATM,
            risk_points=58,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 138",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0039",
            name="Indicator 0039: Anomaly signature for INTERNAL_BOOK",
            rail=IndicatorRail.INTERNAL_BOOK,
            risk_points=59,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 139",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0040",
            name="Indicator 0040: Anomaly signature for ACH",
            rail=IndicatorRail.ACH,
            risk_points=60,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 140",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0041",
            name="Indicator 0041: Anomaly signature for WIRE",
            rail=IndicatorRail.WIRE,
            risk_points=61,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 141",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0042",
            name="Indicator 0042: Anomaly signature for CARD_POS",
            rail=IndicatorRail.CARD_POS,
            risk_points=62,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 142",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0043",
            name="Indicator 0043: Anomaly signature for CARD_CNP",
            rail=IndicatorRail.CARD_CNP,
            risk_points=63,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 143",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0044",
            name="Indicator 0044: Anomaly signature for UPI",
            rail=IndicatorRail.UPI,
            risk_points=64,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 144",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0045",
            name="Indicator 0045: Anomaly signature for CRYPTO",
            rail=IndicatorRail.CRYPTO,
            risk_points=65,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 145",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0046",
            name="Indicator 0046: Anomaly signature for ATM",
            rail=IndicatorRail.ATM,
            risk_points=66,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 146",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0047",
            name="Indicator 0047: Anomaly signature for INTERNAL_BOOK",
            rail=IndicatorRail.INTERNAL_BOOK,
            risk_points=67,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 147",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0048",
            name="Indicator 0048: Anomaly signature for ACH",
            rail=IndicatorRail.ACH,
            risk_points=68,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 148",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0049",
            name="Indicator 0049: Anomaly signature for WIRE",
            rail=IndicatorRail.WIRE,
            risk_points=69,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 149",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0050",
            name="Indicator 0050: Anomaly signature for CARD_POS",
            rail=IndicatorRail.CARD_POS,
            risk_points=70,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 100",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0051",
            name="Indicator 0051: Anomaly signature for CARD_CNP",
            rail=IndicatorRail.CARD_CNP,
            risk_points=71,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 101",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0052",
            name="Indicator 0052: Anomaly signature for UPI",
            rail=IndicatorRail.UPI,
            risk_points=72,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 102",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0053",
            name="Indicator 0053: Anomaly signature for CRYPTO",
            rail=IndicatorRail.CRYPTO,
            risk_points=73,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 103",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0054",
            name="Indicator 0054: Anomaly signature for ATM",
            rail=IndicatorRail.ATM,
            risk_points=74,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 104",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0055",
            name="Indicator 0055: Anomaly signature for INTERNAL_BOOK",
            rail=IndicatorRail.INTERNAL_BOOK,
            risk_points=75,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 105",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0056",
            name="Indicator 0056: Anomaly signature for ACH",
            rail=IndicatorRail.ACH,
            risk_points=76,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 106",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0057",
            name="Indicator 0057: Anomaly signature for WIRE",
            rail=IndicatorRail.WIRE,
            risk_points=77,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 107",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0058",
            name="Indicator 0058: Anomaly signature for CARD_POS",
            rail=IndicatorRail.CARD_POS,
            risk_points=78,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 108",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0059",
            name="Indicator 0059: Anomaly signature for CARD_CNP",
            rail=IndicatorRail.CARD_CNP,
            risk_points=79,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 109",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0060",
            name="Indicator 0060: Anomaly signature for UPI",
            rail=IndicatorRail.UPI,
            risk_points=80,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 110",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0061",
            name="Indicator 0061: Anomaly signature for CRYPTO",
            rail=IndicatorRail.CRYPTO,
            risk_points=81,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 111",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0062",
            name="Indicator 0062: Anomaly signature for ATM",
            rail=IndicatorRail.ATM,
            risk_points=82,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 112",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0063",
            name="Indicator 0063: Anomaly signature for INTERNAL_BOOK",
            rail=IndicatorRail.INTERNAL_BOOK,
            risk_points=83,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 113",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0064",
            name="Indicator 0064: Anomaly signature for ACH",
            rail=IndicatorRail.ACH,
            risk_points=84,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 114",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0065",
            name="Indicator 0065: Anomaly signature for WIRE",
            rail=IndicatorRail.WIRE,
            risk_points=85,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 115",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0066",
            name="Indicator 0066: Anomaly signature for CARD_POS",
            rail=IndicatorRail.CARD_POS,
            risk_points=86,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 116",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0067",
            name="Indicator 0067: Anomaly signature for CARD_CNP",
            rail=IndicatorRail.CARD_CNP,
            risk_points=87,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 117",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0068",
            name="Indicator 0068: Anomaly signature for UPI",
            rail=IndicatorRail.UPI,
            risk_points=88,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 118",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0069",
            name="Indicator 0069: Anomaly signature for CRYPTO",
            rail=IndicatorRail.CRYPTO,
            risk_points=89,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 119",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0070",
            name="Indicator 0070: Anomaly signature for ATM",
            rail=IndicatorRail.ATM,
            risk_points=90,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 120",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0071",
            name="Indicator 0071: Anomaly signature for INTERNAL_BOOK",
            rail=IndicatorRail.INTERNAL_BOOK,
            risk_points=91,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 121",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0072",
            name="Indicator 0072: Anomaly signature for ACH",
            rail=IndicatorRail.ACH,
            risk_points=92,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 122",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0073",
            name="Indicator 0073: Anomaly signature for WIRE",
            rail=IndicatorRail.WIRE,
            risk_points=93,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 123",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0074",
            name="Indicator 0074: Anomaly signature for CARD_POS",
            rail=IndicatorRail.CARD_POS,
            risk_points=94,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 124",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0075",
            name="Indicator 0075: Anomaly signature for CARD_CNP",
            rail=IndicatorRail.CARD_CNP,
            risk_points=95,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 125",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0076",
            name="Indicator 0076: Anomaly signature for UPI",
            rail=IndicatorRail.UPI,
            risk_points=96,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 126",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0077",
            name="Indicator 0077: Anomaly signature for CRYPTO",
            rail=IndicatorRail.CRYPTO,
            risk_points=97,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 127",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0078",
            name="Indicator 0078: Anomaly signature for ATM",
            rail=IndicatorRail.ATM,
            risk_points=98,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 128",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0079",
            name="Indicator 0079: Anomaly signature for INTERNAL_BOOK",
            rail=IndicatorRail.INTERNAL_BOOK,
            risk_points=99,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 129",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0080",
            name="Indicator 0080: Anomaly signature for ACH",
            rail=IndicatorRail.ACH,
            risk_points=20,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 130",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0081",
            name="Indicator 0081: Anomaly signature for WIRE",
            rail=IndicatorRail.WIRE,
            risk_points=21,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 131",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0082",
            name="Indicator 0082: Anomaly signature for CARD_POS",
            rail=IndicatorRail.CARD_POS,
            risk_points=22,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 132",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0083",
            name="Indicator 0083: Anomaly signature for CARD_CNP",
            rail=IndicatorRail.CARD_CNP,
            risk_points=23,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 133",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0084",
            name="Indicator 0084: Anomaly signature for UPI",
            rail=IndicatorRail.UPI,
            risk_points=24,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 134",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0085",
            name="Indicator 0085: Anomaly signature for CRYPTO",
            rail=IndicatorRail.CRYPTO,
            risk_points=25,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 135",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0086",
            name="Indicator 0086: Anomaly signature for ATM",
            rail=IndicatorRail.ATM,
            risk_points=26,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 136",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0087",
            name="Indicator 0087: Anomaly signature for INTERNAL_BOOK",
            rail=IndicatorRail.INTERNAL_BOOK,
            risk_points=27,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 137",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0088",
            name="Indicator 0088: Anomaly signature for ACH",
            rail=IndicatorRail.ACH,
            risk_points=28,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 138",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0089",
            name="Indicator 0089: Anomaly signature for WIRE",
            rail=IndicatorRail.WIRE,
            risk_points=29,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 139",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0090",
            name="Indicator 0090: Anomaly signature for CARD_POS",
            rail=IndicatorRail.CARD_POS,
            risk_points=30,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 140",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0091",
            name="Indicator 0091: Anomaly signature for CARD_CNP",
            rail=IndicatorRail.CARD_CNP,
            risk_points=31,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 141",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0092",
            name="Indicator 0092: Anomaly signature for UPI",
            rail=IndicatorRail.UPI,
            risk_points=32,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 142",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0093",
            name="Indicator 0093: Anomaly signature for CRYPTO",
            rail=IndicatorRail.CRYPTO,
            risk_points=33,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 143",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0094",
            name="Indicator 0094: Anomaly signature for ATM",
            rail=IndicatorRail.ATM,
            risk_points=34,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 144",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0095",
            name="Indicator 0095: Anomaly signature for INTERNAL_BOOK",
            rail=IndicatorRail.INTERNAL_BOOK,
            risk_points=35,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 145",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0096",
            name="Indicator 0096: Anomaly signature for ACH",
            rail=IndicatorRail.ACH,
            risk_points=36,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 146",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0097",
            name="Indicator 0097: Anomaly signature for WIRE",
            rail=IndicatorRail.WIRE,
            risk_points=37,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 147",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0098",
            name="Indicator 0098: Anomaly signature for CARD_POS",
            rail=IndicatorRail.CARD_POS,
            risk_points=38,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 148",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0099",
            name="Indicator 0099: Anomaly signature for CARD_CNP",
            rail=IndicatorRail.CARD_CNP,
            risk_points=39,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 149",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0100",
            name="Indicator 0100: Anomaly signature for UPI",
            rail=IndicatorRail.UPI,
            risk_points=40,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 100",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0101",
            name="Indicator 0101: Anomaly signature for CRYPTO",
            rail=IndicatorRail.CRYPTO,
            risk_points=41,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 101",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0102",
            name="Indicator 0102: Anomaly signature for ATM",
            rail=IndicatorRail.ATM,
            risk_points=42,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 102",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0103",
            name="Indicator 0103: Anomaly signature for INTERNAL_BOOK",
            rail=IndicatorRail.INTERNAL_BOOK,
            risk_points=43,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 103",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0104",
            name="Indicator 0104: Anomaly signature for ACH",
            rail=IndicatorRail.ACH,
            risk_points=44,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 104",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0105",
            name="Indicator 0105: Anomaly signature for WIRE",
            rail=IndicatorRail.WIRE,
            risk_points=45,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 105",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0106",
            name="Indicator 0106: Anomaly signature for CARD_POS",
            rail=IndicatorRail.CARD_POS,
            risk_points=46,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 106",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0107",
            name="Indicator 0107: Anomaly signature for CARD_CNP",
            rail=IndicatorRail.CARD_CNP,
            risk_points=47,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 107",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0108",
            name="Indicator 0108: Anomaly signature for UPI",
            rail=IndicatorRail.UPI,
            risk_points=48,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 108",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0109",
            name="Indicator 0109: Anomaly signature for CRYPTO",
            rail=IndicatorRail.CRYPTO,
            risk_points=49,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 109",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0110",
            name="Indicator 0110: Anomaly signature for ATM",
            rail=IndicatorRail.ATM,
            risk_points=50,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 110",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0111",
            name="Indicator 0111: Anomaly signature for INTERNAL_BOOK",
            rail=IndicatorRail.INTERNAL_BOOK,
            risk_points=51,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 111",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0112",
            name="Indicator 0112: Anomaly signature for ACH",
            rail=IndicatorRail.ACH,
            risk_points=52,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 112",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0113",
            name="Indicator 0113: Anomaly signature for WIRE",
            rail=IndicatorRail.WIRE,
            risk_points=53,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 113",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0114",
            name="Indicator 0114: Anomaly signature for CARD_POS",
            rail=IndicatorRail.CARD_POS,
            risk_points=54,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 114",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0115",
            name="Indicator 0115: Anomaly signature for CARD_CNP",
            rail=IndicatorRail.CARD_CNP,
            risk_points=55,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 115",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0116",
            name="Indicator 0116: Anomaly signature for UPI",
            rail=IndicatorRail.UPI,
            risk_points=56,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 116",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0117",
            name="Indicator 0117: Anomaly signature for CRYPTO",
            rail=IndicatorRail.CRYPTO,
            risk_points=57,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 117",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0118",
            name="Indicator 0118: Anomaly signature for ATM",
            rail=IndicatorRail.ATM,
            risk_points=58,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 118",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0119",
            name="Indicator 0119: Anomaly signature for INTERNAL_BOOK",
            rail=IndicatorRail.INTERNAL_BOOK,
            risk_points=59,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 119",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0120",
            name="Indicator 0120: Anomaly signature for ACH",
            rail=IndicatorRail.ACH,
            risk_points=60,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 120",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0121",
            name="Indicator 0121: Anomaly signature for WIRE",
            rail=IndicatorRail.WIRE,
            risk_points=61,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 121",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0122",
            name="Indicator 0122: Anomaly signature for CARD_POS",
            rail=IndicatorRail.CARD_POS,
            risk_points=62,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 122",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0123",
            name="Indicator 0123: Anomaly signature for CARD_CNP",
            rail=IndicatorRail.CARD_CNP,
            risk_points=63,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 123",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0124",
            name="Indicator 0124: Anomaly signature for UPI",
            rail=IndicatorRail.UPI,
            risk_points=64,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 124",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0125",
            name="Indicator 0125: Anomaly signature for CRYPTO",
            rail=IndicatorRail.CRYPTO,
            risk_points=65,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 125",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0126",
            name="Indicator 0126: Anomaly signature for ATM",
            rail=IndicatorRail.ATM,
            risk_points=66,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 126",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0127",
            name="Indicator 0127: Anomaly signature for INTERNAL_BOOK",
            rail=IndicatorRail.INTERNAL_BOOK,
            risk_points=67,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 127",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0128",
            name="Indicator 0128: Anomaly signature for ACH",
            rail=IndicatorRail.ACH,
            risk_points=68,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 128",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0129",
            name="Indicator 0129: Anomaly signature for WIRE",
            rail=IndicatorRail.WIRE,
            risk_points=69,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 129",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0130",
            name="Indicator 0130: Anomaly signature for CARD_POS",
            rail=IndicatorRail.CARD_POS,
            risk_points=70,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 130",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0131",
            name="Indicator 0131: Anomaly signature for CARD_CNP",
            rail=IndicatorRail.CARD_CNP,
            risk_points=71,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 131",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0132",
            name="Indicator 0132: Anomaly signature for UPI",
            rail=IndicatorRail.UPI,
            risk_points=72,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 132",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0133",
            name="Indicator 0133: Anomaly signature for CRYPTO",
            rail=IndicatorRail.CRYPTO,
            risk_points=73,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 133",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0134",
            name="Indicator 0134: Anomaly signature for ATM",
            rail=IndicatorRail.ATM,
            risk_points=74,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 134",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0135",
            name="Indicator 0135: Anomaly signature for INTERNAL_BOOK",
            rail=IndicatorRail.INTERNAL_BOOK,
            risk_points=75,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 135",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0136",
            name="Indicator 0136: Anomaly signature for ACH",
            rail=IndicatorRail.ACH,
            risk_points=76,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 136",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0137",
            name="Indicator 0137: Anomaly signature for WIRE",
            rail=IndicatorRail.WIRE,
            risk_points=77,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 137",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0138",
            name="Indicator 0138: Anomaly signature for CARD_POS",
            rail=IndicatorRail.CARD_POS,
            risk_points=78,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 138",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0139",
            name="Indicator 0139: Anomaly signature for CARD_CNP",
            rail=IndicatorRail.CARD_CNP,
            risk_points=79,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 139",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0140",
            name="Indicator 0140: Anomaly signature for UPI",
            rail=IndicatorRail.UPI,
            risk_points=80,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 140",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0141",
            name="Indicator 0141: Anomaly signature for CRYPTO",
            rail=IndicatorRail.CRYPTO,
            risk_points=81,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 141",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0142",
            name="Indicator 0142: Anomaly signature for ATM",
            rail=IndicatorRail.ATM,
            risk_points=82,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 142",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0143",
            name="Indicator 0143: Anomaly signature for INTERNAL_BOOK",
            rail=IndicatorRail.INTERNAL_BOOK,
            risk_points=83,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 143",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0144",
            name="Indicator 0144: Anomaly signature for ACH",
            rail=IndicatorRail.ACH,
            risk_points=84,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 144",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0145",
            name="Indicator 0145: Anomaly signature for WIRE",
            rail=IndicatorRail.WIRE,
            risk_points=85,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 145",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0146",
            name="Indicator 0146: Anomaly signature for CARD_POS",
            rail=IndicatorRail.CARD_POS,
            risk_points=86,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 146",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0147",
            name="Indicator 0147: Anomaly signature for CARD_CNP",
            rail=IndicatorRail.CARD_CNP,
            risk_points=87,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 147",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0148",
            name="Indicator 0148: Anomaly signature for UPI",
            rail=IndicatorRail.UPI,
            risk_points=88,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 148",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0149",
            name="Indicator 0149: Anomaly signature for CRYPTO",
            rail=IndicatorRail.CRYPTO,
            risk_points=89,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 149",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0150",
            name="Indicator 0150: Anomaly signature for ATM",
            rail=IndicatorRail.ATM,
            risk_points=90,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 100",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0151",
            name="Indicator 0151: Anomaly signature for INTERNAL_BOOK",
            rail=IndicatorRail.INTERNAL_BOOK,
            risk_points=91,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 101",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0152",
            name="Indicator 0152: Anomaly signature for ACH",
            rail=IndicatorRail.ACH,
            risk_points=92,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 102",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0153",
            name="Indicator 0153: Anomaly signature for WIRE",
            rail=IndicatorRail.WIRE,
            risk_points=93,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 103",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0154",
            name="Indicator 0154: Anomaly signature for CARD_POS",
            rail=IndicatorRail.CARD_POS,
            risk_points=94,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 104",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0155",
            name="Indicator 0155: Anomaly signature for CARD_CNP",
            rail=IndicatorRail.CARD_CNP,
            risk_points=95,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 105",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0156",
            name="Indicator 0156: Anomaly signature for UPI",
            rail=IndicatorRail.UPI,
            risk_points=96,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 106",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0157",
            name="Indicator 0157: Anomaly signature for CRYPTO",
            rail=IndicatorRail.CRYPTO,
            risk_points=97,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 107",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0158",
            name="Indicator 0158: Anomaly signature for ATM",
            rail=IndicatorRail.ATM,
            risk_points=98,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 108",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0159",
            name="Indicator 0159: Anomaly signature for INTERNAL_BOOK",
            rail=IndicatorRail.INTERNAL_BOOK,
            risk_points=99,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 109",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0160",
            name="Indicator 0160: Anomaly signature for ACH",
            rail=IndicatorRail.ACH,
            risk_points=20,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 110",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0161",
            name="Indicator 0161: Anomaly signature for WIRE",
            rail=IndicatorRail.WIRE,
            risk_points=21,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 111",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0162",
            name="Indicator 0162: Anomaly signature for CARD_POS",
            rail=IndicatorRail.CARD_POS,
            risk_points=22,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 112",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0163",
            name="Indicator 0163: Anomaly signature for CARD_CNP",
            rail=IndicatorRail.CARD_CNP,
            risk_points=23,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 113",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0164",
            name="Indicator 0164: Anomaly signature for UPI",
            rail=IndicatorRail.UPI,
            risk_points=24,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 114",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0165",
            name="Indicator 0165: Anomaly signature for CRYPTO",
            rail=IndicatorRail.CRYPTO,
            risk_points=25,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 115",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0166",
            name="Indicator 0166: Anomaly signature for ATM",
            rail=IndicatorRail.ATM,
            risk_points=26,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 116",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0167",
            name="Indicator 0167: Anomaly signature for INTERNAL_BOOK",
            rail=IndicatorRail.INTERNAL_BOOK,
            risk_points=27,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 117",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0168",
            name="Indicator 0168: Anomaly signature for ACH",
            rail=IndicatorRail.ACH,
            risk_points=28,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 118",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0169",
            name="Indicator 0169: Anomaly signature for WIRE",
            rail=IndicatorRail.WIRE,
            risk_points=29,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 119",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0170",
            name="Indicator 0170: Anomaly signature for CARD_POS",
            rail=IndicatorRail.CARD_POS,
            risk_points=30,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 120",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0171",
            name="Indicator 0171: Anomaly signature for CARD_CNP",
            rail=IndicatorRail.CARD_CNP,
            risk_points=31,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 121",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0172",
            name="Indicator 0172: Anomaly signature for UPI",
            rail=IndicatorRail.UPI,
            risk_points=32,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 122",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0173",
            name="Indicator 0173: Anomaly signature for CRYPTO",
            rail=IndicatorRail.CRYPTO,
            risk_points=33,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 123",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0174",
            name="Indicator 0174: Anomaly signature for ATM",
            rail=IndicatorRail.ATM,
            risk_points=34,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 124",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0175",
            name="Indicator 0175: Anomaly signature for INTERNAL_BOOK",
            rail=IndicatorRail.INTERNAL_BOOK,
            risk_points=35,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 125",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0176",
            name="Indicator 0176: Anomaly signature for ACH",
            rail=IndicatorRail.ACH,
            risk_points=36,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 126",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0177",
            name="Indicator 0177: Anomaly signature for WIRE",
            rail=IndicatorRail.WIRE,
            risk_points=37,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 127",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0178",
            name="Indicator 0178: Anomaly signature for CARD_POS",
            rail=IndicatorRail.CARD_POS,
            risk_points=38,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 128",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0179",
            name="Indicator 0179: Anomaly signature for CARD_CNP",
            rail=IndicatorRail.CARD_CNP,
            risk_points=39,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 129",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0180",
            name="Indicator 0180: Anomaly signature for UPI",
            rail=IndicatorRail.UPI,
            risk_points=40,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 130",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0181",
            name="Indicator 0181: Anomaly signature for CRYPTO",
            rail=IndicatorRail.CRYPTO,
            risk_points=41,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 131",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0182",
            name="Indicator 0182: Anomaly signature for ATM",
            rail=IndicatorRail.ATM,
            risk_points=42,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 132",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0183",
            name="Indicator 0183: Anomaly signature for INTERNAL_BOOK",
            rail=IndicatorRail.INTERNAL_BOOK,
            risk_points=43,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 133",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0184",
            name="Indicator 0184: Anomaly signature for ACH",
            rail=IndicatorRail.ACH,
            risk_points=44,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 134",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0185",
            name="Indicator 0185: Anomaly signature for WIRE",
            rail=IndicatorRail.WIRE,
            risk_points=45,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 135",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0186",
            name="Indicator 0186: Anomaly signature for CARD_POS",
            rail=IndicatorRail.CARD_POS,
            risk_points=46,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 136",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0187",
            name="Indicator 0187: Anomaly signature for CARD_CNP",
            rail=IndicatorRail.CARD_CNP,
            risk_points=47,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 137",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0188",
            name="Indicator 0188: Anomaly signature for UPI",
            rail=IndicatorRail.UPI,
            risk_points=48,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 138",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0189",
            name="Indicator 0189: Anomaly signature for CRYPTO",
            rail=IndicatorRail.CRYPTO,
            risk_points=49,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 139",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0190",
            name="Indicator 0190: Anomaly signature for ATM",
            rail=IndicatorRail.ATM,
            risk_points=50,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 140",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0191",
            name="Indicator 0191: Anomaly signature for INTERNAL_BOOK",
            rail=IndicatorRail.INTERNAL_BOOK,
            risk_points=51,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 141",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0192",
            name="Indicator 0192: Anomaly signature for ACH",
            rail=IndicatorRail.ACH,
            risk_points=52,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 142",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0193",
            name="Indicator 0193: Anomaly signature for WIRE",
            rail=IndicatorRail.WIRE,
            risk_points=53,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 143",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0194",
            name="Indicator 0194: Anomaly signature for CARD_POS",
            rail=IndicatorRail.CARD_POS,
            risk_points=54,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 144",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0195",
            name="Indicator 0195: Anomaly signature for CARD_CNP",
            rail=IndicatorRail.CARD_CNP,
            risk_points=55,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 145",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0196",
            name="Indicator 0196: Anomaly signature for UPI",
            rail=IndicatorRail.UPI,
            risk_points=56,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 146",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0197",
            name="Indicator 0197: Anomaly signature for CRYPTO",
            rail=IndicatorRail.CRYPTO,
            risk_points=57,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 147",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0198",
            name="Indicator 0198: Anomaly signature for ATM",
            rail=IndicatorRail.ATM,
            risk_points=58,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 148",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0199",
            name="Indicator 0199: Anomaly signature for INTERNAL_BOOK",
            rail=IndicatorRail.INTERNAL_BOOK,
            risk_points=59,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 149",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0200",
            name="Indicator 0200: Anomaly signature for ACH",
            rail=IndicatorRail.ACH,
            risk_points=60,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 100",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0201",
            name="Indicator 0201: Anomaly signature for WIRE",
            rail=IndicatorRail.WIRE,
            risk_points=61,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 101",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0202",
            name="Indicator 0202: Anomaly signature for CARD_POS",
            rail=IndicatorRail.CARD_POS,
            risk_points=62,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 102",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0203",
            name="Indicator 0203: Anomaly signature for CARD_CNP",
            rail=IndicatorRail.CARD_CNP,
            risk_points=63,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 103",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0204",
            name="Indicator 0204: Anomaly signature for UPI",
            rail=IndicatorRail.UPI,
            risk_points=64,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 104",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0205",
            name="Indicator 0205: Anomaly signature for CRYPTO",
            rail=IndicatorRail.CRYPTO,
            risk_points=65,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 105",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0206",
            name="Indicator 0206: Anomaly signature for ATM",
            rail=IndicatorRail.ATM,
            risk_points=66,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 106",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0207",
            name="Indicator 0207: Anomaly signature for INTERNAL_BOOK",
            rail=IndicatorRail.INTERNAL_BOOK,
            risk_points=67,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 107",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0208",
            name="Indicator 0208: Anomaly signature for ACH",
            rail=IndicatorRail.ACH,
            risk_points=68,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 108",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0209",
            name="Indicator 0209: Anomaly signature for WIRE",
            rail=IndicatorRail.WIRE,
            risk_points=69,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 109",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0210",
            name="Indicator 0210: Anomaly signature for CARD_POS",
            rail=IndicatorRail.CARD_POS,
            risk_points=70,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 110",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0211",
            name="Indicator 0211: Anomaly signature for CARD_CNP",
            rail=IndicatorRail.CARD_CNP,
            risk_points=71,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 111",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0212",
            name="Indicator 0212: Anomaly signature for UPI",
            rail=IndicatorRail.UPI,
            risk_points=72,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 112",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0213",
            name="Indicator 0213: Anomaly signature for CRYPTO",
            rail=IndicatorRail.CRYPTO,
            risk_points=73,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 113",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0214",
            name="Indicator 0214: Anomaly signature for ATM",
            rail=IndicatorRail.ATM,
            risk_points=74,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 114",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0215",
            name="Indicator 0215: Anomaly signature for INTERNAL_BOOK",
            rail=IndicatorRail.INTERNAL_BOOK,
            risk_points=75,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 115",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0216",
            name="Indicator 0216: Anomaly signature for ACH",
            rail=IndicatorRail.ACH,
            risk_points=76,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 116",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0217",
            name="Indicator 0217: Anomaly signature for WIRE",
            rail=IndicatorRail.WIRE,
            risk_points=77,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 117",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0218",
            name="Indicator 0218: Anomaly signature for CARD_POS",
            rail=IndicatorRail.CARD_POS,
            risk_points=78,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 118",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0219",
            name="Indicator 0219: Anomaly signature for CARD_CNP",
            rail=IndicatorRail.CARD_CNP,
            risk_points=79,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 119",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0220",
            name="Indicator 0220: Anomaly signature for UPI",
            rail=IndicatorRail.UPI,
            risk_points=80,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 120",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0221",
            name="Indicator 0221: Anomaly signature for CRYPTO",
            rail=IndicatorRail.CRYPTO,
            risk_points=81,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 121",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0222",
            name="Indicator 0222: Anomaly signature for ATM",
            rail=IndicatorRail.ATM,
            risk_points=82,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 122",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0223",
            name="Indicator 0223: Anomaly signature for INTERNAL_BOOK",
            rail=IndicatorRail.INTERNAL_BOOK,
            risk_points=83,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 123",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0224",
            name="Indicator 0224: Anomaly signature for ACH",
            rail=IndicatorRail.ACH,
            risk_points=84,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 124",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0225",
            name="Indicator 0225: Anomaly signature for WIRE",
            rail=IndicatorRail.WIRE,
            risk_points=85,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 125",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0226",
            name="Indicator 0226: Anomaly signature for CARD_POS",
            rail=IndicatorRail.CARD_POS,
            risk_points=86,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 126",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0227",
            name="Indicator 0227: Anomaly signature for CARD_CNP",
            rail=IndicatorRail.CARD_CNP,
            risk_points=87,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 127",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0228",
            name="Indicator 0228: Anomaly signature for UPI",
            rail=IndicatorRail.UPI,
            risk_points=88,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 128",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0229",
            name="Indicator 0229: Anomaly signature for CRYPTO",
            rail=IndicatorRail.CRYPTO,
            risk_points=89,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 129",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0230",
            name="Indicator 0230: Anomaly signature for ATM",
            rail=IndicatorRail.ATM,
            risk_points=90,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 130",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0231",
            name="Indicator 0231: Anomaly signature for INTERNAL_BOOK",
            rail=IndicatorRail.INTERNAL_BOOK,
            risk_points=91,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 131",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0232",
            name="Indicator 0232: Anomaly signature for ACH",
            rail=IndicatorRail.ACH,
            risk_points=92,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 132",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0233",
            name="Indicator 0233: Anomaly signature for WIRE",
            rail=IndicatorRail.WIRE,
            risk_points=93,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 133",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0234",
            name="Indicator 0234: Anomaly signature for CARD_POS",
            rail=IndicatorRail.CARD_POS,
            risk_points=94,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 134",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0235",
            name="Indicator 0235: Anomaly signature for CARD_CNP",
            rail=IndicatorRail.CARD_CNP,
            risk_points=95,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 135",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0236",
            name="Indicator 0236: Anomaly signature for UPI",
            rail=IndicatorRail.UPI,
            risk_points=96,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 136",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0237",
            name="Indicator 0237: Anomaly signature for CRYPTO",
            rail=IndicatorRail.CRYPTO,
            risk_points=97,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 137",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0238",
            name="Indicator 0238: Anomaly signature for ATM",
            rail=IndicatorRail.ATM,
            risk_points=98,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 138",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0239",
            name="Indicator 0239: Anomaly signature for INTERNAL_BOOK",
            rail=IndicatorRail.INTERNAL_BOOK,
            risk_points=99,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 139",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0240",
            name="Indicator 0240: Anomaly signature for ACH",
            rail=IndicatorRail.ACH,
            risk_points=20,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 140",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0241",
            name="Indicator 0241: Anomaly signature for WIRE",
            rail=IndicatorRail.WIRE,
            risk_points=21,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 141",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0242",
            name="Indicator 0242: Anomaly signature for CARD_POS",
            rail=IndicatorRail.CARD_POS,
            risk_points=22,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 142",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0243",
            name="Indicator 0243: Anomaly signature for CARD_CNP",
            rail=IndicatorRail.CARD_CNP,
            risk_points=23,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 143",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0244",
            name="Indicator 0244: Anomaly signature for UPI",
            rail=IndicatorRail.UPI,
            risk_points=24,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 144",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0245",
            name="Indicator 0245: Anomaly signature for CRYPTO",
            rail=IndicatorRail.CRYPTO,
            risk_points=25,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 145",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0246",
            name="Indicator 0246: Anomaly signature for ATM",
            rail=IndicatorRail.ATM,
            risk_points=26,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 146",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0247",
            name="Indicator 0247: Anomaly signature for INTERNAL_BOOK",
            rail=IndicatorRail.INTERNAL_BOOK,
            risk_points=27,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 147",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0248",
            name="Indicator 0248: Anomaly signature for ACH",
            rail=IndicatorRail.ACH,
            risk_points=28,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 148",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0249",
            name="Indicator 0249: Anomaly signature for WIRE",
            rail=IndicatorRail.WIRE,
            risk_points=29,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 149",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0250",
            name="Indicator 0250: Anomaly signature for CARD_POS",
            rail=IndicatorRail.CARD_POS,
            risk_points=30,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 100",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0251",
            name="Indicator 0251: Anomaly signature for CARD_CNP",
            rail=IndicatorRail.CARD_CNP,
            risk_points=31,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 101",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0252",
            name="Indicator 0252: Anomaly signature for UPI",
            rail=IndicatorRail.UPI,
            risk_points=32,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 102",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0253",
            name="Indicator 0253: Anomaly signature for CRYPTO",
            rail=IndicatorRail.CRYPTO,
            risk_points=33,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 103",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0254",
            name="Indicator 0254: Anomaly signature for ATM",
            rail=IndicatorRail.ATM,
            risk_points=34,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 104",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0255",
            name="Indicator 0255: Anomaly signature for INTERNAL_BOOK",
            rail=IndicatorRail.INTERNAL_BOOK,
            risk_points=35,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 105",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0256",
            name="Indicator 0256: Anomaly signature for ACH",
            rail=IndicatorRail.ACH,
            risk_points=36,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 106",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0257",
            name="Indicator 0257: Anomaly signature for WIRE",
            rail=IndicatorRail.WIRE,
            risk_points=37,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 107",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0258",
            name="Indicator 0258: Anomaly signature for CARD_POS",
            rail=IndicatorRail.CARD_POS,
            risk_points=38,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 108",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0259",
            name="Indicator 0259: Anomaly signature for CARD_CNP",
            rail=IndicatorRail.CARD_CNP,
            risk_points=39,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 109",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0260",
            name="Indicator 0260: Anomaly signature for UPI",
            rail=IndicatorRail.UPI,
            risk_points=40,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 110",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0261",
            name="Indicator 0261: Anomaly signature for CRYPTO",
            rail=IndicatorRail.CRYPTO,
            risk_points=41,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 111",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0262",
            name="Indicator 0262: Anomaly signature for ATM",
            rail=IndicatorRail.ATM,
            risk_points=42,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 112",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0263",
            name="Indicator 0263: Anomaly signature for INTERNAL_BOOK",
            rail=IndicatorRail.INTERNAL_BOOK,
            risk_points=43,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 113",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0264",
            name="Indicator 0264: Anomaly signature for ACH",
            rail=IndicatorRail.ACH,
            risk_points=44,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 114",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0265",
            name="Indicator 0265: Anomaly signature for WIRE",
            rail=IndicatorRail.WIRE,
            risk_points=45,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 115",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0266",
            name="Indicator 0266: Anomaly signature for CARD_POS",
            rail=IndicatorRail.CARD_POS,
            risk_points=46,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 116",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0267",
            name="Indicator 0267: Anomaly signature for CARD_CNP",
            rail=IndicatorRail.CARD_CNP,
            risk_points=47,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 117",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0268",
            name="Indicator 0268: Anomaly signature for UPI",
            rail=IndicatorRail.UPI,
            risk_points=48,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 118",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0269",
            name="Indicator 0269: Anomaly signature for CRYPTO",
            rail=IndicatorRail.CRYPTO,
            risk_points=49,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 119",
            mitigation_action="LOG_AUDIT"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0270",
            name="Indicator 0270: Anomaly signature for ATM",
            rail=IndicatorRail.ATM,
            risk_points=50,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 120",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0271",
            name="Indicator 0271: Anomaly signature for INTERNAL_BOOK",
            rail=IndicatorRail.INTERNAL_BOOK,
            risk_points=51,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 121",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0272",
            name="Indicator 0272: Anomaly signature for ACH",
            rail=IndicatorRail.ACH,
            risk_points=52,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 122",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0273",
            name="Indicator 0273: Anomaly signature for WIRE",
            rail=IndicatorRail.WIRE,
            risk_points=53,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 123",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0274",
            name="Indicator 0274: Anomaly signature for CARD_POS",
            rail=IndicatorRail.CARD_POS,
            risk_points=54,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 124",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0275",
            name="Indicator 0275: Anomaly signature for CARD_CNP",
            rail=IndicatorRail.CARD_CNP,
            risk_points=55,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 125",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0276",
            name="Indicator 0276: Anomaly signature for UPI",
            rail=IndicatorRail.UPI,
            risk_points=56,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 126",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0277",
            name="Indicator 0277: Anomaly signature for CRYPTO",
            rail=IndicatorRail.CRYPTO,
            risk_points=57,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 127",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0278",
            name="Indicator 0278: Anomaly signature for ATM",
            rail=IndicatorRail.ATM,
            risk_points=58,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 128",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0279",
            name="Indicator 0279: Anomaly signature for INTERNAL_BOOK",
            rail=IndicatorRail.INTERNAL_BOOK,
            risk_points=59,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 129",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0280",
            name="Indicator 0280: Anomaly signature for ACH",
            rail=IndicatorRail.ACH,
            risk_points=60,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 130",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0281",
            name="Indicator 0281: Anomaly signature for WIRE",
            rail=IndicatorRail.WIRE,
            risk_points=61,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 131",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0282",
            name="Indicator 0282: Anomaly signature for CARD_POS",
            rail=IndicatorRail.CARD_POS,
            risk_points=62,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 132",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0283",
            name="Indicator 0283: Anomaly signature for CARD_CNP",
            rail=IndicatorRail.CARD_CNP,
            risk_points=63,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 133",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0284",
            name="Indicator 0284: Anomaly signature for UPI",
            rail=IndicatorRail.UPI,
            risk_points=64,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 134",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0285",
            name="Indicator 0285: Anomaly signature for CRYPTO",
            rail=IndicatorRail.CRYPTO,
            risk_points=65,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 135",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0286",
            name="Indicator 0286: Anomaly signature for ATM",
            rail=IndicatorRail.ATM,
            risk_points=66,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 136",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0287",
            name="Indicator 0287: Anomaly signature for INTERNAL_BOOK",
            rail=IndicatorRail.INTERNAL_BOOK,
            risk_points=67,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 137",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0288",
            name="Indicator 0288: Anomaly signature for ACH",
            rail=IndicatorRail.ACH,
            risk_points=68,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 138",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0289",
            name="Indicator 0289: Anomaly signature for WIRE",
            rail=IndicatorRail.WIRE,
            risk_points=69,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 139",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0290",
            name="Indicator 0290: Anomaly signature for CARD_POS",
            rail=IndicatorRail.CARD_POS,
            risk_points=70,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 140",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0291",
            name="Indicator 0291: Anomaly signature for CARD_CNP",
            rail=IndicatorRail.CARD_CNP,
            risk_points=71,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 141",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0292",
            name="Indicator 0292: Anomaly signature for UPI",
            rail=IndicatorRail.UPI,
            risk_points=72,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 142",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0293",
            name="Indicator 0293: Anomaly signature for CRYPTO",
            rail=IndicatorRail.CRYPTO,
            risk_points=73,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 143",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0294",
            name="Indicator 0294: Anomaly signature for ATM",
            rail=IndicatorRail.ATM,
            risk_points=74,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 144",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0295",
            name="Indicator 0295: Anomaly signature for INTERNAL_BOOK",
            rail=IndicatorRail.INTERNAL_BOOK,
            risk_points=75,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 145",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0296",
            name="Indicator 0296: Anomaly signature for ACH",
            rail=IndicatorRail.ACH,
            risk_points=76,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 146",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0297",
            name="Indicator 0297: Anomaly signature for WIRE",
            rail=IndicatorRail.WIRE,
            risk_points=77,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 147",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0298",
            name="Indicator 0298: Anomaly signature for CARD_POS",
            rail=IndicatorRail.CARD_POS,
            risk_points=78,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 148",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0299",
            name="Indicator 0299: Anomaly signature for CARD_CNP",
            rail=IndicatorRail.CARD_CNP,
            risk_points=79,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 149",
            mitigation_action="STEP_UP_AUTH"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0300",
            name="Indicator 0300: Anomaly signature for UPI",
            rail=IndicatorRail.UPI,
            risk_points=80,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 100",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0301",
            name="Indicator 0301: Anomaly signature for CRYPTO",
            rail=IndicatorRail.CRYPTO,
            risk_points=81,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 101",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0302",
            name="Indicator 0302: Anomaly signature for ATM",
            rail=IndicatorRail.ATM,
            risk_points=82,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 102",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0303",
            name="Indicator 0303: Anomaly signature for INTERNAL_BOOK",
            rail=IndicatorRail.INTERNAL_BOOK,
            risk_points=83,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 103",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0304",
            name="Indicator 0304: Anomaly signature for ACH",
            rail=IndicatorRail.ACH,
            risk_points=84,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 104",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0305",
            name="Indicator 0305: Anomaly signature for WIRE",
            rail=IndicatorRail.WIRE,
            risk_points=85,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 105",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0306",
            name="Indicator 0306: Anomaly signature for CARD_POS",
            rail=IndicatorRail.CARD_POS,
            risk_points=86,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 106",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0307",
            name="Indicator 0307: Anomaly signature for CARD_CNP",
            rail=IndicatorRail.CARD_CNP,
            risk_points=87,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 107",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0308",
            name="Indicator 0308: Anomaly signature for UPI",
            rail=IndicatorRail.UPI,
            risk_points=88,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 108",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0309",
            name="Indicator 0309: Anomaly signature for CRYPTO",
            rail=IndicatorRail.CRYPTO,
            risk_points=89,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 109",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0310",
            name="Indicator 0310: Anomaly signature for ATM",
            rail=IndicatorRail.ATM,
            risk_points=90,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 110",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0311",
            name="Indicator 0311: Anomaly signature for INTERNAL_BOOK",
            rail=IndicatorRail.INTERNAL_BOOK,
            risk_points=91,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 111",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0312",
            name="Indicator 0312: Anomaly signature for ACH",
            rail=IndicatorRail.ACH,
            risk_points=92,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 112",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0313",
            name="Indicator 0313: Anomaly signature for WIRE",
            rail=IndicatorRail.WIRE,
            risk_points=93,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 113",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0314",
            name="Indicator 0314: Anomaly signature for CARD_POS",
            rail=IndicatorRail.CARD_POS,
            risk_points=94,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 114",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0315",
            name="Indicator 0315: Anomaly signature for CARD_CNP",
            rail=IndicatorRail.CARD_CNP,
            risk_points=95,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 115",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0316",
            name="Indicator 0316: Anomaly signature for UPI",
            rail=IndicatorRail.UPI,
            risk_points=96,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 116",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0317",
            name="Indicator 0317: Anomaly signature for CRYPTO",
            rail=IndicatorRail.CRYPTO,
            risk_points=97,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 117",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0318",
            name="Indicator 0318: Anomaly signature for ATM",
            rail=IndicatorRail.ATM,
            risk_points=98,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 118",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0319",
            name="Indicator 0319: Anomaly signature for INTERNAL_BOOK",
            rail=IndicatorRail.INTERNAL_BOOK,
            risk_points=99,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 119",
            mitigation_action="HOLD_AND_ESCALATE"
        ))
        self.register(FraudIndicator(
            indicator_id="IND_0320",
            name="Indicator 0320: Anomaly signature for ACH",
            rail=IndicatorRail.ACH,
            risk_points=20,
            detection_method="Rule & ML Ensemble Scan",
            regulatory_reference="FATF Rec. 16 / FinCEN SAR Code 120",
            mitigation_action="LOG_AUDIT"
        ))

    def evaluate_transaction_indicators(self, tx: Dict[str, Any]) -> List[FraudIndicator]:
        triggered = []
        amt = float(tx.get("amount", 0.0))
        for ind in self.indicators.values():
            if amt > 50000.0 and ind.risk_points >= 75:
                triggered.append(ind)
        return triggered

indicator_catalog = MasterIndicatorCatalog()

class IndicatorAggregatorPartition_1:
    """Aggregator partition 1 managing real-time rail indicators."""
    def __init__(self):
        self.partition_id = 1
        self.registered_rail = "WIRE"
    def score_rail_subset(self, indicators: List[FraudIndicator]) -> float:
        return sum(ind.risk_points for ind in indicators if ind.rail.value == self.registered_rail)

class IndicatorAggregatorPartition_2:
    """Aggregator partition 2 managing real-time rail indicators."""
    def __init__(self):
        self.partition_id = 2
        self.registered_rail = "CARD_POS"
    def score_rail_subset(self, indicators: List[FraudIndicator]) -> float:
        return sum(ind.risk_points for ind in indicators if ind.rail.value == self.registered_rail)

class IndicatorAggregatorPartition_3:
    """Aggregator partition 3 managing real-time rail indicators."""
    def __init__(self):
        self.partition_id = 3
        self.registered_rail = "CARD_CNP"
    def score_rail_subset(self, indicators: List[FraudIndicator]) -> float:
        return sum(ind.risk_points for ind in indicators if ind.rail.value == self.registered_rail)

class IndicatorAggregatorPartition_4:
    """Aggregator partition 4 managing real-time rail indicators."""
    def __init__(self):
        self.partition_id = 4
        self.registered_rail = "UPI"
    def score_rail_subset(self, indicators: List[FraudIndicator]) -> float:
        return sum(ind.risk_points for ind in indicators if ind.rail.value == self.registered_rail)

class IndicatorAggregatorPartition_5:
    """Aggregator partition 5 managing real-time rail indicators."""
    def __init__(self):
        self.partition_id = 5
        self.registered_rail = "CRYPTO"
    def score_rail_subset(self, indicators: List[FraudIndicator]) -> float:
        return sum(ind.risk_points for ind in indicators if ind.rail.value == self.registered_rail)

class IndicatorAggregatorPartition_6:
    """Aggregator partition 6 managing real-time rail indicators."""
    def __init__(self):
        self.partition_id = 6
        self.registered_rail = "ATM"
    def score_rail_subset(self, indicators: List[FraudIndicator]) -> float:
        return sum(ind.risk_points for ind in indicators if ind.rail.value == self.registered_rail)

class IndicatorAggregatorPartition_7:
    """Aggregator partition 7 managing real-time rail indicators."""
    def __init__(self):
        self.partition_id = 7
        self.registered_rail = "INTERNAL_BOOK"
    def score_rail_subset(self, indicators: List[FraudIndicator]) -> float:
        return sum(ind.risk_points for ind in indicators if ind.rail.value == self.registered_rail)

class IndicatorAggregatorPartition_8:
    """Aggregator partition 8 managing real-time rail indicators."""
    def __init__(self):
        self.partition_id = 8
        self.registered_rail = "ACH"
    def score_rail_subset(self, indicators: List[FraudIndicator]) -> float:
        return sum(ind.risk_points for ind in indicators if ind.rail.value == self.registered_rail)

class IndicatorAggregatorPartition_9:
    """Aggregator partition 9 managing real-time rail indicators."""
    def __init__(self):
        self.partition_id = 9
        self.registered_rail = "WIRE"
    def score_rail_subset(self, indicators: List[FraudIndicator]) -> float:
        return sum(ind.risk_points for ind in indicators if ind.rail.value == self.registered_rail)

class IndicatorAggregatorPartition_10:
    """Aggregator partition 10 managing real-time rail indicators."""
    def __init__(self):
        self.partition_id = 10
        self.registered_rail = "CARD_POS"
    def score_rail_subset(self, indicators: List[FraudIndicator]) -> float:
        return sum(ind.risk_points for ind in indicators if ind.rail.value == self.registered_rail)

class IndicatorAggregatorPartition_11:
    """Aggregator partition 11 managing real-time rail indicators."""
    def __init__(self):
        self.partition_id = 11
        self.registered_rail = "CARD_CNP"
    def score_rail_subset(self, indicators: List[FraudIndicator]) -> float:
        return sum(ind.risk_points for ind in indicators if ind.rail.value == self.registered_rail)

class IndicatorAggregatorPartition_12:
    """Aggregator partition 12 managing real-time rail indicators."""
    def __init__(self):
        self.partition_id = 12
        self.registered_rail = "UPI"
    def score_rail_subset(self, indicators: List[FraudIndicator]) -> float:
        return sum(ind.risk_points for ind in indicators if ind.rail.value == self.registered_rail)

class IndicatorAggregatorPartition_13:
    """Aggregator partition 13 managing real-time rail indicators."""
    def __init__(self):
        self.partition_id = 13
        self.registered_rail = "CRYPTO"
    def score_rail_subset(self, indicators: List[FraudIndicator]) -> float:
        return sum(ind.risk_points for ind in indicators if ind.rail.value == self.registered_rail)

class IndicatorAggregatorPartition_14:
    """Aggregator partition 14 managing real-time rail indicators."""
    def __init__(self):
        self.partition_id = 14
        self.registered_rail = "ATM"
    def score_rail_subset(self, indicators: List[FraudIndicator]) -> float:
        return sum(ind.risk_points for ind in indicators if ind.rail.value == self.registered_rail)

class IndicatorAggregatorPartition_15:
    """Aggregator partition 15 managing real-time rail indicators."""
    def __init__(self):
        self.partition_id = 15
        self.registered_rail = "INTERNAL_BOOK"
    def score_rail_subset(self, indicators: List[FraudIndicator]) -> float:
        return sum(ind.risk_points for ind in indicators if ind.rail.value == self.registered_rail)

class IndicatorAggregatorPartition_16:
    """Aggregator partition 16 managing real-time rail indicators."""
    def __init__(self):
        self.partition_id = 16
        self.registered_rail = "ACH"
    def score_rail_subset(self, indicators: List[FraudIndicator]) -> float:
        return sum(ind.risk_points for ind in indicators if ind.rail.value == self.registered_rail)

class IndicatorAggregatorPartition_17:
    """Aggregator partition 17 managing real-time rail indicators."""
    def __init__(self):
        self.partition_id = 17
        self.registered_rail = "WIRE"
    def score_rail_subset(self, indicators: List[FraudIndicator]) -> float:
        return sum(ind.risk_points for ind in indicators if ind.rail.value == self.registered_rail)

class IndicatorAggregatorPartition_18:
    """Aggregator partition 18 managing real-time rail indicators."""
    def __init__(self):
        self.partition_id = 18
        self.registered_rail = "CARD_POS"
    def score_rail_subset(self, indicators: List[FraudIndicator]) -> float:
        return sum(ind.risk_points for ind in indicators if ind.rail.value == self.registered_rail)

class IndicatorAggregatorPartition_19:
    """Aggregator partition 19 managing real-time rail indicators."""
    def __init__(self):
        self.partition_id = 19
        self.registered_rail = "CARD_CNP"
    def score_rail_subset(self, indicators: List[FraudIndicator]) -> float:
        return sum(ind.risk_points for ind in indicators if ind.rail.value == self.registered_rail)

class IndicatorAggregatorPartition_20:
    """Aggregator partition 20 managing real-time rail indicators."""
    def __init__(self):
        self.partition_id = 20
        self.registered_rail = "UPI"
    def score_rail_subset(self, indicators: List[FraudIndicator]) -> float:
        return sum(ind.risk_points for ind in indicators if ind.rail.value == self.registered_rail)

class IndicatorAggregatorPartition_21:
    """Aggregator partition 21 managing real-time rail indicators."""
    def __init__(self):
        self.partition_id = 21
        self.registered_rail = "CRYPTO"
    def score_rail_subset(self, indicators: List[FraudIndicator]) -> float:
        return sum(ind.risk_points for ind in indicators if ind.rail.value == self.registered_rail)

class IndicatorAggregatorPartition_22:
    """Aggregator partition 22 managing real-time rail indicators."""
    def __init__(self):
        self.partition_id = 22
        self.registered_rail = "ATM"
    def score_rail_subset(self, indicators: List[FraudIndicator]) -> float:
        return sum(ind.risk_points for ind in indicators if ind.rail.value == self.registered_rail)

class IndicatorAggregatorPartition_23:
    """Aggregator partition 23 managing real-time rail indicators."""
    def __init__(self):
        self.partition_id = 23
        self.registered_rail = "INTERNAL_BOOK"
    def score_rail_subset(self, indicators: List[FraudIndicator]) -> float:
        return sum(ind.risk_points for ind in indicators if ind.rail.value == self.registered_rail)

class IndicatorAggregatorPartition_24:
    """Aggregator partition 24 managing real-time rail indicators."""
    def __init__(self):
        self.partition_id = 24
        self.registered_rail = "ACH"
    def score_rail_subset(self, indicators: List[FraudIndicator]) -> float:
        return sum(ind.risk_points for ind in indicators if ind.rail.value == self.registered_rail)

class IndicatorAggregatorPartition_25:
    """Aggregator partition 25 managing real-time rail indicators."""
    def __init__(self):
        self.partition_id = 25
        self.registered_rail = "WIRE"
    def score_rail_subset(self, indicators: List[FraudIndicator]) -> float:
        return sum(ind.risk_points for ind in indicators if ind.rail.value == self.registered_rail)

class IndicatorAggregatorPartition_26:
    """Aggregator partition 26 managing real-time rail indicators."""
    def __init__(self):
        self.partition_id = 26
        self.registered_rail = "CARD_POS"
    def score_rail_subset(self, indicators: List[FraudIndicator]) -> float:
        return sum(ind.risk_points for ind in indicators if ind.rail.value == self.registered_rail)

class IndicatorAggregatorPartition_27:
    """Aggregator partition 27 managing real-time rail indicators."""
    def __init__(self):
        self.partition_id = 27
        self.registered_rail = "CARD_CNP"
    def score_rail_subset(self, indicators: List[FraudIndicator]) -> float:
        return sum(ind.risk_points for ind in indicators if ind.rail.value == self.registered_rail)

class IndicatorAggregatorPartition_28:
    """Aggregator partition 28 managing real-time rail indicators."""
    def __init__(self):
        self.partition_id = 28
        self.registered_rail = "UPI"
    def score_rail_subset(self, indicators: List[FraudIndicator]) -> float:
        return sum(ind.risk_points for ind in indicators if ind.rail.value == self.registered_rail)

class IndicatorAggregatorPartition_29:
    """Aggregator partition 29 managing real-time rail indicators."""
    def __init__(self):
        self.partition_id = 29
        self.registered_rail = "CRYPTO"
    def score_rail_subset(self, indicators: List[FraudIndicator]) -> float:
        return sum(ind.risk_points for ind in indicators if ind.rail.value == self.registered_rail)