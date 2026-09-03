# Architecture Overview — AI-Powered Financial Fraud Detection & Risk Analytics Platform

## 1. System Design Philosophy
The **AI-Powered Financial Fraud Detection & Risk Analytics Platform** is architected as an enterprise-grade, local-first web application. It eliminates dependencies on external third-party cloud AI APIs, remote relational databases, or proprietary services, executing all machine learning inference, synthetic data modeling, and reporting locally.

```
       +-------------------------------------------------------------+
       |                  React 18 + TypeScript Frontend             |
       |  - 20 Dedicated Operational Modules (Recharts + Lucide SVGs)|
       |  - Strictly Zero Blue Palette (Obsidian + Emerald + Crimson)|
       +------------------------------+------------------------------+
                                      | HTTP REST API (/api/*)
                                      v
       +-------------------------------------------------------------+
       |                  FastAPI Application Server                 |
       |  - Uvicorn ASGI Server                                      |
       |  - 16 Modular Routers (Auth, Datasets, ML, Risk, Audit)     |
       +------------------------------+------------------------------+
                                      |
         +----------------------------+----------------------------+
         |                                                         |
         v                                                         v
+-------------------------------+                         +-------------------------------+
|     Services & ML Pipeline    |                         |    Local-First Persistence    |
| - Synthetic Generator         |                         | - data/ (CSVs, Datasets)      |
| - Validation Engine           |                         | - models/ (Joblib Artifacts)  |
| - Preprocessing Pipeline      |                         | - reports/ (HTML, PDFs)       |
| - Feature Engineering Engine  |                         | - exports/ (CSV, JSON)        |
| - Scikit-Learn Classifiers    |                         | - logs/ (Structured Logging)  |
| - Risk Scoring Engine (0-100) |                         | - data/suspicious_reviews.json|
| - Model Explainability        |                         | - data/audit_history.json     |
+-------------------------------+                         +-------------------------------+
```

---

## 2. Directory Structure
```
project-13/
├── config/
│   ├── settings.py                 # Pydantic BaseSettings and directory path resolvers
│   ├── logging_config.py           # Structured rotation & console logging
│   └── risk_thresholds.json        # Configurable risk scoring calibration rules
├── backend/
│   ├── app/
│   │   ├── main.py                 # FastAPI application, CORS, lifespan, routes
│   │   ├── api/                    # REST API routers (20 distinct endpoints)
│   │   │   ├── auth.py             # Local role session management
│   │   │   ├── datasets.py         # CSV upload, preview, and synthetic generator
│   │   │   ├── validation.py       # Data integrity verification engine
│   │   │   ├── preprocessing.py    # Cleaning, scaling, and train/test splitting
│   │   │   ├── features.py         # Domain feature synthesis
│   │   │   ├── eda.py              # Statistical distributions and correlations
│   │   │   ├── models.py           # Classifier training and registry
│   │   │   ├── predictions.py      # Real-time single & batch inference
│   │   │   ├── risk.py             # Multi-factor risk scoring engine
│   │   │   ├── transactions.py     # Search, filter, and pagination
│   │   │   ├── suspicious.py       # Investigation queue & auditor workflow
│   │   │   ├── explainability.py   # Global and local feature attributions
│   │   │   ├── reports.py          # PDF and HTML report generator
│   │   │   ├── exports.py          # Local CSV and JSON data export
│   │   │   ├── history.py          # Immutable audit logging
│   │   │   └── settings.py         # Platform threshold parameters
│   │   ├── core/                   # Shared system utilities
│   │   ├── models/schemas.py       # Pydantic request/response schemas
│   │   └── services/               # Pure business logic and ML engines
│   └── requirements.txt
├── frontend/                       # React 18 + TypeScript + Vite + Tailwind CSS
│   ├── src/
│   │   ├── components/             # Reusable UI cards, tables, badges, buttons
│   │   ├── context/                # AuthContext and AppStateContext
│   │   ├── services/api.ts         # Axios/Fetch API client
│   │   ├── types/index.ts          # TypeScript interfaces
│   │   └── pages/                  # 20 distinct interactive pages
│   ├── package.json
│   └── vite.config.ts
├── data/                           # Local CSV datasets and JSON stores
├── models/                         # Serialized .joblib model binaries & metadata
├── reports/                        # Compiled PDF & HTML reports
├── exports/                        # Generated CSV & JSON export files
├── logs/                           # Runtime log files
├── tests/                          # Automated pytest suite (20/20 passing)
└── docs/                           # Architectural, data, and ML documentation
```

---

## 3. Machine Learning Pipeline Architecture
1. **Ingestion & Validation**: Checks structural integrity, column presence, negative values, and extreme outliers.
2. **Preprocessing**: Imputes nulls via median/mode, removes duplicate transaction IDs, encodes categorical attributes, and scales numerical values.
3. **Domain Feature Engineering**: Computes amount deviation from customer mean, amount-to-previous ratio, night-hour transactions (01:00–05:00 AM), high velocity bursts, and geographic displacements.
4. **Model Training & Evaluation**: Concurrently trains and compares 5 algorithms:
   - Logistic Regression
   - Decision Tree
   - Random Forest Classifier (100 estimators)
   - Gradient Boosting Classifier
   - Isolation Forest (Unsupervised Anomaly Detector)
5. **Evaluation**: Assesses Precision, Recall, F1-Score, and ROC-AUC. Selects best model based on F1-Score to balance false negatives and false positives.
6. **Risk Scoring Engine**: Blends ML probability (55%) with rule-based heuristics (45%) into a calibrated 0–100 integer score.
