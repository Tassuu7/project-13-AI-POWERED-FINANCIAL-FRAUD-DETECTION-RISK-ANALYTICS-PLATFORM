import React, { useState, useEffect } from 'react';
import { Award, CheckCircle2, AlertCircle, ArrowRight, RefreshCw, Cpu, Layers } from 'lucide-react';
import { useAppState } from '../context/AppStateContext';
import { api } from '../services/api';
import { ModelMetrics } from '../types';
import { Button } from '../components/common/Button';

export const ModelEvaluationPage: React.FC<{ onNavigateNext?: () => void }> = ({ onNavigateNext }) => {
  const { activeModel, setActiveModel, showToast } = useAppState();
  const [models, setModels] = useState<any[]>([]);
  const [selectedForDetail, setSelectedForDetail] = useState<any>(null);
  const [isLoading, setIsLoading] = useState(true);

  const loadModels = async () => {
    setIsLoading(true);
    try {
      const list = await api.listTrainedModels();
      setModels(list);
      if (list.length > 0) {
        // Select active or first
        const cur = list.find((m) => m.model_name === activeModel) || list[0];
        setSelectedForDetail(cur);
      }
    } catch (err) {
      console.warn('Error loading models:', err);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    loadModels();
  }, [activeModel]);

  const handleSelectActive = async (modelName: string) => {
    try {
      await api.selectActiveModel(modelName);
      setActiveModel(modelName);
      showToast(`Active inference model updated to '${modelName}'`, 'success');
      loadModels();
    } catch (err: any) {
      showToast(err.message || 'Failed to update active model', 'error');
    }
  };

  return (
    <div className="space-y-6 max-w-6xl mx-auto pb-12">
      {/* Header Banner */}
      <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-5 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2">
            <Award className="w-5 h-5 text-emerald-400" />
            <h3 className="text-base font-bold text-slate-100">
              Model Benchmarking &amp; Performance Evaluation
            </h3>
          </div>
          <p className="text-xs text-slate-400 mt-0.5">
            Compare classifiers on F1-Score, Recall, and ROC-AUC. Active engine: <span className="text-emerald-400 font-bold font-mono">{activeModel}</span>
          </p>
        </div>
        <div className="flex items-center space-x-3">
          <Button variant="secondary" size="sm" icon={RefreshCw} onClick={loadModels} isLoading={isLoading}>
            Refresh Benchmarks
          </Button>
          {onNavigateNext && (
            <Button variant="primary" size="sm" icon={ArrowRight} onClick={onNavigateNext}>
              Run Fraud Prediction
            </Button>
          )}
        </div>
      </div>

      {/* Critical Fraud Metric Callout */}
      <div className="bg-[#0e1219] border border-[#1f283a] rounded-xl p-4 text-xs text-slate-300 flex items-start space-x-3">
        <AlertCircle className="w-5 h-5 text-amber-400 shrink-0 mt-0.5" />
        <div className="space-y-1">
          <span className="font-bold text-slate-100 uppercase tracking-wider block">
            Why Accuracy is Not Enough in Fraud Analytics
          </span>
          <p className="text-slate-400 leading-relaxed">
            In datasets where fraud represents only 3–7% of volume, a naive model predicting 100% normal achieves 95% accuracy while letting 100% of fraud pass undetected. For financial fraud detection, <strong className="text-emerald-400 font-semibold">Recall</strong> (catching every fraud incident) and <strong className="text-amber-400 font-semibold">Precision</strong> (minimizing false alarms for legitimate users) are the primary engineering metrics.
          </p>
        </div>
      </div>

      {/* Models Comparison Table */}
      <div className="bg-[#11141c] border border-[#1e2432] rounded-xl overflow-hidden shadow-sm">
        <div className="px-5 py-3.5 bg-[#141822] border-b border-[#1e2432] text-xs font-bold text-slate-300 uppercase tracking-wider">
          Algorithm Performance Comparison Matrix
        </div>

        <div className="overflow-x-auto">
          <table className="w-full text-xs text-left">
            <thead className="bg-[#161a24] text-slate-300 font-semibold border-b border-[#1e2432]">
              <tr>
                <th className="px-4 py-3">Algorithm</th>
                <th className="px-4 py-3">Accuracy</th>
                <th className="px-4 py-3">Precision</th>
                <th className="px-4 py-3">Recall</th>
                <th className="px-4 py-3">F1-Score</th>
                <th className="px-4 py-3">ROC-AUC</th>
                <th className="px-4 py-3">Latency</th>
                <th className="px-4 py-3 text-right">Production Action</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-[#181d28] font-mono text-slate-300">
              {models.map((m) => {
                const met: ModelMetrics = m.metrics || {};
                const isActive = m.model_name === activeModel;

                return (
                  <tr
                    key={m.model_name}
                    onClick={() => setSelectedForDetail(m)}
                    className={`cursor-pointer transition-colors ${
                      isActive ? 'bg-emerald-950/25' : 'hover:bg-[#141822]'
                    }`}
                  >
                    <td className="px-4 py-3 font-sans font-bold text-slate-100 flex items-center space-x-2">
                      <span>{m.model_name}</span>
                      {isActive && (
                        <span className="text-[10px] px-2 py-0.5 rounded font-mono font-bold bg-emerald-900/80 text-emerald-300 border border-emerald-700/50">
                          ACTIVE
                        </span>
                      )}
                    </td>
                    <td className="px-4 py-3">{((met.accuracy || 0) * 100).toFixed(1)}%</td>
                    <td className="px-4 py-3 text-emerald-400 font-bold">{((met.precision || 0) * 100).toFixed(1)}%</td>
                    <td className="px-4 py-3 text-emerald-400 font-bold">{((met.recall || 0) * 100).toFixed(1)}%</td>
                    <td className="px-4 py-3 text-amber-400 font-bold">{((met.f1_score || 0) * 100).toFixed(1)}%</td>
                    <td className="px-4 py-3 text-slate-300">
                      {met.roc_auc ? ((met.roc_auc || 0) * 100).toFixed(1) + '%' : 'N/A'}
                    </td>
                    <td className="px-4 py-3 text-slate-400">{met.training_time_seconds || 0}s</td>
                    <td className="px-4 py-3 text-right">
                      <Button
                        size="sm"
                        variant={isActive ? 'secondary' : 'primary'}
                        onClick={(e) => {
                          e.stopPropagation();
                          handleSelectActive(m.model_name);
                        }}
                        disabled={isActive}
                      >
                        {isActive ? 'Active Engine' : 'Deploy Model'}
                      </Button>
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>

      {/* Selected Model Deep Dive: Confusion Matrix & Rationale */}
      {selectedForDetail && (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {/* Confusion Matrix Card */}
          <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-5 shadow-sm">
            <h4 className="text-xs font-bold text-slate-300 uppercase tracking-wider mb-3">
              Confusion Matrix: {selectedForDetail.model_name}
            </h4>

            {selectedForDetail.metrics?.confusion_matrix ? (
              <div className="grid grid-cols-2 gap-3 text-center text-xs font-mono">
                <div className="bg-[#0b0e14] border border-[#1e2432] p-4 rounded-lg">
                  <span className="text-slate-400 text-[11px] block">True Negatives (TN)</span>
                  <div className="text-xl font-bold text-emerald-400 mt-1">
                    {selectedForDetail.metrics.confusion_matrix[0][0]}
                  </div>
                  <span className="text-[10px] text-slate-500">Correct Normal</span>
                </div>

                <div className="bg-[#0b0e14] border border-[#1e2432] p-4 rounded-lg">
                  <span className="text-slate-400 text-[11px] block">False Positives (FP)</span>
                  <div className="text-xl font-bold text-amber-400 mt-1">
                    {selectedForDetail.metrics.confusion_matrix[0][1]}
                  </div>
                  <span className="text-[10px] text-slate-500">Normal Flagged</span>
                </div>

                <div className="bg-[#0b0e14] border border-[#1e2432] p-4 rounded-lg">
                  <span className="text-slate-400 text-[11px] block">False Negatives (FN)</span>
                  <div className="text-xl font-bold text-rose-500 mt-1">
                    {selectedForDetail.metrics.confusion_matrix[1][0]}
                  </div>
                  <span className="text-[10px] text-slate-500">Missed Fraud!</span>
                </div>

                <div className="bg-[#0b0e14] border border-[#1e2432] p-4 rounded-lg">
                  <span className="text-slate-400 text-[11px] block">True Positives (TP)</span>
                  <div className="text-xl font-bold text-emerald-400 mt-1">
                    {selectedForDetail.metrics.confusion_matrix[1][1]}
                  </div>
                  <span className="text-[10px] text-slate-500">Caught Fraud</span>
                </div>
              </div>
            ) : (
              <p className="text-xs text-slate-400">Confusion matrix not recorded for this model.</p>
            )}
          </div>

          {/* Model Architectural Rationale */}
          <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-5 shadow-sm space-y-3">
            <h4 className="text-xs font-bold text-slate-300 uppercase tracking-wider">
              Engineering Rationale &amp; Artifact Details
            </h4>
            <div className="space-y-2 text-xs text-slate-400">
              <div className="flex justify-between py-1 border-b border-[#1a202c]">
                <span>Trained Dataset:</span>
                <span className="font-mono text-slate-200">{selectedForDetail.dataset_name}</span>
              </div>
              <div className="flex justify-between py-1 border-b border-[#1a202c]">
                <span>Trained Timestamp:</span>
                <span className="font-mono text-slate-200">{selectedForDetail.trained_at}</span>
              </div>
              <div className="flex justify-between py-1 border-b border-[#1a202c]">
                <span>Input Feature Count:</span>
                <span className="font-mono text-emerald-400">{selectedForDetail.features?.length || 13} features</span>
              </div>
              <div className="pt-2">
                <span className="text-slate-300 font-semibold block mb-1">Architectural Notes:</span>
                <p className="text-slate-400 leading-relaxed bg-[#0b0e14] p-3 rounded border border-[#1a202c]">
                  {selectedForDetail.metrics?.notes || 'Standard optimized classifier artifact.'}
                </p>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
