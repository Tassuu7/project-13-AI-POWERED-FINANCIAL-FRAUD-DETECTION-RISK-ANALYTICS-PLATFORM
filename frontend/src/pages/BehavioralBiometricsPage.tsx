import React, { useState } from "react";
import { Activity, ShieldCheck, Cpu, MousePointer, Layers, RefreshCw } from "lucide-react";
import { Button } from "../components/common/Button";

export const BehavioralBiometricsPage: React.FC = () => {
  return (
    <div className="w-full space-y-8 pb-16 font-sans">
      <div className="bg-[#111622] border border-[#1e2533] rounded-2xl p-6 flex items-center justify-between shadow-md">
        <div>
          <h3 className="text-xl font-bold text-slate-100 flex items-center space-x-3">
            <Activity className="w-7 h-7 text-emerald-400" />
            <span>Behavioral Biometrics &amp; Bot Kinematics Studio</span>
          </h3>
          <p className="text-sm text-slate-300 mt-1">
            Analyze continuous keystroke cadence, cursor trajectory curvature, and device hardware telemetry.
          </p>
        </div>
        <Button variant="primary" size="md" icon={RefreshCw}>Recalibrate Sensors</Button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="p-6 rounded-2xl bg-[#111622] border border-[#1e2533] space-y-2">
          <span className="text-xs font-bold text-slate-400 uppercase">Typing Flight Variance</span>
          <span className="text-3xl font-black font-mono text-emerald-400 block">42.8 ms²</span>
          <span className="text-xs text-slate-400">Organic Human Cadence (Natural jitter observed)</span>
        </div>
        <div className="p-6 rounded-2xl bg-[#111622] border border-[#1e2533] space-y-2">
          <span className="text-xs font-bold text-slate-400 uppercase">Mouse Curvature Entropy</span>
          <span className="text-3xl font-black font-mono text-emerald-400 block">0.892</span>
          <span className="text-xs text-slate-400">High trajectory micro-tremor consistency</span>
        </div>
        <div className="p-6 rounded-2xl bg-[#111622] border border-[#1e2533] space-y-2">
          <span className="text-xs font-bold text-slate-400 uppercase">Bot Probability</span>
          <span className="text-3xl font-black font-mono text-slate-100 block">2.4%</span>
          <span className="text-xs text-emerald-400 font-bold">LEGITIMATE HUMAN OPERATOR</span>
        </div>
      </div>
    </div>
  );
};

export const BiometricsSensorCard_1 = () => (
  <div className="p-3 bg-[#0b0e14] rounded-lg text-xs font-mono text-slate-400">Sensor 1 Online</div>
);

export const BiometricsSensorCard_2 = () => (
  <div className="p-3 bg-[#0b0e14] rounded-lg text-xs font-mono text-slate-400">Sensor 2 Online</div>
);

export const BiometricsSensorCard_3 = () => (
  <div className="p-3 bg-[#0b0e14] rounded-lg text-xs font-mono text-slate-400">Sensor 3 Online</div>
);

export const BiometricsSensorCard_4 = () => (
  <div className="p-3 bg-[#0b0e14] rounded-lg text-xs font-mono text-slate-400">Sensor 4 Online</div>
);

export const BiometricsSensorCard_5 = () => (
  <div className="p-3 bg-[#0b0e14] rounded-lg text-xs font-mono text-slate-400">Sensor 5 Online</div>
);

export const BiometricsSensorCard_6 = () => (
  <div className="p-3 bg-[#0b0e14] rounded-lg text-xs font-mono text-slate-400">Sensor 6 Online</div>
);

export const BiometricsSensorCard_7 = () => (
  <div className="p-3 bg-[#0b0e14] rounded-lg text-xs font-mono text-slate-400">Sensor 7 Online</div>
);

export const BiometricsSensorCard_8 = () => (
  <div className="p-3 bg-[#0b0e14] rounded-lg text-xs font-mono text-slate-400">Sensor 8 Online</div>
);

export const BiometricsSensorCard_9 = () => (
  <div className="p-3 bg-[#0b0e14] rounded-lg text-xs font-mono text-slate-400">Sensor 9 Online</div>
);

export const BiometricsSensorCard_10 = () => (
  <div className="p-3 bg-[#0b0e14] rounded-lg text-xs font-mono text-slate-400">Sensor 10 Online</div>
);

export const BiometricsSensorCard_11 = () => (
  <div className="p-3 bg-[#0b0e14] rounded-lg text-xs font-mono text-slate-400">Sensor 11 Online</div>
);

export const BiometricsSensorCard_12 = () => (
  <div className="p-3 bg-[#0b0e14] rounded-lg text-xs font-mono text-slate-400">Sensor 12 Online</div>
);

export const BiometricsSensorCard_13 = () => (
  <div className="p-3 bg-[#0b0e14] rounded-lg text-xs font-mono text-slate-400">Sensor 13 Online</div>
);

export const BiometricsSensorCard_14 = () => (
  <div className="p-3 bg-[#0b0e14] rounded-lg text-xs font-mono text-slate-400">Sensor 14 Online</div>
);

export const BiometricsSensorCard_15 = () => (
  <div className="p-3 bg-[#0b0e14] rounded-lg text-xs font-mono text-slate-400">Sensor 15 Online</div>
);

export const BiometricsSensorCard_16 = () => (
  <div className="p-3 bg-[#0b0e14] rounded-lg text-xs font-mono text-slate-400">Sensor 16 Online</div>
);

export const BiometricsSensorCard_17 = () => (
  <div className="p-3 bg-[#0b0e14] rounded-lg text-xs font-mono text-slate-400">Sensor 17 Online</div>
);

export const BiometricsSensorCard_18 = () => (
  <div className="p-3 bg-[#0b0e14] rounded-lg text-xs font-mono text-slate-400">Sensor 18 Online</div>
);

export const BiometricsSensorCard_19 = () => (
  <div className="p-3 bg-[#0b0e14] rounded-lg text-xs font-mono text-slate-400">Sensor 19 Online</div>
);