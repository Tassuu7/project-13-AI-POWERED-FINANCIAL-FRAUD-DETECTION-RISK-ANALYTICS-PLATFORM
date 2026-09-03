import React, { useState } from 'react';
import { ShieldCheck, UserCheck, Key, Shield, ArrowRight } from 'lucide-react';
import { useAuth } from '../context/AuthContext';
import { useAppState } from '../context/AppStateContext';
import { UserRole } from '../types';
import { Button } from '../components/common/Button';

export const LoginPage: React.FC<{ onComplete?: () => void }> = ({ onComplete }) => {
  const { user, login } = useAuth();
  const { showToast } = useAppState();

  const [username, setUsername] = useState(user?.username || 'tasleema_analyst');
  const [role, setRole] = useState<UserRole>('Analyst');
  const [isLoading, setIsLoading] = useState(false);

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsLoading(true);
    try {
      await login(username, role);
      showToast(`Authenticated as ${role} (${username})`, 'success');
      if (onComplete) onComplete();
    } catch (err: any) {
      showToast(err.message || 'Authentication failed', 'error');
    } finally {
      setIsLoading(false);
    }
  };

  const quickRoles = [
    { role: 'Analyst' as UserRole, desc: 'Dataset upload, model training, fraud scoring, analytics' },
    { role: 'Reviewer' as UserRole, desc: 'Investigation desk, fraud audit notes, transaction review' },
    { role: 'Administrator' as UserRole, desc: 'Platform configuration, threshold tuning, audit trail' }
  ];

  return (
    <div className="max-w-3xl mx-auto py-10 px-4">
      <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-8 shadow-xl">
        <div className="flex items-center space-x-3 pb-6 border-b border-[#1e2432]">
          <div className="w-12 h-12 rounded-lg bg-emerald-950/80 border border-emerald-500/40 flex items-center justify-center text-emerald-400">
            <ShieldCheck className="w-7 h-7" />
          </div>
          <div>
            <h2 className="text-xl font-bold text-slate-100">Application Access &amp; Role Authorization</h2>
            <p className="text-xs text-slate-400 mt-0.5">
              Secure local session authorization for AI-Powered Financial Fraud Detection Platform
            </p>
          </div>
        </div>

        <form onSubmit={handleLogin} className="mt-6 space-y-6">
          <div>
            <label className="block text-xs font-semibold text-slate-300 mb-2 uppercase tracking-wider">
              Operator Username
            </label>
            <div className="relative">
              <input
                type="text"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                required
                className="w-full bg-[#0b0e14] border border-[#232a3b] rounded-lg px-3.5 py-2.5 text-sm text-slate-100 placeholder-slate-500 focus:outline-none focus:border-emerald-500 transition-colors"
                placeholder="e.g. shaik_analyst"
              />
              <UserCheck className="w-4 h-4 text-slate-500 absolute right-3.5 top-3" />
            </div>
          </div>

          <div>
            <label className="block text-xs font-semibold text-slate-300 mb-2 uppercase tracking-wider">
              Select Operator Role
            </label>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
              {quickRoles.map((r) => {
                const isSelected = role === r.role;
                return (
                  <button
                    key={r.role}
                    type="button"
                    onClick={() => setRole(r.role)}
                    className={`p-3.5 rounded-lg border text-left transition-all ${
                      isSelected
                        ? 'bg-emerald-950/40 border-emerald-500 text-slate-100'
                        : 'bg-[#0d1017] border-[#1f2535] text-slate-400 hover:border-[#2f384d]'
                    }`}
                  >
                    <div className="flex items-center justify-between">
                      <span className={`text-sm font-bold ${isSelected ? 'text-emerald-400' : 'text-slate-200'}`}>
                        {r.role}
                      </span>
                      {isSelected && <Shield className="w-4 h-4 text-emerald-400" />}
                    </div>
                    <p className="text-xs text-slate-400 mt-1.5 leading-relaxed">{r.desc}</p>
                  </button>
                );
              })}
            </div>
          </div>

          <div className="bg-[#0b0e14] border border-[#1e2536] rounded-lg p-4 text-xs text-slate-400 space-y-2">
            <div className="flex items-center space-x-2 text-emerald-400 font-semibold">
              <Key className="w-4 h-4" />
              <span>Local Security Architecture Notice</span>
            </div>
            <p>
              In accordance with project restrictions, all sessions operate in local-first demo mode. No external database connections or third-party identity servers are contacted. All authentication tokens reside safely in local memory.
            </p>
          </div>

          <div className="pt-2 flex justify-end">
            <Button type="submit" variant="primary" size="lg" icon={ArrowRight} isLoading={isLoading}>
              Confirm Access as {role}
            </Button>
          </div>
        </form>
      </div>
    </div>
  );
};
