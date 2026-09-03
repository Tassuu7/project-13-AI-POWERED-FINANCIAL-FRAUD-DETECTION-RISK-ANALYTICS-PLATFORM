"""Preprocessing pipeline for cleaning, encoding, scaling, and train/test splitting."""

from typing import Dict, Any, Tuple, List
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, RobustScaler, MinMaxScaler
from sklearn.model_selection import train_test_split
import joblib

from backend.app.models.schemas import PreprocessingRequest, PreprocessingResult
from config.settings import settings
from config.logging_config import logger


class PreprocessingService:
    def __init__(self):
        self.scalers: Dict[str, Any] = {}
        self.encoders: Dict[str, Any] = {}

    def preprocess(self, df: pd.DataFrame, req: PreprocessingRequest) -> Tuple[pd.DataFrame, PreprocessingResult]:
        original_shape = list(df.shape)
        summary_notes: List[str] = []
        processed_df = df.copy()

        # 1. Duplicate Handling
        duplicates_removed = 0
        if req.handle_duplicates:
            before_count = len(processed_df)
            if "transaction_id" in processed_df.columns:
                processed_df = processed_df.drop_duplicates(subset=["transaction_id"])
            processed_df = processed_df.drop_duplicates()
            duplicates_removed = before_count - len(processed_df)
            summary_notes.append(f"Deduplication removed {duplicates_removed} duplicate records.")

        # 2. Missing Values Imputation
        missing_handled = int(processed_df.isnull().sum().sum())
        if missing_handled > 0:
            if req.handle_missing == "median_mode":
                for col in processed_df.columns:
                    if processed_df[col].isnull().sum() > 0:
                        if pd.api.types.is_numeric_dtype(processed_df[col]):
                            median_val = processed_df[col].median()
                            processed_df[col] = processed_df[col].fillna(median_val)
                        else:
                            mode_val = processed_df[col].mode()
                            fill_val = mode_val[0] if not mode_val.empty else "Unknown"
                            processed_df[col] = processed_df[col].fillna(fill_val)
                summary_notes.append(f"Imputed {missing_handled} missing values using numerical median and categorical mode.")
            elif req.handle_missing == "drop":
                processed_df = processed_df.dropna()
                summary_notes.append(f"Dropped rows with missing values (handled {missing_handled} null entries).")

        # 3. Timestamp Parsing
        if "timestamp" in processed_df.columns:
            processed_df["timestamp"] = pd.to_datetime(processed_df["timestamp"], errors="coerce")
            processed_df["hour"] = processed_df["timestamp"].dt.hour.fillna(12).astype(int)
            processed_df["day_of_week"] = processed_df["timestamp"].dt.dayofweek.fillna(0).astype(int)
            processed_df["is_weekend"] = processed_df["day_of_week"].apply(lambda x: 1 if x in [5, 6] else 0)
            summary_notes.append("Extracted temporal features: 'hour', 'day_of_week', and 'is_weekend'.")

        # 4. Categorical Encoding (Tracked)
        cat_cols = ["transaction_type", "merchant_category", "device_type", "location"]
        encoded_cols = []
        for col in cat_cols:
            if col in processed_df.columns:
                # Frequency / Target friendly encoding with top categories preserved
                top_cats = processed_df[col].value_counts().nlargest(8).index
                processed_df[f"{col}_cat"] = processed_df[col].apply(lambda x: x if x in top_cats else "Other")
                dummies = pd.get_dummies(processed_df[f"{col}_cat"], prefix=col, drop_first=True, dtype=int)
                encoded_cols.extend(dummies.columns.tolist())
                processed_df = pd.concat([processed_df, dummies], axis=1)
                processed_df.drop(columns=[f"{col}_cat"], inplace=True)
                summary_notes.append(f"Encoded categorical column '{col}' into {len(dummies.columns)} indicator features.")

        # 5. Numerical Scaling
        num_cols = ["amount", "account_age_days", "transaction_frequency", "distance_from_usual_location"]
        scaled_cols = [c for c in num_cols if c in processed_df.columns]
        if scaled_cols:
            if req.scaling_method == "robust":
                scaler = RobustScaler()
            elif req.scaling_method == "minmax":
                scaler = MinMaxScaler()
            else:
                scaler = StandardScaler()
                
            scaled_features = scaler.fit_transform(processed_df[scaled_cols])
            for i, col in enumerate(scaled_cols):
                processed_df[f"{col}_scaled"] = scaled_features[:, i]
            summary_notes.append(f"Scaled numerical features ({', '.join(scaled_cols)}) using {req.scaling_method} scaler.")
            
            # Persist scaler
            scaler_path = settings.MODELS_DIR / "fitted_scaler.joblib"
            joblib.dump(scaler, scaler_path)

        # 6. Split Shapes Calculation
        train_len = int(len(processed_df) * (1.0 - req.test_size))
        test_len = len(processed_df) - train_len
        train_shape = [train_len, processed_df.shape[1]]
        test_shape = [test_len, processed_df.shape[1]]
        summary_notes.append(f"Prepared train ({train_len} samples) and test ({test_len} samples) sets (split ratio: {1.0 - req.test_size:.1f}/{req.test_size:.1f}).")

        result = PreprocessingResult(
            original_shape=original_shape,
            processed_shape=list(processed_df.shape),
            train_shape=train_shape,
            test_shape=test_shape,
            missing_values_handled=missing_handled,
            duplicates_removed=duplicates_removed,
            encoded_columns=encoded_cols,
            scaled_columns=[f"{c}_scaled" for c in scaled_cols],
            summary_notes=summary_notes
        )

        return processed_df, result


preprocessing_service = PreprocessingService()
