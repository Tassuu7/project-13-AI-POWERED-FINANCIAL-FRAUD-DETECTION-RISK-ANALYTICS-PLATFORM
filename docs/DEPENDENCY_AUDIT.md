# Dependency Inventory & License Compliance Audit

## 1. Compliance Statement
This software platform is developed as an original enterprise product. In accordance with strict development requirements:
- Zero copy-pasted or forked open-source repositories were used as project foundation.
- No GPL-licensed dependencies are included.
- No client-owned or employer-proprietary code is included.
- All third-party libraries use commercially permissive open-source licenses (MIT, Apache 2.0, BSD-3-Clause).

---

## 2. Python Backend Dependencies

| Package Name | Version Specifier | Purpose / Role | Software License |
| :--- | :--- | :--- | :--- |
| `fastapi` | &gt;= 0.110.0 | High-performance asynchronous REST API framework | MIT License |
| `uvicorn` | &gt;= 0.28.0 | ASGI production-grade web application server | BSD-3-Clause |
| `pydantic` | &gt;= 2.6.0 | Schema validation and serialization | MIT License |
| `pydantic-settings` | &gt;= 2.2.0 | Configuration management via environment variables | MIT License |
| `scikit-learn` | &gt;= 1.4.0 | Classical machine learning classifiers &amp; scalers | BSD-3-Clause |
| `pandas` | &gt;= 2.2.0 | Tabular dataset manipulation and time-series analysis | BSD-3-Clause |
| `numpy` | &gt;= 1.26.0 | Vectorized mathematical operations | BSD-3-Clause |
| `joblib` | &gt;= 1.3.0 | Fast disk serialization of fitted model pipelines | BSD-3-Clause |
| `reportlab` | &gt;= 4.1.0 | Programmatic PDF document compilation | BSD-3-Clause |
| `pytest` | &gt;= 8.0.0 | Automated unit &amp; endpoint test harness | MIT License |
| `starlette` | &gt;= 0.36.0 | Low-level ASGI routing and test client | BSD-3-Clause |

---

## 3. Frontend JavaScript / TypeScript Dependencies

| Package Name | Version Specifier | Purpose / Role | Software License |
| :--- | :--- | :--- | :--- |
| `react` | ^18.3.0 | Component rendering engine | MIT License |
| `react-dom` | ^18.3.0 | DOM mounting and state reconciliation | MIT License |
| `lucide-react` | ^0.475.0 | Authentic geometric SVG vector icons (Zero AI images) | ISC License |
| `recharts` | ^2.15.0 | Interactive enterprise data visualization charts | MIT License |
| `tailwindcss` | ^4.0.0 | Utility CSS framework (configured with 0% blue) | MIT License |
| `typescript` | ^5.8.0 | Type safety and interface contracts | Apache-2.0 |
| `vite` | ^6.0.0 | Build system and local development server | MIT License |
