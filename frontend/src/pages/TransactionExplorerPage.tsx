import React, { useState, useEffect } from 'react';
import { Database, Search, Filter, ArrowUpDown, ChevronLeft, ChevronRight, Eye, X, ShieldAlert } from 'lucide-react';
import { useAppState } from '../context/AppStateContext';
import { api } from '../services/api';
import { TransactionRecord } from '../types';
import { Button } from '../components/common/Button';

export const TransactionExplorerPage: React.FC = () => {
  const { selectedDataset } = useAppState();

  const [searchTerm, setSearchTerm] = useState('');
  const [riskFilter, setRiskFilter] = useState('ALL');
  const [typeFilter, setTypeFilter] = useState('ALL');
  const [minAmount, setMinAmount] = useState('');
  const [maxAmount, setMaxAmount] = useState('');
  const [sortBy, setSortBy] = useState('timestamp');
  const [sortOrder, setSortOrder] = useState<'asc' | 'desc'>('desc');
  const [currentPage, setCurrentPage] = useState(1);

  const [records, setRecords] = useState<TransactionRecord[]>([]);
  const [totalRecords, setTotalRecords] = useState(0);
  const [totalPages, setTotalPages] = useState(1);
  const [isLoading, setIsLoading] = useState(false);

  const [selectedTx, setSelectedTx] = useState<TransactionRecord | null>(null);

  const fetchTransactions = async () => {
    if (!selectedDataset) return;
    setIsLoading(true);
    try {
      const res = await api.queryTransactions({
        filename: selectedDataset,
        search: searchTerm || undefined,
        risk_level: riskFilter !== 'ALL' ? riskFilter : undefined,
        transaction_type: typeFilter !== 'ALL' ? typeFilter : undefined,
        min_amount: minAmount ? Number(minAmount) : undefined,
        max_amount: maxAmount ? Number(maxAmount) : undefined,
        sort_by: sortBy,
        sort_order: sortOrder,
        page: currentPage,
        page_size: 15,
      });

      setRecords(res.records);
      setTotalRecords(res.total_records);
      setTotalPages(res.total_pages);
    } catch (err) {
      console.warn('Transaction query error:', err);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchTransactions();
  }, [selectedDataset, currentPage, riskFilter, typeFilter, sortBy, sortOrder]);

  const handleSearchSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setCurrentPage(1);
    fetchTransactions();
  };

  return (
    <div className="space-y-6 max-w-7xl mx-auto pb-12">
      {/* Header Controls */}
      <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-5 shadow-sm space-y-4">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div className="flex items-center space-x-2">
            <Database className="w-5 h-5 text-emerald-400" />
            <h3 className="text-base font-bold text-slate-100">
              Enterprise Transaction Explorer &amp; Ledger
            </h3>
          </div>
          <span className="text-xs font-mono text-slate-400">
            Matching: <strong className="text-emerald-400 font-bold">{totalRecords.toLocaleString()}</strong> records
          </span>
        </div>

        {/* Filter Toolbar */}
        <form onSubmit={handleSearchSubmit} className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-3 text-xs">
          {/* Search Input */}
          <div className="relative">
            <input
              type="text"
              placeholder="Search TXN- or CUST- ID..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="w-full bg-[#0b0e14] border border-[#232a3b] rounded-lg pl-8 pr-3 py-2 text-slate-100 placeholder-slate-500 focus:border-emerald-500 focus:outline-none"
            />
            <Search className="w-4 h-4 text-slate-500 absolute left-2.5 top-2.5" />
          </div>

          {/* Risk Filter */}
          <select
            value={riskFilter}
            onChange={(e) => {
              setRiskFilter(e.target.value);
              setCurrentPage(1);
            }}
            className="bg-[#0b0e14] border border-[#232a3b] rounded-lg px-3 py-2 text-slate-100 focus:border-emerald-500 focus:outline-none"
          >
            <option value="ALL">All Risk Tiers</option>
            <option value="HIGH">High Risk Only</option>
            <option value="MEDIUM">Medium Risk Only</option>
            <option value="LOW">Low Risk Only</option>
          </select>

          {/* Transaction Type Filter */}
          <select
            value={typeFilter}
            onChange={(e) => {
              setTypeFilter(e.target.value);
              setCurrentPage(1);
            }}
            className="bg-[#0b0e14] border border-[#232a3b] rounded-lg px-3 py-2 text-slate-100 focus:border-emerald-500 focus:outline-none"
          >
            <option value="ALL">All Channels</option>
            <option value="Online">Online</option>
            <option value="POS / In-Store">POS / In-Store</option>
            <option value="UPI Transfer">UPI Transfer</option>
            <option value="ATM Withdrawal">ATM Withdrawal</option>
            <option value="Wire Transfer">Wire Transfer</option>
          </select>

          {/* Sort By */}
          <select
            value={sortBy}
            onChange={(e) => setSortBy(e.target.value)}
            className="bg-[#0b0e14] border border-[#232a3b] rounded-lg px-3 py-2 text-slate-100 focus:border-emerald-500 focus:outline-none"
          >
            <option value="timestamp">Sort by Timestamp</option>
            <option value="amount">Sort by Amount</option>
            <option value="risk_score">Sort by Risk Score</option>
          </select>

          {/* Sort Order Toggle */}
          <Button
            type="button"
            variant="secondary"
            onClick={() => setSortOrder(sortOrder === 'asc' ? 'desc' : 'asc')}
            icon={ArrowUpDown}
          >
            {sortOrder === 'asc' ? 'Ascending' : 'Descending'}
          </Button>
        </form>
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
                <th className="px-4 py-3">Channel</th>
                <th className="px-4 py-3">Location</th>
                <th className="px-4 py-3">Device Fingerprint</th>
                <th className="px-4 py-3">Risk Assessment</th>
                <th className="px-4 py-3 text-right">Action</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-[#181d28] font-mono text-slate-300">
              {records.map((tx) => {
                const isHigh = tx.risk_level === 'HIGH' || tx.is_fraud === 1;
                const isMed = tx.risk_level === 'MEDIUM';

                return (
                  <tr
                    key={tx.transaction_id}
                    onClick={() => setSelectedTx(tx)}
                    className="hover:bg-[#141822] cursor-pointer transition-colors"
                  >
                    <td className="px-4 py-3 font-bold text-slate-200">{tx.transaction_id}</td>
                    <td className="px-4 py-3 text-slate-400">{tx.customer_id}</td>
                    <td className="px-4 py-3 font-bold text-slate-100">
                      ₹{Number(tx.amount || 0).toLocaleString('en-IN', { minimumFractionDigits: 2 })}
                    </td>
                    <td className="px-4 py-3 text-slate-400">{tx.timestamp}</td>
                    <td className="px-4 py-3 font-sans">{tx.transaction_type}</td>
                    <td className="px-4 py-3 font-sans">{tx.location}</td>
                    <td className="px-4 py-3 font-sans truncate max-w-[130px]">{tx.device_type}</td>
                    <td className="px-4 py-3 font-sans">
                      <span className={`px-2 py-0.5 rounded text-[10px] font-bold ${
                        isHigh ? 'bg-rose-950 text-rose-400 border border-rose-800/40' :
                        isMed ? 'bg-amber-950 text-amber-400 border border-amber-800/40' :
                        'bg-emerald-950 text-emerald-400 border border-emerald-800/40'
                      }`}>
                        {isHigh ? 'HIGH RISK' : isMed ? 'MEDIUM RISK' : 'LOW RISK'}
                      </span>
                    </td>
                    <td className="px-4 py-3 text-right">
                      <Button
                        size="sm"
                        variant="ghost"
                        icon={Eye}
                        onClick={(e) => {
                          e.stopPropagation();
                          setSelectedTx(tx);
                        }}
                      >
                        Inspect
                      </Button>
                    </td>
                  </tr>
                );
              })}

              {records.length === 0 && (
                <tr>
                  <td colSpan={9} className="px-4 py-8 text-center text-slate-500 font-sans">
                    No transactions match the selected criteria.
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>

        {/* Pagination Bar */}
        <div className="px-5 py-3.5 bg-[#141822] border-t border-[#1e2432] flex items-center justify-between text-xs">
          <span className="text-slate-400">
            Page <strong className="text-slate-200">{currentPage}</strong> of <strong className="text-slate-200">{totalPages}</strong>
          </span>
          <div className="flex items-center space-x-2">
            <Button
              size="sm"
              variant="secondary"
              icon={ChevronLeft}
              disabled={currentPage <= 1}
              onClick={() => setCurrentPage((p) => Math.max(1, p - 1))}
            >
              Previous
            </Button>
            <Button
              size="sm"
              variant="secondary"
              disabled={currentPage >= totalPages}
              onClick={() => setCurrentPage((p) => Math.min(totalPages, p + 1))}
            >
              <span>Next</span>
              <ChevronRight className="w-4 h-4 ml-1" />
            </Button>
          </div>
        </div>
      </div>

      {/* Transaction Detail Modal */}
      {selectedTx && (
        <div className="fixed inset-0 bg-black/70 backdrop-blur-sm flex items-center justify-center p-4 z-50 animate-in fade-in duration-150">
          <div className="bg-[#11141c] border border-[#1e2432] rounded-xl max-w-lg w-full p-6 space-y-4 shadow-2xl">
            <div className="flex items-center justify-between pb-3 border-b border-[#1e2432]">
              <div className="flex items-center space-x-2">
                <ShieldAlert className="w-5 h-5 text-emerald-400" />
                <h4 className="text-sm font-bold text-slate-100 font-mono">
                  {selectedTx.transaction_id}
                </h4>
              </div>
              <button
                onClick={() => setSelectedTx(null)}
                className="text-slate-400 hover:text-slate-200 p-1"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            <div className="space-y-2.5 text-xs">
              <div className="flex justify-between py-1 border-b border-[#181d28]">
                <span className="text-slate-400">Customer Identifier:</span>
                <span className="font-mono text-slate-200 font-bold">{selectedTx.customer_id}</span>
              </div>
              <div className="flex justify-between py-1 border-b border-[#181d28]">
                <span className="text-slate-400">Amount:</span>
                <span className="font-mono font-bold text-slate-100 text-sm">
                  ₹{Number(selectedTx.amount || 0).toLocaleString('en-IN', { minimumFractionDigits: 2 })}
                </span>
              </div>
              <div className="flex justify-between py-1 border-b border-[#181d28]">
                <span className="text-slate-400">Timestamp:</span>
                <span className="font-mono text-slate-300">{selectedTx.timestamp}</span>
              </div>
              <div className="flex justify-between py-1 border-b border-[#181d28]">
                <span className="text-slate-400">Merchant Category:</span>
                <span className="text-slate-200">{selectedTx.merchant_category}</span>
              </div>
              <div className="flex justify-between py-1 border-b border-[#181d28]">
                <span className="text-slate-400">Location:</span>
                <span className="text-slate-200">{selectedTx.location}</span>
              </div>
              <div className="flex justify-between py-1 border-b border-[#181d28]">
                <span className="text-slate-400">Hardware Fingerprint:</span>
                <span className="text-slate-200">{selectedTx.device_type}</span>
              </div>
              <div className="flex justify-between py-1 border-b border-[#181d28]">
                <span className="text-slate-400">Radial Distance:</span>
                <span className="font-mono text-slate-200">{selectedTx.distance_from_usual_location || 0} km</span>
              </div>
              <div className="flex justify-between py-1 border-b border-[#181d28]">
                <span className="text-slate-400">Assigned Risk Tier:</span>
                <span className={`px-2 py-0.5 rounded font-bold text-[10px] ${
                  selectedTx.risk_level === 'HIGH' || selectedTx.is_fraud === 1
                    ? 'bg-rose-950 text-rose-400 border border-rose-800/40'
                    : 'bg-emerald-950 text-emerald-400 border border-emerald-800/40'
                }`}>
                  {selectedTx.risk_level || (selectedTx.is_fraud === 1 ? 'HIGH' : 'LOW')}
                </span>
              </div>
            </div>

            <div className="pt-3 flex justify-end">
              <Button variant="secondary" onClick={() => setSelectedTx(null)}>
                Close Details
              </Button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
