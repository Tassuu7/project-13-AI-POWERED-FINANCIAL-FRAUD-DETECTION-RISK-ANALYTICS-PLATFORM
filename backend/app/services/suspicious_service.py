"""Suspicious transaction investigation desk managing review states, notes, and auditor workflows."""

from datetime import datetime
from typing import List, Dict, Any, Optional
from backend.app.models.schemas import SuspiciousItem, ReviewStatus, ReviewUpdateRequest
from backend.app.services.storage_service import storage_service
from config.logging_config import logger


class SuspiciousService:
    def get_all(self, status: Optional[str] = None) -> List[SuspiciousItem]:
        """Fetch all suspicious transactions, optionally filtered by review status."""
        items_data = storage_service.get_suspicious_reviews()
        items = [SuspiciousItem(**item) for item in items_data]
        if status and status.lower() != "all":
            items = [item for item in items if item.review_status.value.lower() == status.lower()]
        return items

    def update_review(self, tx_id: str, req: ReviewUpdateRequest) -> Optional[SuspiciousItem]:
        """Update review status, analyst notes, and timestamp for a flagged transaction."""
        items_data = storage_service.get_suspicious_reviews()
        updated_item = None

        for item in items_data:
            if item.get("transaction_id") == tx_id:
                item["review_status"] = req.review_status.value
                existing_notes = item.get("review_notes", "")
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                new_entry = f"[{timestamp} - {req.analyst_name}]: {req.review_notes}"
                item["review_notes"] = f"{existing_notes}\n{new_entry}".strip()
                item["assigned_analyst"] = req.analyst_name
                item["last_updated"] = timestamp
                updated_item = SuspiciousItem(**item)
                break

        if updated_item:
            storage_service.save_suspicious_reviews(items_data)
            logger.info(f"Updated review status for transaction {tx_id} to '{req.review_status.value}' by {req.analyst_name}")

        return updated_item

    def add_or_update_suspicious_item(self, item: SuspiciousItem):
        """Add newly detected high-risk transaction to investigation queue."""
        items_data = storage_service.get_suspicious_reviews()
        existing_idx = next((i for i, x in enumerate(items_data) if x.get("transaction_id") == item.transaction_id), None)
        
        item_dict = item.model_dump()
        if existing_idx is not None:
            # Preserve existing analyst notes if any
            item_dict["review_notes"] = items_data[existing_idx].get("review_notes", "")
            item_dict["review_status"] = items_data[existing_idx].get("review_status", item.review_status.value)
            items_data[existing_idx] = item_dict
        else:
            item_dict["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            items_data.insert(0, item_dict)

        storage_service.save_suspicious_reviews(items_data)


suspicious_service = SuspiciousService()
