# AI-Powered Financial Fraud Detection & Risk Analytics Platform

An enterprise-grade, local-first software platform designed to analyze financial transaction streams, identify anomalous spending vectors, compute calibrated risk scores, and manage auditor investigation workflows.

Built from scratch with **Python (FastAPI)**, **React 18 (TypeScript)**, **Scikit-Learn**, and **Tailwind CSS**. 

> [!IMPORTANT]
> **Strict Engineering & Design Compliance**:
> - **Zero Blue Palette**: Configured in an executive dark slate and obsidian aesthetic with emerald green, amber, and crimson risk indicators.
> - **Zero AI-Generated Icons/Images**: Uses standard vector stroke icons from `lucide-react`.
> - **Zero External Databases**: Completely database-free local file persistence (`data/`, `models/`, `reports/`, `exports/`, `logs/`).
> - **Zero Cloud AI APIs**: Real local scikit-learn models executed on-device.
> - **Synthetic Data**: 100% privacy-safe synthetic financial records.

---

## Key Features

1. **Executive Fraud Dashboard**: Live dynamic metrics (Total Volume, Normal vs Fraud breakdown, Risk tiers, Precision, Recall, F1) with 6 interactive Recharts visualizations.
2. **Local Role Session Access**: Multi-role support for **Analyst**, **Reviewer**, and **Administrator** permissions.
3. **Data Upload & Validation Engine**: Drag-and-drop CSV upload with a comprehensive 8-point diagnostic checklist (negative amounts, nulls, duplicate IDs, timestamp validity).
4. **Synthetic Data Generator**: Deterministic, reproducible generation (reproducible seed, configurable fraud %, customer counts, amount distributions, nocturnal hours, distance hops).
5. **Preprocessing Pipeline**: Imputation (median/mode), ID deduplication, categorical one-hot encoding, feature scaling (Standard, Robust, MinMax), and train/test splitting.
6. **Domain Feature Engineering**: Synthesizes 9 domain fraud features (amount deviation, amount-to-previous ratio, night transaction flag, high velocity bursts, geographic anomalies).
7. **Exploratory Data Analysis (EDA)**: Five-number numerical summaries, target feature correlations, and channel/location distributions.
8. **Multi-Model ML Training**: Train and compare **Logistic Regression**, **Decision Tree**, **Random Forest**, **Gradient Boosting**, and **Isolation Forest** with cost-sensitive class balancing.
9. **Model Evaluation Center**: Side-by-side benchmarking on Precision, Recall, F1, ROC-AUC, Latency, and Confusion Matrices.
10. **Dual-Mode Fraud Prediction**:
    - *Real-Time Single Inspector*: Live risk scoring with contributing factors and policy recommendations.
    - *Batch Scoring Pipeline*: Bulk dataset inference with auto-routing of high-risk items.
11. **Transparent Risk Scoring (0–100)**: Blends ML model probability (55%) with verifiable heuristic rules (45%) into Low (0–30), Medium (31–70), and High (71–100) risk tiers.
12. **Transaction Explorer**: Search, multi-filter, sort, and paginate through transactions with an interactive inspection drawer.
13. **Suspicious Transactions Investigation Desk**: Auditor triage queue with statuses (`New`, `Under Review`, `Investigating`, `Cleared`, `Confirmed Suspicious`) and audit notes.
14. **Model Explainability**: Global feature attribution rankings and local per-transaction waterfall point breakdowns.
15. **Report Generation**: Compile standalone **HTML** and **PDF** (via ReportLab) reports for datasets, fraud risk, model evaluations, and audits.
16. **Artifact Export Center**: Export CSV queues, model metrics JSON, and datasets locally.
17. **Processing History**: Local JSON audit trail logging every platform operation.
18. **Configurable Settings**: Calibrate risk score thresholds and select default models.
19. **Help & Data Dictionary**: Complete documentation on fraud mechanics and schema definitions.

---

## Technology Stack

- **Backend**: Python 3.14 / 3.10+, FastAPI, Uvicorn, Pydantic v2, Scikit-Learn, Pandas, NumPy, Joblib, ReportLab.
- **Frontend**: React 18, TypeScript, Vite, Tailwind CSS (Dark Obsidian & Emerald), Lucide-React, Recharts.
- **Persistence**: Local File System (`CSV`, `JSON`, `.joblib`).
- **Testing**: Pytest (100% pass rate across 20 automated tests).

---

## Getting Started

### 1. Prerequisites
- Python 3.10 or higher
- Node.js v18 or higher (with npm)

### 2. Backend Setup
```bash
# Navigate to project root
cd project-13

# Install Python backend dependencies
pip install -r backend/requirements.txt

# Start the FastAPI backend server
uvicorn backend.app.main:app --host 0.0.0.0 --port 8013 --reload
```
API Documentation will be available at `http://127.0.0.1:8013/docs`.

### 3. Frontend Setup
```bash
# In a new terminal, navigate to frontend
cd frontend

# Install Node dependencies
npm install

# Start the Vite development server
npm run dev
```
Open your browser at `http://localhost:5193`.

---

## Demonstration Scenario

1. Open **Main Dashboard** to view baseline metrics for `sample_synthetic_transactions.csv`.
2. Navigate to **Fraud Prediction -> Single Transaction Inspector**.
3. Click **"Suspicious Preset"**:
   - Amount: `₹1,85,000.00`
   - Time: `03:15 AM`
   - Device: `Unknown Device`
   - Location: `Mumbai` (280 km from customer baseline)
   - Frequency: `8 txns/hr`
4. Click **Run Real-Time Inference**:
   - Verdict: **HIGH RISK / POTENTIALLY SUSPICIOUS** (Score: ~94 / 100)
   - Auto-routed to **Suspicious Transactions Investigation Desk**.
5. Navigate to **Suspicious Desk**, click **Review**, assign status `Investigating`, and add review notes.
6. Navigate to **Report Generation**, select **Executive Risk Summary**, and click **Generate Report** (HTML/PDF preview & download).

---

## Automated Test Suite
Run the test suite covering data validation, preprocessing, feature synthesis, ML models, risk engine, and endpoints:
```bash
pytest -v tests/
```
Result: **20 passed in 3.06s**.

---

## License & Intellectual Property
Developed as an original project. Commercially permissive dependencies only. Zero GPL code. Zero client/employer proprietary intellectual property.
