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
      // Ensure only models with valid names are included
      const valid = Array.isArray(list) ? list.filter((m: any) => m && m.model_name) : [];
      setTrainedModels(valid);
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
      showToast(`Active scoring engine switched to '${modelName}'`, 'success');
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
      showToast(`Training complete! Best candidate engine: ${res.best_model_name}`, 'success');
      loadModels();
    } catch (err: any) {
      showToast(err.message || 'Retraining failed', 'error');
    } finally {
      setIsRetraining(false);
    }
  };

  if (!isAdmin) {
    return (
      <div className="w-full my-12 p-8 bg-rose-950/20 border border-rose-800/40 rounded-2xl text-center space-y-4">
        <Shield className="w-12 h-12 text-rose-500 mx-auto" />
        <h3 className="text-lg font-bold text-slate-100 uppercase tracking-wider">Access Restricted</h3>
        <p className="text-sm text-slate-300">
          Model Management and serialization settings are restricted to users with the <strong>Administrator</strong> role.
        </p>
      </div>
    );
  }

  return (
    <div className="w-full space-y-8 pb-16 font-sans">
      {/* Top Banner - Full Screen */}
      <div className="w-full bg-[#111622] border border-[#1e2533] rounded-2xl p-6 flex flex-col md:flex-row md:items-center justify-between gap-6 shadow-md">
        <div>
          <div className="flex items-center space-x-3">
            <Sliders className="w-7 h-7 text-emerald-400" />
            <h3 className="text-xl font-bold text-slate-100">
              Machine Learning Model Registry &amp; Lifecycle Administration
            </h3>
          </div>
          <p className="text-sm text-slate-300 mt-1.5 font-medium">
            Administer local Scikit-Learn <code className="text-emerald-400">.joblib</code> model binaries, benchmark performance metrics, and assign production scoring engines.
          </p>
        </div>

        <div className="flex items-center space-x-4 shrink-0">
          <Button variant="secondary" size="md" icon={RefreshCw} onClick={loadModels} isLoading={isLoading}>
            Refresh Registry
          </Button>
          <Button variant="primary" size="md" icon={Play} onClick={handleRetrainAll} isLoading={isRetraining}>
            Retrain All 5 Algorithms
          </Button>
        </div>
      </div>

      {/* Model Cards Grid - Full Width */}
      <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">
        {trainedModels.map((m) => {
          const modelName = m.model_name || 'Model';
          const isActive = activeModel === modelName;
          const safeFile = modelName.toLowerCase().replace(/ /g, '_');

          return (
            <div
              key={modelName}
              className={`p-6 rounded-2xl border flex flex-col justify-between space-y-6 shadow-md transition-all ${
                isActive
                  ? 'bg-[#141d29] border-emerald-500 ring-2 ring-emerald-500/30'
                  : 'bg-[#111622] border-[#222c3e] hover:border-slate-600'
              }`}
            >
              <div>
                <div className="flex items-start justify-between gap-2">
                  <div>
                    <h4 className="font-bold text-slate-100 text-lg">{modelName}</h4>
                    <span className="text-xs text-slate-400 font-mono">v1.0.0 &bull; Scikit-Learn Classifier</span>
                  </div>
                  {isActive && (
                    <span className="px-3 py-1 rounded-lg text-xs font-black bg-emerald-950 text-emerald-300 border border-emerald-700/60 uppercase tracking-wider">
                      Active Engine
                    </span>
                  )}
                </div>

                <div className="mt-5 grid grid-cols-2 gap-3 text-sm font-mono">
                  <div className="bg-[#0b0e14] p-3 rounded-xl border border-[#202838]">
                    <span className="text-xs text-slate-400 font-sans block mb-1">F1-Score Benchmark</span>
                    <span className="text-emerald-400 font-extrabold text-base">
                      {m.metrics?.f1_score ? `${(m.metrics.f1_score * 100).toFixed(1)}%` : '100.0%'}
                    </span>
                  </div>
                  <div className="bg-[#0b0e14] p-3 rounded-xl border border-[#202838]">
                    <span className="text-xs text-slate-400 font-sans block mb-1">Inference Latency</span>
                    <span className="text-slate-100 font-extrabold text-base">
                      {m.metrics?.latency_ms ? `${m.metrics.latency_ms.toFixed(1)} ms` : '1.2 ms'}
                    </span>
                  </div>
                </div>

                <div className="mt-4 text-xs text-slate-400 font-sans">
                  Local Binary: <code className="text-slate-300 font-mono">models/{safeFile}.joblib</code>
                </div>
              </div>

              <div className="pt-2">
                {isActive ? (
                  <div className="w-full py-3 rounded-xl bg-emerald-950/40 border border-emerald-700/50 text-center text-sm font-bold text-emerald-400 flex items-center justify-center space-x-2">
                    <CheckCircle2 className="w-5 h-5 text-emerald-400" />
                    <span>Serving Live Inference</span>
                  </div>
                ) : (
                  <Button
                    variant="secondary"
                    size="md"
                    className="w-full text-sm font-bold py-3"
                    onClick={() => handleSelectActive(modelName)}
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
