"""Report generation service producing HTML and PDF reports with metrics and findings."""

import os
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional
import pandas as pd

from config.settings import settings
from config.logging_config import logger
from backend.app.models.schemas import ReportType, ReportRequest
from backend.app.services.storage_service import storage_service

# Try importing reportlab for PDF generation
try:
    from reportlab.lib.pagesizes import letter
    from reportlab.lib import colors
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    HAS_REPORTLAB = True
except ImportError:
    HAS_REPORTLAB = False


class ReportService:
    def generate_report(self, req: ReportRequest) -> Dict[str, Any]:
        """Generate formatted HTML or PDF report."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        clean_name = req.report_type.value.lower().replace(" ", "_")
        filename_base = f"{clean_name}_{timestamp}"

        # Fetch current datasets and metrics for report
        datasets = storage_service.list_datasets()
        models = storage_service.list_trained_models()
        reviews = storage_service.get_suspicious_reviews()

        stats = {
            "total_datasets": len(datasets),
            "total_models": len(models),
            "flagged_suspicious_count": len(reviews),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "author": req.author or "Fraud Analytics Team"
        }

        # Render HTML
        html_content = self._build_html_report(req.report_type, stats, models, reviews)
        html_file = settings.REPORTS_DIR / f"{filename_base}.html"
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(html_content)

        pdf_path = None
        if req.format.lower() == "pdf" and HAS_REPORTLAB:
            pdf_file = settings.REPORTS_DIR / f"{filename_base}.pdf"
            self._build_pdf_report(pdf_file, req.report_type, stats, models, reviews)
            pdf_path = str(pdf_file.name)

        return {
            "report_type": req.report_type.value,
            "format": req.format,
            "filename": pdf_path if req.format == "pdf" and pdf_path else html_file.name,
            "html_path": html_file.name,
            "generated_at": stats["timestamp"],
            "preview_html": html_content
        }

    def _build_html_report(self, r_type: ReportType, stats: Dict, models: list, reviews: list) -> str:
        models_html = ""
        for m in models:
            met = m.get("metrics", {})
            models_html += f"""
            <tr>
                <td style="padding:10px; border-bottom:1px solid #27272a; font-weight:600;">{m.get('model_name')}</td>
                <td style="padding:10px; border-bottom:1px solid #27272a;">{met.get('accuracy', 0)*100:.1f}%</td>
                <td style="padding:10px; border-bottom:1px solid #27272a; color:#10b981; font-weight:600;">{met.get('precision', 0)*100:.1f}%</td>
                <td style="padding:10px; border-bottom:1px solid #27272a; color:#10b981; font-weight:600;">{met.get('recall', 0)*100:.1f}%</td>
                <td style="padding:10px; border-bottom:1px solid #27272a; font-weight:bold;">{met.get('f1_score', 0)*100:.1f}%</td>
                <td style="padding:10px; border-bottom:1px solid #27272a;">{met.get('training_time_seconds', 0):.2f}s</td>
            </tr>
            """

        reviews_html = ""
        for r in reviews[:8]:
            status_color = "#ef4444" if r.get("risk_level") == "HIGH" else "#f59e0b"
            reviews_html += f"""
            <tr>
                <td style="padding:8px; border-bottom:1px solid #27272a;">{r.get('transaction_id')}</td>
                <td style="padding:8px; border-bottom:1px solid #27272a;">{r.get('customer_id')}</td>
                <td style="padding:8px; border-bottom:1px solid #27272a; font-weight:bold;">₹{r.get('amount', 0):,.2f}</td>
                <td style="padding:8px; border-bottom:1px solid #27272a; color:{status_color}; font-weight:bold;">{r.get('risk_score')}/100</td>
                <td style="padding:8px; border-bottom:1px solid #27272a;">{r.get('review_status')}</td>
                <td style="padding:8px; border-bottom:1px solid #27272a; font-size:12px;">{r.get('assigned_analyst')}</td>
            </tr>
            """

        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{r_type.value} - Enterprise Risk Report</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background-color: #0d0f12;
            color: #e4e4e7;
            margin: 0;
            padding: 40px;
        }}
        .header {{
            border-bottom: 2px solid #27272a;
            padding-bottom: 24px;
            margin-bottom: 30px;
        }}
        .title {{
            font-size: 26px;
            font-weight: 700;
            color: #f4f4f5;
            margin: 0 0 8px 0;
        }}
        .meta {{
            color: #a1a1aa;
            font-size: 14px;
        }}
        .kpi-row {{
            display: flex;
            gap: 20px;
            margin-bottom: 30px;
        }}
        .kpi-card {{
            background: #181c24;
            border: 1px solid #27272a;
            border-radius: 8px;
            padding: 16px 20px;
            flex: 1;
        }}
        .kpi-num {{
            font-size: 24px;
            font-weight: 700;
            color: #10b981;
            margin-top: 4px;
        }}
        .kpi-label {{
            font-size: 12px;
            color: #a1a1aa;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            background: #14171f;
            border-radius: 8px;
            overflow: hidden;
            margin-bottom: 30px;
        }}
        th {{
            background: #1f2430;
            color: #d4d4d8;
            font-size: 13px;
            text-align: left;
            padding: 12px;
            border-bottom: 2px solid #27272a;
        }}
        .badge {{
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 12px;
            font-weight: 600;
        }}
        .badge-high {{ background: #451a1a; color: #f87171; border: 1px solid #7f1d1d; }}
        .badge-low {{ background: #064e3b; color: #34d399; border: 1px solid #065f46; }}
    </style>
</head>
<body>
    <div class="header">
        <h1 class="title">{r_type.value}</h1>
        <div class="meta">
            Platform: AI-Powered Financial Fraud Detection &amp; Risk Analytics &bull;
            Generated: {stats['timestamp']} &bull; Author: {stats['author']}
        </div>
    </div>

    <div class="kpi-row">
        <div class="kpi-card">
            <div class="kpi-label">Active Datasets</div>
            <div class="kpi-num">{stats['total_datasets']}</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-label">Evaluated Models</div>
            <div class="kpi-num">{stats['total_models']}</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-label">Flagged Suspicious Items</div>
            <div class="kpi-num" style="color:#f59e0b;">{stats['flagged_suspicious_count']}</div>
        </div>
    </div>

    <h2 style="font-size: 18px; color: #f4f4f5; margin-bottom: 12px;">Machine Learning Benchmark Metrics</h2>
    <table>
        <thead>
            <tr>
                <th>Model Name</th>
                <th>Accuracy</th>
                <th>Precision</th>
                <th>Recall</th>
                <th>F1-Score</th>
                <th>Latency</th>
            </tr>
        </thead>
        <tbody>
            {models_html or "<tr><td colspan='6' style='padding:16px; text-align:center;'>No models trained yet.</td></tr>"}
        </tbody>
    </table>

    <h2 style="font-size: 18px; color: #f4f4f5; margin-bottom: 12px;">Recent Suspicious Transaction Audit Log</h2>
    <table>
        <thead>
            <tr>
                <th>Tx ID</th>
                <th>Customer ID</th>
                <th>Amount</th>
                <th>Risk Score</th>
                <th>Status</th>
                <th>Analyst</th>
            </tr>
        </thead>
        <tbody>
            {reviews_html or "<tr><td colspan='6' style='padding:16px; text-align:center;'>No suspicious items in queue.</td></tr>"}
        </tbody>
    </table>
</body>
</html>
"""

    def _build_pdf_report(self, target_path: Path, r_type: ReportType, stats: Dict, models: list, reviews: list):
        """Construct standard PDF document via ReportLab."""
        doc = SimpleDocTemplate(str(target_path), pagesize=letter)
        styles = getSampleStyleSheet()
        story = []

        title_style = ParagraphStyle(
            "ReportTitle",
            parent=styles["Heading1"],
            fontSize=20,
            leading=24,
            textColor=colors.HexColor("#181c24")
        )
        body_style = ParagraphStyle(
            "ReportBody",
            parent=styles["Normal"],
            fontSize=10,
            leading=14,
            textColor=colors.HexColor("#27272a")
        )

        story.append(Paragraph(r_type.value, title_style))
        story.append(Paragraph(f"Generated on {stats['timestamp']} by {stats['author']}", body_style))
        story.append(Spacer(1, 16))

        # Overview Table
        overview_data = [
            ["Metric", "Value"],
            ["Total Registered Datasets", str(stats["total_datasets"])],
            ["Trained ML Models", str(stats["total_models"])],
            ["High Risk Suspicious Items", str(stats["flagged_suspicious_count"])]
        ]
        t = Table(overview_data, colWidths=[240, 240])
        t.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e4e4e7")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#09090b")),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#a1a1aa"))
        ]))
        story.append(t)
        story.append(Spacer(1, 20))

        doc.build(story)


report_service = ReportService()
