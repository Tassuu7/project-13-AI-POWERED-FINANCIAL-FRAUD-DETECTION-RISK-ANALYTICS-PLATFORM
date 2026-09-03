export type UserRole = 'Analyst' | 'Reviewer' | 'Administrator';

export type ModelType =
  | 'Logistic Regression'
  | 'Decision Tree'
  | 'Random Forest'
  | 'Gradient Boosting'
  | 'Isolation Forest';

export interface UserSession {
  username: string;
  role: UserRole;
  authenticated: boolean;
  permissions: string[];
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
  valid: boolean;
  total_records: number;
  total_checks: number;
  passed_checks: number;
  failed_checks: number;
  checks: ValidationCheck[];
  recommended_actions: string[];
}

export interface PreprocessingResult {
  original_shape: number[];
  processed_shape: number[];
  train_shape: number[];
  test_shape: number[];
  missing_values_handled: number;
  duplicates_removed: number;
  encoded_columns: string[];
  scaled_columns: string[];
  summary_notes: string[];
}

export interface FeatureSummary {
  feature_name: string;
  feature_type: string;
  description: string;
  importance_rank: number;
}

export interface FeatureResponse {
  original_feature_count: number;
  new_feature_count: number;
  created_features: FeatureSummary[];
  sample_preview: Record<string, any>[];
}

export interface ModelMetrics {
  model_name: string;
  accuracy: number;
  precision: number;
  recall: number;
  f1_score: number;
  roc_auc: number | null;
  training_time_seconds: number;
  confusion_matrix: number[][];
  is_best: boolean;
  notes: string;
}

export interface ModelComparisonResponse {
  trained_timestamp: string;
  dataset_name: string;
  total_train_samples: number;
  total_test_samples: number;
  best_model_name: string;
  models: ModelMetrics[];
}

export interface RiskFactor {
  factor: string;
  impact: 'HIGH' | 'MEDIUM' | 'LOW';
  description: string;
}

export interface PredictionResult {
  transaction_id: string;
  customer_id: string;
  amount: number;
  prediction_label: string;
  is_suspicious: boolean;
  risk_score: number;
  risk_level: 'LOW' | 'MEDIUM' | 'HIGH';
  confidence_probability: number;
  contributing_factors: RiskFactor[];
  recommended_action: string;
  model_used: string;
}

export interface TransactionRecord {
  transaction_id: string;
  customer_id: string;
  amount: number;
  timestamp: string;
  transaction_type: string;
  merchant_category: string;
  location: string;
  device_type: string;
  risk_score?: number;
  risk_level?: string;
  is_fraud?: number;
  [key: string]: any;
}

export type ReviewStatus = 'New' | 'Under Review' | 'Investigating' | 'Cleared' | 'Confirmed Suspicious';

export interface SuspiciousItem {
  transaction_id: string;
  customer_id: string;
  amount: number;
  timestamp: string;
  location: string;
  device_type: string;
  risk_score: number;
  risk_level: string;
  review_status: ReviewStatus;
  review_notes?: string;
  assigned_analyst?: string;
  last_updated?: string;
  flags: string[];
}

export interface AuditLogItem {
  id: string;
  timestamp: string;
  action: string;
  category: string;
  user: string;
  details: Record<string, any>;
  status: string;
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
  storage: {
    data_dir: string;
    models_dir: string;
    reports_dir: string;
    exports_dir: string;
    database_connected: boolean;
    persistence_mode: string;
  };
  theme: {
    palette: string;
    accent: string;
    avoid_blue: boolean;
  };
}
