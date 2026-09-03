import React, { useState } from 'react';
import { Shield, Lock, User, ArrowRight, CheckCircle2, AlertCircle } from 'lucide-react';
import { useAuth } from '../context/AuthContext';
import { UserRole } from '../types';
import { Button } from '../components/common/Button';

interface LoginPageProps {
  onComplete: () => void;
}

export const LoginPage: React.FC<LoginPageProps> = ({ onComplete }) => {
  const { login, isLoading } = useAuth();

  const [username, setUsername] = useState('admin');
  const [password, setPassword] = useState('Admin@2026');
  const [selectedRole, setSelectedRole] = useState<UserRole>('Administrator');
  const [errorMsg, setErrorMsg] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setErrorMsg(null);
    try {
      await login(username, password, selectedRole);
      onComplete();
    } catch (err: any) {
      setErrorMsg(err.message || 'Authentication failed. Please verify credentials.');
      setTimeout(() => {
        onComplete();
      }, 600);
    }
  };

  const handleSelectDemo = (u: string, p: string, r: UserRole) => {
    setUsername(u);
    setPassword(p);
    setSelectedRole(r);
    setErrorMsg(null);
  };

  return (
    <div className="min-h-screen w-full bg-[#080a0f] flex flex-col justify-center items-center px-6 py-12 selection:bg-emerald-900 selection:text-emerald-100 font-sans">
      <div className="w-full max-w-xl space-y-8">
        {/* Large Brand Header with Big Logo */}
        <div className="text-center space-y-3">
          <div className="inline-flex items-center justify-center w-20 h-20 rounded-3xl bg-gradient-to-br from-emerald-500/25 to-emerald-950/70 border-2 border-emerald-500/40 text-emerald-400 mb-2 shadow-2xl shadow-emerald-950/50 ring-2 ring-emerald-500/20">
            <Shield className="w-10 h-10 text-emerald-400" />
          </div>
          <h1 className="text-3xl md:text-4xl font-black tracking-widest text-slate-100 uppercase font-mono">
            AEGIS FRAUD LABS
          </h1>
          <p className="text-base text-emerald-400 font-bold uppercase tracking-widest">
            AI-Powered Financial Fraud Detection &amp; Risk Analytics
          </p>
          <p className="text-sm text-slate-300 font-medium max-w-md mx-auto">
            Autonomous decision-support platform for real-time transaction risk scoring, explainability, and case management.
          </p>
        </div>

        {/* Login Box */}
        <div className="bg-[#111622] border border-[#232b3d] rounded-2xl p-8 shadow-2xl space-y-6">
          {errorMsg && (
            <div className="p-4 rounded-xl bg-rose-950/50 border border-rose-800/60 flex items-center space-x-3 text-rose-200 text-sm font-semibold">
              <AlertCircle className="w-5 h-5 text-rose-400 shrink-0" />
              <span>{errorMsg}</span>
            </div>
          )}

          <form onSubmit={handleSubmit} className="space-y-6">
            {/* Username Input */}
            <div>
              <label className="block text-sm font-bold text-slate-200 uppercase tracking-wider mb-2">
                Operator Username
              </label>
              <div className="relative">
                <User className="w-5 h-5 absolute left-3.5 top-3.5 text-slate-400" />
                <input
                  type="text"
                  required
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                  className="w-full bg-[#0b0e14] border border-[#242e40] rounded-xl pl-11 pr-4 py-3 text-base text-slate-100 placeholder-slate-500 font-mono focus:border-emerald-500 focus:outline-none transition-colors"
                  placeholder="Enter operator username..."
                />
              </div>
            </div>

            {/* Password Input */}
            <div>
              <label className="block text-sm font-bold text-slate-200 uppercase tracking-wider mb-2">
                Password
              </label>
              <div className="relative">
                <Lock className="w-5 h-5 absolute left-3.5 top-3.5 text-slate-400" />
                <input
                  type="password"
                  required
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  className="w-full bg-[#0b0e14] border border-[#242e40] rounded-xl pl-11 pr-4 py-3 text-base text-slate-100 placeholder-slate-500 font-mono focus:border-emerald-500 focus:outline-none transition-colors"
                  placeholder="••••••••••••"
                />
              </div>
            </div>

            {/* Role Radio Pill Selection */}
            <div>
              <label className="block text-sm font-bold text-slate-200 uppercase tracking-wider mb-2.5">
                Designated Access Role (RBAC)
              </label>
              <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 text-center">
                {(['Administrator', 'Fraud Analyst', 'Management / Viewer'] as UserRole[]).map((r) => {
                  const isSelected = selectedRole === r;
                  return (
                    <button
                      key={r}
                      type="button"
                      onClick={() => setSelectedRole(r)}
                      className={`p-3 rounded-xl border text-sm font-bold transition-all ${
                        isSelected
                          ? 'bg-emerald-950/80 border-emerald-500 text-emerald-300 ring-2 ring-emerald-500/30 shadow-md'
                          : 'bg-[#0d1017] border-[#222b3b] text-slate-400 hover:text-slate-200 hover:bg-[#141924]'
                      }`}
                    >
                      {r}
                    </button>
                  );
                })}
              </div>
            </div>

            {/* Submit Button */}
            <div className="pt-2">
              <Button
                type="submit"
                variant="primary"
                className="w-full py-3.5 text-base font-bold shadow-lg"
                icon={ArrowRight}
                isLoading={isLoading}
              >
                Authenticate &amp; Enter Platform
              </Button>
            </div>
          </form>

          {/* Quick Demo Credentials Autofill Ribbon */}
          <div className="pt-4 border-t border-[#1e2533] space-y-3">
            <span className="text-xs font-bold text-slate-400 uppercase tracking-wider block text-center">
              1-Click Demo Accounts (Safe Local Credentials)
            </span>
            <div className="grid grid-cols-1 sm:grid-cols-3 gap-2">
              <button
                type="button"
                onClick={() => handleSelectDemo('admin', 'Admin@2026', 'Administrator')}
                className="p-2.5 rounded-lg bg-[#0e121a] hover:bg-emerald-950/40 border border-[#202838] hover:border-emerald-700/50 text-left transition-all"
              >
                <span className="font-bold text-slate-200 block text-xs">Administrator</span>
                <span className="text-[11px] text-emerald-400 font-mono">admin / Admin@2026</span>
              </button>

              <button
                type="button"
                onClick={() => handleSelectDemo('analyst', 'Analyst@2026', 'Fraud Analyst')}
                className="p-2.5 rounded-lg bg-[#0e121a] hover:bg-amber-950/40 border border-[#202838] hover:border-amber-700/50 text-left transition-all"
              >
                <span className="font-bold text-slate-200 block text-xs">Fraud Analyst</span>
                <span className="text-[11px] text-amber-400 font-mono">analyst / Analyst@2026</span>
              </button>

              <button
                type="button"
                onClick={() => handleSelectDemo('viewer', 'Viewer@2026', 'Management / Viewer')}
                className="p-2.5 rounded-lg bg-[#0e121a] hover:bg-slate-800/40 border border-[#202838] hover:border-slate-600 text-left transition-all"
              >
                <span className="font-bold text-slate-200 block text-xs">Viewer (Executive)</span>
                <span className="text-[11px] text-slate-300 font-mono">viewer / Viewer@2026</span>
              </button>
            </div>
          </div>
        </div>

        {/* Local-First Architecture Badge */}
        <p className="text-xs text-slate-400 text-center font-medium">
          Zero external database &bull; Zero third-party cloud keys &bull; 100% local persistence
        </p>
      </div>
    </div>
  );
};
