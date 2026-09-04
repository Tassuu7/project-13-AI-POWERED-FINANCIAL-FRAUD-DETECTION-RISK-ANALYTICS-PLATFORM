"""
Aegis Fraud Labs – Advanced Fraud Heuristics & Behavioral Scenarios Engine
Defines 250 enterprise heuristics spanning CNP fraud, wire structuring, ATO velocity, and crypto mixers.
"""
from typing import Dict, List, Any, Optional
from dataclasses import dataclass

@dataclass
class FraudHeuristicScenario:
    scenario_id: str
    name: str
    domain: str
    severity: str
    threshold_score: float
    trigger_condition: str
    sar_code: str
    recommended_action: str
    description: str

class FraudHeuristicsCatalog:
    def __init__(self):
        self.scenarios: Dict[str, FraudHeuristicScenario] = {}
        self._init_scenarios()

    def register(self, s: FraudHeuristicScenario):
        self.scenarios[s.scenario_id] = s

    def _init_scenarios(self):
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0001",
            name="Heuristic Scenario 1 - Wire Structuring",
            domain="WIRE_STRUCTURING",
            severity="HIGH",
            threshold_score=46.1,
            trigger_condition="velocity_1h > 2 and amount > 150.00",
            sar_code="SAR_TYPOLOGY_001",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 1 under WIRE_STRUCTURING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0002",
            name="Heuristic Scenario 2 - Account Takeover",
            domain="ACCOUNT_TAKEOVER",
            severity="MEDIUM",
            threshold_score=47.2,
            trigger_condition="velocity_1h > 3 and amount > 300.00",
            sar_code="SAR_TYPOLOGY_002",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 2 under ACCOUNT_TAKEOVER telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0003",
            name="Heuristic Scenario 3 - Merchant Bustout",
            domain="MERCHANT_BUSTOUT",
            severity="LOW",
            threshold_score=48.3,
            trigger_condition="velocity_1h > 4 and amount > 450.00",
            sar_code="SAR_TYPOLOGY_003",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 3 under MERCHANT_BUSTOUT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0004",
            name="Heuristic Scenario 4 - Crypto Tumbling",
            domain="CRYPTO_TUMBLING",
            severity="CRITICAL",
            threshold_score=49.4,
            trigger_condition="velocity_1h > 5 and amount > 600.00",
            sar_code="SAR_TYPOLOGY_004",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 4 under CRYPTO_TUMBLING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0005",
            name="Heuristic Scenario 5 - P2P Rapid Velocity",
            domain="P2P_RAPID_VELOCITY",
            severity="HIGH",
            threshold_score=50.5,
            trigger_condition="velocity_1h > 6 and amount > 750.00",
            sar_code="SAR_TYPOLOGY_005",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 5 under P2P_RAPID_VELOCITY telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0006",
            name="Heuristic Scenario 6 - Card Not Present",
            domain="CARD_NOT_PRESENT",
            severity="MEDIUM",
            threshold_score=51.6,
            trigger_condition="velocity_1h > 7 and amount > 900.00",
            sar_code="SAR_TYPOLOGY_006",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 6 under CARD_NOT_PRESENT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0007",
            name="Heuristic Scenario 7 - Wire Structuring",
            domain="WIRE_STRUCTURING",
            severity="LOW",
            threshold_score=52.7,
            trigger_condition="velocity_1h > 8 and amount > 1050.00",
            sar_code="SAR_TYPOLOGY_007",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 7 under WIRE_STRUCTURING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0008",
            name="Heuristic Scenario 8 - Account Takeover",
            domain="ACCOUNT_TAKEOVER",
            severity="CRITICAL",
            threshold_score=53.8,
            trigger_condition="velocity_1h > 9 and amount > 1200.00",
            sar_code="SAR_TYPOLOGY_008",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 8 under ACCOUNT_TAKEOVER telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0009",
            name="Heuristic Scenario 9 - Merchant Bustout",
            domain="MERCHANT_BUSTOUT",
            severity="HIGH",
            threshold_score=54.9,
            trigger_condition="velocity_1h > 10 and amount > 1350.00",
            sar_code="SAR_TYPOLOGY_009",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 9 under MERCHANT_BUSTOUT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0010",
            name="Heuristic Scenario 10 - Crypto Tumbling",
            domain="CRYPTO_TUMBLING",
            severity="MEDIUM",
            threshold_score=56.0,
            trigger_condition="velocity_1h > 1 and amount > 1500.00",
            sar_code="SAR_TYPOLOGY_010",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 10 under CRYPTO_TUMBLING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0011",
            name="Heuristic Scenario 11 - P2P Rapid Velocity",
            domain="P2P_RAPID_VELOCITY",
            severity="LOW",
            threshold_score=57.1,
            trigger_condition="velocity_1h > 2 and amount > 1650.00",
            sar_code="SAR_TYPOLOGY_011",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 11 under P2P_RAPID_VELOCITY telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0012",
            name="Heuristic Scenario 12 - Card Not Present",
            domain="CARD_NOT_PRESENT",
            severity="CRITICAL",
            threshold_score=58.2,
            trigger_condition="velocity_1h > 3 and amount > 1800.00",
            sar_code="SAR_TYPOLOGY_012",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 12 under CARD_NOT_PRESENT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0013",
            name="Heuristic Scenario 13 - Wire Structuring",
            domain="WIRE_STRUCTURING",
            severity="HIGH",
            threshold_score=59.3,
            trigger_condition="velocity_1h > 4 and amount > 1950.00",
            sar_code="SAR_TYPOLOGY_013",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 13 under WIRE_STRUCTURING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0014",
            name="Heuristic Scenario 14 - Account Takeover",
            domain="ACCOUNT_TAKEOVER",
            severity="MEDIUM",
            threshold_score=60.4,
            trigger_condition="velocity_1h > 5 and amount > 2100.00",
            sar_code="SAR_TYPOLOGY_014",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 14 under ACCOUNT_TAKEOVER telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0015",
            name="Heuristic Scenario 15 - Merchant Bustout",
            domain="MERCHANT_BUSTOUT",
            severity="LOW",
            threshold_score=61.5,
            trigger_condition="velocity_1h > 6 and amount > 2250.00",
            sar_code="SAR_TYPOLOGY_015",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 15 under MERCHANT_BUSTOUT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0016",
            name="Heuristic Scenario 16 - Crypto Tumbling",
            domain="CRYPTO_TUMBLING",
            severity="CRITICAL",
            threshold_score=62.6,
            trigger_condition="velocity_1h > 7 and amount > 2400.00",
            sar_code="SAR_TYPOLOGY_016",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 16 under CRYPTO_TUMBLING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0017",
            name="Heuristic Scenario 17 - P2P Rapid Velocity",
            domain="P2P_RAPID_VELOCITY",
            severity="HIGH",
            threshold_score=63.7,
            trigger_condition="velocity_1h > 8 and amount > 2550.00",
            sar_code="SAR_TYPOLOGY_017",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 17 under P2P_RAPID_VELOCITY telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0018",
            name="Heuristic Scenario 18 - Card Not Present",
            domain="CARD_NOT_PRESENT",
            severity="MEDIUM",
            threshold_score=64.8,
            trigger_condition="velocity_1h > 9 and amount > 2700.00",
            sar_code="SAR_TYPOLOGY_018",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 18 under CARD_NOT_PRESENT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0019",
            name="Heuristic Scenario 19 - Wire Structuring",
            domain="WIRE_STRUCTURING",
            severity="LOW",
            threshold_score=65.9,
            trigger_condition="velocity_1h > 10 and amount > 2850.00",
            sar_code="SAR_TYPOLOGY_019",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 19 under WIRE_STRUCTURING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0020",
            name="Heuristic Scenario 20 - Account Takeover",
            domain="ACCOUNT_TAKEOVER",
            severity="CRITICAL",
            threshold_score=67.0,
            trigger_condition="velocity_1h > 1 and amount > 3000.00",
            sar_code="SAR_TYPOLOGY_020",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 20 under ACCOUNT_TAKEOVER telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0021",
            name="Heuristic Scenario 21 - Merchant Bustout",
            domain="MERCHANT_BUSTOUT",
            severity="HIGH",
            threshold_score=68.1,
            trigger_condition="velocity_1h > 2 and amount > 3150.00",
            sar_code="SAR_TYPOLOGY_021",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 21 under MERCHANT_BUSTOUT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0022",
            name="Heuristic Scenario 22 - Crypto Tumbling",
            domain="CRYPTO_TUMBLING",
            severity="MEDIUM",
            threshold_score=69.2,
            trigger_condition="velocity_1h > 3 and amount > 3300.00",
            sar_code="SAR_TYPOLOGY_022",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 22 under CRYPTO_TUMBLING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0023",
            name="Heuristic Scenario 23 - P2P Rapid Velocity",
            domain="P2P_RAPID_VELOCITY",
            severity="LOW",
            threshold_score=70.3,
            trigger_condition="velocity_1h > 4 and amount > 3450.00",
            sar_code="SAR_TYPOLOGY_023",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 23 under P2P_RAPID_VELOCITY telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0024",
            name="Heuristic Scenario 24 - Card Not Present",
            domain="CARD_NOT_PRESENT",
            severity="CRITICAL",
            threshold_score=71.4,
            trigger_condition="velocity_1h > 5 and amount > 3600.00",
            sar_code="SAR_TYPOLOGY_024",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 24 under CARD_NOT_PRESENT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0025",
            name="Heuristic Scenario 25 - Wire Structuring",
            domain="WIRE_STRUCTURING",
            severity="HIGH",
            threshold_score=72.5,
            trigger_condition="velocity_1h > 6 and amount > 3750.00",
            sar_code="SAR_TYPOLOGY_025",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 25 under WIRE_STRUCTURING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0026",
            name="Heuristic Scenario 26 - Account Takeover",
            domain="ACCOUNT_TAKEOVER",
            severity="MEDIUM",
            threshold_score=73.6,
            trigger_condition="velocity_1h > 7 and amount > 3900.00",
            sar_code="SAR_TYPOLOGY_026",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 26 under ACCOUNT_TAKEOVER telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0027",
            name="Heuristic Scenario 27 - Merchant Bustout",
            domain="MERCHANT_BUSTOUT",
            severity="LOW",
            threshold_score=74.7,
            trigger_condition="velocity_1h > 8 and amount > 4050.00",
            sar_code="SAR_TYPOLOGY_027",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 27 under MERCHANT_BUSTOUT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0028",
            name="Heuristic Scenario 28 - Crypto Tumbling",
            domain="CRYPTO_TUMBLING",
            severity="CRITICAL",
            threshold_score=75.8,
            trigger_condition="velocity_1h > 9 and amount > 4200.00",
            sar_code="SAR_TYPOLOGY_028",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 28 under CRYPTO_TUMBLING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0029",
            name="Heuristic Scenario 29 - P2P Rapid Velocity",
            domain="P2P_RAPID_VELOCITY",
            severity="HIGH",
            threshold_score=76.9,
            trigger_condition="velocity_1h > 10 and amount > 4350.00",
            sar_code="SAR_TYPOLOGY_029",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 29 under P2P_RAPID_VELOCITY telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0030",
            name="Heuristic Scenario 30 - Card Not Present",
            domain="CARD_NOT_PRESENT",
            severity="MEDIUM",
            threshold_score=78.0,
            trigger_condition="velocity_1h > 1 and amount > 4500.00",
            sar_code="SAR_TYPOLOGY_030",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 30 under CARD_NOT_PRESENT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0031",
            name="Heuristic Scenario 31 - Wire Structuring",
            domain="WIRE_STRUCTURING",
            severity="LOW",
            threshold_score=79.1,
            trigger_condition="velocity_1h > 2 and amount > 4650.00",
            sar_code="SAR_TYPOLOGY_031",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 31 under WIRE_STRUCTURING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0032",
            name="Heuristic Scenario 32 - Account Takeover",
            domain="ACCOUNT_TAKEOVER",
            severity="CRITICAL",
            threshold_score=80.2,
            trigger_condition="velocity_1h > 3 and amount > 4800.00",
            sar_code="SAR_TYPOLOGY_032",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 32 under ACCOUNT_TAKEOVER telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0033",
            name="Heuristic Scenario 33 - Merchant Bustout",
            domain="MERCHANT_BUSTOUT",
            severity="HIGH",
            threshold_score=81.3,
            trigger_condition="velocity_1h > 4 and amount > 4950.00",
            sar_code="SAR_TYPOLOGY_033",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 33 under MERCHANT_BUSTOUT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0034",
            name="Heuristic Scenario 34 - Crypto Tumbling",
            domain="CRYPTO_TUMBLING",
            severity="MEDIUM",
            threshold_score=82.4,
            trigger_condition="velocity_1h > 5 and amount > 5100.00",
            sar_code="SAR_TYPOLOGY_034",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 34 under CRYPTO_TUMBLING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0035",
            name="Heuristic Scenario 35 - P2P Rapid Velocity",
            domain="P2P_RAPID_VELOCITY",
            severity="LOW",
            threshold_score=83.5,
            trigger_condition="velocity_1h > 6 and amount > 5250.00",
            sar_code="SAR_TYPOLOGY_035",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 35 under P2P_RAPID_VELOCITY telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0036",
            name="Heuristic Scenario 36 - Card Not Present",
            domain="CARD_NOT_PRESENT",
            severity="CRITICAL",
            threshold_score=84.6,
            trigger_condition="velocity_1h > 7 and amount > 5400.00",
            sar_code="SAR_TYPOLOGY_036",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 36 under CARD_NOT_PRESENT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0037",
            name="Heuristic Scenario 37 - Wire Structuring",
            domain="WIRE_STRUCTURING",
            severity="HIGH",
            threshold_score=85.7,
            trigger_condition="velocity_1h > 8 and amount > 5550.00",
            sar_code="SAR_TYPOLOGY_037",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 37 under WIRE_STRUCTURING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0038",
            name="Heuristic Scenario 38 - Account Takeover",
            domain="ACCOUNT_TAKEOVER",
            severity="MEDIUM",
            threshold_score=86.8,
            trigger_condition="velocity_1h > 9 and amount > 5700.00",
            sar_code="SAR_TYPOLOGY_038",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 38 under ACCOUNT_TAKEOVER telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0039",
            name="Heuristic Scenario 39 - Merchant Bustout",
            domain="MERCHANT_BUSTOUT",
            severity="LOW",
            threshold_score=87.9,
            trigger_condition="velocity_1h > 10 and amount > 5850.00",
            sar_code="SAR_TYPOLOGY_039",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 39 under MERCHANT_BUSTOUT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0040",
            name="Heuristic Scenario 40 - Crypto Tumbling",
            domain="CRYPTO_TUMBLING",
            severity="CRITICAL",
            threshold_score=89.0,
            trigger_condition="velocity_1h > 1 and amount > 6000.00",
            sar_code="SAR_TYPOLOGY_040",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 40 under CRYPTO_TUMBLING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0041",
            name="Heuristic Scenario 41 - P2P Rapid Velocity",
            domain="P2P_RAPID_VELOCITY",
            severity="HIGH",
            threshold_score=90.1,
            trigger_condition="velocity_1h > 2 and amount > 6150.00",
            sar_code="SAR_TYPOLOGY_041",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 41 under P2P_RAPID_VELOCITY telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0042",
            name="Heuristic Scenario 42 - Card Not Present",
            domain="CARD_NOT_PRESENT",
            severity="MEDIUM",
            threshold_score=91.2,
            trigger_condition="velocity_1h > 3 and amount > 6300.00",
            sar_code="SAR_TYPOLOGY_042",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 42 under CARD_NOT_PRESENT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0043",
            name="Heuristic Scenario 43 - Wire Structuring",
            domain="WIRE_STRUCTURING",
            severity="LOW",
            threshold_score=92.3,
            trigger_condition="velocity_1h > 4 and amount > 6450.00",
            sar_code="SAR_TYPOLOGY_043",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 43 under WIRE_STRUCTURING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0044",
            name="Heuristic Scenario 44 - Account Takeover",
            domain="ACCOUNT_TAKEOVER",
            severity="CRITICAL",
            threshold_score=93.4,
            trigger_condition="velocity_1h > 5 and amount > 6600.00",
            sar_code="SAR_TYPOLOGY_044",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 44 under ACCOUNT_TAKEOVER telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0045",
            name="Heuristic Scenario 45 - Merchant Bustout",
            domain="MERCHANT_BUSTOUT",
            severity="HIGH",
            threshold_score=94.5,
            trigger_condition="velocity_1h > 6 and amount > 6750.00",
            sar_code="SAR_TYPOLOGY_045",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 45 under MERCHANT_BUSTOUT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0046",
            name="Heuristic Scenario 46 - Crypto Tumbling",
            domain="CRYPTO_TUMBLING",
            severity="MEDIUM",
            threshold_score=95.6,
            trigger_condition="velocity_1h > 7 and amount > 6900.00",
            sar_code="SAR_TYPOLOGY_046",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 46 under CRYPTO_TUMBLING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0047",
            name="Heuristic Scenario 47 - P2P Rapid Velocity",
            domain="P2P_RAPID_VELOCITY",
            severity="LOW",
            threshold_score=96.7,
            trigger_condition="velocity_1h > 8 and amount > 7050.00",
            sar_code="SAR_TYPOLOGY_047",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 47 under P2P_RAPID_VELOCITY telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0048",
            name="Heuristic Scenario 48 - Card Not Present",
            domain="CARD_NOT_PRESENT",
            severity="CRITICAL",
            threshold_score=97.8,
            trigger_condition="velocity_1h > 9 and amount > 7200.00",
            sar_code="SAR_TYPOLOGY_048",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 48 under CARD_NOT_PRESENT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0049",
            name="Heuristic Scenario 49 - Wire Structuring",
            domain="WIRE_STRUCTURING",
            severity="HIGH",
            threshold_score=98.9,
            trigger_condition="velocity_1h > 10 and amount > 7350.00",
            sar_code="SAR_TYPOLOGY_049",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 49 under WIRE_STRUCTURING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0050",
            name="Heuristic Scenario 50 - Account Takeover",
            domain="ACCOUNT_TAKEOVER",
            severity="MEDIUM",
            threshold_score=45.0,
            trigger_condition="velocity_1h > 1 and amount > 7500.00",
            sar_code="SAR_TYPOLOGY_050",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 50 under ACCOUNT_TAKEOVER telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0051",
            name="Heuristic Scenario 51 - Merchant Bustout",
            domain="MERCHANT_BUSTOUT",
            severity="LOW",
            threshold_score=46.1,
            trigger_condition="velocity_1h > 2 and amount > 7650.00",
            sar_code="SAR_TYPOLOGY_051",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 51 under MERCHANT_BUSTOUT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0052",
            name="Heuristic Scenario 52 - Crypto Tumbling",
            domain="CRYPTO_TUMBLING",
            severity="CRITICAL",
            threshold_score=47.2,
            trigger_condition="velocity_1h > 3 and amount > 7800.00",
            sar_code="SAR_TYPOLOGY_052",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 52 under CRYPTO_TUMBLING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0053",
            name="Heuristic Scenario 53 - P2P Rapid Velocity",
            domain="P2P_RAPID_VELOCITY",
            severity="HIGH",
            threshold_score=48.3,
            trigger_condition="velocity_1h > 4 and amount > 7950.00",
            sar_code="SAR_TYPOLOGY_053",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 53 under P2P_RAPID_VELOCITY telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0054",
            name="Heuristic Scenario 54 - Card Not Present",
            domain="CARD_NOT_PRESENT",
            severity="MEDIUM",
            threshold_score=49.4,
            trigger_condition="velocity_1h > 5 and amount > 8100.00",
            sar_code="SAR_TYPOLOGY_054",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 54 under CARD_NOT_PRESENT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0055",
            name="Heuristic Scenario 55 - Wire Structuring",
            domain="WIRE_STRUCTURING",
            severity="LOW",
            threshold_score=50.5,
            trigger_condition="velocity_1h > 6 and amount > 8250.00",
            sar_code="SAR_TYPOLOGY_055",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 55 under WIRE_STRUCTURING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0056",
            name="Heuristic Scenario 56 - Account Takeover",
            domain="ACCOUNT_TAKEOVER",
            severity="CRITICAL",
            threshold_score=51.6,
            trigger_condition="velocity_1h > 7 and amount > 8400.00",
            sar_code="SAR_TYPOLOGY_056",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 56 under ACCOUNT_TAKEOVER telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0057",
            name="Heuristic Scenario 57 - Merchant Bustout",
            domain="MERCHANT_BUSTOUT",
            severity="HIGH",
            threshold_score=52.7,
            trigger_condition="velocity_1h > 8 and amount > 8550.00",
            sar_code="SAR_TYPOLOGY_057",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 57 under MERCHANT_BUSTOUT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0058",
            name="Heuristic Scenario 58 - Crypto Tumbling",
            domain="CRYPTO_TUMBLING",
            severity="MEDIUM",
            threshold_score=53.8,
            trigger_condition="velocity_1h > 9 and amount > 8700.00",
            sar_code="SAR_TYPOLOGY_058",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 58 under CRYPTO_TUMBLING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0059",
            name="Heuristic Scenario 59 - P2P Rapid Velocity",
            domain="P2P_RAPID_VELOCITY",
            severity="LOW",
            threshold_score=54.9,
            trigger_condition="velocity_1h > 10 and amount > 8850.00",
            sar_code="SAR_TYPOLOGY_059",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 59 under P2P_RAPID_VELOCITY telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0060",
            name="Heuristic Scenario 60 - Card Not Present",
            domain="CARD_NOT_PRESENT",
            severity="CRITICAL",
            threshold_score=56.0,
            trigger_condition="velocity_1h > 1 and amount > 9000.00",
            sar_code="SAR_TYPOLOGY_060",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 60 under CARD_NOT_PRESENT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0061",
            name="Heuristic Scenario 61 - Wire Structuring",
            domain="WIRE_STRUCTURING",
            severity="HIGH",
            threshold_score=57.1,
            trigger_condition="velocity_1h > 2 and amount > 9150.00",
            sar_code="SAR_TYPOLOGY_061",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 61 under WIRE_STRUCTURING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0062",
            name="Heuristic Scenario 62 - Account Takeover",
            domain="ACCOUNT_TAKEOVER",
            severity="MEDIUM",
            threshold_score=58.2,
            trigger_condition="velocity_1h > 3 and amount > 9300.00",
            sar_code="SAR_TYPOLOGY_062",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 62 under ACCOUNT_TAKEOVER telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0063",
            name="Heuristic Scenario 63 - Merchant Bustout",
            domain="MERCHANT_BUSTOUT",
            severity="LOW",
            threshold_score=59.3,
            trigger_condition="velocity_1h > 4 and amount > 9450.00",
            sar_code="SAR_TYPOLOGY_063",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 63 under MERCHANT_BUSTOUT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0064",
            name="Heuristic Scenario 64 - Crypto Tumbling",
            domain="CRYPTO_TUMBLING",
            severity="CRITICAL",
            threshold_score=60.4,
            trigger_condition="velocity_1h > 5 and amount > 9600.00",
            sar_code="SAR_TYPOLOGY_064",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 64 under CRYPTO_TUMBLING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0065",
            name="Heuristic Scenario 65 - P2P Rapid Velocity",
            domain="P2P_RAPID_VELOCITY",
            severity="HIGH",
            threshold_score=61.5,
            trigger_condition="velocity_1h > 6 and amount > 9750.00",
            sar_code="SAR_TYPOLOGY_065",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 65 under P2P_RAPID_VELOCITY telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0066",
            name="Heuristic Scenario 66 - Card Not Present",
            domain="CARD_NOT_PRESENT",
            severity="MEDIUM",
            threshold_score=62.6,
            trigger_condition="velocity_1h > 7 and amount > 9900.00",
            sar_code="SAR_TYPOLOGY_066",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 66 under CARD_NOT_PRESENT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0067",
            name="Heuristic Scenario 67 - Wire Structuring",
            domain="WIRE_STRUCTURING",
            severity="LOW",
            threshold_score=63.7,
            trigger_condition="velocity_1h > 8 and amount > 10050.00",
            sar_code="SAR_TYPOLOGY_067",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 67 under WIRE_STRUCTURING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0068",
            name="Heuristic Scenario 68 - Account Takeover",
            domain="ACCOUNT_TAKEOVER",
            severity="CRITICAL",
            threshold_score=64.8,
            trigger_condition="velocity_1h > 9 and amount > 10200.00",
            sar_code="SAR_TYPOLOGY_068",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 68 under ACCOUNT_TAKEOVER telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0069",
            name="Heuristic Scenario 69 - Merchant Bustout",
            domain="MERCHANT_BUSTOUT",
            severity="HIGH",
            threshold_score=65.9,
            trigger_condition="velocity_1h > 10 and amount > 10350.00",
            sar_code="SAR_TYPOLOGY_069",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 69 under MERCHANT_BUSTOUT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0070",
            name="Heuristic Scenario 70 - Crypto Tumbling",
            domain="CRYPTO_TUMBLING",
            severity="MEDIUM",
            threshold_score=67.0,
            trigger_condition="velocity_1h > 1 and amount > 10500.00",
            sar_code="SAR_TYPOLOGY_070",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 70 under CRYPTO_TUMBLING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0071",
            name="Heuristic Scenario 71 - P2P Rapid Velocity",
            domain="P2P_RAPID_VELOCITY",
            severity="LOW",
            threshold_score=68.1,
            trigger_condition="velocity_1h > 2 and amount > 10650.00",
            sar_code="SAR_TYPOLOGY_071",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 71 under P2P_RAPID_VELOCITY telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0072",
            name="Heuristic Scenario 72 - Card Not Present",
            domain="CARD_NOT_PRESENT",
            severity="CRITICAL",
            threshold_score=69.2,
            trigger_condition="velocity_1h > 3 and amount > 10800.00",
            sar_code="SAR_TYPOLOGY_072",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 72 under CARD_NOT_PRESENT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0073",
            name="Heuristic Scenario 73 - Wire Structuring",
            domain="WIRE_STRUCTURING",
            severity="HIGH",
            threshold_score=70.3,
            trigger_condition="velocity_1h > 4 and amount > 10950.00",
            sar_code="SAR_TYPOLOGY_073",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 73 under WIRE_STRUCTURING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0074",
            name="Heuristic Scenario 74 - Account Takeover",
            domain="ACCOUNT_TAKEOVER",
            severity="MEDIUM",
            threshold_score=71.4,
            trigger_condition="velocity_1h > 5 and amount > 11100.00",
            sar_code="SAR_TYPOLOGY_074",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 74 under ACCOUNT_TAKEOVER telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0075",
            name="Heuristic Scenario 75 - Merchant Bustout",
            domain="MERCHANT_BUSTOUT",
            severity="LOW",
            threshold_score=72.5,
            trigger_condition="velocity_1h > 6 and amount > 11250.00",
            sar_code="SAR_TYPOLOGY_075",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 75 under MERCHANT_BUSTOUT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0076",
            name="Heuristic Scenario 76 - Crypto Tumbling",
            domain="CRYPTO_TUMBLING",
            severity="CRITICAL",
            threshold_score=73.6,
            trigger_condition="velocity_1h > 7 and amount > 11400.00",
            sar_code="SAR_TYPOLOGY_076",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 76 under CRYPTO_TUMBLING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0077",
            name="Heuristic Scenario 77 - P2P Rapid Velocity",
            domain="P2P_RAPID_VELOCITY",
            severity="HIGH",
            threshold_score=74.7,
            trigger_condition="velocity_1h > 8 and amount > 11550.00",
            sar_code="SAR_TYPOLOGY_077",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 77 under P2P_RAPID_VELOCITY telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0078",
            name="Heuristic Scenario 78 - Card Not Present",
            domain="CARD_NOT_PRESENT",
            severity="MEDIUM",
            threshold_score=75.8,
            trigger_condition="velocity_1h > 9 and amount > 11700.00",
            sar_code="SAR_TYPOLOGY_078",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 78 under CARD_NOT_PRESENT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0079",
            name="Heuristic Scenario 79 - Wire Structuring",
            domain="WIRE_STRUCTURING",
            severity="LOW",
            threshold_score=76.9,
            trigger_condition="velocity_1h > 10 and amount > 11850.00",
            sar_code="SAR_TYPOLOGY_079",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 79 under WIRE_STRUCTURING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0080",
            name="Heuristic Scenario 80 - Account Takeover",
            domain="ACCOUNT_TAKEOVER",
            severity="CRITICAL",
            threshold_score=78.0,
            trigger_condition="velocity_1h > 1 and amount > 12000.00",
            sar_code="SAR_TYPOLOGY_000",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 80 under ACCOUNT_TAKEOVER telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0081",
            name="Heuristic Scenario 81 - Merchant Bustout",
            domain="MERCHANT_BUSTOUT",
            severity="HIGH",
            threshold_score=79.1,
            trigger_condition="velocity_1h > 2 and amount > 12150.00",
            sar_code="SAR_TYPOLOGY_001",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 81 under MERCHANT_BUSTOUT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0082",
            name="Heuristic Scenario 82 - Crypto Tumbling",
            domain="CRYPTO_TUMBLING",
            severity="MEDIUM",
            threshold_score=80.2,
            trigger_condition="velocity_1h > 3 and amount > 12300.00",
            sar_code="SAR_TYPOLOGY_002",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 82 under CRYPTO_TUMBLING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0083",
            name="Heuristic Scenario 83 - P2P Rapid Velocity",
            domain="P2P_RAPID_VELOCITY",
            severity="LOW",
            threshold_score=81.3,
            trigger_condition="velocity_1h > 4 and amount > 12450.00",
            sar_code="SAR_TYPOLOGY_003",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 83 under P2P_RAPID_VELOCITY telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0084",
            name="Heuristic Scenario 84 - Card Not Present",
            domain="CARD_NOT_PRESENT",
            severity="CRITICAL",
            threshold_score=82.4,
            trigger_condition="velocity_1h > 5 and amount > 12600.00",
            sar_code="SAR_TYPOLOGY_004",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 84 under CARD_NOT_PRESENT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0085",
            name="Heuristic Scenario 85 - Wire Structuring",
            domain="WIRE_STRUCTURING",
            severity="HIGH",
            threshold_score=83.5,
            trigger_condition="velocity_1h > 6 and amount > 12750.00",
            sar_code="SAR_TYPOLOGY_005",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 85 under WIRE_STRUCTURING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0086",
            name="Heuristic Scenario 86 - Account Takeover",
            domain="ACCOUNT_TAKEOVER",
            severity="MEDIUM",
            threshold_score=84.6,
            trigger_condition="velocity_1h > 7 and amount > 12900.00",
            sar_code="SAR_TYPOLOGY_006",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 86 under ACCOUNT_TAKEOVER telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0087",
            name="Heuristic Scenario 87 - Merchant Bustout",
            domain="MERCHANT_BUSTOUT",
            severity="LOW",
            threshold_score=85.7,
            trigger_condition="velocity_1h > 8 and amount > 13050.00",
            sar_code="SAR_TYPOLOGY_007",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 87 under MERCHANT_BUSTOUT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0088",
            name="Heuristic Scenario 88 - Crypto Tumbling",
            domain="CRYPTO_TUMBLING",
            severity="CRITICAL",
            threshold_score=86.8,
            trigger_condition="velocity_1h > 9 and amount > 13200.00",
            sar_code="SAR_TYPOLOGY_008",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 88 under CRYPTO_TUMBLING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0089",
            name="Heuristic Scenario 89 - P2P Rapid Velocity",
            domain="P2P_RAPID_VELOCITY",
            severity="HIGH",
            threshold_score=87.9,
            trigger_condition="velocity_1h > 10 and amount > 13350.00",
            sar_code="SAR_TYPOLOGY_009",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 89 under P2P_RAPID_VELOCITY telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0090",
            name="Heuristic Scenario 90 - Card Not Present",
            domain="CARD_NOT_PRESENT",
            severity="MEDIUM",
            threshold_score=89.0,
            trigger_condition="velocity_1h > 1 and amount > 13500.00",
            sar_code="SAR_TYPOLOGY_010",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 90 under CARD_NOT_PRESENT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0091",
            name="Heuristic Scenario 91 - Wire Structuring",
            domain="WIRE_STRUCTURING",
            severity="LOW",
            threshold_score=90.1,
            trigger_condition="velocity_1h > 2 and amount > 13650.00",
            sar_code="SAR_TYPOLOGY_011",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 91 under WIRE_STRUCTURING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0092",
            name="Heuristic Scenario 92 - Account Takeover",
            domain="ACCOUNT_TAKEOVER",
            severity="CRITICAL",
            threshold_score=91.2,
            trigger_condition="velocity_1h > 3 and amount > 13800.00",
            sar_code="SAR_TYPOLOGY_012",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 92 under ACCOUNT_TAKEOVER telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0093",
            name="Heuristic Scenario 93 - Merchant Bustout",
            domain="MERCHANT_BUSTOUT",
            severity="HIGH",
            threshold_score=92.3,
            trigger_condition="velocity_1h > 4 and amount > 13950.00",
            sar_code="SAR_TYPOLOGY_013",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 93 under MERCHANT_BUSTOUT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0094",
            name="Heuristic Scenario 94 - Crypto Tumbling",
            domain="CRYPTO_TUMBLING",
            severity="MEDIUM",
            threshold_score=93.4,
            trigger_condition="velocity_1h > 5 and amount > 14100.00",
            sar_code="SAR_TYPOLOGY_014",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 94 under CRYPTO_TUMBLING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0095",
            name="Heuristic Scenario 95 - P2P Rapid Velocity",
            domain="P2P_RAPID_VELOCITY",
            severity="LOW",
            threshold_score=94.5,
            trigger_condition="velocity_1h > 6 and amount > 14250.00",
            sar_code="SAR_TYPOLOGY_015",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 95 under P2P_RAPID_VELOCITY telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0096",
            name="Heuristic Scenario 96 - Card Not Present",
            domain="CARD_NOT_PRESENT",
            severity="CRITICAL",
            threshold_score=95.6,
            trigger_condition="velocity_1h > 7 and amount > 14400.00",
            sar_code="SAR_TYPOLOGY_016",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 96 under CARD_NOT_PRESENT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0097",
            name="Heuristic Scenario 97 - Wire Structuring",
            domain="WIRE_STRUCTURING",
            severity="HIGH",
            threshold_score=96.7,
            trigger_condition="velocity_1h > 8 and amount > 14550.00",
            sar_code="SAR_TYPOLOGY_017",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 97 under WIRE_STRUCTURING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0098",
            name="Heuristic Scenario 98 - Account Takeover",
            domain="ACCOUNT_TAKEOVER",
            severity="MEDIUM",
            threshold_score=97.8,
            trigger_condition="velocity_1h > 9 and amount > 14700.00",
            sar_code="SAR_TYPOLOGY_018",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 98 under ACCOUNT_TAKEOVER telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0099",
            name="Heuristic Scenario 99 - Merchant Bustout",
            domain="MERCHANT_BUSTOUT",
            severity="LOW",
            threshold_score=98.9,
            trigger_condition="velocity_1h > 10 and amount > 14850.00",
            sar_code="SAR_TYPOLOGY_019",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 99 under MERCHANT_BUSTOUT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0100",
            name="Heuristic Scenario 100 - Crypto Tumbling",
            domain="CRYPTO_TUMBLING",
            severity="CRITICAL",
            threshold_score=45.0,
            trigger_condition="velocity_1h > 1 and amount > 15000.00",
            sar_code="SAR_TYPOLOGY_020",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 100 under CRYPTO_TUMBLING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0101",
            name="Heuristic Scenario 101 - P2P Rapid Velocity",
            domain="P2P_RAPID_VELOCITY",
            severity="HIGH",
            threshold_score=46.1,
            trigger_condition="velocity_1h > 2 and amount > 15150.00",
            sar_code="SAR_TYPOLOGY_021",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 101 under P2P_RAPID_VELOCITY telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0102",
            name="Heuristic Scenario 102 - Card Not Present",
            domain="CARD_NOT_PRESENT",
            severity="MEDIUM",
            threshold_score=47.2,
            trigger_condition="velocity_1h > 3 and amount > 15300.00",
            sar_code="SAR_TYPOLOGY_022",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 102 under CARD_NOT_PRESENT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0103",
            name="Heuristic Scenario 103 - Wire Structuring",
            domain="WIRE_STRUCTURING",
            severity="LOW",
            threshold_score=48.3,
            trigger_condition="velocity_1h > 4 and amount > 15450.00",
            sar_code="SAR_TYPOLOGY_023",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 103 under WIRE_STRUCTURING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0104",
            name="Heuristic Scenario 104 - Account Takeover",
            domain="ACCOUNT_TAKEOVER",
            severity="CRITICAL",
            threshold_score=49.4,
            trigger_condition="velocity_1h > 5 and amount > 15600.00",
            sar_code="SAR_TYPOLOGY_024",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 104 under ACCOUNT_TAKEOVER telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0105",
            name="Heuristic Scenario 105 - Merchant Bustout",
            domain="MERCHANT_BUSTOUT",
            severity="HIGH",
            threshold_score=50.5,
            trigger_condition="velocity_1h > 6 and amount > 15750.00",
            sar_code="SAR_TYPOLOGY_025",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 105 under MERCHANT_BUSTOUT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0106",
            name="Heuristic Scenario 106 - Crypto Tumbling",
            domain="CRYPTO_TUMBLING",
            severity="MEDIUM",
            threshold_score=51.6,
            trigger_condition="velocity_1h > 7 and amount > 15900.00",
            sar_code="SAR_TYPOLOGY_026",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 106 under CRYPTO_TUMBLING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0107",
            name="Heuristic Scenario 107 - P2P Rapid Velocity",
            domain="P2P_RAPID_VELOCITY",
            severity="LOW",
            threshold_score=52.7,
            trigger_condition="velocity_1h > 8 and amount > 16050.00",
            sar_code="SAR_TYPOLOGY_027",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 107 under P2P_RAPID_VELOCITY telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0108",
            name="Heuristic Scenario 108 - Card Not Present",
            domain="CARD_NOT_PRESENT",
            severity="CRITICAL",
            threshold_score=53.8,
            trigger_condition="velocity_1h > 9 and amount > 16200.00",
            sar_code="SAR_TYPOLOGY_028",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 108 under CARD_NOT_PRESENT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0109",
            name="Heuristic Scenario 109 - Wire Structuring",
            domain="WIRE_STRUCTURING",
            severity="HIGH",
            threshold_score=54.9,
            trigger_condition="velocity_1h > 10 and amount > 16350.00",
            sar_code="SAR_TYPOLOGY_029",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 109 under WIRE_STRUCTURING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0110",
            name="Heuristic Scenario 110 - Account Takeover",
            domain="ACCOUNT_TAKEOVER",
            severity="MEDIUM",
            threshold_score=56.0,
            trigger_condition="velocity_1h > 1 and amount > 16500.00",
            sar_code="SAR_TYPOLOGY_030",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 110 under ACCOUNT_TAKEOVER telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0111",
            name="Heuristic Scenario 111 - Merchant Bustout",
            domain="MERCHANT_BUSTOUT",
            severity="LOW",
            threshold_score=57.1,
            trigger_condition="velocity_1h > 2 and amount > 16650.00",
            sar_code="SAR_TYPOLOGY_031",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 111 under MERCHANT_BUSTOUT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0112",
            name="Heuristic Scenario 112 - Crypto Tumbling",
            domain="CRYPTO_TUMBLING",
            severity="CRITICAL",
            threshold_score=58.2,
            trigger_condition="velocity_1h > 3 and amount > 16800.00",
            sar_code="SAR_TYPOLOGY_032",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 112 under CRYPTO_TUMBLING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0113",
            name="Heuristic Scenario 113 - P2P Rapid Velocity",
            domain="P2P_RAPID_VELOCITY",
            severity="HIGH",
            threshold_score=59.3,
            trigger_condition="velocity_1h > 4 and amount > 16950.00",
            sar_code="SAR_TYPOLOGY_033",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 113 under P2P_RAPID_VELOCITY telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0114",
            name="Heuristic Scenario 114 - Card Not Present",
            domain="CARD_NOT_PRESENT",
            severity="MEDIUM",
            threshold_score=60.4,
            trigger_condition="velocity_1h > 5 and amount > 17100.00",
            sar_code="SAR_TYPOLOGY_034",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 114 under CARD_NOT_PRESENT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0115",
            name="Heuristic Scenario 115 - Wire Structuring",
            domain="WIRE_STRUCTURING",
            severity="LOW",
            threshold_score=61.5,
            trigger_condition="velocity_1h > 6 and amount > 17250.00",
            sar_code="SAR_TYPOLOGY_035",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 115 under WIRE_STRUCTURING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0116",
            name="Heuristic Scenario 116 - Account Takeover",
            domain="ACCOUNT_TAKEOVER",
            severity="CRITICAL",
            threshold_score=62.6,
            trigger_condition="velocity_1h > 7 and amount > 17400.00",
            sar_code="SAR_TYPOLOGY_036",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 116 under ACCOUNT_TAKEOVER telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0117",
            name="Heuristic Scenario 117 - Merchant Bustout",
            domain="MERCHANT_BUSTOUT",
            severity="HIGH",
            threshold_score=63.7,
            trigger_condition="velocity_1h > 8 and amount > 17550.00",
            sar_code="SAR_TYPOLOGY_037",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 117 under MERCHANT_BUSTOUT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0118",
            name="Heuristic Scenario 118 - Crypto Tumbling",
            domain="CRYPTO_TUMBLING",
            severity="MEDIUM",
            threshold_score=64.8,
            trigger_condition="velocity_1h > 9 and amount > 17700.00",
            sar_code="SAR_TYPOLOGY_038",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 118 under CRYPTO_TUMBLING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0119",
            name="Heuristic Scenario 119 - P2P Rapid Velocity",
            domain="P2P_RAPID_VELOCITY",
            severity="LOW",
            threshold_score=65.9,
            trigger_condition="velocity_1h > 10 and amount > 17850.00",
            sar_code="SAR_TYPOLOGY_039",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 119 under P2P_RAPID_VELOCITY telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0120",
            name="Heuristic Scenario 120 - Card Not Present",
            domain="CARD_NOT_PRESENT",
            severity="CRITICAL",
            threshold_score=67.0,
            trigger_condition="velocity_1h > 1 and amount > 18000.00",
            sar_code="SAR_TYPOLOGY_040",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 120 under CARD_NOT_PRESENT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0121",
            name="Heuristic Scenario 121 - Wire Structuring",
            domain="WIRE_STRUCTURING",
            severity="HIGH",
            threshold_score=68.1,
            trigger_condition="velocity_1h > 2 and amount > 18150.00",
            sar_code="SAR_TYPOLOGY_041",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 121 under WIRE_STRUCTURING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0122",
            name="Heuristic Scenario 122 - Account Takeover",
            domain="ACCOUNT_TAKEOVER",
            severity="MEDIUM",
            threshold_score=69.2,
            trigger_condition="velocity_1h > 3 and amount > 18300.00",
            sar_code="SAR_TYPOLOGY_042",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 122 under ACCOUNT_TAKEOVER telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0123",
            name="Heuristic Scenario 123 - Merchant Bustout",
            domain="MERCHANT_BUSTOUT",
            severity="LOW",
            threshold_score=70.3,
            trigger_condition="velocity_1h > 4 and amount > 18450.00",
            sar_code="SAR_TYPOLOGY_043",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 123 under MERCHANT_BUSTOUT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0124",
            name="Heuristic Scenario 124 - Crypto Tumbling",
            domain="CRYPTO_TUMBLING",
            severity="CRITICAL",
            threshold_score=71.4,
            trigger_condition="velocity_1h > 5 and amount > 18600.00",
            sar_code="SAR_TYPOLOGY_044",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 124 under CRYPTO_TUMBLING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0125",
            name="Heuristic Scenario 125 - P2P Rapid Velocity",
            domain="P2P_RAPID_VELOCITY",
            severity="HIGH",
            threshold_score=72.5,
            trigger_condition="velocity_1h > 6 and amount > 18750.00",
            sar_code="SAR_TYPOLOGY_045",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 125 under P2P_RAPID_VELOCITY telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0126",
            name="Heuristic Scenario 126 - Card Not Present",
            domain="CARD_NOT_PRESENT",
            severity="MEDIUM",
            threshold_score=73.6,
            trigger_condition="velocity_1h > 7 and amount > 18900.00",
            sar_code="SAR_TYPOLOGY_046",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 126 under CARD_NOT_PRESENT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0127",
            name="Heuristic Scenario 127 - Wire Structuring",
            domain="WIRE_STRUCTURING",
            severity="LOW",
            threshold_score=74.7,
            trigger_condition="velocity_1h > 8 and amount > 19050.00",
            sar_code="SAR_TYPOLOGY_047",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 127 under WIRE_STRUCTURING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0128",
            name="Heuristic Scenario 128 - Account Takeover",
            domain="ACCOUNT_TAKEOVER",
            severity="CRITICAL",
            threshold_score=75.8,
            trigger_condition="velocity_1h > 9 and amount > 19200.00",
            sar_code="SAR_TYPOLOGY_048",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 128 under ACCOUNT_TAKEOVER telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0129",
            name="Heuristic Scenario 129 - Merchant Bustout",
            domain="MERCHANT_BUSTOUT",
            severity="HIGH",
            threshold_score=76.9,
            trigger_condition="velocity_1h > 10 and amount > 19350.00",
            sar_code="SAR_TYPOLOGY_049",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 129 under MERCHANT_BUSTOUT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0130",
            name="Heuristic Scenario 130 - Crypto Tumbling",
            domain="CRYPTO_TUMBLING",
            severity="MEDIUM",
            threshold_score=78.0,
            trigger_condition="velocity_1h > 1 and amount > 19500.00",
            sar_code="SAR_TYPOLOGY_050",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 130 under CRYPTO_TUMBLING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0131",
            name="Heuristic Scenario 131 - P2P Rapid Velocity",
            domain="P2P_RAPID_VELOCITY",
            severity="LOW",
            threshold_score=79.1,
            trigger_condition="velocity_1h > 2 and amount > 19650.00",
            sar_code="SAR_TYPOLOGY_051",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 131 under P2P_RAPID_VELOCITY telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0132",
            name="Heuristic Scenario 132 - Card Not Present",
            domain="CARD_NOT_PRESENT",
            severity="CRITICAL",
            threshold_score=80.2,
            trigger_condition="velocity_1h > 3 and amount > 19800.00",
            sar_code="SAR_TYPOLOGY_052",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 132 under CARD_NOT_PRESENT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0133",
            name="Heuristic Scenario 133 - Wire Structuring",
            domain="WIRE_STRUCTURING",
            severity="HIGH",
            threshold_score=81.3,
            trigger_condition="velocity_1h > 4 and amount > 19950.00",
            sar_code="SAR_TYPOLOGY_053",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 133 under WIRE_STRUCTURING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0134",
            name="Heuristic Scenario 134 - Account Takeover",
            domain="ACCOUNT_TAKEOVER",
            severity="MEDIUM",
            threshold_score=82.4,
            trigger_condition="velocity_1h > 5 and amount > 20100.00",
            sar_code="SAR_TYPOLOGY_054",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 134 under ACCOUNT_TAKEOVER telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0135",
            name="Heuristic Scenario 135 - Merchant Bustout",
            domain="MERCHANT_BUSTOUT",
            severity="LOW",
            threshold_score=83.5,
            trigger_condition="velocity_1h > 6 and amount > 20250.00",
            sar_code="SAR_TYPOLOGY_055",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 135 under MERCHANT_BUSTOUT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0136",
            name="Heuristic Scenario 136 - Crypto Tumbling",
            domain="CRYPTO_TUMBLING",
            severity="CRITICAL",
            threshold_score=84.6,
            trigger_condition="velocity_1h > 7 and amount > 20400.00",
            sar_code="SAR_TYPOLOGY_056",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 136 under CRYPTO_TUMBLING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0137",
            name="Heuristic Scenario 137 - P2P Rapid Velocity",
            domain="P2P_RAPID_VELOCITY",
            severity="HIGH",
            threshold_score=85.7,
            trigger_condition="velocity_1h > 8 and amount > 20550.00",
            sar_code="SAR_TYPOLOGY_057",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 137 under P2P_RAPID_VELOCITY telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0138",
            name="Heuristic Scenario 138 - Card Not Present",
            domain="CARD_NOT_PRESENT",
            severity="MEDIUM",
            threshold_score=86.8,
            trigger_condition="velocity_1h > 9 and amount > 20700.00",
            sar_code="SAR_TYPOLOGY_058",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 138 under CARD_NOT_PRESENT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0139",
            name="Heuristic Scenario 139 - Wire Structuring",
            domain="WIRE_STRUCTURING",
            severity="LOW",
            threshold_score=87.9,
            trigger_condition="velocity_1h > 10 and amount > 20850.00",
            sar_code="SAR_TYPOLOGY_059",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 139 under WIRE_STRUCTURING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0140",
            name="Heuristic Scenario 140 - Account Takeover",
            domain="ACCOUNT_TAKEOVER",
            severity="CRITICAL",
            threshold_score=89.0,
            trigger_condition="velocity_1h > 1 and amount > 21000.00",
            sar_code="SAR_TYPOLOGY_060",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 140 under ACCOUNT_TAKEOVER telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0141",
            name="Heuristic Scenario 141 - Merchant Bustout",
            domain="MERCHANT_BUSTOUT",
            severity="HIGH",
            threshold_score=90.1,
            trigger_condition="velocity_1h > 2 and amount > 21150.00",
            sar_code="SAR_TYPOLOGY_061",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 141 under MERCHANT_BUSTOUT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0142",
            name="Heuristic Scenario 142 - Crypto Tumbling",
            domain="CRYPTO_TUMBLING",
            severity="MEDIUM",
            threshold_score=91.2,
            trigger_condition="velocity_1h > 3 and amount > 21300.00",
            sar_code="SAR_TYPOLOGY_062",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 142 under CRYPTO_TUMBLING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0143",
            name="Heuristic Scenario 143 - P2P Rapid Velocity",
            domain="P2P_RAPID_VELOCITY",
            severity="LOW",
            threshold_score=92.3,
            trigger_condition="velocity_1h > 4 and amount > 21450.00",
            sar_code="SAR_TYPOLOGY_063",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 143 under P2P_RAPID_VELOCITY telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0144",
            name="Heuristic Scenario 144 - Card Not Present",
            domain="CARD_NOT_PRESENT",
            severity="CRITICAL",
            threshold_score=93.4,
            trigger_condition="velocity_1h > 5 and amount > 21600.00",
            sar_code="SAR_TYPOLOGY_064",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 144 under CARD_NOT_PRESENT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0145",
            name="Heuristic Scenario 145 - Wire Structuring",
            domain="WIRE_STRUCTURING",
            severity="HIGH",
            threshold_score=94.5,
            trigger_condition="velocity_1h > 6 and amount > 21750.00",
            sar_code="SAR_TYPOLOGY_065",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 145 under WIRE_STRUCTURING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0146",
            name="Heuristic Scenario 146 - Account Takeover",
            domain="ACCOUNT_TAKEOVER",
            severity="MEDIUM",
            threshold_score=95.6,
            trigger_condition="velocity_1h > 7 and amount > 21900.00",
            sar_code="SAR_TYPOLOGY_066",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 146 under ACCOUNT_TAKEOVER telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0147",
            name="Heuristic Scenario 147 - Merchant Bustout",
            domain="MERCHANT_BUSTOUT",
            severity="LOW",
            threshold_score=96.7,
            trigger_condition="velocity_1h > 8 and amount > 22050.00",
            sar_code="SAR_TYPOLOGY_067",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 147 under MERCHANT_BUSTOUT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0148",
            name="Heuristic Scenario 148 - Crypto Tumbling",
            domain="CRYPTO_TUMBLING",
            severity="CRITICAL",
            threshold_score=97.8,
            trigger_condition="velocity_1h > 9 and amount > 22200.00",
            sar_code="SAR_TYPOLOGY_068",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 148 under CRYPTO_TUMBLING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0149",
            name="Heuristic Scenario 149 - P2P Rapid Velocity",
            domain="P2P_RAPID_VELOCITY",
            severity="HIGH",
            threshold_score=98.9,
            trigger_condition="velocity_1h > 10 and amount > 22350.00",
            sar_code="SAR_TYPOLOGY_069",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 149 under P2P_RAPID_VELOCITY telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0150",
            name="Heuristic Scenario 150 - Card Not Present",
            domain="CARD_NOT_PRESENT",
            severity="MEDIUM",
            threshold_score=45.0,
            trigger_condition="velocity_1h > 1 and amount > 22500.00",
            sar_code="SAR_TYPOLOGY_070",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 150 under CARD_NOT_PRESENT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0151",
            name="Heuristic Scenario 151 - Wire Structuring",
            domain="WIRE_STRUCTURING",
            severity="LOW",
            threshold_score=46.1,
            trigger_condition="velocity_1h > 2 and amount > 22650.00",
            sar_code="SAR_TYPOLOGY_071",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 151 under WIRE_STRUCTURING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0152",
            name="Heuristic Scenario 152 - Account Takeover",
            domain="ACCOUNT_TAKEOVER",
            severity="CRITICAL",
            threshold_score=47.2,
            trigger_condition="velocity_1h > 3 and amount > 22800.00",
            sar_code="SAR_TYPOLOGY_072",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 152 under ACCOUNT_TAKEOVER telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0153",
            name="Heuristic Scenario 153 - Merchant Bustout",
            domain="MERCHANT_BUSTOUT",
            severity="HIGH",
            threshold_score=48.3,
            trigger_condition="velocity_1h > 4 and amount > 22950.00",
            sar_code="SAR_TYPOLOGY_073",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 153 under MERCHANT_BUSTOUT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0154",
            name="Heuristic Scenario 154 - Crypto Tumbling",
            domain="CRYPTO_TUMBLING",
            severity="MEDIUM",
            threshold_score=49.4,
            trigger_condition="velocity_1h > 5 and amount > 23100.00",
            sar_code="SAR_TYPOLOGY_074",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 154 under CRYPTO_TUMBLING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0155",
            name="Heuristic Scenario 155 - P2P Rapid Velocity",
            domain="P2P_RAPID_VELOCITY",
            severity="LOW",
            threshold_score=50.5,
            trigger_condition="velocity_1h > 6 and amount > 23250.00",
            sar_code="SAR_TYPOLOGY_075",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 155 under P2P_RAPID_VELOCITY telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0156",
            name="Heuristic Scenario 156 - Card Not Present",
            domain="CARD_NOT_PRESENT",
            severity="CRITICAL",
            threshold_score=51.6,
            trigger_condition="velocity_1h > 7 and amount > 23400.00",
            sar_code="SAR_TYPOLOGY_076",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 156 under CARD_NOT_PRESENT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0157",
            name="Heuristic Scenario 157 - Wire Structuring",
            domain="WIRE_STRUCTURING",
            severity="HIGH",
            threshold_score=52.7,
            trigger_condition="velocity_1h > 8 and amount > 23550.00",
            sar_code="SAR_TYPOLOGY_077",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 157 under WIRE_STRUCTURING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0158",
            name="Heuristic Scenario 158 - Account Takeover",
            domain="ACCOUNT_TAKEOVER",
            severity="MEDIUM",
            threshold_score=53.8,
            trigger_condition="velocity_1h > 9 and amount > 23700.00",
            sar_code="SAR_TYPOLOGY_078",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 158 under ACCOUNT_TAKEOVER telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0159",
            name="Heuristic Scenario 159 - Merchant Bustout",
            domain="MERCHANT_BUSTOUT",
            severity="LOW",
            threshold_score=54.9,
            trigger_condition="velocity_1h > 10 and amount > 23850.00",
            sar_code="SAR_TYPOLOGY_079",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 159 under MERCHANT_BUSTOUT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0160",
            name="Heuristic Scenario 160 - Crypto Tumbling",
            domain="CRYPTO_TUMBLING",
            severity="CRITICAL",
            threshold_score=56.0,
            trigger_condition="velocity_1h > 1 and amount > 24000.00",
            sar_code="SAR_TYPOLOGY_000",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 160 under CRYPTO_TUMBLING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0161",
            name="Heuristic Scenario 161 - P2P Rapid Velocity",
            domain="P2P_RAPID_VELOCITY",
            severity="HIGH",
            threshold_score=57.1,
            trigger_condition="velocity_1h > 2 and amount > 24150.00",
            sar_code="SAR_TYPOLOGY_001",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 161 under P2P_RAPID_VELOCITY telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0162",
            name="Heuristic Scenario 162 - Card Not Present",
            domain="CARD_NOT_PRESENT",
            severity="MEDIUM",
            threshold_score=58.2,
            trigger_condition="velocity_1h > 3 and amount > 24300.00",
            sar_code="SAR_TYPOLOGY_002",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 162 under CARD_NOT_PRESENT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0163",
            name="Heuristic Scenario 163 - Wire Structuring",
            domain="WIRE_STRUCTURING",
            severity="LOW",
            threshold_score=59.3,
            trigger_condition="velocity_1h > 4 and amount > 24450.00",
            sar_code="SAR_TYPOLOGY_003",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 163 under WIRE_STRUCTURING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0164",
            name="Heuristic Scenario 164 - Account Takeover",
            domain="ACCOUNT_TAKEOVER",
            severity="CRITICAL",
            threshold_score=60.4,
            trigger_condition="velocity_1h > 5 and amount > 24600.00",
            sar_code="SAR_TYPOLOGY_004",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 164 under ACCOUNT_TAKEOVER telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0165",
            name="Heuristic Scenario 165 - Merchant Bustout",
            domain="MERCHANT_BUSTOUT",
            severity="HIGH",
            threshold_score=61.5,
            trigger_condition="velocity_1h > 6 and amount > 24750.00",
            sar_code="SAR_TYPOLOGY_005",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 165 under MERCHANT_BUSTOUT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0166",
            name="Heuristic Scenario 166 - Crypto Tumbling",
            domain="CRYPTO_TUMBLING",
            severity="MEDIUM",
            threshold_score=62.6,
            trigger_condition="velocity_1h > 7 and amount > 24900.00",
            sar_code="SAR_TYPOLOGY_006",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 166 under CRYPTO_TUMBLING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0167",
            name="Heuristic Scenario 167 - P2P Rapid Velocity",
            domain="P2P_RAPID_VELOCITY",
            severity="LOW",
            threshold_score=63.7,
            trigger_condition="velocity_1h > 8 and amount > 25050.00",
            sar_code="SAR_TYPOLOGY_007",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 167 under P2P_RAPID_VELOCITY telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0168",
            name="Heuristic Scenario 168 - Card Not Present",
            domain="CARD_NOT_PRESENT",
            severity="CRITICAL",
            threshold_score=64.8,
            trigger_condition="velocity_1h > 9 and amount > 25200.00",
            sar_code="SAR_TYPOLOGY_008",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 168 under CARD_NOT_PRESENT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0169",
            name="Heuristic Scenario 169 - Wire Structuring",
            domain="WIRE_STRUCTURING",
            severity="HIGH",
            threshold_score=65.9,
            trigger_condition="velocity_1h > 10 and amount > 25350.00",
            sar_code="SAR_TYPOLOGY_009",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 169 under WIRE_STRUCTURING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0170",
            name="Heuristic Scenario 170 - Account Takeover",
            domain="ACCOUNT_TAKEOVER",
            severity="MEDIUM",
            threshold_score=67.0,
            trigger_condition="velocity_1h > 1 and amount > 25500.00",
            sar_code="SAR_TYPOLOGY_010",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 170 under ACCOUNT_TAKEOVER telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0171",
            name="Heuristic Scenario 171 - Merchant Bustout",
            domain="MERCHANT_BUSTOUT",
            severity="LOW",
            threshold_score=68.1,
            trigger_condition="velocity_1h > 2 and amount > 25650.00",
            sar_code="SAR_TYPOLOGY_011",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 171 under MERCHANT_BUSTOUT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0172",
            name="Heuristic Scenario 172 - Crypto Tumbling",
            domain="CRYPTO_TUMBLING",
            severity="CRITICAL",
            threshold_score=69.2,
            trigger_condition="velocity_1h > 3 and amount > 25800.00",
            sar_code="SAR_TYPOLOGY_012",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 172 under CRYPTO_TUMBLING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0173",
            name="Heuristic Scenario 173 - P2P Rapid Velocity",
            domain="P2P_RAPID_VELOCITY",
            severity="HIGH",
            threshold_score=70.3,
            trigger_condition="velocity_1h > 4 and amount > 25950.00",
            sar_code="SAR_TYPOLOGY_013",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 173 under P2P_RAPID_VELOCITY telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0174",
            name="Heuristic Scenario 174 - Card Not Present",
            domain="CARD_NOT_PRESENT",
            severity="MEDIUM",
            threshold_score=71.4,
            trigger_condition="velocity_1h > 5 and amount > 26100.00",
            sar_code="SAR_TYPOLOGY_014",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 174 under CARD_NOT_PRESENT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0175",
            name="Heuristic Scenario 175 - Wire Structuring",
            domain="WIRE_STRUCTURING",
            severity="LOW",
            threshold_score=72.5,
            trigger_condition="velocity_1h > 6 and amount > 26250.00",
            sar_code="SAR_TYPOLOGY_015",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 175 under WIRE_STRUCTURING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0176",
            name="Heuristic Scenario 176 - Account Takeover",
            domain="ACCOUNT_TAKEOVER",
            severity="CRITICAL",
            threshold_score=73.6,
            trigger_condition="velocity_1h > 7 and amount > 26400.00",
            sar_code="SAR_TYPOLOGY_016",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 176 under ACCOUNT_TAKEOVER telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0177",
            name="Heuristic Scenario 177 - Merchant Bustout",
            domain="MERCHANT_BUSTOUT",
            severity="HIGH",
            threshold_score=74.7,
            trigger_condition="velocity_1h > 8 and amount > 26550.00",
            sar_code="SAR_TYPOLOGY_017",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 177 under MERCHANT_BUSTOUT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0178",
            name="Heuristic Scenario 178 - Crypto Tumbling",
            domain="CRYPTO_TUMBLING",
            severity="MEDIUM",
            threshold_score=75.8,
            trigger_condition="velocity_1h > 9 and amount > 26700.00",
            sar_code="SAR_TYPOLOGY_018",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 178 under CRYPTO_TUMBLING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0179",
            name="Heuristic Scenario 179 - P2P Rapid Velocity",
            domain="P2P_RAPID_VELOCITY",
            severity="LOW",
            threshold_score=76.9,
            trigger_condition="velocity_1h > 10 and amount > 26850.00",
            sar_code="SAR_TYPOLOGY_019",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 179 under P2P_RAPID_VELOCITY telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0180",
            name="Heuristic Scenario 180 - Card Not Present",
            domain="CARD_NOT_PRESENT",
            severity="CRITICAL",
            threshold_score=78.0,
            trigger_condition="velocity_1h > 1 and amount > 27000.00",
            sar_code="SAR_TYPOLOGY_020",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 180 under CARD_NOT_PRESENT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0181",
            name="Heuristic Scenario 181 - Wire Structuring",
            domain="WIRE_STRUCTURING",
            severity="HIGH",
            threshold_score=79.1,
            trigger_condition="velocity_1h > 2 and amount > 27150.00",
            sar_code="SAR_TYPOLOGY_021",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 181 under WIRE_STRUCTURING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0182",
            name="Heuristic Scenario 182 - Account Takeover",
            domain="ACCOUNT_TAKEOVER",
            severity="MEDIUM",
            threshold_score=80.2,
            trigger_condition="velocity_1h > 3 and amount > 27300.00",
            sar_code="SAR_TYPOLOGY_022",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 182 under ACCOUNT_TAKEOVER telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0183",
            name="Heuristic Scenario 183 - Merchant Bustout",
            domain="MERCHANT_BUSTOUT",
            severity="LOW",
            threshold_score=81.3,
            trigger_condition="velocity_1h > 4 and amount > 27450.00",
            sar_code="SAR_TYPOLOGY_023",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 183 under MERCHANT_BUSTOUT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0184",
            name="Heuristic Scenario 184 - Crypto Tumbling",
            domain="CRYPTO_TUMBLING",
            severity="CRITICAL",
            threshold_score=82.4,
            trigger_condition="velocity_1h > 5 and amount > 27600.00",
            sar_code="SAR_TYPOLOGY_024",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 184 under CRYPTO_TUMBLING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0185",
            name="Heuristic Scenario 185 - P2P Rapid Velocity",
            domain="P2P_RAPID_VELOCITY",
            severity="HIGH",
            threshold_score=83.5,
            trigger_condition="velocity_1h > 6 and amount > 27750.00",
            sar_code="SAR_TYPOLOGY_025",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 185 under P2P_RAPID_VELOCITY telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0186",
            name="Heuristic Scenario 186 - Card Not Present",
            domain="CARD_NOT_PRESENT",
            severity="MEDIUM",
            threshold_score=84.6,
            trigger_condition="velocity_1h > 7 and amount > 27900.00",
            sar_code="SAR_TYPOLOGY_026",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 186 under CARD_NOT_PRESENT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0187",
            name="Heuristic Scenario 187 - Wire Structuring",
            domain="WIRE_STRUCTURING",
            severity="LOW",
            threshold_score=85.7,
            trigger_condition="velocity_1h > 8 and amount > 28050.00",
            sar_code="SAR_TYPOLOGY_027",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 187 under WIRE_STRUCTURING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0188",
            name="Heuristic Scenario 188 - Account Takeover",
            domain="ACCOUNT_TAKEOVER",
            severity="CRITICAL",
            threshold_score=86.8,
            trigger_condition="velocity_1h > 9 and amount > 28200.00",
            sar_code="SAR_TYPOLOGY_028",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 188 under ACCOUNT_TAKEOVER telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0189",
            name="Heuristic Scenario 189 - Merchant Bustout",
            domain="MERCHANT_BUSTOUT",
            severity="HIGH",
            threshold_score=87.9,
            trigger_condition="velocity_1h > 10 and amount > 28350.00",
            sar_code="SAR_TYPOLOGY_029",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 189 under MERCHANT_BUSTOUT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0190",
            name="Heuristic Scenario 190 - Crypto Tumbling",
            domain="CRYPTO_TUMBLING",
            severity="MEDIUM",
            threshold_score=89.0,
            trigger_condition="velocity_1h > 1 and amount > 28500.00",
            sar_code="SAR_TYPOLOGY_030",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 190 under CRYPTO_TUMBLING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0191",
            name="Heuristic Scenario 191 - P2P Rapid Velocity",
            domain="P2P_RAPID_VELOCITY",
            severity="LOW",
            threshold_score=90.1,
            trigger_condition="velocity_1h > 2 and amount > 28650.00",
            sar_code="SAR_TYPOLOGY_031",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 191 under P2P_RAPID_VELOCITY telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0192",
            name="Heuristic Scenario 192 - Card Not Present",
            domain="CARD_NOT_PRESENT",
            severity="CRITICAL",
            threshold_score=91.2,
            trigger_condition="velocity_1h > 3 and amount > 28800.00",
            sar_code="SAR_TYPOLOGY_032",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 192 under CARD_NOT_PRESENT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0193",
            name="Heuristic Scenario 193 - Wire Structuring",
            domain="WIRE_STRUCTURING",
            severity="HIGH",
            threshold_score=92.3,
            trigger_condition="velocity_1h > 4 and amount > 28950.00",
            sar_code="SAR_TYPOLOGY_033",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 193 under WIRE_STRUCTURING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0194",
            name="Heuristic Scenario 194 - Account Takeover",
            domain="ACCOUNT_TAKEOVER",
            severity="MEDIUM",
            threshold_score=93.4,
            trigger_condition="velocity_1h > 5 and amount > 29100.00",
            sar_code="SAR_TYPOLOGY_034",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 194 under ACCOUNT_TAKEOVER telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0195",
            name="Heuristic Scenario 195 - Merchant Bustout",
            domain="MERCHANT_BUSTOUT",
            severity="LOW",
            threshold_score=94.5,
            trigger_condition="velocity_1h > 6 and amount > 29250.00",
            sar_code="SAR_TYPOLOGY_035",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 195 under MERCHANT_BUSTOUT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0196",
            name="Heuristic Scenario 196 - Crypto Tumbling",
            domain="CRYPTO_TUMBLING",
            severity="CRITICAL",
            threshold_score=95.6,
            trigger_condition="velocity_1h > 7 and amount > 29400.00",
            sar_code="SAR_TYPOLOGY_036",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 196 under CRYPTO_TUMBLING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0197",
            name="Heuristic Scenario 197 - P2P Rapid Velocity",
            domain="P2P_RAPID_VELOCITY",
            severity="HIGH",
            threshold_score=96.7,
            trigger_condition="velocity_1h > 8 and amount > 29550.00",
            sar_code="SAR_TYPOLOGY_037",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 197 under P2P_RAPID_VELOCITY telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0198",
            name="Heuristic Scenario 198 - Card Not Present",
            domain="CARD_NOT_PRESENT",
            severity="MEDIUM",
            threshold_score=97.8,
            trigger_condition="velocity_1h > 9 and amount > 29700.00",
            sar_code="SAR_TYPOLOGY_038",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 198 under CARD_NOT_PRESENT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0199",
            name="Heuristic Scenario 199 - Wire Structuring",
            domain="WIRE_STRUCTURING",
            severity="LOW",
            threshold_score=98.9,
            trigger_condition="velocity_1h > 10 and amount > 29850.00",
            sar_code="SAR_TYPOLOGY_039",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 199 under WIRE_STRUCTURING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0200",
            name="Heuristic Scenario 200 - Account Takeover",
            domain="ACCOUNT_TAKEOVER",
            severity="CRITICAL",
            threshold_score=45.0,
            trigger_condition="velocity_1h > 1 and amount > 30000.00",
            sar_code="SAR_TYPOLOGY_040",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 200 under ACCOUNT_TAKEOVER telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0201",
            name="Heuristic Scenario 201 - Merchant Bustout",
            domain="MERCHANT_BUSTOUT",
            severity="HIGH",
            threshold_score=46.1,
            trigger_condition="velocity_1h > 2 and amount > 30150.00",
            sar_code="SAR_TYPOLOGY_041",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 201 under MERCHANT_BUSTOUT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0202",
            name="Heuristic Scenario 202 - Crypto Tumbling",
            domain="CRYPTO_TUMBLING",
            severity="MEDIUM",
            threshold_score=47.2,
            trigger_condition="velocity_1h > 3 and amount > 30300.00",
            sar_code="SAR_TYPOLOGY_042",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 202 under CRYPTO_TUMBLING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0203",
            name="Heuristic Scenario 203 - P2P Rapid Velocity",
            domain="P2P_RAPID_VELOCITY",
            severity="LOW",
            threshold_score=48.3,
            trigger_condition="velocity_1h > 4 and amount > 30450.00",
            sar_code="SAR_TYPOLOGY_043",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 203 under P2P_RAPID_VELOCITY telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0204",
            name="Heuristic Scenario 204 - Card Not Present",
            domain="CARD_NOT_PRESENT",
            severity="CRITICAL",
            threshold_score=49.4,
            trigger_condition="velocity_1h > 5 and amount > 30600.00",
            sar_code="SAR_TYPOLOGY_044",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 204 under CARD_NOT_PRESENT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0205",
            name="Heuristic Scenario 205 - Wire Structuring",
            domain="WIRE_STRUCTURING",
            severity="HIGH",
            threshold_score=50.5,
            trigger_condition="velocity_1h > 6 and amount > 30750.00",
            sar_code="SAR_TYPOLOGY_045",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 205 under WIRE_STRUCTURING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0206",
            name="Heuristic Scenario 206 - Account Takeover",
            domain="ACCOUNT_TAKEOVER",
            severity="MEDIUM",
            threshold_score=51.6,
            trigger_condition="velocity_1h > 7 and amount > 30900.00",
            sar_code="SAR_TYPOLOGY_046",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 206 under ACCOUNT_TAKEOVER telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0207",
            name="Heuristic Scenario 207 - Merchant Bustout",
            domain="MERCHANT_BUSTOUT",
            severity="LOW",
            threshold_score=52.7,
            trigger_condition="velocity_1h > 8 and amount > 31050.00",
            sar_code="SAR_TYPOLOGY_047",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 207 under MERCHANT_BUSTOUT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0208",
            name="Heuristic Scenario 208 - Crypto Tumbling",
            domain="CRYPTO_TUMBLING",
            severity="CRITICAL",
            threshold_score=53.8,
            trigger_condition="velocity_1h > 9 and amount > 31200.00",
            sar_code="SAR_TYPOLOGY_048",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 208 under CRYPTO_TUMBLING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0209",
            name="Heuristic Scenario 209 - P2P Rapid Velocity",
            domain="P2P_RAPID_VELOCITY",
            severity="HIGH",
            threshold_score=54.9,
            trigger_condition="velocity_1h > 10 and amount > 31350.00",
            sar_code="SAR_TYPOLOGY_049",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 209 under P2P_RAPID_VELOCITY telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0210",
            name="Heuristic Scenario 210 - Card Not Present",
            domain="CARD_NOT_PRESENT",
            severity="MEDIUM",
            threshold_score=56.0,
            trigger_condition="velocity_1h > 1 and amount > 31500.00",
            sar_code="SAR_TYPOLOGY_050",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 210 under CARD_NOT_PRESENT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0211",
            name="Heuristic Scenario 211 - Wire Structuring",
            domain="WIRE_STRUCTURING",
            severity="LOW",
            threshold_score=57.1,
            trigger_condition="velocity_1h > 2 and amount > 31650.00",
            sar_code="SAR_TYPOLOGY_051",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 211 under WIRE_STRUCTURING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0212",
            name="Heuristic Scenario 212 - Account Takeover",
            domain="ACCOUNT_TAKEOVER",
            severity="CRITICAL",
            threshold_score=58.2,
            trigger_condition="velocity_1h > 3 and amount > 31800.00",
            sar_code="SAR_TYPOLOGY_052",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 212 under ACCOUNT_TAKEOVER telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0213",
            name="Heuristic Scenario 213 - Merchant Bustout",
            domain="MERCHANT_BUSTOUT",
            severity="HIGH",
            threshold_score=59.3,
            trigger_condition="velocity_1h > 4 and amount > 31950.00",
            sar_code="SAR_TYPOLOGY_053",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 213 under MERCHANT_BUSTOUT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0214",
            name="Heuristic Scenario 214 - Crypto Tumbling",
            domain="CRYPTO_TUMBLING",
            severity="MEDIUM",
            threshold_score=60.4,
            trigger_condition="velocity_1h > 5 and amount > 32100.00",
            sar_code="SAR_TYPOLOGY_054",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 214 under CRYPTO_TUMBLING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0215",
            name="Heuristic Scenario 215 - P2P Rapid Velocity",
            domain="P2P_RAPID_VELOCITY",
            severity="LOW",
            threshold_score=61.5,
            trigger_condition="velocity_1h > 6 and amount > 32250.00",
            sar_code="SAR_TYPOLOGY_055",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 215 under P2P_RAPID_VELOCITY telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0216",
            name="Heuristic Scenario 216 - Card Not Present",
            domain="CARD_NOT_PRESENT",
            severity="CRITICAL",
            threshold_score=62.6,
            trigger_condition="velocity_1h > 7 and amount > 32400.00",
            sar_code="SAR_TYPOLOGY_056",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 216 under CARD_NOT_PRESENT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0217",
            name="Heuristic Scenario 217 - Wire Structuring",
            domain="WIRE_STRUCTURING",
            severity="HIGH",
            threshold_score=63.7,
            trigger_condition="velocity_1h > 8 and amount > 32550.00",
            sar_code="SAR_TYPOLOGY_057",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 217 under WIRE_STRUCTURING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0218",
            name="Heuristic Scenario 218 - Account Takeover",
            domain="ACCOUNT_TAKEOVER",
            severity="MEDIUM",
            threshold_score=64.8,
            trigger_condition="velocity_1h > 9 and amount > 32700.00",
            sar_code="SAR_TYPOLOGY_058",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 218 under ACCOUNT_TAKEOVER telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0219",
            name="Heuristic Scenario 219 - Merchant Bustout",
            domain="MERCHANT_BUSTOUT",
            severity="LOW",
            threshold_score=65.9,
            trigger_condition="velocity_1h > 10 and amount > 32850.00",
            sar_code="SAR_TYPOLOGY_059",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 219 under MERCHANT_BUSTOUT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0220",
            name="Heuristic Scenario 220 - Crypto Tumbling",
            domain="CRYPTO_TUMBLING",
            severity="CRITICAL",
            threshold_score=67.0,
            trigger_condition="velocity_1h > 1 and amount > 33000.00",
            sar_code="SAR_TYPOLOGY_060",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 220 under CRYPTO_TUMBLING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0221",
            name="Heuristic Scenario 221 - P2P Rapid Velocity",
            domain="P2P_RAPID_VELOCITY",
            severity="HIGH",
            threshold_score=68.1,
            trigger_condition="velocity_1h > 2 and amount > 33150.00",
            sar_code="SAR_TYPOLOGY_061",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 221 under P2P_RAPID_VELOCITY telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0222",
            name="Heuristic Scenario 222 - Card Not Present",
            domain="CARD_NOT_PRESENT",
            severity="MEDIUM",
            threshold_score=69.2,
            trigger_condition="velocity_1h > 3 and amount > 33300.00",
            sar_code="SAR_TYPOLOGY_062",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 222 under CARD_NOT_PRESENT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0223",
            name="Heuristic Scenario 223 - Wire Structuring",
            domain="WIRE_STRUCTURING",
            severity="LOW",
            threshold_score=70.3,
            trigger_condition="velocity_1h > 4 and amount > 33450.00",
            sar_code="SAR_TYPOLOGY_063",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 223 under WIRE_STRUCTURING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0224",
            name="Heuristic Scenario 224 - Account Takeover",
            domain="ACCOUNT_TAKEOVER",
            severity="CRITICAL",
            threshold_score=71.4,
            trigger_condition="velocity_1h > 5 and amount > 33600.00",
            sar_code="SAR_TYPOLOGY_064",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 224 under ACCOUNT_TAKEOVER telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0225",
            name="Heuristic Scenario 225 - Merchant Bustout",
            domain="MERCHANT_BUSTOUT",
            severity="HIGH",
            threshold_score=72.5,
            trigger_condition="velocity_1h > 6 and amount > 33750.00",
            sar_code="SAR_TYPOLOGY_065",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 225 under MERCHANT_BUSTOUT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0226",
            name="Heuristic Scenario 226 - Crypto Tumbling",
            domain="CRYPTO_TUMBLING",
            severity="MEDIUM",
            threshold_score=73.6,
            trigger_condition="velocity_1h > 7 and amount > 33900.00",
            sar_code="SAR_TYPOLOGY_066",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 226 under CRYPTO_TUMBLING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0227",
            name="Heuristic Scenario 227 - P2P Rapid Velocity",
            domain="P2P_RAPID_VELOCITY",
            severity="LOW",
            threshold_score=74.7,
            trigger_condition="velocity_1h > 8 and amount > 34050.00",
            sar_code="SAR_TYPOLOGY_067",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 227 under P2P_RAPID_VELOCITY telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0228",
            name="Heuristic Scenario 228 - Card Not Present",
            domain="CARD_NOT_PRESENT",
            severity="CRITICAL",
            threshold_score=75.8,
            trigger_condition="velocity_1h > 9 and amount > 34200.00",
            sar_code="SAR_TYPOLOGY_068",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 228 under CARD_NOT_PRESENT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0229",
            name="Heuristic Scenario 229 - Wire Structuring",
            domain="WIRE_STRUCTURING",
            severity="HIGH",
            threshold_score=76.9,
            trigger_condition="velocity_1h > 10 and amount > 34350.00",
            sar_code="SAR_TYPOLOGY_069",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 229 under WIRE_STRUCTURING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0230",
            name="Heuristic Scenario 230 - Account Takeover",
            domain="ACCOUNT_TAKEOVER",
            severity="MEDIUM",
            threshold_score=78.0,
            trigger_condition="velocity_1h > 1 and amount > 34500.00",
            sar_code="SAR_TYPOLOGY_070",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 230 under ACCOUNT_TAKEOVER telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0231",
            name="Heuristic Scenario 231 - Merchant Bustout",
            domain="MERCHANT_BUSTOUT",
            severity="LOW",
            threshold_score=79.1,
            trigger_condition="velocity_1h > 2 and amount > 34650.00",
            sar_code="SAR_TYPOLOGY_071",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 231 under MERCHANT_BUSTOUT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0232",
            name="Heuristic Scenario 232 - Crypto Tumbling",
            domain="CRYPTO_TUMBLING",
            severity="CRITICAL",
            threshold_score=80.2,
            trigger_condition="velocity_1h > 3 and amount > 34800.00",
            sar_code="SAR_TYPOLOGY_072",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 232 under CRYPTO_TUMBLING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0233",
            name="Heuristic Scenario 233 - P2P Rapid Velocity",
            domain="P2P_RAPID_VELOCITY",
            severity="HIGH",
            threshold_score=81.3,
            trigger_condition="velocity_1h > 4 and amount > 34950.00",
            sar_code="SAR_TYPOLOGY_073",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 233 under P2P_RAPID_VELOCITY telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0234",
            name="Heuristic Scenario 234 - Card Not Present",
            domain="CARD_NOT_PRESENT",
            severity="MEDIUM",
            threshold_score=82.4,
            trigger_condition="velocity_1h > 5 and amount > 35100.00",
            sar_code="SAR_TYPOLOGY_074",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 234 under CARD_NOT_PRESENT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0235",
            name="Heuristic Scenario 235 - Wire Structuring",
            domain="WIRE_STRUCTURING",
            severity="LOW",
            threshold_score=83.5,
            trigger_condition="velocity_1h > 6 and amount > 35250.00",
            sar_code="SAR_TYPOLOGY_075",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 235 under WIRE_STRUCTURING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0236",
            name="Heuristic Scenario 236 - Account Takeover",
            domain="ACCOUNT_TAKEOVER",
            severity="CRITICAL",
            threshold_score=84.6,
            trigger_condition="velocity_1h > 7 and amount > 35400.00",
            sar_code="SAR_TYPOLOGY_076",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 236 under ACCOUNT_TAKEOVER telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0237",
            name="Heuristic Scenario 237 - Merchant Bustout",
            domain="MERCHANT_BUSTOUT",
            severity="HIGH",
            threshold_score=85.7,
            trigger_condition="velocity_1h > 8 and amount > 35550.00",
            sar_code="SAR_TYPOLOGY_077",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 237 under MERCHANT_BUSTOUT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0238",
            name="Heuristic Scenario 238 - Crypto Tumbling",
            domain="CRYPTO_TUMBLING",
            severity="MEDIUM",
            threshold_score=86.8,
            trigger_condition="velocity_1h > 9 and amount > 35700.00",
            sar_code="SAR_TYPOLOGY_078",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 238 under CRYPTO_TUMBLING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0239",
            name="Heuristic Scenario 239 - P2P Rapid Velocity",
            domain="P2P_RAPID_VELOCITY",
            severity="LOW",
            threshold_score=87.9,
            trigger_condition="velocity_1h > 10 and amount > 35850.00",
            sar_code="SAR_TYPOLOGY_079",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 239 under P2P_RAPID_VELOCITY telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0240",
            name="Heuristic Scenario 240 - Card Not Present",
            domain="CARD_NOT_PRESENT",
            severity="CRITICAL",
            threshold_score=89.0,
            trigger_condition="velocity_1h > 1 and amount > 36000.00",
            sar_code="SAR_TYPOLOGY_000",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 240 under CARD_NOT_PRESENT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0241",
            name="Heuristic Scenario 241 - Wire Structuring",
            domain="WIRE_STRUCTURING",
            severity="HIGH",
            threshold_score=90.1,
            trigger_condition="velocity_1h > 2 and amount > 36150.00",
            sar_code="SAR_TYPOLOGY_001",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 241 under WIRE_STRUCTURING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0242",
            name="Heuristic Scenario 242 - Account Takeover",
            domain="ACCOUNT_TAKEOVER",
            severity="MEDIUM",
            threshold_score=91.2,
            trigger_condition="velocity_1h > 3 and amount > 36300.00",
            sar_code="SAR_TYPOLOGY_002",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 242 under ACCOUNT_TAKEOVER telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0243",
            name="Heuristic Scenario 243 - Merchant Bustout",
            domain="MERCHANT_BUSTOUT",
            severity="LOW",
            threshold_score=92.3,
            trigger_condition="velocity_1h > 4 and amount > 36450.00",
            sar_code="SAR_TYPOLOGY_003",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 243 under MERCHANT_BUSTOUT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0244",
            name="Heuristic Scenario 244 - Crypto Tumbling",
            domain="CRYPTO_TUMBLING",
            severity="CRITICAL",
            threshold_score=93.4,
            trigger_condition="velocity_1h > 5 and amount > 36600.00",
            sar_code="SAR_TYPOLOGY_004",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 244 under CRYPTO_TUMBLING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0245",
            name="Heuristic Scenario 245 - P2P Rapid Velocity",
            domain="P2P_RAPID_VELOCITY",
            severity="HIGH",
            threshold_score=94.5,
            trigger_condition="velocity_1h > 6 and amount > 36750.00",
            sar_code="SAR_TYPOLOGY_005",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 245 under P2P_RAPID_VELOCITY telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0246",
            name="Heuristic Scenario 246 - Card Not Present",
            domain="CARD_NOT_PRESENT",
            severity="MEDIUM",
            threshold_score=95.6,
            trigger_condition="velocity_1h > 7 and amount > 36900.00",
            sar_code="SAR_TYPOLOGY_006",
            recommended_action="HOLD_FOR_MANUAL_REVIEW",
            description="Automated heuristic rule detecting high-risk pattern 246 under CARD_NOT_PRESENT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0247",
            name="Heuristic Scenario 247 - Wire Structuring",
            domain="WIRE_STRUCTURING",
            severity="LOW",
            threshold_score=96.7,
            trigger_condition="velocity_1h > 8 and amount > 37050.00",
            sar_code="SAR_TYPOLOGY_007",
            recommended_action="STEP_UP_AUTHENTICATION",
            description="Automated heuristic rule detecting high-risk pattern 247 under WIRE_STRUCTURING telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0248",
            name="Heuristic Scenario 248 - Account Takeover",
            domain="ACCOUNT_TAKEOVER",
            severity="CRITICAL",
            threshold_score=97.8,
            trigger_condition="velocity_1h > 9 and amount > 37200.00",
            sar_code="SAR_TYPOLOGY_008",
            recommended_action="NOTIFY_FRAUD_ANALYST",
            description="Automated heuristic rule detecting high-risk pattern 248 under ACCOUNT_TAKEOVER telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0249",
            name="Heuristic Scenario 249 - Merchant Bustout",
            domain="MERCHANT_BUSTOUT",
            severity="HIGH",
            threshold_score=98.9,
            trigger_condition="velocity_1h > 10 and amount > 37350.00",
            sar_code="SAR_TYPOLOGY_009",
            recommended_action="LOG_AUDIT_TRAIL",
            description="Automated heuristic rule detecting high-risk pattern 249 under MERCHANT_BUSTOUT telemetry."
        ))
        self.register(FraudHeuristicScenario(
            scenario_id="HEUR_0250",
            name="Heuristic Scenario 250 - Crypto Tumbling",
            domain="CRYPTO_TUMBLING",
            severity="MEDIUM",
            threshold_score=45.0,
            trigger_condition="velocity_1h > 1 and amount > 37500.00",
            sar_code="SAR_TYPOLOGY_010",
            recommended_action="BLOCK_TRANSACTION",
            description="Automated heuristic rule detecting high-risk pattern 250 under CRYPTO_TUMBLING telemetry."
        ))

    def get_by_domain(self, domain: str) -> List[FraudHeuristicScenario]:
        return [s for s in self.scenarios.values() if s.domain == domain]

    def get_critical_scenarios(self) -> List[FraudHeuristicScenario]:
        return [s for s in self.scenarios.values() if s.severity == "CRITICAL"]

heuristics_catalog = FraudHeuristicsCatalog()

class FraudHeuristicsEngine:
    def __init__(self):
        self.catalog = heuristics_catalog

    def evaluate_payload(self, transaction: Dict[str, Any]) -> Dict[str, Any]:
        amount = float(transaction.get("amount", 0.0))
        triggered = []
        total_score = 0.0
        for s in self.catalog.scenarios.values():
            if amount > s.threshold_score * 10:
                triggered.append(s.scenario_id)
                total_score += s.threshold_score * 0.05
        return {
            "triggered_count": len(triggered),
            "heuristics_triggered": triggered[:10],
            "aggregated_risk_score": min(100.0, round(total_score, 2)),
            "action_required": len(triggered) > 0
        }

heuristics_engine = FraudHeuristicsEngine()

class HeuristicPartitionEvaluator_1:
    """Specialized evaluation partition 1 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 1
        self.weight_multiplier = 1.05
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_2:
    """Specialized evaluation partition 2 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 2
        self.weight_multiplier = 1.10
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_3:
    """Specialized evaluation partition 3 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 3
        self.weight_multiplier = 1.15
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_4:
    """Specialized evaluation partition 4 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 4
        self.weight_multiplier = 1.20
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_5:
    """Specialized evaluation partition 5 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 5
        self.weight_multiplier = 1.25
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_6:
    """Specialized evaluation partition 6 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 6
        self.weight_multiplier = 1.30
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_7:
    """Specialized evaluation partition 7 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 7
        self.weight_multiplier = 1.35
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_8:
    """Specialized evaluation partition 8 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 8
        self.weight_multiplier = 1.40
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_9:
    """Specialized evaluation partition 9 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 9
        self.weight_multiplier = 1.45
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_10:
    """Specialized evaluation partition 10 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 10
        self.weight_multiplier = 1.00
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_11:
    """Specialized evaluation partition 11 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 11
        self.weight_multiplier = 1.05
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_12:
    """Specialized evaluation partition 12 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 12
        self.weight_multiplier = 1.10
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_13:
    """Specialized evaluation partition 13 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 13
        self.weight_multiplier = 1.15
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_14:
    """Specialized evaluation partition 14 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 14
        self.weight_multiplier = 1.20
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_15:
    """Specialized evaluation partition 15 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 15
        self.weight_multiplier = 1.25
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_16:
    """Specialized evaluation partition 16 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 16
        self.weight_multiplier = 1.30
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_17:
    """Specialized evaluation partition 17 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 17
        self.weight_multiplier = 1.35
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_18:
    """Specialized evaluation partition 18 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 18
        self.weight_multiplier = 1.40
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_19:
    """Specialized evaluation partition 19 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 19
        self.weight_multiplier = 1.45
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_20:
    """Specialized evaluation partition 20 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 20
        self.weight_multiplier = 1.00
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_21:
    """Specialized evaluation partition 21 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 21
        self.weight_multiplier = 1.05
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_22:
    """Specialized evaluation partition 22 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 22
        self.weight_multiplier = 1.10
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_23:
    """Specialized evaluation partition 23 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 23
        self.weight_multiplier = 1.15
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_24:
    """Specialized evaluation partition 24 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 24
        self.weight_multiplier = 1.20
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_25:
    """Specialized evaluation partition 25 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 25
        self.weight_multiplier = 1.25
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_26:
    """Specialized evaluation partition 26 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 26
        self.weight_multiplier = 1.30
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_27:
    """Specialized evaluation partition 27 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 27
        self.weight_multiplier = 1.35
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_28:
    """Specialized evaluation partition 28 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 28
        self.weight_multiplier = 1.40
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_29:
    """Specialized evaluation partition 29 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 29
        self.weight_multiplier = 1.45
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_30:
    """Specialized evaluation partition 30 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 30
        self.weight_multiplier = 1.00
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_31:
    """Specialized evaluation partition 31 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 31
        self.weight_multiplier = 1.05
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_32:
    """Specialized evaluation partition 32 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 32
        self.weight_multiplier = 1.10
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_33:
    """Specialized evaluation partition 33 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 33
        self.weight_multiplier = 1.15
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_34:
    """Specialized evaluation partition 34 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 34
        self.weight_multiplier = 1.20
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_35:
    """Specialized evaluation partition 35 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 35
        self.weight_multiplier = 1.25
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_36:
    """Specialized evaluation partition 36 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 36
        self.weight_multiplier = 1.30
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_37:
    """Specialized evaluation partition 37 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 37
        self.weight_multiplier = 1.35
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_38:
    """Specialized evaluation partition 38 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 38
        self.weight_multiplier = 1.40
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_39:
    """Specialized evaluation partition 39 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 39
        self.weight_multiplier = 1.45
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_40:
    """Specialized evaluation partition 40 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 40
        self.weight_multiplier = 1.00
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_41:
    """Specialized evaluation partition 41 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 41
        self.weight_multiplier = 1.05
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_42:
    """Specialized evaluation partition 42 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 42
        self.weight_multiplier = 1.10
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_43:
    """Specialized evaluation partition 43 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 43
        self.weight_multiplier = 1.15
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_44:
    """Specialized evaluation partition 44 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 44
        self.weight_multiplier = 1.20
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_45:
    """Specialized evaluation partition 45 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 45
        self.weight_multiplier = 1.25
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_46:
    """Specialized evaluation partition 46 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 46
        self.weight_multiplier = 1.30
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_47:
    """Specialized evaluation partition 47 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 47
        self.weight_multiplier = 1.35
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_48:
    """Specialized evaluation partition 48 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 48
        self.weight_multiplier = 1.40
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_49:
    """Specialized evaluation partition 49 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 49
        self.weight_multiplier = 1.45
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0

class HeuristicPartitionEvaluator_50:
    """Specialized evaluation partition 50 for parallel scenario scoring."""
    def __init__(self):
        self.partition_id = 50
        self.weight_multiplier = 1.00
    def evaluate_subset(self, tx_amount: float, tx_count: int) -> float:
        return round(float(tx_amount * 0.001 * tx_count * self.weight_multiplier), 4)
    def is_flagged(self, score: float) -> bool:
        return score > 50.0