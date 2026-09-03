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
    <header className="h-16 bg-[#0c0f16] border-b border-[#1a202c] px-6 flex items-center justify-between shrink-0 select-none">
      {/* Title & Subtitle */}
      <div>
        <h2 className="text-base font-bold text-slate-100 tracking-tight flex items-center space-x-2">
          <span>{pageTitle}</span>
        </h2>
        <p className="text-xs text-slate-400 truncate max-w-md">{pageSubtitle}</p>
      </div>

      {/* Control Strip */}
      <div className="flex items-center space-x-4">
        {/* Active Dataset Picker */}
        <div className="flex items-center space-x-2 bg-[#121620] border border-[#1f2636] px-2.5 py-1.5 rounded-md text-xs">
          <Database className="w-3.5 h-3.5 text-emerald-400 shrink-0" />
          <span className="text-slate-400">Dataset:</span>
          <select
            value={selectedDataset}
            onChange={(e) => setSelectedDataset(e.target.value)}
            className="bg-transparent text-slate-200 font-medium focus:outline-none cursor-pointer max-w-[180px] truncate"
          >
            {datasets.map((d) => (
              <option key={d.filename} value={d.filename} className="bg-[#121620] text-slate-200">
                {d.filename}
              </option>
            ))}
            {datasets.length === 0 && (
              <option value="sample_synthetic_transactions.csv" className="bg-[#121620] text-slate-200">
                sample_synthetic_transactions.csv
              </option>
            )}
          </select>
        </div>

        {/* Model Status Pill */}
        <div className="hidden md:flex items-center space-x-2 bg-[#121620] border border-[#1f2636] px-2.5 py-1.5 rounded-md text-xs">
          <Cpu className="w-3.5 h-3.5 text-emerald-400 shrink-0" />
          <span className="text-slate-400">Model:</span>
          <span className="text-emerald-300 font-medium">{activeModel || 'Random Forest'}</span>
        </div>

        {/* User Role Badge */}
        <div className="flex items-center space-x-2 bg-[#141824] border border-[#232b3d] px-3 py-1.5 rounded-md text-xs">
          <div className="w-5 h-5 rounded-full bg-emerald-950 border border-emerald-500/30 flex items-center justify-center text-[10px] font-bold text-emerald-400">
            {user?.role ? user.role.charAt(0) : 'A'}
          </div>
          <div className="text-left">
            <span className="text-slate-200 font-medium block leading-tight truncate max-w-[100px]">
              {user?.username || 'Analyst'}
            </span>
            <span className="text-[10px] text-emerald-400 block leading-tight font-semibold">
              {user?.role || 'Analyst'}
            </span>
          </div>
        </div>
      </div>
    </header>
  );
};
