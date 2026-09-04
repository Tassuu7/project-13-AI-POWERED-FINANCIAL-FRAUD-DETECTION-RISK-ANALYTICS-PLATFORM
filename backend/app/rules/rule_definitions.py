"""
Aegis Fraud Labs – Master Financial Fraud Detection Rule Definitions
Contains 150+ categorized deterministic and heuristic rules with weights and condition trees.
"""
from typing import Dict, List, Any, Optional, Set
from dataclasses import dataclass, field
from enum import Enum

class RuleCategory(Enum):
    CARD_FRAUD = "CARD_FRAUD"
    ACCOUNT_TAKEOVER = "ACCOUNT_TAKEOVER"
    WIRE_FRAUD = "WIRE_FRAUD"
    AML_STRUCTURING = "AML_STRUCTURING"
    VELOCITY_ABUSE = "VELOCITY_ABUSE"
    GEO_ANOMALY = "GEO_ANOMALY"
    DEVICE_SPOOFING = "DEVICE_SPOOFING"
    BEHAVIORAL_ANOMALY = "BEHAVIORAL_ANOMALY"
    MERCHANT_RISK = "MERCHANT_RISK"
    MULE_ACCOUNT = "MULE_ACCOUNT"
    SYNTHETIC_IDENTITY = "SYNTHETIC_IDENTITY"
    CRYPTO_EXIT = "CRYPTO_EXIT"

class RuleSeverity(Enum):
    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    INFO = "INFO"

@dataclass
class FraudRule:
    rule_id: str
    name: str
    category: RuleCategory
    severity: RuleSeverity
    expression: str
    weight: int
    description: str
    tags: List[str] = field(default_factory=list)
    enabled: bool = True

class RuleDefinitionCatalog:
    def __init__(self):
        self.rules: Dict[str, FraudRule] = {}
        self._init_catalog()

    def register(self, rule: FraudRule):
        self.rules[rule.rule_id] = rule

    def get(self, rule_id: str) -> Optional[FraudRule]:
        return self.rules.get(rule_id)

    def get_by_category(self, cat: RuleCategory) -> List[FraudRule]:
        return [r for r in self.rules.values() if r.category == cat and r.enabled]

    def _init_catalog(self):
        # --- Category: Card Fraud ---
        self.register(FraudRule(
            rule_id="R-0001",
            name="R-0001: High value card not present transaction",
            category=RuleCategory.CARD_FRAUD,
            severity=RuleSeverity.HIGH,
            expression="amount > 100000 AND card_present == False",
            weight=85,
            description="High value card not present transaction",
            tags=['card_fraud', 'risk_weight_85']
        ))
        self.register(FraudRule(
            rule_id="R-0002",
            name="R-0002: Cross-border high value authorization",
            category=RuleCategory.CARD_FRAUD,
            severity=RuleSeverity.MEDIUM,
            expression="is_international == True AND amount > 50000",
            weight=75,
            description="Cross-border high value authorization",
            tags=['card_fraud', 'risk_weight_75']
        ))
        self.register(FraudRule(
            rule_id="R-0003",
            name="R-0003: Brute-force CVV verification failure",
            category=RuleCategory.CARD_FRAUD,
            severity=RuleSeverity.HIGH,
            expression="failed_cvv_attempts >= 3",
            weight=90,
            description="Brute-force CVV verification failure",
            tags=['card_fraud', 'risk_weight_90']
        ))
        self.register(FraudRule(
            rule_id="R-0004",
            name="R-0004: Newly issued card high velocity spend",
            category=RuleCategory.CARD_FRAUD,
            severity=RuleSeverity.MEDIUM,
            expression="card_age_days < 7 AND amount > 25000",
            weight=70,
            description="Newly issued card high velocity spend",
            tags=['card_fraud', 'risk_weight_70']
        ))
        self.register(FraudRule(
            rule_id="R-0005",
            name="R-0005: Distant ATM withdrawal with elevated amount",
            category=RuleCategory.CARD_FRAUD,
            severity=RuleSeverity.HIGH,
            expression="transaction_type == 'ATM' AND amount > 40000 AND distance_km > 100",
            weight=80,
            description="Distant ATM withdrawal with elevated amount",
            tags=['card_fraud', 'risk_weight_80']
        ))
        self.register(FraudRule(
            rule_id="R-0006",
            name="R-0006: Chip fallback to magnetic stripe",
            category=RuleCategory.CARD_FRAUD,
            severity=RuleSeverity.MEDIUM,
            expression="pos_entry_mode == 'FALLBACK_MAGSTRIPE' AND amount > 15000",
            weight=65,
            description="Chip fallback to magnetic stripe",
            tags=['card_fraud', 'risk_weight_65']
        ))
        self.register(FraudRule(
            rule_id="R-0007",
            name="R-0007: High-liquidity merchant categories spend spike",
            category=RuleCategory.CARD_FRAUD,
            severity=RuleSeverity.HIGH,
            expression="merchant_category IN ['Jewelry', 'Electronics', 'GiftCards'] AND amount > 75000",
            weight=85,
            description="High-liquidity merchant categories spend spike",
            tags=['card_fraud', 'risk_weight_85']
        ))
        self.register(FraudRule(
            rule_id="R-0008",
            name="R-0008: Repeat chargeback history on card token",
            category=RuleCategory.CARD_FRAUD,
            severity=RuleSeverity.HIGH,
            expression="previous_fraud_chargeback_count > 0 AND amount > 10000",
            weight=80,
            description="Repeat chargeback history on card token",
            tags=['card_fraud', 'risk_weight_80']
        ))
        self.register(FraudRule(
            rule_id="R-0009",
            name="R-0009: AVS billing and shipping postal mismatch",
            category=RuleCategory.CARD_FRAUD,
            severity=RuleSeverity.LOW,
            expression="billing_postal_code != shipping_postal_code AND amount > 30000",
            weight=60,
            description="AVS billing and shipping postal mismatch",
            tags=['card_fraud', 'risk_weight_60']
        ))
        self.register(FraudRule(
            rule_id="R-0010",
            name="R-0010: Card rapid replay velocity across terminals",
            category=RuleCategory.CARD_FRAUD,
            severity=RuleSeverity.HIGH,
            expression="card_hash_velocity_1h >= 5",
            weight=85,
            description="Card rapid replay velocity across terminals",
            tags=['card_fraud', 'risk_weight_85']
        ))
        self.register(FraudRule(
            rule_id="R-0011",
            name="R-0011: Disposable virtual card large authorization",
            category=RuleCategory.CARD_FRAUD,
            severity=RuleSeverity.MEDIUM,
            expression="is_virtual_card == True AND amount > 80000",
            weight=70,
            description="Disposable virtual card large authorization",
            tags=['card_fraud', 'risk_weight_70']
        ))
        self.register(FraudRule(
            rule_id="R-0012",
            name="R-0012: Repeated authorization attempts post issuer referral",
            category=RuleCategory.CARD_FRAUD,
            severity=RuleSeverity.MEDIUM,
            expression="authorization_response_code == 'CALL_ISSUER' AND retry_count >= 2",
            weight=75,
            description="Repeated authorization attempts post issuer referral",
            tags=['card_fraud', 'risk_weight_75']
        ))
        self.register(FraudRule(
            rule_id="R-0013",
            name="R-0013: Foreign terminal authorization without travel alert",
            category=RuleCategory.CARD_FRAUD,
            severity=RuleSeverity.HIGH,
            expression="terminal_country != card_issuing_country AND amount > 60000",
            weight=80,
            description="Foreign terminal authorization without travel alert",
            tags=['card_fraud', 'risk_weight_80']
        ))
        self.register(FraudRule(
            rule_id="R-0014",
            name="R-0014: Single transaction consuming >90% of daily credit limit",
            category=RuleCategory.CARD_FRAUD,
            severity=RuleSeverity.HIGH,
            expression="daily_spend_percentage > 90 AND amount > 50000",
            weight=85,
            description="Single transaction consuming >90% of daily credit limit",
            tags=['card_fraud', 'risk_weight_85']
        ))
        self.register(FraudRule(
            rule_id="R-0015",
            name="R-0015: Repeated authorization reversal anomalies",
            category=RuleCategory.CARD_FRAUD,
            severity=RuleSeverity.MEDIUM,
            expression="reversal_attempt_count >= 2",
            weight=70,
            description="Repeated authorization reversal anomalies",
            tags=['card_fraud', 'risk_weight_70']
        ))
        self.register(FraudRule(
            rule_id="R-0016",
            name="R-0016: Gambling and crypto onramp card spending",
            category=RuleCategory.CARD_FRAUD,
            severity=RuleSeverity.HIGH,
            expression="merchant_id IN ['HIGH_RISK_MCC_7995', 'HIGH_RISK_MCC_6051'] AND amount > 35000",
            weight=90,
            description="Gambling and crypto onramp card spending",
            tags=['card_fraud', 'risk_weight_90']
        ))
        self.register(FraudRule(
            rule_id="R-0017",
            name="R-0017: Cardholder name mismatch against KYC registry",
            category=RuleCategory.CARD_FRAUD,
            severity=RuleSeverity.MEDIUM,
            expression="cardholder_name_similarity < 0.4",
            weight=65,
            description="Cardholder name mismatch against KYC registry",
            tags=['card_fraud', 'risk_weight_65']
        ))
        self.register(FraudRule(
            rule_id="R-0018",
            name="R-0018: Consecutive contactless transactions bypassing PIN",
            category=RuleCategory.CARD_FRAUD,
            severity=RuleSeverity.LOW,
            expression="contactless_limit_exceeded == True",
            weight=55,
            description="Consecutive contactless transactions bypassing PIN",
            tags=['card_fraud', 'risk_weight_55']
        ))
        self.register(FraudRule(
            rule_id="R-0019",
            name="R-0019: Terminal latitude/longitude mismatch from merchant base",
            category=RuleCategory.CARD_FRAUD,
            severity=RuleSeverity.HIGH,
            expression="pos_geo_lat_diff > 5.0 OR pos_geo_lon_diff > 5.0",
            weight=80,
            description="Terminal latitude/longitude mismatch from merchant base",
            tags=['card_fraud', 'risk_weight_80']
        ))
        self.register(FraudRule(
            rule_id="R-0020",
            name="R-0020: Mobile wallet newly provisioned card rapid burn",
            category=RuleCategory.CARD_FRAUD,
            severity=RuleSeverity.HIGH,
            expression="card_token_provisioned_hours < 24 AND amount > 45000",
            weight=85,
            description="Mobile wallet newly provisioned card rapid burn",
            tags=['card_fraud', 'risk_weight_85']
        ))

        # --- Category: Account Takeover ---
        self.register(FraudRule(
            rule_id="R-0021",
            name="R-0021: Immediate large transfer following credentials reset",
            category=RuleCategory.ACCOUNT_TAKEOVER,
            severity=RuleSeverity.CRITICAL,
            expression="password_reset_hours < 2 AND amount > 20000",
            weight=95,
            description="Immediate large transfer following credentials reset",
            tags=['account_takeover', 'risk_weight_95']
        ))
        self.register(FraudRule(
            rule_id="R-0022",
            name="R-0022: Transfer from unrecognized device post email change",
            category=RuleCategory.ACCOUNT_TAKEOVER,
            severity=RuleSeverity.HIGH,
            expression="new_device_login == True AND email_changed_hours < 24",
            weight=90,
            description="Transfer from unrecognized device post email change",
            tags=['account_takeover', 'risk_weight_90']
        ))
        self.register(FraudRule(
            rule_id="R-0023",
            name="R-0023: MFA bypass or push fatigue exploit detected",
            category=RuleCategory.ACCOUNT_TAKEOVER,
            severity=RuleSeverity.CRITICAL,
            expression="mfa_bypass_attempted == True",
            weight=100,
            description="MFA bypass or push fatigue exploit detected",
            tags=['account_takeover', 'risk_weight_100']
        ))
        self.register(FraudRule(
            rule_id="R-0024",
            name="R-0024: Telco SIM swap notification within 48h of transfer",
            category=RuleCategory.ACCOUNT_TAKEOVER,
            severity=RuleSeverity.CRITICAL,
            expression="sim_swap_detected_hours < 48 AND amount > 10000",
            weight=95,
            description="Telco SIM swap notification within 48h of transfer",
            tags=['account_takeover', 'risk_weight_95']
        ))
        self.register(FraudRule(
            rule_id="R-0025",
            name="R-0025: ASN routing change combined with newly registered payee",
            category=RuleCategory.ACCOUNT_TAKEOVER,
            severity=RuleSeverity.HIGH,
            expression="session_ip_asn_changed == True AND is_beneficiary_new == True",
            weight=85,
            description="ASN routing change combined with newly registered payee",
            tags=['account_takeover', 'risk_weight_85']
        ))
        self.register(FraudRule(
            rule_id="R-0026",
            name="R-0026: Operating system platform change during high-value session",
            category=RuleCategory.ACCOUNT_TAKEOVER,
            severity=RuleSeverity.MEDIUM,
            expression="user_agent_os_changed == True AND amount > 30000",
            weight=75,
            description="Operating system platform change during high-value session",
            tags=['account_takeover', 'risk_weight_75']
        ))
        self.register(FraudRule(
            rule_id="R-0027",
            name="R-0027: Credential stuffing pattern followed by immediate payout",
            category=RuleCategory.ACCOUNT_TAKEOVER,
            severity=RuleSeverity.HIGH,
            expression="login_failed_attempts >= 5 AND login_success_hours < 1",
            weight=85,
            description="Credential stuffing pattern followed by immediate payout",
            tags=['account_takeover', 'risk_weight_85']
        ))
        self.register(FraudRule(
            rule_id="R-0028",
            name="R-0028: Rapid cooling-off bypass on beneficiary addition",
            category=RuleCategory.ACCOUNT_TAKEOVER,
            severity=RuleSeverity.HIGH,
            expression="beneficiary_added_minutes < 15 AND amount > 50000",
            weight=90,
            description="Rapid cooling-off bypass on beneficiary addition",
            tags=['account_takeover', 'risk_weight_90']
        ))
        self.register(FraudRule(
            rule_id="R-0029",
            name="R-0029: AnyDesk / TeamViewer active during banking session",
            category=RuleCategory.ACCOUNT_TAKEOVER,
            severity=RuleSeverity.CRITICAL,
            expression="remote_access_tool_detected == True",
            weight=95,
            description="AnyDesk / TeamViewer active during banking session",
            tags=['account_takeover', 'risk_weight_95']
        ))
        self.register(FraudRule(
            rule_id="R-0030",
            name="R-0030: Account number pasted from clipboard without manual entry",
            category=RuleCategory.ACCOUNT_TAKEOVER,
            severity=RuleSeverity.MEDIUM,
            expression="clipboard_pasted_account == True AND amount > 25000",
            weight=65,
            description="Account number pasted from clipboard without manual entry",
            tags=['account_takeover', 'risk_weight_65']
        ))
        self.register(FraudRule(
            rule_id="R-0031",
            name="R-0031: Device system timezone conflicts with IP geolocation",
            category=RuleCategory.ACCOUNT_TAKEOVER,
            severity=RuleSeverity.MEDIUM,
            expression="browser_timezone_mismatch == True AND amount > 40000",
            weight=70,
            description="Device system timezone conflicts with IP geolocation",
            tags=['account_takeover', 'risk_weight_70']
        ))
        self.register(FraudRule(
            rule_id="R-0032",
            name="R-0032: Security profile phone number modification preceding payout",
            category=RuleCategory.ACCOUNT_TAKEOVER,
            severity=RuleSeverity.HIGH,
            expression="profile_phone_updated_hours < 12 AND amount > 15000",
            weight=85,
            description="Security profile phone number modification preceding payout",
            tags=['account_takeover', 'risk_weight_85']
        ))
        self.register(FraudRule(
            rule_id="R-0033",
            name="R-0033: Rooted mobile device executing financial operations",
            category=RuleCategory.ACCOUNT_TAKEOVER,
            severity=RuleSeverity.HIGH,
            expression="device_rooted_or_jailbroken == True AND amount > 20000",
            weight=80,
            description="Rooted mobile device executing financial operations",
            tags=['account_takeover', 'risk_weight_80']
        ))
        self.register(FraudRule(
            rule_id="R-0034",
            name="R-0034: FaceID/Fingerprint biometric fallback to PIN exploit",
            category=RuleCategory.ACCOUNT_TAKEOVER,
            severity=RuleSeverity.HIGH,
            expression="biometric_auth_failed_count >= 3",
            weight=85,
            description="FaceID/Fingerprint biometric fallback to PIN exploit",
            tags=['account_takeover', 'risk_weight_85']
        ))
        self.register(FraudRule(
            rule_id="R-0035",
            name="R-0035: Concurrent active sessions from geographically disparate IPs",
            category=RuleCategory.ACCOUNT_TAKEOVER,
            severity=RuleSeverity.HIGH,
            expression="concurrent_active_sessions > 1 AND amount > 35000",
            weight=80,
            description="Concurrent active sessions from geographically disparate IPs",
            tags=['account_takeover', 'risk_weight_80']
        ))

        # --- Category: Wire & High Value Payout ---
        self.register(FraudRule(
            rule_id="R-0036",
            name="R-0036: Inaugural wire exceeding ₹5,00,000 threshold",
            category=RuleCategory.WIRE_FRAUD,
            severity=RuleSeverity.CRITICAL,
            expression="amount > 500000 AND is_first_wire == True",
            weight=95,
            description="Inaugural wire exceeding ₹5,00,000 threshold",
            tags=['wire_fraud', 'risk_weight_95']
        ))
        self.register(FraudRule(
            rule_id="R-0037",
            name="R-0037: Wire to high-risk offshore jurisdiction",
            category=RuleCategory.WIRE_FRAUD,
            severity=RuleSeverity.HIGH,
            expression="beneficiary_country IN ['CY', 'SC', 'PA', 'VUT'] AND amount > 200000",
            weight=90,
            description="Wire to high-risk offshore jurisdiction",
            tags=['wire_fraud', 'risk_weight_90']
        ))
        self.register(FraudRule(
            rule_id="R-0038",
            name="R-0038: Weekend wire urgency override indicator",
            category=RuleCategory.WIRE_FRAUD,
            severity=RuleSeverity.HIGH,
            expression="urgent_flag == True AND weekend_wire == True AND amount > 150000",
            weight=85,
            description="Weekend wire urgency override indicator",
            tags=['wire_fraud', 'risk_weight_85']
        ))
        self.register(FraudRule(
            rule_id="R-0039",
            name="R-0039: Direct settlement wire lacking intermediary clearing",
            category=RuleCategory.WIRE_FRAUD,
            severity=RuleSeverity.MEDIUM,
            expression="intermediary_bank_missing == True AND amount > 300000",
            weight=70,
            description="Direct settlement wire lacking intermediary clearing",
            tags=['wire_fraud', 'risk_weight_70']
        ))
        self.register(FraudRule(
            rule_id="R-0040",
            name="R-0040: Commercial treasury payout triggered outside business hours",
            category=RuleCategory.WIRE_FRAUD,
            severity=RuleSeverity.MEDIUM,
            expression="corporate_wire_outside_operating_hours == True",
            weight=75,
            description="Commercial treasury payout triggered outside business hours",
            tags=['wire_fraud', 'risk_weight_75']
        ))
        self.register(FraudRule(
            rule_id="R-0041",
            name="R-0041: Wire directed to newly instantiated beneficiary ledger",
            category=RuleCategory.WIRE_FRAUD,
            severity=RuleSeverity.CRITICAL,
            expression="beneficiary_account_age_days < 3 AND amount > 250000",
            weight=95,
            description="Wire directed to newly instantiated beneficiary ledger",
            tags=['wire_fraud', 'risk_weight_95']
        ))
        self.register(FraudRule(
            rule_id="R-0042",
            name="R-0042: SWIFT BIC code matched against international sanction list",
            category=RuleCategory.WIRE_FRAUD,
            severity=RuleSeverity.CRITICAL,
            expression="swift_bic_sanction_match == True",
            weight=100,
            description="SWIFT BIC code matched against international sanction list",
            tags=['wire_fraud', 'risk_weight_100']
        ))
        self.register(FraudRule(
            rule_id="R-0043",
            name="R-0043: Business Email Compromise (BEC) fraudulent invoice wire",
            category=RuleCategory.WIRE_FRAUD,
            severity=RuleSeverity.HIGH,
            expression="memo_contains_invoice_keywords == True AND vendor_verified == False",
            weight=85,
            description="Business Email Compromise (BEC) fraudulent invoice wire",
            tags=['wire_fraud', 'risk_weight_85']
        ))
        self.register(FraudRule(
            rule_id="R-0044",
            name="R-0044: Consecutive wires splitting large corporate sum",
            category=RuleCategory.WIRE_FRAUD,
            severity=RuleSeverity.HIGH,
            expression="split_wire_detected == True AND combined_amount > 400000",
            weight=90,
            description="Consecutive wires splitting large corporate sum",
            tags=['wire_fraud', 'risk_weight_90']
        ))
        self.register(FraudRule(
            rule_id="R-0045",
            name="R-0045: Dual control authorization bypassed on manual wire entry",
            category=RuleCategory.WIRE_FRAUD,
            severity=RuleSeverity.CRITICAL,
            expression="manual_wire_entry_override == True AND dual_auth_missing == True",
            weight=95,
            description="Dual control authorization bypassed on manual wire entry",
            tags=['wire_fraud', 'risk_weight_95']
        ))
        self.register(FraudRule(
            rule_id="R-0046",
            name="R-0046: BEN fee allocation indicator on high-risk transfer",
            category=RuleCategory.WIRE_FRAUD,
            severity=RuleSeverity.MEDIUM,
            expression="wire_fee_borne_by_beneficiary == True AND amount > 100000",
            weight=65,
            description="BEN fee allocation indicator on high-risk transfer",
            tags=['wire_fraud', 'risk_weight_65']
        ))
        self.register(FraudRule(
            rule_id="R-0047",
            name="R-0047: Follow-up wire following recent clearing recall attempt",
            category=RuleCategory.WIRE_FRAUD,
            severity=RuleSeverity.HIGH,
            expression="wire_reversal_prior_24h == True",
            weight=80,
            description="Follow-up wire following recent clearing recall attempt",
            tags=['wire_fraud', 'risk_weight_80']
        ))
        self.register(FraudRule(
            rule_id="R-0048",
            name="R-0048: IBAN bank code country differs from beneficiary declared residency",
            category=RuleCategory.WIRE_FRAUD,
            severity=RuleSeverity.HIGH,
            expression="beneficiary_iban_country_mismatch == True",
            weight=85,
            description="IBAN bank code country differs from beneficiary declared residency",
            tags=['wire_fraud', 'risk_weight_85']
        ))
        self.register(FraudRule(
            rule_id="R-0049",
            name="R-0049: Wire magnitude exceeds 500% of historical average wire size",
            category=RuleCategory.WIRE_FRAUD,
            severity=RuleSeverity.HIGH,
            expression="wire_amount_variance_from_history > 500.0",
            weight=85,
            description="Wire magnitude exceeds 500% of historical average wire size",
            tags=['wire_fraud', 'risk_weight_85']
        ))
        self.register(FraudRule(
            rule_id="R-0050",
            name="R-0050: Heuristic NLP match for CEO fraud / wire directive memo",
            category=RuleCategory.WIRE_FRAUD,
            severity=RuleSeverity.CRITICAL,
            expression="executive_impersonation_score > 0.85",
            weight=95,
            description="Heuristic NLP match for CEO fraud / wire directive memo",
            tags=['wire_fraud', 'risk_weight_95']
        ))

        # --- Category: AML & Structuring / Smurfing ---
        self.register(FraudRule(
            rule_id="R-0051",
            name="R-0051: Threshold structuring intentionally hovering under $10,000 / ₹10L CTR limit",
            category=RuleCategory.AML_STRUCTURING,
            severity=RuleSeverity.CRITICAL,
            expression="amount >= 9500 AND amount <= 9999",
            weight=95,
            description="Threshold structuring intentionally hovering under $10,000 / ₹10L CTR limit",
            tags=['aml_structuring', 'risk_weight_95']
        ))
        self.register(FraudRule(
            rule_id="R-0052",
            name="R-0052: Exceeded statutory Currency Transaction Reporting threshold",
            category=RuleCategory.AML_STRUCTURING,
            severity=RuleSeverity.HIGH,
            expression="daily_cash_aggregate > 1000000",
            weight=90,
            description="Exceeded statutory Currency Transaction Reporting threshold",
            tags=['aml_structuring', 'risk_weight_90']
        ))
        self.register(FraudRule(
            rule_id="R-0053",
            name="R-0053: Multi-branch smurfing pattern of consecutive sub-limit deposits",
            category=RuleCategory.AML_STRUCTURING,
            severity=RuleSeverity.CRITICAL,
            expression="consecutive_sub_threshold_transfers >= 3",
            weight=95,
            description="Multi-branch smurfing pattern of consecutive sub-limit deposits",
            tags=['aml_structuring', 'risk_weight_95']
        ))
        self.register(FraudRule(
            rule_id="R-0054",
            name="R-0054: Pass-through account: funds withdrawn immediately post deposit",
            category=RuleCategory.AML_STRUCTURING,
            severity=RuleSeverity.HIGH,
            expression="rapid_pass_through_ratio > 0.95",
            weight=90,
            description="Pass-through account: funds withdrawn immediately post deposit",
            tags=['aml_structuring', 'risk_weight_90']
        ))
        self.register(FraudRule(
            rule_id="R-0055",
            name="R-0055: Clean round-number structuring transactions",
            category=RuleCategory.AML_STRUCTURING,
            severity=RuleSeverity.LOW,
            expression="round_number_amount == True AND amount > 50000",
            weight=60,
            description="Clean round-number structuring transactions",
            tags=['aml_structuring', 'risk_weight_60']
        ))
        self.register(FraudRule(
            rule_id="R-0056",
            name="R-0056: Rapid cash layering via ATM network",
            category=RuleCategory.AML_STRUCTURING,
            severity=RuleSeverity.HIGH,
            expression="cash_deposit_to_atm_transfer_minutes < 10",
            weight=85,
            description="Rapid cash layering via ATM network",
            tags=['aml_structuring', 'risk_weight_85']
        ))
        self.register(FraudRule(
            rule_id="R-0057",
            name="R-0057: Funnel account: numerous micro inbound transfers from disparate parties",
            category=RuleCategory.AML_STRUCTURING,
            severity=RuleSeverity.HIGH,
            expression="peer_to_peer_inbound_count_24h >= 10",
            weight=80,
            description="Funnel account: numerous micro inbound transfers from disparate parties",
            tags=['aml_structuring', 'risk_weight_80']
        ))
        self.register(FraudRule(
            rule_id="R-0058",
            name="R-0058: Missing KYC source of wealth declarations on large flow",
            category=RuleCategory.AML_STRUCTURING,
            severity=RuleSeverity.HIGH,
            expression="source_of_funds_undisclosed == True AND amount > 100000",
            weight=85,
            description="Missing KYC source of wealth declarations on large flow",
            tags=['aml_structuring', 'risk_weight_85']
        ))
        self.register(FraudRule(
            rule_id="R-0059",
            name="R-0059: Politically Exposed Person (PEP) high-volume financial routing",
            category=RuleCategory.AML_STRUCTURING,
            severity=RuleSeverity.HIGH,
            expression="pep_exposure_flag == True AND amount > 100000",
            weight=90,
            description="Politically Exposed Person (PEP) high-volume financial routing",
            tags=['aml_structuring', 'risk_weight_90']
        ))
        self.register(FraudRule(
            rule_id="R-0060",
            name="R-0060: Mule hub: consolidated payout from distributed remitters",
            category=RuleCategory.AML_STRUCTURING,
            severity=RuleSeverity.HIGH,
            expression="multiple_remitters_single_beneficiary_24h >= 5",
            weight=90,
            description="Mule hub: consolidated payout from distributed remitters",
            tags=['aml_structuring', 'risk_weight_90']
        ))
        self.register(FraudRule(
            rule_id="R-0061",
            name="R-0061: Cross-border layering through transit hub",
            category=RuleCategory.AML_STRUCTURING,
            severity=RuleSeverity.CRITICAL,
            expression="high_risk_jurisdiction_inbound == True AND rapid_outbound == True",
            weight=95,
            description="Cross-border layering through transit hub",
            tags=['aml_structuring', 'risk_weight_95']
        ))
        self.register(FraudRule(
            rule_id="R-0062",
            name="R-0062: Immediate cash deposit converted to outbound international wire",
            category=RuleCategory.AML_STRUCTURING,
            severity=RuleSeverity.HIGH,
            expression="cash_to_wire_conversion_detected == True",
            weight=85,
            description="Immediate cash deposit converted to outbound international wire",
            tags=['aml_structuring', 'risk_weight_85']
        ))
        self.register(FraudRule(
            rule_id="R-0063",
            name="R-0063: Commingling of commercial corporate revenue with personal accounts",
            category=RuleCategory.AML_STRUCTURING,
            severity=RuleSeverity.MEDIUM,
            expression="business_account_personal_expense_ratio > 0.8",
            weight=75,
            description="Commingling of commercial corporate revenue with personal accounts",
            tags=['aml_structuring', 'risk_weight_75']
        ))
        self.register(FraudRule(
            rule_id="R-0064",
            name="R-0064: Dormant account reactivated with sudden spike in transactions",
            category=RuleCategory.AML_STRUCTURING,
            severity=RuleSeverity.HIGH,
            expression="dor_mant_account_sudden_activation == True AND amount > 100000",
            weight=90,
            description="Dormant account reactivated with sudden spike in transactions",
            tags=['aml_structuring', 'risk_weight_90']
        ))
        self.register(FraudRule(
            rule_id="R-0065",
            name="R-0065: Lack of physical commercial address matching trade turnover",
            category=RuleCategory.AML_STRUCTURING,
            severity=RuleSeverity.CRITICAL,
            expression="shell_company_indicator == True AND annual_turnover_exceeded == True",
            weight=95,
            description="Lack of physical commercial address matching trade turnover",
            tags=['aml_structuring', 'risk_weight_95']
        ))

        # --- Category: Velocity & Bursting ---
        self.register(FraudRule(
            rule_id="R-0066",
            name="R-0066: High frequency automated script: >= 3 txns in 60 seconds",
            category=RuleCategory.VELOCITY_ABUSE,
            severity=RuleSeverity.CRITICAL,
            expression="transactions_count_1m >= 3",
            weight=95,
            description="High frequency automated script: >= 3 txns in 60 seconds",
            tags=['velocity_abuse', 'risk_weight_95']
        ))
        self.register(FraudRule(
            rule_id="R-0067",
            name="R-0067: Card cracking burst velocity: >= 8 txns in 5 minutes",
            category=RuleCategory.VELOCITY_ABUSE,
            severity=RuleSeverity.HIGH,
            expression="transactions_count_5m >= 8",
            weight=90,
            description="Card cracking burst velocity: >= 8 txns in 5 minutes",
            tags=['velocity_abuse', 'risk_weight_90']
        ))
        self.register(FraudRule(
            rule_id="R-0068",
            name="R-0068: Hourly cumulative outlay exceeds normal operating threshold",
            category=RuleCategory.VELOCITY_ABUSE,
            severity=RuleSeverity.HIGH,
            expression="cumulative_amount_1h > 200000",
            weight=85,
            description="Hourly cumulative outlay exceeds normal operating threshold",
            tags=['velocity_abuse', 'risk_weight_85']
        ))
        self.register(FraudRule(
            rule_id="R-0069",
            name="R-0069: Rapid multi-merchant traversal within 60 minutes",
            category=RuleCategory.VELOCITY_ABUSE,
            severity=RuleSeverity.HIGH,
            expression="distinct_merchants_1h >= 5",
            weight=80,
            description="Rapid multi-merchant traversal within 60 minutes",
            tags=['velocity_abuse', 'risk_weight_80']
        ))
        self.register(FraudRule(
            rule_id="R-0070",
            name="R-0070: Single device attempting transactions on >= 3 distinct card numbers",
            category=RuleCategory.VELOCITY_ABUSE,
            severity=RuleSeverity.CRITICAL,
            expression="distinct_cards_1h >= 3",
            weight=95,
            description="Single device attempting transactions on >= 3 distinct card numbers",
            tags=['velocity_abuse', 'risk_weight_95']
        ))
        self.register(FraudRule(
            rule_id="R-0071",
            name="R-0071: Repeated authorization declines preceding approved transaction",
            category=RuleCategory.VELOCITY_ABUSE,
            severity=RuleSeverity.HIGH,
            expression="failed_auth_velocity_1h >= 4",
            weight=85,
            description="Repeated authorization declines preceding approved transaction",
            tags=['velocity_abuse', 'risk_weight_85']
        ))
        self.register(FraudRule(
            rule_id="R-0072",
            name="R-0072: IP address hopping / dynamic proxy rotation within 24 hours",
            category=RuleCategory.VELOCITY_ABUSE,
            severity=RuleSeverity.MEDIUM,
            expression="distinct_ip_addresses_24h >= 4",
            weight=75,
            description="IP address hopping / dynamic proxy rotation within 24 hours",
            tags=['velocity_abuse', 'risk_weight_75']
        ))
        self.register(FraudRule(
            rule_id="R-0073",
            name="R-0073: Net account depletion rate exceeding historical sustainable velocity",
            category=RuleCategory.VELOCITY_ABUSE,
            severity=RuleSeverity.MEDIUM,
            expression="outbound_velocity_exceeds_inbound_7d == True",
            weight=70,
            description="Net account depletion rate exceeding historical sustainable velocity",
            tags=['velocity_abuse', 'risk_weight_70']
        ))
        self.register(FraudRule(
            rule_id="R-0074",
            name="R-0074: Card testing / micro-auth pinging (amounts < ₹100)",
            category=RuleCategory.VELOCITY_ABUSE,
            severity=RuleSeverity.HIGH,
            expression="micro_transaction_count_1h >= 10",
            weight=80,
            description="Card testing / micro-auth pinging (amounts < ₹100)",
            tags=['velocity_abuse', 'risk_weight_80']
        ))
        self.register(FraudRule(
            rule_id="R-0075",
            name="R-0075: Concurrent multi-channel pinging across Web, App, and POS",
            category=RuleCategory.VELOCITY_ABUSE,
            severity=RuleSeverity.MEDIUM,
            expression="payment_channel_hopping_1h >= 3",
            weight=75,
            description="Concurrent multi-channel pinging across Web, App, and POS",
            tags=['velocity_abuse', 'risk_weight_75']
        ))
        self.register(FraudRule(
            rule_id="R-0076",
            name="R-0076: Rapid dispersion of funds to 5+ distinct beneficiaries",
            category=RuleCategory.VELOCITY_ABUSE,
            severity=RuleSeverity.HIGH,
            expression="recipient_velocity_1h >= 5",
            weight=85,
            description="Rapid dispersion of funds to 5+ distinct beneficiaries",
            tags=['velocity_abuse', 'risk_weight_85']
        ))
        self.register(FraudRule(
            rule_id="R-0077",
            name="R-0077: High velocity transactions during nocturnal dead-hours (02:00-05:00)",
            category=RuleCategory.VELOCITY_ABUSE,
            severity=RuleSeverity.HIGH,
            expression="night_time_burst_velocity >= 4",
            weight=85,
            description="High velocity transactions during nocturnal dead-hours (02:00-05:00)",
            tags=['velocity_abuse', 'risk_weight_85']
        ))
        self.register(FraudRule(
            rule_id="R-0078",
            name="R-0078: Programmatic bot execution detected on checkout endpoints",
            category=RuleCategory.VELOCITY_ABUSE,
            severity=RuleSeverity.CRITICAL,
            expression="api_call_rate_per_sec > 10",
            weight=95,
            description="Programmatic bot execution detected on checkout endpoints",
            tags=['velocity_abuse', 'risk_weight_95']
        ))
        self.register(FraudRule(
            rule_id="R-0079",
            name="R-0079: Brute force parameter search succeeded following serial rejections",
            category=RuleCategory.VELOCITY_ABUSE,
            severity=RuleSeverity.HIGH,
            expression="consecutive_declines_then_success == True",
            weight=90,
            description="Brute force parameter search succeeded following serial rejections",
            tags=['velocity_abuse', 'risk_weight_90']
        ))
        self.register(FraudRule(
            rule_id="R-0080",
            name="R-0080: Impossible travel velocity exceeding Mach 1 commercial flight speed",
            category=RuleCategory.VELOCITY_ABUSE,
            severity=RuleSeverity.CRITICAL,
            expression="geographic_velocity_km_per_hour > 900.0",
            weight=100,
            description="Impossible travel velocity exceeding Mach 1 commercial flight speed",
            tags=['velocity_abuse', 'risk_weight_100']
        ))

        # --- Category: Geographic & Teleportation ---
        self.register(FraudRule(
            rule_id="R-0081",
            name="R-0081: Transaction initiated from OFAC sanctioned country code",
            category=RuleCategory.GEO_ANOMALY,
            severity=RuleSeverity.CRITICAL,
            expression="country_sanctioned == True",
            weight=100,
            description="Transaction initiated from OFAC sanctioned country code",
            tags=['geo_anomaly', 'risk_weight_100']
        ))
        self.register(FraudRule(
            rule_id="R-0082",
            name="R-0082: Foreign continent location without customer travel notice",
            category=RuleCategory.GEO_ANOMALY,
            severity=RuleSeverity.HIGH,
            expression="distance_from_home_km > 2000.0 AND travel_notice_active == False",
            weight=85,
            description="Foreign continent location without customer travel notice",
            tags=['geo_anomaly', 'risk_weight_85']
        ))
        self.register(FraudRule(
            rule_id="R-0083",
            name="R-0083: Physical distance between transactions implies impossible transit speed",
            category=RuleCategory.GEO_ANOMALY,
            severity=RuleSeverity.CRITICAL,
            expression="impossible_speed_kmh > 800.0",
            weight=95,
            description="Physical distance between transactions implies impossible transit speed",
            tags=['geo_anomaly', 'risk_weight_95']
        ))
        self.register(FraudRule(
            rule_id="R-0084",
            name="R-0084: Traffic originating from verified TOR anonymity network exit node",
            category=RuleCategory.GEO_ANOMALY,
            severity=RuleSeverity.CRITICAL,
            expression="tor_exit_node == True",
            weight=95,
            description="Traffic originating from verified TOR anonymity network exit node",
            tags=['geo_anomaly', 'risk_weight_95']
        ))
        self.register(FraudRule(
            rule_id="R-0085",
            name="R-0085: Public VPN masking IP during high-value authorization",
            category=RuleCategory.GEO_ANOMALY,
            severity=RuleSeverity.MEDIUM,
            expression="commercial_vpn_detected == True AND amount > 40000",
            weight=75,
            description="Public VPN masking IP during high-value authorization",
            tags=['geo_anomaly', 'risk_weight_75']
        ))
        self.register(FraudRule(
            rule_id="R-0086",
            name="R-0086: IP geolocation country does not match credit card billing country",
            category=RuleCategory.GEO_ANOMALY,
            severity=RuleSeverity.HIGH,
            expression="ip_country != billing_country AND amount > 50000",
            weight=80,
            description="IP geolocation country does not match credit card billing country",
            tags=['geo_anomaly', 'risk_weight_80']
        ))
        self.register(FraudRule(
            rule_id="R-0087",
            name="R-0087: Connection originating from AWS/DigitalOcean/Hetzner hosting datacenter",
            category=RuleCategory.GEO_ANOMALY,
            severity=RuleSeverity.HIGH,
            expression="ip_asn_datacenter == True",
            weight=85,
            description="Connection originating from AWS/DigitalOcean/Hetzner hosting datacenter",
            tags=['geo_anomaly', 'risk_weight_85']
        ))
        self.register(FraudRule(
            rule_id="R-0088",
            name="R-0088: Starlink / maritime satellite connection on domestic payment",
            category=RuleCategory.GEO_ANOMALY,
            severity=RuleSeverity.MEDIUM,
            expression="satellite_isp_detected == True AND amount > 30000",
            weight=65,
            description="Starlink / maritime satellite connection on domestic payment",
            tags=['geo_anomaly', 'risk_weight_65']
        ))
        self.register(FraudRule(
            rule_id="R-0089",
            name="R-0089: Transaction originating from known international cybercrime corridor",
            category=RuleCategory.GEO_ANOMALY,
            severity=RuleSeverity.HIGH,
            expression="high_risk_fraud_region == True AND amount > 60000",
            weight=85,
            description="Transaction originating from known international cybercrime corridor",
            tags=['geo_anomaly', 'risk_weight_85']
        ))
        self.register(FraudRule(
            rule_id="R-0090",
            name="R-0090: Android Mock Location provider detected on mobile banking client",
            category=RuleCategory.GEO_ANOMALY,
            severity=RuleSeverity.CRITICAL,
            expression="gps_spoofing_mock_location == True",
            weight=95,
            description="Android Mock Location provider detected on mobile banking client",
            tags=['geo_anomaly', 'risk_weight_95']
        ))
        self.register(FraudRule(
            rule_id="R-0091",
            name="R-0091: Client advertised BSSID triangulation contradicts IP location",
            category=RuleCategory.GEO_ANOMALY,
            severity=RuleSeverity.MEDIUM,
            expression="wifi_bssid_inconsistent == True",
            weight=70,
            description="Client advertised BSSID triangulation contradicts IP location",
            tags=['geo_anomaly', 'risk_weight_70']
        ))
        self.register(FraudRule(
            rule_id="R-0092",
            name="R-0092: IP address registered on abuse and botnet threat blacklists",
            category=RuleCategory.GEO_ANOMALY,
            severity=RuleSeverity.HIGH,
            expression="ip_reputation_score < 20",
            weight=90,
            description="IP address registered on abuse and botnet threat blacklists",
            tags=['geo_anomaly', 'risk_weight_90']
        ))
        self.register(FraudRule(
            rule_id="R-0093",
            name="R-0093: SIM MNC/MCC country contradicts device physical IP address",
            category=RuleCategory.GEO_ANOMALY,
            severity=RuleSeverity.MEDIUM,
            expression="cellular_carrier_country_mismatch == True",
            weight=75,
            description="SIM MNC/MCC country contradicts device physical IP address",
            tags=['geo_anomaly', 'risk_weight_75']
        ))
        self.register(FraudRule(
            rule_id="R-0094",
            name="R-0094: Trans-border physical authorization inconsistency",
            category=RuleCategory.GEO_ANOMALY,
            severity=RuleSeverity.HIGH,
            expression="border_crossing_transit_hours < 1 AND distance_km > 500",
            weight=90,
            description="Trans-border physical authorization inconsistency",
            tags=['geo_anomaly', 'risk_weight_90']
        ))
        self.register(FraudRule(
            rule_id="R-0095",
            name="R-0095: Device clock configuration deviates >3 hours from geo IP timezone",
            category=RuleCategory.GEO_ANOMALY,
            severity=RuleSeverity.MEDIUM,
            expression="timezone_offset_mismatch_hours > 3",
            weight=70,
            description="Device clock configuration deviates >3 hours from geo IP timezone",
            tags=['geo_anomaly', 'risk_weight_70']
        ))

        # --- Category: Device Integrity & Spoofing ---
        self.register(FraudRule(
            rule_id="R-0096",
            name="R-0096: Canvas HTML5 rendering noise injection detected",
            category=RuleCategory.DEVICE_SPOOFING,
            severity=RuleSeverity.HIGH,
            expression="canvas_fingerprint_spoofed == True",
            weight=90,
            description="Canvas HTML5 rendering noise injection detected",
            tags=['device_spoofing', 'risk_weight_90']
        ))
        self.register(FraudRule(
            rule_id="R-0097",
            name="R-0097: Headless Chromium SwiftShader software rendering",
            category=RuleCategory.DEVICE_SPOOFING,
            severity=RuleSeverity.HIGH,
            expression="webgl_vendor == 'Google Inc. (Google)' AND platform == 'Win32'",
            weight=85,
            description="Headless Chromium SwiftShader software rendering",
            tags=['device_spoofing', 'risk_weight_85']
        ))
        self.register(FraudRule(
            rule_id="R-0098",
            name="R-0098: Sec-CH-UA client hints contradict User-Agent header",
            category=RuleCategory.DEVICE_SPOOFING,
            severity=RuleSeverity.HIGH,
            expression="user_agent_client_hints_mismatch == True",
            weight=80,
            description="Sec-CH-UA client hints contradict User-Agent header",
            tags=['device_spoofing', 'risk_weight_80']
        ))
        self.register(FraudRule(
            rule_id="R-0099",
            name="R-0099: Selenium / Puppeteer `navigator.webdriver` automation flag enabled",
            category=RuleCategory.DEVICE_SPOOFING,
            severity=RuleSeverity.CRITICAL,
            expression="automation_webdriver_present == True",
            weight=100,
            description="Selenium / Puppeteer `navigator.webdriver` automation flag enabled",
            tags=['device_spoofing', 'risk_weight_100']
        ))
        self.register(FraudRule(
            rule_id="R-0100",
            name="R-0100: Bogus hardware specifications characteristic of emulation",
            category=RuleCategory.DEVICE_SPOOFING,
            severity=RuleSeverity.HIGH,
            expression="device_memory_gb == 0 OR hardware_concurrency == 0",
            weight=80,
            description="Bogus hardware specifications characteristic of emulation",
            tags=['device_spoofing', 'risk_weight_80']
        ))
        self.register(FraudRule(
            rule_id="R-0101",
            name="R-0101: Mobile user agent claimed without touchscreen hardware events",
            category=RuleCategory.DEVICE_SPOOFING,
            severity=RuleSeverity.HIGH,
            expression="touch_support_missing_on_mobile == True",
            weight=85,
            description="Mobile user agent claimed without touchscreen hardware events",
            tags=['device_spoofing', 'risk_weight_85']
        ))
        self.register(FraudRule(
            rule_id="R-0102",
            name="R-0102: DynamicsCompressor audio context hash variance across frames",
            category=RuleCategory.DEVICE_SPOOFING,
            severity=RuleSeverity.MEDIUM,
            expression="audio_fingerprint_unstable == True",
            weight=75,
            description="DynamicsCompressor audio context hash variance across frames",
            tags=['device_spoofing', 'risk_weight_75']
        ))
        self.register(FraudRule(
            rule_id="R-0103",
            name="R-0103: Minimal system fonts installed characteristic of Linux Docker container",
            category=RuleCategory.DEVICE_SPOOFING,
            severity=RuleSeverity.MEDIUM,
            expression="fonts_count < 10",
            weight=70,
            description="Minimal system fonts installed characteristic of Linux Docker container",
            tags=['device_spoofing', 'risk_weight_70']
        ))
        self.register(FraudRule(
            rule_id="R-0104",
            name="R-0104: BatteryManager API mocked or returning unnatural charging values",
            category=RuleCategory.DEVICE_SPOOFING,
            severity=RuleSeverity.MEDIUM,
            expression="battery_api_fake == True",
            weight=65,
            description="BatteryManager API mocked or returning unnatural charging values",
            tags=['device_spoofing', 'risk_weight_65']
        ))
        self.register(FraudRule(
            rule_id="R-0105",
            name="R-0105: Browser plugins prototype pollution or unnatural array length",
            category=RuleCategory.DEVICE_SPOOFING,
            severity=RuleSeverity.MEDIUM,
            expression="plugin_array_tampered == True",
            weight=75,
            description="Browser plugins prototype pollution or unnatural array length",
            tags=['device_spoofing', 'risk_weight_75']
        ))
        self.register(FraudRule(
            rule_id="R-0106",
            name="R-0106: WebRTC IP leakage reveals true network origin bypassing VPN",
            category=RuleCategory.DEVICE_SPOOFING,
            severity=RuleSeverity.HIGH,
            expression="webrtc_local_ip_leak == True AND is_private_ip == False",
            weight=80,
            description="WebRTC IP leakage reveals true network origin bypassing VPN",
            tags=['device_spoofing', 'risk_weight_80']
        ))
        self.register(FraudRule(
            rule_id="R-0107",
            name="R-0107: Anti-debugging hook or devtools inspection bypass caught",
            category=RuleCategory.DEVICE_SPOOFING,
            severity=RuleSeverity.HIGH,
            expression="debugger_statement_blocked == True",
            weight=85,
            description="Anti-debugging hook or devtools inspection bypass caught",
            tags=['device_spoofing', 'risk_weight_85']
        ))
        self.register(FraudRule(
            rule_id="R-0108",
            name="R-0108: Same hardware footprint observed across 5+ independent user accounts",
            category=RuleCategory.DEVICE_SPOOFING,
            severity=RuleSeverity.HIGH,
            expression="device_fingerprint_velocity_1d >= 5",
            weight=90,
            description="Same hardware footprint observed across 5+ independent user accounts",
            tags=['device_spoofing', 'risk_weight_90']
        ))
        self.register(FraudRule(
            rule_id="R-0109",
            name="R-0109: Window dimensions (e.g. 800x600) matching automation defaults",
            category=RuleCategory.DEVICE_SPOOFING,
            severity=RuleSeverity.MEDIUM,
            expression="screen_resolution_unnatural == True",
            weight=70,
            description="Window dimensions (e.g. 800x600) matching automation defaults",
            tags=['device_spoofing', 'risk_weight_70']
        ))
        self.register(FraudRule(
            rule_id="R-0110",
            name="R-0110: State persistence explicitly disabled to evade tracking",
            category=RuleCategory.DEVICE_SPOOFING,
            severity=RuleSeverity.HIGH,
            expression="cookie_disabled == True AND local_storage_disabled == True",
            weight=80,
            description="State persistence explicitly disabled to evade tracking",
            tags=['device_spoofing', 'risk_weight_80']
        ))

        # --- Category: Behavioral & Biometrics ---
        self.register(FraudRule(
            rule_id="R-0111",
            name="R-0111: Inhuman uniform keystroke flight time (autofill or bot playback)",
            category=RuleCategory.BEHAVIORAL_ANOMALY,
            severity=RuleSeverity.CRITICAL,
            expression="keystroke_flight_time_variance < 0.005",
            weight=95,
            description="Inhuman uniform keystroke flight time (autofill or bot playback)",
            tags=['behavioral_anomaly', 'risk_weight_95']
        ))
        self.register(FraudRule(
            rule_id="R-0112",
            name="R-0112: Zero curvature synthetic mouse pointer vector",
            category=RuleCategory.BEHAVIORAL_ANOMALY,
            severity=RuleSeverity.HIGH,
            expression="mouse_trajectory_straight_line == True",
            weight=90,
            description="Zero curvature synthetic mouse pointer vector",
            tags=['behavioral_anomaly', 'risk_weight_90']
        ))
        self.register(FraudRule(
            rule_id="R-0113",
            name="R-0113: Instantaneous multi-field form completion without hesitation",
            category=RuleCategory.BEHAVIORAL_ANOMALY,
            severity=RuleSeverity.HIGH,
            expression="hesitation_time_seconds < 0.2 AND form_fields >= 6",
            weight=85,
            description="Instantaneous multi-field form completion without hesitation",
            tags=['behavioral_anomaly', 'risk_weight_85']
        ))
        self.register(FraudRule(
            rule_id="R-0114",
            name="R-0114: Typing speed exceeds physiological limits of human input",
            category=RuleCategory.BEHAVIORAL_ANOMALY,
            severity=RuleSeverity.HIGH,
            expression="typing_speed_wpm > 250",
            weight=90,
            description="Typing speed exceeds physiological limits of human input",
            tags=['behavioral_anomaly', 'risk_weight_90']
        ))
        self.register(FraudRule(
            rule_id="R-0115",
            name="R-0115: Constant velocity wheel scroll event without human deceleration",
            category=RuleCategory.BEHAVIORAL_ANOMALY,
            severity=RuleSeverity.HIGH,
            expression="scroll_velocity_constant == True",
            weight=80,
            description="Constant velocity wheel scroll event without human deceleration",
            tags=['behavioral_anomaly', 'risk_weight_80']
        ))
        self.register(FraudRule(
            rule_id="R-0116",
            name="R-0116: Mass copy-paste of sensitive identification credentials",
            category=RuleCategory.BEHAVIORAL_ANOMALY,
            severity=RuleSeverity.LOW,
            expression="paste_event_count >= 4",
            weight=60,
            description="Mass copy-paste of sensitive identification credentials",
            tags=['behavioral_anomaly', 'risk_weight_60']
        ))
        self.register(FraudRule(
            rule_id="R-0117",
            name="R-0117: Key press dwell time <10ms characteristic of programmatic synthetic input",
            category=RuleCategory.BEHAVIORAL_ANOMALY,
            severity=RuleSeverity.HIGH,
            expression="dwell_time_per_key_ms < 10",
            weight=85,
            description="Key press dwell time <10ms characteristic of programmatic synthetic input",
            tags=['behavioral_anomaly', 'risk_weight_85']
        ))
        self.register(FraudRule(
            rule_id="R-0118",
            name="R-0118: Rapid checkout completion: session under 5 seconds for high value",
            category=RuleCategory.BEHAVIORAL_ANOMALY,
            severity=RuleSeverity.HIGH,
            expression="session_duration_seconds < 5 AND amount > 50000",
            weight=90,
            description="Rapid checkout completion: session under 5 seconds for high value",
            tags=['behavioral_anomaly', 'risk_weight_90']
        ))
        self.register(FraudRule(
            rule_id="R-0119",
            name="R-0119: Touch/Click events without intermediate hover or mouse move events",
            category=RuleCategory.BEHAVIORAL_ANOMALY,
            severity=RuleSeverity.HIGH,
            expression="mouse_movement_missing == True AND clicks >= 3",
            weight=85,
            description="Touch/Click events without intermediate hover or mouse move events",
            tags=['behavioral_anomaly', 'risk_weight_85']
        ))
        self.register(FraudRule(
            rule_id="R-0120",
            name="R-0120: Zero error rate on lengthy alphanumeric address input",
            category=RuleCategory.BEHAVIORAL_ANOMALY,
            severity=RuleSeverity.MEDIUM,
            expression="backspace_correction_rate == 0.0 AND input_length > 40",
            weight=65,
            description="Zero error rate on lengthy alphanumeric address input",
            tags=['behavioral_anomaly', 'risk_weight_65']
        ))
        self.register(FraudRule(
            rule_id="R-0121",
            name="R-0121: Lack of organic physiological micro-tremors in pointer tracking",
            category=RuleCategory.BEHAVIORAL_ANOMALY,
            severity=RuleSeverity.MEDIUM,
            expression="micro_tremor_missing == True",
            weight=75,
            description="Lack of organic physiological micro-tremors in pointer tracking",
            tags=['behavioral_anomaly', 'risk_weight_75']
        ))
        self.register(FraudRule(
            rule_id="R-0122",
            name="R-0122: Frequent application focus loss indicative of external credential lookup",
            category=RuleCategory.BEHAVIORAL_ANOMALY,
            severity=RuleSeverity.MEDIUM,
            expression="tab_switch_count_during_checkout >= 5",
            weight=70,
            description="Frequent application focus loss indicative of external credential lookup",
            tags=['behavioral_anomaly', 'risk_weight_70']
        ))
        self.register(FraudRule(
            rule_id="R-0123",
            name="R-0123: Terms and transaction review skipped instantaneously",
            category=RuleCategory.BEHAVIORAL_ANOMALY,
            severity=RuleSeverity.MEDIUM,
            expression="reading_time_per_word_ms < 50",
            weight=75,
            description="Terms and transaction review skipped instantaneously",
            tags=['behavioral_anomaly', 'risk_weight_75']
        ))
        self.register(FraudRule(
            rule_id="R-0124",
            name="R-0124: Drastic deviation from user\'s historical active trading hours",
            category=RuleCategory.BEHAVIORAL_ANOMALY,
            severity=RuleSeverity.MEDIUM,
            expression="abnormal_checkout_hour == True AND amount > 40000",
            weight=70,
            description="Drastic deviation from user\'s historical active trading hours",
            tags=['behavioral_anomaly', 'risk_weight_70']
        ))
        self.register(FraudRule(
            rule_id="R-0125",
            name="R-0125: Continuous behavioral biometric score drops below verification baseline",
            category=RuleCategory.BEHAVIORAL_ANOMALY,
            severity=RuleSeverity.HIGH,
            expression="biometric_confidence_score < 0.35",
            weight=85,
            description="Continuous behavioral biometric score drops below verification baseline",
            tags=['behavioral_anomaly', 'risk_weight_85']
        ))

        # --- Category: Merchant Bust-Out & Risk ---
        self.register(FraudRule(
            rule_id="R-0126",
            name="R-0126: Merchant bust-out: sudden massive volume surge on young merchant account",
            category=RuleCategory.MERCHANT_RISK,
            severity=RuleSeverity.CRITICAL,
            expression="merchant_account_age_days < 30 AND monthly_volume_spike > 500.0",
            weight=95,
            description="Merchant bust-out: sudden massive volume surge on young merchant account",
            tags=['merchant_risk', 'risk_weight_95']
        ))
        self.register(FraudRule(
            rule_id="R-0127",
            name="R-0127: Merchant refund and reversal rate exceeds 20% threshold",
            category=RuleCategory.MERCHANT_RISK,
            severity=RuleSeverity.HIGH,
            expression="merchant_refund_rate > 0.20",
            weight=90,
            description="Merchant refund and reversal rate exceeds 20% threshold",
            tags=['merchant_risk', 'risk_weight_90']
        ))
        self.register(FraudRule(
            rule_id="R-0128",
            name="R-0128: Merchant breach of Visa/Mastercard 1.5% chargeback monitoring threshold",
            category=RuleCategory.MERCHANT_RISK,
            severity=RuleSeverity.CRITICAL,
            expression="merchant_chargeback_ratio > 0.015",
            weight=95,
            description="Merchant breach of Visa/Mastercard 1.5% chargeback monitoring threshold",
            tags=['merchant_risk', 'risk_weight_95']
        ))
        self.register(FraudRule(
            rule_id="R-0129",
            name="R-0129: Uncharacteristic jump in average transaction ticket size",
            category=RuleCategory.MERCHANT_RISK,
            severity=RuleSeverity.HIGH,
            expression="merchant_average_ticket_size_increase > 300.0",
            weight=85,
            description="Uncharacteristic jump in average transaction ticket size",
            tags=['merchant_risk', 'risk_weight_85']
        ))
        self.register(FraudRule(
            rule_id="R-0130",
            name="R-0130: Merchant processing gambling/forex without proper license credentials",
            category=RuleCategory.MERCHANT_RISK,
            severity=RuleSeverity.CRITICAL,
            expression="merchant_operating_in_unlicensed_category == True",
            weight=95,
            description="Merchant processing gambling/forex without proper license credentials",
            tags=['merchant_risk', 'risk_weight_95']
        ))
        self.register(FraudRule(
            rule_id="R-0131",
            name="R-0131: Excessive rapid onboarding of virtual payment acceptance terminals",
            category=RuleCategory.MERCHANT_RISK,
            severity=RuleSeverity.HIGH,
            expression="merchant_terminal_count_velocity_7d >= 10",
            weight=80,
            description="Excessive rapid onboarding of virtual payment acceptance terminals",
            tags=['merchant_risk', 'risk_weight_80']
        ))
        self.register(FraudRule(
            rule_id="R-0132",
            name="R-0132: Settlement bank routing change immediately preceding volume surge",
            category=RuleCategory.MERCHANT_RISK,
            severity=RuleSeverity.MEDIUM,
            expression="merchant_settlement_bank_changed_days < 7",
            weight=75,
            description="Settlement bank routing change immediately preceding volume surge",
            tags=['merchant_risk', 'risk_weight_75']
        ))
        self.register(FraudRule(
            rule_id="R-0133",
            name="R-0133: Offshore acquirer shopping / unauthorized international aggregation",
            category=RuleCategory.MERCHANT_RISK,
            severity=RuleSeverity.HIGH,
            expression="merchant_cross_border_ratio > 0.85 AND domestic_license == True",
            weight=85,
            description="Offshore acquirer shopping / unauthorized international aggregation",
            tags=['merchant_risk', 'risk_weight_85']
        ))
        self.register(FraudRule(
            rule_id="R-0134",
            name="R-0134: Sudden high-volume reactivation of previously dormant merchant ID",
            category=RuleCategory.MERCHANT_RISK,
            severity=RuleSeverity.HIGH,
            expression="merchant_dormant_reactivation == True AND volume > 1000000",
            weight=90,
            description="Sudden high-volume reactivation of previously dormant merchant ID",
            tags=['merchant_risk', 'risk_weight_90']
        ))
        self.register(FraudRule(
            rule_id="R-0135",
            name="R-0135: Merchant gateway being actively exploited as a card validation dump",
            category=RuleCategory.MERCHANT_RISK,
            severity=RuleSeverity.HIGH,
            expression="merchant_card_testing_ratio > 0.15",
            weight=90,
            description="Merchant gateway being actively exploited as a card validation dump",
            tags=['merchant_risk', 'risk_weight_90']
        ))

        # --- Category: Money Mule & Layering ---
        self.register(FraudRule(
            rule_id="R-0136",
            name="R-0136: Account turnover velocity is 50x baseline ledger balance",
            category=RuleCategory.MULE_ACCOUNT,
            severity=RuleSeverity.CRITICAL,
            expression="account_turnover_to_balance_ratio > 50.0",
            weight=95,
            description="Account turnover velocity is 50x baseline ledger balance",
            tags=['mule_account', 'risk_weight_95']
        ))
        self.register(FraudRule(
            rule_id="R-0137",
            name="R-0137: Layering mule: immediate cashout or outbound transfer post credit",
            category=RuleCategory.MULE_ACCOUNT,
            severity=RuleSeverity.HIGH,
            expression="rapid_withdrawal_post_deposit_minutes < 15",
            weight=90,
            description="Layering mule: immediate cashout or outbound transfer post credit",
            tags=['mule_account', 'risk_weight_90']
        ))
        self.register(FraudRule(
            rule_id="R-0138",
            name="R-0138: College student profile processing massive corporate volume",
            category=RuleCategory.MULE_ACCOUNT,
            severity=RuleSeverity.CRITICAL,
            expression="customer_age_bracket == 'STUDENT' AND turnover > 2000000",
            weight=95,
            description="College student profile processing massive corporate volume",
            tags=['mule_account', 'risk_weight_95']
        ))
        self.register(FraudRule(
            rule_id="R-0139",
            name="R-0139: Funnel account: dozens of P2P inflows aggregated into single wire",
            category=RuleCategory.MULE_ACCOUNT,
            severity=RuleSeverity.HIGH,
            expression="incoming_micro_outgoing_macro == True",
            weight=90,
            description="Funnel account: dozens of P2P inflows aggregated into single wire",
            tags=['mule_account', 'risk_weight_90']
        ))
        self.register(FraudRule(
            rule_id="R-0140",
            name="R-0140: Long-term dormant retail account reactivated for mule laundering",
            category=RuleCategory.MULE_ACCOUNT,
            severity=RuleSeverity.HIGH,
            expression="account_dormant_duration_days > 180 AND first_txn_amount > 200000",
            weight=90,
            description="Long-term dormant retail account reactivated for mule laundering",
            tags=['mule_account', 'risk_weight_90']
        ))
        self.register(FraudRule(
            rule_id="R-0141",
            name="R-0141: Device fingerprint matches confirmed active mule account",
            category=RuleCategory.MULE_ACCOUNT,
            severity=RuleSeverity.CRITICAL,
            expression="shared_payout_device_with_known_mule == True",
            weight=100,
            description="Device fingerprint matches confirmed active mule account",
            tags=['mule_account', 'risk_weight_100']
        ))
        self.register(FraudRule(
            rule_id="R-0142",
            name="R-0142: Immediate redirection of retail funds to cryptocurrency exchange hot-wallet",
            category=RuleCategory.MULE_ACCOUNT,
            severity=RuleSeverity.CRITICAL,
            expression="rapid_crypto_exchange_offramp == True",
            weight=95,
            description="Immediate redirection of retail funds to cryptocurrency exchange hot-wallet",
            tags=['mule_account', 'risk_weight_95']
        ))
        self.register(FraudRule(
            rule_id="R-0143",
            name="R-0143: Nomadic address modifications across disparate state jurisdictions",
            category=RuleCategory.MULE_ACCOUNT,
            severity=RuleSeverity.MEDIUM,
            expression="frequent_address_change_count_1y >= 4",
            weight=75,
            description="Nomadic address modifications across disparate state jurisdictions",
            tags=['mule_account', 'risk_weight_75']
        ))
        self.register(FraudRule(
            rule_id="R-0144",
            name="R-0144: Single mobile contact linked across multiple unassociated account holders",
            category=RuleCategory.MULE_ACCOUNT,
            severity=RuleSeverity.HIGH,
            expression="phone_number_associated_with_multiple_accounts >= 3",
            weight=90,
            description="Single mobile contact linked across multiple unassociated account holders",
            tags=['mule_account', 'risk_weight_90']
        ))
        self.register(FraudRule(
            rule_id="R-0145",
            name="R-0145: Cash withdrawal occurring in state disparate from KYC residence",
            category=RuleCategory.MULE_ACCOUNT,
            severity=RuleSeverity.HIGH,
            expression="atm_cash_out_in_different_state == True",
            weight=85,
            description="Cash withdrawal occurring in state disparate from KYC residence",
            tags=['mule_account', 'risk_weight_85']
        ))

        # --- Category: Synthetic Identity Theft ---
        self.register(FraudRule(
            rule_id="R-0146",
            name="R-0146: SSN issuance date post-dates applicant declared date of birth",
            category=RuleCategory.SYNTHETIC_IDENTITY,
            severity=RuleSeverity.CRITICAL,
            expression="ssn_issued_after_dob == True",
            weight=100,
            description="SSN issuance date post-dates applicant declared date of birth",
            tags=['synthetic_identity', 'risk_weight_100']
        ))
        self.register(FraudRule(
            rule_id="R-0147",
            name="R-0147: Thin credit file applicant seeking substantial initial credit line",
            category=RuleCategory.SYNTHETIC_IDENTITY,
            severity=RuleSeverity.HIGH,
            expression="national_id_credit_file_depth_months < 6 AND amount > 80000",
            weight=90,
            description="Thin credit file applicant seeking substantial initial credit line",
            tags=['synthetic_identity', 'risk_weight_90']
        ))
        self.register(FraudRule(
            rule_id="R-0148",
            name="R-0148: Physical home address resolves to UPS Store or freight forwarder",
            category=RuleCategory.SYNTHETIC_IDENTITY,
            severity=RuleSeverity.HIGH,
            expression="applicant_address_is_commercial_mail_drop == True",
            weight=85,
            description="Physical home address resolves to UPS Store or freight forwarder",
            tags=['synthetic_identity', 'risk_weight_85']
        ))
        self.register(FraudRule(
            rule_id="R-0149",
            name="R-0149: Contact number is disposable virtual VoIP service (Bandwidth, Twilio)",
            category=RuleCategory.SYNTHETIC_IDENTITY,
            severity=RuleSeverity.MEDIUM,
            expression="applicant_phone_is_prepaid_voip == True",
            weight=75,
            description="Contact number is disposable virtual VoIP service (Bandwidth, Twilio)",
            tags=['synthetic_identity', 'risk_weight_75']
        ))
        self.register(FraudRule(
            rule_id="R-0150",
            name="R-0150: Identity fragmentation: components match multiple disparate individuals",
            category=RuleCategory.SYNTHETIC_IDENTITY,
            severity=RuleSeverity.HIGH,
            expression="name_dob_address_fragmented_records >= 3",
            weight=90,
            description="Identity fragmentation: components match multiple disparate individuals",
            tags=['synthetic_identity', 'risk_weight_90']
        ))
        self.register(FraudRule(
            rule_id="R-0151",
            name="R-0151: Credit piggybacking: newly added authorized user on aged trade line",
            category=RuleCategory.SYNTHETIC_IDENTITY,
            severity=RuleSeverity.HIGH,
            expression="authorized_user_piggybacking_detected == True",
            weight=80,
            description="Credit piggybacking: newly added authorized user on aged trade line",
            tags=['synthetic_identity', 'risk_weight_80']
        ))
        self.register(FraudRule(
            rule_id="R-0152",
            name="R-0152: Rapid loan stacking: 10+ credit inquiries across diverse lenders",
            category=RuleCategory.SYNTHETIC_IDENTITY,
            severity=RuleSeverity.HIGH,
            expression="credit_inquiry_velocity_30d >= 10",
            weight=85,
            description="Rapid loan stacking: 10+ credit inquiries across diverse lenders",
            tags=['synthetic_identity', 'risk_weight_85']
        ))
        self.register(FraudRule(
            rule_id="R-0153",
            name="R-0153: Applicant personal phone number submitted as corporate employer contact",
            category=RuleCategory.SYNTHETIC_IDENTITY,
            severity=RuleSeverity.HIGH,
            expression="employer_phone_matches_applicant_phone == True",
            weight=85,
            description="Applicant personal phone number submitted as corporate employer contact",
            tags=['synthetic_identity', 'risk_weight_85']
        ))
        self.register(FraudRule(
            rule_id="R-0154",
            name="R-0154: Social security identifier matches Social Security Death Master File",
            category=RuleCategory.SYNTHETIC_IDENTITY,
            severity=RuleSeverity.CRITICAL,
            expression="deceased_person_master_file_match == True",
            weight=100,
            description="Social security identifier matches Social Security Death Master File",
            tags=['synthetic_identity', 'risk_weight_100']
        ))
        self.register(FraudRule(
            rule_id="R-0155",
            name="R-0155: Combination of SSN/Email/Phone reused across 5+ application submissions",
            category=RuleCategory.SYNTHETIC_IDENTITY,
            severity=RuleSeverity.CRITICAL,
            expression="identity_element_reuse_count >= 5",
            weight=95,
            description="Combination of SSN/Email/Phone reused across 5+ application submissions",
            tags=['synthetic_identity', 'risk_weight_95']
        ))

        # --- Category: Cryptocurrency & Exit Scams ---
        self.register(FraudRule(
            rule_id="R-0156",
            name="R-0156: High-value fiat offramp to cryptocurrency exchange",
            category=RuleCategory.CRYPTO_EXIT,
            severity=RuleSeverity.HIGH,
            expression="merchant_name IN ['Binance', 'Coinbase', 'Kraken', 'WazirX'] AND amount > 200000",
            weight=90,
            description="High-value fiat offramp to cryptocurrency exchange",
            tags=['crypto_exit', 'risk_weight_90']
        ))
        self.register(FraudRule(
            rule_id="R-0157",
            name="R-0157: Rapid consecutive crypto purchases exhausting daily limit",
            category=RuleCategory.CRYPTO_EXIT,
            severity=RuleSeverity.HIGH,
            expression="crypto_purchase_velocity_1d >= 4",
            weight=85,
            description="Rapid consecutive crypto purchases exhausting daily limit",
            tags=['crypto_exit', 'risk_weight_85']
        ))
        self.register(FraudRule(
            rule_id="R-0158",
            name="R-0158: Account linked via Plaid/UPI with immediate crypto drain",
            category=RuleCategory.CRYPTO_EXIT,
            severity=RuleSeverity.CRITICAL,
            expression="newly_linked_bank_immediate_crypto_purchase == True",
            weight=95,
            description="Account linked via Plaid/UPI with immediate crypto drain",
            tags=['crypto_exit', 'risk_weight_95']
        ))
        self.register(FraudRule(
            rule_id="R-0159",
            name="R-0159: Physical Crypto ATM liquidation",
            category=RuleCategory.CRYPTO_EXIT,
            severity=RuleSeverity.HIGH,
            expression="crypto_atm_withdrawal == True AND amount > 25000",
            weight=85,
            description="Physical Crypto ATM liquidation",
            tags=['crypto_exit', 'risk_weight_85']
        ))
        self.register(FraudRule(
            rule_id="R-0160",
            name="R-0160: P2P crypto merchant high velocity counterparty flows",
            category=RuleCategory.CRYPTO_EXIT,
            severity=RuleSeverity.HIGH,
            expression="peer_to_peer_crypto_arbitrage_indicator == True",
            weight=80,
            description="P2P crypto merchant high velocity counterparty flows",
            tags=['crypto_exit', 'risk_weight_80']
        ))
        self.register(FraudRule(
            rule_id="R-0161",
            name="R-0161: Crypto transfer following credential security compromise event",
            category=RuleCategory.CRYPTO_EXIT,
            severity=RuleSeverity.CRITICAL,
            expression="crypto_transaction_preceded_by_phishing_alert == True",
            weight=100,
            description="Crypto transfer following credential security compromise event",
            tags=['crypto_exit', 'risk_weight_100']
        ))
        self.register(FraudRule(
            rule_id="R-0162",
            name="R-0162: Interaction with Tornado Cash / Blender OFAC sanctioned smart contract",
            category=RuleCategory.CRYPTO_EXIT,
            severity=RuleSeverity.CRITICAL,
            expression="unregulated_mixing_service_counterparty == True",
            weight=100,
            description="Interaction with Tornado Cash / Blender OFAC sanctioned smart contract",
            tags=['crypto_exit', 'risk_weight_100']
        ))
        self.register(FraudRule(
            rule_id="R-0163",
            name="R-0163: Total account liquidation leaving zero residual balance",
            category=RuleCategory.CRYPTO_EXIT,
            severity=RuleSeverity.HIGH,
            expression="rapid_drain_to_zero_balance == True AND amount > 100000",
            weight=90,
            description="Total account liquidation leaving zero residual balance",
            tags=['crypto_exit', 'risk_weight_90']
        ))
        self.register(FraudRule(
            rule_id="R-0164",
            name="R-0164: Crypto purchase authorization from unexpected geographic IP",
            category=RuleCategory.CRYPTO_EXIT,
            severity=RuleSeverity.HIGH,
            expression="crypto_outflow_outside_user_geography == True",
            weight=85,
            description="Crypto purchase authorization from unexpected geographic IP",
            tags=['crypto_exit', 'risk_weight_85']
        ))
        self.register(FraudRule(
            rule_id="R-0165",
            name="R-0165: Customer with zero crypto history executing substantial initial buy",
            category=RuleCategory.CRYPTO_EXIT,
            severity=RuleSeverity.HIGH,
            expression="first_ever_crypto_transaction_large_amount == True",
            weight=85,
            description="Customer with zero crypto history executing substantial initial buy",
            tags=['crypto_exit', 'risk_weight_85']
        ))

rule_catalog = RuleDefinitionCatalog()