import React, { useState } from 'react';
import { Sliders, CheckCircle2, ArrowRight, Activity, Settings2, FileCheck } from 'lucide-react';
import { useAppState } from '../context/AppStateContext';
import { api } from '../services/api';
import { PreprocessingResult } from '../types';
import { Button } from '../components/common/Button';

export const PreprocessingPage: React.FC<{ onNavigateNext?: () => void }> = ({ onNavigateNext }) => {
  const { selectedDataset, showToast } = useAppState();

  const [missingStrategy, setMissingStrategy] = useState('median_mode');
  const [handleDuplicates, setHandleDuplicates] = useState(true);
  const [scalingMethod, setScalingMethod] = useState('standard');
  const [testSize, setTestSize] = useState(0.2);
  const [isProcessing, setIsProcessing] = useState(false);
  const [result, setResult] = useState<PreprocessingResult | null>(null);

  const handleRunPreprocessing = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!selectedDataset) return;
    setIsProcessing(true);
    try {
      const res = await api.runPreprocessing({
        filename: selectedDataset,
        handle_missing: missingStrategy,
        handle_duplicates: handleDuplicates,
        scaling_method: scalingMethod,
        test_size: Number(testSize),
      });
      setResult(res);
      showToast('Preprocessing pipeline completed successfully!', 'success');
    } catch (err: any) {
      showToast(err.message || 'Preprocessing error', 'error');
    } finally {
      setIsProcessing(false);
    }
  };

  return (
    <div className="space-y-6 max-w-5xl mx-auto pb-12">
      {/* Configuration Card */}
      <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-6 shadow-sm">
        <div className="flex items-center space-x-3 pb-4 border-b border-[#1e2432] mb-5">
          <div className="w-10 h-10 rounded-lg bg-emerald-950/80 border border-emerald-500/30 flex items-center justify-center text-emerald-400">
            <Sliders className="w-5 h-5" />
          </div>
          <div>
            <h3 className="text-base font-bold text-slate-100">
              Data Preprocessing &amp; Transformation Pipeline
            </h3>
            <p className="text-xs text-slate-400">
              Configure deterministic data cleansing, categorical one-hot encoding, and feature scaling for {selectedDataset}.
            </p>
          </div>
        </div>

        <form onSubmit={handleRunPreprocessing} className="space-y-6 text-xs">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
            <div>
              <label className="block font-semibold text-slate-300 mb-1.5 uppercase tracking-wider">
                Missing Values Imputation Strategy
              </label>
              <select
                value={missingStrategy}
                onChange={(e) => setMissingStrategy(e.target.value)}
                className="w-full bg-[#0b0e14] border border-[#232a3b] rounded-lg px-3 py-2 text-slate-100 focus:border-emerald-500 focus:outline-none"
              >
                <option value="median_mode">Median (Numeric) &amp; Mode (Categorical) — Preserves Distribution</option>
                <option value="drop">Listwise Deletion (Drop Incomplete Rows)</option>
              </select>
            </div>

            <div>
              <label className="block font-semibold text-slate-300 mb-1.5 uppercase tracking-wider">
                Feature Scaling Algorithm
              </label>
              <select
                value={scalingMethod}
                onChange={(e) => setScalingMethod(e.target.value)}
                className="w-full bg-[#0b0e14] border border-[#232a3b] rounded-lg px-3 py-2 text-slate-100 focus:border-emerald-500 focus:outline-none"
              >
                <option value="standard">StandardScaler (Zero Mean, Unit Variance)</option>
                <option value="robust">RobustScaler (Median &amp; IQR, Resists Fraud Outliers)</option>
                <option value="minmax">MinMaxScaler (Bounded [0, 1])</option>
              </select>
            </div>

            <div>
              <label className="block font-semibold text-slate-300 mb-1.5 uppercase tracking-wider">
                Train / Test Validation Split
              </label>
              <select
                value={testSize}
                onChange={(e) => setTestSize(Number(e.target.value))}
                className="w-full bg-[#0b0e14] border border-[#232a3b] rounded-lg px-3 py-2 text-slate-100 focus:border-emerald-500 focus:outline-none font-mono"
              >
                <option value={0.2}>80% Training / 20% Evaluation Test Set (Standard)</option>
                <option value={0.25}>75% Training / 25% Evaluation Test Set</option>
                <option value={0.3}>70% Training / 30% Evaluation Test Set</option>
              </select>
            </div>

            <div className="flex items-center space-x-3 pt-6">
              <input
                type="checkbox"
                id="dedup"
                checked={handleDuplicates}
                onChange={(e) => setHandleDuplicates(e.target.checked)}
                className="w-4 h-4 text-emerald-500 bg-[#0b0e14] border-[#232a3b] rounded focus:ring-emerald-500"
              />
              <label htmlFor="dedup" className="font-semibold text-slate-300 cursor-pointer">
                Strict Transaction ID Deduplication &amp; Row Cleaning
              </label>
            </div>
          </div>

          <div className="flex justify-end pt-2">
            <Button type="submit" variant="primary" icon={Activity} isLoading={isProcessing}>
              Execute Preprocessing Pipeline
            </Button>
          </div>
        </form>
      </div>

      {/* Before & After Results Card */}
      {result && (
        <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-6 space-y-5">
          <div className="flex items-center justify-between pb-3 border-b border-[#1e2432]">
            <div className="flex items-center space-x-2">
              <CheckCircle2 className="w-5 h-5 text-emerald-400" />
              <h4 className="text-sm font-bold text-slate-100 uppercase tracking-wider">
                Pipeline Execution Summary &amp; Matrix Shapes
              </h4>
            </div>
            {onNavigateNext && (
              <Button variant="primary" size="sm" icon={ArrowRight} onClick={onNavigateNext}>
                Proceed to Feature Engineering
              </Button>
            )}
          </div>

          <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 text-xs">
            <div className="bg-[#0b0e14] p-3 rounded-lg border border-[#1e2432]">
              <span className="text-slate-400">Original Matrix</span>
              <div className="text-base font-bold text-slate-200 font-mono mt-1">
                {result.original_shape[0]} × {result.original_shape[1]}
              </div>
            </div>

            <div className="bg-[#0b0e14] p-3 rounded-lg border border-[#1e2432]">
              <span className="text-slate-400">Processed Matrix</span>
              <div className="text-base font-bold text-emerald-400 font-mono mt-1">
                {result.processed_shape[0]} × {result.processed_shape[1]}
              </div>
            </div>

            <div className="bg-[#0b0e14] p-3 rounded-lg border border-[#1e2432]">
              <span className="text-slate-400">Train Split</span>
              <div className="text-base font-bold text-slate-200 font-mono mt-1">
                {result.train_shape[0]} samples
              </div>
            </div>

            <div className="bg-[#0b0e14] p-3 rounded-lg border border-[#1e2432]">
              <span className="text-slate-400">Evaluation Test Split</span>
              <div className="text-base font-bold text-amber-400 font-mono mt-1">
                {result.test_shape[0]} samples
              </div>
            </div>
          </div>

          {/* Audit Notes Log */}
          <div className="bg-[#0b0e14] border border-[#1e2432] rounded-lg p-4 text-xs space-y-2">
            <span className="font-bold text-slate-300 uppercase tracking-wider block">
              Step-by-Step Operations Log
            </span>
            <ul className="space-y-1.5 text-slate-400">
              {result.summary_notes.map((note, idx) => (
                <li key={idx} className="flex items-start space-x-2">
                  <span className="text-emerald-400 font-mono">[{idx + 1}]</span>
                  <span>{note}</span>
                </li>
              ))}
            </ul>
          </div>
        </div>
      )}
    </div>
  );
};
