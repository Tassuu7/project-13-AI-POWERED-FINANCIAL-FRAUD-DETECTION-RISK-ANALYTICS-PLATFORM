import React from 'react';
import {
  LayoutDashboard,
  FileSpreadsheet,
  Cpu,
  ShieldAlert,
  FileText,
  Sliders,
  Clock,
  Settings as SettingsIcon,
  HelpCircle,
  LogOut,
  Shield,
  UserCheck
} from 'lucide-react';
import { useAuth } from '../../context/AuthContext';

interface SidebarProps {
  activePage: string;
  setActivePage: (page: string) => void;
  onLogout: () => void;
}

export const Sidebar: React.FC<SidebarProps> = ({ activePage, setActivePage, onLogout }) => {
  const { user, isAdmin, isAnalyst, isViewer } = useAuth();

  // Role-filtered navigation definitions
  const mainNavItems = [
    { id: 'dashboard', label: 'Dashboard', icon: LayoutDashboard, roles: ['Administrator', 'Fraud Analyst', 'Management / Viewer'] },
    { id: 'analyze', label: 'Transaction Analysis', icon: FileSpreadsheet, roles: ['Administrator', 'Fraud Analyst'] },
    { id: 'fraud-analysis', label: 'Fraud Analysis', icon: Cpu, roles: ['Administrator', 'Fraud Analyst', 'Management / Viewer'] },
    { id: 'investigations', label: 'Investigations', icon: ShieldAlert, roles: ['Administrator', 'Fraud Analyst'] },
    { id: 'reports', label: 'Reports', icon: FileText, roles: ['Administrator', 'Fraud Analyst', 'Management / Viewer'] },
  ];

  const systemNavItems = [
    { id: 'models', label: 'Model Management', icon: Sliders, roles: ['Administrator'] },
    { id: 'history', label: 'Processing History', icon: Clock, roles: ['Administrator'] },
    { id: 'settings', label: 'Settings', icon: SettingsIcon, roles: ['Administrator'] },
    { id: 'help', label: 'Help Documentation', icon: HelpCircle, roles: ['Administrator', 'Fraud Analyst', 'Management / Viewer'] },
  ];

  const userRole = user?.role || 'Administrator';
  const visibleMain = mainNavItems.filter((i) => i.roles.includes(userRole));
  const visibleSystem = systemNavItems.filter((i) => i.roles.includes(userRole));

  return (
    <aside className="w-72 bg-[#090c12] border-r border-[#1e2533] flex flex-col justify-between h-full select-none shrink-0 font-sans shadow-xl">
      <div className="flex flex-col flex-1 min-h-0 overflow-y-auto">
        {/* Large Prominent Brand Header */}
        <div className="p-6 border-b border-[#1e2533] flex items-center space-x-3.5 bg-[#0e121a]">
          <div className="w-12 h-12 rounded-2xl bg-gradient-to-br from-emerald-500/25 to-emerald-950/80 border border-emerald-500/40 flex items-center justify-center text-emerald-400 shrink-0 shadow-md ring-1 ring-emerald-500/30">
            <Shield className="w-7 h-7" />
          </div>
          <div className="min-w-0">
            <h1 className="text-base font-black tracking-widest text-slate-100 uppercase font-mono truncate leading-tight">
              AEGIS FRAUD LABS
            </h1>
            <span className="text-xs text-emerald-400 font-bold tracking-wider uppercase block mt-0.5">
              FinTech Risk Engine
            </span>
          </div>
        </div>

        {/* Current Operator Profile Pill */}
        <div className="p-4 mx-4 my-4 bg-[#111622] border border-[#232b3d] rounded-xl flex items-center space-x-3.5 shadow-sm">
          <div className="w-10 h-10 rounded-xl bg-[#182030] border border-[#2d3850] flex items-center justify-center text-emerald-400 font-bold text-sm font-mono shrink-0">
            {user?.username?.slice(0, 2).toUpperCase() || 'OP'}
          </div>
          <div className="min-w-0 flex-1">
            <span className="text-sm font-bold text-slate-100 block truncate font-mono">
              {user?.username || 'Operator'}
            </span>
            <span className={`inline-block text-xs font-bold rounded-md px-2 py-0.5 mt-1 ${
              isAdmin ? 'bg-emerald-950/80 text-emerald-300 border border-emerald-700/50' :
              isAnalyst ? 'bg-amber-950/80 text-amber-300 border border-amber-700/50' :
              'bg-slate-800 text-slate-200 border border-slate-600'
            }`}>
              {userRole}
            </span>
          </div>
        </div>

        {/* Navigation Sections */}
        <nav className="p-4 space-y-6">
          {/* MAIN Section */}
          <div className="space-y-1.5">
            <span className="px-3 text-xs font-extrabold tracking-widest text-slate-400 uppercase font-mono block mb-2">
              PRIMARY MODULES
            </span>
            {visibleMain.map((item) => {
              const Icon = item.icon;
              const isActive = activePage === item.id;
              return (
                <button
                  key={item.id}
                  onClick={() => setActivePage(item.id)}
                  className={`w-full flex items-center space-x-3.5 px-3.5 py-3 rounded-xl text-sm font-semibold transition-all ${
                    isActive
                      ? 'bg-emerald-950/80 text-emerald-300 border border-emerald-500/50 font-bold shadow-md ring-1 ring-emerald-500/20'
                      : 'text-slate-300 hover:text-white hover:bg-[#141a26]'
                  }`}
                >
                  <Icon className={`w-5 h-5 shrink-0 ${isActive ? 'text-emerald-400' : 'text-slate-400'}`} />
                  <span className="truncate">{item.label}</span>
                </button>
              );
            })}
          </div>

          {/* SYSTEM or HELP Section */}
          {visibleSystem.length > 0 && (
            <div className="space-y-1.5">
              <span className="px-3 text-xs font-extrabold tracking-widest text-slate-400 uppercase font-mono block mb-2">
                {isAdmin ? 'ADMINISTRATION' : 'RESOURCES'}
              </span>
              {visibleSystem.map((item) => {
                const Icon = item.icon;
                const isActive = activePage === item.id;
                return (
                  <button
                    key={item.id}
                    onClick={() => setActivePage(item.id)}
                    className={`w-full flex items-center space-x-3.5 px-3.5 py-3 rounded-xl text-sm font-semibold transition-all ${
                      isActive
                        ? 'bg-emerald-950/80 text-emerald-300 border border-emerald-500/50 font-bold shadow-md ring-1 ring-emerald-500/20'
                        : 'text-slate-300 hover:text-white hover:bg-[#141a26]'
                    }`}
                  >
                    <Icon className={`w-5 h-5 shrink-0 ${isActive ? 'text-emerald-400' : 'text-slate-400'}`} />
                    <span className="truncate">{item.label}</span>
                  </button>
                );
              })}
            </div>
          )}
        </nav>
      </div>

      {/* Logout Footer */}
      <div className="p-4 border-t border-[#1e2533] bg-[#0c1017]">
        <button
          onClick={onLogout}
          className="w-full flex items-center space-x-3 px-4 py-3 rounded-xl text-sm font-bold text-rose-400 hover:text-rose-200 hover:bg-rose-950/40 border border-rose-900/40 hover:border-rose-700/60 transition-all shadow-sm"
        >
          <LogOut className="w-5 h-5" />
          <span>Sign Out / Lock Session</span>
        </button>
      </div>
    </aside>
  );
};
