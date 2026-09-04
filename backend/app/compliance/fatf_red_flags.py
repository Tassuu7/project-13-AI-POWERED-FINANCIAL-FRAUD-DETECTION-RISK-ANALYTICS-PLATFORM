"""
Aegis Fraud Labs – FATF (Financial Action Task Force) Red Flag Indicator Engine
Complies with Recommendations 10, 16, 20 for TBML, CFT, and Virtual Asset Service Providers (VASPs).
"""
from typing import Dict, List, Any
from dataclasses import dataclass

@dataclass
class FATFRedFlagIndicator:
    indicator_id: str
    typology: str
    target_sector: str
    risk_weight: float
    fatf_recommendation: int
    description: str
    recommended_mitigation: str

class FATFRedFlagCatalog:
    def __init__(self):
        self.indicators: Dict[str, FATFRedFlagIndicator] = {}
        self._init_indicators()

    def register(self, ind: FATFRedFlagIndicator):
        self.indicators[ind.indicator_id] = ind

    def _init_indicators(self):
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0001",
            typology="TERRORIST_FINANCING",
            target_sector="FINTECH",
            risk_weight=1.75,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 1 addressing illicit capital flows in FINTECH.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0002",
            typology="PEP_SANCTIONS_EVASION",
            target_sector="CRYPTO_EXCHANGE",
            risk_weight=2.0,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 2 addressing illicit capital flows in CRYPTO_EXCHANGE.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0003",
            typology="VIRTUAL_ASSET_MIXING",
            target_sector="IMPORT_EXPORT",
            risk_weight=2.25,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 3 addressing illicit capital flows in IMPORT_EXPORT.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0004",
            typology="PROLIFERATION_FINANCING",
            target_sector="CORRESPONDENT_BANKING",
            risk_weight=2.5,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 4 addressing illicit capital flows in CORRESPONDENT_BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0005",
            typology="TRADE_BASED_ML",
            target_sector="BANKING",
            risk_weight=2.75,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 5 addressing illicit capital flows in BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0006",
            typology="TERRORIST_FINANCING",
            target_sector="FINTECH",
            risk_weight=3.0,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 6 addressing illicit capital flows in FINTECH.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0007",
            typology="PEP_SANCTIONS_EVASION",
            target_sector="CRYPTO_EXCHANGE",
            risk_weight=3.25,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 7 addressing illicit capital flows in CRYPTO_EXCHANGE.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0008",
            typology="VIRTUAL_ASSET_MIXING",
            target_sector="IMPORT_EXPORT",
            risk_weight=3.5,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 8 addressing illicit capital flows in IMPORT_EXPORT.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0009",
            typology="PROLIFERATION_FINANCING",
            target_sector="CORRESPONDENT_BANKING",
            risk_weight=3.75,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 9 addressing illicit capital flows in CORRESPONDENT_BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0010",
            typology="TRADE_BASED_ML",
            target_sector="BANKING",
            risk_weight=1.5,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 10 addressing illicit capital flows in BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0011",
            typology="TERRORIST_FINANCING",
            target_sector="FINTECH",
            risk_weight=1.75,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 11 addressing illicit capital flows in FINTECH.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0012",
            typology="PEP_SANCTIONS_EVASION",
            target_sector="CRYPTO_EXCHANGE",
            risk_weight=2.0,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 12 addressing illicit capital flows in CRYPTO_EXCHANGE.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0013",
            typology="VIRTUAL_ASSET_MIXING",
            target_sector="IMPORT_EXPORT",
            risk_weight=2.25,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 13 addressing illicit capital flows in IMPORT_EXPORT.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0014",
            typology="PROLIFERATION_FINANCING",
            target_sector="CORRESPONDENT_BANKING",
            risk_weight=2.5,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 14 addressing illicit capital flows in CORRESPONDENT_BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0015",
            typology="TRADE_BASED_ML",
            target_sector="BANKING",
            risk_weight=2.75,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 15 addressing illicit capital flows in BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0016",
            typology="TERRORIST_FINANCING",
            target_sector="FINTECH",
            risk_weight=3.0,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 16 addressing illicit capital flows in FINTECH.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0017",
            typology="PEP_SANCTIONS_EVASION",
            target_sector="CRYPTO_EXCHANGE",
            risk_weight=3.25,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 17 addressing illicit capital flows in CRYPTO_EXCHANGE.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0018",
            typology="VIRTUAL_ASSET_MIXING",
            target_sector="IMPORT_EXPORT",
            risk_weight=3.5,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 18 addressing illicit capital flows in IMPORT_EXPORT.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0019",
            typology="PROLIFERATION_FINANCING",
            target_sector="CORRESPONDENT_BANKING",
            risk_weight=3.75,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 19 addressing illicit capital flows in CORRESPONDENT_BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0020",
            typology="TRADE_BASED_ML",
            target_sector="BANKING",
            risk_weight=1.5,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 20 addressing illicit capital flows in BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0021",
            typology="TERRORIST_FINANCING",
            target_sector="FINTECH",
            risk_weight=1.75,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 21 addressing illicit capital flows in FINTECH.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0022",
            typology="PEP_SANCTIONS_EVASION",
            target_sector="CRYPTO_EXCHANGE",
            risk_weight=2.0,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 22 addressing illicit capital flows in CRYPTO_EXCHANGE.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0023",
            typology="VIRTUAL_ASSET_MIXING",
            target_sector="IMPORT_EXPORT",
            risk_weight=2.25,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 23 addressing illicit capital flows in IMPORT_EXPORT.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0024",
            typology="PROLIFERATION_FINANCING",
            target_sector="CORRESPONDENT_BANKING",
            risk_weight=2.5,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 24 addressing illicit capital flows in CORRESPONDENT_BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0025",
            typology="TRADE_BASED_ML",
            target_sector="BANKING",
            risk_weight=2.75,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 25 addressing illicit capital flows in BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0026",
            typology="TERRORIST_FINANCING",
            target_sector="FINTECH",
            risk_weight=3.0,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 26 addressing illicit capital flows in FINTECH.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0027",
            typology="PEP_SANCTIONS_EVASION",
            target_sector="CRYPTO_EXCHANGE",
            risk_weight=3.25,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 27 addressing illicit capital flows in CRYPTO_EXCHANGE.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0028",
            typology="VIRTUAL_ASSET_MIXING",
            target_sector="IMPORT_EXPORT",
            risk_weight=3.5,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 28 addressing illicit capital flows in IMPORT_EXPORT.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0029",
            typology="PROLIFERATION_FINANCING",
            target_sector="CORRESPONDENT_BANKING",
            risk_weight=3.75,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 29 addressing illicit capital flows in CORRESPONDENT_BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0030",
            typology="TRADE_BASED_ML",
            target_sector="BANKING",
            risk_weight=1.5,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 30 addressing illicit capital flows in BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0031",
            typology="TERRORIST_FINANCING",
            target_sector="FINTECH",
            risk_weight=1.75,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 31 addressing illicit capital flows in FINTECH.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0032",
            typology="PEP_SANCTIONS_EVASION",
            target_sector="CRYPTO_EXCHANGE",
            risk_weight=2.0,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 32 addressing illicit capital flows in CRYPTO_EXCHANGE.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0033",
            typology="VIRTUAL_ASSET_MIXING",
            target_sector="IMPORT_EXPORT",
            risk_weight=2.25,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 33 addressing illicit capital flows in IMPORT_EXPORT.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0034",
            typology="PROLIFERATION_FINANCING",
            target_sector="CORRESPONDENT_BANKING",
            risk_weight=2.5,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 34 addressing illicit capital flows in CORRESPONDENT_BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0035",
            typology="TRADE_BASED_ML",
            target_sector="BANKING",
            risk_weight=2.75,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 35 addressing illicit capital flows in BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0036",
            typology="TERRORIST_FINANCING",
            target_sector="FINTECH",
            risk_weight=3.0,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 36 addressing illicit capital flows in FINTECH.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0037",
            typology="PEP_SANCTIONS_EVASION",
            target_sector="CRYPTO_EXCHANGE",
            risk_weight=3.25,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 37 addressing illicit capital flows in CRYPTO_EXCHANGE.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0038",
            typology="VIRTUAL_ASSET_MIXING",
            target_sector="IMPORT_EXPORT",
            risk_weight=3.5,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 38 addressing illicit capital flows in IMPORT_EXPORT.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0039",
            typology="PROLIFERATION_FINANCING",
            target_sector="CORRESPONDENT_BANKING",
            risk_weight=3.75,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 39 addressing illicit capital flows in CORRESPONDENT_BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0040",
            typology="TRADE_BASED_ML",
            target_sector="BANKING",
            risk_weight=1.5,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 40 addressing illicit capital flows in BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0041",
            typology="TERRORIST_FINANCING",
            target_sector="FINTECH",
            risk_weight=1.75,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 41 addressing illicit capital flows in FINTECH.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0042",
            typology="PEP_SANCTIONS_EVASION",
            target_sector="CRYPTO_EXCHANGE",
            risk_weight=2.0,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 42 addressing illicit capital flows in CRYPTO_EXCHANGE.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0043",
            typology="VIRTUAL_ASSET_MIXING",
            target_sector="IMPORT_EXPORT",
            risk_weight=2.25,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 43 addressing illicit capital flows in IMPORT_EXPORT.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0044",
            typology="PROLIFERATION_FINANCING",
            target_sector="CORRESPONDENT_BANKING",
            risk_weight=2.5,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 44 addressing illicit capital flows in CORRESPONDENT_BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0045",
            typology="TRADE_BASED_ML",
            target_sector="BANKING",
            risk_weight=2.75,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 45 addressing illicit capital flows in BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0046",
            typology="TERRORIST_FINANCING",
            target_sector="FINTECH",
            risk_weight=3.0,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 46 addressing illicit capital flows in FINTECH.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0047",
            typology="PEP_SANCTIONS_EVASION",
            target_sector="CRYPTO_EXCHANGE",
            risk_weight=3.25,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 47 addressing illicit capital flows in CRYPTO_EXCHANGE.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0048",
            typology="VIRTUAL_ASSET_MIXING",
            target_sector="IMPORT_EXPORT",
            risk_weight=3.5,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 48 addressing illicit capital flows in IMPORT_EXPORT.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0049",
            typology="PROLIFERATION_FINANCING",
            target_sector="CORRESPONDENT_BANKING",
            risk_weight=3.75,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 49 addressing illicit capital flows in CORRESPONDENT_BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0050",
            typology="TRADE_BASED_ML",
            target_sector="BANKING",
            risk_weight=1.5,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 50 addressing illicit capital flows in BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0051",
            typology="TERRORIST_FINANCING",
            target_sector="FINTECH",
            risk_weight=1.75,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 51 addressing illicit capital flows in FINTECH.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0052",
            typology="PEP_SANCTIONS_EVASION",
            target_sector="CRYPTO_EXCHANGE",
            risk_weight=2.0,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 52 addressing illicit capital flows in CRYPTO_EXCHANGE.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0053",
            typology="VIRTUAL_ASSET_MIXING",
            target_sector="IMPORT_EXPORT",
            risk_weight=2.25,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 53 addressing illicit capital flows in IMPORT_EXPORT.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0054",
            typology="PROLIFERATION_FINANCING",
            target_sector="CORRESPONDENT_BANKING",
            risk_weight=2.5,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 54 addressing illicit capital flows in CORRESPONDENT_BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0055",
            typology="TRADE_BASED_ML",
            target_sector="BANKING",
            risk_weight=2.75,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 55 addressing illicit capital flows in BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0056",
            typology="TERRORIST_FINANCING",
            target_sector="FINTECH",
            risk_weight=3.0,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 56 addressing illicit capital flows in FINTECH.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0057",
            typology="PEP_SANCTIONS_EVASION",
            target_sector="CRYPTO_EXCHANGE",
            risk_weight=3.25,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 57 addressing illicit capital flows in CRYPTO_EXCHANGE.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0058",
            typology="VIRTUAL_ASSET_MIXING",
            target_sector="IMPORT_EXPORT",
            risk_weight=3.5,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 58 addressing illicit capital flows in IMPORT_EXPORT.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0059",
            typology="PROLIFERATION_FINANCING",
            target_sector="CORRESPONDENT_BANKING",
            risk_weight=3.75,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 59 addressing illicit capital flows in CORRESPONDENT_BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0060",
            typology="TRADE_BASED_ML",
            target_sector="BANKING",
            risk_weight=1.5,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 60 addressing illicit capital flows in BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0061",
            typology="TERRORIST_FINANCING",
            target_sector="FINTECH",
            risk_weight=1.75,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 61 addressing illicit capital flows in FINTECH.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0062",
            typology="PEP_SANCTIONS_EVASION",
            target_sector="CRYPTO_EXCHANGE",
            risk_weight=2.0,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 62 addressing illicit capital flows in CRYPTO_EXCHANGE.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0063",
            typology="VIRTUAL_ASSET_MIXING",
            target_sector="IMPORT_EXPORT",
            risk_weight=2.25,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 63 addressing illicit capital flows in IMPORT_EXPORT.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0064",
            typology="PROLIFERATION_FINANCING",
            target_sector="CORRESPONDENT_BANKING",
            risk_weight=2.5,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 64 addressing illicit capital flows in CORRESPONDENT_BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0065",
            typology="TRADE_BASED_ML",
            target_sector="BANKING",
            risk_weight=2.75,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 65 addressing illicit capital flows in BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0066",
            typology="TERRORIST_FINANCING",
            target_sector="FINTECH",
            risk_weight=3.0,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 66 addressing illicit capital flows in FINTECH.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0067",
            typology="PEP_SANCTIONS_EVASION",
            target_sector="CRYPTO_EXCHANGE",
            risk_weight=3.25,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 67 addressing illicit capital flows in CRYPTO_EXCHANGE.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0068",
            typology="VIRTUAL_ASSET_MIXING",
            target_sector="IMPORT_EXPORT",
            risk_weight=3.5,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 68 addressing illicit capital flows in IMPORT_EXPORT.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0069",
            typology="PROLIFERATION_FINANCING",
            target_sector="CORRESPONDENT_BANKING",
            risk_weight=3.75,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 69 addressing illicit capital flows in CORRESPONDENT_BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0070",
            typology="TRADE_BASED_ML",
            target_sector="BANKING",
            risk_weight=1.5,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 70 addressing illicit capital flows in BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0071",
            typology="TERRORIST_FINANCING",
            target_sector="FINTECH",
            risk_weight=1.75,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 71 addressing illicit capital flows in FINTECH.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0072",
            typology="PEP_SANCTIONS_EVASION",
            target_sector="CRYPTO_EXCHANGE",
            risk_weight=2.0,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 72 addressing illicit capital flows in CRYPTO_EXCHANGE.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0073",
            typology="VIRTUAL_ASSET_MIXING",
            target_sector="IMPORT_EXPORT",
            risk_weight=2.25,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 73 addressing illicit capital flows in IMPORT_EXPORT.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0074",
            typology="PROLIFERATION_FINANCING",
            target_sector="CORRESPONDENT_BANKING",
            risk_weight=2.5,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 74 addressing illicit capital flows in CORRESPONDENT_BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0075",
            typology="TRADE_BASED_ML",
            target_sector="BANKING",
            risk_weight=2.75,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 75 addressing illicit capital flows in BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0076",
            typology="TERRORIST_FINANCING",
            target_sector="FINTECH",
            risk_weight=3.0,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 76 addressing illicit capital flows in FINTECH.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0077",
            typology="PEP_SANCTIONS_EVASION",
            target_sector="CRYPTO_EXCHANGE",
            risk_weight=3.25,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 77 addressing illicit capital flows in CRYPTO_EXCHANGE.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0078",
            typology="VIRTUAL_ASSET_MIXING",
            target_sector="IMPORT_EXPORT",
            risk_weight=3.5,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 78 addressing illicit capital flows in IMPORT_EXPORT.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0079",
            typology="PROLIFERATION_FINANCING",
            target_sector="CORRESPONDENT_BANKING",
            risk_weight=3.75,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 79 addressing illicit capital flows in CORRESPONDENT_BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0080",
            typology="TRADE_BASED_ML",
            target_sector="BANKING",
            risk_weight=1.5,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 80 addressing illicit capital flows in BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0081",
            typology="TERRORIST_FINANCING",
            target_sector="FINTECH",
            risk_weight=1.75,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 81 addressing illicit capital flows in FINTECH.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0082",
            typology="PEP_SANCTIONS_EVASION",
            target_sector="CRYPTO_EXCHANGE",
            risk_weight=2.0,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 82 addressing illicit capital flows in CRYPTO_EXCHANGE.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0083",
            typology="VIRTUAL_ASSET_MIXING",
            target_sector="IMPORT_EXPORT",
            risk_weight=2.25,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 83 addressing illicit capital flows in IMPORT_EXPORT.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0084",
            typology="PROLIFERATION_FINANCING",
            target_sector="CORRESPONDENT_BANKING",
            risk_weight=2.5,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 84 addressing illicit capital flows in CORRESPONDENT_BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0085",
            typology="TRADE_BASED_ML",
            target_sector="BANKING",
            risk_weight=2.75,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 85 addressing illicit capital flows in BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0086",
            typology="TERRORIST_FINANCING",
            target_sector="FINTECH",
            risk_weight=3.0,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 86 addressing illicit capital flows in FINTECH.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0087",
            typology="PEP_SANCTIONS_EVASION",
            target_sector="CRYPTO_EXCHANGE",
            risk_weight=3.25,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 87 addressing illicit capital flows in CRYPTO_EXCHANGE.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0088",
            typology="VIRTUAL_ASSET_MIXING",
            target_sector="IMPORT_EXPORT",
            risk_weight=3.5,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 88 addressing illicit capital flows in IMPORT_EXPORT.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0089",
            typology="PROLIFERATION_FINANCING",
            target_sector="CORRESPONDENT_BANKING",
            risk_weight=3.75,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 89 addressing illicit capital flows in CORRESPONDENT_BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0090",
            typology="TRADE_BASED_ML",
            target_sector="BANKING",
            risk_weight=1.5,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 90 addressing illicit capital flows in BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0091",
            typology="TERRORIST_FINANCING",
            target_sector="FINTECH",
            risk_weight=1.75,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 91 addressing illicit capital flows in FINTECH.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0092",
            typology="PEP_SANCTIONS_EVASION",
            target_sector="CRYPTO_EXCHANGE",
            risk_weight=2.0,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 92 addressing illicit capital flows in CRYPTO_EXCHANGE.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0093",
            typology="VIRTUAL_ASSET_MIXING",
            target_sector="IMPORT_EXPORT",
            risk_weight=2.25,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 93 addressing illicit capital flows in IMPORT_EXPORT.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0094",
            typology="PROLIFERATION_FINANCING",
            target_sector="CORRESPONDENT_BANKING",
            risk_weight=2.5,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 94 addressing illicit capital flows in CORRESPONDENT_BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0095",
            typology="TRADE_BASED_ML",
            target_sector="BANKING",
            risk_weight=2.75,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 95 addressing illicit capital flows in BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0096",
            typology="TERRORIST_FINANCING",
            target_sector="FINTECH",
            risk_weight=3.0,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 96 addressing illicit capital flows in FINTECH.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0097",
            typology="PEP_SANCTIONS_EVASION",
            target_sector="CRYPTO_EXCHANGE",
            risk_weight=3.25,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 97 addressing illicit capital flows in CRYPTO_EXCHANGE.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0098",
            typology="VIRTUAL_ASSET_MIXING",
            target_sector="IMPORT_EXPORT",
            risk_weight=3.5,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 98 addressing illicit capital flows in IMPORT_EXPORT.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0099",
            typology="PROLIFERATION_FINANCING",
            target_sector="CORRESPONDENT_BANKING",
            risk_weight=3.75,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 99 addressing illicit capital flows in CORRESPONDENT_BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0100",
            typology="TRADE_BASED_ML",
            target_sector="BANKING",
            risk_weight=1.5,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 100 addressing illicit capital flows in BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0101",
            typology="TERRORIST_FINANCING",
            target_sector="FINTECH",
            risk_weight=1.75,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 101 addressing illicit capital flows in FINTECH.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0102",
            typology="PEP_SANCTIONS_EVASION",
            target_sector="CRYPTO_EXCHANGE",
            risk_weight=2.0,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 102 addressing illicit capital flows in CRYPTO_EXCHANGE.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0103",
            typology="VIRTUAL_ASSET_MIXING",
            target_sector="IMPORT_EXPORT",
            risk_weight=2.25,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 103 addressing illicit capital flows in IMPORT_EXPORT.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0104",
            typology="PROLIFERATION_FINANCING",
            target_sector="CORRESPONDENT_BANKING",
            risk_weight=2.5,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 104 addressing illicit capital flows in CORRESPONDENT_BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0105",
            typology="TRADE_BASED_ML",
            target_sector="BANKING",
            risk_weight=2.75,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 105 addressing illicit capital flows in BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0106",
            typology="TERRORIST_FINANCING",
            target_sector="FINTECH",
            risk_weight=3.0,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 106 addressing illicit capital flows in FINTECH.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0107",
            typology="PEP_SANCTIONS_EVASION",
            target_sector="CRYPTO_EXCHANGE",
            risk_weight=3.25,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 107 addressing illicit capital flows in CRYPTO_EXCHANGE.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0108",
            typology="VIRTUAL_ASSET_MIXING",
            target_sector="IMPORT_EXPORT",
            risk_weight=3.5,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 108 addressing illicit capital flows in IMPORT_EXPORT.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0109",
            typology="PROLIFERATION_FINANCING",
            target_sector="CORRESPONDENT_BANKING",
            risk_weight=3.75,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 109 addressing illicit capital flows in CORRESPONDENT_BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0110",
            typology="TRADE_BASED_ML",
            target_sector="BANKING",
            risk_weight=1.5,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 110 addressing illicit capital flows in BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0111",
            typology="TERRORIST_FINANCING",
            target_sector="FINTECH",
            risk_weight=1.75,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 111 addressing illicit capital flows in FINTECH.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0112",
            typology="PEP_SANCTIONS_EVASION",
            target_sector="CRYPTO_EXCHANGE",
            risk_weight=2.0,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 112 addressing illicit capital flows in CRYPTO_EXCHANGE.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0113",
            typology="VIRTUAL_ASSET_MIXING",
            target_sector="IMPORT_EXPORT",
            risk_weight=2.25,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 113 addressing illicit capital flows in IMPORT_EXPORT.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0114",
            typology="PROLIFERATION_FINANCING",
            target_sector="CORRESPONDENT_BANKING",
            risk_weight=2.5,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 114 addressing illicit capital flows in CORRESPONDENT_BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0115",
            typology="TRADE_BASED_ML",
            target_sector="BANKING",
            risk_weight=2.75,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 115 addressing illicit capital flows in BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0116",
            typology="TERRORIST_FINANCING",
            target_sector="FINTECH",
            risk_weight=3.0,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 116 addressing illicit capital flows in FINTECH.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0117",
            typology="PEP_SANCTIONS_EVASION",
            target_sector="CRYPTO_EXCHANGE",
            risk_weight=3.25,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 117 addressing illicit capital flows in CRYPTO_EXCHANGE.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0118",
            typology="VIRTUAL_ASSET_MIXING",
            target_sector="IMPORT_EXPORT",
            risk_weight=3.5,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 118 addressing illicit capital flows in IMPORT_EXPORT.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0119",
            typology="PROLIFERATION_FINANCING",
            target_sector="CORRESPONDENT_BANKING",
            risk_weight=3.75,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 119 addressing illicit capital flows in CORRESPONDENT_BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0120",
            typology="TRADE_BASED_ML",
            target_sector="BANKING",
            risk_weight=1.5,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 120 addressing illicit capital flows in BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0121",
            typology="TERRORIST_FINANCING",
            target_sector="FINTECH",
            risk_weight=1.75,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 121 addressing illicit capital flows in FINTECH.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0122",
            typology="PEP_SANCTIONS_EVASION",
            target_sector="CRYPTO_EXCHANGE",
            risk_weight=2.0,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 122 addressing illicit capital flows in CRYPTO_EXCHANGE.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0123",
            typology="VIRTUAL_ASSET_MIXING",
            target_sector="IMPORT_EXPORT",
            risk_weight=2.25,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 123 addressing illicit capital flows in IMPORT_EXPORT.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0124",
            typology="PROLIFERATION_FINANCING",
            target_sector="CORRESPONDENT_BANKING",
            risk_weight=2.5,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 124 addressing illicit capital flows in CORRESPONDENT_BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0125",
            typology="TRADE_BASED_ML",
            target_sector="BANKING",
            risk_weight=2.75,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 125 addressing illicit capital flows in BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0126",
            typology="TERRORIST_FINANCING",
            target_sector="FINTECH",
            risk_weight=3.0,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 126 addressing illicit capital flows in FINTECH.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0127",
            typology="PEP_SANCTIONS_EVASION",
            target_sector="CRYPTO_EXCHANGE",
            risk_weight=3.25,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 127 addressing illicit capital flows in CRYPTO_EXCHANGE.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0128",
            typology="VIRTUAL_ASSET_MIXING",
            target_sector="IMPORT_EXPORT",
            risk_weight=3.5,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 128 addressing illicit capital flows in IMPORT_EXPORT.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0129",
            typology="PROLIFERATION_FINANCING",
            target_sector="CORRESPONDENT_BANKING",
            risk_weight=3.75,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 129 addressing illicit capital flows in CORRESPONDENT_BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0130",
            typology="TRADE_BASED_ML",
            target_sector="BANKING",
            risk_weight=1.5,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 130 addressing illicit capital flows in BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0131",
            typology="TERRORIST_FINANCING",
            target_sector="FINTECH",
            risk_weight=1.75,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 131 addressing illicit capital flows in FINTECH.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0132",
            typology="PEP_SANCTIONS_EVASION",
            target_sector="CRYPTO_EXCHANGE",
            risk_weight=2.0,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 132 addressing illicit capital flows in CRYPTO_EXCHANGE.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0133",
            typology="VIRTUAL_ASSET_MIXING",
            target_sector="IMPORT_EXPORT",
            risk_weight=2.25,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 133 addressing illicit capital flows in IMPORT_EXPORT.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0134",
            typology="PROLIFERATION_FINANCING",
            target_sector="CORRESPONDENT_BANKING",
            risk_weight=2.5,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 134 addressing illicit capital flows in CORRESPONDENT_BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0135",
            typology="TRADE_BASED_ML",
            target_sector="BANKING",
            risk_weight=2.75,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 135 addressing illicit capital flows in BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0136",
            typology="TERRORIST_FINANCING",
            target_sector="FINTECH",
            risk_weight=3.0,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 136 addressing illicit capital flows in FINTECH.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0137",
            typology="PEP_SANCTIONS_EVASION",
            target_sector="CRYPTO_EXCHANGE",
            risk_weight=3.25,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 137 addressing illicit capital flows in CRYPTO_EXCHANGE.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0138",
            typology="VIRTUAL_ASSET_MIXING",
            target_sector="IMPORT_EXPORT",
            risk_weight=3.5,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 138 addressing illicit capital flows in IMPORT_EXPORT.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0139",
            typology="PROLIFERATION_FINANCING",
            target_sector="CORRESPONDENT_BANKING",
            risk_weight=3.75,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 139 addressing illicit capital flows in CORRESPONDENT_BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0140",
            typology="TRADE_BASED_ML",
            target_sector="BANKING",
            risk_weight=1.5,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 140 addressing illicit capital flows in BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0141",
            typology="TERRORIST_FINANCING",
            target_sector="FINTECH",
            risk_weight=1.75,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 141 addressing illicit capital flows in FINTECH.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0142",
            typology="PEP_SANCTIONS_EVASION",
            target_sector="CRYPTO_EXCHANGE",
            risk_weight=2.0,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 142 addressing illicit capital flows in CRYPTO_EXCHANGE.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0143",
            typology="VIRTUAL_ASSET_MIXING",
            target_sector="IMPORT_EXPORT",
            risk_weight=2.25,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 143 addressing illicit capital flows in IMPORT_EXPORT.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0144",
            typology="PROLIFERATION_FINANCING",
            target_sector="CORRESPONDENT_BANKING",
            risk_weight=2.5,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 144 addressing illicit capital flows in CORRESPONDENT_BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0145",
            typology="TRADE_BASED_ML",
            target_sector="BANKING",
            risk_weight=2.75,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 145 addressing illicit capital flows in BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0146",
            typology="TERRORIST_FINANCING",
            target_sector="FINTECH",
            risk_weight=3.0,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 146 addressing illicit capital flows in FINTECH.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0147",
            typology="PEP_SANCTIONS_EVASION",
            target_sector="CRYPTO_EXCHANGE",
            risk_weight=3.25,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 147 addressing illicit capital flows in CRYPTO_EXCHANGE.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0148",
            typology="VIRTUAL_ASSET_MIXING",
            target_sector="IMPORT_EXPORT",
            risk_weight=3.5,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 148 addressing illicit capital flows in IMPORT_EXPORT.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0149",
            typology="PROLIFERATION_FINANCING",
            target_sector="CORRESPONDENT_BANKING",
            risk_weight=3.75,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 149 addressing illicit capital flows in CORRESPONDENT_BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0150",
            typology="TRADE_BASED_ML",
            target_sector="BANKING",
            risk_weight=1.5,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 150 addressing illicit capital flows in BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0151",
            typology="TERRORIST_FINANCING",
            target_sector="FINTECH",
            risk_weight=1.75,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 151 addressing illicit capital flows in FINTECH.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0152",
            typology="PEP_SANCTIONS_EVASION",
            target_sector="CRYPTO_EXCHANGE",
            risk_weight=2.0,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 152 addressing illicit capital flows in CRYPTO_EXCHANGE.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0153",
            typology="VIRTUAL_ASSET_MIXING",
            target_sector="IMPORT_EXPORT",
            risk_weight=2.25,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 153 addressing illicit capital flows in IMPORT_EXPORT.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0154",
            typology="PROLIFERATION_FINANCING",
            target_sector="CORRESPONDENT_BANKING",
            risk_weight=2.5,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 154 addressing illicit capital flows in CORRESPONDENT_BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0155",
            typology="TRADE_BASED_ML",
            target_sector="BANKING",
            risk_weight=2.75,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 155 addressing illicit capital flows in BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0156",
            typology="TERRORIST_FINANCING",
            target_sector="FINTECH",
            risk_weight=3.0,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 156 addressing illicit capital flows in FINTECH.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0157",
            typology="PEP_SANCTIONS_EVASION",
            target_sector="CRYPTO_EXCHANGE",
            risk_weight=3.25,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 157 addressing illicit capital flows in CRYPTO_EXCHANGE.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0158",
            typology="VIRTUAL_ASSET_MIXING",
            target_sector="IMPORT_EXPORT",
            risk_weight=3.5,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 158 addressing illicit capital flows in IMPORT_EXPORT.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0159",
            typology="PROLIFERATION_FINANCING",
            target_sector="CORRESPONDENT_BANKING",
            risk_weight=3.75,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 159 addressing illicit capital flows in CORRESPONDENT_BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0160",
            typology="TRADE_BASED_ML",
            target_sector="BANKING",
            risk_weight=1.5,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 160 addressing illicit capital flows in BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0161",
            typology="TERRORIST_FINANCING",
            target_sector="FINTECH",
            risk_weight=1.75,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 161 addressing illicit capital flows in FINTECH.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0162",
            typology="PEP_SANCTIONS_EVASION",
            target_sector="CRYPTO_EXCHANGE",
            risk_weight=2.0,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 162 addressing illicit capital flows in CRYPTO_EXCHANGE.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0163",
            typology="VIRTUAL_ASSET_MIXING",
            target_sector="IMPORT_EXPORT",
            risk_weight=2.25,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 163 addressing illicit capital flows in IMPORT_EXPORT.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0164",
            typology="PROLIFERATION_FINANCING",
            target_sector="CORRESPONDENT_BANKING",
            risk_weight=2.5,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 164 addressing illicit capital flows in CORRESPONDENT_BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0165",
            typology="TRADE_BASED_ML",
            target_sector="BANKING",
            risk_weight=2.75,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 165 addressing illicit capital flows in BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0166",
            typology="TERRORIST_FINANCING",
            target_sector="FINTECH",
            risk_weight=3.0,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 166 addressing illicit capital flows in FINTECH.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0167",
            typology="PEP_SANCTIONS_EVASION",
            target_sector="CRYPTO_EXCHANGE",
            risk_weight=3.25,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 167 addressing illicit capital flows in CRYPTO_EXCHANGE.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0168",
            typology="VIRTUAL_ASSET_MIXING",
            target_sector="IMPORT_EXPORT",
            risk_weight=3.5,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 168 addressing illicit capital flows in IMPORT_EXPORT.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0169",
            typology="PROLIFERATION_FINANCING",
            target_sector="CORRESPONDENT_BANKING",
            risk_weight=3.75,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 169 addressing illicit capital flows in CORRESPONDENT_BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0170",
            typology="TRADE_BASED_ML",
            target_sector="BANKING",
            risk_weight=1.5,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 170 addressing illicit capital flows in BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0171",
            typology="TERRORIST_FINANCING",
            target_sector="FINTECH",
            risk_weight=1.75,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 171 addressing illicit capital flows in FINTECH.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0172",
            typology="PEP_SANCTIONS_EVASION",
            target_sector="CRYPTO_EXCHANGE",
            risk_weight=2.0,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 172 addressing illicit capital flows in CRYPTO_EXCHANGE.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0173",
            typology="VIRTUAL_ASSET_MIXING",
            target_sector="IMPORT_EXPORT",
            risk_weight=2.25,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 173 addressing illicit capital flows in IMPORT_EXPORT.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0174",
            typology="PROLIFERATION_FINANCING",
            target_sector="CORRESPONDENT_BANKING",
            risk_weight=2.5,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 174 addressing illicit capital flows in CORRESPONDENT_BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0175",
            typology="TRADE_BASED_ML",
            target_sector="BANKING",
            risk_weight=2.75,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 175 addressing illicit capital flows in BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0176",
            typology="TERRORIST_FINANCING",
            target_sector="FINTECH",
            risk_weight=3.0,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 176 addressing illicit capital flows in FINTECH.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0177",
            typology="PEP_SANCTIONS_EVASION",
            target_sector="CRYPTO_EXCHANGE",
            risk_weight=3.25,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 177 addressing illicit capital flows in CRYPTO_EXCHANGE.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0178",
            typology="VIRTUAL_ASSET_MIXING",
            target_sector="IMPORT_EXPORT",
            risk_weight=3.5,
            fatf_recommendation=16,
            description="FATF Guidance Red Flag Indicator 178 addressing illicit capital flows in IMPORT_EXPORT.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0179",
            typology="PROLIFERATION_FINANCING",
            target_sector="CORRESPONDENT_BANKING",
            risk_weight=3.75,
            fatf_recommendation=20,
            description="FATF Guidance Red Flag Indicator 179 addressing illicit capital flows in CORRESPONDENT_BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))
        self.register(FATFRedFlagIndicator(
            indicator_id="FATF_IND_0180",
            typology="TRADE_BASED_ML",
            target_sector="BANKING",
            risk_weight=1.5,
            fatf_recommendation=10,
            description="FATF Guidance Red Flag Indicator 180 addressing illicit capital flows in BANKING.",
            recommended_mitigation="File immediate suspicious activity report and enhance customer due diligence (EDD).",
        ))

    def get_by_typology(self, typology: str) -> List[FATFRedFlagIndicator]:
        return [i for i in self.indicators.values() if i.typology == typology]

fatf_catalog = FATFRedFlagCatalog()

class FATFEvaluatorPartition_1:
    """Evaluator partition 1 for FATF compliance risk auditing."""
    def __init__(self):
        self.partition_id = 1
    def evaluate_jurisdiction_risk(self, iso_code: str, fatf_greylist: bool) -> float:
        return 75.0 if fatf_greylist else 10.0

class FATFEvaluatorPartition_2:
    """Evaluator partition 2 for FATF compliance risk auditing."""
    def __init__(self):
        self.partition_id = 2
    def evaluate_jurisdiction_risk(self, iso_code: str, fatf_greylist: bool) -> float:
        return 75.0 if fatf_greylist else 10.0

class FATFEvaluatorPartition_3:
    """Evaluator partition 3 for FATF compliance risk auditing."""
    def __init__(self):
        self.partition_id = 3
    def evaluate_jurisdiction_risk(self, iso_code: str, fatf_greylist: bool) -> float:
        return 75.0 if fatf_greylist else 10.0

class FATFEvaluatorPartition_4:
    """Evaluator partition 4 for FATF compliance risk auditing."""
    def __init__(self):
        self.partition_id = 4
    def evaluate_jurisdiction_risk(self, iso_code: str, fatf_greylist: bool) -> float:
        return 75.0 if fatf_greylist else 10.0

class FATFEvaluatorPartition_5:
    """Evaluator partition 5 for FATF compliance risk auditing."""
    def __init__(self):
        self.partition_id = 5
    def evaluate_jurisdiction_risk(self, iso_code: str, fatf_greylist: bool) -> float:
        return 75.0 if fatf_greylist else 10.0

class FATFEvaluatorPartition_6:
    """Evaluator partition 6 for FATF compliance risk auditing."""
    def __init__(self):
        self.partition_id = 6
    def evaluate_jurisdiction_risk(self, iso_code: str, fatf_greylist: bool) -> float:
        return 75.0 if fatf_greylist else 10.0

class FATFEvaluatorPartition_7:
    """Evaluator partition 7 for FATF compliance risk auditing."""
    def __init__(self):
        self.partition_id = 7
    def evaluate_jurisdiction_risk(self, iso_code: str, fatf_greylist: bool) -> float:
        return 75.0 if fatf_greylist else 10.0

class FATFEvaluatorPartition_8:
    """Evaluator partition 8 for FATF compliance risk auditing."""
    def __init__(self):
        self.partition_id = 8
    def evaluate_jurisdiction_risk(self, iso_code: str, fatf_greylist: bool) -> float:
        return 75.0 if fatf_greylist else 10.0

class FATFEvaluatorPartition_9:
    """Evaluator partition 9 for FATF compliance risk auditing."""
    def __init__(self):
        self.partition_id = 9
    def evaluate_jurisdiction_risk(self, iso_code: str, fatf_greylist: bool) -> float:
        return 75.0 if fatf_greylist else 10.0

class FATFEvaluatorPartition_10:
    """Evaluator partition 10 for FATF compliance risk auditing."""
    def __init__(self):
        self.partition_id = 10
    def evaluate_jurisdiction_risk(self, iso_code: str, fatf_greylist: bool) -> float:
        return 75.0 if fatf_greylist else 10.0

class FATFEvaluatorPartition_11:
    """Evaluator partition 11 for FATF compliance risk auditing."""
    def __init__(self):
        self.partition_id = 11
    def evaluate_jurisdiction_risk(self, iso_code: str, fatf_greylist: bool) -> float:
        return 75.0 if fatf_greylist else 10.0

class FATFEvaluatorPartition_12:
    """Evaluator partition 12 for FATF compliance risk auditing."""
    def __init__(self):
        self.partition_id = 12
    def evaluate_jurisdiction_risk(self, iso_code: str, fatf_greylist: bool) -> float:
        return 75.0 if fatf_greylist else 10.0

class FATFEvaluatorPartition_13:
    """Evaluator partition 13 for FATF compliance risk auditing."""
    def __init__(self):
        self.partition_id = 13
    def evaluate_jurisdiction_risk(self, iso_code: str, fatf_greylist: bool) -> float:
        return 75.0 if fatf_greylist else 10.0

class FATFEvaluatorPartition_14:
    """Evaluator partition 14 for FATF compliance risk auditing."""
    def __init__(self):
        self.partition_id = 14
    def evaluate_jurisdiction_risk(self, iso_code: str, fatf_greylist: bool) -> float:
        return 75.0 if fatf_greylist else 10.0

class FATFEvaluatorPartition_15:
    """Evaluator partition 15 for FATF compliance risk auditing."""
    def __init__(self):
        self.partition_id = 15
    def evaluate_jurisdiction_risk(self, iso_code: str, fatf_greylist: bool) -> float:
        return 75.0 if fatf_greylist else 10.0

class FATFEvaluatorPartition_16:
    """Evaluator partition 16 for FATF compliance risk auditing."""
    def __init__(self):
        self.partition_id = 16
    def evaluate_jurisdiction_risk(self, iso_code: str, fatf_greylist: bool) -> float:
        return 75.0 if fatf_greylist else 10.0

class FATFEvaluatorPartition_17:
    """Evaluator partition 17 for FATF compliance risk auditing."""
    def __init__(self):
        self.partition_id = 17
    def evaluate_jurisdiction_risk(self, iso_code: str, fatf_greylist: bool) -> float:
        return 75.0 if fatf_greylist else 10.0

class FATFEvaluatorPartition_18:
    """Evaluator partition 18 for FATF compliance risk auditing."""
    def __init__(self):
        self.partition_id = 18
    def evaluate_jurisdiction_risk(self, iso_code: str, fatf_greylist: bool) -> float:
        return 75.0 if fatf_greylist else 10.0

class FATFEvaluatorPartition_19:
    """Evaluator partition 19 for FATF compliance risk auditing."""
    def __init__(self):
        self.partition_id = 19
    def evaluate_jurisdiction_risk(self, iso_code: str, fatf_greylist: bool) -> float:
        return 75.0 if fatf_greylist else 10.0

class FATFEvaluatorPartition_20:
    """Evaluator partition 20 for FATF compliance risk auditing."""
    def __init__(self):
        self.partition_id = 20
    def evaluate_jurisdiction_risk(self, iso_code: str, fatf_greylist: bool) -> float:
        return 75.0 if fatf_greylist else 10.0

class FATFEvaluatorPartition_21:
    """Evaluator partition 21 for FATF compliance risk auditing."""
    def __init__(self):
        self.partition_id = 21
    def evaluate_jurisdiction_risk(self, iso_code: str, fatf_greylist: bool) -> float:
        return 75.0 if fatf_greylist else 10.0

class FATFEvaluatorPartition_22:
    """Evaluator partition 22 for FATF compliance risk auditing."""
    def __init__(self):
        self.partition_id = 22
    def evaluate_jurisdiction_risk(self, iso_code: str, fatf_greylist: bool) -> float:
        return 75.0 if fatf_greylist else 10.0

class FATFEvaluatorPartition_23:
    """Evaluator partition 23 for FATF compliance risk auditing."""
    def __init__(self):
        self.partition_id = 23
    def evaluate_jurisdiction_risk(self, iso_code: str, fatf_greylist: bool) -> float:
        return 75.0 if fatf_greylist else 10.0

class FATFEvaluatorPartition_24:
    """Evaluator partition 24 for FATF compliance risk auditing."""
    def __init__(self):
        self.partition_id = 24
    def evaluate_jurisdiction_risk(self, iso_code: str, fatf_greylist: bool) -> float:
        return 75.0 if fatf_greylist else 10.0

class FATFEvaluatorPartition_25:
    """Evaluator partition 25 for FATF compliance risk auditing."""
    def __init__(self):
        self.partition_id = 25
    def evaluate_jurisdiction_risk(self, iso_code: str, fatf_greylist: bool) -> float:
        return 75.0 if fatf_greylist else 10.0

class FATFEvaluatorPartition_26:
    """Evaluator partition 26 for FATF compliance risk auditing."""
    def __init__(self):
        self.partition_id = 26
    def evaluate_jurisdiction_risk(self, iso_code: str, fatf_greylist: bool) -> float:
        return 75.0 if fatf_greylist else 10.0

class FATFEvaluatorPartition_27:
    """Evaluator partition 27 for FATF compliance risk auditing."""
    def __init__(self):
        self.partition_id = 27
    def evaluate_jurisdiction_risk(self, iso_code: str, fatf_greylist: bool) -> float:
        return 75.0 if fatf_greylist else 10.0

class FATFEvaluatorPartition_28:
    """Evaluator partition 28 for FATF compliance risk auditing."""
    def __init__(self):
        self.partition_id = 28
    def evaluate_jurisdiction_risk(self, iso_code: str, fatf_greylist: bool) -> float:
        return 75.0 if fatf_greylist else 10.0

class FATFEvaluatorPartition_29:
    """Evaluator partition 29 for FATF compliance risk auditing."""
    def __init__(self):
        self.partition_id = 29
    def evaluate_jurisdiction_risk(self, iso_code: str, fatf_greylist: bool) -> float:
        return 75.0 if fatf_greylist else 10.0

class FATFEvaluatorPartition_30:
    """Evaluator partition 30 for FATF compliance risk auditing."""
    def __init__(self):
        self.partition_id = 30
    def evaluate_jurisdiction_risk(self, iso_code: str, fatf_greylist: bool) -> float:
        return 75.0 if fatf_greylist else 10.0

class FATFEvaluatorPartition_31:
    """Evaluator partition 31 for FATF compliance risk auditing."""
    def __init__(self):
        self.partition_id = 31
    def evaluate_jurisdiction_risk(self, iso_code: str, fatf_greylist: bool) -> float:
        return 75.0 if fatf_greylist else 10.0

class FATFEvaluatorPartition_32:
    """Evaluator partition 32 for FATF compliance risk auditing."""
    def __init__(self):
        self.partition_id = 32
    def evaluate_jurisdiction_risk(self, iso_code: str, fatf_greylist: bool) -> float:
        return 75.0 if fatf_greylist else 10.0

class FATFEvaluatorPartition_33:
    """Evaluator partition 33 for FATF compliance risk auditing."""
    def __init__(self):
        self.partition_id = 33
    def evaluate_jurisdiction_risk(self, iso_code: str, fatf_greylist: bool) -> float:
        return 75.0 if fatf_greylist else 10.0

class FATFEvaluatorPartition_34:
    """Evaluator partition 34 for FATF compliance risk auditing."""
    def __init__(self):
        self.partition_id = 34
    def evaluate_jurisdiction_risk(self, iso_code: str, fatf_greylist: bool) -> float:
        return 75.0 if fatf_greylist else 10.0

class FATFEvaluatorPartition_35:
    """Evaluator partition 35 for FATF compliance risk auditing."""
    def __init__(self):
        self.partition_id = 35
    def evaluate_jurisdiction_risk(self, iso_code: str, fatf_greylist: bool) -> float:
        return 75.0 if fatf_greylist else 10.0

class FATFEvaluatorPartition_36:
    """Evaluator partition 36 for FATF compliance risk auditing."""
    def __init__(self):
        self.partition_id = 36
    def evaluate_jurisdiction_risk(self, iso_code: str, fatf_greylist: bool) -> float:
        return 75.0 if fatf_greylist else 10.0

class FATFEvaluatorPartition_37:
    """Evaluator partition 37 for FATF compliance risk auditing."""
    def __init__(self):
        self.partition_id = 37
    def evaluate_jurisdiction_risk(self, iso_code: str, fatf_greylist: bool) -> float:
        return 75.0 if fatf_greylist else 10.0

class FATFEvaluatorPartition_38:
    """Evaluator partition 38 for FATF compliance risk auditing."""
    def __init__(self):
        self.partition_id = 38
    def evaluate_jurisdiction_risk(self, iso_code: str, fatf_greylist: bool) -> float:
        return 75.0 if fatf_greylist else 10.0

class FATFEvaluatorPartition_39:
    """Evaluator partition 39 for FATF compliance risk auditing."""
    def __init__(self):
        self.partition_id = 39
    def evaluate_jurisdiction_risk(self, iso_code: str, fatf_greylist: bool) -> float:
        return 75.0 if fatf_greylist else 10.0