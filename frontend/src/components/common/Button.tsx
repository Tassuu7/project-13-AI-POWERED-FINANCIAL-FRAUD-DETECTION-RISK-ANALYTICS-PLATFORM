import React from 'react';
import { LucideIcon } from 'lucide-react';

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'secondary' | 'danger' | 'ghost';
  size?: 'sm' | 'md' | 'lg';
  icon?: LucideIcon;
  isLoading?: boolean;
}

export const Button: React.FC<ButtonProps> = ({
  children,
  variant = 'primary',
  size = 'md',
  icon: Icon,
  isLoading = false,
  className = '',
  disabled,
  ...props
}) => {
  const variantStyles = {
    // Primary is Emerald Green (Strictly no blue)
    primary: 'bg-emerald-600 hover:bg-emerald-500 text-slate-950 font-semibold shadow-sm focus:ring-emerald-500',
    secondary: 'bg-[#181d27] hover:bg-[#202734] text-slate-200 border border-[#273142] focus:ring-slate-500',
    danger: 'bg-rose-600 hover:bg-rose-500 text-white font-medium focus:ring-rose-500',
    ghost: 'bg-transparent hover:bg-[#181d27] text-slate-300 focus:ring-slate-500'
  };

  const sizeStyles = {
    sm: 'px-2.5 py-1 text-xs',
    md: 'px-3.5 py-1.5 text-sm',
    lg: 'px-5 py-2 text-base'
  };

  return (
    <button
      className={`inline-flex items-center justify-center space-x-2 rounded-md transition-colors focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-[#0d1015] disabled:opacity-50 disabled:cursor-not-allowed ${variantStyles[variant]} ${sizeStyles[size]} ${className}`}
      disabled={disabled || isLoading}
      {...props}
    >
      {isLoading ? (
        <div className="w-4 h-4 border-2 border-current border-t-transparent rounded-full animate-spin" />
      ) : Icon ? (
        <Icon className="w-4 h-4 shrink-0" />
      ) : null}
      <span>{children}</span>
    </button>
  );
};
