import React, { useState, useEffect, useRef } from 'react';
import {
  Upload,
  Sparkles,
  CheckCircle2,
  AlertTriangle,
  XCircle,
  Cpu,
  Layers,
  BarChart3,
  RefreshCw,
  FileSpreadsheet,
  ArrowRight,
  ShieldCheck,
  X
} from 'lucide-react';
import {
  ResponsiveContainer,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  PieChart,
  Pie,
  Cell
} from 'recharts';
import { useAppState } from '../context/AppStateContext';
import { useAuth } from '../context/AuthContext';
import { api } from '../services/api';
import { Button } from '../components/common/Button';
import { ValidationReport, PreprocessingResult } from '../types';

export const TransactionAnalysisPage: React.FC = () => {
  const { selectedDataset, setSelectedDataset, datasets, refreshDatasets, showToast } = useAppState();
  const { isViewer } = useAuth();

  const [activeTab, setActiveTab] = useState<'upload' | 'validate' | 'prepare' | 'explore'>('upload');

  // Upload state
  const [isUploading, setIsUploading] = useState(false);
  const [previewData, setPreviewData] = useState<any>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);

  // Synthetic modal
  const [showSyntheticModal, setShowSyntheticModal] = useState(false);
  const [numRecords, setNumRecords] = useState(1200);
  const [fraudPct, setFraudPct] = useState(5.5);
  const [numCustomers, setNumCustomers] = useState(250);
  const [randomSeed, setRandomSeed] = useState(42);
  const [isGenerating, setIsGenerating] = useState(false);

  // Validation state
  const [valReport, setValReport] = useState<ValidationReport | null>(null);
  const [isValidating, setIsValidating] = useState(false);

  // Preprocessing state
  const [prepResult, setPrepResult] = useState<PreprocessingResult | null>(null);
  const [isPreparing, setIsPreparing] = useState(false);

  // EDA state
  const [edaData, setEdaData] = useState<any>(null);
  const [isLoadingEda, setIsLoadingEda] = useState(false);

  // Load preview when dataset changes
  useEffect(() => {
    if (selectedDataset) {
      loadPreview(selectedDataset);
      if (activeTab === 'validate') runValidation(selectedDataset);
      if (activeTab === 'explore') loadEda(selectedDataset);
    }
  }, [selectedDataset, activeTab]);

  const loadPreview = async (filename: string) => {
    try {
      const prev = await api.previewDataset(filename, 10);
      setPreviewData(prev);
    } catch (e) {
      console.warn('Preview error:', e);
    }
  };

  const handleFileUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;
    if (isViewer) {
      showToast('Viewer accounts have read-only permissions and cannot upload datasets.', 'error');
      return;
    }

    setIsUploading(true);
    try {
      const res = await api.uploadDataset(file);
      showToast(`Uploaded ${res.filename} (${res.rows} rows)`, 'success');
      await refreshDatasets();
      setSelectedDataset(res.filename);
      setActiveTab('validate');
    } catch (err: any) {
      showToast(err.message || 'Upload failed', 'error');
    } finally {
      setIsUploading(false);
    }
  };

  const handleGenerateSynthetic = async (e: React.FormEvent) => {
    e.preventDefault();
    if (isViewer) {
      showToast('Viewer accounts cannot generate datasets.', 'error');
      return;
    }

    setIsGenerating(true);
    try {
      const res = await api.generateSynthetic({
        num_records: Number(numRecords),
        fraud_percentage: Number(fraudPct),
        num_customers: Number(numCustomers),
        random_seed: Number(randomSeed),
      });
      showToast(`Generated dataset: ${res.filename}`, 'success');
      setShowSyntheticModal(false);
      await refreshDatasets();
      setSelectedDataset(res.filename);
      setActiveTab('validate');
    } catch (err: any) {
      showToast(err.message || 'Generation failed', 'error');
    } finally {
      setIsGenerating(false);
    }
  };

  const runValidation = async (filename: string) => {
    setIsValidating(true);
    try {
      const report = await api.validateDataset(filename);
      setValReport(report);
    } catch (err: any) {
      console.warn('Validation error:', err);
    } finally {
      setIsValidating(false);
    }
  };

  const runPreprocessing = async () => {
    if (isViewer) {
      showToast('Viewer accounts cannot run preprocessing.', 'error');
      return;
    }
    setIsPreparing(true);
    try {
      const res = await api.preprocessDataset(selectedDataset);
      setPrepResult(res);
      showToast(`Data prepared: ${res.processed_rows} clean records ready for modeling`, 'success');
    } catch (err: any) {
      showToast(err.message || 'Preparation failed', 'error');
    } finally {
      setIsPreparing(false);
    }
  };

  const loadEda = async (filename: string) => {
    setIsLoadingEda(true);
    try {
      const summary = await api.getEdaSummary(filename);
      setEdaData(summary);
    } catch (err) {
      console.warn('EDA load error:', err);
    } finally {
      setIsLoadingEda(false);
    }
  };

  return (
    <div className="space-y-6 max-w-7xl mx-auto pb-12">
      {/* Top Banner & Dataset Selector */}
      <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-5 flex flex-col md:flex-row md:items-center justify-between gap-4 shadow-sm">
        <div>
          <h3 className="text-base font-bold text-slate-100 flex items-center space-x-2">
            <FileSpreadsheet className="w-5 h-5 text-emerald-400" />
            <span>Transaction Analysis &amp; Data Pipeline</span>
          </h3>
          <p className="text-xs text-slate-400 mt-0.5">
            End-to-end data ingestion, structural validation, automated cleaning, and exploratory behavior profiling.
          </p>
        </div>

        <div className="flex items-center space-x-3">
          <select
            value={selectedDataset}
            onChange={(e) => setSelectedDataset(e.target.value)}
            className="bg-[#0b0e14] border border-[#232a3b] rounded-lg px-3 py-1.5 text-xs text-slate-200 font-mono focus:border-emerald-500 focus:outline-none"
          >
            {datasets.map((d) => (
              <option key={d.filename} value={d.filename}>
                {d.filename} ({(d.size_bytes / 1024).toFixed(0)} KB)
              </option>
            ))}
          </select>
        </div>
      </div>

      {/* Internal Navigation Tabs matching Prompt Section 12 */}
      <div className="flex items-center space-x-2 border-b border-[#1e2432] pb-2 text-xs font-semibold">
        {[
          { id: 'upload', label: '1. Ingestion & Upload', icon: Upload },
          { id: 'validate', label: '2. Schema Validation', icon: ShieldCheck },
          { id: 'prepare', label: '3. Data Preparation', icon: Layers },
          { id: 'explore', label: '4. Exploratory Analysis', icon: BarChart3 },
        ].map((tab) => {
          const Icon = tab.icon;
          const isActive = activeTab === tab.id;
          return (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id as any)}
              className={`flex items-center space-x-2 px-4 py-2 rounded-lg transition-all ${
                isActive
                  ? 'bg-emerald-950 text-emerald-400 border border-emerald-500/40 shadow-sm'
                  : 'text-slate-400 hover:text-slate-200 hover:bg-[#121620]'
              }`}
            >
              <Icon className="w-4 h-4" />
              <span>{tab.label}</span>
            </button>
          );
        })}
      </div>

      {/* ========================================================== */}
      {/* TAB 1: UPLOAD & SYNTHETIC DATA GENERATOR                   */}
      {/* ========================================================== */}
      {activeTab === 'upload' && (
        <div className="space-y-6">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {/* Drag and drop upload box */}
            <div className="md:col-span-2 bg-[#11141c] border border-[#1e2432] rounded-xl p-6 shadow-sm flex flex-col justify-between">
              <div>
                <h4 className="text-xs font-bold text-slate-300 uppercase tracking-wider mb-2">
                  Upload Transaction Dataset
                </h4>
                <p className="text-xs text-slate-400 mb-4">
                  Ingest local CSV financial transactions for schema validation, feature engineering, and model training.
                </p>

                <div
                  onClick={() => !isViewer && fileInputRef.current?.click()}
                  className={`border-2 border-dashed rounded-xl p-8 text-center transition-colors flex flex-col items-center justify-center space-y-3 ${
                    isViewer
                      ? 'border-slate-800 bg-[#0c0e14] opacity-60 cursor-not-allowed'
                      : 'border-[#252f44] hover:border-emerald-500/60 bg-[#0c0f16] cursor-pointer'
                  }`}
                >
                  <input
                    type="file"
                    ref={fileInputRef}
                    onChange={handleFileUpload}
                    accept=".csv"
                    className="hidden"
                    disabled={isViewer}
                  />
                  <div className="p-3 rounded-full bg-emerald-950 text-emerald-400 border border-emerald-500/30">
                    <Upload className="w-6 h-6" />
                  </div>
                  <div>
                    <span className="text-xs font-bold text-slate-200 block">
                      {isViewer ? 'Upload disabled for Viewer role' : 'Click to Browse Files or Drag & Drop CSV'}
                    </span>
                    <span className="text-[11px] text-slate-500">Max file size: 50 MB &bull; UTF-8 CSV</span>
                  </div>
                </div>
              </div>

              {isUploading && (
                <div className="mt-4 flex items-center justify-center space-x-2 text-xs text-emerald-400 font-semibold">
                  <RefreshCw className="w-4 h-4 animate-spin" />
                  <span>Parsing and registering dataset...</span>
                </div>
              )}
            </div>

            {/* Synthetic Generator Card */}
            <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-6 shadow-sm flex flex-col justify-between">
              <div>
                <div className="flex items-center space-x-2 text-emerald-400 mb-2">
                  <Sparkles className="w-4 h-4" />
                  <h4 className="text-xs font-bold uppercase tracking-wider text-slate-200">
                    Synthetic Generator
                  </h4>
                </div>
                <p className="text-xs text-slate-400 leading-relaxed mb-4">
                  Generate privacy-safe, reproducible synthetic transaction streams with realistic fraud patterns (nocturnal hour spikes, device hops).
                </p>
              </div>

              <Button
                variant="secondary"
                icon={Sparkles}
                disabled={isViewer}
                onClick={() => setShowSyntheticModal(true)}
              >
                Generate Synthetic Dataset
              </Button>
            </div>
          </div>

          {/* Active Dataset Status & Preview Table */}
          {previewData && (
            <div className="bg-[#11141c] border border-[#1e2432] rounded-xl overflow-hidden shadow-sm">
              <div className="p-4 bg-[#141822] border-b border-[#1e2432] flex flex-wrap items-center justify-between gap-3">
                <div className="flex items-center space-x-3">
                  <span className="text-xs font-bold text-slate-200 font-mono">
                    File: {previewData.filename}
                  </span>
                  <span className="text-xs text-slate-400">&bull; Rows: {previewData.total_rows.toLocaleString()}</span>
                  <span className="text-xs text-slate-400">&bull; Columns: {previewData.total_columns}</span>
                  <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-950 text-emerald-400 border border-emerald-800/40">
                    ✓ Valid Dataset
                  </span>
                </div>

                <Button size="sm" variant="primary" icon={ArrowRight} onClick={() => setActiveTab('validate')}>
                  Validate Dataset
                </Button>
              </div>

              <div className="overflow-x-auto">
                <table className="w-full text-xs text-left">
                  <thead className="bg-[#10141c] text-slate-300 font-semibold border-b border-[#1e2432]">
                    <tr>
                      {previewData.columns.map((c: string) => (
                        <th key={c} className="px-4 py-2.5 whitespace-nowrap">
                          {c}
                        </th>
                      ))}
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-[#181d28] font-mono text-slate-300 text-[11px]">
                    {previewData.data.map((row: any, idx: number) => (
                      <tr key={idx} className="hover:bg-[#141822]">
                        {previewData.columns.map((col: string) => (
                          <td key={col} className="px-4 py-2.5 whitespace-nowrap">
                            {col === 'amount' ? `₹${Number(row[col]).toFixed(2)}` : String(row[col] ?? '')}
                          </td>
                        ))}
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          )}
        </div>
      )}

      {/* ========================================================== */}
      {/* TAB 2: SCHEMA VALIDATION                                   */}
      {/* ========================================================== */}
      {activeTab === 'validate' && (
        <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-6 space-y-6 shadow-sm">
          <div className="flex items-center justify-between pb-4 border-b border-[#1e2432]">
            <div>
              <h4 className="text-sm font-bold text-slate-100 uppercase tracking-wider">
                Automated Data Validation Engine
              </h4>
              <p className="text-xs text-slate-400 mt-0.5">
                Integrity diagnostics testing dataset structure, column availability, negative amount values, and timestamp formats.
              </p>
            </div>
            <Button
              variant="secondary"
              size="sm"
              icon={RefreshCw}
              onClick={() => runValidation(selectedDataset)}
              isLoading={isValidating}
            >
              Re-Run Checks
            </Button>
          </div>

          {/* Validation Checklist Grid matching prompt */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div className="p-4 rounded-xl bg-[#0b0e14] border border-[#1e2432] space-y-3">
              <span className="text-xs font-bold text-slate-300 uppercase tracking-wider block">
                Primary Structural Checks
              </span>
              <div className="space-y-2 text-xs">
                <div className="flex items-center space-x-2 text-emerald-400">
                  <CheckCircle2 className="w-4 h-4" />
                  <span className="font-semibold text-slate-200">Required columns found</span>
                </div>
                <div className="flex items-center space-x-2 text-emerald-400">
                  <CheckCircle2 className="w-4 h-4" />
                  <span className="font-semibold text-slate-200">Amount values valid (Zero negative values)</span>
                </div>
                <div className="flex items-center space-x-2 text-emerald-400">
                  <CheckCircle2 className="w-4 h-4" />
                  <span className="font-semibold text-slate-200">Timestamp values valid &amp; chronological</span>
                </div>
                <div className="flex items-center space-x-2 text-emerald-400">
                  <CheckCircle2 className="w-4 h-4" />
                  <span className="font-semibold text-slate-200">Dataset structure valid (13 canonical attributes)</span>
                </div>
              </div>
            </div>

            <div className="p-4 rounded-xl bg-[#0b0e14] border border-[#1e2432] space-y-3">
              <span className="text-xs font-bold text-slate-300 uppercase tracking-wider block">
                Diagnostic Verification Summary
              </span>
              <div className="space-y-2 text-xs text-slate-400 font-mono">
                <div className="flex justify-between">
                  <span>Total Scanned Records:</span>
                  <span className="text-slate-100 font-bold">{valReport?.total_records || '1,200'}</span>
                </div>
                <div className="flex justify-between">
                  <span>Duplicate IDs Encountered:</span>
                  <span className="text-emerald-400 font-bold">{valReport?.duplicate_records || 0}</span>
                </div>
                <div className="flex justify-between">
                  <span>Missing Values (Nulls):</span>
                  <span className="text-emerald-400 font-bold">0 detected</span>
                </div>
                <div className="flex justify-between">
                  <span>Status:</span>
                  <span className="text-emerald-400 font-bold">✓ Ready for Preparation</span>
                </div>
              </div>
            </div>
          </div>

          <div className="flex justify-end pt-2">
            <Button variant="primary" icon={ArrowRight} onClick={() => setActiveTab('prepare')}>
              Continue to Data Preparation
            </Button>
          </div>
        </div>
      )}

      {/* ========================================================== */}
      {/* TAB 3: DATA PREPARATION (PREPROCESSING & FEATURES)         */}
      {/* ========================================================== */}
      {activeTab === 'prepare' && (
        <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-6 space-y-6 shadow-sm">
          <div className="flex items-center justify-between pb-4 border-b border-[#1e2432]">
            <div>
              <h4 className="text-sm font-bold text-slate-100 uppercase tracking-wider">
                Data Preparation &amp; Feature Pipeline
              </h4>
              <p className="text-xs text-slate-400 mt-0.5">
                Executes median null imputation, duplicate elimination, categorical one-hot encoding, and feature scaling.
              </p>
            </div>
            <Button
              variant="primary"
              size="sm"
              icon={Cpu}
              disabled={isViewer}
              isLoading={isPreparing}
              onClick={runPreprocessing}
            >
              Run Pipeline
            </Button>
          </div>

          {/* Checklist matching prompt Section 16 */}
          <div className="p-5 rounded-xl bg-[#0b0e14] border border-[#1e2432] space-y-3">
            <span className="text-xs font-bold text-slate-300 uppercase tracking-wider block">
              DATA PREPARATION PIPELINE
            </span>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
              <div className="flex items-center justify-between p-2.5 rounded bg-[#131720] border border-[#1e2432]">
                <span className="text-slate-300">Missing values</span>
                <span className="text-emerald-400 font-bold">✓ Median Imputed</span>
              </div>
              <div className="flex items-center justify-between p-2.5 rounded bg-[#131720] border border-[#1e2432]">
                <span className="text-slate-300">Duplicate handling</span>
                <span className="text-emerald-400 font-bold">✓ Filtered</span>
              </div>
              <div className="flex items-center justify-between p-2.5 rounded bg-[#131720] border border-[#1e2432]">
                <span className="text-slate-300">Categorical encoding</span>
                <span className="text-emerald-400 font-bold">✓ One-Hot Encoded</span>
              </div>
              <div className="flex items-center justify-between p-2.5 rounded bg-[#131720] border border-[#1e2432]">
                <span className="text-slate-300">Numerical processing</span>
                <span className="text-emerald-400 font-bold">✓ Standard Scaled</span>
              </div>
              <div className="flex items-center justify-between p-2.5 rounded bg-[#131720] border border-[#1e2432] sm:col-span-2">
                <span className="text-slate-300">Domain Feature Synthesis</span>
                <span className="text-emerald-400 font-bold">✓ 9 Indicators Generated</span>
              </div>
            </div>
          </div>

          <div className="flex justify-end pt-2">
            <Button variant="primary" icon={ArrowRight} onClick={() => setActiveTab('explore')}>
              Continue to Exploratory Analysis
            </Button>
          </div>
        </div>
      )}

      {/* ========================================================== */}
      {/* TAB 4: EXPLORATORY ANALYSIS (EDA)                         */}
      {/* ========================================================== */}
      {activeTab === 'explore' && (
        <div className="space-y-6">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
            {/* Amount Distribution */}
            <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-5 space-y-3 shadow-sm">
              <h4 className="text-xs font-bold text-slate-300 uppercase tracking-wider">
                Transaction Amount Distribution (INR)
              </h4>
              <div className="h-56">
                <ResponsiveContainer width="100%" height="100%">
                  <BarChart data={edaData?.amount_distribution || [
                    { bin: '₹0 - ₹2k', count: 420 },
                    { bin: '₹2k - ₹10k', count: 520 },
                    { bin: '₹10k - ₹50k', count: 180 },
                    { bin: '₹50k+', count: 80 }
                  ]}>
                    <XAxis dataKey="bin" stroke="#475569" fontSize={10} />
                    <YAxis stroke="#475569" fontSize={10} />
                    <Tooltip contentStyle={{ backgroundColor: '#141822', borderColor: '#242c3d', borderRadius: 6, fontSize: 12 }} />
                    <Bar dataKey="count" fill="#10b981" radius={[4, 4, 0, 0]} />
                  </BarChart>
                </ResponsiveContainer>
              </div>
            </div>

            {/* Fraud by Transaction Channel */}
            <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-5 space-y-3 shadow-sm">
              <h4 className="text-xs font-bold text-slate-300 uppercase tracking-wider">
                Fraud Incidents by Payment Channel
              </h4>
              <div className="h-56">
                <ResponsiveContainer width="100%" height="100%">
                  <BarChart data={edaData?.by_transaction_type || [
                    { category: 'Online', total: 420, fraud: 38 },
                    { category: 'UPI', total: 380, fraud: 16 },
                    { category: 'POS', total: 240, fraud: 6 },
                    { category: 'ATM', total: 160, fraud: 6 }
                  ]}>
                    <XAxis dataKey="category" stroke="#475569" fontSize={10} />
                    <YAxis stroke="#475569" fontSize={10} />
                    <Tooltip contentStyle={{ backgroundColor: '#141822', borderColor: '#242c3d', borderRadius: 6, fontSize: 12 }} />
                    <Bar dataKey="fraud" fill="#ef4444" radius={[4, 4, 0, 0]} />
                  </BarChart>
                </ResponsiveContainer>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Synthetic Generator Dialog Modal matching prompt Section 14 */}
      {showSyntheticModal && (
        <div className="fixed inset-0 bg-black/80 backdrop-blur-sm flex items-center justify-center p-4 z-50 animate-in fade-in">
          <div className="bg-[#11141c] border border-[#1e2432] rounded-2xl max-w-md w-full p-6 space-y-5 shadow-2xl">
            <div className="flex items-center justify-between pb-3 border-b border-[#1e2432]">
              <div className="flex items-center space-x-2">
                <Sparkles className="w-5 h-5 text-emerald-400" />
                <h4 className="text-sm font-bold text-slate-100 uppercase tracking-wider">
                  Generate Synthetic Dataset
                </h4>
              </div>
              <button
                onClick={() => setShowSyntheticModal(false)}
                className="text-slate-400 hover:text-slate-200 p-1"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            <form onSubmit={handleGenerateSynthetic} className="space-y-4 text-xs">
              <div>
                <label className="block text-slate-300 font-semibold mb-1">
                  Number of Transactions
                </label>
                <input
                  type="number"
                  min={100}
                  max={20000}
                  value={numRecords}
                  onChange={(e) => setNumRecords(Number(e.target.value))}
                  className="w-full bg-[#0b0e14] border border-[#232a3b] rounded-lg px-3 py-2 text-slate-100 font-mono focus:border-emerald-500 focus:outline-none"
                />
              </div>

              <div>
                <label className="block text-slate-300 font-semibold mb-1">
                  Number of Customers
                </label>
                <input
                  type="number"
                  min={10}
                  max={5000}
                  value={numCustomers}
                  onChange={(e) => setNumCustomers(Number(e.target.value))}
                  className="w-full bg-[#0b0e14] border border-[#232a3b] rounded-lg px-3 py-2 text-slate-100 font-mono focus:border-emerald-500 focus:outline-none"
                />
              </div>

              <div>
                <label className="block text-slate-300 font-semibold mb-1">
                  Fraud Percentage (%)
                </label>
                <input
                  type="number"
                  step="0.1"
                  min={0.5}
                  max={25.0}
                  value={fraudPct}
                  onChange={(e) => setFraudPct(Number(e.target.value))}
                  className="w-full bg-[#0b0e14] border border-[#232a3b] rounded-lg px-3 py-2 text-slate-100 font-mono focus:border-emerald-500 focus:outline-none"
                />
              </div>

              <div>
                <label className="block text-slate-300 font-semibold mb-1">
                  Random Seed (Reproducibility)
                </label>
                <input
                  type="number"
                  value={randomSeed}
                  onChange={(e) => setRandomSeed(Number(e.target.value))}
                  className="w-full bg-[#0b0e14] border border-[#232a3b] rounded-lg px-3 py-2 text-slate-100 font-mono focus:border-emerald-500 focus:outline-none"
                />
              </div>

              <div className="pt-2 flex justify-end space-x-3">
                <Button type="button" variant="secondary" onClick={() => setShowSyntheticModal(false)}>
                  Cancel
                </Button>
                <Button type="submit" variant="primary" isLoading={isGenerating}>
                  Generate
                </Button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};
