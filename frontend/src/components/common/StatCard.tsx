import React from 'react';
import { LucideIcon } from 'lucide-react';

interface StatCardProps {
  title: string;
  value: string | number;
  subtitle?: string;
  icon: LucideIcon;
  trend?: string;
  trendUp?: boolean;
  color?: 'emerald' | 'amber' | 'rose' | 'slate';
}

export const StatCard: React.FC<StatCardProps> = ({
  title,
  value,
  subtitle,
  icon: Icon,
  trend,
  trendUp,
  color = 'slate'
}) => {
  const colorStyles = {
    emerald: 'text-emerald-400 bg-emerald-950/80 border-emerald-700/60',
    amber: 'text-amber-400 bg-amber-950/80 border-amber-700/60',
    rose: 'text-rose-400 bg-rose-950/80 border-rose-700/60',
    slate: 'text-slate-200 bg-slate-900/80 border-slate-700/60'
  };

  return (
    <div className="bg-[#111622] border border-[#1e2533] rounded-2xl p-5 flex flex-col justify-between shadow-md hover:border-slate-600 transition-all">
      <div className="flex items-center justify-between">
        <span className="text-xs md:text-sm font-extrabold text-slate-300 uppercase tracking-wider">{title}</span>
        <div className={`p-2.5 rounded-xl border ${colorStyles[color]}`}>
          <Icon className="w-5 h-5" />
        </div>
      </div>
      <div className="mt-4">
        <div className="text-3xl font-black text-slate-100 tracking-tight font-mono">{value}</div>
        {(subtitle || trend) && (
          <div className="mt-1.5 flex items-center space-x-2 text-xs font-medium">
            {trend && (
              <span className={`font-bold ${trendUp ? 'text-emerald-400' : 'text-rose-400'}`}>
                {trend}
              </span>
            )}
            {subtitle && <span className="text-slate-400">{subtitle}</span>}
          </div>
        )}
      </div>
    </div>
  );
};
