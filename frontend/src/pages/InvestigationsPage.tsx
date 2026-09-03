import React, { useState, useEffect } from 'react';
import {
  ShieldAlert,
  AlertTriangle,
  CheckCircle2,
  Download,
  RefreshCw,
  Edit3,
  X,
  Search,
  User,
  Clock,
  MapPin,
  Smartphone,
  CreditCard,
  Save,
  Lock
} from 'lucide-react';
import { useAppState } from '../context/AppStateContext';
import { useAuth } from '../context/AuthContext';
import { api } from '../services/api';
import { SuspiciousItem, ReviewStatus } from '../types';
import { Button } from '../components/common/Button';

export const InvestigationsPage: React.FC = () => {
  const { showToast } = useAppState();
  const { user, isViewer } = useAuth();

  const [items, setItems] = useState<SuspiciousItem[]>([]);
  const [filterStatus, setFilterStatus] = useState<string>('All');
  const [searchQuery, setSearchQuery] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [selectedCase, setSelectedCase] = useState<SuspiciousItem | null>(null);

  // Modal editing state
  const [newStatus, setNewStatus] = useState<ReviewStatus>('Under Review');
  const [newNotes, setNewNotes] = useState('');
  const [isSaving, setIsSaving] = useState(false);

  const loadSuspicious = async () => {
    setIsLoading(true);
    try {
      const data = await api.listSuspicious(filterStatus);
      setItems(data);
    } catch (err) {
      console.warn('Error loading investigations queue:', err);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    loadSuspicious();
  }, [filterStatus]);

  const handleOpenCase = (item: SuspiciousItem) => {
    setSelectedCase(item);
    setNewStatus(item.review_status);
    setNewNotes('');
  };

  const handleSaveInvestigation = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!selectedCase) return;
    if (isViewer) {
      showToast('Viewer accounts have read-only access and cannot modify investigations.', 'error');
      return;
    }

    setIsSaving(true);
    try {
      await api.updateReview(selectedCase.transaction_id, {
        review_status: newStatus,
        review_notes: newNotes,
        analyst_name: user?.username || 'Analyst_Desk',
      });
      showToast(`Saved review for ${selectedCase.transaction_id}: Status -> ${newStatus}`, 'success');
      setSelectedCase(null);
      loadSuspicious();
    } catch (err: any) {
      showToast(err.message || 'Update failed', 'error');
    } finally {
      setIsSaving(false);
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

  const filteredItems = items.filter((item) => {
    if (!searchQuery) return true;
    const q = searchQuery.toLowerCase();
    return (
      item.transaction_id.toLowerCase().includes(q) ||
      item.customer_id.toLowerCase().includes(q) ||
      (item.location && item.location.toLowerCase().includes(q))
    );
  });

  return (
    <div className="space-y-6 max-w-7xl mx-auto pb-12 font-sans">
      {/* Top Banner */}
      <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-5 flex flex-col md:flex-row md:items-center justify-between gap-4 shadow-sm">
        <div>
          <div className="flex items-center space-x-2">
            <ShieldAlert className="w-5 h-5 text-rose-400" />
            <h3 className="text-base font-bold text-slate-100">
              Fraud Investigation Desk &amp; Case Management
            </h3>
          </div>
          <p className="text-xs text-slate-400 mt-0.5">
            Triaged queue of high-risk transactions requiring auditor evaluation, step-up authentication, card holds, or clearance.
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

      {/* Filter and Search Ribbon */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
        <div className="flex items-center space-x-1.5 overflow-x-auto text-xs pb-1">
          {['All', 'New', 'Under Review', 'Investigating', 'Cleared', 'Confirmed Suspicious'].map((st) => (
            <button
              key={st}
              onClick={() => setFilterStatus(st)}
              className={`px-3 py-1.5 rounded-lg font-medium transition-colors shrink-0 ${
                filterStatus === st
                  ? 'bg-emerald-950/60 text-emerald-400 border border-emerald-500/40 font-bold'
                  : 'text-slate-400 hover:text-slate-200 bg-[#11141c] border border-[#1e2432]'
              }`}
            >
              {st}
            </button>
          ))}
        </div>

        <div className="relative w-full sm:w-64">
          <Search className="w-3.5 h-3.5 absolute left-3 top-2.5 text-slate-500" />
          <input
            type="text"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder="Search Tx ID, Customer..."
            className="w-full bg-[#11141c] border border-[#1e2432] rounded-lg pl-8 pr-3 py-1.5 text-xs text-slate-200 focus:border-emerald-500 focus:outline-none"
          />
        </div>
      </div>

      {/* Main Investigations Table matching prompt Sections 23-24 */}
      <div className="bg-[#11141c] border border-[#1e2432] rounded-xl overflow-hidden shadow-sm">
        <div className="overflow-x-auto">
          <table className="w-full text-xs text-left">
            <thead className="bg-[#161a24] text-slate-300 font-semibold border-b border-[#1e2432]">
              <tr>
                <th className="px-4 py-3">Transaction ID</th>
                <th className="px-4 py-3">Customer</th>
                <th className="px-4 py-3">Amount (INR)</th>
                <th className="px-4 py-3">Risk Score</th>
                <th className="px-4 py-3">Risk Level</th>
                <th className="px-4 py-3">Location / Device</th>
                <th className="px-4 py-3">Timestamp</th>
                <th className="px-4 py-3">Status</th>
                <th className="px-4 py-3 text-right">Investigation Action</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-[#181d28] font-mono text-slate-300">
              {filteredItems.map((item) => (
                <tr key={item.transaction_id} className="hover:bg-[#141822] transition-colors">
                  <td className="px-4 py-3 font-bold text-slate-100">{item.transaction_id}</td>
                  <td className="px-4 py-3 text-slate-400">{item.customer_id}</td>
                  <td className="px-4 py-3 font-bold text-rose-400">
                    ₹{Number(item.amount || 0).toLocaleString('en-IN', { minimumFractionDigits: 2 })}
                  </td>
                  <td className="px-4 py-3">
                    <span className="font-bold text-rose-400">{item.risk_score} / 100</span>
                  </td>
                  <td className="px-4 py-3 font-sans">
                    <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-rose-950 text-rose-400 border border-rose-800/40">
                      {item.risk_level || 'HIGH'}
                    </span>
                  </td>
                  <td className="px-4 py-3 font-sans text-slate-300">
                    <div>{item.location}</div>
                    <div className="text-[10px] text-slate-500">{item.device_type}</div>
                  </td>
                  <td className="px-4 py-3 text-slate-400">{item.timestamp}</td>
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
                  <td className="px-4 py-3 text-right">
                    <Button size="sm" variant="primary" icon={Edit3} onClick={() => handleOpenCase(item)}>
                      Open Investigation
                    </Button>
                  </td>
                </tr>
              ))}

              {filteredItems.length === 0 && (
                <tr>
                  <td colSpan={9} className="px-4 py-10 text-center text-slate-500 font-sans">
                    No suspicious items matching the current filter.
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>

      {/* Case Details Modal matching prompt Section 24 */}
      {selectedCase && (
        <div className="fixed inset-0 bg-black/80 backdrop-blur-sm flex items-center justify-center p-4 z-50 animate-in fade-in">
          <div className="bg-[#11141c] border border-[#1e2432] rounded-2xl max-w-xl w-full p-6 space-y-4 shadow-2xl">
            <div className="flex items-center justify-between pb-3 border-b border-[#1e2432]">
              <div className="flex items-center space-x-2">
                <ShieldAlert className="w-5 h-5 text-rose-500" />
                <h4 className="text-sm font-bold text-slate-100 font-mono">
                  Investigation: {selectedCase.transaction_id}
                </h4>
              </div>
              <button
                onClick={() => setSelectedCase(null)}
                className="text-slate-400 hover:text-slate-200 p-1"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            <form onSubmit={handleSaveInvestigation} className="space-y-4 text-xs">
              {/* Detailed Metrics Panel */}
              <div className="grid grid-cols-2 sm:grid-cols-3 gap-3 bg-[#0b0e14] p-3 rounded-xl border border-[#1e2432]">
                <div>
                  <span className="text-slate-500 block text-[10px] uppercase">Customer ID</span>
                  <span className="font-mono font-bold text-slate-200">{selectedCase.customer_id}</span>
                </div>
                <div>
                  <span className="text-slate-500 block text-[10px] uppercase">Amount</span>
                  <span className="font-mono font-bold text-rose-400">
                    ₹{Number(selectedCase.amount).toLocaleString('en-IN', { minimumFractionDigits: 2 })}
                  </span>
                </div>
                <div>
                  <span className="text-slate-500 block text-[10px] uppercase">Risk Score</span>
                  <span className="font-mono font-bold text-rose-400">{selectedCase.risk_score} / 100</span>
                </div>
                <div>
                  <span className="text-slate-500 block text-[10px] uppercase">Origin Location</span>
                  <span className="font-sans text-slate-200">{selectedCase.location}</span>
                </div>
                <div>
                  <span className="text-slate-500 block text-[10px] uppercase">Device Signature</span>
                  <span className="font-sans text-slate-200 truncate block">{selectedCase.device_type}</span>
                </div>
                <div>
                  <span className="text-slate-500 block text-[10px] uppercase">Timestamp</span>
                  <span className="font-mono text-slate-300 truncate block">{selectedCase.timestamp}</span>
                </div>
              </div>

              {/* Status Selector */}
              <div>
                <label className="block font-semibold text-slate-300 mb-1.5 uppercase tracking-wider text-[11px]">
                  Investigation Status
                </label>
                <select
                  disabled={isViewer}
                  value={newStatus}
                  onChange={(e) => setNewStatus(e.target.value as ReviewStatus)}
                  className={`w-full bg-[#0b0e14] border border-[#232a3b] rounded-lg px-3 py-2 text-slate-100 font-sans focus:border-emerald-500 focus:outline-none ${
                    isViewer ? 'opacity-60 cursor-not-allowed' : ''
                  }`}
                >
                  <option value="New">NEW</option>
                  <option value="Under Review">UNDER REVIEW</option>
                  <option value="Investigating">INVESTIGATING</option>
                  <option value="Cleared">CLEARED (False Positive)</option>
                  <option value="Confirmed Suspicious">CONFIRMED SUSPICIOUS (Freeze Payment)</option>
                </select>
              </div>

              {/* Notes Area */}
              <div>
                <label className="block font-semibold text-slate-300 mb-1.5 uppercase tracking-wider text-[11px]">
                  Investigation Notes
                </label>
                <textarea
                  rows={3}
                  disabled={isViewer}
                  value={newNotes}
                  onChange={(e) => setNewNotes(e.target.value)}
                  placeholder={isViewer ? 'Read-only access' : 'Enter rationale, customer callback confirmation, or action taken...'}
                  className={`w-full bg-[#0b0e14] border border-[#232a3b] rounded-lg p-2.5 text-slate-100 font-sans focus:border-emerald-500 focus:outline-none ${
                    isViewer ? 'opacity-60 cursor-not-allowed' : ''
                  }`}
                />
              </div>

              {selectedCase.review_notes && (
                <div className="bg-[#0b0e14] p-3 rounded-lg border border-[#1e2432] text-slate-400 font-mono text-[11px]">
                  <span className="text-slate-500 font-sans font-bold block mb-1">Audit History:</span>
                  <pre className="whitespace-pre-wrap">{selectedCase.review_notes}</pre>
                </div>
              )}

              <div className="pt-2 flex justify-end space-x-3">
                <Button type="button" variant="secondary" onClick={() => setSelectedCase(null)}>
                  Close
                </Button>
                {!isViewer && (
                  <Button type="submit" variant="primary" icon={Save} isLoading={isSaving}>
                    Save Note &amp; Status
                  </Button>
                )}
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};
