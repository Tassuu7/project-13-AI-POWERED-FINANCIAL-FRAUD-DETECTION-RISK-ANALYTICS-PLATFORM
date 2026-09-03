"""Audit history and processing log service for tracking platform operations."""

import uuid
from datetime import datetime
from typing import Dict, Any, List
from backend.app.models.schemas import AuditLogItem
from backend.app.services.storage_service import storage_service


class HistoryService:
    def record_action(
        self,
        action: str,
        category: str,
        user: str = "Analyst",
        details: Dict[str, Any] = None,
        status: str = "SUCCESS"
    ) -> AuditLogItem:
        """Create and persist an audit history log record."""
        entry = AuditLogItem(
            id=f"LOG-{uuid.uuid4().hex[:8].upper()}",
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            action=action,
            category=category,
            user=user,
            details=details or {},
            status=status
        )
        storage_service.append_audit_log(entry.model_dump())
        return entry

    def get_history(self, category: str = None) -> List[AuditLogItem]:
        """Fetch audit history records, optionally filtered by category."""
        raw_logs = storage_service.get_audit_logs()
        items = [AuditLogItem(**item) for item in raw_logs]
        if category and category.upper() != "ALL":
            items = [item for item in items if item.category.upper() == category.upper()]
        return items


history_service = HistoryService()
