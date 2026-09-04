import React, { useState, useEffect } from 'react';
import {
  ResponsiveContainer,
  AreaChart,
  Area,
  BarChart,
  Bar,
  PieChart,
  Pie,
  Cell,
  XAxis,
  YAxis,
  Tooltip
} from 'recharts';
import {
  ShieldAlert,
  ShieldCheck,
  TrendingUp,
  AlertTriangle,
  FileSpreadsheet,
  CheckCircle2,
  Clock,
  ArrowRight,
  RefreshCw,
  Eye,
  Sliders,
  Award,
  Sparkles,
  Play,
  Database,
  X
} from 'lucide-react';
import { useAuth } from '../context/AuthContext';
import { useAppState } from '../context/AppStateContext';
import { api } from '../services/api';
import { StatCard } from '../components/common/StatCard';
import { Button } from '../components/common/Button';

interface DashboardPageProps {
  onNavigate: (page: string) => void;
}

export const DashboardPage: React.FC<DashboardPageProps> = ({ onNavigate }) => {
  const { user, isAdmin, isAnalyst, isViewer } = useAuth();
  const { selectedDataset, setSelectedDataset, refreshDatasets, activeModel, showToast } = useAppState();

  const [telemetry, setTelemetry] = useState<any>(null);
  const [isLoading, setIsLoading] = useState<boolean>(true);

  // Admin Synthetic Data Generator State
  const [showAdminSynthModal, setShowAdminSynthModal] = useState<boolean>(false);
  const [isGeneratingSynth, setIsGeneratingSynth] = useState<boolean>(false);
  const [synthRecords, setSynthRecords] = useState<number>(1200);
  const [synthFraudPct, setSynthFraudPct] = useState<number>(5.5);
  const [synthCustomers, setSynthCustomers] = useState<number>(250);
  const [synthSeed, setSynthSeed] = useState<number>(42);

  const handleAdminGenerateSynthetic = async (e?: React.FormEvent, customRecords?: number, customFraudPct?: number) => {
    if (e) e.preventDefault();
    setIsGeneratingSynth(true);
    try {
      const recordsToGen = customRecords || Number(synthRecords) || 1000;
      const fraudToGen = customFraudPct !== undefined ? customFraudPct : (Number(synthFraudPct) || 5.0);
      const res = await api.generateSynthetic({
        num_records: recordsToGen,
        fraud_percentage: fraudToGen,
        num_customers: Number(synthCustomers) || 200,
        random_seed: Number(synthSeed) || 42,
      });
      const count = res.rows || res.records_count || recordsToGen;
      showToast(`Successfully generated ${res.filename} with ${count} synthetic transactions!`, 'success');
      setShowAdminSynthModal(false);
      await refreshDatasets();
      setSelectedDataset(res.filename);
      await loadTelemetry();
    } catch (err: any) {
      showToast(err.message || 'Synthetic data generation failed', 'error');
    } finally {
      setIsGeneratingSynth(false);
    }
  };

  const loadTelemetry = async () => {
    setIsLoading(true);
    try {
      const data = await api.getDashboardTelemetry(selectedDataset);
      setTelemetry(data);
    } catch (err) {
      console.warn('Dashboard telemetry fetch error:', err);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    loadTelemetry();
  }, [user?.role, selectedDataset]);

  const stats = telemetry?.stats || {};
  const charts = telemetry?.charts || {};

  // ==========================================
  // 1. ADMINISTRATOR DASHBOARD
  // ==========================================
  if (isAdmin) {
    return (
      <div className="w-full space-y-8 pb-16 font-sans">
        {/* Admin Header */}
        <div className="w-full bg-[#111622] border border-[#1e2533] rounded-2xl p-6 flex flex-col md:flex-row md:items-center justify-between gap-6 shadow-md">
          <div>
            <div className="flex items-center space-x-2.5">
              <span className="px-3 py-1 rounded-lg bg-emerald-950 text-emerald-300 border border-emerald-700/60 text-xs font-black font-mono tracking-wider">
                ADMIN CONSOLE
              </span>
              <span className="text-slate-400 text-sm font-mono">&bull; Active Dataset: {selectedDataset}</span>
            </div>
            <h2 className="text-2xl font-black text-slate-100 mt-2">Welcome, Administrator</h2>
            <p className="text-sm text-slate-300 mt-1 font-medium">
              Complete administrative overview of financial fraud operations, machine learning model telemetry, and system throughput.
            </p>
          </div>
          <div className="flex items-center space-x-3 shrink-0 flex-wrap gap-2">
            <Button variant="secondary" size="md" icon={RefreshCw} onClick={loadTelemetry} isLoading={isLoading}>
              Refresh Telemetry
            </Button>
            <Button
              variant="secondary"
              size="md"
              icon={Sparkles}
              onClick={() => setShowAdminSynthModal(true)}
              isLoading={isGeneratingSynth}
              className="border-emerald-500/40 text-emerald-300 hover:bg-emerald-950/40"
            >
              Generate Synthetic Data
            </Button>
            <Button variant="primary" size="md" icon={FileSpreadsheet} onClick={() => onNavigate('analyze')}>
              Transaction Analysis
            </Button>
          </div>
        </div>

        {/* Admin Primary KPIs */}
        <div className="grid grid-cols-2 lg:grid-cols-6 gap-3">
          <StatCard
            title="Total Volume"
            value={stats.total_transactions ? Number(stats.total_transactions).toLocaleString() : '1,200'}
            subtitle="Scored transactions"
            icon={FileSpreadsheet}
          />
          <StatCard
            title="Normal Transactions"
            value={stats.normal_transactions ? Number(stats.normal_transactions).toLocaleString() : '1,134'}
            subtitle="Baseline verified"
            icon={ShieldCheck}
            trend="positive"
          />
          <StatCard
            title="Suspicious Items"
            value={stats.suspicious_transactions || '66'}
            subtitle="Flagged anomalies"
            icon={AlertTriangle}
            trend="negative"
          />
          <StatCard
            title="High-Risk Items"
            value={stats.high_risk_transactions || '37'}
            subtitle="Score &gt;= 70"
            icon={ShieldAlert}
            trend="negative"
          />
          <StatCard
            title="Fraud Rate"
            value={`${stats.fraud_rate || 5.5}%`}
            subtitle="Of total volume"
            icon={TrendingUp}
          />
          <StatCard
            title="Active ML Model"
            value={stats.active_model || activeModel}
            subtitle="Production Engine"
            icon={Sliders}
          />
        </div>

        {/* Administrator Synthetic Dataset Generator Studio */}
        <div className="w-full bg-[#111622] border border-[#1e2533] rounded-2xl p-6 space-y-5 shadow-md">
          <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-4 border-b border-[#1e2533]">
            <div className="flex items-center space-x-3">
              <div className="w-10 h-10 rounded-xl bg-emerald-950/80 border border-emerald-500/40 flex items-center justify-center text-emerald-400 shrink-0">
                <Sparkles className="w-5 h-5" />
              </div>
              <div>
                <h3 className="text-base font-bold text-slate-100 flex items-center space-x-2">
                  <span>Synthetic Data Generator &amp; Stress-Testing Studio</span>
                  <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-950 text-emerald-300 border border-emerald-700/60 font-mono">
                    ADMIN PRIVILEGE
                  </span>
                </h3>
                <p className="text-xs text-slate-300 mt-0.5">
                  Generate realistic financial transaction records with configurable fraud velocity spikes, nocturnal hours, and impossible travel patterns.
                </p>
              </div>
            </div>
            <div className="flex items-center space-x-2 shrink-0">
              <Button
                variant="secondary"
                size="sm"
                icon={Sparkles}
                onClick={() => setShowAdminSynthModal(true)}
              >
                Customize Parameters
              </Button>
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div className="p-4 rounded-xl bg-[#0b0e14] border border-[#1e2533] flex flex-col justify-between space-y-3">
              <div>
                <span className="text-xs font-bold text-emerald-400 uppercase tracking-wider block mb-1">Preset 1: Baseline Flow</span>
                <h4 className="text-sm font-bold text-slate-200">1,000 Transactions (5% Fraud)</h4>
                <p className="text-xs text-slate-400 mt-1">Standard retail flow with 50 fraud incidents across 150 customer entities.</p>
              </div>
              <Button
                variant="primary"
                size="sm"
                icon={Play}
                isLoading={isGeneratingSynth}
                onClick={() => handleAdminGenerateSynthetic(undefined, 1000, 5.0)}
                className="w-full text-xs font-bold"
              >
                Generate 1,000 Tx
              </Button>
            </div>

            <div className="p-4 rounded-xl bg-[#0b0e14] border border-[#1e2533] flex flex-col justify-between space-y-3">
              <div>
                <span className="text-xs font-bold text-amber-400 uppercase tracking-wider block mb-1">Preset 2: Velocity Surge</span>
                <h4 className="text-sm font-bold text-slate-200">2,500 Transactions (8% Fraud)</h4>
                <p className="text-xs text-slate-400 mt-1">Elevated card-not-present burst with 200 high-risk transactions across 300 entities.</p>
              </div>
              <Button
                variant="secondary"
                size="sm"
                icon={Play}
                isLoading={isGeneratingSynth}
                onClick={() => handleAdminGenerateSynthetic(undefined, 2500, 8.0)}
                className="w-full text-xs font-bold border-amber-600/40 text-amber-300 hover:bg-amber-950/30"
              >
                Generate 2,500 Tx
              </Button>
            </div>

            <div className="p-4 rounded-xl bg-[#0b0e14] border border-[#1e2533] flex flex-col justify-between space-y-3">
              <div>
                <span className="text-xs font-bold text-rose-400 uppercase tracking-wider block mb-1">Preset 3: Stress Benchmark</span>
                <h4 className="text-sm font-bold text-slate-200">5,000 Transactions (12% Fraud)</h4>
                <p className="text-xs text-slate-400 mt-1">Heavy enterprise simulation with 600 complex fraud anomalies for model benchmark.</p>
              </div>
              <Button
                variant="secondary"
                size="sm"
                icon={Play}
                isLoading={isGeneratingSynth}
                onClick={() => handleAdminGenerateSynthetic(undefined, 5000, 12.0)}
                className="w-full text-xs font-bold border-rose-600/40 text-rose-300 hover:bg-rose-950/30"
              >
                Generate 5,000 Tx
              </Button>
            </div>
          </div>
        </div>

        {/* Charts Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-5">
          {/* Risk Distribution */}
          <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-5 space-y-3 shadow-sm">
            <h4 className="text-xs font-bold text-slate-300 uppercase tracking-wider">
              Transaction Risk Distribution
            </h4>
            <div className="h-56">
              <ResponsiveContainer width="100%" height="100%">
                <BarChart data={charts.risk_distribution || [
                  { bin: 'Low (0-30)', count: 940 },
                  { bin: 'Med (31-70)', count: 194 },
                  { bin: 'High (71-100)', count: 66 }
                ]}>
                  <XAxis dataKey="bin" stroke="#475569" fontSize={10} />
                  <YAxis stroke="#475569" fontSize={10} />
                  <Tooltip contentStyle={{ backgroundColor: '#141822', borderColor: '#242c3d', borderRadius: 6, fontSize: 12 }} />
                  <Bar dataKey="count" fill="#10b981" radius={[4, 4, 0, 0]} />
                </BarChart>
              </ResponsiveContainer>
            </div>
          </div>

          {/* Incident Timeline */}
          <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-5 space-y-3 shadow-sm">
            <h4 className="text-xs font-bold text-slate-300 uppercase tracking-wider">
              24-Hour Transaction &amp; Anomaly Activity
            </h4>
            <div className="h-56">
              <ResponsiveContainer width="100%" height="100%">
                <AreaChart data={charts.timeline || [
                  { hour: '00:00', normal: 30, fraud: 1 },
                  { hour: '03:00', normal: 15, fraud: 8 },
                  { hour: '09:00', normal: 85, fraud: 2 },
                  { hour: '14:00', normal: 110, fraud: 4 },
                  { hour: '20:00', normal: 75, fraud: 3 }
                ]}>
                  <XAxis dataKey="hour" stroke="#475569" fontSize={10} />
                  <YAxis stroke="#475569" fontSize={10} />
                  <Tooltip contentStyle={{ backgroundColor: '#141822', borderColor: '#242c3d', borderRadius: 6, fontSize: 12 }} />
                  <Area type="monotone" dataKey="normal" stroke="#10b981" fill="#10b981" fillOpacity={0.15} />
                  <Area type="monotone" dataKey="fraud" stroke="#ef4444" fill="#ef4444" fillOpacity={0.25} />
                </AreaChart>
              </ResponsiveContainer>
            </div>
          </div>
        </div>

        {/* Recent Suspicious Transactions Queue */}
        <div className="bg-[#11141c] border border-[#1e2432] rounded-xl overflow-hidden shadow-sm">
          <div className="p-4 bg-[#141822] border-b border-[#1e2432] flex items-center justify-between">
            <div className="flex items-center space-x-2">
              <ShieldAlert className="w-4 h-4 text-rose-400" />
              <h4 className="text-xs font-bold text-slate-200 uppercase tracking-wider">
                Recent Suspicious Transactions Requiring Review
              </h4>
            </div>
            <button
              onClick={() => onNavigate('investigations')}
              className="text-xs text-emerald-400 hover:text-emerald-300 flex items-center space-x-1 font-semibold"
            >
              <span>View Investigation Desk</span>
              <ArrowRight className="w-3.5 h-3.5" />
            </button>
          </div>
          <div className="overflow-x-auto">
            <table className="w-full text-xs text-left">
              <thead className="bg-[#10141c] text-slate-400 border-b border-[#1e2432]">
                <tr>
                  <th className="px-4 py-2.5">Tx ID</th>
                  <th className="px-4 py-2.5">Amount</th>
                  <th className="px-4 py-2.5">Risk Score</th>
                  <th className="px-4 py-2.5">Level</th>
                  <th className="px-4 py-2.5">Timestamp</th>
                  <th className="px-4 py-2.5">Status</th>
                  <th className="px-4 py-2.5 text-right">Action</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-[#181d28] font-mono text-slate-300">
                {(telemetry?.recent_suspicious || [
                  { transaction_id: 'TXN-10452', amount: 185000, risk_score: 94, risk_level: 'HIGH', timestamp: '03:15:00', review_status: 'Under Review' },
                  { transaction_id: 'TXN-10891', amount: 240000, risk_score: 88, risk_level: 'HIGH', timestamp: '04:22:10', review_status: 'New' },
                  { transaction_id: 'TXN-10114', amount: 95000, risk_score: 78, risk_level: 'HIGH', timestamp: '02:40:15', review_status: 'Investigating' },
                ]).slice(0, 5).map((tx: any) => (
                  <tr key={tx.transaction_id} className="hover:bg-[#141822]">
                    <td className="px-4 py-3 font-bold text-slate-100">{tx.transaction_id}</td>
                    <td className="px-4 py-3 font-bold text-rose-400">₹{Number(tx.amount).toLocaleString()}</td>
                    <td className="px-4 py-3 font-bold text-rose-400">{tx.risk_score} / 100</td>
                    <td className="px-4 py-3">
                      <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-rose-950 text-rose-400 border border-rose-800/40">
                        {tx.risk_level || 'HIGH'}
                      </span>
                    </td>
                    <td className="px-4 py-3 text-slate-400">{tx.timestamp}</td>
                    <td className="px-4 py-3 font-sans text-slate-300">{tx.review_status?.value || tx.review_status || 'New'}</td>
                    <td className="px-4 py-3 text-right">
                      <button
                        onClick={() => onNavigate('investigations')}
                        className="text-xs text-emerald-400 hover:text-emerald-300 font-semibold"
                      >
                        Investigate &rarr;
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>

        {/* Administrator Custom Synthetic Data Generator Modal */}
        {showAdminSynthModal && (
          <div className="fixed inset-0 bg-black/80 backdrop-blur-sm flex items-center justify-center p-6 z-50 animate-in fade-in">
            <div className="bg-[#111622] border border-[#242e40] rounded-3xl max-w-lg w-full p-8 space-y-6 shadow-2xl">
              <div className="flex items-center justify-between pb-4 border-b border-[#202838]">
                <div className="flex items-center space-x-3">
                  <Sparkles className="w-6 h-6 text-emerald-400" />
                  <h4 className="text-lg font-bold text-slate-100">
                    Administrator Data Generator
                  </h4>
                </div>
                <button
                  onClick={() => setShowAdminSynthModal(false)}
                  className="text-slate-400 hover:text-slate-200 p-1"
                >
                  <X className="w-6 h-6" />
                </button>
              </div>

              <form onSubmit={(e) => handleAdminGenerateSynthetic(e)} className="space-y-5 text-sm">
                <div>
                  <label className="block text-slate-300 font-bold mb-1.5">Number of Transactions</label>
                  <input
                    type="number"
                    min={100}
                    max={50000}
                    value={synthRecords}
                    onChange={(e) => setSynthRecords(Number(e.target.value))}
                    className="w-full bg-[#0b0e14] border border-[#202838] rounded-xl px-4 py-2.5 text-slate-100 text-base font-mono focus:border-emerald-500 focus:outline-none"
                  />
                </div>

                <div>
                  <label className="block text-slate-300 font-bold mb-1.5">Target Fraud Ratio (%)</label>
                  <input
                    type="number"
                    min={0.5}
                    max={50}
                    step="0.1"
                    value={synthFraudPct}
                    onChange={(e) => setSynthFraudPct(Number(e.target.value))}
                    className="w-full bg-[#0b0e14] border border-[#202838] rounded-xl px-4 py-2.5 text-slate-100 text-base font-mono focus:border-emerald-500 focus:outline-none"
                  />
                </div>

                <div>
                  <label className="block text-slate-300 font-bold mb-1.5">Unique Customer Accounts</label>
                  <input
                    type="number"
                    min={10}
                    max={5000}
                    value={synthCustomers}
                    onChange={(e) => setSynthCustomers(Number(e.target.value))}
                    className="w-full bg-[#0b0e14] border border-[#202838] rounded-xl px-4 py-2.5 text-slate-100 text-base font-mono focus:border-emerald-500 focus:outline-none"
                  />
                </div>

                <div className="pt-3 flex justify-end space-x-3">
                  <Button type="button" variant="secondary" onClick={() => setShowAdminSynthModal(false)}>
                    Cancel
                  </Button>
                  <Button type="submit" variant="primary" icon={Sparkles} isLoading={isGeneratingSynth}>
                    Generate Dataset
                  </Button>
                </div>
              </form>
            </div>
          </div>
        )}
      </div>
    );
  }

  // ==========================================
  // 2. FRAUD ANALYST DASHBOARD
  // ==========================================
  if (isAnalyst) {
    return (
      <div className="w-full space-y-8 pb-16 font-sans">
        {/* Analyst Header */}
        <div className="w-full bg-[#111622] border border-[#1e2533] rounded-2xl p-6 flex flex-col md:flex-row md:items-center justify-between gap-6 shadow-md">
          <div>
            <div className="flex items-center space-x-2.5">
              <span className="px-3 py-1 rounded-lg bg-amber-950 text-amber-300 border border-amber-700/60 text-xs font-black font-mono tracking-wider">
                INVESTIGATION TRIAGE
              </span>
              <span className="text-slate-400 text-sm font-mono">&bull; Shift Status: Active</span>
            </div>
            <h2 className="text-2xl font-black text-slate-100 mt-2">Fraud Analyst Operational Dashboard</h2>
            <p className="text-sm text-slate-300 mt-1 font-medium">
              Prioritized caseload queue. Identify high-risk transactions requiring secondary verification, investigation review, or clearance.
            </p>
          </div>
          <div className="flex items-center space-x-3 shrink-0">
            <Button variant="primary" size="md" icon={ShieldAlert} onClick={() => onNavigate('investigations')}>
              Open Investigation Desk
            </Button>
          </div>
        </div>

        {/* Analyst Focus Cards (Workload Metric Row) */}
        <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
          <div className="bg-[#11141c] border border-rose-900/40 rounded-xl p-5 shadow-sm space-y-1">
            <span className="text-xs font-semibold text-rose-400 block uppercase tracking-wider">Cases Requiring Review</span>
            <div className="text-2xl font-extrabold text-slate-100 font-mono">
              {stats.cases_requiring_review || 124}
            </div>
            <span className="text-[11px] text-slate-500">Unresolved priority queue items</span>
          </div>

          <div className="bg-[#11141c] border border-amber-900/40 rounded-xl p-5 shadow-sm space-y-1">
            <span className="text-xs font-semibold text-amber-400 block uppercase tracking-wider">High Risk Transactions</span>
            <div className="text-2xl font-extrabold text-slate-100 font-mono">
              {stats.high_risk_transactions || 37}
            </div>
            <span className="text-[11px] text-slate-500">Risk Score &gt;= 70/100</span>
          </div>

          <div className="bg-[#11141c] border border-slate-800 rounded-xl p-5 shadow-sm space-y-1">
            <span className="text-xs font-semibold text-slate-300 block uppercase tracking-wider">Under Investigation</span>
            <div className="text-2xl font-extrabold text-slate-100 font-mono">
              {stats.under_investigation || 52}
            </div>
            <span className="text-[11px] text-slate-500">Assigned to auditor review</span>
          </div>

          <div className="bg-[#11141c] border border-emerald-900/40 rounded-xl p-5 shadow-sm space-y-1">
            <span className="text-xs font-semibold text-emerald-400 block uppercase tracking-wider">Cleared / False Positives</span>
            <div className="text-2xl font-extrabold text-slate-100 font-mono">
              {stats.cleared || 35}
            </div>
            <span className="text-[11px] text-slate-500">Verified as legitimate customer spending</span>
          </div>
        </div>

        {/* Priority Action Queue */}
        <div className="bg-[#11141c] border border-[#1e2432] rounded-xl overflow-hidden shadow-sm">
          <div className="p-4 bg-[#141822] border-b border-[#1e2432] flex items-center justify-between">
            <div className="flex items-center space-x-2">
              <ShieldAlert className="w-4 h-4 text-rose-500" />
              <h4 className="text-xs font-bold text-slate-200 uppercase tracking-wider">
                Priority Action Queue — Immediate Auditor Review
              </h4>
            </div>
            <span className="text-xs text-slate-400 font-mono">Action required before payment settlement</span>
          </div>

          <div className="divide-y divide-[#181d28] font-mono text-xs">
            {(telemetry?.priority_queue || [
              { transaction_id: 'TX10452', customer_id: 'CUST-1044', amount: 185000, risk_score: 94, risk_level: 'HIGH', location: 'Mumbai', device_type: 'Unknown Device', review_status: 'New' },
              { transaction_id: 'TX10891', customer_id: 'CUST-2081', amount: 240000, risk_score: 88, risk_level: 'HIGH', location: 'Bengaluru', device_type: 'New Emulated Device', review_status: 'Under Review' },
              { transaction_id: 'TX10114', customer_id: 'CUST-3902', amount: 95000, risk_score: 78, risk_level: 'HIGH', location: 'Delhi', device_type: 'Desktop Web Browser', review_status: 'Investigating' },
            ]).map((tx: any) => (
              <div key={tx.transaction_id} className="p-4 flex flex-col sm:flex-row sm:items-center justify-between gap-3 hover:bg-[#141822] transition-colors">
                <div className="space-y-1">
                  <div className="flex items-center space-x-3">
                    <span className="font-bold text-slate-100 text-sm">{tx.transaction_id}</span>
                    <span className="text-slate-400">({tx.customer_id})</span>
                    <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-rose-950 text-rose-400 border border-rose-800/40">
                      Score: {tx.risk_score}/100 &bull; {tx.risk_level || 'HIGH'}
                    </span>
                  </div>
                  <div className="text-slate-400 font-sans text-xs flex items-center space-x-3">
                    <span>Location: <strong className="text-slate-200 font-mono">{tx.location}</strong></span>
                    <span>&bull;</span>
                    <span>Device: <strong className="text-slate-200">{tx.device_type}</strong></span>
                    <span>&bull;</span>
                    <span>Status: <strong className="text-amber-400">{tx.review_status?.value || tx.review_status || 'New'}</strong></span>
                  </div>
                </div>

                <div className="flex items-center space-x-3 shrink-0">
                  <span className="text-rose-400 font-bold text-base">
                    ₹{Number(tx.amount).toLocaleString('en-IN', { minimumFractionDigits: 2 })}
                  </span>
                  <Button
                    size="sm"
                    variant="primary"
                    onClick={() => onNavigate('investigations')}
                  >
                    Open Case
                  </Button>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    );
  }

  // ==========================================
  // 3. MANAGEMENT / VIEWER DASHBOARD
  // ==========================================
  return (
    <div className="w-full space-y-8 pb-16 font-sans">
      {/* Viewer Header */}
      <div className="w-full bg-[#111622] border border-[#1e2533] rounded-2xl p-6 flex flex-col md:flex-row md:items-center justify-between gap-6 shadow-md">
        <div>
          <div className="flex items-center space-x-2.5">
            <span className="px-3 py-1 rounded-lg bg-slate-800 text-slate-200 border border-slate-600 text-xs font-black font-mono tracking-wider">
              EXECUTIVE RISK OVERVIEW
            </span>
            <span className="text-slate-400 text-sm font-mono">&bull; Read-Only Reporting Access</span>
          </div>
          <h2 className="text-2xl font-black text-slate-100 mt-2">Financial Risk &amp; Loss Exposure Summary</h2>
          <p className="text-sm text-slate-300 mt-1 font-medium">
            High-level executive metrics detailing overall portfolio health, intercepted fraud exposure, and risk mitigation trends.
          </p>
        </div>
        <div className="flex items-center space-x-3 shrink-0">
          <Button variant="primary" size="md" icon={Eye} onClick={() => onNavigate('reports')}>
            Executive Reports
          </Button>
        </div>
      </div>

      {/* Viewer Executive Metrics */}
      <div className="grid grid-cols-2 lg:grid-cols-5 gap-4">
        <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-5 shadow-sm space-y-1">
          <span className="text-xs font-semibold text-slate-400 block uppercase tracking-wider">Total Transactions</span>
          <div className="text-2xl font-extrabold text-slate-100 font-mono">
            {stats.total_transactions ? Number(stats.total_transactions).toLocaleString() : '100,000'}
          </div>
          <span className="text-[11px] text-slate-500">Gross monitored volume</span>
        </div>

        <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-5 shadow-sm space-y-1">
          <span className="text-xs font-semibold text-emerald-400 block uppercase tracking-wider">Normal Transactions</span>
          <div className="text-2xl font-extrabold text-slate-100 font-mono">
            {stats.normal_transactions ? Number(stats.normal_transactions).toLocaleString() : '96,400'}
          </div>
          <span className="text-[11px] text-slate-500">Clean processing rate: 96.4%</span>
        </div>

        <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-5 shadow-sm space-y-1">
          <span className="text-xs font-semibold text-amber-400 block uppercase tracking-wider">Suspicious Transactions</span>
          <div className="text-2xl font-extrabold text-slate-100 font-mono">
            {stats.suspicious_transactions ? Number(stats.suspicious_transactions).toLocaleString() : '3,600'}
          </div>
          <span className="text-[11px] text-slate-500">Intercepted by ML scoring</span>
        </div>

        <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-5 shadow-sm space-y-1">
          <span className="text-xs font-semibold text-rose-400 block uppercase tracking-wider">High Risk</span>
          <div className="text-2xl font-extrabold text-slate-100 font-mono">
            {stats.high_risk || 425}
          </div>
          <span className="text-[11px] text-slate-500">Immediate hold exposure</span>
        </div>

        <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-5 shadow-sm space-y-1">
          <span className="text-xs font-semibold text-emerald-400 block uppercase tracking-wider">Fraud Incident Rate</span>
          <div className="text-2xl font-extrabold text-emerald-400 font-mono">
            {stats.fraud_rate || 3.6}%
          </div>
          <span className="text-[11px] text-slate-500">Industry benchmark: 2-5%</span>
        </div>
      </div>

      {/* Executive Key Takeaways */}
      <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-5 space-y-3 shadow-sm">
        <h4 className="text-xs font-bold text-slate-200 uppercase tracking-wider flex items-center space-x-2">
          <Award className="w-4 h-4 text-emerald-400" />
          <span>Executive Loss Mitigation Assessment</span>
        </h4>
        <div className="space-y-2">
          {(telemetry?.executive_notes || [
            'Overall fraud incident rate is tracking at 3.6%, within the acceptable FinTech risk boundary.',
            'Automated ML risk scoring intercepted an estimated ₹42,68,000 in fraudulent attempts before settlement.',
            'Primary vulnerability identified: nocturnal high-value transfers initiated from untrusted hardware signatures.'
          ]).map((note: string, idx: number) => (
            <div key={idx} className="p-3 bg-[#0b0e14] rounded-lg border border-[#1e2432] text-xs text-slate-300 flex items-start space-x-2">
              <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0 mt-0.5" />
              <span>{note}</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
