import React, { useState, useEffect } from 'react';
import {
  ResponsiveContainer,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  Legend,
  ScatterChart,
  Scatter
} from 'recharts';
import { BarChart2, TrendingUp, RefreshCw, ArrowRight, Table, Layers } from 'lucide-react';
import { useAppState } from '../context/AppStateContext';
import { api } from '../services/api';
import { Button } from '../components/common/Button';

export const EdaPage: React.FC<{ onNavigateNext?: () => void }> = ({ onNavigateNext }) => {
  const { selectedDataset } = useAppState();
  const [data, setData] = useState<any>(null);
  const [isLoading, setIsLoading] = useState(true);

  const loadEda = async () => {
    if (!selectedDataset) return;
    setIsLoading(true);
    try {
      const summary = await api.getEdaSummary(selectedDataset);
      setData(summary);
    } catch (err) {
      console.warn('EDA load error:', err);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    loadEda();
  }, [selectedDataset]);

  if (isLoading) {
    return (
      <div className="flex flex-col items-center justify-center h-96 space-y-3">
        <RefreshCw className="w-8 h-8 text-emerald-400 animate-spin" />
        <span className="text-sm text-slate-400">Computing exploratory data analytics for {selectedDataset}...</span>
      </div>
    );
  }

  if (!data || data.error) {
    return (
      <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-8 text-center max-w-md mx-auto my-12">
        <p className="text-sm text-slate-300">No EDA statistics found for dataset.</p>
      </div>
    );
  }

  return (
    <div className="space-y-6 max-w-6xl mx-auto pb-12">
      {/* Header Strip */}
      <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-5 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2">
            <BarChart2 className="w-5 h-5 text-emerald-400" />
            <h3 className="text-base font-bold text-slate-100">
              Exploratory Data Analysis (EDA) &amp; Statistical Profiling
            </h3>
          </div>
          <p className="text-xs text-slate-400 mt-0.5">
            Statistical correlations, variable distributions, and fraud density mappings across {data.total_transactions} records.
          </p>
        </div>
        <div className="flex items-center space-x-3">
          <Button variant="secondary" size="sm" icon={RefreshCw} onClick={loadEda}>
            Recompute EDA
          </Button>
          {onNavigateNext && (
            <Button variant="primary" size="sm" icon={ArrowRight} onClick={onNavigateNext}>
              Proceed to Model Training
            </Button>
          )}
        </div>
      </div>

      {/* Row 1: Numerical Statistical Properties Table */}
      <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-5 shadow-sm">
        <h4 className="text-xs font-bold text-slate-300 uppercase tracking-wider mb-3">
          Numerical Distribution Statistics (Five-Number Summary)
        </h4>
        <div className="overflow-x-auto rounded border border-[#1e2432]">
          <table className="w-full text-xs text-left">
            <thead className="bg-[#161a24] text-slate-300 font-semibold border-b border-[#1e2432]">
              <tr>
                <th className="px-3.5 py-2.5">Feature Name</th>
                <th className="px-3.5 py-2.5">Mean</th>
                <th className="px-3.5 py-2.5">Std Dev</th>
                <th className="px-3.5 py-2.5">Min</th>
                <th className="px-3.5 py-2.5">Q1 (25%)</th>
                <th className="px-3.5 py-2.5">Median</th>
                <th className="px-3.5 py-2.5">Q3 (75%)</th>
                <th className="px-3.5 py-2.5">Max</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-[#181d28] font-mono text-slate-300">
              {Object.entries(data.numeric_stats || {}).map(([key, st]: [string, any]) => (
                <tr key={key} className="hover:bg-[#141822]">
                  <td className="px-3.5 py-2 font-bold text-slate-200">{key}</td>
                  <td className="px-3.5 py-2">{st.mean}</td>
                  <td className="px-3.5 py-2 text-slate-400">{st.std}</td>
                  <td className="px-3.5 py-2">{st.min}</td>
                  <td className="px-3.5 py-2 text-slate-400">{st.q25}</td>
                  <td className="px-3.5 py-2 text-emerald-400 font-bold">{st.median}</td>
                  <td className="px-3.5 py-2 text-slate-400">{st.q75}</td>
                  <td className="px-3.5 py-2 text-rose-400">{st.max}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>

      {/* Row 2: Correlation Analysis with Target Column */}
      <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-5 shadow-sm">
        <h4 className="text-xs font-bold text-slate-300 uppercase tracking-wider mb-3">
          Feature Correlation with Fraud Occurrence (`is_fraud`)
        </h4>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3 text-xs">
          {(data.correlations || []).slice(0, 8).map((c: any) => {
            const isPos = c.correlation > 0;
            return (
              <div key={c.feature} className="bg-[#0c0f16] border border-[#1d2330] p-3 rounded-lg flex flex-col justify-between">
                <div>
                  <span className="font-mono text-slate-200 font-bold block truncate">{c.feature}</span>
                  <span className="text-[10px] text-slate-500 uppercase">{c.strength} Correlation</span>
                </div>
                <div className="mt-2 flex items-center justify-between">
                  <span className={`text-base font-bold font-mono ${isPos ? 'text-rose-400' : 'text-emerald-400'}`}>
                    {c.correlation > 0 ? `+${c.correlation}` : c.correlation}
                  </span>
                  <span className={`text-[10px] px-1.5 py-0.5 rounded font-bold ${
                    isPos ? 'bg-rose-950 text-rose-400 border border-rose-800/40' : 'bg-emerald-950 text-emerald-400 border border-emerald-800/40'
                  }`}>
                    {c.relationship}
                  </span>
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* Row 3: Geographical & Device Incident Rates */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Location Breakdowns */}
        <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-5">
          <h4 className="text-xs font-bold text-slate-300 uppercase tracking-wider mb-3">
            Top Fraud Occurrence by Metropolitan Location
          </h4>
          <div className="h-64">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={(data.by_location || []).slice(0, 7)} layout="vertical">
                <XAxis type="number" stroke="#475569" fontSize={10} unit="%" />
                <YAxis dataKey="location" type="category" stroke="#475569" fontSize={10} width={90} />
                <Tooltip contentStyle={{ backgroundColor: '#141822', borderColor: '#242c3d', borderRadius: 6, fontSize: 12 }} />
                <Bar dataKey="fraud_rate" name="Fraud Rate (%)" fill="#ef4444" radius={[0, 4, 4, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* Device Breakdowns */}
        <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-5">
          <h4 className="text-xs font-bold text-slate-300 uppercase tracking-wider mb-3">
            Hardware &amp; Browser Device Fingerprint Risk
          </h4>
          <div className="h-64">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={(data.by_device || []).slice(0, 7)} layout="vertical">
                <XAxis type="number" stroke="#475569" fontSize={10} unit="%" />
                <YAxis dataKey="device" type="category" stroke="#475569" fontSize={10} width={120} />
                <Tooltip contentStyle={{ backgroundColor: '#141822', borderColor: '#242c3d', borderRadius: 6, fontSize: 12 }} />
                <Bar dataKey="fraud_rate" name="Fraud Rate (%)" fill="#f59e0b" radius={[0, 4, 4, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>
    </div>
  );
};
