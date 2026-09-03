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
    emerald: 'text-emerald-400 bg-emerald-950/60 border-emerald-800/40',
    amber: 'text-amber-400 bg-amber-950/60 border-amber-800/40',
    rose: 'text-rose-400 bg-rose-950/60 border-rose-800/40',
    slate: 'text-slate-300 bg-slate-900/60 border-slate-700/40'
  };

  return (
    <div className="bg-[#11141c] border border-[#1d2330] rounded-lg p-4 flex flex-col justify-between shadow-sm">
      <div className="flex items-center justify-between">
        <span className="text-xs font-medium text-slate-400 uppercase tracking-wider">{title}</span>
        <div className={`p-2 rounded-md border ${colorStyles[color]}`}>
          <Icon className="w-4 h-4" />
        </div>
      </div>
      <div className="mt-3">
        <div className="text-2xl font-bold text-slate-100 tracking-tight font-mono">{value}</div>
        {(subtitle || trend) && (
          <div className="mt-1 flex items-center space-x-2 text-xs">
            {trend && (
              <span className={`font-semibold ${trendUp ? 'text-emerald-400' : 'text-rose-400'}`}>
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
