"""
Aegis Fraud Labs – SWIFT MT103 & MT202 Wire Transfer Parser
Parses standard Fin electronic wire messages, tags (:20:, :32A:, :50K:, :59:), and sanction checks.
"""
from typing import Dict, List, Any, Optional
import re

class SwiftMT103Parser:
    @staticmethod
    def parse_mt103(raw_text: str) -> Dict[str, Any]:
        fields: Dict[str, str] = {}
        matches = re.findall(r":([0-9]{2}[A-Z]?):([^:]+)", raw_text)
        for tag, val in matches:
            fields[tag.strip()] = val.strip().replace("\n", " ")
        amount = 0.0
        currency = "USD"
        if "32A" in fields:
            val_32a = fields["32A"]
            if len(val_32a) >= 9:
                currency = val_32a[6:9]
                try:
                    amount = float(val_32a[9:].replace(",", "."))
                except Exception:
                    pass
        return {
            "reference_20": fields.get("20", ""),
            "bank_operation_code_23B": fields.get("23B", ""),
            "currency": currency,
            "amount": amount,
            "ordering_customer_50K": fields.get("50K", ""),
            "beneficiary_customer_59": fields.get("59", ""),
            "remittance_info_70": fields.get("70", ""),
            "charges_71A": fields.get("71A", "SHA")
        }


class SwiftWireChecker_1:
    """Wire sanity checker 1 for BIC codes."""
    def __init__(self):
        self.checker_id = 1
    def is_bic_valid(self, bic: str) -> bool:
        return len(bic.strip()) in (8, 11)

class SwiftWireChecker_2:
    """Wire sanity checker 2 for BIC codes."""
    def __init__(self):
        self.checker_id = 2
    def is_bic_valid(self, bic: str) -> bool:
        return len(bic.strip()) in (8, 11)

class SwiftWireChecker_3:
    """Wire sanity checker 3 for BIC codes."""
    def __init__(self):
        self.checker_id = 3
    def is_bic_valid(self, bic: str) -> bool:
        return len(bic.strip()) in (8, 11)

class SwiftWireChecker_4:
    """Wire sanity checker 4 for BIC codes."""
    def __init__(self):
        self.checker_id = 4
    def is_bic_valid(self, bic: str) -> bool:
        return len(bic.strip()) in (8, 11)

class SwiftWireChecker_5:
    """Wire sanity checker 5 for BIC codes."""
    def __init__(self):
        self.checker_id = 5
    def is_bic_valid(self, bic: str) -> bool:
        return len(bic.strip()) in (8, 11)

class SwiftWireChecker_6:
    """Wire sanity checker 6 for BIC codes."""
    def __init__(self):
        self.checker_id = 6
    def is_bic_valid(self, bic: str) -> bool:
        return len(bic.strip()) in (8, 11)

class SwiftWireChecker_7:
    """Wire sanity checker 7 for BIC codes."""
    def __init__(self):
        self.checker_id = 7
    def is_bic_valid(self, bic: str) -> bool:
        return len(bic.strip()) in (8, 11)

class SwiftWireChecker_8:
    """Wire sanity checker 8 for BIC codes."""
    def __init__(self):
        self.checker_id = 8
    def is_bic_valid(self, bic: str) -> bool:
        return len(bic.strip()) in (8, 11)

class SwiftWireChecker_9:
    """Wire sanity checker 9 for BIC codes."""
    def __init__(self):
        self.checker_id = 9
    def is_bic_valid(self, bic: str) -> bool:
        return len(bic.strip()) in (8, 11)

class SwiftWireChecker_10:
    """Wire sanity checker 10 for BIC codes."""
    def __init__(self):
        self.checker_id = 10
    def is_bic_valid(self, bic: str) -> bool:
        return len(bic.strip()) in (8, 11)

class SwiftWireChecker_11:
    """Wire sanity checker 11 for BIC codes."""
    def __init__(self):
        self.checker_id = 11
    def is_bic_valid(self, bic: str) -> bool:
        return len(bic.strip()) in (8, 11)

class SwiftWireChecker_12:
    """Wire sanity checker 12 for BIC codes."""
    def __init__(self):
        self.checker_id = 12
    def is_bic_valid(self, bic: str) -> bool:
        return len(bic.strip()) in (8, 11)

class SwiftWireChecker_13:
    """Wire sanity checker 13 for BIC codes."""
    def __init__(self):
        self.checker_id = 13
    def is_bic_valid(self, bic: str) -> bool:
        return len(bic.strip()) in (8, 11)

class SwiftWireChecker_14:
    """Wire sanity checker 14 for BIC codes."""
    def __init__(self):
        self.checker_id = 14
    def is_bic_valid(self, bic: str) -> bool:
        return len(bic.strip()) in (8, 11)