import React from 'react';
import { Database, Cpu, User, Bell } from 'lucide-react';
import { useAppState } from '../../context/AppStateContext';
import { useAuth } from '../../context/AuthContext';

interface HeaderProps {
  pageTitle: string;
  pageSubtitle: string;
}

export const Header: React.FC<HeaderProps> = ({ pageTitle, pageSubtitle }) => {
  const { selectedDataset, setSelectedDataset, datasets, activeModel } = useAppState();
  const { user } = useAuth();

  return (
    <header className="h-20 bg-[#0c1017] border-b border-[#1e2533] px-8 flex items-center justify-between shrink-0 select-none shadow-sm">
      {/* Title & Subtitle with Large Clear Typography */}
      <div className="min-w-0 pr-4">
        <h2 className="text-xl md:text-2xl font-black text-slate-100 tracking-tight flex items-center space-x-3">
          <span>{pageTitle}</span>
        </h2>
        <p className="text-sm text-slate-300 font-medium truncate mt-0.5">{pageSubtitle}</p>
      </div>

      {/* Control Strip */}
      <div className="flex items-center space-x-4 shrink-0">
        {/* Active Dataset Picker */}
        <div className="flex items-center space-x-2.5 bg-[#121722] border border-[#232c3f] px-3.5 py-2 rounded-xl text-sm shadow-sm">
          <Database className="w-4 h-4 text-emerald-400 shrink-0" />
          <span className="text-slate-400 font-semibold">Dataset:</span>
          <select
            value={selectedDataset}
            onChange={(e) => setSelectedDataset(e.target.value)}
            className="bg-transparent text-slate-100 font-bold focus:outline-none cursor-pointer max-w-[220px] truncate"
          >
            {datasets.map((d) => (
              <option key={d.filename} value={d.filename} className="bg-[#121722] text-slate-100">
                {d.filename}
              </option>
            ))}
            {datasets.length === 0 && (
              <option value="sample_synthetic_transactions.csv" className="bg-[#121722] text-slate-100">
                sample_synthetic_transactions.csv
              </option>
            )}
          </select>
        </div>

        {/* Model Status Pill */}
        <div className="hidden lg:flex items-center space-x-2.5 bg-[#121722] border border-[#232c3f] px-3.5 py-2 rounded-xl text-sm shadow-sm">
          <Cpu className="w-4 h-4 text-emerald-400 shrink-0" />
          <span className="text-slate-400 font-semibold">Active Engine:</span>
          <span className="text-emerald-300 font-bold font-mono">{activeModel || 'Random Forest'}</span>
        </div>

        {/* User Role Badge */}
        <div className="flex items-center space-x-3 bg-[#151c2a] border border-[#263348] px-4 py-2 rounded-xl text-sm shadow-sm">
          <div className="w-7 h-7 rounded-lg bg-emerald-950/90 border border-emerald-500/40 flex items-center justify-center text-xs font-black text-emerald-400 font-mono">
            {user?.role ? user.role.charAt(0) : 'A'}
          </div>
          <div className="text-left">
            <span className="text-slate-100 font-bold block leading-tight truncate max-w-[120px]">
              {user?.username || 'Analyst'}
            </span>
            <span className="text-xs text-emerald-400 block leading-tight font-semibold mt-0.5">
              {user?.role || 'Analyst'}
            </span>
          </div>
        </div>
      </div>
    </header>
  );
};
