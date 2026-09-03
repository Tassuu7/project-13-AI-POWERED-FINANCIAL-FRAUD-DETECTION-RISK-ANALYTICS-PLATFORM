# Canonical Data Dictionary — AI-Powered Financial Fraud Detection Platform

## Core Transaction Dataset Schema

| Column Name | Data Type | Permitted Values / Range | Description & Fraud Detection Context |
| :--- | :--- | :--- | :--- |
| `transaction_id` | String | `TXN-100000` to `TXN-999999` | Unique primary transaction identifier. Duplicate IDs trigger validation errors. |
| `customer_id` | String | `CUST-1000` to `CUST-9999` | Anonymized unique customer identifier used to calculate baseline averages. |
| `timestamp` | Datetime | `YYYY-MM-DD HH:MM:SS` | Transaction authorization timestamp. Used to derive temporal anomaly indicators. |
| `amount` | Float | `₹50.00` to `₹10,00,000.00` | Gross financial transaction value in Indian Rupees (INR). |
| `transaction_type` | Categorical | `Online`, `POS / In-Store`, `ATM Withdrawal`, `UPI Transfer`, `Wire Transfer` | Originating payment instrument and channel. |
| `merchant_category` | Categorical | `Grocery & Supermarkets`, `Dining & Food`, `Electronics & Gadgets`, `Crypto & Digital Assets`, `Luxury Goods & Jewelry` | Retail segment classification. High-liquidity categories receive increased risk weights. |
| `location` | Categorical | `Mumbai`, `Delhi`, `Bengaluru`, `Hyderabad`, `Chennai`, `Kolkata`, `Pune`, `Ahmedabad`, etc. | Physical or IP geolocation of payment origination. |
| `device_type` | Categorical | `Trusted Mobile App (iOS)`, `Trusted Mobile App (Android)`, `Desktop Web Browser`, `Unknown Device`, `New Emulated Device` | Client hardware and environment fingerprint. Unfamiliar devices escalate risk score. |
| `account_age_days` | Integer | `1` to `3650` days | Time elapsed since account opening. Accounts younger than 45 days face higher fraud rates. |
| `transaction_frequency`| Integer | `1` to `25` txns/hr | Number of transactions initiated by customer within current observation window. |
| `previous_transaction_amount` | Float | `₹0.00` to `₹5,00,000.00` | Dollar value of the most recent preceding transaction for baseline ratio calculation. |
| `distance_from_usual_location` | Float | `0.1` to `1,500.0` km | Radial geographic distance from the customer's registered primary cluster. |
| `is_fraud` | Binary | `0` or `1` | Ground-truth verification label: `0` for Legitimate/Normal, `1` for Fraudulent. |

---

## Synthesized Domain Features

| Feature Name | Derived From | Calculation & Rationale |
| :--- | :--- | :--- |
| `amount_to_prev_ratio` | `amount`, `previous_transaction_amount` | `amount / max(previous_amount, 100)`. Ratios &gt; 3.5x signal potential account takeover. |
| `amount_deviation` | `amount`, `customer_id` | `amount - customer_mean`. Absolute departure from typical individual expenditure. |
| `is_night_transaction` | `timestamp` | Binary flag for hours between 01:00 AM and 05:00 AM (elevated automated fraud window). |
| `is_high_value` | `amount` | Flag for amounts &gt;= ₹50,000 requiring elevated step-up security. |
| `high_velocity_flag` | `transaction_frequency` | Flag for frequency &gt;= 5 txns/hr (characteristic of card testing bots). |
| `distance_anomaly` | `distance_from_usual_location` | Flag for geographic displacement exceeding 100 km. |
| `suspicious_device_flag` | `device_type` | Flag for unknown, emulated, or rooted device fingerprints. |
| `compound_risk_index` | Multiple | Composite index combining high value, night hours, distance, and device anomalies. |
