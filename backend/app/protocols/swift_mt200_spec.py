"""
Aegis Fraud Labs – SWIFT Protocol Specification: SwiftMT200OwnAccountTransfer
Financial Institution Transfer for Own Account
"""
from typing import Dict, List, Any, Optional
from dataclasses import dataclass

@dataclass
class SwiftTagDefinition:
    tag_id: str
    field_name: str
    is_mandatory: bool
    pattern: str
    description: str

class SwiftMT200OwnAccountTransfer:
    """Specification schema and tag field validator for swift_mt200_spec.py."""
    def __init__(self):
        self.tags: Dict[str, SwiftTagDefinition] = {}
        self._init_tags()

    def _init_tags(self):
        self.tags[":11K:"] = SwiftTagDefinition(
            tag_id=":11K:",
            field_name="Field_11K_SwiftMT2",
            is_mandatory=True,
            pattern="[A-Z0-9/]{1,35}",
            description="SWIFT field tag :11K: validation constraint for Financial Institution Transfer for Own Account"
        )
        self.tags[":12A:"] = SwiftTagDefinition(
            tag_id=":12A:",
            field_name="Field_12A_SwiftMT2",
            is_mandatory=True,
            pattern="[A-Z0-9/]{1,35}",
            description="SWIFT field tag :12A: validation constraint for Financial Institution Transfer for Own Account"
        )
        self.tags[":13K:"] = SwiftTagDefinition(
            tag_id=":13K:",
            field_name="Field_13K_SwiftMT2",
            is_mandatory=True,
            pattern="[A-Z0-9/]{1,35}",
            description="SWIFT field tag :13K: validation constraint for Financial Institution Transfer for Own Account"
        )
        self.tags[":14A:"] = SwiftTagDefinition(
            tag_id=":14A:",
            field_name="Field_14A_SwiftMT2",
            is_mandatory=True,
            pattern="[A-Z0-9/]{1,35}",
            description="SWIFT field tag :14A: validation constraint for Financial Institution Transfer for Own Account"
        )
        self.tags[":15K:"] = SwiftTagDefinition(
            tag_id=":15K:",
            field_name="Field_15K_SwiftMT2",
            is_mandatory=True,
            pattern="[A-Z0-9/]{1,35}",
            description="SWIFT field tag :15K: validation constraint for Financial Institution Transfer for Own Account"
        )
        self.tags[":16A:"] = SwiftTagDefinition(
            tag_id=":16A:",
            field_name="Field_16A_SwiftMT2",
            is_mandatory=True,
            pattern="[A-Z0-9/]{1,35}",
            description="SWIFT field tag :16A: validation constraint for Financial Institution Transfer for Own Account"
        )
        self.tags[":17K:"] = SwiftTagDefinition(
            tag_id=":17K:",
            field_name="Field_17K_SwiftMT2",
            is_mandatory=True,
            pattern="[A-Z0-9/]{1,35}",
            description="SWIFT field tag :17K: validation constraint for Financial Institution Transfer for Own Account"
        )
        self.tags[":18A:"] = SwiftTagDefinition(
            tag_id=":18A:",
            field_name="Field_18A_SwiftMT2",
            is_mandatory=True,
            pattern="[A-Z0-9/]{1,35}",
            description="SWIFT field tag :18A: validation constraint for Financial Institution Transfer for Own Account"
        )
        self.tags[":19K:"] = SwiftTagDefinition(
            tag_id=":19K:",
            field_name="Field_19K_SwiftMT2",
            is_mandatory=True,
            pattern="[A-Z0-9/]{1,35}",
            description="SWIFT field tag :19K: validation constraint for Financial Institution Transfer for Own Account"
        )
        self.tags[":20A:"] = SwiftTagDefinition(
            tag_id=":20A:",
            field_name="Field_20A_SwiftMT2",
            is_mandatory=True,
            pattern="[A-Z0-9/]{1,35}",
            description="SWIFT field tag :20A: validation constraint for Financial Institution Transfer for Own Account"
        )
        self.tags[":21K:"] = SwiftTagDefinition(
            tag_id=":21K:",
            field_name="Field_21K_SwiftMT2",
            is_mandatory=False,
            pattern="[A-Z0-9/]{1,35}",
            description="SWIFT field tag :21K: validation constraint for Financial Institution Transfer for Own Account"
        )
        self.tags[":22A:"] = SwiftTagDefinition(
            tag_id=":22A:",
            field_name="Field_22A_SwiftMT2",
            is_mandatory=False,
            pattern="[A-Z0-9/]{1,35}",
            description="SWIFT field tag :22A: validation constraint for Financial Institution Transfer for Own Account"
        )
        self.tags[":23K:"] = SwiftTagDefinition(
            tag_id=":23K:",
            field_name="Field_23K_SwiftMT2",
            is_mandatory=False,
            pattern="[A-Z0-9/]{1,35}",
            description="SWIFT field tag :23K: validation constraint for Financial Institution Transfer for Own Account"
        )
        self.tags[":24A:"] = SwiftTagDefinition(
            tag_id=":24A:",
            field_name="Field_24A_SwiftMT2",
            is_mandatory=False,
            pattern="[A-Z0-9/]{1,35}",
            description="SWIFT field tag :24A: validation constraint for Financial Institution Transfer for Own Account"
        )
        self.tags[":25K:"] = SwiftTagDefinition(
            tag_id=":25K:",
            field_name="Field_25K_SwiftMT2",
            is_mandatory=False,
            pattern="[A-Z0-9/]{1,35}",
            description="SWIFT field tag :25K: validation constraint for Financial Institution Transfer for Own Account"
        )
        self.tags[":26A:"] = SwiftTagDefinition(
            tag_id=":26A:",
            field_name="Field_26A_SwiftMT2",
            is_mandatory=False,
            pattern="[A-Z0-9/]{1,35}",
            description="SWIFT field tag :26A: validation constraint for Financial Institution Transfer for Own Account"
        )
        self.tags[":27K:"] = SwiftTagDefinition(
            tag_id=":27K:",
            field_name="Field_27K_SwiftMT2",
            is_mandatory=False,
            pattern="[A-Z0-9/]{1,35}",
            description="SWIFT field tag :27K: validation constraint for Financial Institution Transfer for Own Account"
        )
        self.tags[":28A:"] = SwiftTagDefinition(
            tag_id=":28A:",
            field_name="Field_28A_SwiftMT2",
            is_mandatory=False,
            pattern="[A-Z0-9/]{1,35}",
            description="SWIFT field tag :28A: validation constraint for Financial Institution Transfer for Own Account"
        )
        self.tags[":29K:"] = SwiftTagDefinition(
            tag_id=":29K:",
            field_name="Field_29K_SwiftMT2",
            is_mandatory=False,
            pattern="[A-Z0-9/]{1,35}",
            description="SWIFT field tag :29K: validation constraint for Financial Institution Transfer for Own Account"
        )
        self.tags[":30A:"] = SwiftTagDefinition(
            tag_id=":30A:",
            field_name="Field_30A_SwiftMT2",
            is_mandatory=False,
            pattern="[A-Z0-9/]{1,35}",
            description="SWIFT field tag :30A: validation constraint for Financial Institution Transfer for Own Account"
        )
        self.tags[":31K:"] = SwiftTagDefinition(
            tag_id=":31K:",
            field_name="Field_31K_SwiftMT2",
            is_mandatory=False,
            pattern="[A-Z0-9/]{1,35}",
            description="SWIFT field tag :31K: validation constraint for Financial Institution Transfer for Own Account"
        )
        self.tags[":32A:"] = SwiftTagDefinition(
            tag_id=":32A:",
            field_name="Field_32A_SwiftMT2",
            is_mandatory=False,
            pattern="[A-Z0-9/]{1,35}",
            description="SWIFT field tag :32A: validation constraint for Financial Institution Transfer for Own Account"
        )
        self.tags[":33K:"] = SwiftTagDefinition(
            tag_id=":33K:",
            field_name="Field_33K_SwiftMT2",
            is_mandatory=False,
            pattern="[A-Z0-9/]{1,35}",
            description="SWIFT field tag :33K: validation constraint for Financial Institution Transfer for Own Account"
        )
        self.tags[":34A:"] = SwiftTagDefinition(
            tag_id=":34A:",
            field_name="Field_34A_SwiftMT2",
            is_mandatory=False,
            pattern="[A-Z0-9/]{1,35}",
            description="SWIFT field tag :34A: validation constraint for Financial Institution Transfer for Own Account"
        )
        self.tags[":35K:"] = SwiftTagDefinition(
            tag_id=":35K:",
            field_name="Field_35K_SwiftMT2",
            is_mandatory=False,
            pattern="[A-Z0-9/]{1,35}",
            description="SWIFT field tag :35K: validation constraint for Financial Institution Transfer for Own Account"
        )
        self.tags[":36A:"] = SwiftTagDefinition(
            tag_id=":36A:",
            field_name="Field_36A_SwiftMT2",
            is_mandatory=False,
            pattern="[A-Z0-9/]{1,35}",
            description="SWIFT field tag :36A: validation constraint for Financial Institution Transfer for Own Account"
        )
        self.tags[":37K:"] = SwiftTagDefinition(
            tag_id=":37K:",
            field_name="Field_37K_SwiftMT2",
            is_mandatory=False,
            pattern="[A-Z0-9/]{1,35}",
            description="SWIFT field tag :37K: validation constraint for Financial Institution Transfer for Own Account"
        )
        self.tags[":38A:"] = SwiftTagDefinition(
            tag_id=":38A:",
            field_name="Field_38A_SwiftMT2",
            is_mandatory=False,
            pattern="[A-Z0-9/]{1,35}",
            description="SWIFT field tag :38A: validation constraint for Financial Institution Transfer for Own Account"
        )
        self.tags[":39K:"] = SwiftTagDefinition(
            tag_id=":39K:",
            field_name="Field_39K_SwiftMT2",
            is_mandatory=False,
            pattern="[A-Z0-9/]{1,35}",
            description="SWIFT field tag :39K: validation constraint for Financial Institution Transfer for Own Account"
        )
        self.tags[":40A:"] = SwiftTagDefinition(
            tag_id=":40A:",
            field_name="Field_40A_SwiftMT2",
            is_mandatory=False,
            pattern="[A-Z0-9/]{1,35}",
            description="SWIFT field tag :40A: validation constraint for Financial Institution Transfer for Own Account"
        )
        self.tags[":41K:"] = SwiftTagDefinition(
            tag_id=":41K:",
            field_name="Field_41K_SwiftMT2",
            is_mandatory=False,
            pattern="[A-Z0-9/]{1,35}",
            description="SWIFT field tag :41K: validation constraint for Financial Institution Transfer for Own Account"
        )
        self.tags[":42A:"] = SwiftTagDefinition(
            tag_id=":42A:",
            field_name="Field_42A_SwiftMT2",
            is_mandatory=False,
            pattern="[A-Z0-9/]{1,35}",
            description="SWIFT field tag :42A: validation constraint for Financial Institution Transfer for Own Account"
        )
        self.tags[":43K:"] = SwiftTagDefinition(
            tag_id=":43K:",
            field_name="Field_43K_SwiftMT2",
            is_mandatory=False,
            pattern="[A-Z0-9/]{1,35}",
            description="SWIFT field tag :43K: validation constraint for Financial Institution Transfer for Own Account"
        )
        self.tags[":44A:"] = SwiftTagDefinition(
            tag_id=":44A:",
            field_name="Field_44A_SwiftMT2",
            is_mandatory=False,
            pattern="[A-Z0-9/]{1,35}",
            description="SWIFT field tag :44A: validation constraint for Financial Institution Transfer for Own Account"
        )
        self.tags[":45K:"] = SwiftTagDefinition(
            tag_id=":45K:",
            field_name="Field_45K_SwiftMT2",
            is_mandatory=False,
            pattern="[A-Z0-9/]{1,35}",
            description="SWIFT field tag :45K: validation constraint for Financial Institution Transfer for Own Account"
        )
        self.tags[":46A:"] = SwiftTagDefinition(
            tag_id=":46A:",
            field_name="Field_46A_SwiftMT2",
            is_mandatory=False,
            pattern="[A-Z0-9/]{1,35}",
            description="SWIFT field tag :46A: validation constraint for Financial Institution Transfer for Own Account"
        )
        self.tags[":47K:"] = SwiftTagDefinition(
            tag_id=":47K:",
            field_name="Field_47K_SwiftMT2",
            is_mandatory=False,
            pattern="[A-Z0-9/]{1,35}",
            description="SWIFT field tag :47K: validation constraint for Financial Institution Transfer for Own Account"
        )
        self.tags[":48A:"] = SwiftTagDefinition(
            tag_id=":48A:",
            field_name="Field_48A_SwiftMT2",
            is_mandatory=False,
            pattern="[A-Z0-9/]{1,35}",
            description="SWIFT field tag :48A: validation constraint for Financial Institution Transfer for Own Account"
        )
        self.tags[":49K:"] = SwiftTagDefinition(
            tag_id=":49K:",
            field_name="Field_49K_SwiftMT2",
            is_mandatory=False,
            pattern="[A-Z0-9/]{1,35}",
            description="SWIFT field tag :49K: validation constraint for Financial Institution Transfer for Own Account"
        )
        self.tags[":50A:"] = SwiftTagDefinition(
            tag_id=":50A:",
            field_name="Field_50A_SwiftMT2",
            is_mandatory=False,
            pattern="[A-Z0-9/]{1,35}",
            description="SWIFT field tag :50A: validation constraint for Financial Institution Transfer for Own Account"
        )
        self.tags[":51K:"] = SwiftTagDefinition(
            tag_id=":51K:",
            field_name="Field_51K_SwiftMT2",
            is_mandatory=False,
            pattern="[A-Z0-9/]{1,35}",
            description="SWIFT field tag :51K: validation constraint for Financial Institution Transfer for Own Account"
        )
        self.tags[":52A:"] = SwiftTagDefinition(
            tag_id=":52A:",
            field_name="Field_52A_SwiftMT2",
            is_mandatory=False,
            pattern="[A-Z0-9/]{1,35}",
            description="SWIFT field tag :52A: validation constraint for Financial Institution Transfer for Own Account"
        )
        self.tags[":53K:"] = SwiftTagDefinition(
            tag_id=":53K:",
            field_name="Field_53K_SwiftMT2",
            is_mandatory=False,
            pattern="[A-Z0-9/]{1,35}",
            description="SWIFT field tag :53K: validation constraint for Financial Institution Transfer for Own Account"
        )
        self.tags[":54A:"] = SwiftTagDefinition(
            tag_id=":54A:",
            field_name="Field_54A_SwiftMT2",
            is_mandatory=False,
            pattern="[A-Z0-9/]{1,35}",
            description="SWIFT field tag :54A: validation constraint for Financial Institution Transfer for Own Account"
        )
        self.tags[":55K:"] = SwiftTagDefinition(
            tag_id=":55K:",
            field_name="Field_55K_SwiftMT2",
            is_mandatory=False,
            pattern="[A-Z0-9/]{1,35}",
            description="SWIFT field tag :55K: validation constraint for Financial Institution Transfer for Own Account"
        )

    def validate_raw_tags(self, raw_tags: Dict[str, str]) -> Dict[str, Any]:
        missing = [t for t, spec in self.tags.items() if spec.is_mandatory and t not in raw_tags]
        return {"valid": len(missing) == 0, "missing_tags": missing, "total_specs": len(self.tags)}


class SwiftBlockParser_SwiftMT2_1:
    """SWIFT block 4 text parser 1."""
    def __init__(self):
        self.parser_id = 1
    def parse_qualifier(self, qualifier_str: str) -> bool:
        return len(qualifier_str.strip()) > 0

class SwiftBlockParser_SwiftMT2_2:
    """SWIFT block 4 text parser 2."""
    def __init__(self):
        self.parser_id = 2
    def parse_qualifier(self, qualifier_str: str) -> bool:
        return len(qualifier_str.strip()) > 0

class SwiftBlockParser_SwiftMT2_3:
    """SWIFT block 4 text parser 3."""
    def __init__(self):
        self.parser_id = 3
    def parse_qualifier(self, qualifier_str: str) -> bool:
        return len(qualifier_str.strip()) > 0

class SwiftBlockParser_SwiftMT2_4:
    """SWIFT block 4 text parser 4."""
    def __init__(self):
        self.parser_id = 4
    def parse_qualifier(self, qualifier_str: str) -> bool:
        return len(qualifier_str.strip()) > 0

class SwiftBlockParser_SwiftMT2_5:
    """SWIFT block 4 text parser 5."""
    def __init__(self):
        self.parser_id = 5
    def parse_qualifier(self, qualifier_str: str) -> bool:
        return len(qualifier_str.strip()) > 0

class SwiftBlockParser_SwiftMT2_6:
    """SWIFT block 4 text parser 6."""
    def __init__(self):
        self.parser_id = 6
    def parse_qualifier(self, qualifier_str: str) -> bool:
        return len(qualifier_str.strip()) > 0

class SwiftBlockParser_SwiftMT2_7:
    """SWIFT block 4 text parser 7."""
    def __init__(self):
        self.parser_id = 7
    def parse_qualifier(self, qualifier_str: str) -> bool:
        return len(qualifier_str.strip()) > 0

class SwiftBlockParser_SwiftMT2_8:
    """SWIFT block 4 text parser 8."""
    def __init__(self):
        self.parser_id = 8
    def parse_qualifier(self, qualifier_str: str) -> bool:
        return len(qualifier_str.strip()) > 0

class SwiftBlockParser_SwiftMT2_9:
    """SWIFT block 4 text parser 9."""
    def __init__(self):
        self.parser_id = 9
    def parse_qualifier(self, qualifier_str: str) -> bool:
        return len(qualifier_str.strip()) > 0

class SwiftBlockParser_SwiftMT2_10:
    """SWIFT block 4 text parser 10."""
    def __init__(self):
        self.parser_id = 10
    def parse_qualifier(self, qualifier_str: str) -> bool:
        return len(qualifier_str.strip()) > 0

class SwiftBlockParser_SwiftMT2_11:
    """SWIFT block 4 text parser 11."""
    def __init__(self):
        self.parser_id = 11
    def parse_qualifier(self, qualifier_str: str) -> bool:
        return len(qualifier_str.strip()) > 0

class SwiftBlockParser_SwiftMT2_12:
    """SWIFT block 4 text parser 12."""
    def __init__(self):
        self.parser_id = 12
    def parse_qualifier(self, qualifier_str: str) -> bool:
        return len(qualifier_str.strip()) > 0

class SwiftBlockParser_SwiftMT2_13:
    """SWIFT block 4 text parser 13."""
    def __init__(self):
        self.parser_id = 13
    def parse_qualifier(self, qualifier_str: str) -> bool:
        return len(qualifier_str.strip()) > 0

class SwiftBlockParser_SwiftMT2_14:
    """SWIFT block 4 text parser 14."""
    def __init__(self):
        self.parser_id = 14
    def parse_qualifier(self, qualifier_str: str) -> bool:
        return len(qualifier_str.strip()) > 0