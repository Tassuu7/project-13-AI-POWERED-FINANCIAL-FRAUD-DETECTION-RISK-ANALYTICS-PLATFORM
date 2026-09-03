import React, { useState } from 'react';
import { Activity, CheckSquare, Square, Play, CheckCircle2, ArrowRight, Shield, Cpu } from 'lucide-react';
import { useAppState } from '../context/AppStateContext';
import { api } from '../services/api';
import { ModelType, ModelComparisonResponse } from '../types';
import { Button } from '../components/common/Button';

export const ModelTrainingPage: React.FC<{ onNavigateNext?: () => void }> = ({ onNavigateNext }) => {
  const { selectedDataset, setActiveModel, showToast } = useAppState();

  const availableModels = [
    { type: 'Logistic Regression', desc: 'Linear baseline with balanced class weights. Extremely fast inference.' },
    { type: 'Decision Tree', desc: 'Captures non-linear thresholds and decision rules with high interpretability.' },
    { type: 'Random Forest', desc: 'Ensemble of 100 bagging trees. Superior generalization and high recall.' },
    { type: 'Gradient Boosting', desc: 'Sequential residual minimization. Yields high precision on subtle anomalies.' },
    { type: 'Isolation Forest', desc: 'Unsupervised tree isolation. Detects novel zero-day fraud patterns.' }
  ];

  const [selectedModels, setSelectedModels] = useState<string[]>([
    'Logistic Regression',
    'Decision Tree',
    'Random Forest',
    'Gradient Boosting'
  ]);
  const [handleImbalance, setHandleImbalance] = useState(true);
  const [testSplit, setTestSplit] = useState(0.2);
  const [isTraining, setIsTraining] = useState(false);
  const [comparisonResult, setComparisonResult] = useState<ModelComparisonResponse | null>(null);

  const toggleModel = (model: string) => {
    if (selectedModels.includes(model)) {
      if (selectedModels.length === 1) {
        showToast('Please select at least one algorithm to train.', 'info');
        return;
      }
      setSelectedModels(selectedModels.filter((m) => m !== model));
    } else {
      setSelectedModels([...selectedModels, model]);
    }
  };

  const handleTrain = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!selectedDataset) return;
    setIsTraining(true);
    try {
      const res = await api.trainModels({
        dataset_name: selectedDataset,
        models_to_train: selectedModels,
        handle_imbalance: handleImbalance,
        test_size: Number(testSplit),
      });

      setComparisonResult(res);
      setActiveModel(res.best_model_name);
      showToast(`Trained ${res.models.length} algorithms! Top model: ${res.best_model_name}`, 'success');
    } catch (err: any) {
      showToast(err.message || 'Model training failed', 'error');
    } finally {
      setIsTraining(false);
    }
  };

  return (
    <div className="space-y-6 max-w-5xl mx-auto pb-12">
      {/* Configuration Card */}
      <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-6 shadow-sm">
        <div className="flex items-center space-x-3 pb-4 border-b border-[#1e2432] mb-5">
          <div className="w-10 h-10 rounded-lg bg-emerald-950/80 border border-emerald-500/30 flex items-center justify-center text-emerald-400">
            <Activity className="w-5 h-5" />
          </div>
          <div>
            <h3 className="text-base font-bold text-slate-100">
              Machine Learning Model Training Center
            </h3>
            <p className="text-xs text-slate-400">
              Train local scikit-learn classifiers on <span className="font-mono text-emerald-400 font-bold">{selectedDataset}</span>. Zero cloud AI APIs.
            </p>
          </div>
        </div>

        <form onSubmit={handleTrain} className="space-y-6 text-xs">
          <div>
            <label className="block font-semibold text-slate-300 mb-2 uppercase tracking-wider">
              Select Algorithms to Train &amp; Benchmark
            </label>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
              {availableModels.map((m) => {
                const isChecked = selectedModels.includes(m.type);
                return (
                  <div
                    key={m.type}
                    onClick={() => toggleModel(m.type)}
                    className={`p-3.5 rounded-lg border cursor-pointer transition-all ${
                      isChecked
                        ? 'bg-emerald-950/30 border-emerald-500/80 text-slate-200'
                        : 'bg-[#0d1017] border-[#1e2432] text-slate-400 hover:border-slate-700'
                    }`}
                  >
                    <div className="flex items-center space-x-2.5">
                      {isChecked ? (
                        <CheckSquare className="w-4 h-4 text-emerald-400 shrink-0" />
                      ) : (
                        <Square className="w-4 h-4 text-slate-600 shrink-0" />
                      )}
                      <span className={`text-sm font-bold ${isChecked ? 'text-emerald-300' : 'text-slate-300'}`}>
                        {m.type}
                      </span>
                    </div>
                    <p className="text-xs text-slate-400 mt-1.5 pl-6.5 leading-relaxed">{m.desc}</p>
                  </div>
                );
              })}
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-5 pt-2 border-t border-[#1e2432]">
            <div>
              <label className="block font-semibold text-slate-300 mb-1.5 uppercase tracking-wider">
                Evaluation Test Split Ratio
              </label>
              <select
                value={testSplit}
                onChange={(e) => setTestSplit(Number(e.target.value))}
                className="w-full bg-[#0b0e14] border border-[#232a3b] rounded-lg px-3 py-2 text-slate-100 focus:border-emerald-500 focus:outline-none"
              >
                <option value={0.2}>80% Training / 20% Evaluation Test (Standard)</option>
                <option value={0.25}>75% Training / 25% Evaluation Test</option>
                <option value={0.3}>70% Training / 30% Evaluation Test</option>
              </select>
            </div>

            <div className="flex items-center space-x-3 pt-6">
              <input
                type="checkbox"
                id="imbalance"
                checked={handleImbalance}
                onChange={(e) => setHandleImbalance(e.target.checked)}
                className="w-4 h-4 text-emerald-500 bg-[#0b0e14] border-[#232a3b] rounded focus:ring-emerald-500"
              />
              <label htmlFor="imbalance" className="font-semibold text-slate-300 cursor-pointer">
                Class Imbalance Penalization (`class_weight='balanced'`)
              </label>
            </div>
          </div>

          <div className="flex justify-end pt-2">
            <Button type="submit" variant="primary" icon={Play} isLoading={isTraining}>
              {isTraining ? 'Training Models...' : `Train ${selectedModels.length} Selected Models`}
            </Button>
          </div>
        </form>
      </div>

      {/* Real Training Output Banner */}
      {comparisonResult && (
        <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-6 space-y-4">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 border-b border-[#1e2432]">
            <div>
              <div className="flex items-center space-x-2 text-emerald-400 font-bold uppercase tracking-wider text-xs">
                <CheckCircle2 className="w-4 h-4" />
                <span>Training Run Finished &amp; Serialized to Disk</span>
              </div>
              <h4 className="text-base font-bold text-slate-100 mt-0.5">
                Top Performing Architecture: <span className="text-emerald-400 font-mono">{comparisonResult.best_model_name}</span>
              </h4>
            </div>
            {onNavigateNext && (
              <Button variant="primary" size="sm" icon={ArrowRight} onClick={onNavigateNext}>
                View Full Model Evaluation
              </Button>
            )}
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
            {comparisonResult.models.map((m) => (
              <div
                key={m.model_name}
                className={`p-3.5 rounded-lg border ${
                  m.is_best
                    ? 'bg-emerald-950/30 border-emerald-500/60'
                    : 'bg-[#0b0e14] border-[#1e2432]'
                }`}
              >
                <div className="flex items-center justify-between">
                  <span className="font-bold text-slate-200 text-sm">{m.model_name}</span>
                  {m.is_best && (
                    <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-900 text-emerald-300 border border-emerald-700/40">
                      SELECTED BEST
                    </span>
                  )}
                </div>
                <div className="grid grid-cols-4 gap-2 mt-2.5 font-mono text-[11px]">
                  <div>
                    <span className="text-slate-500 block">F1</span>
                    <span className="font-bold text-slate-200">{(m.f1_score * 100).toFixed(1)}%</span>
                  </div>
                  <div>
                    <span className="text-slate-500 block">Recall</span>
                    <span className="font-bold text-emerald-400">{(m.recall * 100).toFixed(1)}%</span>
                  </div>
                  <div>
                    <span className="text-slate-500 block">Precision</span>
                    <span className="font-bold text-emerald-400">{(m.precision * 100).toFixed(1)}%</span>
                  </div>
                  <div>
                    <span className="text-slate-500 block">Latency</span>
                    <span className="text-slate-400">{m.training_time_seconds}s</span>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};
