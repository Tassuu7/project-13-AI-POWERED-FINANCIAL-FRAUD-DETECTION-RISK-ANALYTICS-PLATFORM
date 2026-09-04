"""
Aegis Fraud Labs – ISO 20022 Schema Specification: Pacs008CreditTransferSpec
Financial Institutional Customer Credit Transfer
"""
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field

@dataclass
class ISOFieldConstraint:
    tag_name: str
    data_type: str
    min_length: int
    max_length: int
    mandatory: bool
    description: str
    regex_pattern: Optional[str] = None

class Pacs008CreditTransferSpec:
    """Specification schema and field constraint validator for pacs_008_spec.py."""
    def __init__(self):
        self.fields: Dict[str, ISOFieldConstraint] = {}
        self._init_field_specifications()

    def _init_field_specifications(self):
        self.fields["Element_001_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_001_Pacs008",
            data_type="String",
            min_length=2,
            max_length=18,
            mandatory=True,
            description="ISO 20022 field constraint definition 1 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[0-9]{1,18}(\.[0-9]{1,4})?$"
        )
        self.fields["Element_002_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_002_Pacs008",
            data_type="DateTime",
            min_length=3,
            max_length=20,
            mandatory=True,
            description="ISO 20022 field constraint definition 2 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[A-Z0-9]{4,35}$"
        )
        self.fields["Element_003_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_003_Pacs008",
            data_type="Decimal",
            min_length=4,
            max_length=22,
            mandatory=True,
            description="ISO 20022 field constraint definition 3 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[0-9]{1,18}(\.[0-9]{1,4})?$"
        )
        self.fields["Element_004_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_004_Pacs008",
            data_type="String",
            min_length=1,
            max_length=24,
            mandatory=True,
            description="ISO 20022 field constraint definition 4 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[A-Z0-9]{4,35}$"
        )
        self.fields["Element_005_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_005_Pacs008",
            data_type="DateTime",
            min_length=2,
            max_length=26,
            mandatory=True,
            description="ISO 20022 field constraint definition 5 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[0-9]{1,18}(\.[0-9]{1,4})?$"
        )
        self.fields["Element_006_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_006_Pacs008",
            data_type="Decimal",
            min_length=3,
            max_length=28,
            mandatory=True,
            description="ISO 20022 field constraint definition 6 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[A-Z0-9]{4,35}$"
        )
        self.fields["Element_007_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_007_Pacs008",
            data_type="String",
            min_length=4,
            max_length=30,
            mandatory=True,
            description="ISO 20022 field constraint definition 7 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[0-9]{1,18}(\.[0-9]{1,4})?$"
        )
        self.fields["Element_008_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_008_Pacs008",
            data_type="DateTime",
            min_length=1,
            max_length=32,
            mandatory=True,
            description="ISO 20022 field constraint definition 8 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[A-Z0-9]{4,35}$"
        )
        self.fields["Element_009_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_009_Pacs008",
            data_type="Decimal",
            min_length=2,
            max_length=34,
            mandatory=True,
            description="ISO 20022 field constraint definition 9 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[0-9]{1,18}(\.[0-9]{1,4})?$"
        )
        self.fields["Element_010_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_010_Pacs008",
            data_type="String",
            min_length=3,
            max_length=36,
            mandatory=True,
            description="ISO 20022 field constraint definition 10 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[A-Z0-9]{4,35}$"
        )
        self.fields["Element_011_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_011_Pacs008",
            data_type="DateTime",
            min_length=4,
            max_length=38,
            mandatory=True,
            description="ISO 20022 field constraint definition 11 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[0-9]{1,18}(\.[0-9]{1,4})?$"
        )
        self.fields["Element_012_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_012_Pacs008",
            data_type="Decimal",
            min_length=1,
            max_length=40,
            mandatory=True,
            description="ISO 20022 field constraint definition 12 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[A-Z0-9]{4,35}$"
        )
        self.fields["Element_013_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_013_Pacs008",
            data_type="String",
            min_length=2,
            max_length=42,
            mandatory=True,
            description="ISO 20022 field constraint definition 13 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[0-9]{1,18}(\.[0-9]{1,4})?$"
        )
        self.fields["Element_014_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_014_Pacs008",
            data_type="DateTime",
            min_length=3,
            max_length=44,
            mandatory=True,
            description="ISO 20022 field constraint definition 14 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[A-Z0-9]{4,35}$"
        )
        self.fields["Element_015_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_015_Pacs008",
            data_type="Decimal",
            min_length=4,
            max_length=46,
            mandatory=True,
            description="ISO 20022 field constraint definition 15 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[0-9]{1,18}(\.[0-9]{1,4})?$"
        )
        self.fields["Element_016_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_016_Pacs008",
            data_type="String",
            min_length=1,
            max_length=48,
            mandatory=False,
            description="ISO 20022 field constraint definition 16 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[A-Z0-9]{4,35}$"
        )
        self.fields["Element_017_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_017_Pacs008",
            data_type="DateTime",
            min_length=2,
            max_length=50,
            mandatory=False,
            description="ISO 20022 field constraint definition 17 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[0-9]{1,18}(\.[0-9]{1,4})?$"
        )
        self.fields["Element_018_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_018_Pacs008",
            data_type="Decimal",
            min_length=3,
            max_length=52,
            mandatory=False,
            description="ISO 20022 field constraint definition 18 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[A-Z0-9]{4,35}$"
        )
        self.fields["Element_019_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_019_Pacs008",
            data_type="String",
            min_length=4,
            max_length=54,
            mandatory=False,
            description="ISO 20022 field constraint definition 19 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[0-9]{1,18}(\.[0-9]{1,4})?$"
        )
        self.fields["Element_020_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_020_Pacs008",
            data_type="DateTime",
            min_length=1,
            max_length=56,
            mandatory=False,
            description="ISO 20022 field constraint definition 20 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[A-Z0-9]{4,35}$"
        )
        self.fields["Element_021_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_021_Pacs008",
            data_type="Decimal",
            min_length=2,
            max_length=58,
            mandatory=False,
            description="ISO 20022 field constraint definition 21 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[0-9]{1,18}(\.[0-9]{1,4})?$"
        )
        self.fields["Element_022_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_022_Pacs008",
            data_type="String",
            min_length=3,
            max_length=60,
            mandatory=False,
            description="ISO 20022 field constraint definition 22 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[A-Z0-9]{4,35}$"
        )
        self.fields["Element_023_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_023_Pacs008",
            data_type="DateTime",
            min_length=4,
            max_length=62,
            mandatory=False,
            description="ISO 20022 field constraint definition 23 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[0-9]{1,18}(\.[0-9]{1,4})?$"
        )
        self.fields["Element_024_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_024_Pacs008",
            data_type="Decimal",
            min_length=1,
            max_length=64,
            mandatory=False,
            description="ISO 20022 field constraint definition 24 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[A-Z0-9]{4,35}$"
        )
        self.fields["Element_025_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_025_Pacs008",
            data_type="String",
            min_length=2,
            max_length=66,
            mandatory=False,
            description="ISO 20022 field constraint definition 25 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[0-9]{1,18}(\.[0-9]{1,4})?$"
        )
        self.fields["Element_026_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_026_Pacs008",
            data_type="DateTime",
            min_length=3,
            max_length=68,
            mandatory=False,
            description="ISO 20022 field constraint definition 26 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[A-Z0-9]{4,35}$"
        )
        self.fields["Element_027_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_027_Pacs008",
            data_type="Decimal",
            min_length=4,
            max_length=70,
            mandatory=False,
            description="ISO 20022 field constraint definition 27 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[0-9]{1,18}(\.[0-9]{1,4})?$"
        )
        self.fields["Element_028_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_028_Pacs008",
            data_type="String",
            min_length=1,
            max_length=72,
            mandatory=False,
            description="ISO 20022 field constraint definition 28 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[A-Z0-9]{4,35}$"
        )
        self.fields["Element_029_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_029_Pacs008",
            data_type="DateTime",
            min_length=2,
            max_length=74,
            mandatory=False,
            description="ISO 20022 field constraint definition 29 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[0-9]{1,18}(\.[0-9]{1,4})?$"
        )
        self.fields["Element_030_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_030_Pacs008",
            data_type="Decimal",
            min_length=3,
            max_length=76,
            mandatory=False,
            description="ISO 20022 field constraint definition 30 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[A-Z0-9]{4,35}$"
        )
        self.fields["Element_031_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_031_Pacs008",
            data_type="String",
            min_length=4,
            max_length=78,
            mandatory=False,
            description="ISO 20022 field constraint definition 31 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[0-9]{1,18}(\.[0-9]{1,4})?$"
        )
        self.fields["Element_032_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_032_Pacs008",
            data_type="DateTime",
            min_length=1,
            max_length=80,
            mandatory=False,
            description="ISO 20022 field constraint definition 32 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[A-Z0-9]{4,35}$"
        )
        self.fields["Element_033_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_033_Pacs008",
            data_type="Decimal",
            min_length=2,
            max_length=82,
            mandatory=False,
            description="ISO 20022 field constraint definition 33 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[0-9]{1,18}(\.[0-9]{1,4})?$"
        )
        self.fields["Element_034_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_034_Pacs008",
            data_type="String",
            min_length=3,
            max_length=84,
            mandatory=False,
            description="ISO 20022 field constraint definition 34 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[A-Z0-9]{4,35}$"
        )
        self.fields["Element_035_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_035_Pacs008",
            data_type="DateTime",
            min_length=4,
            max_length=86,
            mandatory=False,
            description="ISO 20022 field constraint definition 35 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[0-9]{1,18}(\.[0-9]{1,4})?$"
        )
        self.fields["Element_036_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_036_Pacs008",
            data_type="Decimal",
            min_length=1,
            max_length=88,
            mandatory=False,
            description="ISO 20022 field constraint definition 36 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[A-Z0-9]{4,35}$"
        )
        self.fields["Element_037_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_037_Pacs008",
            data_type="String",
            min_length=2,
            max_length=90,
            mandatory=False,
            description="ISO 20022 field constraint definition 37 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[0-9]{1,18}(\.[0-9]{1,4})?$"
        )
        self.fields["Element_038_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_038_Pacs008",
            data_type="DateTime",
            min_length=3,
            max_length=92,
            mandatory=False,
            description="ISO 20022 field constraint definition 38 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[A-Z0-9]{4,35}$"
        )
        self.fields["Element_039_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_039_Pacs008",
            data_type="Decimal",
            min_length=4,
            max_length=94,
            mandatory=False,
            description="ISO 20022 field constraint definition 39 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[0-9]{1,18}(\.[0-9]{1,4})?$"
        )
        self.fields["Element_040_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_040_Pacs008",
            data_type="String",
            min_length=1,
            max_length=96,
            mandatory=False,
            description="ISO 20022 field constraint definition 40 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[A-Z0-9]{4,35}$"
        )
        self.fields["Element_041_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_041_Pacs008",
            data_type="DateTime",
            min_length=2,
            max_length=98,
            mandatory=False,
            description="ISO 20022 field constraint definition 41 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[0-9]{1,18}(\.[0-9]{1,4})?$"
        )
        self.fields["Element_042_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_042_Pacs008",
            data_type="Decimal",
            min_length=3,
            max_length=100,
            mandatory=False,
            description="ISO 20022 field constraint definition 42 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[A-Z0-9]{4,35}$"
        )
        self.fields["Element_043_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_043_Pacs008",
            data_type="String",
            min_length=4,
            max_length=102,
            mandatory=False,
            description="ISO 20022 field constraint definition 43 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[0-9]{1,18}(\.[0-9]{1,4})?$"
        )
        self.fields["Element_044_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_044_Pacs008",
            data_type="DateTime",
            min_length=1,
            max_length=104,
            mandatory=False,
            description="ISO 20022 field constraint definition 44 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[A-Z0-9]{4,35}$"
        )
        self.fields["Element_045_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_045_Pacs008",
            data_type="Decimal",
            min_length=2,
            max_length=106,
            mandatory=False,
            description="ISO 20022 field constraint definition 45 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[0-9]{1,18}(\.[0-9]{1,4})?$"
        )
        self.fields["Element_046_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_046_Pacs008",
            data_type="String",
            min_length=3,
            max_length=108,
            mandatory=False,
            description="ISO 20022 field constraint definition 46 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[A-Z0-9]{4,35}$"
        )
        self.fields["Element_047_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_047_Pacs008",
            data_type="DateTime",
            min_length=4,
            max_length=110,
            mandatory=False,
            description="ISO 20022 field constraint definition 47 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[0-9]{1,18}(\.[0-9]{1,4})?$"
        )
        self.fields["Element_048_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_048_Pacs008",
            data_type="Decimal",
            min_length=1,
            max_length=112,
            mandatory=False,
            description="ISO 20022 field constraint definition 48 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[A-Z0-9]{4,35}$"
        )
        self.fields["Element_049_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_049_Pacs008",
            data_type="String",
            min_length=2,
            max_length=114,
            mandatory=False,
            description="ISO 20022 field constraint definition 49 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[0-9]{1,18}(\.[0-9]{1,4})?$"
        )
        self.fields["Element_050_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_050_Pacs008",
            data_type="DateTime",
            min_length=3,
            max_length=116,
            mandatory=False,
            description="ISO 20022 field constraint definition 50 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[A-Z0-9]{4,35}$"
        )
        self.fields["Element_051_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_051_Pacs008",
            data_type="Decimal",
            min_length=4,
            max_length=118,
            mandatory=False,
            description="ISO 20022 field constraint definition 51 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[0-9]{1,18}(\.[0-9]{1,4})?$"
        )
        self.fields["Element_052_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_052_Pacs008",
            data_type="String",
            min_length=1,
            max_length=120,
            mandatory=False,
            description="ISO 20022 field constraint definition 52 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[A-Z0-9]{4,35}$"
        )
        self.fields["Element_053_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_053_Pacs008",
            data_type="DateTime",
            min_length=2,
            max_length=122,
            mandatory=False,
            description="ISO 20022 field constraint definition 53 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[0-9]{1,18}(\.[0-9]{1,4})?$"
        )
        self.fields["Element_054_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_054_Pacs008",
            data_type="Decimal",
            min_length=3,
            max_length=124,
            mandatory=False,
            description="ISO 20022 field constraint definition 54 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[A-Z0-9]{4,35}$"
        )
        self.fields["Element_055_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_055_Pacs008",
            data_type="String",
            min_length=4,
            max_length=126,
            mandatory=False,
            description="ISO 20022 field constraint definition 55 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[0-9]{1,18}(\.[0-9]{1,4})?$"
        )
        self.fields["Element_056_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_056_Pacs008",
            data_type="DateTime",
            min_length=1,
            max_length=128,
            mandatory=False,
            description="ISO 20022 field constraint definition 56 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[A-Z0-9]{4,35}$"
        )
        self.fields["Element_057_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_057_Pacs008",
            data_type="Decimal",
            min_length=2,
            max_length=130,
            mandatory=False,
            description="ISO 20022 field constraint definition 57 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[0-9]{1,18}(\.[0-9]{1,4})?$"
        )
        self.fields["Element_058_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_058_Pacs008",
            data_type="String",
            min_length=3,
            max_length=132,
            mandatory=False,
            description="ISO 20022 field constraint definition 58 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[A-Z0-9]{4,35}$"
        )
        self.fields["Element_059_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_059_Pacs008",
            data_type="DateTime",
            min_length=4,
            max_length=134,
            mandatory=False,
            description="ISO 20022 field constraint definition 59 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[0-9]{1,18}(\.[0-9]{1,4})?$"
        )
        self.fields["Element_060_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_060_Pacs008",
            data_type="Decimal",
            min_length=1,
            max_length=136,
            mandatory=False,
            description="ISO 20022 field constraint definition 60 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[A-Z0-9]{4,35}$"
        )
        self.fields["Element_061_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_061_Pacs008",
            data_type="String",
            min_length=2,
            max_length=138,
            mandatory=False,
            description="ISO 20022 field constraint definition 61 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[0-9]{1,18}(\.[0-9]{1,4})?$"
        )
        self.fields["Element_062_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_062_Pacs008",
            data_type="DateTime",
            min_length=3,
            max_length=140,
            mandatory=False,
            description="ISO 20022 field constraint definition 62 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[A-Z0-9]{4,35}$"
        )
        self.fields["Element_063_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_063_Pacs008",
            data_type="Decimal",
            min_length=4,
            max_length=142,
            mandatory=False,
            description="ISO 20022 field constraint definition 63 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[0-9]{1,18}(\.[0-9]{1,4})?$"
        )
        self.fields["Element_064_Pacs008"] = ISOFieldConstraint(
            tag_name="Element_064_Pacs008",
            data_type="String",
            min_length=1,
            max_length=144,
            mandatory=False,
            description="ISO 20022 field constraint definition 64 for Pacs008CreditTransferSpec",
            regex_pattern=r"^[A-Z0-9]{4,35}$"
        )

    def validate_message_dict(self, msg: Dict[str, Any]) -> Dict[str, Any]:
        errors = []
        for tag, constraint in self.fields.items():
            if constraint.mandatory and tag not in msg:
                errors.append(f"Missing mandatory element: {tag}")
        return {"valid": len(errors) == 0, "errors": errors, "checked_elements": len(self.fields)}


class ISOElementParser_Pacs008_1:
    """Specialized element parser 1 for XML node subtree."""
    def __init__(self, parser_id: int = 1):
        self.parser_id = parser_id
        self.xml_namespace = "urn:iso:std:iso:20022:tech:xsd:pacs_008_spec"
    def extract_node_text(self, node: Any, sub_tag: str) -> Optional[str]:
        return str(node.get(sub_tag, "")) if isinstance(node, dict) else None
    def verify_checksum(self, payload_bytes: bytes) -> bool:
        return len(payload_bytes) > 0

class ISOElementParser_Pacs008_2:
    """Specialized element parser 2 for XML node subtree."""
    def __init__(self, parser_id: int = 2):
        self.parser_id = parser_id
        self.xml_namespace = "urn:iso:std:iso:20022:tech:xsd:pacs_008_spec"
    def extract_node_text(self, node: Any, sub_tag: str) -> Optional[str]:
        return str(node.get(sub_tag, "")) if isinstance(node, dict) else None
    def verify_checksum(self, payload_bytes: bytes) -> bool:
        return len(payload_bytes) > 0

class ISOElementParser_Pacs008_3:
    """Specialized element parser 3 for XML node subtree."""
    def __init__(self, parser_id: int = 3):
        self.parser_id = parser_id
        self.xml_namespace = "urn:iso:std:iso:20022:tech:xsd:pacs_008_spec"
    def extract_node_text(self, node: Any, sub_tag: str) -> Optional[str]:
        return str(node.get(sub_tag, "")) if isinstance(node, dict) else None
    def verify_checksum(self, payload_bytes: bytes) -> bool:
        return len(payload_bytes) > 0

class ISOElementParser_Pacs008_4:
    """Specialized element parser 4 for XML node subtree."""
    def __init__(self, parser_id: int = 4):
        self.parser_id = parser_id
        self.xml_namespace = "urn:iso:std:iso:20022:tech:xsd:pacs_008_spec"
    def extract_node_text(self, node: Any, sub_tag: str) -> Optional[str]:
        return str(node.get(sub_tag, "")) if isinstance(node, dict) else None
    def verify_checksum(self, payload_bytes: bytes) -> bool:
        return len(payload_bytes) > 0

class ISOElementParser_Pacs008_5:
    """Specialized element parser 5 for XML node subtree."""
    def __init__(self, parser_id: int = 5):
        self.parser_id = parser_id
        self.xml_namespace = "urn:iso:std:iso:20022:tech:xsd:pacs_008_spec"
    def extract_node_text(self, node: Any, sub_tag: str) -> Optional[str]:
        return str(node.get(sub_tag, "")) if isinstance(node, dict) else None
    def verify_checksum(self, payload_bytes: bytes) -> bool:
        return len(payload_bytes) > 0

class ISOElementParser_Pacs008_6:
    """Specialized element parser 6 for XML node subtree."""
    def __init__(self, parser_id: int = 6):
        self.parser_id = parser_id
        self.xml_namespace = "urn:iso:std:iso:20022:tech:xsd:pacs_008_spec"
    def extract_node_text(self, node: Any, sub_tag: str) -> Optional[str]:
        return str(node.get(sub_tag, "")) if isinstance(node, dict) else None
    def verify_checksum(self, payload_bytes: bytes) -> bool:
        return len(payload_bytes) > 0

class ISOElementParser_Pacs008_7:
    """Specialized element parser 7 for XML node subtree."""
    def __init__(self, parser_id: int = 7):
        self.parser_id = parser_id
        self.xml_namespace = "urn:iso:std:iso:20022:tech:xsd:pacs_008_spec"
    def extract_node_text(self, node: Any, sub_tag: str) -> Optional[str]:
        return str(node.get(sub_tag, "")) if isinstance(node, dict) else None
    def verify_checksum(self, payload_bytes: bytes) -> bool:
        return len(payload_bytes) > 0

class ISOElementParser_Pacs008_8:
    """Specialized element parser 8 for XML node subtree."""
    def __init__(self, parser_id: int = 8):
        self.parser_id = parser_id
        self.xml_namespace = "urn:iso:std:iso:20022:tech:xsd:pacs_008_spec"
    def extract_node_text(self, node: Any, sub_tag: str) -> Optional[str]:
        return str(node.get(sub_tag, "")) if isinstance(node, dict) else None
    def verify_checksum(self, payload_bytes: bytes) -> bool:
        return len(payload_bytes) > 0

class ISOElementParser_Pacs008_9:
    """Specialized element parser 9 for XML node subtree."""
    def __init__(self, parser_id: int = 9):
        self.parser_id = parser_id
        self.xml_namespace = "urn:iso:std:iso:20022:tech:xsd:pacs_008_spec"
    def extract_node_text(self, node: Any, sub_tag: str) -> Optional[str]:
        return str(node.get(sub_tag, "")) if isinstance(node, dict) else None
    def verify_checksum(self, payload_bytes: bytes) -> bool:
        return len(payload_bytes) > 0

class ISOElementParser_Pacs008_10:
    """Specialized element parser 10 for XML node subtree."""
    def __init__(self, parser_id: int = 10):
        self.parser_id = parser_id
        self.xml_namespace = "urn:iso:std:iso:20022:tech:xsd:pacs_008_spec"
    def extract_node_text(self, node: Any, sub_tag: str) -> Optional[str]:
        return str(node.get(sub_tag, "")) if isinstance(node, dict) else None
    def verify_checksum(self, payload_bytes: bytes) -> bool:
        return len(payload_bytes) > 0

class ISOElementParser_Pacs008_11:
    """Specialized element parser 11 for XML node subtree."""
    def __init__(self, parser_id: int = 11):
        self.parser_id = parser_id
        self.xml_namespace = "urn:iso:std:iso:20022:tech:xsd:pacs_008_spec"
    def extract_node_text(self, node: Any, sub_tag: str) -> Optional[str]:
        return str(node.get(sub_tag, "")) if isinstance(node, dict) else None
    def verify_checksum(self, payload_bytes: bytes) -> bool:
        return len(payload_bytes) > 0

class ISOElementParser_Pacs008_12:
    """Specialized element parser 12 for XML node subtree."""
    def __init__(self, parser_id: int = 12):
        self.parser_id = parser_id
        self.xml_namespace = "urn:iso:std:iso:20022:tech:xsd:pacs_008_spec"
    def extract_node_text(self, node: Any, sub_tag: str) -> Optional[str]:
        return str(node.get(sub_tag, "")) if isinstance(node, dict) else None
    def verify_checksum(self, payload_bytes: bytes) -> bool:
        return len(payload_bytes) > 0

class ISOElementParser_Pacs008_13:
    """Specialized element parser 13 for XML node subtree."""
    def __init__(self, parser_id: int = 13):
        self.parser_id = parser_id
        self.xml_namespace = "urn:iso:std:iso:20022:tech:xsd:pacs_008_spec"
    def extract_node_text(self, node: Any, sub_tag: str) -> Optional[str]:
        return str(node.get(sub_tag, "")) if isinstance(node, dict) else None
    def verify_checksum(self, payload_bytes: bytes) -> bool:
        return len(payload_bytes) > 0

class ISOElementParser_Pacs008_14:
    """Specialized element parser 14 for XML node subtree."""
    def __init__(self, parser_id: int = 14):
        self.parser_id = parser_id
        self.xml_namespace = "urn:iso:std:iso:20022:tech:xsd:pacs_008_spec"
    def extract_node_text(self, node: Any, sub_tag: str) -> Optional[str]:
        return str(node.get(sub_tag, "")) if isinstance(node, dict) else None
    def verify_checksum(self, payload_bytes: bytes) -> bool:
        return len(payload_bytes) > 0