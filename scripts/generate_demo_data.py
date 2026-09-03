"""Pre-seed sample synthetic transactions dataset for demonstration."""

import sys
from pathlib import Path

# Ensure project root is in sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from backend.app.models.schemas import SyntheticGenerateRequest
from backend.app.services.synthetic_generator import synthetic_generator
from backend.app.services.storage_service import storage_service
from config.settings import settings


def main():
    print("Generating standard demo synthetic dataset...")
    req = SyntheticGenerateRequest(
        num_records=1200,
        num_customers=180,
        fraud_percentage=5.5,
        random_seed=42,
        start_date="2025-01-01",
        end_date="2025-06-30"
    )
    df = synthetic_generator.generate(req)
    out_file = "sample_synthetic_transactions.csv"
    storage_service.save_dataset(out_file, df)
    print(f"Successfully generated '{out_file}' with {len(df)} transactions ({df['is_fraud'].sum()} fraud).")


if __name__ == "__main__":
    main()
