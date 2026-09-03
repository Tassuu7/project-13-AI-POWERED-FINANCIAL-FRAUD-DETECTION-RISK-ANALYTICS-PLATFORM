"""Data validation engine assessing dataset integrity, schema, types, and outliers."""

from typing import List, Dict, Any, Tuple
import numpy as np
import pandas as pd
from backend.app.models.schemas import ValidationReport, ValidationCheck
from config.logging_config import logger

REQUIRED_COLUMNS = [
    "transaction_id", "customer_id", "timestamp", "amount",
    "transaction_type", "merchant_category", "location", "device_type"
]


class ValidationService:
    def validate(self, df: pd.DataFrame) -> ValidationReport:
        checks: List[ValidationCheck] = []
        recommended_actions: List[str] = []
        total_records = len(df)

        if total_records == 0:
            return ValidationReport(
                valid=False,
                total_records=0,
                total_checks=1,
                passed_checks=0,
                failed_checks=1,
                checks=[
                    ValidationCheck(
                        name="Empty Dataset Check",
                        passed=False,
                        severity="error",
                        details="The dataset contains zero rows.",
                        affected_count=0
                    )
                ],
                recommended_actions=["Upload a non-empty CSV dataset with transaction records."]
            )

        # 1. Required Columns Check
        missing_cols = [col for col in REQUIRED_COLUMNS if col not in df.columns]
        if missing_cols:
            checks.append(ValidationCheck(
                name="Required Columns Verification",
                passed=False,
                severity="error",
                details=f"Missing essential columns: {', '.join(missing_cols)}",
                affected_count=len(missing_cols)
            ))
            recommended_actions.append(f"Ensure dataset contains the mandatory columns: {', '.join(REQUIRED_COLUMNS)}")
        else:
            checks.append(ValidationCheck(
                name="Required Columns Verification",
                passed=True,
                severity="info",
                details="All mandatory transaction columns are present.",
                affected_count=0
            ))

        # 2. Missing Values Check
        null_counts = df.isnull().sum().to_dict()
        total_nulls = sum(null_counts.values())
        if total_nulls > 0:
            null_cols = [f"{col} ({cnt})" for col, cnt in null_counts.items() if cnt > 0]
            checks.append(ValidationCheck(
                name="Missing Values Detection",
                passed=False,
                severity="warning",
                details=f"Found {total_nulls} missing values in: {', '.join(null_cols)}",
                affected_count=total_nulls
            ))
            recommended_actions.append("Apply missing value imputation during Preprocessing.")
        else:
            checks.append(ValidationCheck(
                name="Missing Values Detection",
                passed=True,
                severity="info",
                details="No missing or NaN values detected in dataset.",
                affected_count=0
            ))

        # 3. Duplicate Transaction ID Check
        if "transaction_id" in df.columns:
            dup_id_count = df["transaction_id"].duplicated().sum()
            if dup_id_count > 0:
                checks.append(ValidationCheck(
                    name="Unique Transaction IDs",
                    passed=False,
                    severity="error",
                    details=f"Found {dup_id_count} duplicate transaction IDs.",
                    affected_count=int(dup_id_count)
                ))
                recommended_actions.append("Deduplicate records by transaction ID in Preprocessing.")
            else:
                checks.append(ValidationCheck(
                    name="Unique Transaction IDs",
                    passed=True,
                    severity="info",
                    details="All transaction IDs are unique.",
                    affected_count=0
                ))

        # 4. Entire Row Duplicates Check
        dup_rows = df.duplicated().sum()
        if dup_rows > 0:
            checks.append(ValidationCheck(
                name="Duplicate Rows Check",
                passed=False,
                severity="warning",
                details=f"Found {dup_rows} identical duplicate rows.",
                affected_count=int(dup_rows)
            ))
            recommended_actions.append("Enable duplicate row removal in the Preprocessing step.")
        else:
            checks.append(ValidationCheck(
                name="Duplicate Rows Check",
                passed=True,
                severity="info",
                details="No duplicate rows found.",
                affected_count=0
            ))

        # 5. Transaction Amount Validation
        if "amount" in df.columns:
            try:
                numeric_amounts = pd.to_numeric(df["amount"], errors="coerce")
                non_num_count = numeric_amounts.isnull().sum() - df["amount"].isnull().sum()
                negative_count = (numeric_amounts < 0).sum()
                zero_count = (numeric_amounts == 0).sum()

                if non_num_count > 0 or negative_count > 0:
                    details = []
                    if non_num_count > 0:
                        details.append(f"{non_num_count} non-numeric amounts")
                    if negative_count > 0:
                        details.append(f"{negative_count} negative amounts")
                    checks.append(ValidationCheck(
                        name="Amount Integrity Check",
                        passed=False,
                        severity="error",
                        details=f"Invalid transaction amounts: {', '.join(details)}",
                        affected_count=int(non_num_count + negative_count)
                    ))
                    recommended_actions.append("Cleanse or filter non-positive transaction amounts.")
                elif zero_count > 0:
                    checks.append(ValidationCheck(
                        name="Amount Integrity Check",
                        passed=True,
                        severity="warning",
                        details=f"{zero_count} zero-value transactions found (may represent authorization tests).",
                        affected_count=int(zero_count)
                    ))
                else:
                    checks.append(ValidationCheck(
                        name="Amount Integrity Check",
                        passed=True,
                        severity="info",
                        details=f"All transaction amounts are positive (min: ₹{numeric_amounts.min():.2f}, max: ₹{numeric_amounts.max():.2f}).",
                        affected_count=0
                    ))
            except Exception as e:
                checks.append(ValidationCheck(
                    name="Amount Integrity Check",
                    passed=False,
                    severity="error",
                    details=f"Error evaluating amounts: {e}",
                    affected_count=total_records
                ))

        # 6. Timestamp Format Validation
        if "timestamp" in df.columns:
            try:
                parsed_dates = pd.to_datetime(df["timestamp"], errors="coerce")
                invalid_dates = parsed_dates.isnull().sum() - df["timestamp"].isnull().sum()
                if invalid_dates > 0:
                    checks.append(ValidationCheck(
                        name="Timestamp Format Validity",
                        passed=False,
                        severity="error",
                        details=f"Found {invalid_dates} unparseable timestamps.",
                        affected_count=int(invalid_dates)
                    ))
                    recommended_actions.append("Ensure timestamps conform to ISO or standard YYYY-MM-DD HH:MM:SS format.")
                else:
                    checks.append(ValidationCheck(
                        name="Timestamp Format Validity",
                        passed=True,
                        severity="info",
                        details=f"All timestamps valid ({parsed_dates.min().strftime('%Y-%m-%d')} to {parsed_dates.max().strftime('%Y-%m-%d')}).",
                        affected_count=0
                    ))
            except Exception as e:
                checks.append(ValidationCheck(
                    name="Timestamp Format Validity",
                    passed=False,
                    severity="error",
                    details=f"Timestamp check error: {e}",
                    affected_count=total_records
                ))

        # 7. Fraud Label Verification (if present)
        if "is_fraud" in df.columns:
            unique_labels = set(df["is_fraud"].dropna().unique())
            valid_labels = {0, 1, 0.0, 1.0, "0", "1"}
            if not unique_labels.issubset(valid_labels):
                checks.append(ValidationCheck(
                    name="Fraud Label Verification",
                    passed=False,
                    severity="error",
                    details=f"Unexpected fraud labels found: {unique_labels}. Must be 0 (Normal) or 1 (Fraud).",
                    affected_count=int((~df["is_fraud"].isin([0, 1])).sum())
                ))
            else:
                fraud_count = int(df["is_fraud"].sum())
                fraud_pct = (fraud_count / total_records) * 100.0
                checks.append(ValidationCheck(
                    name="Fraud Label Verification",
                    passed=True,
                    severity="info",
                    details=f"Target column 'is_fraud' valid ({fraud_count} fraud cases, {fraud_pct:.2f}% prevalence).",
                    affected_count=0
                ))

        # 8. Outlier & Extreme Value Inspection
        if "amount" in df.columns and pd.api.types.is_numeric_dtype(df["amount"]):
            p99 = df["amount"].quantile(0.99)
            extreme_outliers = (df["amount"] > 500000).sum()
            if extreme_outliers > 0:
                checks.append(ValidationCheck(
                    name="Extreme Outlier Detection",
                    passed=True,
                    severity="warning",
                    details=f"{extreme_outliers} transactions exceed ₹5,00,000 (99th percentile: ₹{p99:.2f}).",
                    affected_count=int(extreme_outliers)
                ))
            else:
                checks.append(ValidationCheck(
                    name="Extreme Outlier Detection",
                    passed=True,
                    severity="info",
                    details=f"Transaction amounts within standard enterprise parameters (99th pct: ₹{p99:.2f}).",
                    affected_count=0
                ))

        total_checks = len(checks)
        passed_checks = sum(1 for c in checks if c.passed)
        failed_checks = sum(1 for c in checks if not c.passed)
        has_critical_error = any(not c.passed and c.severity == "error" for c in checks)

        if not recommended_actions:
            recommended_actions.append("Dataset passed all validation checks. Ready for Preprocessing and ML modeling.")

        return ValidationReport(
            valid=not has_critical_error,
            total_records=total_records,
            total_checks=total_checks,
            passed_checks=passed_checks,
            failed_checks=failed_checks,
            checks=checks,
            recommended_actions=recommended_actions
        )


validation_service = ValidationService()
