import React, { useState, useEffect } from 'react';
import { Settings as SettingsIcon, Shield, Database, Cpu, Palette, Save, CheckCircle2 } from 'lucide-react';
import { useAppState } from '../context/AppStateContext';
import { api } from '../services/api';
import { PlatformSettings } from '../types';
import { Button } from '../components/common/Button';

export const SettingsPage: React.FC = () => {
  const { activeModel, setActiveModel, showToast } = useAppState();

  const [settings, setSettings] = useState<PlatformSettings | null>(null);
  const [lowMax, setLowMax] = useState(30);
  const [medMax, setMedMax] = useState(70);
  const [isSaving, setIsSaving] = useState(false);

  const loadSettings = async () => {
    try {
      const data = await api.getSettings();
      setSettings(data);
      setLowMax(data.risk_thresholds.low_max);
      setMedMax(data.risk_thresholds.medium_max);
    } catch (err) {
      console.warn('Error fetching settings:', err);
    }
  };

  useEffect(() => {
    loadSettings();
  }, []);

  const handleSaveThresholds = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsSaving(true);
    try {
      await api.updateRiskThresholds(Number(lowMax), Number(medMax));
      showToast('System configuration saved!', 'success');
      loadSettings();
    } catch (err: any) {
      showToast(err.message || 'Failed to update settings', 'error');
    } finally {
      setIsSaving(false);
    }
  };

  return (
    <div className="w-full space-y-8 pb-16 font-sans">
      {/* Header Banner - Full Screen */}
      <div className="w-full bg-[#111622] border border-[#1e2533] rounded-2xl p-6 flex items-center space-x-4 shadow-md">
        <div className="w-12 h-12 rounded-2xl bg-emerald-950/80 border border-emerald-500/40 flex items-center justify-center text-emerald-400 shrink-0 shadow-sm">
          <SettingsIcon className="w-7 h-7" />
        </div>
        <div>
          <h3 className="text-xl font-bold text-slate-100">Platform Settings &amp; Architecture Control</h3>
          <p className="text-sm text-slate-300 mt-1 font-medium">
            Configure risk classification boundaries, active model defaults, and local filesystem retention rules.
          </p>
        </div>
      </div>

      {/* Grid Configuration Cards */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 w-full">
        {/* Risk Threshold Calibration Form */}
        <div className="bg-[#111622] border border-[#1e2533] rounded-2xl p-7 space-y-6 shadow-md">
          <div className="flex items-center space-x-3 pb-4 border-b border-[#1e2533]">
            <Shield className="w-6 h-6 text-emerald-400" />
            <h4 className="text-base font-bold text-slate-100 uppercase tracking-wider">
              Risk Severity Boundary Tuning
            </h4>
          </div>

          <form onSubmit={handleSaveThresholds} className="space-y-6 text-sm">
            <div>
              <div className="flex justify-between mb-2">
                <label className="font-bold text-slate-200">
                  Low Risk Upper Cutoff (Current: {lowMax}/100)
                </label>
                <span className="text-emerald-400 font-mono font-black text-base">0 &ndash; {lowMax}</span>
              </div>
              <input
                type="range"
                min={10}
                max={50}
                value={lowMax}
                onChange={(e) => setLowMax(Number(e.target.value))}
                className="w-full accent-emerald-500 h-2 bg-[#0b0e14] rounded-lg cursor-pointer"
              />
              <span className="text-xs text-slate-400 mt-1 block">
                Transactions below this score are classified as Normal (Verified).
              </span>
            </div>

            <div>
              <div className="flex justify-between mb-2">
                <label className="font-bold text-slate-200">
                  Medium Risk Upper Cutoff (Current: {medMax}/100)
                </label>
                <span className="text-amber-400 font-mono font-black text-base">{lowMax + 1} &ndash; {medMax}</span>
              </div>
              <input
                type="range"
                min={51}
                max={90}
                value={medMax}
                onChange={(e) => setMedMax(Number(e.target.value))}
                className="w-full accent-amber-500 h-2 bg-[#0b0e14] rounded-lg cursor-pointer"
              />
              <span className="text-xs text-slate-400 mt-1 block">
                Transactions between {lowMax + 1} and {medMax} are routed to Medium review. Transactions &gt; {medMax} trigger High Alert.
              </span>
            </div>

            <div className="pt-2 flex justify-end">
              <Button type="submit" variant="primary" icon={Save} isLoading={isSaving} className="py-3 px-6 text-sm font-bold shadow-lg">
                Persist Threshold Configuration
              </Button>
            </div>
          </form>
        </div>

        {/* Local-First Architecture Specifications */}
        <div className="bg-[#111622] border border-[#1e2533] rounded-2xl p-7 space-y-6 shadow-md">
          <div className="flex items-center space-x-3 pb-4 border-b border-[#1e2533]">
            <Database className="w-6 h-6 text-emerald-400" />
            <h4 className="text-base font-bold text-slate-100 uppercase tracking-wider">
              Local Storage Environment Diagnostics
            </h4>
          </div>

          <div className="space-y-4 text-sm font-mono">
            <div className="p-4 rounded-xl bg-[#0b0e14] border border-[#1e2533] flex justify-between items-center">
              <span className="text-slate-400 font-sans">Database Driver:</span>
              <span className="text-emerald-400 font-bold">None (Local JSON / CSV / Joblib)</span>
            </div>
            <div className="p-4 rounded-xl bg-[#0b0e14] border border-[#1e2533] flex justify-between items-center">
              <span className="text-slate-400 font-sans">Model Serialization:</span>
              <span className="text-slate-200 font-bold">models/*.joblib (Scikit-Learn)</span>
            </div>
            <div className="p-4 rounded-xl bg-[#0b0e14] border border-[#1e2533] flex justify-between items-center">
              <span className="text-slate-400 font-sans">External Cloud AI Keys:</span>
              <span className="text-emerald-400 font-bold">Disabled (100% Local Inference)</span>
            </div>
            <div className="p-4 rounded-xl bg-[#0b0e14] border border-[#1e2533] flex justify-between items-center">
              <span className="text-slate-400 font-sans">Enterprise Palette:</span>
              <span className="text-slate-200 font-bold">Obsidian &bull; Emerald &bull; Amber &bull; Crimson</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
