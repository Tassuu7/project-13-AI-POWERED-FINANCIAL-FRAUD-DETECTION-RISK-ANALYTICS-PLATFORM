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

  const handleSaveReview = async (e: React.FormEvent) => {
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
        analyst_name: user?.username || 'Analyst',
      });

      showToast(`Case ${selectedCase.transaction_id} updated to '${newStatus}'`, 'success');

      // Update local state item
      setItems((prev) =>
        prev.map((it) =>
          it.transaction_id === selectedCase.transaction_id
            ? {
                ...it,
                review_status: newStatus,
                review_notes: newNotes
                  ? `${it.review_notes ? it.review_notes + ' | ' : ''}${user?.username || 'Analyst'}: ${newNotes}`
                  : it.review_notes,
              }
            : it
        )
      );

      setSelectedCase(null);
    } catch (err: any) {
      showToast(err.message || 'Failed to update review status', 'error');
    } finally {
      setIsSaving(false);
    }
  };

  const handleExport = () => {
    api.exportSuspicious();
    showToast('Exporting filtered investigations queue...', 'info');
  };

  const filteredItems = items.filter((item) => {
    const q = searchQuery.toLowerCase();
    return (
      item.transaction_id.toLowerCase().includes(q) ||
      item.customer_id.toLowerCase().includes(q) ||
      (item.location && item.location.toLowerCase().includes(q))
    );
  });

  return (
    <div className="w-full space-y-8 pb-16 font-sans">
      {/* Top Banner - Full Screen */}
      <div className="w-full bg-[#111622] border border-[#1e2533] rounded-2xl p-6 flex flex-col md:flex-row md:items-center justify-between gap-6 shadow-md">
        <div>
          <div className="flex items-center space-x-3">
            <ShieldAlert className="w-7 h-7 text-rose-400" />
            <h3 className="text-xl font-bold text-slate-100">
              Fraud Investigation Desk &amp; Case Management
            </h3>
          </div>
          <p className="text-sm text-slate-300 mt-1 font-medium">
            Triaged queue of high-risk transactions requiring auditor evaluation, step-up verification, customer contact, or clearance.
          </p>
        </div>

        <div className="flex items-center space-x-3 shrink-0">
          <Button variant="secondary" size="md" icon={Download} onClick={handleExport}>
            Export Queue CSV
          </Button>
          <Button variant="secondary" size="md" icon={RefreshCw} onClick={loadSuspicious} isLoading={isLoading}>
            Refresh Queue
          </Button>
        </div>
      </div>

      {/* Filter and Search Ribbon */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 w-full">
        <div className="flex items-center space-x-2 overflow-x-auto text-sm pb-1">
          {['All', 'New', 'Under Review', 'Investigating', 'Cleared', 'Confirmed Suspicious'].map((st) => (
            <button
              key={st}
              onClick={() => setFilterStatus(st)}
              className={`px-4 py-2.5 rounded-xl font-bold transition-all shrink-0 ${
                filterStatus === st
                  ? 'bg-emerald-950 text-emerald-300 border border-emerald-500/60 shadow-sm'
                  : 'text-slate-400 hover:text-slate-200 bg-[#111622] border border-[#1e2533]'
              }`}
            >
              {st}
            </button>
          ))}
        </div>

        <div className="relative w-full sm:w-80">
          <Search className="w-4 h-4 absolute left-3.5 top-3.5 text-slate-400" />
          <input
            type="text"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder="Search Tx ID, Customer, Location..."
            className="w-full bg-[#111622] border border-[#1e2533] rounded-xl pl-10 pr-4 py-2.5 text-sm text-slate-100 placeholder-slate-500 focus:border-emerald-500 focus:outline-none shadow-sm"
          />
        </div>
      </div>

      {/* Main Investigations Table - Full Width */}
      <div className="bg-[#111622] border border-[#1e2533] rounded-2xl overflow-hidden shadow-md w-full">
        <div className="overflow-x-auto w-full">
          <table className="w-full text-sm text-left">
            <thead className="bg-[#141a26] text-slate-200 font-bold border-b border-[#1e2533]">
              <tr>
                <th className="px-5 py-4">Transaction ID</th>
                <th className="px-5 py-4">Customer ID</th>
                <th className="px-5 py-4">Amount</th>
                <th className="px-5 py-4">Risk Score</th>
                <th className="px-5 py-4">Severity Tier</th>
                <th className="px-5 py-4">Location / Device</th>
                <th className="px-5 py-4">Timestamp</th>
                <th className="px-5 py-4">Lifecycle Status</th>
                <th className="px-5 py-4 text-right">Investigation Action</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-[#181f2e] font-mono text-slate-200">
              {filteredItems.map((item) => {
                const isHigh = item.risk_level === 'HIGH' || item.risk_score >= 70;
                const isMedium = item.risk_level === 'MEDIUM' || (item.risk_score >= 40 && item.risk_score < 70);

                return (
                  <tr key={item.transaction_id} className="hover:bg-[#141c29] transition-colors">
                    <td className="px-5 py-4 font-bold text-slate-100">{item.transaction_id}</td>
                    <td className="px-5 py-4 text-slate-300 font-sans">{item.customer_id}</td>
                    <td className="px-5 py-4 font-bold text-slate-100 font-mono">
                      ₹{Number(item.amount).toLocaleString('en-IN', { minimumFractionDigits: 2 })}
                    </td>
                    <td className="px-5 py-4">
                      <span className={`font-black ${isHigh ? 'text-rose-400' : isMedium ? 'text-amber-400' : 'text-emerald-400'}`}>
                        {item.risk_score} / 100
                      </span>
                    </td>
                    <td className="px-5 py-4">
                      <span className={`px-2.5 py-1 rounded-lg text-xs font-black uppercase ${
                        isHigh
                          ? 'bg-rose-950 text-rose-300 border border-rose-700/60'
                          : isMedium
                          ? 'bg-amber-950 text-amber-300 border border-amber-700/60'
                          : 'bg-emerald-950 text-emerald-300 border border-emerald-700/60'
                      }`}>
                        {item.risk_level}
                      </span>
                    </td>
                    <td className="px-5 py-4 text-xs font-sans text-slate-300">
                      <div>{item.location || 'Unknown Cluster'}</div>
                      <div className="text-slate-400 mt-0.5">{item.device_type}</div>
                    </td>
                    <td className="px-5 py-4 text-xs text-slate-300 font-mono">{item.timestamp}</td>
                    <td className="px-5 py-4 font-sans font-bold">
                      <span className={`px-2.5 py-1 rounded-lg text-xs ${
                        item.review_status === 'Confirmed Suspicious' ? 'bg-rose-950 text-rose-300 border border-rose-800' :
                        item.review_status === 'Cleared' ? 'bg-emerald-950 text-emerald-300 border border-emerald-800' :
                        item.review_status === 'Investigating' ? 'bg-amber-950 text-amber-300 border border-amber-800' :
                        'bg-slate-800 text-slate-200 border border-slate-700'
                      }`}>
                        {item.review_status}
                      </span>
                    </td>
                    <td className="px-5 py-4 text-right font-sans">
                      <button
                        onClick={() => handleOpenCase(item)}
                        className="px-3.5 py-1.5 rounded-lg bg-[#182030] hover:bg-emerald-950/80 text-emerald-400 border border-[#2c3850] hover:border-emerald-600/60 text-xs font-bold transition-all shadow-sm"
                      >
                        Open Case Dossier &rarr;
                      </button>
                    </td>
                  </tr>
                );
              })}

              {filteredItems.length === 0 && (
                <tr>
                  <td colSpan={9} className="p-12 text-center text-slate-400 font-sans text-sm">
                    No transactions match the selected filter query.
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>

      {/* Case Investigation Dossier Modal Dialog */}
      {selectedCase && (
        <div className="fixed inset-0 bg-black/80 backdrop-blur-sm flex items-center justify-center p-6 z-50 animate-in fade-in">
          <div className="bg-[#111622] border border-[#242e40] rounded-3xl max-w-2xl w-full p-8 space-y-6 shadow-2xl">
            <div className="flex items-center justify-between pb-4 border-b border-[#202838]">
              <div className="flex items-center space-x-3">
                <ShieldAlert className="w-7 h-7 text-rose-400" />
                <div>
                  <h4 className="text-xl font-bold text-slate-100 font-mono">
                    Investigation Dossier: {selectedCase.transaction_id}
                  </h4>
                  <span className="text-xs text-slate-400 font-sans">
                    Customer ID: {selectedCase.customer_id} &bull; Device: {selectedCase.device_type}
                  </span>
                </div>
              </div>
              <button
                onClick={() => setSelectedCase(null)}
                className="text-slate-400 hover:text-slate-200 p-1"
              >
                <X className="w-6 h-6" />
              </button>
            </div>

            {/* Transaction Key Data Cards */}
            <div className="grid grid-cols-3 gap-4 text-center">
              <div className="p-4 rounded-xl bg-[#0b0e14] border border-[#202838]">
                <span className="text-xs text-slate-400 block mb-1">Amount</span>
                <span className="text-xl font-black font-mono text-rose-400">
                  ₹{Number(selectedCase.amount).toLocaleString()}
                </span>
              </div>
              <div className="p-4 rounded-xl bg-[#0b0e14] border border-[#202838]">
                <span className="text-xs text-slate-400 block mb-1">Calibrated Risk</span>
                <span className="text-xl font-black font-mono text-rose-400">
                  {selectedCase.risk_score} / 100
                </span>
              </div>
              <div className="p-4 rounded-xl bg-[#0b0e14] border border-[#202838]">
                <span className="text-xs text-slate-400 block mb-1">Current Status</span>
                <span className="text-xs font-bold font-sans text-amber-400">
                  {selectedCase.review_status}
                </span>
              </div>
            </div>

            {/* Audit Notes Trail */}
            <div className="space-y-2 text-sm">
              <span className="font-bold text-slate-200 text-xs uppercase tracking-wider block">
                Auditor Activity Log &amp; Notes
              </span>
              <div className="p-4 rounded-xl bg-[#0b0e14] border border-[#202838] max-h-36 overflow-y-auto space-y-2 text-xs font-mono text-slate-300">
                {selectedCase.review_notes ? (
                  <div className="pb-1 text-slate-300">
                    &bull; {selectedCase.review_notes}
                  </div>
                ) : (
                  <span className="text-slate-500 font-sans">No prior analyst notes recorded on this transaction.</span>
                )}
              </div>
            </div>

            {/* Edit Case Form */}
            <form onSubmit={handleSaveReview} className="space-y-4 pt-2 border-t border-[#202838]">
              <div>
                <label className="block text-slate-200 font-bold text-sm mb-1.5">
                  Update Investigation Lifecycle Status
                </label>
                <select
                  value={newStatus}
                  onChange={(e) => setNewStatus(e.target.value as ReviewStatus)}
                  disabled={isViewer}
                  className="w-full bg-[#0b0e14] border border-[#242e40] rounded-xl px-4 py-2.5 text-slate-100 font-bold text-sm focus:border-emerald-500 focus:outline-none"
                >
                  <option value="New">New (Unreviewed)</option>
                  <option value="Under Review">Under Review</option>
                  <option value="Investigating">Investigating (Customer Outreach)</option>
                  <option value="Cleared">Cleared (Legitimate Customer Activity)</option>
                  <option value="Confirmed Suspicious">Confirmed Suspicious (Escalate to Legal/Card Block)</option>
                </select>
              </div>

              <div>
                <label className="block text-slate-200 font-bold text-sm mb-1.5">
                  Append Analyst Rationale / Findings
                </label>
                <textarea
                  rows={3}
                  value={newNotes}
                  onChange={(e) => setNewNotes(e.target.value)}
                  disabled={isViewer}
                  placeholder="Record customer outreach results, device checks, or justification for status change..."
                  className="w-full bg-[#0b0e14] border border-[#242e40] rounded-xl p-3 text-slate-100 text-sm focus:border-emerald-500 focus:outline-none"
                />
              </div>

              <div className="flex justify-end space-x-3 pt-2">
                <Button type="button" variant="secondary" onClick={() => setSelectedCase(null)}>
                  Cancel
                </Button>
                <Button
                  type="submit"
                  variant="primary"
                  icon={Save}
                  isLoading={isSaving}
                  disabled={isViewer}
                >
                  Save Dossier Findings
                </Button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};
