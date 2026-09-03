"""Synthetic financial transaction generator producing realistic, reproducible data."""

import random
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import numpy as np
import pandas as pd

from backend.app.models.schemas import SyntheticGenerateRequest
from config.logging_config import logger

DEFAULT_LOCATIONS = [
    "Mumbai", "Delhi", "Bengaluru", "Hyderabad", "Chennai",
    "Kolkata", "Pune", "Ahmedabad", "Jaipur", "Kochi"
]

DEFAULT_TRANSACTION_TYPES = [
    "Online", "POS / In-Store", "ATM Withdrawal", "UPI Transfer", "Wire Transfer"
]

DEFAULT_MERCHANT_CATEGORIES = [
    "Grocery & Supermarkets", "Dining & Food", "Electronics & Gadgets",
    "Travel & Airlines", "Utilities & Bills", "Luxury Goods & Jewelry",
    "Crypto & Digital Assets", "Healthcare & Medical"
]

DEFAULT_DEVICE_TYPES = [
    "Trusted Mobile App (iOS)", "Trusted Mobile App (Android)",
    "Desktop Web Browser", "Mobile Web Browser",
    "POS Terminal", "ATM Terminal", "Unknown Device", "New Emulated Device"
]


class SyntheticDataGenerator:
    def __init__(self):
        pass

    def generate(self, req: SyntheticGenerateRequest) -> pd.DataFrame:
        """Generate realistic synthetic financial transaction records."""
        np.random.seed(req.random_seed)
        random.seed(req.random_seed)

        logger.info(
            f"Generating synthetic dataset: {req.num_records} rows, "
            f"{req.fraud_percentage}% fraud, {req.num_customers} customers."
        )

        locations = req.locations or DEFAULT_LOCATIONS
        tx_types = req.transaction_types or DEFAULT_TRANSACTION_TYPES
        merchants = req.merchant_categories or DEFAULT_MERCHANT_CATEGORIES
        devices = req.device_types or DEFAULT_DEVICE_TYPES

        # 1. Establish Customer Profiles
        customer_profiles = {}
        for i in range(1, req.num_customers + 1):
            cust_id = f"CUST-{1000 + i}"
            base_amt = float(np.random.gamma(shape=3.5, scale=250.0))  # avg around ₹875
            base_amt = max(150.0, round(base_amt, 2))
            home_loc = random.choice(locations)
            primary_device = random.choice([
                "Trusted Mobile App (iOS)",
                "Trusted Mobile App (Android)",
                "Desktop Web Browser"
            ])
            account_age = random.randint(30, 1800)
            customer_profiles[cust_id] = {
                "base_amount": base_amt,
                "home_location": home_loc,
                "primary_device": primary_device,
                "account_age_days": account_age,
                "last_tx_amount": base_amt
            }

        # 2. Determine Fraud vs Normal Counts
        num_fraud = int(round((req.fraud_percentage / 100.0) * req.num_records))
        num_fraud = max(1, min(num_fraud, req.num_records - 1))
        num_normal = req.num_records - num_fraud

        # Date range handling
        try:
            start_dt = datetime.strptime(req.start_date, "%Y-%m-%d")
            end_dt = datetime.strptime(req.end_date, "%Y-%m-%d")
        except Exception:
            start_dt = datetime(2025, 1, 1)
            end_dt = datetime(2025, 6, 30)

        total_seconds = max(86400, int((end_dt - start_dt).total_seconds()))

        records: List[Dict] = []
        tx_counter = 100001

        # Generate Normal Transactions
        for _ in range(num_normal):
            tx_id = f"TXN-{tx_counter}"
            tx_counter += 1
            cust_id = random.choice(list(customer_profiles.keys()))
            profile = customer_profiles[cust_id]

            # Normal amount varies reasonably around base amount
            amount_multiplier = np.random.lognormal(mean=0.0, sigma=0.4)
            amount = round(profile["base_amount"] * amount_multiplier, 2)
            amount = max(50.0, min(amount, 12000.0))

            # Daytime hours (7 AM to 11 PM) mostly
            sec_offset = random.randint(0, total_seconds)
            tx_time = start_dt + timedelta(seconds=sec_offset)
            if random.random() < 0.88:
                tx_time = tx_time.replace(hour=random.randint(7, 22), minute=random.randint(0, 59))

            # Normal devices & location
            if random.random() < 0.92:
                location = profile["home_location"]
                distance = round(random.uniform(0.5, 18.0), 2)
            else:
                location = random.choice(locations)
                distance = round(random.uniform(20.0, 75.0), 2)

            device = profile["primary_device"] if random.random() < 0.90 else random.choice(devices[:4])
            tx_type = random.choice(["Online", "UPI Transfer", "POS / In-Store"])
            category = random.choice([
                "Grocery & Supermarkets", "Dining & Food",
                "Utilities & Bills", "Healthcare & Medical"
            ])
            frequency = random.randint(1, 3)

            records.append({
                "transaction_id": tx_id,
                "customer_id": cust_id,
                "timestamp": tx_time.strftime("%Y-%m-%d %H:%M:%S"),
                "amount": amount,
                "transaction_type": tx_type,
                "merchant_category": category,
                "location": location,
                "device_type": device,
                "account_age_days": profile["account_age_days"],
                "transaction_frequency": frequency,
                "previous_transaction_amount": profile["last_tx_amount"],
                "distance_from_usual_location": distance,
                "is_fraud": 0
            })
            profile["last_tx_amount"] = amount

        # Generate Fraudulent / Suspicious Transactions
        for _ in range(num_fraud):
            tx_id = f"TXN-{tx_counter}"
            tx_counter += 1
            cust_id = random.choice(list(customer_profiles.keys()))
            profile = customer_profiles[cust_id]

            # Significant amount spike (e.g. ₹45,000 - ₹280,000)
            amount = round(float(random.uniform(45000.0, 280000.0)), 2)

            # High risk hours: 01:00 AM - 04:30 AM
            sec_offset = random.randint(0, total_seconds)
            tx_time = start_dt + timedelta(seconds=sec_offset)
            tx_time = tx_time.replace(hour=random.randint(1, 4), minute=random.randint(0, 59))

            # Distant location & suspicious devices
            other_locations = [loc for loc in locations if loc != profile["home_location"]]
            location = random.choice(other_locations) if other_locations else profile["home_location"]
            distance = round(random.uniform(120.0, 850.0), 2)

            device = random.choice([
                "Unknown Device",
                "New Emulated Device",
                "Mobile Web Browser"
            ])
            tx_type = random.choice(["Online", "Wire Transfer", "ATM Withdrawal"])
            category = random.choice([
                "Crypto & Digital Assets",
                "Luxury Goods & Jewelry",
                "Electronics & Gadgets"
            ])
            frequency = random.randint(5, 12)  # High rapid velocity

            records.append({
                "transaction_id": tx_id,
                "customer_id": cust_id,
                "timestamp": tx_time.strftime("%Y-%m-%d %H:%M:%S"),
                "amount": amount,
                "transaction_type": tx_type,
                "merchant_category": category,
                "location": location,
                "device_type": device,
                "account_age_days": max(1, profile["account_age_days"] - random.randint(0, 100)),
                "transaction_frequency": frequency,
                "previous_transaction_amount": profile["last_tx_amount"],
                "distance_from_usual_location": distance,
                "is_fraud": 1
            })

        # Shuffle deterministically
        random.shuffle(records)

        df = pd.DataFrame(records)
        # Sort by timestamp for chronological order
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df = df.sort_values("timestamp").reset_index(drop=True)
        df["timestamp"] = df["timestamp"].dt.strftime("%Y-%m-%d %H:%M:%S")

        logger.info(
            f"Successfully generated {len(df)} transactions with {df['is_fraud'].sum()} fraud samples."
        )
        return df


synthetic_generator = SyntheticDataGenerator()
