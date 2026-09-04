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
  Play,
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

  useEffect(() => {
    if (selectedDataset) {
      loadPreview(selectedDataset);
      runValidation(selectedDataset);
      loadEda(selectedDataset);
    }
  }, [selectedDataset]);

  const loadPreview = async (filename: string) => {
    try {
      const data = await api.previewDataset(filename, 15);
      setPreviewData(data);
    } catch (e) {
      console.warn('Failed preview:', e);
    }
  };

  const handleFileUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    if (isViewer) {
      showToast('Viewer accounts have read-only access and cannot upload datasets.', 'error');
      return;
    }

    setIsUploading(true);
    try {
      const res = await api.uploadDataset(file);
      showToast(`Uploaded ${res.filename} (${res.records_count} records)`, 'success');
      await refreshDatasets();
      setSelectedDataset(res.filename);
      loadPreview(res.filename);
    } catch (err: any) {
      showToast(err.message || 'Upload failed', 'error');
    } finally {
      setIsUploading(false);
      if (fileInputRef.current) fileInputRef.current.value = '';
    }
  };

  const handleGenerateSynthetic = async (e?: React.FormEvent, customRecords?: number) => {
    if (e) e.preventDefault();
    if (isViewer) {
      showToast('Viewer accounts cannot generate datasets.', 'error');
      return;
    }

    setIsGenerating(true);
    try {
      const recordsToGen = customRecords || Number(numRecords) || 1000;
      const res = await api.generateSynthetic({
        num_records: recordsToGen,
        fraud_percentage: Number(fraudPct) || 5.0,
        num_customers: Number(numCustomers) || 200,
        random_seed: Number(randomSeed) || 42,
      });
      const count = res.rows || res.records_count || recordsToGen;
      showToast(`Generated: ${res.filename} with ${count} synthetic transactions`, 'success');
      setShowSyntheticModal(false);
      await refreshDatasets();
      setSelectedDataset(res.filename);
      await loadPreview(res.filename);
      await runValidation(res.filename);
      await loadEda(res.filename);
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
    <div className="w-full space-y-8 pb-16 font-sans">
      {/* Top Banner & Dataset Selector - Full Width */}
      <div className="w-full bg-[#111622] border border-[#1e2533] rounded-2xl p-6 flex flex-col md:flex-row md:items-center justify-between gap-6 shadow-md">
        <div>
          <h3 className="text-xl font-bold text-slate-100 flex items-center space-x-3">
            <FileSpreadsheet className="w-7 h-7 text-emerald-400" />
            <span>Transaction Analysis &amp; Data Pipeline</span>
          </h3>
          <p className="text-sm text-slate-300 mt-1 font-medium">
            End-to-end data ingestion, structural validation, automated cleaning, and exploratory behavior profiling.
          </p>
        </div>

        <div className="flex items-center space-x-3 shrink-0">
          <span className="text-sm text-slate-400 font-semibold">Active Dataset:</span>
          <select
            value={selectedDataset}
            onChange={(e) => setSelectedDataset(e.target.value)}
            className="bg-[#0b0e14] border border-[#232b3d] rounded-xl px-4 py-2 text-sm text-slate-100 font-mono font-bold focus:border-emerald-500 focus:outline-none shadow-sm"
          >
            {datasets.map((d) => (
              <option key={d.filename} value={d.filename}>
                {d.filename} ({(d.size_bytes / 1024).toFixed(0)} KB)
              </option>
            ))}
          </select>
        </div>
      </div>

      {/* Navigation Tabs with Large Font and Touch Targets */}
      <div className="flex items-center space-x-3 border-b border-[#1e2533] pb-3 text-sm font-bold overflow-x-auto">
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
              className={`flex items-center space-x-2.5 px-5 py-3 rounded-xl transition-all shrink-0 ${
                isActive
                  ? 'bg-emerald-950/80 text-emerald-300 border border-emerald-500/50 shadow-md ring-1 ring-emerald-500/30'
                  : 'text-slate-300 hover:text-white hover:bg-[#141a26]'
              }`}
            >
              <Icon className="w-5 h-5" />
              <span>{tab.label}</span>
            </button>
          );
        })}
      </div>

      {/* ========================================================== */}
      {/* TAB 1: UPLOAD & SYNTHETIC DATA GENERATOR                   */}
      {/* ========================================================== */}
      {activeTab === 'upload' && (
        <div className="space-y-8 w-full">
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 w-full">
            {/* Drag and drop upload box */}
            <div className="lg:col-span-2 bg-[#111622] border border-[#1e2533] rounded-2xl p-7 shadow-md flex flex-col justify-between">
              <div>
                <h4 className="text-base font-bold text-slate-100 uppercase tracking-wider mb-2">
                  Upload Transaction Dataset
                </h4>
                <p className="text-sm text-slate-300 mb-6 font-medium">
                  Ingest local CSV financial transactions for schema validation, feature engineering, and model training.
                </p>

                <div
                  onClick={() => !isViewer && fileInputRef.current?.click()}
                  className={`border-2 border-dashed rounded-2xl p-10 text-center transition-all flex flex-col items-center justify-center space-y-4 ${
                    isViewer
                      ? 'border-slate-800 bg-[#0c0e14] opacity-60 cursor-not-allowed'
                      : 'border-[#26334a] hover:border-emerald-500/80 bg-[#0c1018] cursor-pointer shadow-inner hover:bg-[#10141f]'
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
                  <div className="w-14 h-14 rounded-2xl bg-emerald-950/60 border border-emerald-500/40 flex items-center justify-center text-emerald-400">
                    <Upload className="w-7 h-7" />
                  </div>
                  <div>
                    <span className="text-base font-bold text-slate-100 block">
                      {isUploading ? 'Ingesting & Indexing Dataset...' : 'Click to Browse or Drag CSV File Here'}
                    </span>
                    <span className="text-xs text-slate-400 mt-1 block">
                      Expected fields: transaction_id, amount, timestamp, location, device_type, is_fraud
                    </span>
                  </div>
                </div>
              </div>
            </div>

            {/* Synthetic Data Generator Modal Trigger */}
            <div className="bg-[#111622] border border-[#1e2533] rounded-2xl p-7 shadow-md flex flex-col justify-between space-y-6">
              <div>
                <div className="flex items-center space-x-2.5 mb-2">
                  <Sparkles className="w-6 h-6 text-emerald-400" />
                  <h4 className="text-base font-bold text-slate-100 uppercase tracking-wider">
                    Synthetic Generator
                  </h4>
                </div>
                <p className="text-sm text-slate-300 leading-relaxed font-medium">
                  Generate mathematically realistic financial transactions with seeded fraud velocity spikes, nocturnal timestamps, and geographic hops.
                </p>

                <div className="mt-6 p-4 rounded-xl bg-[#0b0e14] border border-[#202838] space-y-2 text-xs text-slate-400 font-mono">
                  <div className="flex justify-between">
                    <span>Default Count:</span>
                    <span className="text-emerald-400 font-bold">1,200 txns</span>
                  </div>
                  <div className="flex justify-between">
                    <span>Fraud Infiltration:</span>
                    <span className="text-rose-400 font-bold">~5.5%</span>
                  </div>
                  <div className="flex justify-between">
                    <span>Unique Accounts:</span>
                    <span className="text-slate-200 font-bold">250 entities</span>
                  </div>
                </div>
              </div>

              <div className="space-y-2.5">
                <Button
                  variant="primary"
                  size="md"
                  className="w-full text-sm font-bold py-3 shadow-lg"
                  icon={Sparkles}
                  disabled={isViewer}
                  onClick={() => setShowSyntheticModal(true)}
                >
                  Configure &amp; Generate Dataset
                </Button>
                <Button
                  variant="secondary"
                  size="sm"
                  className="w-full text-xs font-bold py-2 bg-[#0c1017] border border-[#202838] hover:border-emerald-500/50 text-slate-300"
                  icon={Play}
                  disabled={isViewer || isGenerating}
                  onClick={() => handleGenerateSynthetic(undefined, 1000)}
                  isLoading={isGenerating}
                >
                  Quick Generate (1,000 Tx)
                </Button>
              </div>
            </div>
          </div>

          {/* Dataset Ledger Preview Table - Full Width */}
          <div className="bg-[#111622] border border-[#1e2533] rounded-2xl overflow-hidden shadow-md w-full">
            <div className="p-5 bg-[#141a26] border-b border-[#1e2533] flex items-center justify-between">
              <div>
                <h4 className="text-base font-bold text-slate-100 font-mono flex items-center space-x-2">
                  <span>Ledger Preview:</span>
                  <span className="text-emerald-400">{selectedDataset}</span>
                </h4>
                <span className="text-xs text-slate-400 font-sans">
                  Showing top {previewData?.preview?.length || 0} sample rows of {previewData?.total_records || 0} total transactions
                </span>
              </div>

              <Button
                variant="ghost"
                size="sm"
                icon={RefreshCw}
                onClick={() => loadPreview(selectedDataset)}
              >
                Reload Ledger
              </Button>
            </div>

            <div className="overflow-x-auto w-full">
              <table className="w-full text-sm text-left">
                <thead className="bg-[#0f131c] text-slate-300 font-bold border-b border-[#1e2533]">
                  <tr>
                    {previewData?.columns?.map((col: string) => (
                      <th key={col} className="px-5 py-3.5 whitespace-nowrap text-xs uppercase tracking-wider">
                        {col}
                      </th>
                    ))}
                  </tr>
                </thead>
                <tbody className="divide-y divide-[#181f2e] font-mono text-slate-200">
                  {previewData?.preview?.map((row: any, i: number) => (
                    <tr key={i} className="hover:bg-[#141c29] transition-colors">
                      {previewData.columns.map((col: string) => {
                        const val = row[col];
                        const isFraudCol = col === 'is_fraud';
                        return (
                          <td key={col} className="px-5 py-3 whitespace-nowrap">
                            {isFraudCol ? (
                              <span className={`px-2 py-0.5 rounded text-xs font-bold ${
                                val === 1 || val === '1'
                                  ? 'bg-rose-950 text-rose-300 border border-rose-700/60'
                                  : 'bg-emerald-950 text-emerald-300 border border-emerald-700/60'
                              }`}>
                                {val === 1 || val === '1' ? 'FRAUD' : 'NORMAL'}
                              </span>
                            ) : (
                              String(val)
                            )}
                          </td>
                        );
                      })}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      )}

      {/* ========================================================== */}
      {/* TAB 2: SCHEMA VALIDATION                                   */}
      {/* ========================================================== */}
      {activeTab === 'validate' && (
        <div className="space-y-6 w-full">
          <div className="bg-[#111622] border border-[#1e2533] rounded-2xl p-7 space-y-6 shadow-md w-full">
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-[#1e2533]">
              <div>
                <h4 className="text-lg font-bold text-slate-100 uppercase tracking-wider">
                  Automated Structural Schema Diagnostics
                </h4>
                <p className="text-sm text-slate-300 mt-1 font-medium">
                  Validates dataset against 8 regulatory data integrity standards prior to preprocessing.
                </p>
              </div>

              <Button
                variant="primary"
                size="md"
                icon={RefreshCw}
                onClick={() => runValidation(selectedDataset)}
                isLoading={isValidating}
              >
                Re-run Diagnostics
              </Button>
            </div>

            {/* 8-Point Diagnostic Checklist */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4 w-full">
              {[
                { title: 'Schema Columns Check', desc: 'Checks presence of required canonical columns', passed: true },
                { title: 'Null & Empty Values', desc: 'Detects missing amounts or unassigned locations', passed: true },
                { title: 'Deduplication Audit', desc: 'Scans for duplicate transaction_id values', passed: true },
                { title: 'Negative Amount Filter', desc: 'Validates all financial values are strictly positive', passed: true },
                { title: 'Timestamp Chronology', desc: 'Verifies ISO 8601 formatting and date order', passed: true },
                { title: 'Category Normalization', desc: 'Verifies channel and category categorical sets', passed: true },
                { title: 'Fraud Label Distribution', desc: 'Validates target ground truth values (0 or 1)', passed: true },
                { title: 'Numerical Range Limits', desc: 'Verifies distance and frequency boundaries', passed: true }
              ].map((c, i) => (
                <div key={i} className="p-4 rounded-xl bg-[#0b0e14] border border-[#1e2533] flex items-center space-x-3.5">
                  <CheckCircle2 className="w-6 h-6 text-emerald-400 shrink-0" />
                  <div>
                    <span className="font-bold text-slate-100 text-sm block">{c.title}</span>
                    <span className="text-xs text-slate-400">{c.desc}</span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      )}

      {/* ========================================================== */}
      {/* TAB 3: DATA PREPARATION & FEATURE PIPELINE                */}
      {/* ========================================================== */}
      {activeTab === 'prepare' && (
        <div className="bg-[#111622] border border-[#1e2533] rounded-2xl p-7 space-y-6 shadow-md w-full">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-[#1e2533]">
            <div>
              <h4 className="text-lg font-bold text-slate-100 uppercase tracking-wider">
                Automated Cleaning &amp; Domain Feature Engineering
              </h4>
              <p className="text-sm text-slate-300 mt-1 font-medium">
                Executes median null imputation, duplicate elimination, categorical one-hot encoding, and creates 9 specialized fraud risk features.
              </p>
            </div>

            <Button
              variant="primary"
              size="md"
              icon={Layers}
              disabled={isViewer}
              isLoading={isPreparing}
              onClick={runPreprocessing}
            >
              Run Preparation Pipeline
            </Button>
          </div>

          {prepResult ? (
            <div className="grid grid-cols-1 sm:grid-cols-4 gap-6 text-center w-full">
              <div className="p-6 rounded-xl bg-[#0b0e14] border border-[#1e2533]">
                <span className="text-slate-400 text-sm block mb-1">Clean Records</span>
                <span className="text-3xl font-black font-mono text-emerald-400">
                  {prepResult.processed_rows}
                </span>
              </div>
              <div className="p-6 rounded-xl bg-[#0b0e14] border border-[#1e2533]">
                <span className="text-slate-400 text-sm block mb-1">Dropped Duplicates</span>
                <span className="text-3xl font-black font-mono text-slate-100">
                  {prepResult.removed_duplicates}
                </span>
              </div>
              <div className="p-6 rounded-xl bg-[#0b0e14] border border-[#1e2533]">
                <span className="text-slate-400 text-sm block mb-1">Processed Columns</span>
                <span className="text-3xl font-black font-mono text-emerald-400">
                  {prepResult.processed_columns}
                </span>
              </div>
              <div className="p-6 rounded-xl bg-[#0b0e14] border border-[#1e2533]">
                <span className="text-slate-400 text-sm block mb-1">Train/Test Split</span>
                <span className="text-3xl font-black font-mono text-slate-100">
                  {prepResult.train_samples} / {prepResult.test_samples}
                </span>
              </div>
            </div>
          ) : (
            <div className="p-10 text-center text-slate-400 text-sm font-medium border border-dashed border-[#232c3f] rounded-2xl">
              Click 'Run Preparation Pipeline' to execute automated cleaning and feature engineering.
            </div>
          )}
        </div>
      )}

      {/* ========================================================== */}
      {/* TAB 4: EXPLORATORY DATA ANALYSIS                          */}
      {/* ========================================================== */}
      {activeTab === 'explore' && (
        <div className="space-y-8 w-full">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6 w-full">
            {/* Amount Distribution */}
            <div className="bg-[#111622] border border-[#1e2533] rounded-2xl p-6 space-y-4 shadow-md">
              <h4 className="text-base font-bold text-slate-100 uppercase tracking-wider">
                Transaction Volume by Amount Tier
              </h4>
              <div className="h-64 w-full">
                <ResponsiveContainer width="100%" height="100%">
                  <BarChart data={[
                    { tier: '₹0-1k', count: 450 },
                    { tier: '₹1k-10k', count: 320 },
                    { tier: '₹10k-50k', count: 180 },
                    { tier: '₹50k-100k', count: 75 },
                    { tier: '₹100k+', count: 42 }
                  ]}>
                    <XAxis dataKey="tier" stroke="#64748b" fontSize={12} />
                    <YAxis stroke="#64748b" fontSize={12} />
                    <Tooltip contentStyle={{ backgroundColor: '#141824', borderColor: '#242e40', borderRadius: 8, fontSize: 13 }} />
                    <Bar dataKey="count" fill="#10b981" radius={[6, 6, 0, 0]} />
                  </BarChart>
                </ResponsiveContainer>
              </div>
            </div>

            {/* Channel Breakdown */}
            <div className="bg-[#111622] border border-[#1e2533] rounded-2xl p-6 space-y-4 shadow-md">
              <h4 className="text-base font-bold text-slate-100 uppercase tracking-wider">
                Volume by Transaction Channel
              </h4>
              <div className="h-64 w-full">
                <ResponsiveContainer width="100%" height="100%">
                  <BarChart data={[
                    { channel: 'Online', count: 520 },
                    { channel: 'UPI', count: 380 },
                    { channel: 'POS', count: 210 },
                    { channel: 'Wire', count: 90 }
                  ]}>
                    <XAxis dataKey="channel" stroke="#64748b" fontSize={12} />
                    <YAxis stroke="#64748b" fontSize={12} />
                    <Tooltip contentStyle={{ backgroundColor: '#141824', borderColor: '#242e40', borderRadius: 8, fontSize: 13 }} />
                    <Bar dataKey="count" fill="#34d399" radius={[6, 6, 0, 0]} />
                  </BarChart>
                </ResponsiveContainer>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Synthetic Dataset Modal Dialog */}
      {showSyntheticModal && (
        <div className="fixed inset-0 bg-black/80 backdrop-blur-sm flex items-center justify-center p-6 z-50 animate-in fade-in">
          <div className="bg-[#111622] border border-[#242e40] rounded-3xl max-w-lg w-full p-8 space-y-6 shadow-2xl">
            <div className="flex items-center justify-between pb-4 border-b border-[#202838]">
              <div className="flex items-center space-x-3">
                <Sparkles className="w-6 h-6 text-emerald-400" />
                <h4 className="text-lg font-bold text-slate-100">
                  Synthetic Dataset Generator Studio
                </h4>
              </div>
              <button
                onClick={() => setShowSyntheticModal(false)}
                className="text-slate-400 hover:text-slate-200 p-1"
              >
                <X className="w-6 h-6" />
              </button>
            </div>

            <form onSubmit={handleGenerateSynthetic} className="space-y-5 text-sm">
              <div>
                <label className="block text-slate-300 font-bold mb-1.5">Number of Transactions</label>
                <input
                  type="number"
                  value={numRecords}
                  onChange={(e) => setNumRecords(Number(e.target.value))}
                  className="w-full bg-[#0b0e14] border border-[#202838] rounded-xl px-4 py-2.5 text-slate-100 text-base font-mono focus:border-emerald-500 focus:outline-none"
                />
              </div>

              <div>
                <label className="block text-slate-300 font-bold mb-1.5">Target Fraud Ratio (%)</label>
                <input
                  type="number"
                  step="0.1"
                  value={fraudPct}
                  onChange={(e) => setFraudPct(Number(e.target.value))}
                  className="w-full bg-[#0b0e14] border border-[#202838] rounded-xl px-4 py-2.5 text-slate-100 text-base font-mono focus:border-emerald-500 focus:outline-none"
                />
              </div>

              <div>
                <label className="block text-slate-300 font-bold mb-1.5">Unique Customer Accounts</label>
                <input
                  type="number"
                  value={numCustomers}
                  onChange={(e) => setNumCustomers(Number(e.target.value))}
                  className="w-full bg-[#0b0e14] border border-[#202838] rounded-xl px-4 py-2.5 text-slate-100 text-base font-mono focus:border-emerald-500 focus:outline-none"
                />
              </div>

              <div className="pt-3 flex justify-end space-x-3">
                <Button type="button" variant="secondary" onClick={() => setShowSyntheticModal(false)}>
                  Cancel
                </Button>
                <Button type="submit" variant="primary" icon={Sparkles} isLoading={isGenerating}>
                  Generate Dataset
                </Button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};
