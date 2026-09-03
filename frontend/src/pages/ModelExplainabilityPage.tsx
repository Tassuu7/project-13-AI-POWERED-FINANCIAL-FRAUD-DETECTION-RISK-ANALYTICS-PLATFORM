import React, { useState, useEffect } from 'react';
import {
  ResponsiveContainer,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip
} from 'recharts';
import { HelpCircle, ArrowUpRight, ArrowDownRight, RefreshCw, Zap } from 'lucide-react';
import { useAppState } from '../context/AppStateContext';
import { api } from '../services/api';
import { Button } from '../components/common/Button';

export const ModelExplainabilityPage: React.FC = () => {
  const { activeModel } = useAppState();

  const [globalImportance, setGlobalImportance] = useState<any[]>([]);
  const [localFactors, setLocalFactors] = useState<any[]>([]);
  const [isLoading, setIsLoading] = useState(true);

  // Local sample tester
  const [amount, setAmount] = useState(185000);
  const [distance, setDistance] = useState(240);
  const [frequency, setFrequency] = useState(6);
  const [device, setDevice] = useState('Unknown Device');

  const loadGlobal = async () => {
    setIsLoading(true);
    try {
      const data = await api.getGlobalImportance(activeModel);
      setGlobalImportance(data);

      // Also compute local explanation for current sample
      runLocalExplain();
    } catch (err) {
      console.warn('Explainability load error:', err);
    } finally {
      setIsLoading(false);
    }
  };

  const runLocalExplain = async () => {
    try {
      const sample = {
        amount: Number(amount),
        distance_from_usual_location: Number(distance),
        transaction_frequency: Number(frequency),
        device_type: device,
        timestamp: '2025-03-01 03:15:00'
      };
      const factors = await api.explainLocal(sample);
      setLocalFactors(factors);
    } catch (err) {
      console.warn('Local explain error:', err);
    }
  };

  useEffect(() => {
    loadGlobal();
  }, [activeModel]);

  return (
    <div className="space-y-6 max-w-6xl mx-auto pb-12">
      {/* Header Banner */}
      <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-5 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2">
            <HelpCircle className="w-5 h-5 text-emerald-400" />
            <h3 className="text-base font-bold text-slate-100">
              Model Interpretability &amp; Feature Attribution
            </h3>
          </div>
          <p className="text-xs text-slate-400 mt-0.5">
            Decipher model decision boundaries via global Gini feature importance and local per-transaction Shapley-style attributions.
          </p>
        </div>
        <Button variant="secondary" size="sm" icon={RefreshCw} onClick={loadGlobal} isLoading={isLoading}>
          Refresh Explainability
        </Button>
      </div>

      {/* Row 1: Global Feature Importance */}
      <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-6 space-y-4 shadow-sm">
        <h4 className="text-xs font-bold text-slate-300 uppercase tracking-wider">
          Global Feature Attribution Rankings ({activeModel})
        </h4>

        <div className="h-64">
          <ResponsiveContainer width="100%" height="100%">
            <BarChart data={globalImportance.slice(0, 8)} layout="vertical">
              <XAxis type="number" stroke="#475569" fontSize={10} unit="%" />
              <YAxis dataKey="feature" type="category" stroke="#475569" fontSize={10} width={160} />
              <Tooltip
                contentStyle={{ backgroundColor: '#141822', borderColor: '#242c3d', borderRadius: 6, fontSize: 12 }}
                formatter={(val: any) => [`${val}%`, 'Relative Weight']}
              />
              <Bar dataKey="importance_percent" name="Importance %" fill="#10b981" radius={[0, 4, 4, 0]} />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>

      {/* Row 2: Local Per-Transaction Attribution Waterfall */}
      <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-6 space-y-5 shadow-sm">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 border-b border-[#1e2432]">
          <div>
            <h4 className="text-xs font-bold text-slate-300 uppercase tracking-wider">
              Local Transaction Risk Attribution Waterfall
            </h4>
            <span className="text-xs text-slate-400">
              Quantify how specific transaction attributes escalate or mitigate the overall risk score.
            </span>
          </div>
          <Button variant="primary" size="sm" icon={Zap} onClick={runLocalExplain}>
            Recalculate Attribution
          </Button>
        </div>

        {/* Quick parameters strip */}
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 text-xs">
          <div>
            <label className="block text-slate-400 mb-1">Amount (INR)</label>
            <input
              type="number"
              value={amount}
              onChange={(e) => setAmount(Number(e.target.value))}
              className="w-full bg-[#0b0e14] border border-[#1e2432] rounded p-2 text-slate-100 font-mono"
            />
          </div>
          <div>
            <label className="block text-slate-400 mb-1">Distance (km)</label>
            <input
              type="number"
              value={distance}
              onChange={(e) => setDistance(Number(e.target.value))}
              className="w-full bg-[#0b0e14] border border-[#1e2432] rounded p-2 text-slate-100 font-mono"
            />
          </div>
          <div>
            <label className="block text-slate-400 mb-1">Frequency</label>
            <input
              type="number"
              value={frequency}
              onChange={(e) => setFrequency(Number(e.target.value))}
              className="w-full bg-[#0b0e14] border border-[#1e2432] rounded p-2 text-slate-100 font-mono"
            />
          </div>
          <div>
            <label className="block text-slate-400 mb-1">Device Token</label>
            <select
              value={device}
              onChange={(e) => setDevice(e.target.value)}
              className="w-full bg-[#0b0e14] border border-[#1e2432] rounded p-2 text-slate-100"
            >
              <option value="Unknown Device">Unknown Device</option>
              <option value="Trusted Mobile App">Trusted Mobile App</option>
            </select>
          </div>
        </div>

        {/* Contribution Cards */}
        <div className="space-y-2">
          {localFactors.map((f, idx) => {
            const isEscalator = f.contribution_points > 0;
            return (
              <div
                key={idx}
                className={`p-3.5 rounded-lg border flex items-center justify-between transition-colors ${
                  isEscalator
                    ? 'bg-rose-950/20 border-rose-800/40'
                    : 'bg-emerald-950/20 border-emerald-800/40'
                }`}
              >
                <div className="flex items-start space-x-3">
                  <div className={`p-1 rounded mt-0.5 ${isEscalator ? 'text-rose-400 bg-rose-950' : 'text-emerald-400 bg-emerald-950'}`}>
                    {isEscalator ? <ArrowUpRight className="w-4 h-4" /> : <ArrowDownRight className="w-4 h-4" />}
                  </div>
                  <div>
                    <div className="flex items-center space-x-2">
                      <span className="text-sm font-bold text-slate-200">{f.factor}</span>
                      <span className="text-xs font-mono text-slate-400 font-semibold">({f.value})</span>
                    </div>
                    <p className="text-xs text-slate-400 mt-0.5 leading-relaxed">{f.explanation}</p>
                  </div>
                </div>

                <div className="text-right shrink-0 ml-4 font-mono font-bold">
                  <span className={`text-sm ${isEscalator ? 'text-rose-400' : 'text-emerald-400'}`}>
                    {f.contribution_points > 0 ? `+${f.contribution_points}` : f.contribution_points} pts
                  </span>
                  <span className="block text-[10px] text-slate-500 uppercase">{f.direction}</span>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};
