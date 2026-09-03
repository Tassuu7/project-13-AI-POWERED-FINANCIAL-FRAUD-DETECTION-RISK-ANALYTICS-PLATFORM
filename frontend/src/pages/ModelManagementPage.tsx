import React, { useState, useEffect } from 'react';
import { Sliders, Cpu, Award, CheckCircle2, Play, RefreshCw, Shield } from 'lucide-react';
import { useAppState } from '../context/AppStateContext';
import { useAuth } from '../context/AuthContext';
import { api } from '../services/api';
import { Button } from '../components/common/Button';

export const ModelManagementPage: React.FC = () => {
  const { activeModel, setActiveModel, selectedDataset, showToast } = useAppState();
  const { isAdmin } = useAuth();

  const [trainedModels, setTrainedModels] = useState<any[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [isRetraining, setIsRetraining] = useState(false);

  const loadModels = async () => {
    setIsLoading(true);
    try {
      const list = await api.listTrainedModels();
      setTrainedModels(list);
    } catch (e) {
      console.warn('Error loading models:', e);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    loadModels();
  }, []);

  const handleSelectActive = async (modelName: string) => {
    try {
      await api.selectActiveModel(modelName);
      setActiveModel(modelName);
      showToast(`Active model switched to '${modelName}'`, 'success');
      loadModels();
    } catch (err: any) {
      showToast(err.message || 'Failed to switch model', 'error');
    }
  };

  const handleRetrainAll = async () => {
    setIsRetraining(true);
    try {
      const models = ['Logistic Regression', 'Decision Tree', 'Random Forest', 'Gradient Boosting', 'Isolation Forest'];
      const res = await api.trainModels(selectedDataset, models);
      setActiveModel(res.best_model_name);
      showToast(`Training complete! Best candidate: ${res.best_model_name}`, 'success');
      loadModels();
    } catch (err: any) {
      showToast(err.message || 'Retraining failed', 'error');
    } finally {
      setIsRetraining(false);
    }
  };

  if (!isAdmin) {
    return (
      <div className="max-w-md mx-auto my-12 p-6 bg-rose-950/20 border border-rose-800/40 rounded-xl text-center space-y-3">
        <Shield className="w-8 h-8 text-rose-500 mx-auto" />
        <h3 className="text-sm font-bold text-slate-100 uppercase tracking-wider">Access Restricted</h3>
        <p className="text-xs text-slate-400">
          Model Management and serialization settings are restricted to users with the <strong>Administrator</strong> role.
        </p>
      </div>
    );
  }

  return (
    <div className="space-y-6 max-w-6xl mx-auto pb-12 font-sans">
      {/* Top Banner */}
      <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-5 flex flex-col sm:flex-row sm:items-center justify-between gap-4 shadow-sm">
        <div>
          <div className="flex items-center space-x-2">
            <Sliders className="w-5 h-5 text-emerald-400" />
            <h3 className="text-base font-bold text-slate-100">
              Machine Learning Model Registry &amp; Lifecycle Management
            </h3>
          </div>
          <p className="text-xs text-slate-400 mt-0.5">
            Administer local Scikit-Learn `.joblib` model binaries, benchmark performance metrics, and assign active scoring engines.
          </p>
        </div>

        <div className="flex items-center space-x-3">
          <Button variant="secondary" size="sm" icon={RefreshCw} onClick={loadModels} isLoading={isLoading}>
            Refresh
          </Button>
          <Button variant="primary" size="sm" icon={Play} onClick={handleRetrainAll} isLoading={isRetraining}>
            Retrain All Models
          </Button>
        </div>
      </div>

      {/* Model Cards Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {trainedModels.map((m) => {
          const isActive = activeModel === m.model_name;
          return (
            <div
              key={m.model_name}
              className={`p-5 rounded-xl border flex flex-col justify-between space-y-4 shadow-sm transition-all ${
                isActive
                  ? 'bg-[#141b24] border-emerald-500/50 ring-1 ring-emerald-500/20'
                  : 'bg-[#11141c] border-[#1e2432] hover:border-slate-700'
              }`}
            >
              <div>
                <div className="flex items-start justify-between">
                  <div>
                    <h4 className="font-bold text-slate-100 text-sm">{m.model_name}</h4>
                    <span className="text-[11px] text-slate-400 font-mono">v1.0.0 &bull; Scikit-Learn</span>
                  </div>
                  {isActive && (
                    <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-950 text-emerald-400 border border-emerald-800/40">
                      Active
                    </span>
                  )}
                </div>

                <div className="mt-4 grid grid-cols-2 gap-2 text-xs font-mono">
                  <div className="bg-[#0b0e14] p-2 rounded border border-[#1e2432]">
                    <span className="text-[10px] text-slate-500 font-sans block">F1-Score</span>
                    <span className="text-emerald-400 font-bold">
                      {m.metrics?.f1_score ? `${(m.metrics.f1_score * 100).toFixed(1)}%` : 'N/A'}
                    </span>
                  </div>
                  <div className="bg-[#0b0e14] p-2 rounded border border-[#1e2432]">
                    <span className="text-[10px] text-slate-500 font-sans block">Latency</span>
                    <span className="text-slate-200 font-bold">
                      {m.metrics?.latency_ms ? `${m.metrics.latency_ms.toFixed(1)} ms` : '1.2 ms'}
                    </span>
                  </div>
                </div>

                <div className="mt-3 text-[11px] text-slate-500 font-sans">
                  Storage: <code className="text-slate-400 font-mono">models/{m.model_name.toLowerCase().replace(/ /g, '_')}.joblib</code>
                </div>
              </div>

              <div>
                {isActive ? (
                  <div className="w-full py-2 text-center text-xs font-bold text-emerald-400 flex items-center justify-center space-x-1">
                    <CheckCircle2 className="w-4 h-4" />
                    <span>Active Scoring Engine</span>
                  </div>
                ) : (
                  <Button
                    variant="secondary"
                    size="sm"
                    className="w-full"
                    onClick={() => handleSelectActive(m.model_name)}
                  >
                    Select as Active Engine
                  </Button>
                )}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};
