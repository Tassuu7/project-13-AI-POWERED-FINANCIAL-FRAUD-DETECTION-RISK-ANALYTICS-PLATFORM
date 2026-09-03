import React, { useState, useEffect } from 'react';
import { Clock, CheckCircle2, AlertCircle, RefreshCw, Filter } from 'lucide-react';
import { api } from '../services/api';
import { AuditLogItem } from '../types';
import { Button } from '../components/common/Button';

export const ProcessingHistoryPage: React.FC = () => {
  const [logs, setLogs] = useState<AuditLogItem[]>([]);
  const [category, setCategory] = useState<string>('ALL');
  const [isLoading, setIsLoading] = useState(false);

  const loadHistory = async () => {
    setIsLoading(true);
    try {
      const data = await api.getHistory(category);
      setLogs(data);
    } catch (err) {
      console.warn('Error loading history:', err);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    loadHistory();
  }, [category]);

  const categories = ['ALL', 'DATASET', 'MODEL', 'PREDICTION', 'REVIEW', 'EXPORT', 'SETTINGS'];

  return (
    <div className="space-y-6 max-w-6xl mx-auto pb-12">
      {/* Header Banner */}
      <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-5 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2">
            <Clock className="w-5 h-5 text-emerald-400" />
            <h3 className="text-base font-bold text-slate-100">
              Processing History &amp; Immutable Audit Trail
            </h3>
          </div>
          <p className="text-xs text-slate-400 mt-0.5">
            Local JSON audit trail tracking model deployments, batch inference executions, and auditor triage actions.
          </p>
        </div>
        <Button variant="secondary" size="sm" icon={RefreshCw} onClick={loadHistory} isLoading={isLoading}>
          Refresh Audit Trail
        </Button>
      </div>

      {/* Category Filter Ribbon */}
      <div className="flex items-center space-x-2 text-xs overflow-x-auto pb-1">
        <span className="text-slate-400 font-semibold shrink-0">Filter Event:</span>
        {categories.map((c) => (
          <button
            key={c}
            onClick={() => setCategory(c)}
            className={`px-3 py-1.5 rounded-lg font-medium transition-colors shrink-0 ${
              category === c
                ? 'bg-emerald-950/60 text-emerald-400 border border-emerald-500/40 font-bold'
                : 'text-slate-400 hover:text-slate-200 bg-[#11141c] border border-[#1e2432]'
            }`}
          >
            {c}
          </button>
        ))}
      </div>

      {/* Audit Log Table */}
      <div className="bg-[#11141c] border border-[#1e2432] rounded-xl overflow-hidden shadow-sm">
        <div className="overflow-x-auto">
          <table className="w-full text-xs text-left">
            <thead className="bg-[#161a24] text-slate-300 font-semibold border-b border-[#1e2432]">
              <tr>
                <th className="px-4 py-3">Audit ID</th>
                <th className="px-4 py-3">Timestamp</th>
                <th className="px-4 py-3">Category</th>
                <th className="px-4 py-3">Action Description</th>
                <th className="px-4 py-3">Operator</th>
                <th className="px-4 py-3 text-right">Result</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-[#181d28] font-mono text-slate-300">
              {logs.map((log) => {
                const isSuccess = log.status === 'SUCCESS';

                return (
                  <tr key={log.id} className="hover:bg-[#141822] transition-colors">
                    <td className="px-4 py-3 font-bold text-slate-200">{log.id}</td>
                    <td className="px-4 py-3 text-slate-400">{log.timestamp}</td>
                    <td className="px-4 py-3 font-sans">
                      <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-[#171c26] text-slate-300 border border-[#222938]">
                        {log.category}
                      </span>
                    </td>
                    <td className="px-4 py-3 font-sans text-slate-200">{log.action}</td>
                    <td className="px-4 py-3 font-sans text-emerald-400 font-medium">{log.user}</td>
                    <td className="px-4 py-3 text-right font-sans">
                      <span className={`inline-flex items-center space-x-1 text-[11px] font-bold ${
                        isSuccess ? 'text-emerald-400' : 'text-amber-400'
                      }`}>
                        {isSuccess ? <CheckCircle2 className="w-3.5 h-3.5" /> : <AlertCircle className="w-3.5 h-3.5" />}
                        <span>{log.status}</span>
                      </span>
                    </td>
                  </tr>
                );
              })}

              {logs.length === 0 && (
                <tr>
                  <td colSpan={6} className="px-4 py-8 text-center text-slate-500 font-sans">
                    No processing events recorded for category '{category}'.
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};
