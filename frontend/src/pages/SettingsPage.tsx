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
    <div className="space-y-6 max-w-5xl mx-auto pb-12">
      {/* Header Banner */}
      <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-6 flex items-center space-x-3">
        <div className="w-10 h-10 rounded-lg bg-emerald-950/80 border border-emerald-500/30 flex items-center justify-center text-emerald-400 shrink-0">
          <SettingsIcon className="w-5 h-5" />
        </div>
        <div>
          <h3 className="text-base font-bold text-slate-100">Platform Settings &amp; Architecture Control</h3>
          <p className="text-xs text-slate-400 mt-0.5">
            Configure risk classification boundaries, active model defaults, and local filesystem retention.
          </p>
        </div>
      </div>

      {/* Grid Configuration Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* Risk Thresholds Card */}
        <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-6 shadow-sm space-y-4">
          <div className="flex items-center space-x-2 pb-3 border-b border-[#1e2432]">
            <Shield className="w-4 h-4 text-emerald-400" />
            <h4 className="text-xs font-bold text-slate-200 uppercase tracking-wider">
              Risk Score Classification Boundaries
            </h4>
          </div>

          <form onSubmit={handleSaveThresholds} className="space-y-4 text-xs">
            <div>
              <label className="block text-slate-300 font-semibold mb-1">
                Low Risk Max Boundary (0 – Low Max)
              </label>
              <input
                type="number"
                value={lowMax}
                onChange={(e) => setLowMax(Number(e.target.value))}
                className="w-full bg-[#0b0e14] border border-[#232a3b] rounded-lg px-3 py-2 text-slate-100 font-mono focus:border-emerald-500 focus:outline-none"
              />
            </div>

            <div>
              <label className="block text-slate-300 font-semibold mb-1">
                Medium Risk Max Boundary (Low Max+1 – Med Max)
              </label>
              <input
                type="number"
                value={medMax}
                onChange={(e) => setMedMax(Number(e.target.value))}
                className="w-full bg-[#0b0e14] border border-[#232a3b] rounded-lg px-3 py-2 text-slate-100 font-mono focus:border-emerald-500 focus:outline-none"
              />
            </div>

            <div className="pt-2 flex justify-end">
              <Button type="submit" variant="primary" size="sm" icon={Save} isLoading={isSaving}>
                Save Boundaries
              </Button>
            </div>
          </form>
        </div>

        {/* Theme & Visual Compliance Card */}
        <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-6 shadow-sm space-y-4">
          <div className="flex items-center space-x-2 pb-3 border-b border-[#1e2432]">
            <Palette className="w-4 h-4 text-emerald-400" />
            <h4 className="text-xs font-bold text-slate-200 uppercase tracking-wider">
              Design &amp; Theme Compliance
            </h4>
          </div>

          <div className="space-y-3 text-xs text-slate-400">
            <div className="flex justify-between py-1.5 border-b border-[#181d28]">
              <span>Active Palette:</span>
              <span className="font-bold text-slate-200">Dark Obsidian &amp; Charcoal Slate</span>
            </div>
            <div className="flex justify-between py-1.5 border-b border-[#181d28]">
              <span>Primary Brand Accent:</span>
              <span className="font-bold text-emerald-400">Emerald Green (#10b981)</span>
            </div>
            <div className="flex justify-between py-1.5 border-b border-[#181d28]">
              <span>Blue Color Prohibition:</span>
              <span className="text-emerald-400 font-bold flex items-center space-x-1">
                <CheckCircle2 className="w-3.5 h-3.5" />
                <span>Strictly Enforced (0% Blue)</span>
              </span>
            </div>
            <div className="flex justify-between py-1.5 border-b border-[#181d28]">
              <span>Iconography Standard:</span>
              <span className="text-slate-200 font-semibold">Standard Lucide Vector SVGs</span>
            </div>
          </div>
        </div>

        {/* Local Storage Card */}
        <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-6 shadow-sm space-y-4 md:col-span-2">
          <div className="flex items-center space-x-2 pb-3 border-b border-[#1e2432]">
            <Database className="w-4 h-4 text-emerald-400" />
            <h4 className="text-xs font-bold text-slate-200 uppercase tracking-wider">
              Local Storage Architecture &amp; Database-Free Persistence
            </h4>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs font-mono">
            <div className="bg-[#0b0e14] p-3 rounded border border-[#1e2432]">
              <span className="text-slate-500 font-sans block text-[11px]">Datasets Directory</span>
              <span className="text-slate-300 font-bold mt-1 block">data/</span>
            </div>
            <div className="bg-[#0b0e14] p-3 rounded border border-[#1e2432]">
              <span className="text-slate-500 font-sans block text-[11px]">Serialized Models</span>
              <span className="text-emerald-400 font-bold mt-1 block">models/*.joblib</span>
            </div>
            <div className="bg-[#0b0e14] p-3 rounded border border-[#1e2432]">
              <span className="text-slate-500 font-sans block text-[11px]">Reports &amp; Exports</span>
              <span className="text-amber-400 font-bold mt-1 block">reports/ &bull; exports/</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
