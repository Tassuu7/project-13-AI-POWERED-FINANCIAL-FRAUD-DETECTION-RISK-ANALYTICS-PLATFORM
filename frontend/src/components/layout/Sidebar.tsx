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
    { id: 'help', label: 'Help', icon: HelpCircle, roles: ['Administrator', 'Fraud Analyst', 'Management / Viewer'] },
  ];

  const userRole = user?.role || 'Administrator';
  const visibleMain = mainNavItems.filter((i) => i.roles.includes(userRole));
  const visibleSystem = systemNavItems.filter((i) => i.roles.includes(userRole));

  return (
    <aside className="w-64 bg-[#0a0d13] border-r border-[#1a202c] flex flex-col justify-between h-full select-none shrink-0 font-sans">
      <div className="flex flex-col flex-1 min-h-0 overflow-y-auto">
        {/* Brand Header */}
        <div className="p-5 border-b border-[#1a202c] flex items-center space-x-3">
          <div className="w-9 h-9 rounded-xl bg-gradient-to-br from-emerald-500/20 to-emerald-950/60 border border-emerald-500/30 flex items-center justify-center text-emerald-400 shrink-0 shadow-sm">
            <Shield className="w-5 h-5" />
          </div>
          <div className="min-w-0">
            <h1 className="text-xs font-black tracking-widest text-slate-100 uppercase font-mono truncate">
              AEGIS FRAUD LABS
            </h1>
            <span className="text-[10px] text-slate-500 font-medium block">
              Risk &amp; Analytics Platform
            </span>
          </div>
        </div>

        {/* Current Operator Profile Pill */}
        <div className="p-3 mx-3 my-3 bg-[#11141c] border border-[#1e2432] rounded-xl flex items-center space-x-3">
          <div className="w-8 h-8 rounded-lg bg-[#181d28] border border-[#252e40] flex items-center justify-center text-emerald-400 font-bold text-xs font-mono shrink-0">
            {user?.username?.slice(0, 2).toUpperCase() || 'OP'}
          </div>
          <div className="min-w-0 flex-1">
            <span className="text-xs font-bold text-slate-200 block truncate font-mono">
              {user?.username || 'Operator'}
            </span>
            <span className={`inline-block text-[10px] font-bold rounded px-1.5 py-0.2 mt-0.5 ${
              isAdmin ? 'bg-emerald-950 text-emerald-400 border border-emerald-800/40' :
              isAnalyst ? 'bg-amber-950 text-amber-400 border border-amber-800/40' :
              'bg-slate-800 text-slate-300 border border-slate-700'
            }`}>
              {userRole}
            </span>
          </div>
        </div>

        {/* Navigation Sections */}
        <nav className="p-3 space-y-5">
          {/* MAIN Section */}
          <div className="space-y-1">
            <span className="px-3 text-[10px] font-bold tracking-wider text-slate-500 uppercase font-mono">
              MAIN
            </span>
            {visibleMain.map((item) => {
              const Icon = item.icon;
              const isActive = activePage === item.id;
              return (
                <button
                  key={item.id}
                  onClick={() => setActivePage(item.id)}
                  className={`w-full flex items-center space-x-3 px-3 py-2.5 rounded-lg text-xs font-medium transition-all ${
                    isActive
                      ? 'bg-emerald-950/60 text-emerald-400 border border-emerald-500/30 font-semibold shadow-sm'
                      : 'text-slate-400 hover:text-slate-200 hover:bg-[#121620]'
                  }`}
                >
                  <Icon className={`w-4 h-4 shrink-0 ${isActive ? 'text-emerald-400' : 'text-slate-500'}`} />
                  <span className="truncate">{item.label}</span>
                </button>
              );
            })}
          </div>

          {/* SYSTEM or HELP Section */}
          {visibleSystem.length > 0 && (
            <div className="space-y-1">
              <span className="px-3 text-[10px] font-bold tracking-wider text-slate-500 uppercase font-mono">
                {isAdmin ? 'SYSTEM' : 'HELP'}
              </span>
              {visibleSystem.map((item) => {
                const Icon = item.icon;
                const isActive = activePage === item.id;
                return (
                  <button
                    key={item.id}
                    onClick={() => setActivePage(item.id)}
                    className={`w-full flex items-center space-x-3 px-3 py-2.5 rounded-lg text-xs font-medium transition-all ${
                      isActive
                        ? 'bg-emerald-950/60 text-emerald-400 border border-emerald-500/30 font-semibold shadow-sm'
                        : 'text-slate-400 hover:text-slate-200 hover:bg-[#121620]'
                    }`}
                  >
                    <Icon className={`w-4 h-4 shrink-0 ${isActive ? 'text-emerald-400' : 'text-slate-500'}`} />
                    <span className="truncate">{item.label}</span>
                  </button>
                );
              })}
            </div>
          )}
        </nav>
      </div>

      {/* Logout Footer */}
      <div className="p-3 border-t border-[#1a202c]">
        <button
          onClick={onLogout}
          className="w-full flex items-center space-x-3 px-3 py-2.5 rounded-lg text-xs font-semibold text-rose-400 hover:text-rose-300 hover:bg-rose-950/30 border border-transparent hover:border-rose-800/40 transition-all"
        >
          <LogOut className="w-4 h-4" />
          <span>Sign Out</span>
        </button>
      </div>
    </aside>
  );
};
