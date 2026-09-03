"""Machine Learning service managing model training, multi-algorithm evaluation, and inference."""

import time
from typing import Dict, List, Any, Tuple, Optional
from datetime import datetime
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, IsolationForest
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from backend.app.models.schemas import ModelType, ModelTrainRequest, ModelMetrics, ModelComparisonResponse
from backend.app.services.storage_service import storage_service
from config.settings import settings
from config.logging_config import logger


class MLService:
    def __init__(self):
        self.feature_columns: List[str] = [
            "amount", "account_age_days", "transaction_frequency",
            "distance_from_usual_location", "amount_to_prev_ratio",
            "amount_deviation", "is_night_transaction", "is_high_value",
            "high_velocity_flag", "distance_anomaly", "suspicious_device_flag",
            "account_youth_risk", "compound_risk_index"
        ]
        self.scaler = StandardScaler()
        self.active_model_name: str = "Random Forest"

    def _prepare_features(self, df: pd.DataFrame, is_training: bool = False) -> Tuple[np.ndarray, Optional[np.ndarray], List[str]]:
        """Extract and align numeric modeling features."""
        # Ensure engineered features exist
        from backend.app.services.feature_service import feature_service
        prepared_df, _ = feature_service.engineer_features(df)

        # Ensure all required feature columns exist in prepared_df
        for col in self.feature_columns:
            if col not in prepared_df.columns:
                prepared_df[col] = 0.0

        # Always select features in exact canonical order
        X = prepared_df[self.feature_columns].fillna(0).to_numpy()

        if is_training:
            self.scaler.fit(X)
            # Save scaler
            storage_service.save_model_artifact("feature_scaler", self.scaler, {"features": self.feature_columns})
            X_scaled = self.scaler.transform(X)
        else:
            try:
                scaler_obj, _ = storage_service.load_model_artifact("feature_scaler")
                X_scaled = scaler_obj.transform(X)
            except Exception:
                X_scaled = self.scaler.fit_transform(X)

        y = prepared_df["is_fraud"].to_numpy() if "is_fraud" in prepared_df.columns else None
        return X_scaled, y, self.feature_columns

    def train_models(self, df: pd.DataFrame, req: ModelTrainRequest) -> ModelComparisonResponse:
        """Train and rigorously compare multiple machine learning algorithms."""
        logger.info(f"Initiating ML training for models: {[m.value for m in req.models_to_train]}")

        X, y, feature_names = self._prepare_features(df, is_training=True)

        if y is None:
            raise ValueError("Target column 'is_fraud' is required for model training.")

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=req.test_size, random_state=req.random_state, stratify=y
        )

        model_results: List[ModelMetrics] = []
        best_f1 = -1.0
        best_model_name = ""

        for model_type in req.models_to_train:
            t0 = time.time()
            m_name = model_type.value

            if model_type == ModelType.LOGISTIC_REGRESSION:
                clf = LogisticRegression(
                    class_weight="balanced" if req.handle_imbalance else None,
                    max_iter=1000,
                    random_state=req.random_state
                )
                clf.fit(X_train, y_train)
                y_pred = clf.predict(X_test)
                y_prob = clf.predict_proba(X_test)[:, 1]
                notes = "Linear baseline with balanced class weights. High interpretability."

            elif model_type == ModelType.DECISION_TREE:
                clf = DecisionTreeClassifier(
                    max_depth=6,
                    class_weight="balanced" if req.handle_imbalance else None,
                    random_state=req.random_state
                )
                clf.fit(X_train, y_train)
                y_pred = clf.predict(X_test)
                y_prob = clf.predict_proba(X_test)[:, 1]
                notes = "Interpretable tree structure capturing non-linear threshold patterns."

            elif model_type == ModelType.RANDOM_FOREST:
                clf = RandomForestClassifier(
                    n_estimators=100,
                    max_depth=8,
                    class_weight="balanced" if req.handle_imbalance else None,
                    random_state=req.random_state,
                    n_jobs=-1
                )
                clf.fit(X_train, y_train)
                y_pred = clf.predict(X_test)
                y_prob = clf.predict_proba(X_test)[:, 1]
                notes = "Ensemble of 100 decision trees. Robust against overfitting, excellent recall."

            elif model_type == ModelType.GRADIENT_BOOSTING:
                clf = GradientBoostingClassifier(
                    n_estimators=100,
                    learning_rate=0.08,
                    max_depth=4,
                    random_state=req.random_state
                )
                clf.fit(X_train, y_train)
                y_pred = clf.predict(X_test)
                y_prob = clf.predict_proba(X_test)[:, 1]
                notes = "Sequential boosting optimizing residual loss. High precision."

            elif model_type == ModelType.ISOLATION_FOREST:
                # Unsupervised anomaly detection
                contamination = float(np.mean(y_train)) if np.mean(y_train) > 0 else 0.05
                clf = IsolationForest(
                    contamination=max(0.01, min(0.2, contamination)),
                    random_state=req.random_state
                )
                clf.fit(X_train)
                raw_pred = clf.predict(X_test)
                # Map Isolation Forest (-1: anomaly, 1: normal) to (1: fraud, 0: normal)
                y_pred = np.where(raw_pred == -1, 1, 0)
                scores = -clf.decision_function(X_test)
                y_prob = (scores - scores.min()) / (scores.max() - scores.min() + 1e-9)
                notes = "Unsupervised tree isolation. Detects novel, zero-day fraud anomalies."

            else:
                continue

            duration = round(time.time() - t0, 3)

            # Metrics
            acc = round(float(accuracy_score(y_test, y_pred)), 4)
            prec = round(float(precision_score(y_test, y_pred, zero_division=0)), 4)
            rec = round(float(recall_score(y_test, y_pred, zero_division=0)), 4)
            f1 = round(float(f1_score(y_test, y_pred, zero_division=0)), 4)

            try:
                roc = round(float(roc_auc_score(y_test, y_prob)), 4)
            except Exception:
                roc = None

            cm = confusion_matrix(y_test, y_pred).tolist()

            is_curr_best = f1 > best_f1
            if is_curr_best:
                best_f1 = f1
                best_model_name = m_name

            metrics = ModelMetrics(
                model_name=m_name,
                accuracy=acc,
                precision=prec,
                recall=rec,
                f1_score=f1,
                roc_auc=roc,
                training_time_seconds=duration,
                confusion_matrix=cm,
                is_best=False,
                notes=notes
            )
            model_results.append(metrics)

            # Save model artifact locally
            metadata = {
                "model_name": m_name,
                "dataset_name": req.dataset_name,
                "trained_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "features": feature_names,
                "metrics": metrics.model_dump()
            }
            storage_service.save_model_artifact(m_name, clf, metadata)

        # Mark best model
        for m in model_results:
            if m.model_name == best_model_name:
                m.is_best = True
                self.active_model_name = best_model_name

        response = ModelComparisonResponse(
            trained_timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            dataset_name=req.dataset_name,
            total_train_samples=len(X_train),
            total_test_samples=len(X_test),
            best_model_name=best_model_name or (model_results[0].model_name if model_results else "None"),
            models=model_results
        )

        return response

    def predict_single(self, input_data: Dict[str, Any], model_name: Optional[str] = None) -> Tuple[int, float, str]:
        """Perform inference on single transaction."""
        m_name = model_name or self.active_model_name
        try:
            clf, meta = storage_service.load_model_artifact(m_name)
        except Exception:
            # Fallback to Random Forest or first available
            trained = storage_service.list_trained_models()
            if trained:
                m_name = trained[0]["model_name"]
                clf, meta = storage_service.load_model_artifact(m_name)
            else:
                # Rule-based fallback if no model trained yet
                return self._rule_based_fallback(input_data)

        single_df = pd.DataFrame([input_data])
        X, _, _ = self._prepare_features(single_df, is_training=False)

        if isinstance(clf, IsolationForest):
            raw_pred = clf.predict(X)[0]
            is_suspicious = 1 if raw_pred == -1 else 0
            score = -clf.decision_function(X)[0]
            prob = float(min(1.0, max(0.0, score + 0.5)))
        else:
            is_suspicious = int(clf.predict(X)[0])
            if hasattr(clf, "predict_proba"):
                prob = float(clf.predict_proba(X)[0][1])
            else:
                prob = 0.9 if is_suspicious else 0.1

        return is_suspicious, prob, m_name

    def _rule_based_fallback(self, tx: Dict[str, Any]) -> Tuple[int, float, str]:
        amount = float(tx.get("amount", 0))
        dist = float(tx.get("distance_from_usual_location", 0))
        freq = int(tx.get("transaction_frequency", 1))
        
        score = 0
        if amount > 50000:
            score += 45
        if dist > 100:
            score += 25
        if freq >= 5:
            score += 20
        if "Unknown" in str(tx.get("device_type", "")):
            score += 15
            
        prob = min(0.98, score / 100.0)
        is_suspicious = 1 if prob >= 0.5 else 0
        return is_suspicious, prob, "Rule-Based Heuristic (Pre-trained Baseline)"


ml_service = MLService()
