import React, { useState, useEffect } from 'react';
import {
  ResponsiveContainer,
  PieChart,
  Pie,
  Cell,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  Legend,
  AreaChart,
  Area
} from 'recharts';
import {
  ShieldAlert,
  ShieldCheck,
  TrendingUp,
  Activity,
  DollarSign,
  AlertTriangle,
  RefreshCw,
  Award
} from 'lucide-react';
import { useAppState } from '../context/AppStateContext';
import { api } from '../services/api';
import { StatCard } from '../components/common/StatCard';
import { Button } from '../components/common/Button';

export const DashboardPage: React.FC = () => {
  const { selectedDataset } = useAppState();
  const [data, setData] = useState<any>(null);
  const [modelMetrics, setModelMetrics] = useState<any>(null);
  const [isLoading, setIsLoading] = useState<boolean>(true);

  const loadDashboardData = async () => {
    setIsLoading(true);
    try {
      const edaSummary = await api.getEdaSummary(selectedDataset);
      setData(edaSummary);

      const models = await api.listTrainedModels();
      if (models && models.length > 0) {
        // Find best or first model
        const best = models.find((m: any) => m.metrics?.is_best) || models[0];
        setModelMetrics(best.metrics || null);
      }
    } catch (err) {
      console.warn('Dashboard data fetch error:', err);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    if (selectedDataset) {
      loadDashboardData();
    }
  }, [selectedDataset]);

  if (isLoading) {
    return (
      <div className="flex flex-col items-center justify-center h-96 space-y-3">
        <RefreshCw className="w-8 h-8 text-emerald-400 animate-spin" />
        <span className="text-sm text-slate-400">Loading risk analytics dashboard for {selectedDataset}...</span>
      </div>
    );
  }

  if (!data || data.error) {
    return (
      <div className="bg-[#11141c] border border-[#1e2432] rounded-lg p-8 text-center max-w-lg mx-auto my-12">
        <AlertTriangle className="w-10 h-10 text-amber-400 mx-auto mb-3" />
        <h3 className="text-base font-bold text-slate-200">No Dataset Data Available</h3>
        <p className="text-xs text-slate-400 mt-1 mb-4">
          Upload or generate a synthetic dataset to view risk analytics and trends.
        </p>
        <Button variant="primary" onClick={loadDashboardData} icon={RefreshCw}>
          Retry Load
        </Button>
      </div>
    );
  }

  // Risk Distribution Data (Derived from ground truth & thresholds)
  const total = data.total_transactions || 1;
  const fraud = data.fraud_count || 0;
  const normal = data.normal_count || (total - fraud);
  const mediumRisk = Math.round(total * 0.08);
  const highRisk = fraud;
  const lowRisk = Math.max(0, total - highRisk - mediumRisk);

  const riskPieData = [
    { name: 'Low Risk', value: lowRisk, color: '#10b981' },
    { name: 'Medium Risk', value: mediumRisk, color: '#f59e0b' },
    { name: 'High Risk', value: highRisk, color: '#ef4444' },
  ];

  return (
    <div className="space-y-6 pb-12">
      {/* Top Controls & Status Bar */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 bg-[#11141c] border border-[#1d2330] p-4 rounded-lg">
        <div>
          <span className="text-xs text-slate-400">Target Investigation Dataset:</span>
          <span className="ml-2 text-sm font-bold text-emerald-400 font-mono">{selectedDataset}</span>
        </div>
        <div className="flex items-center space-x-3">
          <Button variant="secondary" size="sm" icon={RefreshCw} onClick={loadDashboardData}>
            Refresh Analytics
          </Button>
        </div>
      </div>

      {/* Row 1: Primary Metrics */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <StatCard
          title="Total Transactions"
          value={total.toLocaleString()}
          subtitle={`Analyzed in ${selectedDataset}`}
          icon={Activity}
          color="slate"
        />
        <StatCard
          title="Normal Transactions"
          value={normal.toLocaleString()}
          subtitle={`${((normal / total) * 100).toFixed(1)}% of total volume`}
          icon={ShieldCheck}
          color="emerald"
        />
        <StatCard
          title="Suspicious / Fraudulent"
          value={fraud.toLocaleString()}
          subtitle={`${data.fraud_rate}% incident rate`}
          icon={ShieldAlert}
          color="rose"
        />
        <StatCard
          title="Total Volume (INR)"
          value={`₹${(data.total_volume_inr || 0).toLocaleString('en-IN')}`}
          subtitle={`Avg: ₹${(data.avg_amount_inr || 0).toFixed(2)}`}
          icon={DollarSign}
          color="amber"
        />
      </div>

      {/* Row 2: ML Model Benchmark Strip */}
      {modelMetrics && (
        <div className="bg-[#121620] border border-[#202736] rounded-lg p-4">
          <div className="flex items-center justify-between mb-3">
            <div className="flex items-center space-x-2">
              <Award className="w-4 h-4 text-emerald-400" />
              <span className="text-xs font-bold text-slate-200 uppercase tracking-wider">
                Active ML Performance Benchmark ({modelMetrics.model_name})
              </span>
            </div>
            <span className="text-[11px] text-emerald-400 font-mono bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40">
              Latency: {modelMetrics.training_time_seconds}s
            </span>
          </div>
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
            <div className="bg-[#0c0f16] p-2.5 rounded border border-[#1a202c]">
              <span className="text-[11px] text-slate-400">Accuracy</span>
              <div className="text-lg font-bold text-slate-100 font-mono">
                {(modelMetrics.accuracy * 100).toFixed(1)}%
              </div>
            </div>
            <div className="bg-[#0c0f16] p-2.5 rounded border border-[#1a202c]">
              <span className="text-[11px] text-slate-400">Precision</span>
              <div className="text-lg font-bold text-emerald-400 font-mono">
                {(modelMetrics.precision * 100).toFixed(1)}%
              </div>
            </div>
            <div className="bg-[#0c0f16] p-2.5 rounded border border-[#1a202c]">
              <span className="text-[11px] text-slate-400">Recall</span>
              <div className="text-lg font-bold text-emerald-400 font-mono">
                {(modelMetrics.recall * 100).toFixed(1)}%
              </div>
            </div>
            <div className="bg-[#0c0f16] p-2.5 rounded border border-[#1a202c]">
              <span className="text-[11px] text-slate-400">F1-Score</span>
              <div className="text-lg font-bold text-amber-400 font-mono">
                {(modelMetrics.f1_score * 100).toFixed(1)}%
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Row 3: Charts - Risk Distribution & Hourly Trends */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Risk Distribution Donut */}
        <div className="bg-[#11141c] border border-[#1d2330] rounded-lg p-4 flex flex-col justify-between">
          <h3 className="text-xs font-bold text-slate-300 uppercase tracking-wider mb-2">
            Risk Tier Distribution
          </h3>
          <div className="h-60">
            <ResponsiveContainer width="100%" height="100%">
              <PieChart>
                <Pie
                  data={riskPieData}
                  dataKey="value"
                  nameKey="name"
                  cx="50%"
                  cy="50%"
                  innerRadius={55}
                  outerRadius={80}
                  paddingAngle={3}
                >
                  {riskPieData.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={entry.color} stroke="#11141c" strokeWidth={2} />
                  ))}
                </Pie>
                <Tooltip
                  contentStyle={{ backgroundColor: '#141822', borderColor: '#242c3d', borderRadius: 6, color: '#f8fafc', fontSize: 12 }}
                />
                <Legend verticalAlign="bottom" height={36} wrapperStyle={{ fontSize: 11, color: '#94a3b8' }} />
              </PieChart>
            </ResponsiveContainer>
          </div>
          <div className="grid grid-cols-3 gap-2 text-center pt-2 border-t border-[#1d2330] text-[11px]">
            <div>
              <span className="text-emerald-400 font-semibold">{lowRisk}</span>
              <span className="block text-slate-400">Low</span>
            </div>
            <div>
              <span className="text-amber-400 font-semibold">{mediumRisk}</span>
              <span className="block text-slate-400">Medium</span>
            </div>
            <div>
              <span className="text-rose-400 font-semibold">{highRisk}</span>
              <span className="block text-slate-400">High</span>
            </div>
          </div>
        </div>

        {/* 24-Hour Timeline */}
        <div className="lg:col-span-2 bg-[#11141c] border border-[#1d2330] rounded-lg p-4">
          <div className="flex items-center justify-between mb-2">
            <h3 className="text-xs font-bold text-slate-300 uppercase tracking-wider">
              24-Hour Transaction &amp; Fraud Trend
            </h3>
            <span className="text-[11px] text-rose-400 font-medium bg-rose-950/40 px-2 py-0.5 rounded border border-rose-800/30">
              Vulnerable Window: 01:00 - 05:00
            </span>
          </div>
          <div className="h-64">
            <ResponsiveContainer width="100%" height="100%">
              <AreaChart data={data.by_hour || []}>
                <defs>
                  <linearGradient id="colorTotal" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="5%" stopColor="#10b981" stopOpacity={0.3}/>
                    <stop offset="95%" stopColor="#10b981" stopOpacity={0}/>
                  </linearGradient>
                  <linearGradient id="colorFraud" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="5%" stopColor="#ef4444" stopOpacity={0.4}/>
                    <stop offset="95%" stopColor="#ef4444" stopOpacity={0}/>
                  </linearGradient>
                </defs>
                <XAxis dataKey="hour" stroke="#475569" fontSize={11} />
                <YAxis stroke="#475569" fontSize={11} />
                <Tooltip contentStyle={{ backgroundColor: '#141822', borderColor: '#242c3d', borderRadius: 6, fontSize: 12 }} />
                <Area type="monotone" dataKey="total" name="Total Txns" stroke="#10b981" fillOpacity={1} fill="url(#colorTotal)" />
                <Area type="monotone" dataKey="fraud" name="Fraud Txns" stroke="#ef4444" fillOpacity={1} fill="url(#colorFraud)" />
              </AreaChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>

      {/* Row 4: Category & Location Breakdowns */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Fraud by Transaction Type */}
        <div className="bg-[#11141c] border border-[#1d2330] rounded-lg p-4">
          <h3 className="text-xs font-bold text-slate-300 uppercase tracking-wider mb-3">
            Fraud Incident Rate by Channel
          </h3>
          <div className="h-60">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={data.by_transaction_type || []} layout="vertical">
                <XAxis type="number" stroke="#475569" fontSize={11} unit="%" />
                <YAxis dataKey="category" type="category" stroke="#475569" fontSize={10} width={100} />
                <Tooltip contentStyle={{ backgroundColor: '#141822', borderColor: '#242c3d', borderRadius: 6, fontSize: 12 }} />
                <Bar dataKey="fraud_rate" name="Fraud %" fill="#f59e0b" radius={[0, 4, 4, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* Amount Buckets */}
        <div className="bg-[#11141c] border border-[#1d2330] rounded-lg p-4">
          <h3 className="text-xs font-bold text-slate-300 uppercase tracking-wider mb-3">
            Transaction Exposure by Amount Range
          </h3>
          <div className="h-60">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={data.amount_distribution || []}>
                <XAxis dataKey="bucket" stroke="#475569" fontSize={10} />
                <YAxis stroke="#475569" fontSize={11} />
                <Tooltip contentStyle={{ backgroundColor: '#141822', borderColor: '#242c3d', borderRadius: 6, fontSize: 12 }} />
                <Legend wrapperStyle={{ fontSize: 11 }} />
                <Bar dataKey="normal" name="Normal" fill="#10b981" stackId="a" />
                <Bar dataKey="fraud" name="Fraud" fill="#ef4444" stackId="a" />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>
    </div>
  );
};
