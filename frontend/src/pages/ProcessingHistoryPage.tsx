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
    <div className="w-full space-y-8 pb-16 font-sans">
      {/* Header Banner - Full Screen */}
      <div className="w-full bg-[#111622] border border-[#1e2533] rounded-2xl p-6 flex flex-col sm:flex-row sm:items-center justify-between gap-6 shadow-md">
        <div>
          <div className="flex items-center space-x-3">
            <Clock className="w-7 h-7 text-emerald-400" />
            <h3 className="text-xl font-bold text-slate-100">
              Processing History &amp; Immutable Audit Trail
            </h3>
          </div>
          <p className="text-sm text-slate-300 mt-1 font-medium">
            Local JSON audit trail tracking model deployments, batch inference executions, threshold changes, and auditor triage actions.
          </p>
        </div>
        <Button variant="secondary" size="md" icon={RefreshCw} onClick={loadHistory} isLoading={isLoading}>
          Refresh Audit Trail
        </Button>
      </div>

      {/* Category Filter Ribbon */}
      <div className="flex items-center space-x-2 text-sm overflow-x-auto pb-1 w-full">
        <span className="text-slate-400 font-bold shrink-0 mr-2">Filter Event Type:</span>
        {categories.map((c) => (
          <button
            key={c}
            onClick={() => setCategory(c)}
            className={`px-4 py-2.5 rounded-xl font-bold transition-all shrink-0 ${
              category === c
                ? 'bg-emerald-950 text-emerald-300 border border-emerald-500/60 shadow-sm'
                : 'text-slate-400 hover:text-slate-200 bg-[#111622] border border-[#1e2533]'
            }`}
          >
            {c}
          </button>
        ))}
      </div>

      {/* Audit Log Table - Full Width */}
      <div className="bg-[#111622] border border-[#1e2533] rounded-2xl overflow-hidden shadow-md w-full">
        <div className="overflow-x-auto w-full">
          <table className="w-full text-sm text-left">
            <thead className="bg-[#141a26] text-slate-200 font-bold border-b border-[#1e2533]">
              <tr>
                <th className="px-5 py-4">Timestamp (UTC)</th>
                <th className="px-5 py-4">Category</th>
                <th className="px-5 py-4">Action Summary</th>
                <th className="px-5 py-4">Operator</th>
                <th className="px-5 py-4">Status</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-[#181f2e] font-mono text-slate-200">
              {logs.map((log, idx) => (
                <tr key={idx} className="hover:bg-[#141c29] transition-colors">
                  <td className="px-5 py-4 text-xs text-slate-400 whitespace-nowrap">{log.timestamp}</td>
                  <td className="px-5 py-4">
                    <span className="px-2.5 py-1 rounded-lg text-xs font-black bg-slate-800 text-slate-300 border border-slate-700">
                      {log.category}
                    </span>
                  </td>
                  <td className="px-5 py-4 text-slate-100 font-sans font-medium">{log.action}</td>
                  <td className="px-5 py-4 text-emerald-400 font-bold">{log.user || 'system'}</td>
                  <td className="px-5 py-4">
                    <span className="inline-flex items-center space-x-1.5 text-xs text-emerald-400 font-bold">
                      <CheckCircle2 className="w-4 h-4" />
                      <span>{log.status || 'SUCCESS'}</span>
                    </span>
                  </td>
                </tr>
              ))}
              {logs.length === 0 && (
                <tr>
                  <td colSpan={5} className="p-12 text-center text-slate-400 font-sans text-sm">
                    No audit records recorded in this category.
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
