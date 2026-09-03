import React from 'react';

interface BadgeProps {
  children: React.ReactNode;
  variant?: 'low' | 'medium' | 'high' | 'neutral' | 'success';
  size?: 'sm' | 'md';
}

export const Badge: React.FC<BadgeProps> = ({
  children,
  variant = 'neutral',
  size = 'sm'
}) => {
  const variantStyles = {
    low: 'bg-emerald-950/70 text-emerald-400 border-emerald-800/50',
    medium: 'bg-amber-950/70 text-amber-400 border-amber-800/50',
    high: 'bg-rose-950/70 text-rose-400 border-rose-800/50',
    success: 'bg-emerald-950/70 text-emerald-300 border-emerald-700/50',
    neutral: 'bg-slate-900/80 text-slate-300 border-slate-700/50'
  };

  const sizeStyles = {
    sm: 'px-2 py-0.5 text-[11px]',
    md: 'px-2.5 py-1 text-xs'
  };

  return (
    <span className={`inline-flex items-center font-medium rounded border ${variantStyles[variant]} ${sizeStyles[size]}`}>
      {children}
    </span>
  );
};
