"""Transparent risk scoring engine combining ML probabilities with verifiable heuristic rules."""

from typing import Dict, List, Any, Tuple
from backend.app.models.schemas import RiskFactor, PredictionResult, SingleTransactionInput
from config.settings import settings


class RiskScoringService:
    def calculate_risk(
        self,
        tx_dict: Dict[str, Any],
        ml_probability: float,
        model_name: str
    ) -> PredictionResult:
        """Compute calibrated 0-100 risk score and explainable contributing factors."""
        factors: List[RiskFactor] = []
        heuristic_score = 0.0

        amount = float(tx_dict.get("amount", 0.0))
        prev_amount = float(tx_dict.get("previous_transaction_amount", 1000.0))
        dist = float(tx_dict.get("distance_from_usual_location", 0.0))
        device = str(tx_dict.get("device_type", ""))
        category = str(tx_dict.get("merchant_category", ""))
        frequency = int(tx_dict.get("transaction_frequency", 1))
        account_age = int(tx_dict.get("account_age_days", 365))
        tx_type = str(tx_dict.get("transaction_type", ""))
        timestamp_str = str(tx_dict.get("timestamp", ""))

        # 1. Amount Surge Factor
        ratio = amount / max(100.0, prev_amount)
        if amount >= 100000.0 or ratio >= 5.0:
            heuristic_score += 35.0
            factors.append(RiskFactor(
                factor="Extreme Amount Surge",
                impact="HIGH",
                description=f"Transaction of ₹{amount:,.2f} is {ratio:.1f}x higher than historical baseline of ₹{prev_amount:,.2f}."
            ))
        elif amount >= 30000.0 or ratio >= 2.5:
            heuristic_score += 20.0
            factors.append(RiskFactor(
                factor="Elevated Amount Deviation",
                impact="MEDIUM",
                description=f"Transaction amount of ₹{amount:,.2f} is moderately higher than usual activity."
            ))

        # 2. Time-of-Day Factor
        hour = 12
        if ":" in timestamp_str:
            try:
                if " " in timestamp_str:
                    time_part = timestamp_str.split(" ")[1]
                else:
                    time_part = timestamp_str
                hour = int(time_part.split(":")[0])
            except Exception:
                hour = 12

        if 1 <= hour <= 5:
            heuristic_score += 25.0
            factors.append(RiskFactor(
                factor="Anomalous Transaction Time",
                impact="HIGH" if heuristic_score > 30 else "MEDIUM",
                description=f"Transaction initiated at {hour:02d}:00 hours (vulnerable window: 01:00 - 05:00 AM)."
            ))

        # 3. Location Displacement Factor
        if dist >= 200.0:
            heuristic_score += 30.0
            factors.append(RiskFactor(
                factor="Severe Geographic Displacement",
                impact="HIGH",
                description=f"Transaction located {dist:.1f} km from user's registered home cluster."
            ))
        elif dist >= 80.0:
            heuristic_score += 15.0
            factors.append(RiskFactor(
                factor="Moderate Geographic Deviation",
                impact="MEDIUM",
                description=f"Transaction originated {dist:.1f} km away from typical usage radius."
            ))

        # 4. Device Fingerprint Factor
        if any(untrusted in device for untrusted in ["Unknown", "Emulated", "Rooted", "Tor"]):
            heuristic_score += 25.0
            factors.append(RiskFactor(
                factor="Untrusted Device Fingerprint",
                impact="HIGH",
                description=f"Hardware fingerprint '{device}' is not registered in user's known device list."
            ))

        # 5. Velocity Spike
        if frequency >= 5:
            heuristic_score += 20.0
            factors.append(RiskFactor(
                factor="Rapid Transaction Velocity",
                impact="MEDIUM",
                description=f"{frequency} transactions executed within a short monitoring window."
            ))

        # 6. Merchant / Channel Risk
        if any(high_risk in category for high_risk in ["Crypto", "Digital Assets", "Luxury Goods", "Jewelry"]):
            heuristic_score += 15.0
            factors.append(RiskFactor(
                factor="High-Liquidity Merchant Category",
                impact="LOW",
                description=f"Merchant category '{category}' represents a rapid cash-out vector."
            ))

        # 7. Account Youth
        if account_age < 45:
            heuristic_score += 10.0
            factors.append(RiskFactor(
                factor="New Account Velocity",
                impact="LOW",
                description=f"Account age ({account_age} days) has not completed the 60-day stabilization window."
            ))

        # Calibration: 55% ML probability + 45% domain heuristic
        ml_score = ml_probability * 100.0
        heuristic_score = min(100.0, heuristic_score)

        blended_score = int(round(0.55 * ml_score + 0.45 * heuristic_score))
        blended_score = max(1, min(99, blended_score))

        # Band determination
        if blended_score <= settings.RISK_LOW_MAX:
            risk_level = "LOW"
            prediction_label = "Normal"
            is_suspicious = False
            rec_action = "Approve / Standard Processing"
        elif blended_score <= settings.RISK_MEDIUM_MAX:
            risk_level = "MEDIUM"
            prediction_label = "Requires Review"
            is_suspicious = True
            rec_action = "Trigger Secondary Step-Up Authentication (SMS OTP / Biometric)"
        else:
            risk_level = "HIGH"
            prediction_label = "Potentially Suspicious"
            is_suspicious = True
            rec_action = "Hold Transaction & Route to Fraud Investigation Desk"

        if not factors:
            factors.append(RiskFactor(
                factor="Baseline Conformity",
                impact="LOW",
                description="Transaction parameters align consistently with customer historical habits."
            ))

        tx_id = str(tx_dict.get("transaction_id", f"TXN-{int(amount * 7) % 999999}"))
        cust_id = str(tx_dict.get("customer_id", "CUST-VERIFIED"))

        return PredictionResult(
            transaction_id=tx_id,
            customer_id=cust_id,
            amount=amount,
            prediction_label=prediction_label,
            is_suspicious=is_suspicious,
            risk_score=blended_score,
            risk_level=risk_level,
            confidence_probability=round(ml_probability, 4),
            contributing_factors=factors,
            recommended_action=rec_action,
            model_used=model_name
        )


risk_service = RiskScoringService()
