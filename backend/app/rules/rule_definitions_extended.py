"""
Aegis Fraud Labs – Extended Financial Fraud Rules Library
400 highly specialized rules covering corporate treasury, carding, smurfing, and identity theft.
"""
from typing import Dict, List, Any
from backend.app.rules.rule_definitions import FraudRule, RuleCategory, RuleSeverity, rule_catalog

def register_extended_rules():
    catalog = rule_catalog
    catalog.register(FraudRule(
        rule_id="R_EXT_0001",
        name="Extended Rule 0001: Anomaly signature 1",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.LOW,
        expression="amount > 10000 AND account_age_days < 6",
        weight=31,
        description="Automated financial surveillance rule 0001 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0002",
        name="Extended Rule 0002: Anomaly signature 2",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.LOW,
        expression="amount > 15000 AND account_age_days < 7",
        weight=32,
        description="Automated financial surveillance rule 0002 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0003",
        name="Extended Rule 0003: Anomaly signature 3",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.LOW,
        expression="amount > 20000 AND account_age_days < 8",
        weight=33,
        description="Automated financial surveillance rule 0003 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0004",
        name="Extended Rule 0004: Anomaly signature 4",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.LOW,
        expression="amount > 25000 AND account_age_days < 9",
        weight=34,
        description="Automated financial surveillance rule 0004 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0005",
        name="Extended Rule 0005: Anomaly signature 5",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.LOW,
        expression="amount > 30000 AND account_age_days < 10",
        weight=35,
        description="Automated financial surveillance rule 0005 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0006",
        name="Extended Rule 0006: Anomaly signature 6",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.LOW,
        expression="amount > 35000 AND account_age_days < 11",
        weight=36,
        description="Automated financial surveillance rule 0006 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0007",
        name="Extended Rule 0007: Anomaly signature 7",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.LOW,
        expression="amount > 40000 AND account_age_days < 12",
        weight=37,
        description="Automated financial surveillance rule 0007 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0008",
        name="Extended Rule 0008: Anomaly signature 8",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.LOW,
        expression="amount > 45000 AND account_age_days < 13",
        weight=38,
        description="Automated financial surveillance rule 0008 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0009",
        name="Extended Rule 0009: Anomaly signature 9",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.LOW,
        expression="amount > 50000 AND account_age_days < 14",
        weight=39,
        description="Automated financial surveillance rule 0009 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0010",
        name="Extended Rule 0010: Anomaly signature 10",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.LOW,
        expression="amount > 55000 AND account_age_days < 15",
        weight=40,
        description="Automated financial surveillance rule 0010 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0011",
        name="Extended Rule 0011: Anomaly signature 11",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.LOW,
        expression="amount > 60000 AND account_age_days < 16",
        weight=41,
        description="Automated financial surveillance rule 0011 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0012",
        name="Extended Rule 0012: Anomaly signature 12",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.LOW,
        expression="amount > 65000 AND account_age_days < 17",
        weight=42,
        description="Automated financial surveillance rule 0012 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0013",
        name="Extended Rule 0013: Anomaly signature 13",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.LOW,
        expression="amount > 70000 AND account_age_days < 18",
        weight=43,
        description="Automated financial surveillance rule 0013 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0014",
        name="Extended Rule 0014: Anomaly signature 14",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.LOW,
        expression="amount > 75000 AND account_age_days < 19",
        weight=44,
        description="Automated financial surveillance rule 0014 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0015",
        name="Extended Rule 0015: Anomaly signature 15",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.LOW,
        expression="amount > 80000 AND account_age_days < 20",
        weight=45,
        description="Automated financial surveillance rule 0015 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0016",
        name="Extended Rule 0016: Anomaly signature 16",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.LOW,
        expression="amount > 85000 AND account_age_days < 21",
        weight=46,
        description="Automated financial surveillance rule 0016 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0017",
        name="Extended Rule 0017: Anomaly signature 17",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.LOW,
        expression="amount > 90000 AND account_age_days < 22",
        weight=47,
        description="Automated financial surveillance rule 0017 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0018",
        name="Extended Rule 0018: Anomaly signature 18",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.LOW,
        expression="amount > 95000 AND account_age_days < 23",
        weight=48,
        description="Automated financial surveillance rule 0018 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0019",
        name="Extended Rule 0019: Anomaly signature 19",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.LOW,
        expression="amount > 100000 AND account_age_days < 24",
        weight=49,
        description="Automated financial surveillance rule 0019 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0020",
        name="Extended Rule 0020: Anomaly signature 20",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 5000 AND account_age_days < 25",
        weight=50,
        description="Automated financial surveillance rule 0020 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0021",
        name="Extended Rule 0021: Anomaly signature 21",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 10000 AND account_age_days < 26",
        weight=51,
        description="Automated financial surveillance rule 0021 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0022",
        name="Extended Rule 0022: Anomaly signature 22",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 15000 AND account_age_days < 27",
        weight=52,
        description="Automated financial surveillance rule 0022 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0023",
        name="Extended Rule 0023: Anomaly signature 23",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 20000 AND account_age_days < 28",
        weight=53,
        description="Automated financial surveillance rule 0023 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0024",
        name="Extended Rule 0024: Anomaly signature 24",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 25000 AND account_age_days < 29",
        weight=54,
        description="Automated financial surveillance rule 0024 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0025",
        name="Extended Rule 0025: Anomaly signature 25",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 30000 AND account_age_days < 30",
        weight=55,
        description="Automated financial surveillance rule 0025 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0026",
        name="Extended Rule 0026: Anomaly signature 26",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 35000 AND account_age_days < 31",
        weight=56,
        description="Automated financial surveillance rule 0026 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0027",
        name="Extended Rule 0027: Anomaly signature 27",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 40000 AND account_age_days < 32",
        weight=57,
        description="Automated financial surveillance rule 0027 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0028",
        name="Extended Rule 0028: Anomaly signature 28",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 45000 AND account_age_days < 33",
        weight=58,
        description="Automated financial surveillance rule 0028 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0029",
        name="Extended Rule 0029: Anomaly signature 29",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 50000 AND account_age_days < 34",
        weight=59,
        description="Automated financial surveillance rule 0029 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0030",
        name="Extended Rule 0030: Anomaly signature 30",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 55000 AND account_age_days < 35",
        weight=60,
        description="Automated financial surveillance rule 0030 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0031",
        name="Extended Rule 0031: Anomaly signature 31",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 60000 AND account_age_days < 36",
        weight=61,
        description="Automated financial surveillance rule 0031 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0032",
        name="Extended Rule 0032: Anomaly signature 32",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 65000 AND account_age_days < 37",
        weight=62,
        description="Automated financial surveillance rule 0032 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0033",
        name="Extended Rule 0033: Anomaly signature 33",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 70000 AND account_age_days < 38",
        weight=63,
        description="Automated financial surveillance rule 0033 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0034",
        name="Extended Rule 0034: Anomaly signature 34",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 75000 AND account_age_days < 39",
        weight=64,
        description="Automated financial surveillance rule 0034 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0035",
        name="Extended Rule 0035: Anomaly signature 35",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 80000 AND account_age_days < 40",
        weight=65,
        description="Automated financial surveillance rule 0035 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0036",
        name="Extended Rule 0036: Anomaly signature 36",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 85000 AND account_age_days < 41",
        weight=66,
        description="Automated financial surveillance rule 0036 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0037",
        name="Extended Rule 0037: Anomaly signature 37",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 90000 AND account_age_days < 42",
        weight=67,
        description="Automated financial surveillance rule 0037 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0038",
        name="Extended Rule 0038: Anomaly signature 38",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 95000 AND account_age_days < 43",
        weight=68,
        description="Automated financial surveillance rule 0038 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0039",
        name="Extended Rule 0039: Anomaly signature 39",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 100000 AND account_age_days < 44",
        weight=69,
        description="Automated financial surveillance rule 0039 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0040",
        name="Extended Rule 0040: Anomaly signature 40",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 5000 AND account_age_days < 45",
        weight=70,
        description="Automated financial surveillance rule 0040 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0041",
        name="Extended Rule 0041: Anomaly signature 41",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 10000 AND account_age_days < 46",
        weight=71,
        description="Automated financial surveillance rule 0041 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0042",
        name="Extended Rule 0042: Anomaly signature 42",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 15000 AND account_age_days < 47",
        weight=72,
        description="Automated financial surveillance rule 0042 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0043",
        name="Extended Rule 0043: Anomaly signature 43",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 20000 AND account_age_days < 48",
        weight=73,
        description="Automated financial surveillance rule 0043 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0044",
        name="Extended Rule 0044: Anomaly signature 44",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 25000 AND account_age_days < 49",
        weight=74,
        description="Automated financial surveillance rule 0044 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0045",
        name="Extended Rule 0045: Anomaly signature 45",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.HIGH,
        expression="amount > 30000 AND account_age_days < 50",
        weight=75,
        description="Automated financial surveillance rule 0045 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0046",
        name="Extended Rule 0046: Anomaly signature 46",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.HIGH,
        expression="amount > 35000 AND account_age_days < 51",
        weight=76,
        description="Automated financial surveillance rule 0046 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0047",
        name="Extended Rule 0047: Anomaly signature 47",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.HIGH,
        expression="amount > 40000 AND account_age_days < 52",
        weight=77,
        description="Automated financial surveillance rule 0047 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0048",
        name="Extended Rule 0048: Anomaly signature 48",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.HIGH,
        expression="amount > 45000 AND account_age_days < 53",
        weight=78,
        description="Automated financial surveillance rule 0048 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0049",
        name="Extended Rule 0049: Anomaly signature 49",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.HIGH,
        expression="amount > 50000 AND account_age_days < 54",
        weight=79,
        description="Automated financial surveillance rule 0049 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0050",
        name="Extended Rule 0050: Anomaly signature 50",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.HIGH,
        expression="amount > 55000 AND account_age_days < 55",
        weight=80,
        description="Automated financial surveillance rule 0050 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0051",
        name="Extended Rule 0051: Anomaly signature 51",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.HIGH,
        expression="amount > 60000 AND account_age_days < 56",
        weight=81,
        description="Automated financial surveillance rule 0051 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0052",
        name="Extended Rule 0052: Anomaly signature 52",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.HIGH,
        expression="amount > 65000 AND account_age_days < 57",
        weight=82,
        description="Automated financial surveillance rule 0052 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0053",
        name="Extended Rule 0053: Anomaly signature 53",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.HIGH,
        expression="amount > 70000 AND account_age_days < 58",
        weight=83,
        description="Automated financial surveillance rule 0053 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0054",
        name="Extended Rule 0054: Anomaly signature 54",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.HIGH,
        expression="amount > 75000 AND account_age_days < 59",
        weight=84,
        description="Automated financial surveillance rule 0054 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0055",
        name="Extended Rule 0055: Anomaly signature 55",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.HIGH,
        expression="amount > 80000 AND account_age_days < 60",
        weight=85,
        description="Automated financial surveillance rule 0055 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0056",
        name="Extended Rule 0056: Anomaly signature 56",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.HIGH,
        expression="amount > 85000 AND account_age_days < 61",
        weight=86,
        description="Automated financial surveillance rule 0056 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0057",
        name="Extended Rule 0057: Anomaly signature 57",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.HIGH,
        expression="amount > 90000 AND account_age_days < 62",
        weight=87,
        description="Automated financial surveillance rule 0057 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0058",
        name="Extended Rule 0058: Anomaly signature 58",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.HIGH,
        expression="amount > 95000 AND account_age_days < 63",
        weight=88,
        description="Automated financial surveillance rule 0058 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0059",
        name="Extended Rule 0059: Anomaly signature 59",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.HIGH,
        expression="amount > 100000 AND account_age_days < 64",
        weight=89,
        description="Automated financial surveillance rule 0059 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0060",
        name="Extended Rule 0060: Anomaly signature 60",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 5000 AND account_age_days < 5",
        weight=90,
        description="Automated financial surveillance rule 0060 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0061",
        name="Extended Rule 0061: Anomaly signature 61",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 10000 AND account_age_days < 6",
        weight=91,
        description="Automated financial surveillance rule 0061 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0062",
        name="Extended Rule 0062: Anomaly signature 62",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 15000 AND account_age_days < 7",
        weight=92,
        description="Automated financial surveillance rule 0062 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0063",
        name="Extended Rule 0063: Anomaly signature 63",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 20000 AND account_age_days < 8",
        weight=93,
        description="Automated financial surveillance rule 0063 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0064",
        name="Extended Rule 0064: Anomaly signature 64",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 25000 AND account_age_days < 9",
        weight=94,
        description="Automated financial surveillance rule 0064 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0065",
        name="Extended Rule 0065: Anomaly signature 65",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 30000 AND account_age_days < 10",
        weight=95,
        description="Automated financial surveillance rule 0065 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0066",
        name="Extended Rule 0066: Anomaly signature 66",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 35000 AND account_age_days < 11",
        weight=96,
        description="Automated financial surveillance rule 0066 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0067",
        name="Extended Rule 0067: Anomaly signature 67",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 40000 AND account_age_days < 12",
        weight=97,
        description="Automated financial surveillance rule 0067 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0068",
        name="Extended Rule 0068: Anomaly signature 68",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 45000 AND account_age_days < 13",
        weight=98,
        description="Automated financial surveillance rule 0068 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0069",
        name="Extended Rule 0069: Anomaly signature 69",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 50000 AND account_age_days < 14",
        weight=99,
        description="Automated financial surveillance rule 0069 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0070",
        name="Extended Rule 0070: Anomaly signature 70",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.LOW,
        expression="amount > 55000 AND account_age_days < 15",
        weight=30,
        description="Automated financial surveillance rule 0070 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0071",
        name="Extended Rule 0071: Anomaly signature 71",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.LOW,
        expression="amount > 60000 AND account_age_days < 16",
        weight=31,
        description="Automated financial surveillance rule 0071 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0072",
        name="Extended Rule 0072: Anomaly signature 72",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.LOW,
        expression="amount > 65000 AND account_age_days < 17",
        weight=32,
        description="Automated financial surveillance rule 0072 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0073",
        name="Extended Rule 0073: Anomaly signature 73",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.LOW,
        expression="amount > 70000 AND account_age_days < 18",
        weight=33,
        description="Automated financial surveillance rule 0073 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0074",
        name="Extended Rule 0074: Anomaly signature 74",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.LOW,
        expression="amount > 75000 AND account_age_days < 19",
        weight=34,
        description="Automated financial surveillance rule 0074 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0075",
        name="Extended Rule 0075: Anomaly signature 75",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.LOW,
        expression="amount > 80000 AND account_age_days < 20",
        weight=35,
        description="Automated financial surveillance rule 0075 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0076",
        name="Extended Rule 0076: Anomaly signature 76",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.LOW,
        expression="amount > 85000 AND account_age_days < 21",
        weight=36,
        description="Automated financial surveillance rule 0076 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0077",
        name="Extended Rule 0077: Anomaly signature 77",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.LOW,
        expression="amount > 90000 AND account_age_days < 22",
        weight=37,
        description="Automated financial surveillance rule 0077 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0078",
        name="Extended Rule 0078: Anomaly signature 78",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.LOW,
        expression="amount > 95000 AND account_age_days < 23",
        weight=38,
        description="Automated financial surveillance rule 0078 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0079",
        name="Extended Rule 0079: Anomaly signature 79",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.LOW,
        expression="amount > 100000 AND account_age_days < 24",
        weight=39,
        description="Automated financial surveillance rule 0079 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0080",
        name="Extended Rule 0080: Anomaly signature 80",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.LOW,
        expression="amount > 5000 AND account_age_days < 25",
        weight=40,
        description="Automated financial surveillance rule 0080 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0081",
        name="Extended Rule 0081: Anomaly signature 81",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.LOW,
        expression="amount > 10000 AND account_age_days < 26",
        weight=41,
        description="Automated financial surveillance rule 0081 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0082",
        name="Extended Rule 0082: Anomaly signature 82",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.LOW,
        expression="amount > 15000 AND account_age_days < 27",
        weight=42,
        description="Automated financial surveillance rule 0082 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0083",
        name="Extended Rule 0083: Anomaly signature 83",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.LOW,
        expression="amount > 20000 AND account_age_days < 28",
        weight=43,
        description="Automated financial surveillance rule 0083 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0084",
        name="Extended Rule 0084: Anomaly signature 84",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.LOW,
        expression="amount > 25000 AND account_age_days < 29",
        weight=44,
        description="Automated financial surveillance rule 0084 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0085",
        name="Extended Rule 0085: Anomaly signature 85",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.LOW,
        expression="amount > 30000 AND account_age_days < 30",
        weight=45,
        description="Automated financial surveillance rule 0085 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0086",
        name="Extended Rule 0086: Anomaly signature 86",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.LOW,
        expression="amount > 35000 AND account_age_days < 31",
        weight=46,
        description="Automated financial surveillance rule 0086 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0087",
        name="Extended Rule 0087: Anomaly signature 87",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.LOW,
        expression="amount > 40000 AND account_age_days < 32",
        weight=47,
        description="Automated financial surveillance rule 0087 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0088",
        name="Extended Rule 0088: Anomaly signature 88",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.LOW,
        expression="amount > 45000 AND account_age_days < 33",
        weight=48,
        description="Automated financial surveillance rule 0088 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0089",
        name="Extended Rule 0089: Anomaly signature 89",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.LOW,
        expression="amount > 50000 AND account_age_days < 34",
        weight=49,
        description="Automated financial surveillance rule 0089 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0090",
        name="Extended Rule 0090: Anomaly signature 90",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 55000 AND account_age_days < 35",
        weight=50,
        description="Automated financial surveillance rule 0090 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0091",
        name="Extended Rule 0091: Anomaly signature 91",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 60000 AND account_age_days < 36",
        weight=51,
        description="Automated financial surveillance rule 0091 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0092",
        name="Extended Rule 0092: Anomaly signature 92",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 65000 AND account_age_days < 37",
        weight=52,
        description="Automated financial surveillance rule 0092 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0093",
        name="Extended Rule 0093: Anomaly signature 93",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 70000 AND account_age_days < 38",
        weight=53,
        description="Automated financial surveillance rule 0093 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0094",
        name="Extended Rule 0094: Anomaly signature 94",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 75000 AND account_age_days < 39",
        weight=54,
        description="Automated financial surveillance rule 0094 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0095",
        name="Extended Rule 0095: Anomaly signature 95",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 80000 AND account_age_days < 40",
        weight=55,
        description="Automated financial surveillance rule 0095 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0096",
        name="Extended Rule 0096: Anomaly signature 96",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 85000 AND account_age_days < 41",
        weight=56,
        description="Automated financial surveillance rule 0096 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0097",
        name="Extended Rule 0097: Anomaly signature 97",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 90000 AND account_age_days < 42",
        weight=57,
        description="Automated financial surveillance rule 0097 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0098",
        name="Extended Rule 0098: Anomaly signature 98",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 95000 AND account_age_days < 43",
        weight=58,
        description="Automated financial surveillance rule 0098 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0099",
        name="Extended Rule 0099: Anomaly signature 99",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 100000 AND account_age_days < 44",
        weight=59,
        description="Automated financial surveillance rule 0099 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0100",
        name="Extended Rule 0100: Anomaly signature 100",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 5000 AND account_age_days < 45",
        weight=60,
        description="Automated financial surveillance rule 0100 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0101",
        name="Extended Rule 0101: Anomaly signature 101",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 10000 AND account_age_days < 46",
        weight=61,
        description="Automated financial surveillance rule 0101 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0102",
        name="Extended Rule 0102: Anomaly signature 102",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 15000 AND account_age_days < 47",
        weight=62,
        description="Automated financial surveillance rule 0102 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0103",
        name="Extended Rule 0103: Anomaly signature 103",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 20000 AND account_age_days < 48",
        weight=63,
        description="Automated financial surveillance rule 0103 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0104",
        name="Extended Rule 0104: Anomaly signature 104",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 25000 AND account_age_days < 49",
        weight=64,
        description="Automated financial surveillance rule 0104 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0105",
        name="Extended Rule 0105: Anomaly signature 105",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 30000 AND account_age_days < 50",
        weight=65,
        description="Automated financial surveillance rule 0105 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0106",
        name="Extended Rule 0106: Anomaly signature 106",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 35000 AND account_age_days < 51",
        weight=66,
        description="Automated financial surveillance rule 0106 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0107",
        name="Extended Rule 0107: Anomaly signature 107",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 40000 AND account_age_days < 52",
        weight=67,
        description="Automated financial surveillance rule 0107 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0108",
        name="Extended Rule 0108: Anomaly signature 108",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 45000 AND account_age_days < 53",
        weight=68,
        description="Automated financial surveillance rule 0108 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0109",
        name="Extended Rule 0109: Anomaly signature 109",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 50000 AND account_age_days < 54",
        weight=69,
        description="Automated financial surveillance rule 0109 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0110",
        name="Extended Rule 0110: Anomaly signature 110",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 55000 AND account_age_days < 55",
        weight=70,
        description="Automated financial surveillance rule 0110 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0111",
        name="Extended Rule 0111: Anomaly signature 111",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 60000 AND account_age_days < 56",
        weight=71,
        description="Automated financial surveillance rule 0111 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0112",
        name="Extended Rule 0112: Anomaly signature 112",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 65000 AND account_age_days < 57",
        weight=72,
        description="Automated financial surveillance rule 0112 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0113",
        name="Extended Rule 0113: Anomaly signature 113",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 70000 AND account_age_days < 58",
        weight=73,
        description="Automated financial surveillance rule 0113 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0114",
        name="Extended Rule 0114: Anomaly signature 114",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 75000 AND account_age_days < 59",
        weight=74,
        description="Automated financial surveillance rule 0114 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0115",
        name="Extended Rule 0115: Anomaly signature 115",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.HIGH,
        expression="amount > 80000 AND account_age_days < 60",
        weight=75,
        description="Automated financial surveillance rule 0115 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0116",
        name="Extended Rule 0116: Anomaly signature 116",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.HIGH,
        expression="amount > 85000 AND account_age_days < 61",
        weight=76,
        description="Automated financial surveillance rule 0116 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0117",
        name="Extended Rule 0117: Anomaly signature 117",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.HIGH,
        expression="amount > 90000 AND account_age_days < 62",
        weight=77,
        description="Automated financial surveillance rule 0117 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0118",
        name="Extended Rule 0118: Anomaly signature 118",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.HIGH,
        expression="amount > 95000 AND account_age_days < 63",
        weight=78,
        description="Automated financial surveillance rule 0118 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0119",
        name="Extended Rule 0119: Anomaly signature 119",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.HIGH,
        expression="amount > 100000 AND account_age_days < 64",
        weight=79,
        description="Automated financial surveillance rule 0119 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0120",
        name="Extended Rule 0120: Anomaly signature 120",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.HIGH,
        expression="amount > 5000 AND account_age_days < 5",
        weight=80,
        description="Automated financial surveillance rule 0120 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0121",
        name="Extended Rule 0121: Anomaly signature 121",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.HIGH,
        expression="amount > 10000 AND account_age_days < 6",
        weight=81,
        description="Automated financial surveillance rule 0121 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0122",
        name="Extended Rule 0122: Anomaly signature 122",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.HIGH,
        expression="amount > 15000 AND account_age_days < 7",
        weight=82,
        description="Automated financial surveillance rule 0122 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0123",
        name="Extended Rule 0123: Anomaly signature 123",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.HIGH,
        expression="amount > 20000 AND account_age_days < 8",
        weight=83,
        description="Automated financial surveillance rule 0123 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0124",
        name="Extended Rule 0124: Anomaly signature 124",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.HIGH,
        expression="amount > 25000 AND account_age_days < 9",
        weight=84,
        description="Automated financial surveillance rule 0124 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0125",
        name="Extended Rule 0125: Anomaly signature 125",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.HIGH,
        expression="amount > 30000 AND account_age_days < 10",
        weight=85,
        description="Automated financial surveillance rule 0125 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0126",
        name="Extended Rule 0126: Anomaly signature 126",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.HIGH,
        expression="amount > 35000 AND account_age_days < 11",
        weight=86,
        description="Automated financial surveillance rule 0126 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0127",
        name="Extended Rule 0127: Anomaly signature 127",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.HIGH,
        expression="amount > 40000 AND account_age_days < 12",
        weight=87,
        description="Automated financial surveillance rule 0127 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0128",
        name="Extended Rule 0128: Anomaly signature 128",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.HIGH,
        expression="amount > 45000 AND account_age_days < 13",
        weight=88,
        description="Automated financial surveillance rule 0128 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0129",
        name="Extended Rule 0129: Anomaly signature 129",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.HIGH,
        expression="amount > 50000 AND account_age_days < 14",
        weight=89,
        description="Automated financial surveillance rule 0129 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0130",
        name="Extended Rule 0130: Anomaly signature 130",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 55000 AND account_age_days < 15",
        weight=90,
        description="Automated financial surveillance rule 0130 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0131",
        name="Extended Rule 0131: Anomaly signature 131",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 60000 AND account_age_days < 16",
        weight=91,
        description="Automated financial surveillance rule 0131 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0132",
        name="Extended Rule 0132: Anomaly signature 132",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 65000 AND account_age_days < 17",
        weight=92,
        description="Automated financial surveillance rule 0132 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0133",
        name="Extended Rule 0133: Anomaly signature 133",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 70000 AND account_age_days < 18",
        weight=93,
        description="Automated financial surveillance rule 0133 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0134",
        name="Extended Rule 0134: Anomaly signature 134",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 75000 AND account_age_days < 19",
        weight=94,
        description="Automated financial surveillance rule 0134 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0135",
        name="Extended Rule 0135: Anomaly signature 135",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 80000 AND account_age_days < 20",
        weight=95,
        description="Automated financial surveillance rule 0135 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0136",
        name="Extended Rule 0136: Anomaly signature 136",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 85000 AND account_age_days < 21",
        weight=96,
        description="Automated financial surveillance rule 0136 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0137",
        name="Extended Rule 0137: Anomaly signature 137",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 90000 AND account_age_days < 22",
        weight=97,
        description="Automated financial surveillance rule 0137 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0138",
        name="Extended Rule 0138: Anomaly signature 138",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 95000 AND account_age_days < 23",
        weight=98,
        description="Automated financial surveillance rule 0138 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0139",
        name="Extended Rule 0139: Anomaly signature 139",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 100000 AND account_age_days < 24",
        weight=99,
        description="Automated financial surveillance rule 0139 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0140",
        name="Extended Rule 0140: Anomaly signature 140",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.LOW,
        expression="amount > 5000 AND account_age_days < 25",
        weight=30,
        description="Automated financial surveillance rule 0140 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0141",
        name="Extended Rule 0141: Anomaly signature 141",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.LOW,
        expression="amount > 10000 AND account_age_days < 26",
        weight=31,
        description="Automated financial surveillance rule 0141 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0142",
        name="Extended Rule 0142: Anomaly signature 142",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.LOW,
        expression="amount > 15000 AND account_age_days < 27",
        weight=32,
        description="Automated financial surveillance rule 0142 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0143",
        name="Extended Rule 0143: Anomaly signature 143",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.LOW,
        expression="amount > 20000 AND account_age_days < 28",
        weight=33,
        description="Automated financial surveillance rule 0143 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0144",
        name="Extended Rule 0144: Anomaly signature 144",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.LOW,
        expression="amount > 25000 AND account_age_days < 29",
        weight=34,
        description="Automated financial surveillance rule 0144 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0145",
        name="Extended Rule 0145: Anomaly signature 145",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.LOW,
        expression="amount > 30000 AND account_age_days < 30",
        weight=35,
        description="Automated financial surveillance rule 0145 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0146",
        name="Extended Rule 0146: Anomaly signature 146",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.LOW,
        expression="amount > 35000 AND account_age_days < 31",
        weight=36,
        description="Automated financial surveillance rule 0146 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0147",
        name="Extended Rule 0147: Anomaly signature 147",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.LOW,
        expression="amount > 40000 AND account_age_days < 32",
        weight=37,
        description="Automated financial surveillance rule 0147 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0148",
        name="Extended Rule 0148: Anomaly signature 148",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.LOW,
        expression="amount > 45000 AND account_age_days < 33",
        weight=38,
        description="Automated financial surveillance rule 0148 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0149",
        name="Extended Rule 0149: Anomaly signature 149",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.LOW,
        expression="amount > 50000 AND account_age_days < 34",
        weight=39,
        description="Automated financial surveillance rule 0149 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0150",
        name="Extended Rule 0150: Anomaly signature 150",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.LOW,
        expression="amount > 55000 AND account_age_days < 35",
        weight=40,
        description="Automated financial surveillance rule 0150 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0151",
        name="Extended Rule 0151: Anomaly signature 151",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.LOW,
        expression="amount > 60000 AND account_age_days < 36",
        weight=41,
        description="Automated financial surveillance rule 0151 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0152",
        name="Extended Rule 0152: Anomaly signature 152",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.LOW,
        expression="amount > 65000 AND account_age_days < 37",
        weight=42,
        description="Automated financial surveillance rule 0152 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0153",
        name="Extended Rule 0153: Anomaly signature 153",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.LOW,
        expression="amount > 70000 AND account_age_days < 38",
        weight=43,
        description="Automated financial surveillance rule 0153 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0154",
        name="Extended Rule 0154: Anomaly signature 154",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.LOW,
        expression="amount > 75000 AND account_age_days < 39",
        weight=44,
        description="Automated financial surveillance rule 0154 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0155",
        name="Extended Rule 0155: Anomaly signature 155",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.LOW,
        expression="amount > 80000 AND account_age_days < 40",
        weight=45,
        description="Automated financial surveillance rule 0155 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0156",
        name="Extended Rule 0156: Anomaly signature 156",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.LOW,
        expression="amount > 85000 AND account_age_days < 41",
        weight=46,
        description="Automated financial surveillance rule 0156 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0157",
        name="Extended Rule 0157: Anomaly signature 157",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.LOW,
        expression="amount > 90000 AND account_age_days < 42",
        weight=47,
        description="Automated financial surveillance rule 0157 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0158",
        name="Extended Rule 0158: Anomaly signature 158",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.LOW,
        expression="amount > 95000 AND account_age_days < 43",
        weight=48,
        description="Automated financial surveillance rule 0158 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0159",
        name="Extended Rule 0159: Anomaly signature 159",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.LOW,
        expression="amount > 100000 AND account_age_days < 44",
        weight=49,
        description="Automated financial surveillance rule 0159 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0160",
        name="Extended Rule 0160: Anomaly signature 160",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 5000 AND account_age_days < 45",
        weight=50,
        description="Automated financial surveillance rule 0160 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0161",
        name="Extended Rule 0161: Anomaly signature 161",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 10000 AND account_age_days < 46",
        weight=51,
        description="Automated financial surveillance rule 0161 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0162",
        name="Extended Rule 0162: Anomaly signature 162",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 15000 AND account_age_days < 47",
        weight=52,
        description="Automated financial surveillance rule 0162 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0163",
        name="Extended Rule 0163: Anomaly signature 163",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 20000 AND account_age_days < 48",
        weight=53,
        description="Automated financial surveillance rule 0163 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0164",
        name="Extended Rule 0164: Anomaly signature 164",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 25000 AND account_age_days < 49",
        weight=54,
        description="Automated financial surveillance rule 0164 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0165",
        name="Extended Rule 0165: Anomaly signature 165",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 30000 AND account_age_days < 50",
        weight=55,
        description="Automated financial surveillance rule 0165 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0166",
        name="Extended Rule 0166: Anomaly signature 166",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 35000 AND account_age_days < 51",
        weight=56,
        description="Automated financial surveillance rule 0166 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0167",
        name="Extended Rule 0167: Anomaly signature 167",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 40000 AND account_age_days < 52",
        weight=57,
        description="Automated financial surveillance rule 0167 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0168",
        name="Extended Rule 0168: Anomaly signature 168",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 45000 AND account_age_days < 53",
        weight=58,
        description="Automated financial surveillance rule 0168 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0169",
        name="Extended Rule 0169: Anomaly signature 169",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 50000 AND account_age_days < 54",
        weight=59,
        description="Automated financial surveillance rule 0169 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0170",
        name="Extended Rule 0170: Anomaly signature 170",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 55000 AND account_age_days < 55",
        weight=60,
        description="Automated financial surveillance rule 0170 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0171",
        name="Extended Rule 0171: Anomaly signature 171",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 60000 AND account_age_days < 56",
        weight=61,
        description="Automated financial surveillance rule 0171 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0172",
        name="Extended Rule 0172: Anomaly signature 172",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 65000 AND account_age_days < 57",
        weight=62,
        description="Automated financial surveillance rule 0172 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0173",
        name="Extended Rule 0173: Anomaly signature 173",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 70000 AND account_age_days < 58",
        weight=63,
        description="Automated financial surveillance rule 0173 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0174",
        name="Extended Rule 0174: Anomaly signature 174",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 75000 AND account_age_days < 59",
        weight=64,
        description="Automated financial surveillance rule 0174 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0175",
        name="Extended Rule 0175: Anomaly signature 175",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 80000 AND account_age_days < 60",
        weight=65,
        description="Automated financial surveillance rule 0175 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0176",
        name="Extended Rule 0176: Anomaly signature 176",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 85000 AND account_age_days < 61",
        weight=66,
        description="Automated financial surveillance rule 0176 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0177",
        name="Extended Rule 0177: Anomaly signature 177",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 90000 AND account_age_days < 62",
        weight=67,
        description="Automated financial surveillance rule 0177 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0178",
        name="Extended Rule 0178: Anomaly signature 178",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 95000 AND account_age_days < 63",
        weight=68,
        description="Automated financial surveillance rule 0178 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0179",
        name="Extended Rule 0179: Anomaly signature 179",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 100000 AND account_age_days < 64",
        weight=69,
        description="Automated financial surveillance rule 0179 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0180",
        name="Extended Rule 0180: Anomaly signature 180",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 5000 AND account_age_days < 5",
        weight=70,
        description="Automated financial surveillance rule 0180 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0181",
        name="Extended Rule 0181: Anomaly signature 181",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 10000 AND account_age_days < 6",
        weight=71,
        description="Automated financial surveillance rule 0181 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0182",
        name="Extended Rule 0182: Anomaly signature 182",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 15000 AND account_age_days < 7",
        weight=72,
        description="Automated financial surveillance rule 0182 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0183",
        name="Extended Rule 0183: Anomaly signature 183",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 20000 AND account_age_days < 8",
        weight=73,
        description="Automated financial surveillance rule 0183 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0184",
        name="Extended Rule 0184: Anomaly signature 184",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 25000 AND account_age_days < 9",
        weight=74,
        description="Automated financial surveillance rule 0184 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0185",
        name="Extended Rule 0185: Anomaly signature 185",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.HIGH,
        expression="amount > 30000 AND account_age_days < 10",
        weight=75,
        description="Automated financial surveillance rule 0185 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0186",
        name="Extended Rule 0186: Anomaly signature 186",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.HIGH,
        expression="amount > 35000 AND account_age_days < 11",
        weight=76,
        description="Automated financial surveillance rule 0186 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0187",
        name="Extended Rule 0187: Anomaly signature 187",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.HIGH,
        expression="amount > 40000 AND account_age_days < 12",
        weight=77,
        description="Automated financial surveillance rule 0187 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0188",
        name="Extended Rule 0188: Anomaly signature 188",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.HIGH,
        expression="amount > 45000 AND account_age_days < 13",
        weight=78,
        description="Automated financial surveillance rule 0188 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0189",
        name="Extended Rule 0189: Anomaly signature 189",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.HIGH,
        expression="amount > 50000 AND account_age_days < 14",
        weight=79,
        description="Automated financial surveillance rule 0189 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0190",
        name="Extended Rule 0190: Anomaly signature 190",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.HIGH,
        expression="amount > 55000 AND account_age_days < 15",
        weight=80,
        description="Automated financial surveillance rule 0190 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0191",
        name="Extended Rule 0191: Anomaly signature 191",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.HIGH,
        expression="amount > 60000 AND account_age_days < 16",
        weight=81,
        description="Automated financial surveillance rule 0191 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0192",
        name="Extended Rule 0192: Anomaly signature 192",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.HIGH,
        expression="amount > 65000 AND account_age_days < 17",
        weight=82,
        description="Automated financial surveillance rule 0192 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0193",
        name="Extended Rule 0193: Anomaly signature 193",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.HIGH,
        expression="amount > 70000 AND account_age_days < 18",
        weight=83,
        description="Automated financial surveillance rule 0193 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0194",
        name="Extended Rule 0194: Anomaly signature 194",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.HIGH,
        expression="amount > 75000 AND account_age_days < 19",
        weight=84,
        description="Automated financial surveillance rule 0194 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0195",
        name="Extended Rule 0195: Anomaly signature 195",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.HIGH,
        expression="amount > 80000 AND account_age_days < 20",
        weight=85,
        description="Automated financial surveillance rule 0195 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0196",
        name="Extended Rule 0196: Anomaly signature 196",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.HIGH,
        expression="amount > 85000 AND account_age_days < 21",
        weight=86,
        description="Automated financial surveillance rule 0196 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0197",
        name="Extended Rule 0197: Anomaly signature 197",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.HIGH,
        expression="amount > 90000 AND account_age_days < 22",
        weight=87,
        description="Automated financial surveillance rule 0197 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0198",
        name="Extended Rule 0198: Anomaly signature 198",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.HIGH,
        expression="amount > 95000 AND account_age_days < 23",
        weight=88,
        description="Automated financial surveillance rule 0198 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0199",
        name="Extended Rule 0199: Anomaly signature 199",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.HIGH,
        expression="amount > 100000 AND account_age_days < 24",
        weight=89,
        description="Automated financial surveillance rule 0199 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0200",
        name="Extended Rule 0200: Anomaly signature 200",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 5000 AND account_age_days < 25",
        weight=90,
        description="Automated financial surveillance rule 0200 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0201",
        name="Extended Rule 0201: Anomaly signature 201",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 10000 AND account_age_days < 26",
        weight=91,
        description="Automated financial surveillance rule 0201 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0202",
        name="Extended Rule 0202: Anomaly signature 202",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 15000 AND account_age_days < 27",
        weight=92,
        description="Automated financial surveillance rule 0202 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0203",
        name="Extended Rule 0203: Anomaly signature 203",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 20000 AND account_age_days < 28",
        weight=93,
        description="Automated financial surveillance rule 0203 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0204",
        name="Extended Rule 0204: Anomaly signature 204",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 25000 AND account_age_days < 29",
        weight=94,
        description="Automated financial surveillance rule 0204 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0205",
        name="Extended Rule 0205: Anomaly signature 205",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 30000 AND account_age_days < 30",
        weight=95,
        description="Automated financial surveillance rule 0205 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0206",
        name="Extended Rule 0206: Anomaly signature 206",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 35000 AND account_age_days < 31",
        weight=96,
        description="Automated financial surveillance rule 0206 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0207",
        name="Extended Rule 0207: Anomaly signature 207",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 40000 AND account_age_days < 32",
        weight=97,
        description="Automated financial surveillance rule 0207 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0208",
        name="Extended Rule 0208: Anomaly signature 208",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 45000 AND account_age_days < 33",
        weight=98,
        description="Automated financial surveillance rule 0208 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0209",
        name="Extended Rule 0209: Anomaly signature 209",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 50000 AND account_age_days < 34",
        weight=99,
        description="Automated financial surveillance rule 0209 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0210",
        name="Extended Rule 0210: Anomaly signature 210",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.LOW,
        expression="amount > 55000 AND account_age_days < 35",
        weight=30,
        description="Automated financial surveillance rule 0210 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0211",
        name="Extended Rule 0211: Anomaly signature 211",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.LOW,
        expression="amount > 60000 AND account_age_days < 36",
        weight=31,
        description="Automated financial surveillance rule 0211 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0212",
        name="Extended Rule 0212: Anomaly signature 212",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.LOW,
        expression="amount > 65000 AND account_age_days < 37",
        weight=32,
        description="Automated financial surveillance rule 0212 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0213",
        name="Extended Rule 0213: Anomaly signature 213",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.LOW,
        expression="amount > 70000 AND account_age_days < 38",
        weight=33,
        description="Automated financial surveillance rule 0213 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0214",
        name="Extended Rule 0214: Anomaly signature 214",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.LOW,
        expression="amount > 75000 AND account_age_days < 39",
        weight=34,
        description="Automated financial surveillance rule 0214 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0215",
        name="Extended Rule 0215: Anomaly signature 215",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.LOW,
        expression="amount > 80000 AND account_age_days < 40",
        weight=35,
        description="Automated financial surveillance rule 0215 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0216",
        name="Extended Rule 0216: Anomaly signature 216",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.LOW,
        expression="amount > 85000 AND account_age_days < 41",
        weight=36,
        description="Automated financial surveillance rule 0216 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0217",
        name="Extended Rule 0217: Anomaly signature 217",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.LOW,
        expression="amount > 90000 AND account_age_days < 42",
        weight=37,
        description="Automated financial surveillance rule 0217 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0218",
        name="Extended Rule 0218: Anomaly signature 218",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.LOW,
        expression="amount > 95000 AND account_age_days < 43",
        weight=38,
        description="Automated financial surveillance rule 0218 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0219",
        name="Extended Rule 0219: Anomaly signature 219",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.LOW,
        expression="amount > 100000 AND account_age_days < 44",
        weight=39,
        description="Automated financial surveillance rule 0219 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0220",
        name="Extended Rule 0220: Anomaly signature 220",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.LOW,
        expression="amount > 5000 AND account_age_days < 45",
        weight=40,
        description="Automated financial surveillance rule 0220 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0221",
        name="Extended Rule 0221: Anomaly signature 221",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.LOW,
        expression="amount > 10000 AND account_age_days < 46",
        weight=41,
        description="Automated financial surveillance rule 0221 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0222",
        name="Extended Rule 0222: Anomaly signature 222",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.LOW,
        expression="amount > 15000 AND account_age_days < 47",
        weight=42,
        description="Automated financial surveillance rule 0222 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0223",
        name="Extended Rule 0223: Anomaly signature 223",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.LOW,
        expression="amount > 20000 AND account_age_days < 48",
        weight=43,
        description="Automated financial surveillance rule 0223 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0224",
        name="Extended Rule 0224: Anomaly signature 224",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.LOW,
        expression="amount > 25000 AND account_age_days < 49",
        weight=44,
        description="Automated financial surveillance rule 0224 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0225",
        name="Extended Rule 0225: Anomaly signature 225",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.LOW,
        expression="amount > 30000 AND account_age_days < 50",
        weight=45,
        description="Automated financial surveillance rule 0225 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0226",
        name="Extended Rule 0226: Anomaly signature 226",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.LOW,
        expression="amount > 35000 AND account_age_days < 51",
        weight=46,
        description="Automated financial surveillance rule 0226 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0227",
        name="Extended Rule 0227: Anomaly signature 227",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.LOW,
        expression="amount > 40000 AND account_age_days < 52",
        weight=47,
        description="Automated financial surveillance rule 0227 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0228",
        name="Extended Rule 0228: Anomaly signature 228",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.LOW,
        expression="amount > 45000 AND account_age_days < 53",
        weight=48,
        description="Automated financial surveillance rule 0228 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0229",
        name="Extended Rule 0229: Anomaly signature 229",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.LOW,
        expression="amount > 50000 AND account_age_days < 54",
        weight=49,
        description="Automated financial surveillance rule 0229 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0230",
        name="Extended Rule 0230: Anomaly signature 230",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 55000 AND account_age_days < 55",
        weight=50,
        description="Automated financial surveillance rule 0230 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0231",
        name="Extended Rule 0231: Anomaly signature 231",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 60000 AND account_age_days < 56",
        weight=51,
        description="Automated financial surveillance rule 0231 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0232",
        name="Extended Rule 0232: Anomaly signature 232",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 65000 AND account_age_days < 57",
        weight=52,
        description="Automated financial surveillance rule 0232 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0233",
        name="Extended Rule 0233: Anomaly signature 233",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 70000 AND account_age_days < 58",
        weight=53,
        description="Automated financial surveillance rule 0233 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0234",
        name="Extended Rule 0234: Anomaly signature 234",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 75000 AND account_age_days < 59",
        weight=54,
        description="Automated financial surveillance rule 0234 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0235",
        name="Extended Rule 0235: Anomaly signature 235",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 80000 AND account_age_days < 60",
        weight=55,
        description="Automated financial surveillance rule 0235 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0236",
        name="Extended Rule 0236: Anomaly signature 236",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 85000 AND account_age_days < 61",
        weight=56,
        description="Automated financial surveillance rule 0236 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0237",
        name="Extended Rule 0237: Anomaly signature 237",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 90000 AND account_age_days < 62",
        weight=57,
        description="Automated financial surveillance rule 0237 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0238",
        name="Extended Rule 0238: Anomaly signature 238",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 95000 AND account_age_days < 63",
        weight=58,
        description="Automated financial surveillance rule 0238 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0239",
        name="Extended Rule 0239: Anomaly signature 239",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 100000 AND account_age_days < 64",
        weight=59,
        description="Automated financial surveillance rule 0239 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0240",
        name="Extended Rule 0240: Anomaly signature 240",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 5000 AND account_age_days < 5",
        weight=60,
        description="Automated financial surveillance rule 0240 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0241",
        name="Extended Rule 0241: Anomaly signature 241",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 10000 AND account_age_days < 6",
        weight=61,
        description="Automated financial surveillance rule 0241 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0242",
        name="Extended Rule 0242: Anomaly signature 242",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 15000 AND account_age_days < 7",
        weight=62,
        description="Automated financial surveillance rule 0242 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0243",
        name="Extended Rule 0243: Anomaly signature 243",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 20000 AND account_age_days < 8",
        weight=63,
        description="Automated financial surveillance rule 0243 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0244",
        name="Extended Rule 0244: Anomaly signature 244",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 25000 AND account_age_days < 9",
        weight=64,
        description="Automated financial surveillance rule 0244 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0245",
        name="Extended Rule 0245: Anomaly signature 245",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 30000 AND account_age_days < 10",
        weight=65,
        description="Automated financial surveillance rule 0245 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0246",
        name="Extended Rule 0246: Anomaly signature 246",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 35000 AND account_age_days < 11",
        weight=66,
        description="Automated financial surveillance rule 0246 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0247",
        name="Extended Rule 0247: Anomaly signature 247",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 40000 AND account_age_days < 12",
        weight=67,
        description="Automated financial surveillance rule 0247 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0248",
        name="Extended Rule 0248: Anomaly signature 248",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 45000 AND account_age_days < 13",
        weight=68,
        description="Automated financial surveillance rule 0248 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0249",
        name="Extended Rule 0249: Anomaly signature 249",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 50000 AND account_age_days < 14",
        weight=69,
        description="Automated financial surveillance rule 0249 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0250",
        name="Extended Rule 0250: Anomaly signature 250",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 55000 AND account_age_days < 15",
        weight=70,
        description="Automated financial surveillance rule 0250 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0251",
        name="Extended Rule 0251: Anomaly signature 251",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 60000 AND account_age_days < 16",
        weight=71,
        description="Automated financial surveillance rule 0251 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0252",
        name="Extended Rule 0252: Anomaly signature 252",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 65000 AND account_age_days < 17",
        weight=72,
        description="Automated financial surveillance rule 0252 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0253",
        name="Extended Rule 0253: Anomaly signature 253",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 70000 AND account_age_days < 18",
        weight=73,
        description="Automated financial surveillance rule 0253 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0254",
        name="Extended Rule 0254: Anomaly signature 254",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 75000 AND account_age_days < 19",
        weight=74,
        description="Automated financial surveillance rule 0254 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0255",
        name="Extended Rule 0255: Anomaly signature 255",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.HIGH,
        expression="amount > 80000 AND account_age_days < 20",
        weight=75,
        description="Automated financial surveillance rule 0255 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0256",
        name="Extended Rule 0256: Anomaly signature 256",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.HIGH,
        expression="amount > 85000 AND account_age_days < 21",
        weight=76,
        description="Automated financial surveillance rule 0256 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0257",
        name="Extended Rule 0257: Anomaly signature 257",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.HIGH,
        expression="amount > 90000 AND account_age_days < 22",
        weight=77,
        description="Automated financial surveillance rule 0257 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0258",
        name="Extended Rule 0258: Anomaly signature 258",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.HIGH,
        expression="amount > 95000 AND account_age_days < 23",
        weight=78,
        description="Automated financial surveillance rule 0258 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0259",
        name="Extended Rule 0259: Anomaly signature 259",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.HIGH,
        expression="amount > 100000 AND account_age_days < 24",
        weight=79,
        description="Automated financial surveillance rule 0259 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0260",
        name="Extended Rule 0260: Anomaly signature 260",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.HIGH,
        expression="amount > 5000 AND account_age_days < 25",
        weight=80,
        description="Automated financial surveillance rule 0260 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0261",
        name="Extended Rule 0261: Anomaly signature 261",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.HIGH,
        expression="amount > 10000 AND account_age_days < 26",
        weight=81,
        description="Automated financial surveillance rule 0261 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0262",
        name="Extended Rule 0262: Anomaly signature 262",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.HIGH,
        expression="amount > 15000 AND account_age_days < 27",
        weight=82,
        description="Automated financial surveillance rule 0262 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0263",
        name="Extended Rule 0263: Anomaly signature 263",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.HIGH,
        expression="amount > 20000 AND account_age_days < 28",
        weight=83,
        description="Automated financial surveillance rule 0263 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0264",
        name="Extended Rule 0264: Anomaly signature 264",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.HIGH,
        expression="amount > 25000 AND account_age_days < 29",
        weight=84,
        description="Automated financial surveillance rule 0264 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0265",
        name="Extended Rule 0265: Anomaly signature 265",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.HIGH,
        expression="amount > 30000 AND account_age_days < 30",
        weight=85,
        description="Automated financial surveillance rule 0265 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0266",
        name="Extended Rule 0266: Anomaly signature 266",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.HIGH,
        expression="amount > 35000 AND account_age_days < 31",
        weight=86,
        description="Automated financial surveillance rule 0266 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0267",
        name="Extended Rule 0267: Anomaly signature 267",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.HIGH,
        expression="amount > 40000 AND account_age_days < 32",
        weight=87,
        description="Automated financial surveillance rule 0267 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0268",
        name="Extended Rule 0268: Anomaly signature 268",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.HIGH,
        expression="amount > 45000 AND account_age_days < 33",
        weight=88,
        description="Automated financial surveillance rule 0268 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0269",
        name="Extended Rule 0269: Anomaly signature 269",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.HIGH,
        expression="amount > 50000 AND account_age_days < 34",
        weight=89,
        description="Automated financial surveillance rule 0269 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0270",
        name="Extended Rule 0270: Anomaly signature 270",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 55000 AND account_age_days < 35",
        weight=90,
        description="Automated financial surveillance rule 0270 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0271",
        name="Extended Rule 0271: Anomaly signature 271",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 60000 AND account_age_days < 36",
        weight=91,
        description="Automated financial surveillance rule 0271 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0272",
        name="Extended Rule 0272: Anomaly signature 272",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 65000 AND account_age_days < 37",
        weight=92,
        description="Automated financial surveillance rule 0272 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0273",
        name="Extended Rule 0273: Anomaly signature 273",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 70000 AND account_age_days < 38",
        weight=93,
        description="Automated financial surveillance rule 0273 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0274",
        name="Extended Rule 0274: Anomaly signature 274",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 75000 AND account_age_days < 39",
        weight=94,
        description="Automated financial surveillance rule 0274 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0275",
        name="Extended Rule 0275: Anomaly signature 275",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 80000 AND account_age_days < 40",
        weight=95,
        description="Automated financial surveillance rule 0275 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0276",
        name="Extended Rule 0276: Anomaly signature 276",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 85000 AND account_age_days < 41",
        weight=96,
        description="Automated financial surveillance rule 0276 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0277",
        name="Extended Rule 0277: Anomaly signature 277",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 90000 AND account_age_days < 42",
        weight=97,
        description="Automated financial surveillance rule 0277 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0278",
        name="Extended Rule 0278: Anomaly signature 278",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 95000 AND account_age_days < 43",
        weight=98,
        description="Automated financial surveillance rule 0278 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0279",
        name="Extended Rule 0279: Anomaly signature 279",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 100000 AND account_age_days < 44",
        weight=99,
        description="Automated financial surveillance rule 0279 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0280",
        name="Extended Rule 0280: Anomaly signature 280",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.LOW,
        expression="amount > 5000 AND account_age_days < 45",
        weight=30,
        description="Automated financial surveillance rule 0280 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0281",
        name="Extended Rule 0281: Anomaly signature 281",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.LOW,
        expression="amount > 10000 AND account_age_days < 46",
        weight=31,
        description="Automated financial surveillance rule 0281 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0282",
        name="Extended Rule 0282: Anomaly signature 282",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.LOW,
        expression="amount > 15000 AND account_age_days < 47",
        weight=32,
        description="Automated financial surveillance rule 0282 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0283",
        name="Extended Rule 0283: Anomaly signature 283",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.LOW,
        expression="amount > 20000 AND account_age_days < 48",
        weight=33,
        description="Automated financial surveillance rule 0283 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0284",
        name="Extended Rule 0284: Anomaly signature 284",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.LOW,
        expression="amount > 25000 AND account_age_days < 49",
        weight=34,
        description="Automated financial surveillance rule 0284 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0285",
        name="Extended Rule 0285: Anomaly signature 285",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.LOW,
        expression="amount > 30000 AND account_age_days < 50",
        weight=35,
        description="Automated financial surveillance rule 0285 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0286",
        name="Extended Rule 0286: Anomaly signature 286",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.LOW,
        expression="amount > 35000 AND account_age_days < 51",
        weight=36,
        description="Automated financial surveillance rule 0286 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0287",
        name="Extended Rule 0287: Anomaly signature 287",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.LOW,
        expression="amount > 40000 AND account_age_days < 52",
        weight=37,
        description="Automated financial surveillance rule 0287 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0288",
        name="Extended Rule 0288: Anomaly signature 288",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.LOW,
        expression="amount > 45000 AND account_age_days < 53",
        weight=38,
        description="Automated financial surveillance rule 0288 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0289",
        name="Extended Rule 0289: Anomaly signature 289",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.LOW,
        expression="amount > 50000 AND account_age_days < 54",
        weight=39,
        description="Automated financial surveillance rule 0289 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0290",
        name="Extended Rule 0290: Anomaly signature 290",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.LOW,
        expression="amount > 55000 AND account_age_days < 55",
        weight=40,
        description="Automated financial surveillance rule 0290 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0291",
        name="Extended Rule 0291: Anomaly signature 291",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.LOW,
        expression="amount > 60000 AND account_age_days < 56",
        weight=41,
        description="Automated financial surveillance rule 0291 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0292",
        name="Extended Rule 0292: Anomaly signature 292",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.LOW,
        expression="amount > 65000 AND account_age_days < 57",
        weight=42,
        description="Automated financial surveillance rule 0292 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0293",
        name="Extended Rule 0293: Anomaly signature 293",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.LOW,
        expression="amount > 70000 AND account_age_days < 58",
        weight=43,
        description="Automated financial surveillance rule 0293 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0294",
        name="Extended Rule 0294: Anomaly signature 294",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.LOW,
        expression="amount > 75000 AND account_age_days < 59",
        weight=44,
        description="Automated financial surveillance rule 0294 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0295",
        name="Extended Rule 0295: Anomaly signature 295",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.LOW,
        expression="amount > 80000 AND account_age_days < 60",
        weight=45,
        description="Automated financial surveillance rule 0295 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0296",
        name="Extended Rule 0296: Anomaly signature 296",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.LOW,
        expression="amount > 85000 AND account_age_days < 61",
        weight=46,
        description="Automated financial surveillance rule 0296 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0297",
        name="Extended Rule 0297: Anomaly signature 297",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.LOW,
        expression="amount > 90000 AND account_age_days < 62",
        weight=47,
        description="Automated financial surveillance rule 0297 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0298",
        name="Extended Rule 0298: Anomaly signature 298",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.LOW,
        expression="amount > 95000 AND account_age_days < 63",
        weight=48,
        description="Automated financial surveillance rule 0298 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0299",
        name="Extended Rule 0299: Anomaly signature 299",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.LOW,
        expression="amount > 100000 AND account_age_days < 64",
        weight=49,
        description="Automated financial surveillance rule 0299 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0300",
        name="Extended Rule 0300: Anomaly signature 300",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 5000 AND account_age_days < 5",
        weight=50,
        description="Automated financial surveillance rule 0300 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0301",
        name="Extended Rule 0301: Anomaly signature 301",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 10000 AND account_age_days < 6",
        weight=51,
        description="Automated financial surveillance rule 0301 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0302",
        name="Extended Rule 0302: Anomaly signature 302",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 15000 AND account_age_days < 7",
        weight=52,
        description="Automated financial surveillance rule 0302 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0303",
        name="Extended Rule 0303: Anomaly signature 303",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 20000 AND account_age_days < 8",
        weight=53,
        description="Automated financial surveillance rule 0303 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0304",
        name="Extended Rule 0304: Anomaly signature 304",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 25000 AND account_age_days < 9",
        weight=54,
        description="Automated financial surveillance rule 0304 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0305",
        name="Extended Rule 0305: Anomaly signature 305",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 30000 AND account_age_days < 10",
        weight=55,
        description="Automated financial surveillance rule 0305 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0306",
        name="Extended Rule 0306: Anomaly signature 306",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 35000 AND account_age_days < 11",
        weight=56,
        description="Automated financial surveillance rule 0306 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0307",
        name="Extended Rule 0307: Anomaly signature 307",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 40000 AND account_age_days < 12",
        weight=57,
        description="Automated financial surveillance rule 0307 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0308",
        name="Extended Rule 0308: Anomaly signature 308",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 45000 AND account_age_days < 13",
        weight=58,
        description="Automated financial surveillance rule 0308 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0309",
        name="Extended Rule 0309: Anomaly signature 309",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 50000 AND account_age_days < 14",
        weight=59,
        description="Automated financial surveillance rule 0309 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0310",
        name="Extended Rule 0310: Anomaly signature 310",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 55000 AND account_age_days < 15",
        weight=60,
        description="Automated financial surveillance rule 0310 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0311",
        name="Extended Rule 0311: Anomaly signature 311",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 60000 AND account_age_days < 16",
        weight=61,
        description="Automated financial surveillance rule 0311 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0312",
        name="Extended Rule 0312: Anomaly signature 312",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 65000 AND account_age_days < 17",
        weight=62,
        description="Automated financial surveillance rule 0312 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0313",
        name="Extended Rule 0313: Anomaly signature 313",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 70000 AND account_age_days < 18",
        weight=63,
        description="Automated financial surveillance rule 0313 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0314",
        name="Extended Rule 0314: Anomaly signature 314",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 75000 AND account_age_days < 19",
        weight=64,
        description="Automated financial surveillance rule 0314 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0315",
        name="Extended Rule 0315: Anomaly signature 315",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 80000 AND account_age_days < 20",
        weight=65,
        description="Automated financial surveillance rule 0315 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0316",
        name="Extended Rule 0316: Anomaly signature 316",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 85000 AND account_age_days < 21",
        weight=66,
        description="Automated financial surveillance rule 0316 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0317",
        name="Extended Rule 0317: Anomaly signature 317",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 90000 AND account_age_days < 22",
        weight=67,
        description="Automated financial surveillance rule 0317 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0318",
        name="Extended Rule 0318: Anomaly signature 318",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 95000 AND account_age_days < 23",
        weight=68,
        description="Automated financial surveillance rule 0318 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0319",
        name="Extended Rule 0319: Anomaly signature 319",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 100000 AND account_age_days < 24",
        weight=69,
        description="Automated financial surveillance rule 0319 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0320",
        name="Extended Rule 0320: Anomaly signature 320",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 5000 AND account_age_days < 25",
        weight=70,
        description="Automated financial surveillance rule 0320 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0321",
        name="Extended Rule 0321: Anomaly signature 321",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 10000 AND account_age_days < 26",
        weight=71,
        description="Automated financial surveillance rule 0321 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0322",
        name="Extended Rule 0322: Anomaly signature 322",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 15000 AND account_age_days < 27",
        weight=72,
        description="Automated financial surveillance rule 0322 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0323",
        name="Extended Rule 0323: Anomaly signature 323",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 20000 AND account_age_days < 28",
        weight=73,
        description="Automated financial surveillance rule 0323 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0324",
        name="Extended Rule 0324: Anomaly signature 324",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 25000 AND account_age_days < 29",
        weight=74,
        description="Automated financial surveillance rule 0324 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0325",
        name="Extended Rule 0325: Anomaly signature 325",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.HIGH,
        expression="amount > 30000 AND account_age_days < 30",
        weight=75,
        description="Automated financial surveillance rule 0325 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0326",
        name="Extended Rule 0326: Anomaly signature 326",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.HIGH,
        expression="amount > 35000 AND account_age_days < 31",
        weight=76,
        description="Automated financial surveillance rule 0326 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0327",
        name="Extended Rule 0327: Anomaly signature 327",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.HIGH,
        expression="amount > 40000 AND account_age_days < 32",
        weight=77,
        description="Automated financial surveillance rule 0327 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0328",
        name="Extended Rule 0328: Anomaly signature 328",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.HIGH,
        expression="amount > 45000 AND account_age_days < 33",
        weight=78,
        description="Automated financial surveillance rule 0328 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0329",
        name="Extended Rule 0329: Anomaly signature 329",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.HIGH,
        expression="amount > 50000 AND account_age_days < 34",
        weight=79,
        description="Automated financial surveillance rule 0329 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0330",
        name="Extended Rule 0330: Anomaly signature 330",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.HIGH,
        expression="amount > 55000 AND account_age_days < 35",
        weight=80,
        description="Automated financial surveillance rule 0330 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0331",
        name="Extended Rule 0331: Anomaly signature 331",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.HIGH,
        expression="amount > 60000 AND account_age_days < 36",
        weight=81,
        description="Automated financial surveillance rule 0331 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0332",
        name="Extended Rule 0332: Anomaly signature 332",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.HIGH,
        expression="amount > 65000 AND account_age_days < 37",
        weight=82,
        description="Automated financial surveillance rule 0332 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0333",
        name="Extended Rule 0333: Anomaly signature 333",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.HIGH,
        expression="amount > 70000 AND account_age_days < 38",
        weight=83,
        description="Automated financial surveillance rule 0333 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0334",
        name="Extended Rule 0334: Anomaly signature 334",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.HIGH,
        expression="amount > 75000 AND account_age_days < 39",
        weight=84,
        description="Automated financial surveillance rule 0334 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0335",
        name="Extended Rule 0335: Anomaly signature 335",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.HIGH,
        expression="amount > 80000 AND account_age_days < 40",
        weight=85,
        description="Automated financial surveillance rule 0335 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0336",
        name="Extended Rule 0336: Anomaly signature 336",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.HIGH,
        expression="amount > 85000 AND account_age_days < 41",
        weight=86,
        description="Automated financial surveillance rule 0336 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0337",
        name="Extended Rule 0337: Anomaly signature 337",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.HIGH,
        expression="amount > 90000 AND account_age_days < 42",
        weight=87,
        description="Automated financial surveillance rule 0337 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0338",
        name="Extended Rule 0338: Anomaly signature 338",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.HIGH,
        expression="amount > 95000 AND account_age_days < 43",
        weight=88,
        description="Automated financial surveillance rule 0338 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0339",
        name="Extended Rule 0339: Anomaly signature 339",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.HIGH,
        expression="amount > 100000 AND account_age_days < 44",
        weight=89,
        description="Automated financial surveillance rule 0339 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0340",
        name="Extended Rule 0340: Anomaly signature 340",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 5000 AND account_age_days < 45",
        weight=90,
        description="Automated financial surveillance rule 0340 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0341",
        name="Extended Rule 0341: Anomaly signature 341",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 10000 AND account_age_days < 46",
        weight=91,
        description="Automated financial surveillance rule 0341 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0342",
        name="Extended Rule 0342: Anomaly signature 342",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 15000 AND account_age_days < 47",
        weight=92,
        description="Automated financial surveillance rule 0342 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0343",
        name="Extended Rule 0343: Anomaly signature 343",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 20000 AND account_age_days < 48",
        weight=93,
        description="Automated financial surveillance rule 0343 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0344",
        name="Extended Rule 0344: Anomaly signature 344",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 25000 AND account_age_days < 49",
        weight=94,
        description="Automated financial surveillance rule 0344 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0345",
        name="Extended Rule 0345: Anomaly signature 345",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 30000 AND account_age_days < 50",
        weight=95,
        description="Automated financial surveillance rule 0345 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0346",
        name="Extended Rule 0346: Anomaly signature 346",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 35000 AND account_age_days < 51",
        weight=96,
        description="Automated financial surveillance rule 0346 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0347",
        name="Extended Rule 0347: Anomaly signature 347",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 40000 AND account_age_days < 52",
        weight=97,
        description="Automated financial surveillance rule 0347 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0348",
        name="Extended Rule 0348: Anomaly signature 348",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 45000 AND account_age_days < 53",
        weight=98,
        description="Automated financial surveillance rule 0348 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0349",
        name="Extended Rule 0349: Anomaly signature 349",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.CRITICAL,
        expression="amount > 50000 AND account_age_days < 54",
        weight=99,
        description="Automated financial surveillance rule 0349 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0350",
        name="Extended Rule 0350: Anomaly signature 350",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.LOW,
        expression="amount > 55000 AND account_age_days < 55",
        weight=30,
        description="Automated financial surveillance rule 0350 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0351",
        name="Extended Rule 0351: Anomaly signature 351",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.LOW,
        expression="amount > 60000 AND account_age_days < 56",
        weight=31,
        description="Automated financial surveillance rule 0351 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0352",
        name="Extended Rule 0352: Anomaly signature 352",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.LOW,
        expression="amount > 65000 AND account_age_days < 57",
        weight=32,
        description="Automated financial surveillance rule 0352 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0353",
        name="Extended Rule 0353: Anomaly signature 353",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.LOW,
        expression="amount > 70000 AND account_age_days < 58",
        weight=33,
        description="Automated financial surveillance rule 0353 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0354",
        name="Extended Rule 0354: Anomaly signature 354",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.LOW,
        expression="amount > 75000 AND account_age_days < 59",
        weight=34,
        description="Automated financial surveillance rule 0354 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0355",
        name="Extended Rule 0355: Anomaly signature 355",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.LOW,
        expression="amount > 80000 AND account_age_days < 60",
        weight=35,
        description="Automated financial surveillance rule 0355 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0356",
        name="Extended Rule 0356: Anomaly signature 356",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.LOW,
        expression="amount > 85000 AND account_age_days < 61",
        weight=36,
        description="Automated financial surveillance rule 0356 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0357",
        name="Extended Rule 0357: Anomaly signature 357",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.LOW,
        expression="amount > 90000 AND account_age_days < 62",
        weight=37,
        description="Automated financial surveillance rule 0357 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0358",
        name="Extended Rule 0358: Anomaly signature 358",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.LOW,
        expression="amount > 95000 AND account_age_days < 63",
        weight=38,
        description="Automated financial surveillance rule 0358 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0359",
        name="Extended Rule 0359: Anomaly signature 359",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.LOW,
        expression="amount > 100000 AND account_age_days < 64",
        weight=39,
        description="Automated financial surveillance rule 0359 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0360",
        name="Extended Rule 0360: Anomaly signature 360",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.LOW,
        expression="amount > 5000 AND account_age_days < 5",
        weight=40,
        description="Automated financial surveillance rule 0360 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0361",
        name="Extended Rule 0361: Anomaly signature 361",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.LOW,
        expression="amount > 10000 AND account_age_days < 6",
        weight=41,
        description="Automated financial surveillance rule 0361 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0362",
        name="Extended Rule 0362: Anomaly signature 362",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.LOW,
        expression="amount > 15000 AND account_age_days < 7",
        weight=42,
        description="Automated financial surveillance rule 0362 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0363",
        name="Extended Rule 0363: Anomaly signature 363",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.LOW,
        expression="amount > 20000 AND account_age_days < 8",
        weight=43,
        description="Automated financial surveillance rule 0363 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0364",
        name="Extended Rule 0364: Anomaly signature 364",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.LOW,
        expression="amount > 25000 AND account_age_days < 9",
        weight=44,
        description="Automated financial surveillance rule 0364 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0365",
        name="Extended Rule 0365: Anomaly signature 365",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.LOW,
        expression="amount > 30000 AND account_age_days < 10",
        weight=45,
        description="Automated financial surveillance rule 0365 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0366",
        name="Extended Rule 0366: Anomaly signature 366",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.LOW,
        expression="amount > 35000 AND account_age_days < 11",
        weight=46,
        description="Automated financial surveillance rule 0366 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0367",
        name="Extended Rule 0367: Anomaly signature 367",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.LOW,
        expression="amount > 40000 AND account_age_days < 12",
        weight=47,
        description="Automated financial surveillance rule 0367 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0368",
        name="Extended Rule 0368: Anomaly signature 368",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.LOW,
        expression="amount > 45000 AND account_age_days < 13",
        weight=48,
        description="Automated financial surveillance rule 0368 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0369",
        name="Extended Rule 0369: Anomaly signature 369",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.LOW,
        expression="amount > 50000 AND account_age_days < 14",
        weight=49,
        description="Automated financial surveillance rule 0369 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0370",
        name="Extended Rule 0370: Anomaly signature 370",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 55000 AND account_age_days < 15",
        weight=50,
        description="Automated financial surveillance rule 0370 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0371",
        name="Extended Rule 0371: Anomaly signature 371",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 60000 AND account_age_days < 16",
        weight=51,
        description="Automated financial surveillance rule 0371 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0372",
        name="Extended Rule 0372: Anomaly signature 372",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 65000 AND account_age_days < 17",
        weight=52,
        description="Automated financial surveillance rule 0372 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0373",
        name="Extended Rule 0373: Anomaly signature 373",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 70000 AND account_age_days < 18",
        weight=53,
        description="Automated financial surveillance rule 0373 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0374",
        name="Extended Rule 0374: Anomaly signature 374",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 75000 AND account_age_days < 19",
        weight=54,
        description="Automated financial surveillance rule 0374 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0375",
        name="Extended Rule 0375: Anomaly signature 375",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 80000 AND account_age_days < 20",
        weight=55,
        description="Automated financial surveillance rule 0375 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0376",
        name="Extended Rule 0376: Anomaly signature 376",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 85000 AND account_age_days < 21",
        weight=56,
        description="Automated financial surveillance rule 0376 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0377",
        name="Extended Rule 0377: Anomaly signature 377",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 90000 AND account_age_days < 22",
        weight=57,
        description="Automated financial surveillance rule 0377 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0378",
        name="Extended Rule 0378: Anomaly signature 378",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 95000 AND account_age_days < 23",
        weight=58,
        description="Automated financial surveillance rule 0378 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0379",
        name="Extended Rule 0379: Anomaly signature 379",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 100000 AND account_age_days < 24",
        weight=59,
        description="Automated financial surveillance rule 0379 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0380",
        name="Extended Rule 0380: Anomaly signature 380",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 5000 AND account_age_days < 25",
        weight=60,
        description="Automated financial surveillance rule 0380 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0381",
        name="Extended Rule 0381: Anomaly signature 381",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 10000 AND account_age_days < 26",
        weight=61,
        description="Automated financial surveillance rule 0381 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0382",
        name="Extended Rule 0382: Anomaly signature 382",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 15000 AND account_age_days < 27",
        weight=62,
        description="Automated financial surveillance rule 0382 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0383",
        name="Extended Rule 0383: Anomaly signature 383",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 20000 AND account_age_days < 28",
        weight=63,
        description="Automated financial surveillance rule 0383 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0384",
        name="Extended Rule 0384: Anomaly signature 384",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 25000 AND account_age_days < 29",
        weight=64,
        description="Automated financial surveillance rule 0384 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0385",
        name="Extended Rule 0385: Anomaly signature 385",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 30000 AND account_age_days < 30",
        weight=65,
        description="Automated financial surveillance rule 0385 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0386",
        name="Extended Rule 0386: Anomaly signature 386",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 35000 AND account_age_days < 31",
        weight=66,
        description="Automated financial surveillance rule 0386 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0387",
        name="Extended Rule 0387: Anomaly signature 387",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 40000 AND account_age_days < 32",
        weight=67,
        description="Automated financial surveillance rule 0387 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0388",
        name="Extended Rule 0388: Anomaly signature 388",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 45000 AND account_age_days < 33",
        weight=68,
        description="Automated financial surveillance rule 0388 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0389",
        name="Extended Rule 0389: Anomaly signature 389",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 50000 AND account_age_days < 34",
        weight=69,
        description="Automated financial surveillance rule 0389 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0390",
        name="Extended Rule 0390: Anomaly signature 390",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 55000 AND account_age_days < 35",
        weight=70,
        description="Automated financial surveillance rule 0390 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0391",
        name="Extended Rule 0391: Anomaly signature 391",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 60000 AND account_age_days < 36",
        weight=71,
        description="Automated financial surveillance rule 0391 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0392",
        name="Extended Rule 0392: Anomaly signature 392",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 65000 AND account_age_days < 37",
        weight=72,
        description="Automated financial surveillance rule 0392 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0393",
        name="Extended Rule 0393: Anomaly signature 393",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 70000 AND account_age_days < 38",
        weight=73,
        description="Automated financial surveillance rule 0393 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0394",
        name="Extended Rule 0394: Anomaly signature 394",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.MEDIUM,
        expression="amount > 75000 AND account_age_days < 39",
        weight=74,
        description="Automated financial surveillance rule 0394 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0395",
        name="Extended Rule 0395: Anomaly signature 395",
        category=RuleCategory.GEO_ANOMALY,
        severity=RuleSeverity.HIGH,
        expression="amount > 80000 AND account_age_days < 40",
        weight=75,
        description="Automated financial surveillance rule 0395 monitoring GEO_ANOMALY across payment streams.",
        tags=["extended", "geo_anomaly"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0396",
        name="Extended Rule 0396: Anomaly signature 396",
        category=RuleCategory.CARD_FRAUD,
        severity=RuleSeverity.HIGH,
        expression="amount > 85000 AND account_age_days < 41",
        weight=76,
        description="Automated financial surveillance rule 0396 monitoring CARD_FRAUD across payment streams.",
        tags=["extended", "card_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0397",
        name="Extended Rule 0397: Anomaly signature 397",
        category=RuleCategory.WIRE_FRAUD,
        severity=RuleSeverity.HIGH,
        expression="amount > 90000 AND account_age_days < 42",
        weight=77,
        description="Automated financial surveillance rule 0397 monitoring WIRE_FRAUD across payment streams.",
        tags=["extended", "wire_fraud"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0398",
        name="Extended Rule 0398: Anomaly signature 398",
        category=RuleCategory.ACCOUNT_TAKEOVER,
        severity=RuleSeverity.HIGH,
        expression="amount > 95000 AND account_age_days < 43",
        weight=78,
        description="Automated financial surveillance rule 0398 monitoring ACCOUNT_TAKEOVER across payment streams.",
        tags=["extended", "account_takeover"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0399",
        name="Extended Rule 0399: Anomaly signature 399",
        category=RuleCategory.AML_STRUCTURING,
        severity=RuleSeverity.HIGH,
        expression="amount > 100000 AND account_age_days < 44",
        weight=79,
        description="Automated financial surveillance rule 0399 monitoring AML_STRUCTURING across payment streams.",
        tags=["extended", "aml_structuring"]
    ))
    catalog.register(FraudRule(
        rule_id="R_EXT_0400",
        name="Extended Rule 0400: Anomaly signature 400",
        category=RuleCategory.VELOCITY_ABUSE,
        severity=RuleSeverity.HIGH,
        expression="amount > 5000 AND account_age_days < 45",
        weight=80,
        description="Automated financial surveillance rule 0400 monitoring VELOCITY_ABUSE across payment streams.",
        tags=["extended", "velocity_abuse"]
    ))

register_extended_rules()

class RulePartitionEvaluator_1:
    """Partition worker 1 evaluating extended rule chunk."""
    def __init__(self):
        self.chunk_id = 1
    def evaluate_chunk(self, tx: Dict[str, Any]) -> int:
        return 1 if float(tx.get("amount", 0)) > 10000 else 0

class RulePartitionEvaluator_2:
    """Partition worker 2 evaluating extended rule chunk."""
    def __init__(self):
        self.chunk_id = 2
    def evaluate_chunk(self, tx: Dict[str, Any]) -> int:
        return 1 if float(tx.get("amount", 0)) > 20000 else 0

class RulePartitionEvaluator_3:
    """Partition worker 3 evaluating extended rule chunk."""
    def __init__(self):
        self.chunk_id = 3
    def evaluate_chunk(self, tx: Dict[str, Any]) -> int:
        return 1 if float(tx.get("amount", 0)) > 30000 else 0

class RulePartitionEvaluator_4:
    """Partition worker 4 evaluating extended rule chunk."""
    def __init__(self):
        self.chunk_id = 4
    def evaluate_chunk(self, tx: Dict[str, Any]) -> int:
        return 1 if float(tx.get("amount", 0)) > 40000 else 0

class RulePartitionEvaluator_5:
    """Partition worker 5 evaluating extended rule chunk."""
    def __init__(self):
        self.chunk_id = 5
    def evaluate_chunk(self, tx: Dict[str, Any]) -> int:
        return 1 if float(tx.get("amount", 0)) > 50000 else 0

class RulePartitionEvaluator_6:
    """Partition worker 6 evaluating extended rule chunk."""
    def __init__(self):
        self.chunk_id = 6
    def evaluate_chunk(self, tx: Dict[str, Any]) -> int:
        return 1 if float(tx.get("amount", 0)) > 60000 else 0

class RulePartitionEvaluator_7:
    """Partition worker 7 evaluating extended rule chunk."""
    def __init__(self):
        self.chunk_id = 7
    def evaluate_chunk(self, tx: Dict[str, Any]) -> int:
        return 1 if float(tx.get("amount", 0)) > 70000 else 0

class RulePartitionEvaluator_8:
    """Partition worker 8 evaluating extended rule chunk."""
    def __init__(self):
        self.chunk_id = 8
    def evaluate_chunk(self, tx: Dict[str, Any]) -> int:
        return 1 if float(tx.get("amount", 0)) > 80000 else 0

class RulePartitionEvaluator_9:
    """Partition worker 9 evaluating extended rule chunk."""
    def __init__(self):
        self.chunk_id = 9
    def evaluate_chunk(self, tx: Dict[str, Any]) -> int:
        return 1 if float(tx.get("amount", 0)) > 90000 else 0

class RulePartitionEvaluator_10:
    """Partition worker 10 evaluating extended rule chunk."""
    def __init__(self):
        self.chunk_id = 10
    def evaluate_chunk(self, tx: Dict[str, Any]) -> int:
        return 1 if float(tx.get("amount", 0)) > 100000 else 0

class RulePartitionEvaluator_11:
    """Partition worker 11 evaluating extended rule chunk."""
    def __init__(self):
        self.chunk_id = 11
    def evaluate_chunk(self, tx: Dict[str, Any]) -> int:
        return 1 if float(tx.get("amount", 0)) > 110000 else 0

class RulePartitionEvaluator_12:
    """Partition worker 12 evaluating extended rule chunk."""
    def __init__(self):
        self.chunk_id = 12
    def evaluate_chunk(self, tx: Dict[str, Any]) -> int:
        return 1 if float(tx.get("amount", 0)) > 120000 else 0

class RulePartitionEvaluator_13:
    """Partition worker 13 evaluating extended rule chunk."""
    def __init__(self):
        self.chunk_id = 13
    def evaluate_chunk(self, tx: Dict[str, Any]) -> int:
        return 1 if float(tx.get("amount", 0)) > 130000 else 0

class RulePartitionEvaluator_14:
    """Partition worker 14 evaluating extended rule chunk."""
    def __init__(self):
        self.chunk_id = 14
    def evaluate_chunk(self, tx: Dict[str, Any]) -> int:
        return 1 if float(tx.get("amount", 0)) > 140000 else 0

class RulePartitionEvaluator_15:
    """Partition worker 15 evaluating extended rule chunk."""
    def __init__(self):
        self.chunk_id = 15
    def evaluate_chunk(self, tx: Dict[str, Any]) -> int:
        return 1 if float(tx.get("amount", 0)) > 150000 else 0

class RulePartitionEvaluator_16:
    """Partition worker 16 evaluating extended rule chunk."""
    def __init__(self):
        self.chunk_id = 16
    def evaluate_chunk(self, tx: Dict[str, Any]) -> int:
        return 1 if float(tx.get("amount", 0)) > 160000 else 0

class RulePartitionEvaluator_17:
    """Partition worker 17 evaluating extended rule chunk."""
    def __init__(self):
        self.chunk_id = 17
    def evaluate_chunk(self, tx: Dict[str, Any]) -> int:
        return 1 if float(tx.get("amount", 0)) > 170000 else 0

class RulePartitionEvaluator_18:
    """Partition worker 18 evaluating extended rule chunk."""
    def __init__(self):
        self.chunk_id = 18
    def evaluate_chunk(self, tx: Dict[str, Any]) -> int:
        return 1 if float(tx.get("amount", 0)) > 180000 else 0

class RulePartitionEvaluator_19:
    """Partition worker 19 evaluating extended rule chunk."""
    def __init__(self):
        self.chunk_id = 19
    def evaluate_chunk(self, tx: Dict[str, Any]) -> int:
        return 1 if float(tx.get("amount", 0)) > 190000 else 0