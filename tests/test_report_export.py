"""Tests for report generation and export services."""

import pytest
from backend.app.models.schemas import ReportRequest, ReportType
from backend.app.services.report_service import report_service
from backend.app.services.export_service import export_service


def test_generate_html_report():
    req = ReportRequest(
        report_type=ReportType.EXECUTIVE_SUMMARY,
        format="html",
        author="Quality Assurance Test"
    )
    result = report_service.generate_report(req)
    assert result["format"] == "html"
    assert "preview_html" in result
    assert "Enterprise Risk Report" in result["preview_html"]


def test_export_csv_and_json():
    mock_data = [
        {"tx_id": "T1", "amount": 500, "status": "Clean"},
        {"tx_id": "T2", "amount": 100000, "status": "Suspicious"}
    ]
    csv_file = export_service.export_csv("unit_test_export", mock_data)
    json_file = export_service.export_json("unit_test_export", mock_data)

    assert csv_file.endswith(".csv")
    assert json_file.endswith(".json")
