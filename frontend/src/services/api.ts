import {
  UserSession,
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

const API_BASE = 'http://localhost:8000/api';

async function handleResponse<T>(res: Response): Promise<T> {
  if (!res.ok) {
    const errorText = await res.text();
    let detail = errorText;
    try {
      const errJson = JSON.parse(errorText);
      detail = errJson.detail || errJson.message || errorText;
    } catch {
      // Keep plain error text
    }
    throw new Error(detail);
  }
  return res.json();
}

export const api = {
  // Auth
  async login(username: string, role: string): Promise<UserSession> {
    const res = await fetch(`${API_BASE}/auth/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, role, demo_mode: true }),
    });
    return handleResponse<UserSession>(res);
  },

  async getSession(): Promise<UserSession> {
    const res = await fetch(`${API_BASE}/auth/session`);
    return handleResponse<UserSession>(res);
  },

  // Datasets
  async listDatasets(): Promise<DatasetInfo[]> {
    const res = await fetch(`${API_BASE}/datasets`);
    return handleResponse<DatasetInfo[]>(res);
  },

  async previewDataset(filename: string, rows: number = 15): Promise<DatasetPreview> {
    const res = await fetch(`${API_BASE}/datasets/${filename}/preview?rows=${rows}`);
    return handleResponse<DatasetPreview>(res);
  },

  async uploadDataset(file: File): Promise<any> {
    const formData = new FormData();
    formData.append('file', file);
    const res = await fetch(`${API_BASE}/datasets/upload`, {
      method: 'POST',
      body: formData,
    });
    return handleResponse<any>(res);
  },

  async generateSynthetic(params: {
    num_records: number;
    num_customers: number;
    fraud_percentage: number;
    random_seed: number;
  }): Promise<any> {
    const res = await fetch(`${API_BASE}/datasets/generate`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(params),
    });
    return handleResponse<any>(res);
  },

  // Validation
  async validateDataset(filename: string): Promise<ValidationReport> {
    const res = await fetch(`${API_BASE}/validation/${filename}`);
    return handleResponse<ValidationReport>(res);
  },

  // Preprocessing
  async runPreprocessing(params: {
    filename: string;
    handle_missing: string;
    handle_duplicates: boolean;
    scaling_method: string;
    test_size: number;
  }): Promise<PreprocessingResult> {
    const res = await fetch(`${API_BASE}/preprocessing/run`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(params),
    });
    return handleResponse<PreprocessingResult>(res);
  },

  // Feature Engineering
  async generateFeatures(filename: string): Promise<FeatureResponse> {
    const res = await fetch(`${API_BASE}/features/${filename}/generate`, {
      method: 'POST',
    });
    return handleResponse<FeatureResponse>(res);
  },

  // EDA
  async getEdaSummary(filename: string): Promise<any> {
    const res = await fetch(`${API_BASE}/eda/${filename}/summary`);
    return handleResponse<any>(res);
  },

  // Models
  async trainModels(params: {
    dataset_name: string;
    models_to_train: string[];
    handle_imbalance: boolean;
    test_size: number;
  }): Promise<ModelComparisonResponse> {
    const res = await fetch(`${API_BASE}/models/train`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(params),
    });
    return handleResponse<ModelComparisonResponse>(res);
  },

  async listTrainedModels(): Promise<any[]> {
    const res = await fetch(`${API_BASE}/models`);
    return handleResponse<any[]>(res);
  },

  async selectActiveModel(modelName: string): Promise<any> {
    const res = await fetch(`${API_BASE}/models/${modelName}/select`, {
      method: 'POST',
    });
    return handleResponse<any>(res);
  },

  // Predictions
  async predictSingle(payload: any, modelName?: string): Promise<PredictionResult> {
    const url = modelName ? `${API_BASE}/predictions/single?model_name=${encodeURIComponent(modelName)}` : `${API_BASE}/predictions/single`;
    const res = await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    });
    return handleResponse<PredictionResult>(res);
  },

  async predictBatch(filename: string, modelName?: string): Promise<any> {
    const res = await fetch(`${API_BASE}/predictions/batch`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ filename, model_name: modelName }),
    });
    return handleResponse<any>(res);
  },

  // Risk Engine
  async getRiskThresholds(): Promise<any> {
    const res = await fetch(`${API_BASE}/risk/thresholds`);
    return handleResponse<any>(res);
  },

  // Transactions
  async queryTransactions(params: Record<string, any>): Promise<any> {
    const query = new URLSearchParams();
    Object.entries(params).forEach(([key, val]) => {
      if (val !== undefined && val !== null && val !== '') {
        query.append(key, String(val));
      }
    });
    const res = await fetch(`${API_BASE}/transactions?${query.toString()}`);
    return handleResponse<any>(res);
  },

  // Suspicious Desk
  async listSuspicious(status?: string): Promise<SuspiciousItem[]> {
    const url = status && status !== 'All' ? `${API_BASE}/suspicious?status=${status}` : `${API_BASE}/suspicious`;
    const res = await fetch(url);
    return handleResponse<SuspiciousItem[]>(res);
  },

  async updateReview(txId: string, payload: { review_status: ReviewStatus; review_notes: string; analyst_name: string }): Promise<SuspiciousItem> {
    const res = await fetch(`${API_BASE}/suspicious/${txId}/review`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    });
    return handleResponse<SuspiciousItem>(res);
  },

  // Explainability
  async getGlobalImportance(modelName?: string): Promise<any[]> {
    const url = modelName ? `${API_BASE}/explainability/global?model_name=${encodeURIComponent(modelName)}` : `${API_BASE}/explainability/global`;
    const res = await fetch(url);
    return handleResponse<any[]>(res);
  },

  async explainLocal(tx: any): Promise<any[]> {
    const res = await fetch(`${API_BASE}/explainability/local`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(tx),
    });
    return handleResponse<any[]>(res);
  },

  // Reports
  async generateReport(reportType: string, format: string = 'html'): Promise<any> {
    const res = await fetch(`${API_BASE}/reports/generate`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ report_type: reportType, format }),
    });
    return handleResponse<any>(res);
  },

  async listReports(): Promise<any[]> {
    const res = await fetch(`${API_BASE}/reports`);
    return handleResponse<any[]>(res);
  },

  // Exports
  async exportSuspicious(): Promise<any> {
    const res = await fetch(`${API_BASE}/exports/suspicious`, { method: 'POST' });
    return handleResponse<any>(res);
  },

  async exportMetrics(): Promise<any> {
    const res = await fetch(`${API_BASE}/exports/model_metrics`, { method: 'POST' });
    return handleResponse<any>(res);
  },

  async listExportFiles(): Promise<any[]> {
    const res = await fetch(`${API_BASE}/exports/files`);
    return handleResponse<any[]>(res);
  },

  // History
  async getHistory(category?: string): Promise<AuditLogItem[]> {
    const url = category && category !== 'ALL' ? `${API_BASE}/history?category=${category}` : `${API_BASE}/history`;
    const res = await fetch(url);
    return handleResponse<AuditLogItem[]>(res);
  },

  // Settings
  async getSettings(): Promise<PlatformSettings> {
    const res = await fetch(`${API_BASE}/settings`);
    return handleResponse<PlatformSettings>(res);
  },

  async updateRiskThresholds(low_max: number, medium_max: number): Promise<any> {
    const res = await fetch(`${API_BASE}/settings/thresholds`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ low_max, medium_max }),
    });
    return handleResponse<any>(res);
  }
};
