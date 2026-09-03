import React, { useState } from 'react';
import { GitBranch, CheckCircle2, ArrowRight, Lightbulb, Zap } from 'lucide-react';
import { useAppState } from '../context/AppStateContext';
import { api } from '../services/api';
import { FeatureResponse, FeatureSummary } from '../types';
import { Button } from '../components/common/Button';

export const FeatureEngineeringPage: React.FC<{ onNavigateNext?: () => void }> = ({ onNavigateNext }) => {
  const { selectedDataset, showToast } = useAppState();
  const [isGenerating, setIsGenerating] = useState(false);
  const [featureData, setFeatureData] = useState<FeatureResponse | null>(null);

  const handleGenerateFeatures = async () => {
    if (!selectedDataset) return;
    setIsGenerating(true);
    try {
      const res = await api.generateFeatures(selectedDataset);
      setFeatureData(res);
      showToast(`Synthesized ${res.created_features.length} domain fraud indicators!`, 'success');
    } catch (err: any) {
      showToast(err.message || 'Feature engineering failed', 'error');
    } finally {
      setIsGenerating(false);
    }
  };

  return (
    <div className="space-y-6 max-w-5xl mx-auto pb-12">
      {/* Header Banner */}
      <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-6 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2">
            <GitBranch className="w-5 h-5 text-emerald-400" />
            <h3 className="text-base font-bold text-slate-100">
              Domain-Specific Fraud Feature Engineering
            </h3>
          </div>
          <p className="text-xs text-slate-400 mt-1">
            Deriving behavioral risk indicators, velocity counters, and geographic anomaly signals for{' '}
            <span className="font-mono text-emerald-400 font-bold">{selectedDataset}</span>.
          </p>
        </div>

        <Button
          variant="primary"
          icon={Zap}
          onClick={handleGenerateFeatures}
          isLoading={isGenerating}
        >
          Compute Engineered Features
        </Button>
      </div>

      {featureData && (
        <>
          {/* Metrics summary */}
          <div className="grid grid-cols-2 sm:grid-cols-3 gap-4">
            <div className="bg-[#11141c] border border-[#1e2432] p-4 rounded-xl">
              <span className="text-xs text-slate-400 uppercase tracking-wider">Raw Input Dimensions</span>
              <div className="text-xl font-bold text-slate-200 font-mono mt-1">
                {featureData.original_feature_count} Columns
              </div>
            </div>
            <div className="bg-[#11141c] border border-[#1e2432] p-4 rounded-xl">
              <span className="text-xs text-slate-400 uppercase tracking-wider">New Risk Signals Added</span>
              <div className="text-xl font-bold text-emerald-400 font-mono mt-1">
                +{featureData.created_features.length} Features
              </div>
            </div>
            <div className="bg-[#11141c] border border-[#1e2432] p-4 rounded-xl">
              <span className="text-xs text-slate-400 uppercase tracking-wider">Engineered Feature Space</span>
              <div className="text-xl font-bold text-slate-100 font-mono mt-1">
                {featureData.new_feature_count} Columns
              </div>
            </div>
          </div>

          {/* Feature Breakdown Table */}
          <div className="bg-[#11141c] border border-[#1e2432] rounded-xl overflow-hidden shadow-sm">
            <div className="px-5 py-3.5 bg-[#141822] border-b border-[#1e2432] flex items-center justify-between">
              <span className="text-xs font-bold text-slate-300 uppercase tracking-wider">
                Synthesized Behavioral Features &amp; Human Explanations
              </span>
              {onNavigateNext && (
                <Button variant="primary" size="sm" icon={ArrowRight} onClick={onNavigateNext}>
                  Proceed to Exploratory EDA
                </Button>
              )}
            </div>

            <div className="divide-y divide-[#181d28]">
              {featureData.created_features.map((f: FeatureSummary) => (
                <div key={f.feature_name} className="p-4 hover:bg-[#141824] transition-colors">
                  <div className="flex items-center space-x-3">
                    <span className="w-6 h-6 rounded-full bg-emerald-950 border border-emerald-500/40 text-emerald-400 text-xs font-bold font-mono flex items-center justify-center shrink-0">
                      {f.importance_rank}
                    </span>
                    <span className="text-sm font-mono font-bold text-slate-100">
                      {f.feature_name}
                    </span>
                    <span className="px-2 py-0.5 rounded text-[10px] font-mono bg-[#1a202c] text-slate-300 border border-[#273142]">
                      {f.feature_type}
                    </span>
                  </div>
                  <p className="text-xs text-slate-400 mt-2 pl-9 leading-relaxed">
                    {f.description}
                  </p>
                </div>
              ))}
            </div>
          </div>
        </>
      )}
    </div>
  );
};
