import React, { useState } from 'react';
import { Cpu, Download, ArrowRight, CheckCircle2, ShieldCheck, RefreshCw, Table } from 'lucide-react';
import { useAppState } from '../context/AppStateContext';
import { api } from '../services/api';
import { Button } from '../components/common/Button';

export const SyntheticGeneratorPage: React.FC<{ onNavigateNext?: () => void }> = ({ onNavigateNext }) => {
  const { setSelectedDataset, refreshDatasets, showToast } = useAppState();

  const [numRecords, setNumRecords] = useState(1500);
  const [numCustomers, setNumCustomers] = useState(200);
  const [fraudPct, setFraudPct] = useState(5.0);
  const [seed, setSeed] = useState(42);
  const [isGenerating, setIsGenerating] = useState(false);
  const [generatedResult, setGeneratedResult] = useState<any>(null);

  const handleGenerate = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsGenerating(true);
    try {
      const res = await api.generateSynthetic({
        num_records: Number(numRecords),
        num_customers: Number(numCustomers),
        fraud_percentage: Number(fraudPct),
        random_seed: Number(seed),
      });

      setGeneratedResult(res);
      await refreshDatasets();
      setSelectedDataset(res.filename);
      showToast(`Generated ${res.rows} records (${res.fraud_count} fraud) in ${res.filename}`, 'success');
    } catch (err: any) {
      showToast(err.message || 'Generation failed', 'error');
    } finally {
      setIsGenerating(false);
    }
  };

  const handleDownload = () => {
    if (!generatedResult) return;
    window.open(`http://localhost:8000/api/datasets/${generatedResult.filename}/download`, '_blank');
  };

  return (
    <div className="space-y-6 max-w-5xl mx-auto pb-12">
      {/* Configuration Card */}
      <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-6 shadow-sm">
        <div className="flex items-center space-x-3 pb-4 border-b border-[#1e2432] mb-5">
          <div className="w-10 h-10 rounded-lg bg-emerald-950/80 border border-emerald-500/30 flex items-center justify-center text-emerald-400">
            <Cpu className="w-5 h-5" />
          </div>
          <div>
            <h3 className="text-base font-bold text-slate-100">
              Synthetic Financial Transaction Generator
            </h3>
            <p className="text-xs text-slate-400">
              Generate realistic, privacy-safe transaction logs with authentic fraud behavioral patterns.
            </p>
          </div>
        </div>

        <form onSubmit={handleGenerate} className="space-y-6">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-5 text-xs">
            <div>
              <label className="block font-semibold text-slate-300 mb-1.5 uppercase tracking-wider">
                Total Transaction Volume
              </label>
              <input
                type="number"
                min={100}
                max={25000}
                value={numRecords}
                onChange={(e) => setNumRecords(Number(e.target.value))}
                className="w-full bg-[#0b0e14] border border-[#232a3b] rounded-lg px-3 py-2 text-slate-100 font-mono focus:border-emerald-500 focus:outline-none"
              />
              <span className="text-[11px] text-slate-500 mt-1 block">Supported: 100 to 25,000 records</span>
            </div>

            <div>
              <label className="block font-semibold text-slate-300 mb-1.5 uppercase tracking-wider">
                Simulated Customer Accounts
              </label>
              <input
                type="number"
                min={10}
                max={5000}
                value={numCustomers}
                onChange={(e) => setNumCustomers(Number(e.target.value))}
                className="w-full bg-[#0b0e14] border border-[#232a3b] rounded-lg px-3 py-2 text-slate-100 font-mono focus:border-emerald-500 focus:outline-none"
              />
              <span className="text-[11px] text-slate-500 mt-1 block">Defines customer baseline spending histories</span>
            </div>

            <div>
              <label className="block font-semibold text-slate-300 mb-1.5 uppercase tracking-wider">
                Target Fraud Prevalence (%)
              </label>
              <input
                type="number"
                step="0.5"
                min={0.5}
                max={30}
                value={fraudPct}
                onChange={(e) => setFraudPct(Number(e.target.value))}
                className="w-full bg-[#0b0e14] border border-[#232a3b] rounded-lg px-3 py-2 text-slate-100 font-mono focus:border-emerald-500 focus:outline-none"
              />
              <span className="text-[11px] text-slate-500 mt-1 block">Real-world financial fraud is typically 1% - 8%</span>
            </div>

            <div>
              <label className="block font-semibold text-slate-300 mb-1.5 uppercase tracking-wider">
                Deterministic Random Seed
              </label>
              <input
                type="number"
                value={seed}
                onChange={(e) => setSeed(Number(e.target.value))}
                className="w-full bg-[#0b0e14] border border-[#232a3b] rounded-lg px-3 py-2 text-slate-100 font-mono focus:border-emerald-500 focus:outline-none"
              />
              <span className="text-[11px] text-slate-500 mt-1 block">Guarantees 100% reproducible data distribution</span>
            </div>
          </div>

          <div className="bg-[#0b0e14] border border-[#1e2536] p-3.5 rounded-lg text-xs text-slate-400 space-y-1">
            <div className="text-emerald-400 font-bold flex items-center space-x-1.5">
              <ShieldCheck className="w-4 h-4" />
              <span>Synthetic Attack Vectors Injected</span>
            </div>
            <p>
              Generates genuine anomaly characteristics: nocturnal hour transactions (01:00-05:00 AM), exponential spend deviations (&gt;5x customer mean), distant location hops (&gt;150 km), untrusted device fingerprints, and rapid velocity bursts.
            </p>
          </div>

          <div className="flex justify-end space-x-3 pt-2">
            <Button type="submit" variant="primary" icon={Cpu} isLoading={isGenerating}>
              Generate Synthetic Dataset
            </Button>
          </div>
        </form>
      </div>

      {/* Generation Results Card */}
      {generatedResult && (
        <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-6 space-y-4">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 border-b border-[#1e2432]">
            <div>
              <span className="text-xs text-emerald-400 font-bold uppercase tracking-wider flex items-center space-x-1.5">
                <CheckCircle2 className="w-4 h-4" />
                <span>Dataset Ready &amp; Saved Locally</span>
              </span>
              <h4 className="text-base font-bold text-slate-100 font-mono mt-0.5">
                {generatedResult.filename}
              </h4>
            </div>
            <div className="flex items-center space-x-2">
              <Button variant="secondary" size="sm" icon={Download} onClick={handleDownload}>
                Download CSV
              </Button>
              {onNavigateNext && (
                <Button variant="primary" size="sm" icon={ArrowRight} onClick={onNavigateNext}>
                  Run Validation
                </Button>
              )}
            </div>
          </div>

          <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 text-xs">
            <div className="bg-[#0b0e14] p-3 rounded border border-[#1e2432]">
              <span className="text-slate-400">Total Rows</span>
              <div className="text-base font-bold text-slate-100 font-mono mt-0.5">
                {generatedResult.rows.toLocaleString()}
              </div>
            </div>
            <div className="bg-[#0b0e14] p-3 rounded border border-[#1e2432]">
              <span className="text-slate-400">Total Features</span>
              <div className="text-base font-bold text-slate-100 font-mono mt-0.5">
                {generatedResult.columns.length}
              </div>
            </div>
            <div className="bg-[#0b0e14] p-3 rounded border border-[#1e2432]">
              <span className="text-slate-400">Fraud Samples</span>
              <div className="text-base font-bold text-rose-400 font-mono mt-0.5">
                {generatedResult.fraud_count}
              </div>
            </div>
            <div className="bg-[#0b0e14] p-3 rounded border border-[#1e2432]">
              <span className="text-slate-400">Normal Samples</span>
              <div className="text-base font-bold text-emerald-400 font-mono mt-0.5">
                {generatedResult.rows - generatedResult.fraud_count}
              </div>
            </div>
          </div>

          {/* Sample Table Preview */}
          <div className="overflow-x-auto rounded border border-[#1d2330]">
            <table className="w-full text-xs text-left">
              <thead className="bg-[#171c26] text-slate-300 font-semibold border-b border-[#1d2330]">
                <tr>
                  <th className="px-3 py-2">Transaction ID</th>
                  <th className="px-3 py-2">Customer</th>
                  <th className="px-3 py-2">Amount (INR)</th>
                  <th className="px-3 py-2">Timestamp</th>
                  <th className="px-3 py-2">Channel</th>
                  <th className="px-3 py-2">Location</th>
                  <th className="px-3 py-2">Ground Truth</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-[#171c26] text-slate-300">
                {generatedResult.sample_preview.map((tx: any) => (
                  <tr key={tx.transaction_id} className="hover:bg-[#151923]">
                    <td className="px-3 py-2 font-mono text-slate-200">{tx.transaction_id}</td>
                    <td className="px-3 py-2 font-mono text-slate-400">{tx.customer_id}</td>
                    <td className="px-3 py-2 font-mono font-bold text-slate-100">₹{tx.amount.toFixed(2)}</td>
                    <td className="px-3 py-2 font-mono text-slate-400">{tx.timestamp}</td>
                    <td className="px-3 py-2">{tx.transaction_type}</td>
                    <td className="px-3 py-2">{tx.location}</td>
                    <td className="px-3 py-2">
                      <span className={`px-2 py-0.5 rounded text-[10px] font-bold ${
                        tx.is_fraud === 1 ? 'bg-rose-950 text-rose-400 border border-rose-800/40' : 'bg-emerald-950 text-emerald-400 border border-emerald-800/40'
                      }`}>
                        {tx.is_fraud === 1 ? 'FRAUD' : 'NORMAL'}
                      </span>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      )}
    </div>
  );
};
