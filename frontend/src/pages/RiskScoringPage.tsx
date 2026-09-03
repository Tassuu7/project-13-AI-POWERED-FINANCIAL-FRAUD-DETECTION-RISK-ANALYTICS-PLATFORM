import React, { useState, useEffect } from 'react';
import { ShieldAlert, Sliders, CheckCircle2, AlertTriangle, Save, RefreshCw } from 'lucide-react';
import { useAppState } from '../context/AppStateContext';
import { api } from '../services/api';
import { Button } from '../components/common/Button';

export const RiskScoringPage: React.FC = () => {
  const { showToast } = useAppState();
  const [thresholds, setThresholds] = useState<any>(null);
  const [lowMax, setLowMax] = useState(30);
  const [medMax, setMedMax] = useState(70);
  const [isSaving, setIsSaving] = useState(false);

  const loadThresholds = async () => {
    try {
      const res = await api.getRiskThresholds();
      setThresholds(res);
      setLowMax(res.bands.low.max);
      setMedMax(res.bands.medium.max);
    } catch (err) {
      console.warn('Error loading thresholds:', err);
    }
  };

  useEffect(() => {
    loadThresholds();
  }, []);

  const handleSave = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsSaving(true);
    try {
      await api.updateRiskThresholds(Number(lowMax), Number(medMax));
      showToast('Risk scoring thresholds updated successfully!', 'success');
      loadThresholds();
    } catch (err: any) {
      showToast(err.message || 'Failed to update thresholds', 'error');
    } finally {
      setIsSaving(false);
    }
  };

  const factors = [
    { name: 'Extreme Amount Surge', weight: '35 pts', impact: 'HIGH', rule: 'Amount >= ₹1,00,000 OR >= 5x historical baseline' },
    { name: 'Geographic Displacement', weight: '30 pts', impact: 'HIGH', rule: 'Displacement >= 200 km from usual registered cluster' },
    { name: 'Anomalous Transaction Hour', weight: '25 pts', impact: 'HIGH', rule: 'Initiated during dark hours (01:00 AM - 05:00 AM)' },
    { name: 'Untrusted Hardware Fingerprint', weight: '25 pts', impact: 'HIGH', rule: 'Hardware signature unknown, emulated, or rooted' },
    { name: 'Burst Velocity Frequency', weight: '20 pts', impact: 'MEDIUM', rule: '>= 5 transactions initiated within the current window' },
    { name: 'High-Liquidity Channel', weight: '15 pts', impact: 'LOW', rule: 'Category represents Crypto, Wire, or Luxury Goods' }
  ];

  return (
    <div className="space-y-6 max-w-5xl mx-auto pb-12">
      {/* Overview Banner */}
      <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-6 flex items-center space-x-3">
        <div className="w-10 h-10 rounded-lg bg-emerald-950/80 border border-emerald-500/30 flex items-center justify-center text-emerald-400 shrink-0">
          <ShieldAlert className="w-5 h-5" />
        </div>
        <div>
          <h3 className="text-base font-bold text-slate-100">Transparent Risk Scoring Engine</h3>
          <p className="text-xs text-slate-400 mt-0.5">
            Deterministic 0–100 calibrated risk evaluation blending supervised machine learning probability with rule-based heuristics.
          </p>
        </div>
      </div>

      {/* Score Bands Display */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div className="bg-[#11141c] border border-emerald-800/40 rounded-xl p-5 shadow-sm">
          <div className="flex items-center justify-between">
            <span className="text-xs font-bold text-emerald-400 uppercase tracking-wider">Tier 1: Low Risk</span>
            <span className="font-mono font-bold text-emerald-300 text-sm">0 – {lowMax}</span>
          </div>
          <div className="mt-3 text-xs text-slate-300 space-y-1">
            <span className="font-semibold block text-slate-200">Standard Processing</span>
            <p className="text-slate-400 leading-relaxed">
              Conforms to customer baseline history. Instant automated authorization approved.
            </p>
          </div>
        </div>

        <div className="bg-[#11141c] border border-amber-800/40 rounded-xl p-5 shadow-sm">
          <div className="flex items-center justify-between">
            <span className="text-xs font-bold text-amber-400 uppercase tracking-wider">Tier 2: Medium Risk</span>
            <span className="font-mono font-bold text-amber-300 text-sm">{lowMax + 1} – {medMax}</span>
          </div>
          <div className="mt-3 text-xs text-slate-300 space-y-1">
            <span className="font-semibold block text-slate-200">Step-up Authentication</span>
            <p className="text-slate-400 leading-relaxed">
              Triggers secondary verification (biometric or time-based one-time password OTP).
            </p>
          </div>
        </div>

        <div className="bg-[#11141c] border border-rose-800/40 rounded-xl p-5 shadow-sm">
          <div className="flex items-center justify-between">
            <span className="text-xs font-bold text-rose-400 uppercase tracking-wider">Tier 3: High Risk</span>
            <span className="font-mono font-bold text-rose-300 text-sm">{medMax + 1} – 100</span>
          </div>
          <div className="mt-3 text-xs text-slate-300 space-y-1">
            <span className="font-semibold block text-slate-200">Hold &amp; Manual Review</span>
            <p className="text-slate-400 leading-relaxed">
              Automated hold triggered. Transaction routed to fraud investigation desk for analyst triage.
            </p>
          </div>
        </div>
      </div>

      {/* Threshold Tuner */}
      <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-6 shadow-sm">
        <h4 className="text-xs font-bold text-slate-300 uppercase tracking-wider mb-4 flex items-center space-x-2">
          <Sliders className="w-4 h-4 text-emerald-400" />
          <span>Calibrate Risk Threshold Boundaries</span>
        </h4>

        <form onSubmit={handleSave} className="grid grid-cols-1 md:grid-cols-2 gap-5 text-xs">
          <div>
            <label className="block font-semibold text-slate-300 mb-1.5 uppercase tracking-wider">
              Low Risk Ceiling (Max Score for Low Tier)
            </label>
            <input
              type="number"
              min={10}
              max={50}
              value={lowMax}
              onChange={(e) => setLowMax(Number(e.target.value))}
              className="w-full bg-[#0b0e14] border border-[#232a3b] rounded-lg px-3 py-2 text-slate-100 font-mono focus:border-emerald-500 focus:outline-none"
            />
            <span className="text-[11px] text-slate-500 mt-1 block">Default: 30</span>
          </div>

          <div>
            <label className="block font-semibold text-slate-300 mb-1.5 uppercase tracking-wider">
              Medium Risk Ceiling (Boundary before High Risk)
            </label>
            <input
              type="number"
              min={51}
              max={85}
              value={medMax}
              onChange={(e) => setMedMax(Number(e.target.value))}
              className="w-full bg-[#0b0e14] border border-[#232a3b] rounded-lg px-3 py-2 text-slate-100 font-mono focus:border-emerald-500 focus:outline-none"
            />
            <span className="text-[11px] text-slate-500 mt-1 block">Default: 70</span>
          </div>

          <div className="md:col-span-2 flex justify-end">
            <Button type="submit" variant="primary" icon={Save} isLoading={isSaving}>
              Save Risk Threshold Settings
            </Button>
          </div>
        </form>
      </div>

      {/* Verifiable Contributing Heuristics Table */}
      <div className="bg-[#11141c] border border-[#1e2432] rounded-xl overflow-hidden shadow-sm">
        <div className="px-5 py-3.5 bg-[#141822] border-b border-[#1e2432] text-xs font-bold text-slate-300 uppercase tracking-wider">
          Transparent Heuristic Anomaly Point Allocations
        </div>
        <div className="divide-y divide-[#181d28] text-xs">
          {factors.map((f, i) => (
            <div key={i} className="p-4 flex items-center justify-between hover:bg-[#141824] transition-colors">
              <div>
                <span className="font-semibold text-slate-200 block text-sm">{f.name}</span>
                <span className="text-slate-400 text-xs mt-0.5 block">{f.rule}</span>
              </div>
              <div className="text-right shrink-0 ml-4">
                <span className="font-mono font-bold text-emerald-400 block text-sm">+{f.weight}</span>
                <span className={`px-2 py-0.5 rounded text-[10px] font-bold ${
                  f.impact === 'HIGH' ? 'bg-rose-950 text-rose-400 border border-rose-800/40' :
                  f.impact === 'MEDIUM' ? 'bg-amber-950 text-amber-400 border border-amber-800/40' :
                  'bg-slate-800 text-slate-300'
                }`}>
                  {f.impact}
                </span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
