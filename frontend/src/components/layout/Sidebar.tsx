import React from 'react';
import {
  LayoutDashboard,
  UploadCloud,
  Cpu,
  CheckSquare,
  Sliders,
  GitBranch,
  BarChart2,
  Activity,
  Award,
  Search,
  ShieldAlert,
  Database,
  AlertTriangle,
  HelpCircle,
  FileText,
  Download,
  Clock,
  Settings as SettingsIcon,
  BookOpen,
  LogIn,
  ShieldCheck
} from 'lucide-react';

interface SidebarProps {
  activePage: string;
  setActivePage: (page: string) => void;
}

export const Sidebar: React.FC<SidebarProps> = ({ activePage, setActivePage }) => {
  const navSections = [
    {
      title: 'CORE PLATFORM',
      items: [
        { id: 'dashboard', label: 'Main Dashboard', icon: LayoutDashboard },
        { id: 'login', label: 'Access & Role Auth', icon: LogIn },
      ]
    },
    {
      title: 'DATA ENGINEERING',
      items: [
        { id: 'upload', label: 'Data Upload', icon: UploadCloud },
        { id: 'generator', label: 'Synthetic Generator', icon: Cpu },
        { id: 'validation', label: 'Data Validation', icon: CheckSquare },
        { id: 'preprocessing', label: 'Preprocessing Pipeline', icon: Sliders },
        { id: 'features', label: 'Feature Engineering', icon: GitBranch },
        { id: 'eda', label: 'Exploratory EDA', icon: BarChart2 },
      ]
    },
    {
      title: 'ML & PREDICTION',
      items: [
        { id: 'training', label: 'Model Training', icon: Activity },
        { id: 'evaluation', label: 'Model Evaluation', icon: Award },
        { id: 'prediction', label: 'Fraud Prediction', icon: Search },
        { id: 'risk', label: 'Risk Scoring Engine', icon: ShieldAlert },
        { id: 'explainability', label: 'Explainability & SHAP', icon: HelpCircle },
      ]
    },
    {
      title: 'INVESTIGATION & OPS',
      items: [
        { id: 'transactions', label: 'Transaction Explorer', icon: Database },
        { id: 'suspicious', label: 'Suspicious Desk', icon: AlertTriangle },
        { id: 'reports', label: 'Report Generation', icon: FileText },
        { id: 'exports', label: 'Export Center', icon: Download },
      ]
    },
    {
      title: 'SYSTEM & AUDIT',
      items: [
        { id: 'history', label: 'Processing History', icon: Clock },
        { id: 'settings', label: 'Settings & Thresholds', icon: SettingsIcon },
        { id: 'help', label: 'Help & Documentation', icon: BookOpen },
      ]
    }
  ];

  return (
    <aside className="w-64 bg-[#0a0d13] border-r border-[#1a202c] flex flex-col h-screen shrink-0 select-none">
      {/* Brand Header */}
      <div className="p-4 border-b border-[#1a202c] flex items-center space-x-3 bg-[#0d1017]">
        <div className="w-9 h-9 rounded-lg bg-emerald-950/80 border border-emerald-500/30 flex items-center justify-center text-emerald-400 shrink-0 shadow-sm">
          <ShieldCheck className="w-5 h-5 text-emerald-400" />
        </div>
        <div className="overflow-hidden">
          <h1 className="text-sm font-bold text-slate-100 truncate tracking-tight">
            AEGIS FRAUD LABS
          </h1>
          <p className="text-[11px] font-mono text-emerald-500/90 font-medium">
            Risk &amp; Analytics v1.0
          </p>
        </div>
      </div>

      {/* Nav List */}
      <nav className="flex-1 overflow-y-auto px-3 py-4 space-y-5 text-xs">
        {navSections.map((section) => (
          <div key={section.title}>
            <div className="px-3 mb-1.5 text-[10px] font-semibold text-slate-400 tracking-wider">
              {section.title}
            </div>
            <div className="space-y-0.5">
              {section.items.map((item) => {
                const Icon = item.icon;
                const isActive = activePage === item.id;
                return (
                  <button
                    key={item.id}
                    onClick={() => setActivePage(item.id)}
                    className={`w-full flex items-center space-x-2.5 px-3 py-2 rounded-md font-medium transition-all text-left ${
                      isActive
                        ? 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/25 shadow-sm font-semibold'
                        : 'text-slate-400 hover:text-slate-200 hover:bg-[#141822]'
                    }`}
                  >
                    <Icon className={`w-4 h-4 shrink-0 ${isActive ? 'text-emerald-400' : 'text-slate-400'}`} />
                    <span className="truncate">{item.label}</span>
                  </button>
                );
              })}
            </div>
          </div>
        ))}
      </nav>

      {/* Footer Info */}
      <div className="p-3 border-t border-[#1a202c] bg-[#0d1017] text-[11px] text-slate-400 flex items-center justify-between">
        <div className="flex items-center space-x-2">
          <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
          <span>Engine Online</span>
        </div>
        <span className="font-mono text-[10px] text-slate-400">Local-First</span>
      </div>
    </aside>
  );
};
