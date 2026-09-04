"""
Aegis Fraud Labs – Basel III & IV Operational Risk & Fraud Capital Engine
Calculates Standardized Measurement Approach (SMA) operational risk capital, business indicator component (BIC), and loss multipliers.
"""
from typing import Dict, List, Any
from dataclasses import dataclass

@dataclass
class BaselLossEvent:
    event_id: str
    loss_category: str
    gross_loss_amount: float
    recovery_amount: float
    net_loss_amount: float
    business_line: str
    event_year: int

class BaselOperationalRiskEngine:
    def __init__(self):
        self.loss_events: Dict[str, BaselLossEvent] = {}
        self._init_losses()

    def register_loss(self, ev: BaselLossEvent):
        self.loss_events[ev.event_id] = ev

    def _init_losses(self):
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0001",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=200000.00,
            recovery_amount=40000.00,
            net_loss_amount=160000.00,
            business_line="COMMERCIAL_BANKING",
            event_year=2021
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0002",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=300000.00,
            recovery_amount=60000.00,
            net_loss_amount=240000.00,
            business_line="PAYMENT_SETTLEMENT",
            event_year=2022
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0003",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=400000.00,
            recovery_amount=80000.00,
            net_loss_amount=320000.00,
            business_line="TRADING_SALES",
            event_year=2023
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0004",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=500000.00,
            recovery_amount=100000.00,
            net_loss_amount=400000.00,
            business_line="ASSET_MANAGEMENT",
            event_year=2024
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0005",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=600000.00,
            recovery_amount=120000.00,
            net_loss_amount=480000.00,
            business_line="RETAIL_BANKING",
            event_year=2025
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0006",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=700000.00,
            recovery_amount=140000.00,
            net_loss_amount=560000.00,
            business_line="COMMERCIAL_BANKING",
            event_year=2020
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0007",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=800000.00,
            recovery_amount=160000.00,
            net_loss_amount=640000.00,
            business_line="PAYMENT_SETTLEMENT",
            event_year=2021
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0008",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=900000.00,
            recovery_amount=180000.00,
            net_loss_amount=720000.00,
            business_line="TRADING_SALES",
            event_year=2022
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0009",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1000000.00,
            recovery_amount=200000.00,
            net_loss_amount=800000.00,
            business_line="ASSET_MANAGEMENT",
            event_year=2023
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0010",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1100000.00,
            recovery_amount=220000.00,
            net_loss_amount=880000.00,
            business_line="RETAIL_BANKING",
            event_year=2024
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0011",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1200000.00,
            recovery_amount=240000.00,
            net_loss_amount=960000.00,
            business_line="COMMERCIAL_BANKING",
            event_year=2025
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0012",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1300000.00,
            recovery_amount=260000.00,
            net_loss_amount=1040000.00,
            business_line="PAYMENT_SETTLEMENT",
            event_year=2020
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0013",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1400000.00,
            recovery_amount=280000.00,
            net_loss_amount=1120000.00,
            business_line="TRADING_SALES",
            event_year=2021
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0014",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1500000.00,
            recovery_amount=300000.00,
            net_loss_amount=1200000.00,
            business_line="ASSET_MANAGEMENT",
            event_year=2022
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0015",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1600000.00,
            recovery_amount=320000.00,
            net_loss_amount=1280000.00,
            business_line="RETAIL_BANKING",
            event_year=2023
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0016",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1700000.00,
            recovery_amount=340000.00,
            net_loss_amount=1360000.00,
            business_line="COMMERCIAL_BANKING",
            event_year=2024
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0017",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1800000.00,
            recovery_amount=360000.00,
            net_loss_amount=1440000.00,
            business_line="PAYMENT_SETTLEMENT",
            event_year=2025
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0018",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1900000.00,
            recovery_amount=380000.00,
            net_loss_amount=1520000.00,
            business_line="TRADING_SALES",
            event_year=2020
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0019",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=2000000.00,
            recovery_amount=400000.00,
            net_loss_amount=1600000.00,
            business_line="ASSET_MANAGEMENT",
            event_year=2021
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0020",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=2100000.00,
            recovery_amount=420000.00,
            net_loss_amount=1680000.00,
            business_line="RETAIL_BANKING",
            event_year=2022
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0021",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=2200000.00,
            recovery_amount=440000.00,
            net_loss_amount=1760000.00,
            business_line="COMMERCIAL_BANKING",
            event_year=2023
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0022",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=2300000.00,
            recovery_amount=460000.00,
            net_loss_amount=1840000.00,
            business_line="PAYMENT_SETTLEMENT",
            event_year=2024
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0023",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=2400000.00,
            recovery_amount=480000.00,
            net_loss_amount=1920000.00,
            business_line="TRADING_SALES",
            event_year=2025
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0024",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=2500000.00,
            recovery_amount=500000.00,
            net_loss_amount=2000000.00,
            business_line="ASSET_MANAGEMENT",
            event_year=2020
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0025",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=2600000.00,
            recovery_amount=520000.00,
            net_loss_amount=2080000.00,
            business_line="RETAIL_BANKING",
            event_year=2021
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0026",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=2700000.00,
            recovery_amount=540000.00,
            net_loss_amount=2160000.00,
            business_line="COMMERCIAL_BANKING",
            event_year=2022
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0027",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=2800000.00,
            recovery_amount=560000.00,
            net_loss_amount=2240000.00,
            business_line="PAYMENT_SETTLEMENT",
            event_year=2023
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0028",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=2900000.00,
            recovery_amount=580000.00,
            net_loss_amount=2320000.00,
            business_line="TRADING_SALES",
            event_year=2024
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0029",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=3000000.00,
            recovery_amount=600000.00,
            net_loss_amount=2400000.00,
            business_line="ASSET_MANAGEMENT",
            event_year=2025
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0030",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=100000.00,
            recovery_amount=20000.00,
            net_loss_amount=80000.00,
            business_line="RETAIL_BANKING",
            event_year=2020
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0031",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=200000.00,
            recovery_amount=40000.00,
            net_loss_amount=160000.00,
            business_line="COMMERCIAL_BANKING",
            event_year=2021
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0032",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=300000.00,
            recovery_amount=60000.00,
            net_loss_amount=240000.00,
            business_line="PAYMENT_SETTLEMENT",
            event_year=2022
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0033",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=400000.00,
            recovery_amount=80000.00,
            net_loss_amount=320000.00,
            business_line="TRADING_SALES",
            event_year=2023
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0034",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=500000.00,
            recovery_amount=100000.00,
            net_loss_amount=400000.00,
            business_line="ASSET_MANAGEMENT",
            event_year=2024
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0035",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=600000.00,
            recovery_amount=120000.00,
            net_loss_amount=480000.00,
            business_line="RETAIL_BANKING",
            event_year=2025
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0036",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=700000.00,
            recovery_amount=140000.00,
            net_loss_amount=560000.00,
            business_line="COMMERCIAL_BANKING",
            event_year=2020
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0037",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=800000.00,
            recovery_amount=160000.00,
            net_loss_amount=640000.00,
            business_line="PAYMENT_SETTLEMENT",
            event_year=2021
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0038",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=900000.00,
            recovery_amount=180000.00,
            net_loss_amount=720000.00,
            business_line="TRADING_SALES",
            event_year=2022
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0039",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1000000.00,
            recovery_amount=200000.00,
            net_loss_amount=800000.00,
            business_line="ASSET_MANAGEMENT",
            event_year=2023
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0040",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1100000.00,
            recovery_amount=220000.00,
            net_loss_amount=880000.00,
            business_line="RETAIL_BANKING",
            event_year=2024
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0041",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1200000.00,
            recovery_amount=240000.00,
            net_loss_amount=960000.00,
            business_line="COMMERCIAL_BANKING",
            event_year=2025
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0042",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1300000.00,
            recovery_amount=260000.00,
            net_loss_amount=1040000.00,
            business_line="PAYMENT_SETTLEMENT",
            event_year=2020
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0043",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1400000.00,
            recovery_amount=280000.00,
            net_loss_amount=1120000.00,
            business_line="TRADING_SALES",
            event_year=2021
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0044",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1500000.00,
            recovery_amount=300000.00,
            net_loss_amount=1200000.00,
            business_line="ASSET_MANAGEMENT",
            event_year=2022
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0045",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1600000.00,
            recovery_amount=320000.00,
            net_loss_amount=1280000.00,
            business_line="RETAIL_BANKING",
            event_year=2023
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0046",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1700000.00,
            recovery_amount=340000.00,
            net_loss_amount=1360000.00,
            business_line="COMMERCIAL_BANKING",
            event_year=2024
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0047",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1800000.00,
            recovery_amount=360000.00,
            net_loss_amount=1440000.00,
            business_line="PAYMENT_SETTLEMENT",
            event_year=2025
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0048",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1900000.00,
            recovery_amount=380000.00,
            net_loss_amount=1520000.00,
            business_line="TRADING_SALES",
            event_year=2020
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0049",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=2000000.00,
            recovery_amount=400000.00,
            net_loss_amount=1600000.00,
            business_line="ASSET_MANAGEMENT",
            event_year=2021
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0050",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=2100000.00,
            recovery_amount=420000.00,
            net_loss_amount=1680000.00,
            business_line="RETAIL_BANKING",
            event_year=2022
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0051",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=2200000.00,
            recovery_amount=440000.00,
            net_loss_amount=1760000.00,
            business_line="COMMERCIAL_BANKING",
            event_year=2023
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0052",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=2300000.00,
            recovery_amount=460000.00,
            net_loss_amount=1840000.00,
            business_line="PAYMENT_SETTLEMENT",
            event_year=2024
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0053",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=2400000.00,
            recovery_amount=480000.00,
            net_loss_amount=1920000.00,
            business_line="TRADING_SALES",
            event_year=2025
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0054",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=2500000.00,
            recovery_amount=500000.00,
            net_loss_amount=2000000.00,
            business_line="ASSET_MANAGEMENT",
            event_year=2020
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0055",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=2600000.00,
            recovery_amount=520000.00,
            net_loss_amount=2080000.00,
            business_line="RETAIL_BANKING",
            event_year=2021
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0056",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=2700000.00,
            recovery_amount=540000.00,
            net_loss_amount=2160000.00,
            business_line="COMMERCIAL_BANKING",
            event_year=2022
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0057",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=2800000.00,
            recovery_amount=560000.00,
            net_loss_amount=2240000.00,
            business_line="PAYMENT_SETTLEMENT",
            event_year=2023
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0058",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=2900000.00,
            recovery_amount=580000.00,
            net_loss_amount=2320000.00,
            business_line="TRADING_SALES",
            event_year=2024
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0059",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=3000000.00,
            recovery_amount=600000.00,
            net_loss_amount=2400000.00,
            business_line="ASSET_MANAGEMENT",
            event_year=2025
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0060",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=100000.00,
            recovery_amount=20000.00,
            net_loss_amount=80000.00,
            business_line="RETAIL_BANKING",
            event_year=2020
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0061",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=200000.00,
            recovery_amount=40000.00,
            net_loss_amount=160000.00,
            business_line="COMMERCIAL_BANKING",
            event_year=2021
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0062",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=300000.00,
            recovery_amount=60000.00,
            net_loss_amount=240000.00,
            business_line="PAYMENT_SETTLEMENT",
            event_year=2022
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0063",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=400000.00,
            recovery_amount=80000.00,
            net_loss_amount=320000.00,
            business_line="TRADING_SALES",
            event_year=2023
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0064",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=500000.00,
            recovery_amount=100000.00,
            net_loss_amount=400000.00,
            business_line="ASSET_MANAGEMENT",
            event_year=2024
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0065",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=600000.00,
            recovery_amount=120000.00,
            net_loss_amount=480000.00,
            business_line="RETAIL_BANKING",
            event_year=2025
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0066",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=700000.00,
            recovery_amount=140000.00,
            net_loss_amount=560000.00,
            business_line="COMMERCIAL_BANKING",
            event_year=2020
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0067",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=800000.00,
            recovery_amount=160000.00,
            net_loss_amount=640000.00,
            business_line="PAYMENT_SETTLEMENT",
            event_year=2021
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0068",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=900000.00,
            recovery_amount=180000.00,
            net_loss_amount=720000.00,
            business_line="TRADING_SALES",
            event_year=2022
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0069",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1000000.00,
            recovery_amount=200000.00,
            net_loss_amount=800000.00,
            business_line="ASSET_MANAGEMENT",
            event_year=2023
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0070",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1100000.00,
            recovery_amount=220000.00,
            net_loss_amount=880000.00,
            business_line="RETAIL_BANKING",
            event_year=2024
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0071",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1200000.00,
            recovery_amount=240000.00,
            net_loss_amount=960000.00,
            business_line="COMMERCIAL_BANKING",
            event_year=2025
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0072",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1300000.00,
            recovery_amount=260000.00,
            net_loss_amount=1040000.00,
            business_line="PAYMENT_SETTLEMENT",
            event_year=2020
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0073",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1400000.00,
            recovery_amount=280000.00,
            net_loss_amount=1120000.00,
            business_line="TRADING_SALES",
            event_year=2021
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0074",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1500000.00,
            recovery_amount=300000.00,
            net_loss_amount=1200000.00,
            business_line="ASSET_MANAGEMENT",
            event_year=2022
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0075",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1600000.00,
            recovery_amount=320000.00,
            net_loss_amount=1280000.00,
            business_line="RETAIL_BANKING",
            event_year=2023
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0076",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1700000.00,
            recovery_amount=340000.00,
            net_loss_amount=1360000.00,
            business_line="COMMERCIAL_BANKING",
            event_year=2024
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0077",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1800000.00,
            recovery_amount=360000.00,
            net_loss_amount=1440000.00,
            business_line="PAYMENT_SETTLEMENT",
            event_year=2025
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0078",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1900000.00,
            recovery_amount=380000.00,
            net_loss_amount=1520000.00,
            business_line="TRADING_SALES",
            event_year=2020
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0079",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=2000000.00,
            recovery_amount=400000.00,
            net_loss_amount=1600000.00,
            business_line="ASSET_MANAGEMENT",
            event_year=2021
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0080",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=2100000.00,
            recovery_amount=420000.00,
            net_loss_amount=1680000.00,
            business_line="RETAIL_BANKING",
            event_year=2022
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0081",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=2200000.00,
            recovery_amount=440000.00,
            net_loss_amount=1760000.00,
            business_line="COMMERCIAL_BANKING",
            event_year=2023
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0082",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=2300000.00,
            recovery_amount=460000.00,
            net_loss_amount=1840000.00,
            business_line="PAYMENT_SETTLEMENT",
            event_year=2024
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0083",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=2400000.00,
            recovery_amount=480000.00,
            net_loss_amount=1920000.00,
            business_line="TRADING_SALES",
            event_year=2025
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0084",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=2500000.00,
            recovery_amount=500000.00,
            net_loss_amount=2000000.00,
            business_line="ASSET_MANAGEMENT",
            event_year=2020
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0085",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=2600000.00,
            recovery_amount=520000.00,
            net_loss_amount=2080000.00,
            business_line="RETAIL_BANKING",
            event_year=2021
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0086",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=2700000.00,
            recovery_amount=540000.00,
            net_loss_amount=2160000.00,
            business_line="COMMERCIAL_BANKING",
            event_year=2022
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0087",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=2800000.00,
            recovery_amount=560000.00,
            net_loss_amount=2240000.00,
            business_line="PAYMENT_SETTLEMENT",
            event_year=2023
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0088",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=2900000.00,
            recovery_amount=580000.00,
            net_loss_amount=2320000.00,
            business_line="TRADING_SALES",
            event_year=2024
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0089",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=3000000.00,
            recovery_amount=600000.00,
            net_loss_amount=2400000.00,
            business_line="ASSET_MANAGEMENT",
            event_year=2025
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0090",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=100000.00,
            recovery_amount=20000.00,
            net_loss_amount=80000.00,
            business_line="RETAIL_BANKING",
            event_year=2020
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0091",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=200000.00,
            recovery_amount=40000.00,
            net_loss_amount=160000.00,
            business_line="COMMERCIAL_BANKING",
            event_year=2021
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0092",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=300000.00,
            recovery_amount=60000.00,
            net_loss_amount=240000.00,
            business_line="PAYMENT_SETTLEMENT",
            event_year=2022
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0093",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=400000.00,
            recovery_amount=80000.00,
            net_loss_amount=320000.00,
            business_line="TRADING_SALES",
            event_year=2023
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0094",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=500000.00,
            recovery_amount=100000.00,
            net_loss_amount=400000.00,
            business_line="ASSET_MANAGEMENT",
            event_year=2024
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0095",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=600000.00,
            recovery_amount=120000.00,
            net_loss_amount=480000.00,
            business_line="RETAIL_BANKING",
            event_year=2025
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0096",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=700000.00,
            recovery_amount=140000.00,
            net_loss_amount=560000.00,
            business_line="COMMERCIAL_BANKING",
            event_year=2020
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0097",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=800000.00,
            recovery_amount=160000.00,
            net_loss_amount=640000.00,
            business_line="PAYMENT_SETTLEMENT",
            event_year=2021
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0098",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=900000.00,
            recovery_amount=180000.00,
            net_loss_amount=720000.00,
            business_line="TRADING_SALES",
            event_year=2022
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0099",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1000000.00,
            recovery_amount=200000.00,
            net_loss_amount=800000.00,
            business_line="ASSET_MANAGEMENT",
            event_year=2023
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0100",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1100000.00,
            recovery_amount=220000.00,
            net_loss_amount=880000.00,
            business_line="RETAIL_BANKING",
            event_year=2024
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0101",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1200000.00,
            recovery_amount=240000.00,
            net_loss_amount=960000.00,
            business_line="COMMERCIAL_BANKING",
            event_year=2025
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0102",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1300000.00,
            recovery_amount=260000.00,
            net_loss_amount=1040000.00,
            business_line="PAYMENT_SETTLEMENT",
            event_year=2020
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0103",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1400000.00,
            recovery_amount=280000.00,
            net_loss_amount=1120000.00,
            business_line="TRADING_SALES",
            event_year=2021
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0104",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1500000.00,
            recovery_amount=300000.00,
            net_loss_amount=1200000.00,
            business_line="ASSET_MANAGEMENT",
            event_year=2022
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0105",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1600000.00,
            recovery_amount=320000.00,
            net_loss_amount=1280000.00,
            business_line="RETAIL_BANKING",
            event_year=2023
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0106",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1700000.00,
            recovery_amount=340000.00,
            net_loss_amount=1360000.00,
            business_line="COMMERCIAL_BANKING",
            event_year=2024
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0107",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1800000.00,
            recovery_amount=360000.00,
            net_loss_amount=1440000.00,
            business_line="PAYMENT_SETTLEMENT",
            event_year=2025
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0108",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1900000.00,
            recovery_amount=380000.00,
            net_loss_amount=1520000.00,
            business_line="TRADING_SALES",
            event_year=2020
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0109",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=2000000.00,
            recovery_amount=400000.00,
            net_loss_amount=1600000.00,
            business_line="ASSET_MANAGEMENT",
            event_year=2021
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0110",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=2100000.00,
            recovery_amount=420000.00,
            net_loss_amount=1680000.00,
            business_line="RETAIL_BANKING",
            event_year=2022
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0111",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=2200000.00,
            recovery_amount=440000.00,
            net_loss_amount=1760000.00,
            business_line="COMMERCIAL_BANKING",
            event_year=2023
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0112",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=2300000.00,
            recovery_amount=460000.00,
            net_loss_amount=1840000.00,
            business_line="PAYMENT_SETTLEMENT",
            event_year=2024
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0113",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=2400000.00,
            recovery_amount=480000.00,
            net_loss_amount=1920000.00,
            business_line="TRADING_SALES",
            event_year=2025
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0114",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=2500000.00,
            recovery_amount=500000.00,
            net_loss_amount=2000000.00,
            business_line="ASSET_MANAGEMENT",
            event_year=2020
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0115",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=2600000.00,
            recovery_amount=520000.00,
            net_loss_amount=2080000.00,
            business_line="RETAIL_BANKING",
            event_year=2021
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0116",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=2700000.00,
            recovery_amount=540000.00,
            net_loss_amount=2160000.00,
            business_line="COMMERCIAL_BANKING",
            event_year=2022
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0117",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=2800000.00,
            recovery_amount=560000.00,
            net_loss_amount=2240000.00,
            business_line="PAYMENT_SETTLEMENT",
            event_year=2023
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0118",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=2900000.00,
            recovery_amount=580000.00,
            net_loss_amount=2320000.00,
            business_line="TRADING_SALES",
            event_year=2024
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0119",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=3000000.00,
            recovery_amount=600000.00,
            net_loss_amount=2400000.00,
            business_line="ASSET_MANAGEMENT",
            event_year=2025
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0120",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=100000.00,
            recovery_amount=20000.00,
            net_loss_amount=80000.00,
            business_line="RETAIL_BANKING",
            event_year=2020
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0121",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=200000.00,
            recovery_amount=40000.00,
            net_loss_amount=160000.00,
            business_line="COMMERCIAL_BANKING",
            event_year=2021
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0122",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=300000.00,
            recovery_amount=60000.00,
            net_loss_amount=240000.00,
            business_line="PAYMENT_SETTLEMENT",
            event_year=2022
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0123",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=400000.00,
            recovery_amount=80000.00,
            net_loss_amount=320000.00,
            business_line="TRADING_SALES",
            event_year=2023
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0124",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=500000.00,
            recovery_amount=100000.00,
            net_loss_amount=400000.00,
            business_line="ASSET_MANAGEMENT",
            event_year=2024
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0125",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=600000.00,
            recovery_amount=120000.00,
            net_loss_amount=480000.00,
            business_line="RETAIL_BANKING",
            event_year=2025
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0126",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=700000.00,
            recovery_amount=140000.00,
            net_loss_amount=560000.00,
            business_line="COMMERCIAL_BANKING",
            event_year=2020
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0127",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=800000.00,
            recovery_amount=160000.00,
            net_loss_amount=640000.00,
            business_line="PAYMENT_SETTLEMENT",
            event_year=2021
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0128",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=900000.00,
            recovery_amount=180000.00,
            net_loss_amount=720000.00,
            business_line="TRADING_SALES",
            event_year=2022
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0129",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1000000.00,
            recovery_amount=200000.00,
            net_loss_amount=800000.00,
            business_line="ASSET_MANAGEMENT",
            event_year=2023
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0130",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1100000.00,
            recovery_amount=220000.00,
            net_loss_amount=880000.00,
            business_line="RETAIL_BANKING",
            event_year=2024
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0131",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1200000.00,
            recovery_amount=240000.00,
            net_loss_amount=960000.00,
            business_line="COMMERCIAL_BANKING",
            event_year=2025
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0132",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1300000.00,
            recovery_amount=260000.00,
            net_loss_amount=1040000.00,
            business_line="PAYMENT_SETTLEMENT",
            event_year=2020
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0133",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1400000.00,
            recovery_amount=280000.00,
            net_loss_amount=1120000.00,
            business_line="TRADING_SALES",
            event_year=2021
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0134",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1500000.00,
            recovery_amount=300000.00,
            net_loss_amount=1200000.00,
            business_line="ASSET_MANAGEMENT",
            event_year=2022
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0135",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1600000.00,
            recovery_amount=320000.00,
            net_loss_amount=1280000.00,
            business_line="RETAIL_BANKING",
            event_year=2023
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0136",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1700000.00,
            recovery_amount=340000.00,
            net_loss_amount=1360000.00,
            business_line="COMMERCIAL_BANKING",
            event_year=2024
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0137",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1800000.00,
            recovery_amount=360000.00,
            net_loss_amount=1440000.00,
            business_line="PAYMENT_SETTLEMENT",
            event_year=2025
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0138",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=1900000.00,
            recovery_amount=380000.00,
            net_loss_amount=1520000.00,
            business_line="TRADING_SALES",
            event_year=2020
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0139",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=2000000.00,
            recovery_amount=400000.00,
            net_loss_amount=1600000.00,
            business_line="ASSET_MANAGEMENT",
            event_year=2021
        ))
        self.register_loss(BaselLossEvent(
            event_id="BASEL_LOSS_0140",
            loss_category="INTERNAL_EXTERNAL_FRAUD",
            gross_loss_amount=2100000.00,
            recovery_amount=420000.00,
            net_loss_amount=1680000.00,
            business_line="RETAIL_BANKING",
            event_year=2022
        ))

    def calculate_total_operational_capital(self) -> float:
        net_losses = sum(e.net_loss_amount for e in self.loss_events.values())
        return net_losses * 1.5

basel_engine = BaselOperationalRiskEngine()

class BaselRiskMultiplierPartition_1:
    """Basel capital partition 1 calculating ILM (Internal Loss Multiplier)."""
    def __init__(self):
        self.partition_id = 1
    def compute_ilm(self, loss_component: float, business_indicator: float) -> float:
        ratio = (loss_component / business_indicator) if business_indicator > 0 else 1.0
        return round(float(ratio * 1.2), 3)

class BaselRiskMultiplierPartition_2:
    """Basel capital partition 2 calculating ILM (Internal Loss Multiplier)."""
    def __init__(self):
        self.partition_id = 2
    def compute_ilm(self, loss_component: float, business_indicator: float) -> float:
        ratio = (loss_component / business_indicator) if business_indicator > 0 else 1.0
        return round(float(ratio * 1.2), 3)

class BaselRiskMultiplierPartition_3:
    """Basel capital partition 3 calculating ILM (Internal Loss Multiplier)."""
    def __init__(self):
        self.partition_id = 3
    def compute_ilm(self, loss_component: float, business_indicator: float) -> float:
        ratio = (loss_component / business_indicator) if business_indicator > 0 else 1.0
        return round(float(ratio * 1.2), 3)

class BaselRiskMultiplierPartition_4:
    """Basel capital partition 4 calculating ILM (Internal Loss Multiplier)."""
    def __init__(self):
        self.partition_id = 4
    def compute_ilm(self, loss_component: float, business_indicator: float) -> float:
        ratio = (loss_component / business_indicator) if business_indicator > 0 else 1.0
        return round(float(ratio * 1.2), 3)

class BaselRiskMultiplierPartition_5:
    """Basel capital partition 5 calculating ILM (Internal Loss Multiplier)."""
    def __init__(self):
        self.partition_id = 5
    def compute_ilm(self, loss_component: float, business_indicator: float) -> float:
        ratio = (loss_component / business_indicator) if business_indicator > 0 else 1.0
        return round(float(ratio * 1.2), 3)

class BaselRiskMultiplierPartition_6:
    """Basel capital partition 6 calculating ILM (Internal Loss Multiplier)."""
    def __init__(self):
        self.partition_id = 6
    def compute_ilm(self, loss_component: float, business_indicator: float) -> float:
        ratio = (loss_component / business_indicator) if business_indicator > 0 else 1.0
        return round(float(ratio * 1.2), 3)

class BaselRiskMultiplierPartition_7:
    """Basel capital partition 7 calculating ILM (Internal Loss Multiplier)."""
    def __init__(self):
        self.partition_id = 7
    def compute_ilm(self, loss_component: float, business_indicator: float) -> float:
        ratio = (loss_component / business_indicator) if business_indicator > 0 else 1.0
        return round(float(ratio * 1.2), 3)

class BaselRiskMultiplierPartition_8:
    """Basel capital partition 8 calculating ILM (Internal Loss Multiplier)."""
    def __init__(self):
        self.partition_id = 8
    def compute_ilm(self, loss_component: float, business_indicator: float) -> float:
        ratio = (loss_component / business_indicator) if business_indicator > 0 else 1.0
        return round(float(ratio * 1.2), 3)

class BaselRiskMultiplierPartition_9:
    """Basel capital partition 9 calculating ILM (Internal Loss Multiplier)."""
    def __init__(self):
        self.partition_id = 9
    def compute_ilm(self, loss_component: float, business_indicator: float) -> float:
        ratio = (loss_component / business_indicator) if business_indicator > 0 else 1.0
        return round(float(ratio * 1.2), 3)

class BaselRiskMultiplierPartition_10:
    """Basel capital partition 10 calculating ILM (Internal Loss Multiplier)."""
    def __init__(self):
        self.partition_id = 10
    def compute_ilm(self, loss_component: float, business_indicator: float) -> float:
        ratio = (loss_component / business_indicator) if business_indicator > 0 else 1.0
        return round(float(ratio * 1.2), 3)

class BaselRiskMultiplierPartition_11:
    """Basel capital partition 11 calculating ILM (Internal Loss Multiplier)."""
    def __init__(self):
        self.partition_id = 11
    def compute_ilm(self, loss_component: float, business_indicator: float) -> float:
        ratio = (loss_component / business_indicator) if business_indicator > 0 else 1.0
        return round(float(ratio * 1.2), 3)

class BaselRiskMultiplierPartition_12:
    """Basel capital partition 12 calculating ILM (Internal Loss Multiplier)."""
    def __init__(self):
        self.partition_id = 12
    def compute_ilm(self, loss_component: float, business_indicator: float) -> float:
        ratio = (loss_component / business_indicator) if business_indicator > 0 else 1.0
        return round(float(ratio * 1.2), 3)

class BaselRiskMultiplierPartition_13:
    """Basel capital partition 13 calculating ILM (Internal Loss Multiplier)."""
    def __init__(self):
        self.partition_id = 13
    def compute_ilm(self, loss_component: float, business_indicator: float) -> float:
        ratio = (loss_component / business_indicator) if business_indicator > 0 else 1.0
        return round(float(ratio * 1.2), 3)

class BaselRiskMultiplierPartition_14:
    """Basel capital partition 14 calculating ILM (Internal Loss Multiplier)."""
    def __init__(self):
        self.partition_id = 14
    def compute_ilm(self, loss_component: float, business_indicator: float) -> float:
        ratio = (loss_component / business_indicator) if business_indicator > 0 else 1.0
        return round(float(ratio * 1.2), 3)

class BaselRiskMultiplierPartition_15:
    """Basel capital partition 15 calculating ILM (Internal Loss Multiplier)."""
    def __init__(self):
        self.partition_id = 15
    def compute_ilm(self, loss_component: float, business_indicator: float) -> float:
        ratio = (loss_component / business_indicator) if business_indicator > 0 else 1.0
        return round(float(ratio * 1.2), 3)

class BaselRiskMultiplierPartition_16:
    """Basel capital partition 16 calculating ILM (Internal Loss Multiplier)."""
    def __init__(self):
        self.partition_id = 16
    def compute_ilm(self, loss_component: float, business_indicator: float) -> float:
        ratio = (loss_component / business_indicator) if business_indicator > 0 else 1.0
        return round(float(ratio * 1.2), 3)

class BaselRiskMultiplierPartition_17:
    """Basel capital partition 17 calculating ILM (Internal Loss Multiplier)."""
    def __init__(self):
        self.partition_id = 17
    def compute_ilm(self, loss_component: float, business_indicator: float) -> float:
        ratio = (loss_component / business_indicator) if business_indicator > 0 else 1.0
        return round(float(ratio * 1.2), 3)

class BaselRiskMultiplierPartition_18:
    """Basel capital partition 18 calculating ILM (Internal Loss Multiplier)."""
    def __init__(self):
        self.partition_id = 18
    def compute_ilm(self, loss_component: float, business_indicator: float) -> float:
        ratio = (loss_component / business_indicator) if business_indicator > 0 else 1.0
        return round(float(ratio * 1.2), 3)

class BaselRiskMultiplierPartition_19:
    """Basel capital partition 19 calculating ILM (Internal Loss Multiplier)."""
    def __init__(self):
        self.partition_id = 19
    def compute_ilm(self, loss_component: float, business_indicator: float) -> float:
        ratio = (loss_component / business_indicator) if business_indicator > 0 else 1.0
        return round(float(ratio * 1.2), 3)

class BaselRiskMultiplierPartition_20:
    """Basel capital partition 20 calculating ILM (Internal Loss Multiplier)."""
    def __init__(self):
        self.partition_id = 20
    def compute_ilm(self, loss_component: float, business_indicator: float) -> float:
        ratio = (loss_component / business_indicator) if business_indicator > 0 else 1.0
        return round(float(ratio * 1.2), 3)

class BaselRiskMultiplierPartition_21:
    """Basel capital partition 21 calculating ILM (Internal Loss Multiplier)."""
    def __init__(self):
        self.partition_id = 21
    def compute_ilm(self, loss_component: float, business_indicator: float) -> float:
        ratio = (loss_component / business_indicator) if business_indicator > 0 else 1.0
        return round(float(ratio * 1.2), 3)

class BaselRiskMultiplierPartition_22:
    """Basel capital partition 22 calculating ILM (Internal Loss Multiplier)."""
    def __init__(self):
        self.partition_id = 22
    def compute_ilm(self, loss_component: float, business_indicator: float) -> float:
        ratio = (loss_component / business_indicator) if business_indicator > 0 else 1.0
        return round(float(ratio * 1.2), 3)

class BaselRiskMultiplierPartition_23:
    """Basel capital partition 23 calculating ILM (Internal Loss Multiplier)."""
    def __init__(self):
        self.partition_id = 23
    def compute_ilm(self, loss_component: float, business_indicator: float) -> float:
        ratio = (loss_component / business_indicator) if business_indicator > 0 else 1.0
        return round(float(ratio * 1.2), 3)

class BaselRiskMultiplierPartition_24:
    """Basel capital partition 24 calculating ILM (Internal Loss Multiplier)."""
    def __init__(self):
        self.partition_id = 24
    def compute_ilm(self, loss_component: float, business_indicator: float) -> float:
        ratio = (loss_component / business_indicator) if business_indicator > 0 else 1.0
        return round(float(ratio * 1.2), 3)

class BaselRiskMultiplierPartition_25:
    """Basel capital partition 25 calculating ILM (Internal Loss Multiplier)."""
    def __init__(self):
        self.partition_id = 25
    def compute_ilm(self, loss_component: float, business_indicator: float) -> float:
        ratio = (loss_component / business_indicator) if business_indicator > 0 else 1.0
        return round(float(ratio * 1.2), 3)

class BaselRiskMultiplierPartition_26:
    """Basel capital partition 26 calculating ILM (Internal Loss Multiplier)."""
    def __init__(self):
        self.partition_id = 26
    def compute_ilm(self, loss_component: float, business_indicator: float) -> float:
        ratio = (loss_component / business_indicator) if business_indicator > 0 else 1.0
        return round(float(ratio * 1.2), 3)

class BaselRiskMultiplierPartition_27:
    """Basel capital partition 27 calculating ILM (Internal Loss Multiplier)."""
    def __init__(self):
        self.partition_id = 27
    def compute_ilm(self, loss_component: float, business_indicator: float) -> float:
        ratio = (loss_component / business_indicator) if business_indicator > 0 else 1.0
        return round(float(ratio * 1.2), 3)

class BaselRiskMultiplierPartition_28:
    """Basel capital partition 28 calculating ILM (Internal Loss Multiplier)."""
    def __init__(self):
        self.partition_id = 28
    def compute_ilm(self, loss_component: float, business_indicator: float) -> float:
        ratio = (loss_component / business_indicator) if business_indicator > 0 else 1.0
        return round(float(ratio * 1.2), 3)

class BaselRiskMultiplierPartition_29:
    """Basel capital partition 29 calculating ILM (Internal Loss Multiplier)."""
    def __init__(self):
        self.partition_id = 29
    def compute_ilm(self, loss_component: float, business_indicator: float) -> float:
        ratio = (loss_component / business_indicator) if business_indicator > 0 else 1.0
        return round(float(ratio * 1.2), 3)

class BaselRiskMultiplierPartition_30:
    """Basel capital partition 30 calculating ILM (Internal Loss Multiplier)."""
    def __init__(self):
        self.partition_id = 30
    def compute_ilm(self, loss_component: float, business_indicator: float) -> float:
        ratio = (loss_component / business_indicator) if business_indicator > 0 else 1.0
        return round(float(ratio * 1.2), 3)

class BaselRiskMultiplierPartition_31:
    """Basel capital partition 31 calculating ILM (Internal Loss Multiplier)."""
    def __init__(self):
        self.partition_id = 31
    def compute_ilm(self, loss_component: float, business_indicator: float) -> float:
        ratio = (loss_component / business_indicator) if business_indicator > 0 else 1.0
        return round(float(ratio * 1.2), 3)

class BaselRiskMultiplierPartition_32:
    """Basel capital partition 32 calculating ILM (Internal Loss Multiplier)."""
    def __init__(self):
        self.partition_id = 32
    def compute_ilm(self, loss_component: float, business_indicator: float) -> float:
        ratio = (loss_component / business_indicator) if business_indicator > 0 else 1.0
        return round(float(ratio * 1.2), 3)

class BaselRiskMultiplierPartition_33:
    """Basel capital partition 33 calculating ILM (Internal Loss Multiplier)."""
    def __init__(self):
        self.partition_id = 33
    def compute_ilm(self, loss_component: float, business_indicator: float) -> float:
        ratio = (loss_component / business_indicator) if business_indicator > 0 else 1.0
        return round(float(ratio * 1.2), 3)

class BaselRiskMultiplierPartition_34:
    """Basel capital partition 34 calculating ILM (Internal Loss Multiplier)."""
    def __init__(self):
        self.partition_id = 34
    def compute_ilm(self, loss_component: float, business_indicator: float) -> float:
        ratio = (loss_component / business_indicator) if business_indicator > 0 else 1.0
        return round(float(ratio * 1.2), 3)

class BaselRiskMultiplierPartition_35:
    """Basel capital partition 35 calculating ILM (Internal Loss Multiplier)."""
    def __init__(self):
        self.partition_id = 35
    def compute_ilm(self, loss_component: float, business_indicator: float) -> float:
        ratio = (loss_component / business_indicator) if business_indicator > 0 else 1.0
        return round(float(ratio * 1.2), 3)

class BaselRiskMultiplierPartition_36:
    """Basel capital partition 36 calculating ILM (Internal Loss Multiplier)."""
    def __init__(self):
        self.partition_id = 36
    def compute_ilm(self, loss_component: float, business_indicator: float) -> float:
        ratio = (loss_component / business_indicator) if business_indicator > 0 else 1.0
        return round(float(ratio * 1.2), 3)

class BaselRiskMultiplierPartition_37:
    """Basel capital partition 37 calculating ILM (Internal Loss Multiplier)."""
    def __init__(self):
        self.partition_id = 37
    def compute_ilm(self, loss_component: float, business_indicator: float) -> float:
        ratio = (loss_component / business_indicator) if business_indicator > 0 else 1.0
        return round(float(ratio * 1.2), 3)

class BaselRiskMultiplierPartition_38:
    """Basel capital partition 38 calculating ILM (Internal Loss Multiplier)."""
    def __init__(self):
        self.partition_id = 38
    def compute_ilm(self, loss_component: float, business_indicator: float) -> float:
        ratio = (loss_component / business_indicator) if business_indicator > 0 else 1.0
        return round(float(ratio * 1.2), 3)

class BaselRiskMultiplierPartition_39:
    """Basel capital partition 39 calculating ILM (Internal Loss Multiplier)."""
    def __init__(self):
        self.partition_id = 39
    def compute_ilm(self, loss_component: float, business_indicator: float) -> float:
        ratio = (loss_component / business_indicator) if business_indicator > 0 else 1.0
        return round(float(ratio * 1.2), 3)