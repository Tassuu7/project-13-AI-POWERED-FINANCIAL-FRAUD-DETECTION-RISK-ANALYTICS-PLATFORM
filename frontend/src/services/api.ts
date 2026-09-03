import {
  UserSession,
  UserRole,
  DatasetInfo,
  DatasetPreview,
  ValidationReport,
  PreprocessingResult,
  FeatureResponse,
  ModelComparisonResponse,
  PredictionResult,
  SuspiciousItem,
  AuditLogItem,
  PlatformSettings,
  ReviewStatus
} from '../types';

const API_BASE = (typeof window !== 'undefined' && window.location.port === '5173') ? '/api' : 'http://localhost:8000/api';

function getAuthHeaders(): Record<string, string> {
  const headers: Record<string, string> = {};
  if (typeof window !== 'undefined') {
    const stored = localStorage.getItem('aegis_session');
    if (stored) {
      try {
        const sess = JSON.parse(stored);
        if (sess.role) headers['X-User-Role'] = sess.role;
        if (sess.username) headers['X-User-Name'] = sess.username;
        if (sess.token) headers['Authorization'] = `Bearer ${sess.token}`;
      } catch {}
    }
  }
  return headers;
}

async function handleResponse<T>(res: Response): Promise<T> {
  if (!res.ok) {
    const errorText = await res.text();
    let detail = errorText;
    try {
      const errJson = JSON.parse(errorText);
      detail = errJson.detail || errJson.message || errorText;
    } catch {
      // Keep plain text
    }
    throw new Error(detail);
  }
  return res.json();
}

export const api = {
  // Auth & Session
  async login(username: string, password: string, role: UserRole): Promise<UserSession> {
    const res = await fetch(`${API_BASE}/auth/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, password, role }),
    });
    const session = await handleResponse<UserSession>(res);
    localStorage.setItem('aegis_session', JSON.stringify(session));
    return session;
  },

  async getSession(): Promise<UserSession> {
    const res = await fetch(`${API_BASE}/auth/session`, {
      headers: getAuthHeaders()
    });
    return handleResponse<UserSession>(res);
  },

  async getDemoAccounts(): Promise<any[]> {
    const res = await fetch(`${API_BASE}/auth/demo-accounts`);
    return handleResponse<any[]>(res);
  },

  async getDashboardTelemetry(datasetName: string = 'sample_synthetic_transactions.csv'): Promise<any> {
    const res = await fetch(`${API_BASE}/auth/dashboard-telemetry?dataset_name=${encodeURIComponent(datasetName)}`, {
      headers: getAuthHeaders()
    });
    return handleResponse<any>(res);
  },

  // Datasets
  async listDatasets(): Promise<DatasetInfo[]> {
    const res = await fetch(`${API_BASE}/datasets`, {
      headers: getAuthHeaders()
    });
    return handleResponse<DatasetInfo[]>(res);
  },

  async uploadDataset(file: File): Promise<any> {
    const formData = new FormData();
    formData.append('file', file);
    const res = await fetch(`${API_BASE}/datasets/upload`, {
      method: 'POST',
      headers: getAuthHeaders(),
      body: formData,
    });
    return handleResponse<any>(res);
  },

  async generateSynthetic(params: {
    num_records: number;
    fraud_percentage: number;
    num_customers: number;
    random_seed: number;
  }): Promise<any> {
    const res = await fetch(`${API_BASE}/datasets/generate`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', ...getAuthHeaders() },
      body: JSON.stringify(params),
    });
    return handleResponse<any>(res);
  },

  async previewDataset(name: string, limit: number = 25): Promise<DatasetPreview> {
    const res = await fetch(`${API_BASE}/datasets/${encodeURIComponent(name)}/preview?limit=${limit}`, {
      headers: getAuthHeaders()
    });
    return handleResponse<DatasetPreview>(res);
  },

  // Validation
  async validateDataset(name: string): Promise<ValidationReport> {
    const res = await fetch(`${API_BASE}/validation/${encodeURIComponent(name)}`, {
      headers: getAuthHeaders()
    });
    return handleResponse<ValidationReport>(res);
  },

  // Preprocessing
  async preprocessDataset(name: string, scalerType: string = 'standard', testSize: number = 0.2): Promise<PreprocessingResult> {
    const res = await fetch(`${API_BASE}/preprocessing/run`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', ...getAuthHeaders() },
      body: JSON.stringify({
        dataset_name: name,
        impute_strategy: 'median',
        handle_duplicates: true,
        encode_categorical: true,
        scaler_type: scalerType,
        test_size: testSize,
        random_state: 42,
      }),
    });
    return handleResponse<PreprocessingResult>(res);
  },

  // Features
  async engineerFeatures(name: string): Promise<FeatureResponse> {
    const res = await fetch(`${API_BASE}/features/generate`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', ...getAuthHeaders() },
      body: JSON.stringify({ dataset_name: name, include_domain_features: true }),
    });
    return handleResponse<FeatureResponse>(res);
  },

  // EDA
  async getEdaSummary(name: string): Promise<any> {
    const res = await fetch(`${API_BASE}/eda/${encodeURIComponent(name)}`, {
      headers: getAuthHeaders()
    });
    return handleResponse<any>(res);
  },

  // Models
  async trainModels(name: string, models: string[]): Promise<ModelComparisonResponse> {
    const res = await fetch(`${API_BASE}/models/train`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', ...getAuthHeaders() },
      body: JSON.stringify({
        dataset_name: name,
        models_to_train: models,
        comparison_metric: 'f1_score',
        save_artifacts: true,
      }),
    });
    return handleResponse<ModelComparisonResponse>(res);
  },

  async listTrainedModels(): Promise<any[]> {
    const res = await fetch(`${API_BASE}/models`, {
      headers: getAuthHeaders()
    });
    return handleResponse<any[]>(res);
  },

  async selectActiveModel(name: string): Promise<any> {
    const res = await fetch(`${API_BASE}/models/${encodeURIComponent(name)}/select`, {
      method: 'POST',
      headers: getAuthHeaders()
    });
    return handleResponse<any>(res);
  },

  // Predictions & Risk Scoring
  async predictSingle(data: Record<string, any>): Promise<PredictionResult> {
    const res = await fetch(`${API_BASE}/predictions/single`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', ...getAuthHeaders() },
      body: JSON.stringify({ transaction_data: data }),
    });
    return handleResponse<PredictionResult>(res);
  },

  async scoreRisk(data: Record<string, any>): Promise<any> {
    const res = await fetch(`${API_BASE}/risk/score`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', ...getAuthHeaders() },
      body: JSON.stringify(data),
    });
    return handleResponse<any>(res);
  },

  async predictBatch(datasetName: string): Promise<any> {
    const res = await fetch(`${API_BASE}/predictions/batch`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', ...getAuthHeaders() },
      body: JSON.stringify({ dataset_name: datasetName }),
    });
    return handleResponse<any>(res);
  },

  // Transactions Explorer
  async queryTransactions(params: Record<string, any>): Promise<any> {
    const query = new URLSearchParams();
    Object.entries(params).forEach(([k, v]) => {
      if (v !== undefined && v !== null && v !== '') {
        query.append(k, String(v));
      }
    });
    const res = await fetch(`${API_BASE}/transactions/search?${query.toString()}`, {
      headers: getAuthHeaders()
    });
    return handleResponse<any>(res);
  },

  // Suspicious Desk
  async listSuspicious(statusFilter?: string): Promise<SuspiciousItem[]> {
    const url = statusFilter && statusFilter !== 'All'
      ? `${API_BASE}/suspicious?status=${encodeURIComponent(statusFilter)}`
      : `${API_BASE}/suspicious`;
    const res = await fetch(url, {
      headers: getAuthHeaders()
    });
    return handleResponse<SuspiciousItem[]>(res);
  },

  async updateReview(txId: string, payload: { review_status: ReviewStatus; review_notes: string; analyst_name: string }): Promise<SuspiciousItem> {
    const res = await fetch(`${API_BASE}/suspicious/${encodeURIComponent(txId)}/review`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json', ...getAuthHeaders() },
      body: JSON.stringify(payload),
    });
    return handleResponse<SuspiciousItem>(res);
  },

  // Explainability
  async getGlobalImportance(modelName?: string): Promise<any[]> {
    const url = modelName ? `${API_BASE}/explainability/global?model_name=${encodeURIComponent(modelName)}` : `${API_BASE}/explainability/global`;
    const res = await fetch(url, {
      headers: getAuthHeaders()
    });
    return handleResponse<any[]>(res);
  },

  async explainLocal(transactionData: Record<string, any>): Promise<any[]> {
    const res = await fetch(`${API_BASE}/explainability/local`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', ...getAuthHeaders() },
      body: JSON.stringify({ transaction_data: transactionData }),
    });
    return handleResponse<any[]>(res);
  },

  // Reports
  async generateReport(type: string, format: string = 'html'): Promise<any> {
    const res = await fetch(`${API_BASE}/reports/generate`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', ...getAuthHeaders() },
      body: JSON.stringify({ report_type: type, format }),
    });
    return handleResponse<any>(res);
  },

  async listReports(): Promise<any[]> {
    const res = await fetch(`${API_BASE}/reports`, {
      headers: getAuthHeaders()
    });
    return handleResponse<any[]>(res);
  },

  // Exports
  async exportSuspicious(): Promise<any> {
    const res = await fetch(`${API_BASE}/exports/suspicious`, {
      method: 'POST',
      headers: getAuthHeaders()
    });
    return handleResponse<any>(res);
  },

  async exportMetrics(): Promise<any> {
    const res = await fetch(`${API_BASE}/exports/metrics`, {
      method: 'POST',
      headers: getAuthHeaders()
    });
    return handleResponse<any>(res);
  },

  async listExportFiles(): Promise<any[]> {
    const res = await fetch(`${API_BASE}/exports/files`, {
      headers: getAuthHeaders()
    });
    return handleResponse<any[]>(res);
  },

  // Processing History
  async getHistory(category?: string): Promise<AuditLogItem[]> {
    const url = category && category !== 'ALL'
      ? `${API_BASE}/history?category=${encodeURIComponent(category)}`
      : `${API_BASE}/history`;
    const res = await fetch(url, {
      headers: getAuthHeaders()
    });
    return handleResponse<AuditLogItem[]>(res);
  },

  // Settings
  async getSettings(): Promise<PlatformSettings> {
    const res = await fetch(`${API_BASE}/settings`, {
      headers: getAuthHeaders()
    });
    return handleResponse<PlatformSettings>(res);
  },

  async updateRiskThresholds(lowMax: number, medMax: number): Promise<any> {
    const res = await fetch(`${API_BASE}/settings/thresholds`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', ...getAuthHeaders() },
      body: JSON.stringify({ low_max: lowMax, medium_max: medMax }),
    });
    return handleResponse<any>(res);
  },
};
