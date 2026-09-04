"""
Aegis Fraud Labs – Synthetic Identity Theft Attribute Matrix
SSN area number validation, credit piggybacking detection, and multi-bureau fragmentation markers.
"""
from typing import Dict, List, Any
from dataclasses import dataclass

@dataclass
class SyntheticIdentityProfile:
    profile_id: str
    ssn_hash: str
    dob_consistency_score: float
    address_type: str
    thin_file_months: int
    revolving_utilization: float
    fraud_syndicate_cluster: str

class SyntheticIdentityMatrixCatalog:
    def __init__(self):
        self.profiles: Dict[str, SyntheticIdentityProfile] = {}
        self._init_profiles()

    def register(self, p: SyntheticIdentityProfile):
        self.profiles[p.profile_id] = p

    def _init_profiles(self):
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0001",
            ssn_hash="SSN_HASH_00017fba",
            dob_consistency_score=0.16,
            address_type="RESIDENTIAL_SINGLE_FAMILY",
            thin_file_months=1,
            revolving_utilization=0.46,
            fraud_syndicate_cluster="CLUSTER_1"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0002",
            ssn_hash="SSN_HASH_0002ff74",
            dob_consistency_score=0.17,
            address_type="MULTI_UNIT_APARTMENT",
            thin_file_months=2,
            revolving_utilization=0.47,
            fraud_syndicate_cluster="CLUSTER_2"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0003",
            ssn_hash="SSN_HASH_00047f2e",
            dob_consistency_score=0.18,
            address_type="FREIGHT_FORWARDER",
            thin_file_months=3,
            revolving_utilization=0.48,
            fraud_syndicate_cluster="CLUSTER_3"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0004",
            ssn_hash="SSN_HASH_0005fee8",
            dob_consistency_score=0.19,
            address_type="PO_BOX",
            thin_file_months=4,
            revolving_utilization=0.49,
            fraud_syndicate_cluster="CLUSTER_4"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0005",
            ssn_hash="SSN_HASH_00077ea2",
            dob_consistency_score=0.20,
            address_type="VIRTUAL_OFFICE",
            thin_file_months=5,
            revolving_utilization=0.50,
            fraud_syndicate_cluster="CLUSTER_5"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0006",
            ssn_hash="SSN_HASH_0008fe5c",
            dob_consistency_score=0.21,
            address_type="COMMERCIAL_MAIL_DROP",
            thin_file_months=6,
            revolving_utilization=0.51,
            fraud_syndicate_cluster="CLUSTER_6"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0007",
            ssn_hash="SSN_HASH_000a7e16",
            dob_consistency_score=0.22,
            address_type="RESIDENTIAL_SINGLE_FAMILY",
            thin_file_months=7,
            revolving_utilization=0.52,
            fraud_syndicate_cluster="CLUSTER_7"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0008",
            ssn_hash="SSN_HASH_000bfdd0",
            dob_consistency_score=0.23,
            address_type="MULTI_UNIT_APARTMENT",
            thin_file_months=8,
            revolving_utilization=0.53,
            fraud_syndicate_cluster="CLUSTER_8"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0009",
            ssn_hash="SSN_HASH_000d7d8a",
            dob_consistency_score=0.24,
            address_type="FREIGHT_FORWARDER",
            thin_file_months=9,
            revolving_utilization=0.54,
            fraud_syndicate_cluster="CLUSTER_9"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0010",
            ssn_hash="SSN_HASH_000efd44",
            dob_consistency_score=0.25,
            address_type="PO_BOX",
            thin_file_months=10,
            revolving_utilization=0.55,
            fraud_syndicate_cluster="CLUSTER_10"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0011",
            ssn_hash="SSN_HASH_00107cfe",
            dob_consistency_score=0.26,
            address_type="VIRTUAL_OFFICE",
            thin_file_months=11,
            revolving_utilization=0.56,
            fraud_syndicate_cluster="CLUSTER_11"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0012",
            ssn_hash="SSN_HASH_0011fcb8",
            dob_consistency_score=0.27,
            address_type="COMMERCIAL_MAIL_DROP",
            thin_file_months=12,
            revolving_utilization=0.57,
            fraud_syndicate_cluster="CLUSTER_0"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0013",
            ssn_hash="SSN_HASH_00137c72",
            dob_consistency_score=0.28,
            address_type="RESIDENTIAL_SINGLE_FAMILY",
            thin_file_months=13,
            revolving_utilization=0.58,
            fraud_syndicate_cluster="CLUSTER_1"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0014",
            ssn_hash="SSN_HASH_0014fc2c",
            dob_consistency_score=0.29,
            address_type="MULTI_UNIT_APARTMENT",
            thin_file_months=14,
            revolving_utilization=0.59,
            fraud_syndicate_cluster="CLUSTER_2"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0015",
            ssn_hash="SSN_HASH_00167be6",
            dob_consistency_score=0.30,
            address_type="FREIGHT_FORWARDER",
            thin_file_months=15,
            revolving_utilization=0.60,
            fraud_syndicate_cluster="CLUSTER_3"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0016",
            ssn_hash="SSN_HASH_0017fba0",
            dob_consistency_score=0.31,
            address_type="PO_BOX",
            thin_file_months=16,
            revolving_utilization=0.61,
            fraud_syndicate_cluster="CLUSTER_4"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0017",
            ssn_hash="SSN_HASH_00197b5a",
            dob_consistency_score=0.32,
            address_type="VIRTUAL_OFFICE",
            thin_file_months=17,
            revolving_utilization=0.62,
            fraud_syndicate_cluster="CLUSTER_5"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0018",
            ssn_hash="SSN_HASH_001afb14",
            dob_consistency_score=0.33,
            address_type="COMMERCIAL_MAIL_DROP",
            thin_file_months=18,
            revolving_utilization=0.63,
            fraud_syndicate_cluster="CLUSTER_6"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0019",
            ssn_hash="SSN_HASH_001c7ace",
            dob_consistency_score=0.34,
            address_type="RESIDENTIAL_SINGLE_FAMILY",
            thin_file_months=19,
            revolving_utilization=0.64,
            fraud_syndicate_cluster="CLUSTER_7"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0020",
            ssn_hash="SSN_HASH_001dfa88",
            dob_consistency_score=0.35,
            address_type="MULTI_UNIT_APARTMENT",
            thin_file_months=20,
            revolving_utilization=0.65,
            fraud_syndicate_cluster="CLUSTER_8"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0021",
            ssn_hash="SSN_HASH_001f7a42",
            dob_consistency_score=0.36,
            address_type="FREIGHT_FORWARDER",
            thin_file_months=21,
            revolving_utilization=0.66,
            fraud_syndicate_cluster="CLUSTER_9"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0022",
            ssn_hash="SSN_HASH_0020f9fc",
            dob_consistency_score=0.37,
            address_type="PO_BOX",
            thin_file_months=22,
            revolving_utilization=0.67,
            fraud_syndicate_cluster="CLUSTER_10"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0023",
            ssn_hash="SSN_HASH_002279b6",
            dob_consistency_score=0.38,
            address_type="VIRTUAL_OFFICE",
            thin_file_months=23,
            revolving_utilization=0.68,
            fraud_syndicate_cluster="CLUSTER_11"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0024",
            ssn_hash="SSN_HASH_0023f970",
            dob_consistency_score=0.39,
            address_type="COMMERCIAL_MAIL_DROP",
            thin_file_months=24,
            revolving_utilization=0.69,
            fraud_syndicate_cluster="CLUSTER_0"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0025",
            ssn_hash="SSN_HASH_0025792a",
            dob_consistency_score=0.40,
            address_type="RESIDENTIAL_SINGLE_FAMILY",
            thin_file_months=25,
            revolving_utilization=0.70,
            fraud_syndicate_cluster="CLUSTER_1"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0026",
            ssn_hash="SSN_HASH_0026f8e4",
            dob_consistency_score=0.41,
            address_type="MULTI_UNIT_APARTMENT",
            thin_file_months=26,
            revolving_utilization=0.71,
            fraud_syndicate_cluster="CLUSTER_2"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0027",
            ssn_hash="SSN_HASH_0028789e",
            dob_consistency_score=0.42,
            address_type="FREIGHT_FORWARDER",
            thin_file_months=27,
            revolving_utilization=0.72,
            fraud_syndicate_cluster="CLUSTER_3"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0028",
            ssn_hash="SSN_HASH_0029f858",
            dob_consistency_score=0.43,
            address_type="PO_BOX",
            thin_file_months=28,
            revolving_utilization=0.73,
            fraud_syndicate_cluster="CLUSTER_4"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0029",
            ssn_hash="SSN_HASH_002b7812",
            dob_consistency_score=0.44,
            address_type="VIRTUAL_OFFICE",
            thin_file_months=29,
            revolving_utilization=0.74,
            fraud_syndicate_cluster="CLUSTER_5"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0030",
            ssn_hash="SSN_HASH_002cf7cc",
            dob_consistency_score=0.45,
            address_type="COMMERCIAL_MAIL_DROP",
            thin_file_months=30,
            revolving_utilization=0.75,
            fraud_syndicate_cluster="CLUSTER_6"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0031",
            ssn_hash="SSN_HASH_002e7786",
            dob_consistency_score=0.46,
            address_type="RESIDENTIAL_SINGLE_FAMILY",
            thin_file_months=31,
            revolving_utilization=0.76,
            fraud_syndicate_cluster="CLUSTER_7"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0032",
            ssn_hash="SSN_HASH_002ff740",
            dob_consistency_score=0.47,
            address_type="MULTI_UNIT_APARTMENT",
            thin_file_months=32,
            revolving_utilization=0.77,
            fraud_syndicate_cluster="CLUSTER_8"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0033",
            ssn_hash="SSN_HASH_003176fa",
            dob_consistency_score=0.48,
            address_type="FREIGHT_FORWARDER",
            thin_file_months=33,
            revolving_utilization=0.78,
            fraud_syndicate_cluster="CLUSTER_9"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0034",
            ssn_hash="SSN_HASH_0032f6b4",
            dob_consistency_score=0.49,
            address_type="PO_BOX",
            thin_file_months=34,
            revolving_utilization=0.79,
            fraud_syndicate_cluster="CLUSTER_10"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0035",
            ssn_hash="SSN_HASH_0034766e",
            dob_consistency_score=0.50,
            address_type="VIRTUAL_OFFICE",
            thin_file_months=35,
            revolving_utilization=0.80,
            fraud_syndicate_cluster="CLUSTER_11"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0036",
            ssn_hash="SSN_HASH_0035f628",
            dob_consistency_score=0.51,
            address_type="COMMERCIAL_MAIL_DROP",
            thin_file_months=0,
            revolving_utilization=0.81,
            fraud_syndicate_cluster="CLUSTER_0"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0037",
            ssn_hash="SSN_HASH_003775e2",
            dob_consistency_score=0.52,
            address_type="RESIDENTIAL_SINGLE_FAMILY",
            thin_file_months=1,
            revolving_utilization=0.82,
            fraud_syndicate_cluster="CLUSTER_1"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0038",
            ssn_hash="SSN_HASH_0038f59c",
            dob_consistency_score=0.53,
            address_type="MULTI_UNIT_APARTMENT",
            thin_file_months=2,
            revolving_utilization=0.83,
            fraud_syndicate_cluster="CLUSTER_2"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0039",
            ssn_hash="SSN_HASH_003a7556",
            dob_consistency_score=0.54,
            address_type="FREIGHT_FORWARDER",
            thin_file_months=3,
            revolving_utilization=0.84,
            fraud_syndicate_cluster="CLUSTER_3"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0040",
            ssn_hash="SSN_HASH_003bf510",
            dob_consistency_score=0.55,
            address_type="PO_BOX",
            thin_file_months=4,
            revolving_utilization=0.85,
            fraud_syndicate_cluster="CLUSTER_4"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0041",
            ssn_hash="SSN_HASH_003d74ca",
            dob_consistency_score=0.56,
            address_type="VIRTUAL_OFFICE",
            thin_file_months=5,
            revolving_utilization=0.86,
            fraud_syndicate_cluster="CLUSTER_5"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0042",
            ssn_hash="SSN_HASH_003ef484",
            dob_consistency_score=0.57,
            address_type="COMMERCIAL_MAIL_DROP",
            thin_file_months=6,
            revolving_utilization=0.87,
            fraud_syndicate_cluster="CLUSTER_6"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0043",
            ssn_hash="SSN_HASH_0040743e",
            dob_consistency_score=0.58,
            address_type="RESIDENTIAL_SINGLE_FAMILY",
            thin_file_months=7,
            revolving_utilization=0.88,
            fraud_syndicate_cluster="CLUSTER_7"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0044",
            ssn_hash="SSN_HASH_0041f3f8",
            dob_consistency_score=0.59,
            address_type="MULTI_UNIT_APARTMENT",
            thin_file_months=8,
            revolving_utilization=0.89,
            fraud_syndicate_cluster="CLUSTER_8"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0045",
            ssn_hash="SSN_HASH_004373b2",
            dob_consistency_score=0.60,
            address_type="FREIGHT_FORWARDER",
            thin_file_months=9,
            revolving_utilization=0.90,
            fraud_syndicate_cluster="CLUSTER_9"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0046",
            ssn_hash="SSN_HASH_0044f36c",
            dob_consistency_score=0.61,
            address_type="PO_BOX",
            thin_file_months=10,
            revolving_utilization=0.91,
            fraud_syndicate_cluster="CLUSTER_10"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0047",
            ssn_hash="SSN_HASH_00467326",
            dob_consistency_score=0.62,
            address_type="VIRTUAL_OFFICE",
            thin_file_months=11,
            revolving_utilization=0.92,
            fraud_syndicate_cluster="CLUSTER_11"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0048",
            ssn_hash="SSN_HASH_0047f2e0",
            dob_consistency_score=0.63,
            address_type="COMMERCIAL_MAIL_DROP",
            thin_file_months=12,
            revolving_utilization=0.93,
            fraud_syndicate_cluster="CLUSTER_0"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0049",
            ssn_hash="SSN_HASH_0049729a",
            dob_consistency_score=0.64,
            address_type="RESIDENTIAL_SINGLE_FAMILY",
            thin_file_months=13,
            revolving_utilization=0.94,
            fraud_syndicate_cluster="CLUSTER_1"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0050",
            ssn_hash="SSN_HASH_004af254",
            dob_consistency_score=0.65,
            address_type="MULTI_UNIT_APARTMENT",
            thin_file_months=14,
            revolving_utilization=0.45,
            fraud_syndicate_cluster="CLUSTER_2"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0051",
            ssn_hash="SSN_HASH_004c720e",
            dob_consistency_score=0.66,
            address_type="FREIGHT_FORWARDER",
            thin_file_months=15,
            revolving_utilization=0.46,
            fraud_syndicate_cluster="CLUSTER_3"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0052",
            ssn_hash="SSN_HASH_004df1c8",
            dob_consistency_score=0.67,
            address_type="PO_BOX",
            thin_file_months=16,
            revolving_utilization=0.47,
            fraud_syndicate_cluster="CLUSTER_4"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0053",
            ssn_hash="SSN_HASH_004f7182",
            dob_consistency_score=0.68,
            address_type="VIRTUAL_OFFICE",
            thin_file_months=17,
            revolving_utilization=0.48,
            fraud_syndicate_cluster="CLUSTER_5"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0054",
            ssn_hash="SSN_HASH_0050f13c",
            dob_consistency_score=0.69,
            address_type="COMMERCIAL_MAIL_DROP",
            thin_file_months=18,
            revolving_utilization=0.49,
            fraud_syndicate_cluster="CLUSTER_6"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0055",
            ssn_hash="SSN_HASH_005270f6",
            dob_consistency_score=0.70,
            address_type="RESIDENTIAL_SINGLE_FAMILY",
            thin_file_months=19,
            revolving_utilization=0.50,
            fraud_syndicate_cluster="CLUSTER_7"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0056",
            ssn_hash="SSN_HASH_0053f0b0",
            dob_consistency_score=0.71,
            address_type="MULTI_UNIT_APARTMENT",
            thin_file_months=20,
            revolving_utilization=0.51,
            fraud_syndicate_cluster="CLUSTER_8"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0057",
            ssn_hash="SSN_HASH_0055706a",
            dob_consistency_score=0.72,
            address_type="FREIGHT_FORWARDER",
            thin_file_months=21,
            revolving_utilization=0.52,
            fraud_syndicate_cluster="CLUSTER_9"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0058",
            ssn_hash="SSN_HASH_0056f024",
            dob_consistency_score=0.73,
            address_type="PO_BOX",
            thin_file_months=22,
            revolving_utilization=0.53,
            fraud_syndicate_cluster="CLUSTER_10"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0059",
            ssn_hash="SSN_HASH_00586fde",
            dob_consistency_score=0.74,
            address_type="VIRTUAL_OFFICE",
            thin_file_months=23,
            revolving_utilization=0.54,
            fraud_syndicate_cluster="CLUSTER_11"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0060",
            ssn_hash="SSN_HASH_0059ef98",
            dob_consistency_score=0.75,
            address_type="COMMERCIAL_MAIL_DROP",
            thin_file_months=24,
            revolving_utilization=0.55,
            fraud_syndicate_cluster="CLUSTER_0"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0061",
            ssn_hash="SSN_HASH_005b6f52",
            dob_consistency_score=0.76,
            address_type="RESIDENTIAL_SINGLE_FAMILY",
            thin_file_months=25,
            revolving_utilization=0.56,
            fraud_syndicate_cluster="CLUSTER_1"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0062",
            ssn_hash="SSN_HASH_005cef0c",
            dob_consistency_score=0.77,
            address_type="MULTI_UNIT_APARTMENT",
            thin_file_months=26,
            revolving_utilization=0.57,
            fraud_syndicate_cluster="CLUSTER_2"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0063",
            ssn_hash="SSN_HASH_005e6ec6",
            dob_consistency_score=0.78,
            address_type="FREIGHT_FORWARDER",
            thin_file_months=27,
            revolving_utilization=0.58,
            fraud_syndicate_cluster="CLUSTER_3"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0064",
            ssn_hash="SSN_HASH_005fee80",
            dob_consistency_score=0.79,
            address_type="PO_BOX",
            thin_file_months=28,
            revolving_utilization=0.59,
            fraud_syndicate_cluster="CLUSTER_4"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0065",
            ssn_hash="SSN_HASH_00616e3a",
            dob_consistency_score=0.80,
            address_type="VIRTUAL_OFFICE",
            thin_file_months=29,
            revolving_utilization=0.60,
            fraud_syndicate_cluster="CLUSTER_5"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0066",
            ssn_hash="SSN_HASH_0062edf4",
            dob_consistency_score=0.81,
            address_type="COMMERCIAL_MAIL_DROP",
            thin_file_months=30,
            revolving_utilization=0.61,
            fraud_syndicate_cluster="CLUSTER_6"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0067",
            ssn_hash="SSN_HASH_00646dae",
            dob_consistency_score=0.82,
            address_type="RESIDENTIAL_SINGLE_FAMILY",
            thin_file_months=31,
            revolving_utilization=0.62,
            fraud_syndicate_cluster="CLUSTER_7"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0068",
            ssn_hash="SSN_HASH_0065ed68",
            dob_consistency_score=0.83,
            address_type="MULTI_UNIT_APARTMENT",
            thin_file_months=32,
            revolving_utilization=0.63,
            fraud_syndicate_cluster="CLUSTER_8"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0069",
            ssn_hash="SSN_HASH_00676d22",
            dob_consistency_score=0.84,
            address_type="FREIGHT_FORWARDER",
            thin_file_months=33,
            revolving_utilization=0.64,
            fraud_syndicate_cluster="CLUSTER_9"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0070",
            ssn_hash="SSN_HASH_0068ecdc",
            dob_consistency_score=0.85,
            address_type="PO_BOX",
            thin_file_months=34,
            revolving_utilization=0.65,
            fraud_syndicate_cluster="CLUSTER_10"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0071",
            ssn_hash="SSN_HASH_006a6c96",
            dob_consistency_score=0.86,
            address_type="VIRTUAL_OFFICE",
            thin_file_months=35,
            revolving_utilization=0.66,
            fraud_syndicate_cluster="CLUSTER_11"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0072",
            ssn_hash="SSN_HASH_006bec50",
            dob_consistency_score=0.87,
            address_type="COMMERCIAL_MAIL_DROP",
            thin_file_months=0,
            revolving_utilization=0.67,
            fraud_syndicate_cluster="CLUSTER_0"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0073",
            ssn_hash="SSN_HASH_006d6c0a",
            dob_consistency_score=0.88,
            address_type="RESIDENTIAL_SINGLE_FAMILY",
            thin_file_months=1,
            revolving_utilization=0.68,
            fraud_syndicate_cluster="CLUSTER_1"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0074",
            ssn_hash="SSN_HASH_006eebc4",
            dob_consistency_score=0.89,
            address_type="MULTI_UNIT_APARTMENT",
            thin_file_months=2,
            revolving_utilization=0.69,
            fraud_syndicate_cluster="CLUSTER_2"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0075",
            ssn_hash="SSN_HASH_00706b7e",
            dob_consistency_score=0.90,
            address_type="FREIGHT_FORWARDER",
            thin_file_months=3,
            revolving_utilization=0.70,
            fraud_syndicate_cluster="CLUSTER_3"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0076",
            ssn_hash="SSN_HASH_0071eb38",
            dob_consistency_score=0.91,
            address_type="PO_BOX",
            thin_file_months=4,
            revolving_utilization=0.71,
            fraud_syndicate_cluster="CLUSTER_4"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0077",
            ssn_hash="SSN_HASH_00736af2",
            dob_consistency_score=0.92,
            address_type="VIRTUAL_OFFICE",
            thin_file_months=5,
            revolving_utilization=0.72,
            fraud_syndicate_cluster="CLUSTER_5"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0078",
            ssn_hash="SSN_HASH_0074eaac",
            dob_consistency_score=0.93,
            address_type="COMMERCIAL_MAIL_DROP",
            thin_file_months=6,
            revolving_utilization=0.73,
            fraud_syndicate_cluster="CLUSTER_6"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0079",
            ssn_hash="SSN_HASH_00766a66",
            dob_consistency_score=0.94,
            address_type="RESIDENTIAL_SINGLE_FAMILY",
            thin_file_months=7,
            revolving_utilization=0.74,
            fraud_syndicate_cluster="CLUSTER_7"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0080",
            ssn_hash="SSN_HASH_0077ea20",
            dob_consistency_score=0.15,
            address_type="MULTI_UNIT_APARTMENT",
            thin_file_months=8,
            revolving_utilization=0.75,
            fraud_syndicate_cluster="CLUSTER_8"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0081",
            ssn_hash="SSN_HASH_007969da",
            dob_consistency_score=0.16,
            address_type="FREIGHT_FORWARDER",
            thin_file_months=9,
            revolving_utilization=0.76,
            fraud_syndicate_cluster="CLUSTER_9"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0082",
            ssn_hash="SSN_HASH_007ae994",
            dob_consistency_score=0.17,
            address_type="PO_BOX",
            thin_file_months=10,
            revolving_utilization=0.77,
            fraud_syndicate_cluster="CLUSTER_10"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0083",
            ssn_hash="SSN_HASH_007c694e",
            dob_consistency_score=0.18,
            address_type="VIRTUAL_OFFICE",
            thin_file_months=11,
            revolving_utilization=0.78,
            fraud_syndicate_cluster="CLUSTER_11"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0084",
            ssn_hash="SSN_HASH_007de908",
            dob_consistency_score=0.19,
            address_type="COMMERCIAL_MAIL_DROP",
            thin_file_months=12,
            revolving_utilization=0.79,
            fraud_syndicate_cluster="CLUSTER_0"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0085",
            ssn_hash="SSN_HASH_007f68c2",
            dob_consistency_score=0.20,
            address_type="RESIDENTIAL_SINGLE_FAMILY",
            thin_file_months=13,
            revolving_utilization=0.80,
            fraud_syndicate_cluster="CLUSTER_1"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0086",
            ssn_hash="SSN_HASH_0080e87c",
            dob_consistency_score=0.21,
            address_type="MULTI_UNIT_APARTMENT",
            thin_file_months=14,
            revolving_utilization=0.81,
            fraud_syndicate_cluster="CLUSTER_2"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0087",
            ssn_hash="SSN_HASH_00826836",
            dob_consistency_score=0.22,
            address_type="FREIGHT_FORWARDER",
            thin_file_months=15,
            revolving_utilization=0.82,
            fraud_syndicate_cluster="CLUSTER_3"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0088",
            ssn_hash="SSN_HASH_0083e7f0",
            dob_consistency_score=0.23,
            address_type="PO_BOX",
            thin_file_months=16,
            revolving_utilization=0.83,
            fraud_syndicate_cluster="CLUSTER_4"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0089",
            ssn_hash="SSN_HASH_008567aa",
            dob_consistency_score=0.24,
            address_type="VIRTUAL_OFFICE",
            thin_file_months=17,
            revolving_utilization=0.84,
            fraud_syndicate_cluster="CLUSTER_5"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0090",
            ssn_hash="SSN_HASH_0086e764",
            dob_consistency_score=0.25,
            address_type="COMMERCIAL_MAIL_DROP",
            thin_file_months=18,
            revolving_utilization=0.85,
            fraud_syndicate_cluster="CLUSTER_6"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0091",
            ssn_hash="SSN_HASH_0088671e",
            dob_consistency_score=0.26,
            address_type="RESIDENTIAL_SINGLE_FAMILY",
            thin_file_months=19,
            revolving_utilization=0.86,
            fraud_syndicate_cluster="CLUSTER_7"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0092",
            ssn_hash="SSN_HASH_0089e6d8",
            dob_consistency_score=0.27,
            address_type="MULTI_UNIT_APARTMENT",
            thin_file_months=20,
            revolving_utilization=0.87,
            fraud_syndicate_cluster="CLUSTER_8"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0093",
            ssn_hash="SSN_HASH_008b6692",
            dob_consistency_score=0.28,
            address_type="FREIGHT_FORWARDER",
            thin_file_months=21,
            revolving_utilization=0.88,
            fraud_syndicate_cluster="CLUSTER_9"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0094",
            ssn_hash="SSN_HASH_008ce64c",
            dob_consistency_score=0.29,
            address_type="PO_BOX",
            thin_file_months=22,
            revolving_utilization=0.89,
            fraud_syndicate_cluster="CLUSTER_10"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0095",
            ssn_hash="SSN_HASH_008e6606",
            dob_consistency_score=0.30,
            address_type="VIRTUAL_OFFICE",
            thin_file_months=23,
            revolving_utilization=0.90,
            fraud_syndicate_cluster="CLUSTER_11"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0096",
            ssn_hash="SSN_HASH_008fe5c0",
            dob_consistency_score=0.31,
            address_type="COMMERCIAL_MAIL_DROP",
            thin_file_months=24,
            revolving_utilization=0.91,
            fraud_syndicate_cluster="CLUSTER_0"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0097",
            ssn_hash="SSN_HASH_0091657a",
            dob_consistency_score=0.32,
            address_type="RESIDENTIAL_SINGLE_FAMILY",
            thin_file_months=25,
            revolving_utilization=0.92,
            fraud_syndicate_cluster="CLUSTER_1"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0098",
            ssn_hash="SSN_HASH_0092e534",
            dob_consistency_score=0.33,
            address_type="MULTI_UNIT_APARTMENT",
            thin_file_months=26,
            revolving_utilization=0.93,
            fraud_syndicate_cluster="CLUSTER_2"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0099",
            ssn_hash="SSN_HASH_009464ee",
            dob_consistency_score=0.34,
            address_type="FREIGHT_FORWARDER",
            thin_file_months=27,
            revolving_utilization=0.94,
            fraud_syndicate_cluster="CLUSTER_3"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0100",
            ssn_hash="SSN_HASH_0095e4a8",
            dob_consistency_score=0.35,
            address_type="PO_BOX",
            thin_file_months=28,
            revolving_utilization=0.45,
            fraud_syndicate_cluster="CLUSTER_4"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0101",
            ssn_hash="SSN_HASH_00976462",
            dob_consistency_score=0.36,
            address_type="VIRTUAL_OFFICE",
            thin_file_months=29,
            revolving_utilization=0.46,
            fraud_syndicate_cluster="CLUSTER_5"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0102",
            ssn_hash="SSN_HASH_0098e41c",
            dob_consistency_score=0.37,
            address_type="COMMERCIAL_MAIL_DROP",
            thin_file_months=30,
            revolving_utilization=0.47,
            fraud_syndicate_cluster="CLUSTER_6"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0103",
            ssn_hash="SSN_HASH_009a63d6",
            dob_consistency_score=0.38,
            address_type="RESIDENTIAL_SINGLE_FAMILY",
            thin_file_months=31,
            revolving_utilization=0.48,
            fraud_syndicate_cluster="CLUSTER_7"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0104",
            ssn_hash="SSN_HASH_009be390",
            dob_consistency_score=0.39,
            address_type="MULTI_UNIT_APARTMENT",
            thin_file_months=32,
            revolving_utilization=0.49,
            fraud_syndicate_cluster="CLUSTER_8"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0105",
            ssn_hash="SSN_HASH_009d634a",
            dob_consistency_score=0.40,
            address_type="FREIGHT_FORWARDER",
            thin_file_months=33,
            revolving_utilization=0.50,
            fraud_syndicate_cluster="CLUSTER_9"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0106",
            ssn_hash="SSN_HASH_009ee304",
            dob_consistency_score=0.41,
            address_type="PO_BOX",
            thin_file_months=34,
            revolving_utilization=0.51,
            fraud_syndicate_cluster="CLUSTER_10"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0107",
            ssn_hash="SSN_HASH_00a062be",
            dob_consistency_score=0.42,
            address_type="VIRTUAL_OFFICE",
            thin_file_months=35,
            revolving_utilization=0.52,
            fraud_syndicate_cluster="CLUSTER_11"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0108",
            ssn_hash="SSN_HASH_00a1e278",
            dob_consistency_score=0.43,
            address_type="COMMERCIAL_MAIL_DROP",
            thin_file_months=0,
            revolving_utilization=0.53,
            fraud_syndicate_cluster="CLUSTER_0"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0109",
            ssn_hash="SSN_HASH_00a36232",
            dob_consistency_score=0.44,
            address_type="RESIDENTIAL_SINGLE_FAMILY",
            thin_file_months=1,
            revolving_utilization=0.54,
            fraud_syndicate_cluster="CLUSTER_1"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0110",
            ssn_hash="SSN_HASH_00a4e1ec",
            dob_consistency_score=0.45,
            address_type="MULTI_UNIT_APARTMENT",
            thin_file_months=2,
            revolving_utilization=0.55,
            fraud_syndicate_cluster="CLUSTER_2"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0111",
            ssn_hash="SSN_HASH_00a661a6",
            dob_consistency_score=0.46,
            address_type="FREIGHT_FORWARDER",
            thin_file_months=3,
            revolving_utilization=0.56,
            fraud_syndicate_cluster="CLUSTER_3"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0112",
            ssn_hash="SSN_HASH_00a7e160",
            dob_consistency_score=0.47,
            address_type="PO_BOX",
            thin_file_months=4,
            revolving_utilization=0.57,
            fraud_syndicate_cluster="CLUSTER_4"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0113",
            ssn_hash="SSN_HASH_00a9611a",
            dob_consistency_score=0.48,
            address_type="VIRTUAL_OFFICE",
            thin_file_months=5,
            revolving_utilization=0.58,
            fraud_syndicate_cluster="CLUSTER_5"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0114",
            ssn_hash="SSN_HASH_00aae0d4",
            dob_consistency_score=0.49,
            address_type="COMMERCIAL_MAIL_DROP",
            thin_file_months=6,
            revolving_utilization=0.59,
            fraud_syndicate_cluster="CLUSTER_6"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0115",
            ssn_hash="SSN_HASH_00ac608e",
            dob_consistency_score=0.50,
            address_type="RESIDENTIAL_SINGLE_FAMILY",
            thin_file_months=7,
            revolving_utilization=0.60,
            fraud_syndicate_cluster="CLUSTER_7"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0116",
            ssn_hash="SSN_HASH_00ade048",
            dob_consistency_score=0.51,
            address_type="MULTI_UNIT_APARTMENT",
            thin_file_months=8,
            revolving_utilization=0.61,
            fraud_syndicate_cluster="CLUSTER_8"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0117",
            ssn_hash="SSN_HASH_00af6002",
            dob_consistency_score=0.52,
            address_type="FREIGHT_FORWARDER",
            thin_file_months=9,
            revolving_utilization=0.62,
            fraud_syndicate_cluster="CLUSTER_9"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0118",
            ssn_hash="SSN_HASH_00b0dfbc",
            dob_consistency_score=0.53,
            address_type="PO_BOX",
            thin_file_months=10,
            revolving_utilization=0.63,
            fraud_syndicate_cluster="CLUSTER_10"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0119",
            ssn_hash="SSN_HASH_00b25f76",
            dob_consistency_score=0.54,
            address_type="VIRTUAL_OFFICE",
            thin_file_months=11,
            revolving_utilization=0.64,
            fraud_syndicate_cluster="CLUSTER_11"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0120",
            ssn_hash="SSN_HASH_00b3df30",
            dob_consistency_score=0.55,
            address_type="COMMERCIAL_MAIL_DROP",
            thin_file_months=12,
            revolving_utilization=0.65,
            fraud_syndicate_cluster="CLUSTER_0"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0121",
            ssn_hash="SSN_HASH_00b55eea",
            dob_consistency_score=0.56,
            address_type="RESIDENTIAL_SINGLE_FAMILY",
            thin_file_months=13,
            revolving_utilization=0.66,
            fraud_syndicate_cluster="CLUSTER_1"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0122",
            ssn_hash="SSN_HASH_00b6dea4",
            dob_consistency_score=0.57,
            address_type="MULTI_UNIT_APARTMENT",
            thin_file_months=14,
            revolving_utilization=0.67,
            fraud_syndicate_cluster="CLUSTER_2"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0123",
            ssn_hash="SSN_HASH_00b85e5e",
            dob_consistency_score=0.58,
            address_type="FREIGHT_FORWARDER",
            thin_file_months=15,
            revolving_utilization=0.68,
            fraud_syndicate_cluster="CLUSTER_3"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0124",
            ssn_hash="SSN_HASH_00b9de18",
            dob_consistency_score=0.59,
            address_type="PO_BOX",
            thin_file_months=16,
            revolving_utilization=0.69,
            fraud_syndicate_cluster="CLUSTER_4"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0125",
            ssn_hash="SSN_HASH_00bb5dd2",
            dob_consistency_score=0.60,
            address_type="VIRTUAL_OFFICE",
            thin_file_months=17,
            revolving_utilization=0.70,
            fraud_syndicate_cluster="CLUSTER_5"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0126",
            ssn_hash="SSN_HASH_00bcdd8c",
            dob_consistency_score=0.61,
            address_type="COMMERCIAL_MAIL_DROP",
            thin_file_months=18,
            revolving_utilization=0.71,
            fraud_syndicate_cluster="CLUSTER_6"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0127",
            ssn_hash="SSN_HASH_00be5d46",
            dob_consistency_score=0.62,
            address_type="RESIDENTIAL_SINGLE_FAMILY",
            thin_file_months=19,
            revolving_utilization=0.72,
            fraud_syndicate_cluster="CLUSTER_7"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0128",
            ssn_hash="SSN_HASH_00bfdd00",
            dob_consistency_score=0.63,
            address_type="MULTI_UNIT_APARTMENT",
            thin_file_months=20,
            revolving_utilization=0.73,
            fraud_syndicate_cluster="CLUSTER_8"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0129",
            ssn_hash="SSN_HASH_00c15cba",
            dob_consistency_score=0.64,
            address_type="FREIGHT_FORWARDER",
            thin_file_months=21,
            revolving_utilization=0.74,
            fraud_syndicate_cluster="CLUSTER_9"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0130",
            ssn_hash="SSN_HASH_00c2dc74",
            dob_consistency_score=0.65,
            address_type="PO_BOX",
            thin_file_months=22,
            revolving_utilization=0.75,
            fraud_syndicate_cluster="CLUSTER_10"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0131",
            ssn_hash="SSN_HASH_00c45c2e",
            dob_consistency_score=0.66,
            address_type="VIRTUAL_OFFICE",
            thin_file_months=23,
            revolving_utilization=0.76,
            fraud_syndicate_cluster="CLUSTER_11"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0132",
            ssn_hash="SSN_HASH_00c5dbe8",
            dob_consistency_score=0.67,
            address_type="COMMERCIAL_MAIL_DROP",
            thin_file_months=24,
            revolving_utilization=0.77,
            fraud_syndicate_cluster="CLUSTER_0"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0133",
            ssn_hash="SSN_HASH_00c75ba2",
            dob_consistency_score=0.68,
            address_type="RESIDENTIAL_SINGLE_FAMILY",
            thin_file_months=25,
            revolving_utilization=0.78,
            fraud_syndicate_cluster="CLUSTER_1"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0134",
            ssn_hash="SSN_HASH_00c8db5c",
            dob_consistency_score=0.69,
            address_type="MULTI_UNIT_APARTMENT",
            thin_file_months=26,
            revolving_utilization=0.79,
            fraud_syndicate_cluster="CLUSTER_2"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0135",
            ssn_hash="SSN_HASH_00ca5b16",
            dob_consistency_score=0.70,
            address_type="FREIGHT_FORWARDER",
            thin_file_months=27,
            revolving_utilization=0.80,
            fraud_syndicate_cluster="CLUSTER_3"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0136",
            ssn_hash="SSN_HASH_00cbdad0",
            dob_consistency_score=0.71,
            address_type="PO_BOX",
            thin_file_months=28,
            revolving_utilization=0.81,
            fraud_syndicate_cluster="CLUSTER_4"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0137",
            ssn_hash="SSN_HASH_00cd5a8a",
            dob_consistency_score=0.72,
            address_type="VIRTUAL_OFFICE",
            thin_file_months=29,
            revolving_utilization=0.82,
            fraud_syndicate_cluster="CLUSTER_5"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0138",
            ssn_hash="SSN_HASH_00ceda44",
            dob_consistency_score=0.73,
            address_type="COMMERCIAL_MAIL_DROP",
            thin_file_months=30,
            revolving_utilization=0.83,
            fraud_syndicate_cluster="CLUSTER_6"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0139",
            ssn_hash="SSN_HASH_00d059fe",
            dob_consistency_score=0.74,
            address_type="RESIDENTIAL_SINGLE_FAMILY",
            thin_file_months=31,
            revolving_utilization=0.84,
            fraud_syndicate_cluster="CLUSTER_7"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0140",
            ssn_hash="SSN_HASH_00d1d9b8",
            dob_consistency_score=0.75,
            address_type="MULTI_UNIT_APARTMENT",
            thin_file_months=32,
            revolving_utilization=0.85,
            fraud_syndicate_cluster="CLUSTER_8"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0141",
            ssn_hash="SSN_HASH_00d35972",
            dob_consistency_score=0.76,
            address_type="FREIGHT_FORWARDER",
            thin_file_months=33,
            revolving_utilization=0.86,
            fraud_syndicate_cluster="CLUSTER_9"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0142",
            ssn_hash="SSN_HASH_00d4d92c",
            dob_consistency_score=0.77,
            address_type="PO_BOX",
            thin_file_months=34,
            revolving_utilization=0.87,
            fraud_syndicate_cluster="CLUSTER_10"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0143",
            ssn_hash="SSN_HASH_00d658e6",
            dob_consistency_score=0.78,
            address_type="VIRTUAL_OFFICE",
            thin_file_months=35,
            revolving_utilization=0.88,
            fraud_syndicate_cluster="CLUSTER_11"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0144",
            ssn_hash="SSN_HASH_00d7d8a0",
            dob_consistency_score=0.79,
            address_type="COMMERCIAL_MAIL_DROP",
            thin_file_months=0,
            revolving_utilization=0.89,
            fraud_syndicate_cluster="CLUSTER_0"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0145",
            ssn_hash="SSN_HASH_00d9585a",
            dob_consistency_score=0.80,
            address_type="RESIDENTIAL_SINGLE_FAMILY",
            thin_file_months=1,
            revolving_utilization=0.90,
            fraud_syndicate_cluster="CLUSTER_1"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0146",
            ssn_hash="SSN_HASH_00dad814",
            dob_consistency_score=0.81,
            address_type="MULTI_UNIT_APARTMENT",
            thin_file_months=2,
            revolving_utilization=0.91,
            fraud_syndicate_cluster="CLUSTER_2"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0147",
            ssn_hash="SSN_HASH_00dc57ce",
            dob_consistency_score=0.82,
            address_type="FREIGHT_FORWARDER",
            thin_file_months=3,
            revolving_utilization=0.92,
            fraud_syndicate_cluster="CLUSTER_3"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0148",
            ssn_hash="SSN_HASH_00ddd788",
            dob_consistency_score=0.83,
            address_type="PO_BOX",
            thin_file_months=4,
            revolving_utilization=0.93,
            fraud_syndicate_cluster="CLUSTER_4"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0149",
            ssn_hash="SSN_HASH_00df5742",
            dob_consistency_score=0.84,
            address_type="VIRTUAL_OFFICE",
            thin_file_months=5,
            revolving_utilization=0.94,
            fraud_syndicate_cluster="CLUSTER_5"
        ))
        self.register(SyntheticIdentityProfile(
            profile_id="SYN_ID_0150",
            ssn_hash="SSN_HASH_00e0d6fc",
            dob_consistency_score=0.85,
            address_type="COMMERCIAL_MAIL_DROP",
            thin_file_months=6,
            revolving_utilization=0.45,
            fraud_syndicate_cluster="CLUSTER_6"
        ))

    def get_high_probability_synthetics(self) -> List[SyntheticIdentityProfile]:
        return [p for p in self.profiles.values() if p.dob_consistency_score < 0.40 and p.thin_file_months < 12]

synthetic_catalog = SyntheticIdentityMatrixCatalog()

class SyntheticClusterAnalyzer_1:
    """Evaluates synthetic identity cluster grouping 1."""
    def __init__(self):
        self.group_id = 1
    def is_synthetic_ring(self, count_records: int) -> bool:
        return count_records >= 4

class SyntheticClusterAnalyzer_2:
    """Evaluates synthetic identity cluster grouping 2."""
    def __init__(self):
        self.group_id = 2
    def is_synthetic_ring(self, count_records: int) -> bool:
        return count_records >= 4

class SyntheticClusterAnalyzer_3:
    """Evaluates synthetic identity cluster grouping 3."""
    def __init__(self):
        self.group_id = 3
    def is_synthetic_ring(self, count_records: int) -> bool:
        return count_records >= 4

class SyntheticClusterAnalyzer_4:
    """Evaluates synthetic identity cluster grouping 4."""
    def __init__(self):
        self.group_id = 4
    def is_synthetic_ring(self, count_records: int) -> bool:
        return count_records >= 4

class SyntheticClusterAnalyzer_5:
    """Evaluates synthetic identity cluster grouping 5."""
    def __init__(self):
        self.group_id = 5
    def is_synthetic_ring(self, count_records: int) -> bool:
        return count_records >= 4

class SyntheticClusterAnalyzer_6:
    """Evaluates synthetic identity cluster grouping 6."""
    def __init__(self):
        self.group_id = 6
    def is_synthetic_ring(self, count_records: int) -> bool:
        return count_records >= 4

class SyntheticClusterAnalyzer_7:
    """Evaluates synthetic identity cluster grouping 7."""
    def __init__(self):
        self.group_id = 7
    def is_synthetic_ring(self, count_records: int) -> bool:
        return count_records >= 4

class SyntheticClusterAnalyzer_8:
    """Evaluates synthetic identity cluster grouping 8."""
    def __init__(self):
        self.group_id = 8
    def is_synthetic_ring(self, count_records: int) -> bool:
        return count_records >= 4

class SyntheticClusterAnalyzer_9:
    """Evaluates synthetic identity cluster grouping 9."""
    def __init__(self):
        self.group_id = 9
    def is_synthetic_ring(self, count_records: int) -> bool:
        return count_records >= 4

class SyntheticClusterAnalyzer_10:
    """Evaluates synthetic identity cluster grouping 10."""
    def __init__(self):
        self.group_id = 10
    def is_synthetic_ring(self, count_records: int) -> bool:
        return count_records >= 4

class SyntheticClusterAnalyzer_11:
    """Evaluates synthetic identity cluster grouping 11."""
    def __init__(self):
        self.group_id = 11
    def is_synthetic_ring(self, count_records: int) -> bool:
        return count_records >= 4

class SyntheticClusterAnalyzer_12:
    """Evaluates synthetic identity cluster grouping 12."""
    def __init__(self):
        self.group_id = 12
    def is_synthetic_ring(self, count_records: int) -> bool:
        return count_records >= 4

class SyntheticClusterAnalyzer_13:
    """Evaluates synthetic identity cluster grouping 13."""
    def __init__(self):
        self.group_id = 13
    def is_synthetic_ring(self, count_records: int) -> bool:
        return count_records >= 4

class SyntheticClusterAnalyzer_14:
    """Evaluates synthetic identity cluster grouping 14."""
    def __init__(self):
        self.group_id = 14
    def is_synthetic_ring(self, count_records: int) -> bool:
        return count_records >= 4

class SyntheticClusterAnalyzer_15:
    """Evaluates synthetic identity cluster grouping 15."""
    def __init__(self):
        self.group_id = 15
    def is_synthetic_ring(self, count_records: int) -> bool:
        return count_records >= 4

class SyntheticClusterAnalyzer_16:
    """Evaluates synthetic identity cluster grouping 16."""
    def __init__(self):
        self.group_id = 16
    def is_synthetic_ring(self, count_records: int) -> bool:
        return count_records >= 4

class SyntheticClusterAnalyzer_17:
    """Evaluates synthetic identity cluster grouping 17."""
    def __init__(self):
        self.group_id = 17
    def is_synthetic_ring(self, count_records: int) -> bool:
        return count_records >= 4

class SyntheticClusterAnalyzer_18:
    """Evaluates synthetic identity cluster grouping 18."""
    def __init__(self):
        self.group_id = 18
    def is_synthetic_ring(self, count_records: int) -> bool:
        return count_records >= 4

class SyntheticClusterAnalyzer_19:
    """Evaluates synthetic identity cluster grouping 19."""
    def __init__(self):
        self.group_id = 19
    def is_synthetic_ring(self, count_records: int) -> bool:
        return count_records >= 4

class SyntheticClusterAnalyzer_20:
    """Evaluates synthetic identity cluster grouping 20."""
    def __init__(self):
        self.group_id = 20
    def is_synthetic_ring(self, count_records: int) -> bool:
        return count_records >= 4

class SyntheticClusterAnalyzer_21:
    """Evaluates synthetic identity cluster grouping 21."""
    def __init__(self):
        self.group_id = 21
    def is_synthetic_ring(self, count_records: int) -> bool:
        return count_records >= 4

class SyntheticClusterAnalyzer_22:
    """Evaluates synthetic identity cluster grouping 22."""
    def __init__(self):
        self.group_id = 22
    def is_synthetic_ring(self, count_records: int) -> bool:
        return count_records >= 4

class SyntheticClusterAnalyzer_23:
    """Evaluates synthetic identity cluster grouping 23."""
    def __init__(self):
        self.group_id = 23
    def is_synthetic_ring(self, count_records: int) -> bool:
        return count_records >= 4

class SyntheticClusterAnalyzer_24:
    """Evaluates synthetic identity cluster grouping 24."""
    def __init__(self):
        self.group_id = 24
    def is_synthetic_ring(self, count_records: int) -> bool:
        return count_records >= 4

class SyntheticClusterAnalyzer_25:
    """Evaluates synthetic identity cluster grouping 25."""
    def __init__(self):
        self.group_id = 25
    def is_synthetic_ring(self, count_records: int) -> bool:
        return count_records >= 4

class SyntheticClusterAnalyzer_26:
    """Evaluates synthetic identity cluster grouping 26."""
    def __init__(self):
        self.group_id = 26
    def is_synthetic_ring(self, count_records: int) -> bool:
        return count_records >= 4

class SyntheticClusterAnalyzer_27:
    """Evaluates synthetic identity cluster grouping 27."""
    def __init__(self):
        self.group_id = 27
    def is_synthetic_ring(self, count_records: int) -> bool:
        return count_records >= 4

class SyntheticClusterAnalyzer_28:
    """Evaluates synthetic identity cluster grouping 28."""
    def __init__(self):
        self.group_id = 28
    def is_synthetic_ring(self, count_records: int) -> bool:
        return count_records >= 4

class SyntheticClusterAnalyzer_29:
    """Evaluates synthetic identity cluster grouping 29."""
    def __init__(self):
        self.group_id = 29
    def is_synthetic_ring(self, count_records: int) -> bool:
        return count_records >= 4

class SyntheticClusterAnalyzer_30:
    """Evaluates synthetic identity cluster grouping 30."""
    def __init__(self):
        self.group_id = 30
    def is_synthetic_ring(self, count_records: int) -> bool:
        return count_records >= 4

class SyntheticClusterAnalyzer_31:
    """Evaluates synthetic identity cluster grouping 31."""
    def __init__(self):
        self.group_id = 31
    def is_synthetic_ring(self, count_records: int) -> bool:
        return count_records >= 4

class SyntheticClusterAnalyzer_32:
    """Evaluates synthetic identity cluster grouping 32."""
    def __init__(self):
        self.group_id = 32
    def is_synthetic_ring(self, count_records: int) -> bool:
        return count_records >= 4

class SyntheticClusterAnalyzer_33:
    """Evaluates synthetic identity cluster grouping 33."""
    def __init__(self):
        self.group_id = 33
    def is_synthetic_ring(self, count_records: int) -> bool:
        return count_records >= 4

class SyntheticClusterAnalyzer_34:
    """Evaluates synthetic identity cluster grouping 34."""
    def __init__(self):
        self.group_id = 34
    def is_synthetic_ring(self, count_records: int) -> bool:
        return count_records >= 4

class SyntheticClusterAnalyzer_35:
    """Evaluates synthetic identity cluster grouping 35."""
    def __init__(self):
        self.group_id = 35
    def is_synthetic_ring(self, count_records: int) -> bool:
        return count_records >= 4

class SyntheticClusterAnalyzer_36:
    """Evaluates synthetic identity cluster grouping 36."""
    def __init__(self):
        self.group_id = 36
    def is_synthetic_ring(self, count_records: int) -> bool:
        return count_records >= 4

class SyntheticClusterAnalyzer_37:
    """Evaluates synthetic identity cluster grouping 37."""
    def __init__(self):
        self.group_id = 37
    def is_synthetic_ring(self, count_records: int) -> bool:
        return count_records >= 4

class SyntheticClusterAnalyzer_38:
    """Evaluates synthetic identity cluster grouping 38."""
    def __init__(self):
        self.group_id = 38
    def is_synthetic_ring(self, count_records: int) -> bool:
        return count_records >= 4

class SyntheticClusterAnalyzer_39:
    """Evaluates synthetic identity cluster grouping 39."""
    def __init__(self):
        self.group_id = 39
    def is_synthetic_ring(self, count_records: int) -> bool:
        return count_records >= 4