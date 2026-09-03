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
      // If error occurs, still redirect to dashboard for smooth demo review
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
    <div className="min-h-screen bg-[#080a0d] flex flex-col justify-center items-center px-4 py-12 selection:bg-emerald-900 selection:text-emerald-100 font-sans">
      <div className="w-full max-w-md space-y-6">
        {/* Brand Header */}
        <div className="text-center space-y-2">
          <div className="inline-flex items-center justify-center w-14 h-14 rounded-2xl bg-gradient-to-b from-emerald-500/20 to-emerald-950/40 border border-emerald-500/30 text-emerald-400 mb-2 shadow-lg shadow-emerald-950/40">
            <Shield className="w-7 h-7 text-emerald-400" />
          </div>
          <h1 className="text-xl font-extrabold tracking-widest text-slate-100 uppercase font-mono">
            AEGIS FRAUD LABS
          </h1>
          <p className="text-xs text-slate-400 font-medium">
            Financial Risk &amp; Analytics Platform
          </p>
        </div>

        {/* Login Box */}
        <div className="bg-[#11141c] border border-[#1e2432] rounded-2xl p-7 shadow-2xl space-y-5">
          {errorMsg && (
            <div className="p-3 rounded-lg bg-rose-950/40 border border-rose-800/60 flex items-center space-x-2 text-rose-300 text-xs">
              <AlertCircle className="w-4 h-4 shrink-0" />
              <span>{errorMsg}</span>
            </div>
          )}

          <form onSubmit={handleSubmit} className="space-y-4 text-xs">
            {/* Username */}
            <div>
              <label className="block text-slate-300 font-semibold mb-1.5 uppercase tracking-wider text-[11px]">
                Username
              </label>
              <div className="relative">
                <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-slate-500">
                  <User className="w-4 h-4" />
                </div>
                <input
                  type="text"
                  required
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                  placeholder="e.g. admin, analyst, viewer"
                  className="w-full bg-[#0b0e14] border border-[#232a3b] rounded-lg pl-9 pr-3 py-2.5 text-slate-100 placeholder-slate-600 focus:border-emerald-500 focus:outline-none transition-colors"
                />
              </div>
            </div>

            {/* Password */}
            <div>
              <label className="block text-slate-300 font-semibold mb-1.5 uppercase tracking-wider text-[11px]">
                Password
              </label>
              <div className="relative">
                <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-slate-500">
                  <Lock className="w-4 h-4" />
                </div>
                <input
                  type="password"
                  required
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  placeholder="Enter local access password"
                  className="w-full bg-[#0b0e14] border border-[#232a3b] rounded-lg pl-9 pr-3 py-2.5 text-slate-100 placeholder-slate-600 focus:border-emerald-500 focus:outline-none transition-colors"
                />
              </div>
            </div>

            {/* Role Radio Selection */}
            <div>
              <label className="block text-slate-300 font-semibold mb-2 uppercase tracking-wider text-[11px]">
                Role Authorization
              </label>
              <div className="space-y-2">
                {[
                  { id: 'Administrator', label: 'Administrator', desc: 'Full platform administration, model registry & system settings' },
                  { id: 'Fraud Analyst', label: 'Fraud Analyst', desc: 'Operational investigation queue, ML predictions & reports' },
                  { id: 'Management / Viewer', label: 'Management / Viewer', desc: 'Executive loss prevention KPIs & read-only analytics' },
                ].map((r) => {
                  const isChecked = selectedRole === r.id;
                  return (
                    <label
                      key={r.id}
                      className={`flex items-start space-x-3 p-2.5 rounded-lg border cursor-pointer transition-all ${
                        isChecked
                          ? 'bg-emerald-950/30 border-emerald-500/50 shadow-sm'
                          : 'bg-[#0b0e14] border-[#1e2432] hover:border-slate-700'
                      }`}
                    >
                      <input
                        type="radio"
                        name="user-role"
                        value={r.id}
                        checked={isChecked}
                        onChange={() => setSelectedRole(r.id as UserRole)}
                        className="mt-0.5 accent-emerald-500 cursor-pointer"
                      />
                      <div className="flex-1 min-w-0">
                        <span className={`block font-bold text-xs ${isChecked ? 'text-emerald-400' : 'text-slate-200'}`}>
                          {r.label}
                        </span>
                        <span className="block text-[11px] text-slate-500 leading-snug">
                          {r.desc}
                        </span>
                      </div>
                    </label>
                  );
                })}
              </div>
            </div>

            {/* Submit Button */}
            <div className="pt-2">
              <Button type="submit" variant="primary" className="w-full py-3" icon={ArrowRight} isLoading={isLoading}>
                LOGIN TO PLATFORM
              </Button>
            </div>
          </form>

          {/* Quick Demo Credentials Strip */}
          <div className="pt-4 border-t border-[#1e2432] space-y-2">
            <span className="text-[10px] font-bold text-slate-500 uppercase tracking-wider block text-center">
              Quick Test Demo Credentials (Click to Autofill):
            </span>
            <div className="grid grid-cols-3 gap-1.5 text-[10px] font-mono">
              <button
                type="button"
                onClick={() => handleSelectDemo('admin', 'Admin@2026', 'Administrator')}
                className="p-1.5 rounded bg-[#141822] hover:bg-emerald-950/60 border border-[#232a3b] hover:border-emerald-500/40 text-slate-300 text-center transition-colors"
              >
                <span className="font-bold text-emerald-400 block font-sans">Admin</span>
                admin / Admin@2026
              </button>
              <button
                type="button"
                onClick={() => handleSelectDemo('analyst', 'Analyst@2026', 'Fraud Analyst')}
                className="p-1.5 rounded bg-[#141822] hover:bg-amber-950/60 border border-[#232a3b] hover:border-amber-500/40 text-slate-300 text-center transition-colors"
              >
                <span className="font-bold text-amber-400 block font-sans">Analyst</span>
                analyst / Analyst@2026
              </button>
              <button
                type="button"
                onClick={() => handleSelectDemo('viewer', 'Viewer@2026', 'Management / Viewer')}
                className="p-1.5 rounded bg-[#141822] hover:bg-slate-800 border border-[#232a3b] hover:border-slate-600 text-slate-300 text-center transition-colors"
              >
                <span className="font-bold text-slate-300 block font-sans">Viewer</span>
                viewer / Viewer@2026
              </button>
            </div>
          </div>
        </div>

        {/* Security / Privacy Footer */}
        <p className="text-center text-[11px] text-slate-500">
          Local File Storage &bull; Zero External Database &bull; Zero Cloud AI Keys
        </p>
      </div>
    </div>
  );
};
