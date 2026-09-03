export type UserRole = 'Administrator' | 'Fraud Analyst' | 'Management / Viewer';

export type ModelType =
  | 'Logistic Regression'
  | 'Decision Tree'
  | 'Random Forest'
  | 'Gradient Boosting'
  | 'Isolation Forest';

export interface UserSession {
  username: string;
  display_name?: string;
  role: UserRole;
  permissions: string[];
  token: string;
}

export interface DatasetInfo {
  filename: string;
  filepath: string;
  size_bytes: number;
  modified_time: number;
  columns: string[];
  has_fraud_label: boolean;
}

export interface DatasetPreview {
  filename: string;
  total_rows: number;
  total_columns: number;
  columns: string[];
  has_fraud_label: boolean;
  fraud_count: number;
  fraud_rate: number;
  data: Record<string, any>[];
}

export interface ValidationCheck {
  name: string;
  passed: boolean;
  severity: 'error' | 'warning' | 'info';
  details: string;
  affected_count: number;
}

export interface ValidationReport {
  dataset_name: string;
  valid: boolean;
  total_records: number;
  total_columns: number;
  checks: ValidationCheck[];
  missing_values: Record<string, number>;
  duplicate_records: number;
  negative_amount_count: number;
  date_parse_errors: number;
  recommended_actions: string[];
}

export interface PreprocessingResult {
  dataset_name: string;
  original_rows: number;
  processed_rows: number;
  original_columns: number;
  processed_columns: number;
  imputed_nulls: number;
  removed_duplicates: number;
  encoded_columns: string[];
  scaler_used: string;
  train_samples: number;
  test_samples: number;
}

export interface FeatureResponse {
  dataset_name: string;
  total_features: number;
  engineered_features: {
    name: string;
    description: string;
    calculation: string;
    data_type: string;
  }[];
}

export interface ModelMetrics {
  accuracy: number;
  precision: number;
  recall: number;
  f1_score: number;
  roc_auc: number;
  latency_ms: number;
  confusion_matrix: {
    true_negatives: number;
    false_positives: number;
    false_negatives: number;
    true_positives: number;
  };
}

export interface ModelComparisonResponse {
  dataset_name: string;
  trained_models: Record<string, ModelMetrics>;
  best_model_name: string;
  comparison_metric: string;
  total_train_samples: number;
  total_test_samples: number;
}

export interface PredictionResult {
  transaction_id: string;
  is_fraud: boolean;
  fraud_probability: number;
  risk_score: number;
  risk_level: 'LOW' | 'MEDIUM' | 'HIGH';
  prediction_label: string;
  contributing_factors: string[];
  policy_recommendation: string;
}

export type ReviewStatus =
  | 'New'
  | 'Under Review'
  | 'Investigating'
  | 'Cleared'
  | 'Confirmed Suspicious';

export interface SuspiciousItem {
  transaction_id: string;
  customer_id: string;
  amount: number;
  timestamp: string;
  location: string;
  device_type: string;
  risk_score: number;
  risk_level: 'LOW' | 'MEDIUM' | 'HIGH';
  review_status: ReviewStatus;
  review_notes?: string;
  assigned_analyst?: string;
  last_updated?: string;
}

export interface AuditLogItem {
  id: string;
  timestamp: string;
  action: string;
  category: string;
  user: string;
  status: string;
  details?: Record<string, any>;
}

export interface PlatformSettings {
  project_name: string;
  version: string;
  active_model: string;
  risk_thresholds: {
    low_max: number;
    medium_max: number;
    high_min: number;
  };
  storage: Record<string, any>;
  theme: Record<string, any>;
}
