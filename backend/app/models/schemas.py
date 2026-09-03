"""Pydantic schemas and data validation models for API requests and responses."""

from typing import Dict, List, Optional, Any
from enum import Enum
from pydantic import BaseModel, Field


# --- Auth & Roles ---
class UserRole(str, Enum):
    ANALYST = "Analyst"
    REVIEWER = "Reviewer"
    ADMIN = "Administrator"


class LoginRequest(BaseModel):
    username: str
    role: UserRole = UserRole.ANALYST
    demo_mode: bool = True


class UserSession(BaseModel):
    username: str
    role: UserRole
    authenticated: bool
    permissions: List[str]


# --- Synthetic Data Generation ---
class SyntheticGenerateRequest(BaseModel):
    num_records: int = Field(default=1000, ge=50, le=50000)
    num_customers: int = Field(default=150, ge=10, le=5000)
    fraud_percentage: float = Field(default=5.0, ge=0.5, le=40.0)
    random_seed: int = Field(default=42, ge=0)
    start_date: Optional[str] = "2025-01-01"
    end_date: Optional[str] = "2025-06-30"
    locations: Optional[List[str]] = None
    transaction_types: Optional[List[str]] = None
    merchant_categories: Optional[List[str]] = None
    device_types: Optional[List[str]] = None


# --- Dataset & Validation ---
class DatasetInfo(BaseModel):
    filename: str
    file_size_bytes: int
    row_count: int
    column_count: int
    columns: List[str]
    has_labels: bool
    fraud_count: Optional[int] = 0
    fraud_rate: Optional[float] = 0.0


class ValidationCheck(BaseModel):
    name: str
    passed: bool
    severity: str  # "error", "warning", "info"
    details: str
    affected_count: int = 0


class ValidationReport(BaseModel):
    valid: bool
    total_records: int
    total_checks: int
    passed_checks: int
    failed_checks: int
    checks: List[ValidationCheck]
    recommended_actions: List[str]


# --- Preprocessing & Feature Engineering ---
class PreprocessingRequest(BaseModel):
    filename: str
    handle_missing: str = "median_mode"  # "median_mode", "drop", "constant"
    handle_duplicates: bool = True
    scaling_method: str = "standard"  # "standard", "minmax", "robust"
    test_size: float = Field(default=0.2, ge=0.1, le=0.4)
    random_state: int = 42


class PreprocessingResult(BaseModel):
    original_shape: List[int]
    processed_shape: List[int]
    train_shape: List[int]
    test_shape: List[int]
    missing_values_handled: int
    duplicates_removed: int
    encoded_columns: List[str]
    scaled_columns: List[str]
    summary_notes: List[str]


class FeatureSummary(BaseModel):
    feature_name: str
    feature_type: str
    description: str
    importance_rank: Optional[int] = None


class FeatureEngineeringResponse(BaseModel):
    original_feature_count: int
    new_feature_count: int
    created_features: List[FeatureSummary]
    sample_preview: List[Dict[str, Any]]


# --- Model Training & Evaluation ---
class ModelType(str, Enum):
    LOGISTIC_REGRESSION = "Logistic Regression"
    DECISION_TREE = "Decision Tree"
    RANDOM_FOREST = "Random Forest"
    GRADIENT_BOOSTING = "Gradient Boosting"
    ISOLATION_FOREST = "Isolation Forest"


class ModelTrainRequest(BaseModel):
    dataset_name: str
    models_to_train: List[ModelType] = [
        ModelType.LOGISTIC_REGRESSION,
        ModelType.RANDOM_FOREST,
        ModelType.GRADIENT_BOOSTING
    ]
    handle_imbalance: bool = True  # class_weight / oversampling
    test_size: float = 0.2
    random_state: int = 42


class ModelMetrics(BaseModel):
    model_name: str
    accuracy: float
    precision: float
    recall: float
    f1_score: float
    roc_auc: Optional[float] = None
    training_time_seconds: float
    confusion_matrix: List[List[int]]
    is_best: bool = False
    notes: str


class ModelComparisonResponse(BaseModel):
    trained_timestamp: str
    dataset_name: str
    total_train_samples: int
    total_test_samples: int
    best_model_name: str
    models: List[ModelMetrics]


# --- Prediction & Risk Scoring ---
class SingleTransactionInput(BaseModel):
    amount: float = Field(..., gt=0)
    transaction_type: str = "Online"
    merchant_category: str = "Electronics"
    location: str = "Mumbai"
    device_type: str = "Mobile"
    timestamp: Optional[str] = "2025-03-01 03:15:00"
    account_age_days: int = 180
    transaction_frequency: int = 2
    previous_transaction_amount: float = 1200.0
    distance_from_usual_location: float = 15.0
    customer_id: Optional[str] = "CUST-9999"


class RiskFactor(BaseModel):
    factor: str
    impact: str  # "HIGH", "MEDIUM", "LOW"
    description: str


class PredictionResult(BaseModel):
    transaction_id: str
    customer_id: str
    amount: float
    prediction_label: str  # "Normal" or "Potentially Suspicious"
    is_suspicious: bool
    risk_score: int  # 0 to 100
    risk_level: str  # "LOW", "MEDIUM", "HIGH"
    confidence_probability: float
    contributing_factors: List[RiskFactor]
    recommended_action: str
    model_used: str


class BatchPredictionRequest(BaseModel):
    filename: str
    model_name: Optional[str] = None


# --- Suspicious Transactions Review ---
class ReviewStatus(str, Enum):
    NEW = "New"
    UNDER_REVIEW = "Under Review"
    INVESTIGATING = "Investigating"
    CLEARED = "Cleared"
    CONFIRMED_SUSPICIOUS = "Confirmed Suspicious"


class SuspiciousItem(BaseModel):
    transaction_id: str
    customer_id: str
    amount: float
    timestamp: str
    location: str
    device_type: str
    risk_score: int
    risk_level: str
    review_status: ReviewStatus = ReviewStatus.NEW
    review_notes: Optional[str] = ""
    assigned_analyst: Optional[str] = "Unassigned"
    last_updated: Optional[str] = ""
    flags: List[str]


class ReviewUpdateRequest(BaseModel):
    review_status: ReviewStatus
    review_notes: str
    analyst_name: str


# --- Reports & History ---
class ReportType(str, Enum):
    DATASET_SUMMARY = "Dataset Overview Report"
    FRAUD_ANALYSIS = "Fraud Risk Analysis Report"
    MODEL_PERFORMANCE = "ML Model Evaluation Report"
    SUSPICIOUS_INVESTIGATION = "Suspicious Transaction Audit"
    EXECUTIVE_SUMMARY = "Executive Risk Summary"


class ReportRequest(BaseModel):
    report_type: ReportType
    format: str = "html"  # "html" or "pdf"
    title: Optional[str] = None
    author: Optional[str] = "Fraud Analytics Team"


class AuditLogItem(BaseModel):
    id: str
    timestamp: str
    action: str
    category: str  # "DATASET", "MODEL", "PREDICTION", "REVIEW", "EXPORT"
    user: str
    details: Dict[str, Any]
    status: str = "SUCCESS"
