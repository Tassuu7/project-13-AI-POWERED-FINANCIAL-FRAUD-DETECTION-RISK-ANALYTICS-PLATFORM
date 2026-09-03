"""Transaction explorer service providing search, multi-factor filtering, sorting, and pagination."""

from typing import Dict, List, Any, Optional
import pandas as pd
from backend.app.services.storage_service import storage_service


class TransactionService:
    def query_transactions(
        self,
        filename: str,
        search: Optional[str] = None,
        risk_level: Optional[str] = None,
        transaction_type: Optional[str] = None,
        location: Optional[str] = None,
        device_type: Optional[str] = None,
        min_amount: Optional[float] = None,
        max_amount: Optional[float] = None,
        sort_by: str = "timestamp",
        sort_order: str = "desc",
        page: int = 1,
        page_size: int = 15
    ) -> Dict[str, Any]:
        df = storage_service.load_dataset(filename)

        # Assign risk score and level if not in dataset
        if "risk_score" not in df.columns:
            if "is_fraud" in df.columns:
                df["risk_score"] = df["is_fraud"].apply(lambda f: 88 if f == 1 else 14)
                df["risk_level"] = df["is_fraud"].apply(lambda f: "HIGH" if f == 1 else "LOW")
            else:
                df["risk_score"] = 20
                df["risk_level"] = "LOW"

        # Apply Filters
        filtered = df.copy()

        if search:
            s = search.strip().lower()
            filtered = filtered[
                filtered["transaction_id"].astype(str).str.lower().str.contains(s) |
                filtered["customer_id"].astype(str).str.lower().str.contains(s)
            ]

        if risk_level and risk_level.upper() != "ALL":
            filtered = filtered[filtered["risk_level"].str.upper() == risk_level.upper()]

        if transaction_type and transaction_type.upper() != "ALL":
            filtered = filtered[filtered["transaction_type"].str.lower() == transaction_type.lower()]

        if location and location.upper() != "ALL":
            filtered = filtered[filtered["location"].str.lower() == location.lower()]

        if device_type and device_type.upper() != "ALL":
            filtered = filtered[filtered["device_type"].str.lower() == device_type.lower()]

        if min_amount is not None:
            filtered = filtered[filtered["amount"] >= min_amount]

        if max_amount is not None:
            filtered = filtered[filtered["amount"] <= max_amount]

        total_count = len(filtered)

        # Sorting
        ascending = (sort_order.lower() == "asc")
        if sort_by in filtered.columns:
            filtered = filtered.sort_values(by=sort_by, ascending=ascending)

        # Pagination
        start_idx = (page - 1) * page_size
        end_idx = start_idx + page_size
        page_records = filtered.iloc[start_idx:end_idx].to_dict(orient="records")

        total_pages = max(1, (total_count + page_size - 1) // page_size)

        return {
            "total_records": total_count,
            "page": page,
            "page_size": page_size,
            "total_pages": total_pages,
            "records": page_records
        }


transaction_service = TransactionService()
