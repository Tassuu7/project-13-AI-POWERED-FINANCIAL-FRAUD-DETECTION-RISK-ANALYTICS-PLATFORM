# Machine Learning Methodology & Model Evaluation

## 1. Class Imbalance Handling
Financial fraud detection suffers from extreme class imbalance: legitimate transactions account for 95%–99% of total volume. Evaluating purely on **Accuracy** gives misleading results—a trivial model predicting "Normal" for all transactions yields 96% accuracy while allowing 100% of financial fraud to occur.

To counteract this:
- Supervised algorithms (Logistic Regression, Decision Tree, Random Forest) utilize inversely proportional cost-sensitive class weighting:
  $$\text{weight}_c = \frac{N}{2 \times N_c}$$
- The primary benchmark metric is the **F1-Score** (harmonic mean of Precision and Recall) alongside **Recall** (Sensitivity):
  $$\text{Recall} = \frac{TP}{TP + FN}, \quad \text{Precision} = \frac{TP}{TP + FP}$$

---

## 2. Algorithms Implemented
1. **Logistic Regression**: Linear boundary with balanced weights providing baseline probability calibration.
2. **Decision Tree Classifier**: Interpretable orthogonal splits capturing non-linear threshold logic.
3. **Random Forest Classifier**: Ensemble of 100 decorrelated decision trees using bagging and feature sub-sampling to reduce variance.
4. **Gradient Boosting Classifier**: Sequential ensemble minimizing logistic loss via gradient descent on residual errors.
5. **Isolation Forest**: Unsupervised tree isolation isolating anomalies in few splits without requiring target labels.

---

## 3. Calibrated Risk Scoring Formula
The final integer risk score $S \in [1, 99]$ is calculated by blending model probability $P_{\text{ML}}$ with a heuristic rule index $H$:
$$S = \text{round}\left( 0.55 \times (P_{\text{ML}} \times 100) + 0.45 \times \min(100, H) \right)$$

Where $H$ is the sum of verifiable anomaly factors:
- Extreme Amount Surge: $+35$ pts
- Geographic Displacement (&gt;200 km): $+30$ pts
- Nocturnal Window (01:00–05:00 AM): $+25$ pts
- Untrusted Hardware Fingerprint: $+25$ pts
- Burst Velocity (&gt;= 5): $+20$ pts
- High-Liquidity Merchant Category: $+15$ pts
- New Account Age (&lt; 45 days): $+10$ pts

### Risk Tiers
- **0 – 30**: Low Risk (Approve / Standard Processing)
- **31 – 70**: Medium Risk (Trigger SMS OTP / Biometric Step-Up)
- **71 – 100**: High Risk (Hold Transaction &amp; Route to Fraud Analyst Desk)
