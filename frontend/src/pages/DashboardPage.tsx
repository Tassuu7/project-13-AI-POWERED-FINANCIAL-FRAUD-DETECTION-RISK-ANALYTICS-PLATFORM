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
  Award
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
  const { selectedDataset, activeModel } = useAppState();

  const [telemetry, setTelemetry] = useState<any>(null);
  const [isLoading, setIsLoading] = useState<boolean>(true);

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
          <div className="flex items-center space-x-3 shrink-0">
            <Button variant="secondary" size="md" icon={RefreshCw} onClick={loadTelemetry} isLoading={isLoading}>
              Refresh Telemetry
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
