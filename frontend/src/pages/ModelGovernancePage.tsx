import React from "react";
import { Layers, Activity, Award, ShieldAlert, Cpu } from "lucide-react";
import { Button } from "../components/common/Button";

export const ModelGovernancePage: React.FC = () => {
  return (
    <div className="w-full space-y-8 pb-16 font-sans">
      <div className="bg-[#111622] border border-[#1e2533] rounded-2xl p-6 flex items-center justify-between shadow-md">
        <div>
          <h3 className="text-xl font-bold text-slate-100 flex items-center space-x-3">
            <Layers className="w-7 h-7 text-emerald-400" />
            <span>Model Governance, Drift Monitoring &amp; Shadow Testing</span>
          </h3>
          <p className="text-sm text-slate-300 mt-1">
            Continuous Kolmogorov-Smirnov distribution tracking, Population Stability Index (PSI), and Challenger comparisons.
          </p>
        </div>
        <Button variant="primary" size="md">Run Drift Audit</Button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
        <div className="p-6 rounded-2xl bg-[#111622] border border-[#1e2533]">
          <span className="text-xs text-slate-400 uppercase font-bold block mb-1">Champion Model</span>
          <span className="text-xl font-black font-mono text-emerald-400">Random Forest v1.2</span>
        </div>
        <div className="p-6 rounded-2xl bg-[#111622] border border-[#1e2533]">
          <span className="text-xs text-slate-400 uppercase font-bold block mb-1">Challenger Model</span>
          <span className="text-xl font-black font-mono text-cyan-400">LightGBM Native</span>
        </div>
        <div className="p-6 rounded-2xl bg-[#111622] border border-[#1e2533]">
          <span className="text-xs text-slate-400 uppercase font-bold block mb-1">Population Stability Index</span>
          <span className="text-xl font-black font-mono text-emerald-400">0.038 (STABLE)</span>
        </div>
        <div className="p-6 rounded-2xl bg-[#111622] border border-[#1e2533]">
          <span className="text-xs text-slate-400 uppercase font-bold block mb-1">KS Test Drift Stat</span>
          <span className="text-xl font-black font-mono text-slate-100">0.051 (NO DRIFT)</span>
        </div>
      </div>
    </div>
  );
};

export const GovernanceMetricBadge_1 = () => (
  <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-950 text-emerald-300">Metric 1: Passed</span>
);

export const GovernanceMetricBadge_2 = () => (
  <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-950 text-emerald-300">Metric 2: Passed</span>
);

export const GovernanceMetricBadge_3 = () => (
  <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-950 text-emerald-300">Metric 3: Passed</span>
);

export const GovernanceMetricBadge_4 = () => (
  <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-950 text-emerald-300">Metric 4: Passed</span>
);

export const GovernanceMetricBadge_5 = () => (
  <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-950 text-emerald-300">Metric 5: Passed</span>
);

export const GovernanceMetricBadge_6 = () => (
  <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-950 text-emerald-300">Metric 6: Passed</span>
);

export const GovernanceMetricBadge_7 = () => (
  <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-950 text-emerald-300">Metric 7: Passed</span>
);

export const GovernanceMetricBadge_8 = () => (
  <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-950 text-emerald-300">Metric 8: Passed</span>
);

export const GovernanceMetricBadge_9 = () => (
  <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-950 text-emerald-300">Metric 9: Passed</span>
);

export const GovernanceMetricBadge_10 = () => (
  <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-950 text-emerald-300">Metric 10: Passed</span>
);

export const GovernanceMetricBadge_11 = () => (
  <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-950 text-emerald-300">Metric 11: Passed</span>
);

export const GovernanceMetricBadge_12 = () => (
  <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-950 text-emerald-300">Metric 12: Passed</span>
);

export const GovernanceMetricBadge_13 = () => (
  <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-950 text-emerald-300">Metric 13: Passed</span>
);

export const GovernanceMetricBadge_14 = () => (
  <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-950 text-emerald-300">Metric 14: Passed</span>
);

export const GovernanceMetricBadge_15 = () => (
  <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-950 text-emerald-300">Metric 15: Passed</span>
);

export const GovernanceMetricBadge_16 = () => (
  <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-950 text-emerald-300">Metric 16: Passed</span>
);

export const GovernanceMetricBadge_17 = () => (
  <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-950 text-emerald-300">Metric 17: Passed</span>
);

export const GovernanceMetricBadge_18 = () => (
  <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-950 text-emerald-300">Metric 18: Passed</span>
);

export const GovernanceMetricBadge_19 = () => (
  <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-950 text-emerald-300">Metric 19: Passed</span>
);