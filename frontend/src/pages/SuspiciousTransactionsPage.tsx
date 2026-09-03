import React, { useState, useEffect } from 'react';
import { AlertTriangle, ShieldAlert, CheckCircle2, Download, RefreshCw, Edit3, X, User } from 'lucide-react';
import { useAppState } from '../context/AppStateContext';
import { useAuth } from '../context/AuthContext';
import { api } from '../services/api';
import { SuspiciousItem, ReviewStatus } from '../types';
import { Button } from '../components/common/Button';

export const SuspiciousTransactionsPage: React.FC = () => {
  const { showToast } = useAppState();
  const { user } = useAuth();

  const [items, setItems] = useState<SuspiciousItem[]>([]);
  const [filterStatus, setFilterStatus] = useState<string>('All');
  const [isLoading, setIsLoading] = useState(false);
  const [activeItemForReview, setActiveItemForReview] = useState<SuspiciousItem | null>(null);

  // Review modal state
  const [newStatus, setNewStatus] = useState<ReviewStatus>('Under Review');
  const [newNotes, setNewNotes] = useState('');
  const [isUpdating, setIsUpdating] = useState(false);

  const loadSuspicious = async () => {
    setIsLoading(true);
    try {
      const data = await api.listSuspicious(filterStatus);
      setItems(data);
    } catch (err) {
      console.warn('Error loading suspicious queue:', err);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    loadSuspicious();
  }, [filterStatus]);

  const handleOpenReview = (item: SuspiciousItem) => {
    setActiveItemForReview(item);
    setNewStatus(item.review_status);
    setNewNotes('');
  };

  const handleSaveReview = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!activeItemForReview) return;
    setIsUpdating(true);
    try {
      await api.updateReview(activeItemForReview.transaction_id, {
        review_status: newStatus,
        review_notes: newNotes,
        analyst_name: user?.username || 'Analyst_Desk',
      });
      showToast(`Updated ${activeItemForReview.transaction_id} to '${newStatus}'`, 'success');
      setActiveItemForReview(null);
      loadSuspicious();
    } catch (err: any) {
      showToast(err.message || 'Review update failed', 'error');
    } finally {
      setIsUpdating(false);
    }
  };

  const handleExport = async () => {
    try {
      const res = await api.exportSuspicious();
      showToast(`Exported queue to ${res.filename}`, 'success');
      window.open(`http://localhost:8000/api/exports/download/${res.filename}`, '_blank');
    } catch (err: any) {
      showToast(err.message || 'Export failed', 'error');
    }
  };

  return (
    <div className="space-y-6 max-w-7xl mx-auto pb-12">
      {/* Header Banner */}
      <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-5 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2">
            <AlertTriangle className="w-5 h-5 text-rose-500" />
            <h3 className="text-base font-bold text-slate-100">
              Suspicious Transactions &amp; Fraud Investigation Desk
            </h3>
          </div>
          <p className="text-xs text-slate-400 mt-0.5">
            Active triaged queue of high-risk transactions awaiting auditor review, secondary authentication, or freeze.
          </p>
        </div>

        <div className="flex items-center space-x-3">
          <Button variant="secondary" size="sm" icon={Download} onClick={handleExport}>
            Export Queue CSV
          </Button>
          <Button variant="secondary" size="sm" icon={RefreshCw} onClick={loadSuspicious} isLoading={isLoading}>
            Refresh
          </Button>
        </div>
      </div>

      {/* Filter Ribbon */}
      <div className="flex items-center space-x-2 text-xs">
        <span className="text-slate-400 font-semibold">Filter Status:</span>
        {['All', 'New', 'Under Review', 'Investigating', 'Cleared', 'Confirmed Suspicious'].map((st) => (
          <button
            key={st}
            onClick={() => setFilterStatus(st)}
            className={`px-3 py-1.5 rounded-lg font-medium transition-colors ${
              filterStatus === st
                ? 'bg-emerald-950/60 text-emerald-400 border border-emerald-500/40 font-bold'
                : 'text-slate-400 hover:text-slate-200 bg-[#11141c] border border-[#1e2432]'
            }`}
          >
            {st}
          </button>
        ))}
      </div>

      {/* Main Table */}
      <div className="bg-[#11141c] border border-[#1e2432] rounded-xl overflow-hidden shadow-sm">
        <div className="overflow-x-auto">
          <table className="w-full text-xs text-left">
            <thead className="bg-[#161a24] text-slate-300 font-semibold border-b border-[#1e2432]">
              <tr>
                <th className="px-4 py-3">Tx ID</th>
                <th className="px-4 py-3">Customer</th>
                <th className="px-4 py-3">Amount (INR)</th>
                <th className="px-4 py-3">Timestamp</th>
                <th className="px-4 py-3">Radial Dist</th>
                <th className="px-4 py-3">Risk Score</th>
                <th className="px-4 py-3">Review Status</th>
                <th className="px-4 py-3">Assigned Auditor</th>
                <th className="px-4 py-3 text-right">Audit Action</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-[#181d28] font-mono text-slate-300">
              {items.map((item) => (
                <tr key={item.transaction_id} className="hover:bg-[#141822] transition-colors">
                  <td className="px-4 py-3 font-bold text-slate-200">{item.transaction_id}</td>
                  <td className="px-4 py-3 text-slate-400">{item.customer_id}</td>
                  <td className="px-4 py-3 font-bold text-rose-400">
                    ₹{Number(item.amount || 0).toLocaleString('en-IN', { minimumFractionDigits: 2 })}
                  </td>
                  <td className="px-4 py-3 text-slate-400">{item.timestamp}</td>
                  <td className="px-4 py-3">{item.location}</td>
                  <td className="px-4 py-3">
                    <span className="text-rose-400 font-bold">{item.risk_score} / 100</span>
                  </td>
                  <td className="px-4 py-3 font-sans">
                    <span className={`px-2 py-0.5 rounded text-[10px] font-bold ${
                      item.review_status === 'New' ? 'bg-rose-950 text-rose-400 border border-rose-800/40' :
                      item.review_status === 'Under Review' ? 'bg-amber-950 text-amber-400 border border-amber-800/40' :
                      item.review_status === 'Cleared' ? 'bg-emerald-950 text-emerald-400 border border-emerald-800/40' :
                      'bg-red-950 text-red-300 border border-red-700/60'
                    }`}>
                      {item.review_status}
                    </span>
                  </td>
                  <td className="px-4 py-3 font-sans text-slate-300">{item.assigned_analyst || 'Unassigned'}</td>
                  <td className="px-4 py-3 text-right">
                    <Button size="sm" variant="primary" icon={Edit3} onClick={() => handleOpenReview(item)}>
                      Review
                    </Button>
                  </td>
                </tr>
              ))}

              {items.length === 0 && (
                <tr>
                  <td colSpan={9} className="px-4 py-8 text-center text-slate-500 font-sans">
                    No suspicious items found in current status filter.
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>

      {/* Review Modal */}
      {activeItemForReview && (
        <div className="fixed inset-0 bg-black/75 backdrop-blur-sm flex items-center justify-center p-4 z-50 animate-in fade-in duration-150">
          <div className="bg-[#11141c] border border-[#1e2432] rounded-xl max-w-lg w-full p-6 space-y-4 shadow-2xl">
            <div className="flex items-center justify-between pb-3 border-b border-[#1e2432]">
              <div className="flex items-center space-x-2">
                <ShieldAlert className="w-5 h-5 text-rose-500" />
                <h4 className="text-sm font-bold text-slate-100 font-mono">
                  Audit Review: {activeItemForReview.transaction_id}
                </h4>
              </div>
              <button
                onClick={() => setActiveItemForReview(null)}
                className="text-slate-400 hover:text-slate-200 p-1"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            <form onSubmit={handleSaveReview} className="space-y-4 text-xs">
              <div className="grid grid-cols-2 gap-3 bg-[#0b0e14] p-3 rounded-lg border border-[#1e2432]">
                <div>
                  <span className="text-slate-500 block">Customer ID</span>
                  <span className="font-mono font-bold text-slate-200">{activeItemForReview.customer_id}</span>
                </div>
                <div>
                  <span className="text-slate-500 block">Transaction Amount</span>
                  <span className="font-mono font-bold text-rose-400">
                    ₹{Number(activeItemForReview.amount).toLocaleString('en-IN', { minimumFractionDigits: 2 })}
                  </span>
                </div>
                <div>
                  <span className="text-slate-500 block">Risk Score</span>
                  <span className="font-mono font-bold text-rose-400">{activeItemForReview.risk_score} / 100</span>
                </div>
                <div>
                  <span className="text-slate-500 block">Device</span>
                  <span className="font-sans text-slate-200 truncate block">{activeItemForReview.device_type}</span>
                </div>
              </div>

              <div>
                <label className="block font-semibold text-slate-300 mb-1.5 uppercase tracking-wider">
                  Update Investigation Status
                </label>
                <select
                  value={newStatus}
                  onChange={(e) => setNewStatus(e.target.value as ReviewStatus)}
                  className="w-full bg-[#0b0e14] border border-[#232a3b] rounded-lg px-3 py-2 text-slate-100 font-sans focus:border-emerald-500 focus:outline-none"
                >
                  <option value="New">New</option>
                  <option value="Under Review">Under Review</option>
                  <option value="Investigating">Investigating</option>
                  <option value="Cleared">Cleared (False Positive)</option>
                  <option value="Confirmed Suspicious">Confirmed Suspicious (Freeze Card)</option>
                </select>
              </div>

              <div>
                <label className="block font-semibold text-slate-300 mb-1.5 uppercase tracking-wider">
                  Analyst Investigation Notes
                </label>
                <textarea
                  rows={3}
                  value={newNotes}
                  onChange={(e) => setNewNotes(e.target.value)}
                  placeholder="Record customer contact notes, step-up verification outcomes, or rationale..."
                  className="w-full bg-[#0b0e14] border border-[#232a3b] rounded-lg p-2.5 text-slate-100 font-sans focus:border-emerald-500 focus:outline-none"
                />
              </div>

              {activeItemForReview.review_notes && (
                <div className="bg-[#0b0e14] p-3 rounded-lg border border-[#1e2432] text-slate-400 max-h-28 overflow-y-auto font-mono text-[11px]">
                  <span className="text-slate-500 font-sans font-bold block mb-1">Previous Notes:</span>
                  <pre className="whitespace-pre-wrap font-mono">{activeItemForReview.review_notes}</pre>
                </div>
              )}

              <div className="pt-2 flex justify-end space-x-3">
                <Button type="button" variant="secondary" onClick={() => setActiveItemForReview(null)}>
                  Cancel
                </Button>
                <Button type="submit" variant="primary" isLoading={isUpdating}>
                  Save Audit Record
                </Button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};
