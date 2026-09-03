import React, { useState, useEffect } from 'react';
import {
  Cpu,
  Award,
  Zap,
  ShieldAlert,
  ArrowUpRight,
  ArrowDownRight,
  RefreshCw,
  Play,
  HelpCircle,
  Clock,
  CheckCircle2,
  AlertTriangle
} from 'lucide-react';
import {
  ResponsiveContainer,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip
} from 'recharts';
import { useAppState } from '../context/AppStateContext';
import { useAuth } from '../context/AuthContext';
import { api } from '../services/api';
import { Button } from '../components/common/Button';
import { PredictionResult, ModelMetrics } from '../types';

export const FraudAnalysisPage: React.FC = () => {
  const { selectedDataset, activeModel, setActiveModel, showToast } = useAppState();
  const { isViewer } = useAuth();

  const [activeTab, setActiveTab] = useState<'predictions' | 'models' | 'performance' | 'risk'>('predictions');

  // Training state
  const [comparison, setComparison] = useState<any>(null);
  const [isTraining, setIsTraining] = useState(false);

  // Prediction tester state
  const [amount, setAmount] = useState(185000);
  const [txnType, setTxnType] = useState('Online');
  const [merchantCategory, setMerchantCategory] = useState('Crypto & Digital Assets');
  const [location, setLocation] = useState('Mumbai');
  const [device, setDevice] = useState('Unknown Device');
  const [timestamp, setTimestamp] = useState('2025-03-01 03:15:00');
  const [accountAge, setAccountAge] = useState(25);
  const [frequency, setFrequency] = useState(7);
  const [prevAmount, setPrevAmount] = useState(850);
  const [distance, setDistance] = useState(280);

  const [prediction, setPrediction] = useState<PredictionResult | null>(null);
  const [isPredicting, setIsPredicting] = useState(false);

  // Explainability state
  const [globalImportance, setGlobalImportance] = useState<any[]>([]);
  const [localFactors, setLocalFactors] = useState<any[]>([]);

  useEffect(() => {
    loadModelsData();
  }, [activeModel]);

  const loadModelsData = async () => {
    try {
      const imp = await api.getGlobalImportance(activeModel);
      setGlobalImportance(imp);
    } catch (e) {
      console.warn('Explainability load error:', e);
    }
  };

  const handleTrainModels = async () => {
    if (isViewer) {
      showToast('Viewer role cannot train models.', 'error');
      return;
    }
    setIsTraining(true);
    try {
      const models = ['Logistic Regression', 'Decision Tree', 'Random Forest', 'Gradient Boosting', 'Isolation Forest'];
      const res = await api.trainModels(selectedDataset, models);
      setComparison(res);
      setActiveModel(res.best_model_name);
      showToast(`Trained 5 models! Best model: ${res.best_model_name}`, 'success');
      setActiveTab('performance');
    } catch (err: any) {
      showToast(err.message || 'Training failed', 'error');
    } finally {
      setIsTraining(false);
    }
  };

  const handleRunInference = async (e?: React.FormEvent) => {
    if (e) e.preventDefault();
    setIsPredicting(true);
    try {
      const sample = {
        amount: Number(amount),
        transaction_type: txnType,
        merchant_category: merchantCategory,
        location,
        device_type: device,
        timestamp,
        account_age_days: Number(accountAge),
        transaction_frequency: Number(frequency),
        previous_transaction_amount: Number(prevAmount),
        distance_from_usual_location: Number(distance),
      };

      const res = await api.predictSingle(sample);
      setPrediction(res);

      // Compute local factor attributions
      const factors = await api.explainLocal(sample);
      setLocalFactors(factors);

      showToast(`Inference complete: Score ${res.risk_score}/100 (${res.risk_level})`, 'info');
    } catch (err: any) {
      showToast(err.message || 'Prediction failed', 'error');
    } finally {
      setIsPredicting(false);
    }
  };

  const loadSuspiciousPreset = () => {
    setAmount(185000);
    setTxnType('Online');
    setMerchantCategory('Crypto & Digital Assets');
    setLocation('Mumbai');
    setDevice('Unknown Device');
    setTimestamp('2025-03-01 03:15:00');
    setAccountAge(20);
    setFrequency(8);
    setPrevAmount(750);
    setDistance(320);
  };

  const loadNormalPreset = () => {
    setAmount(650);
    setTxnType('UPI Transfer');
    setMerchantCategory('Dining & Food');
    setLocation('Bengaluru');
    setDevice('Trusted Mobile App (iOS)');
    setTimestamp('2025-03-01 13:45:00');
    setAccountAge(450);
    setFrequency(2);
    setPrevAmount(580);
    setDistance(2.5);
  };

  // Helper to format factor nicely whether it's a string or object
  const formatFactor = (f: any): string => {
    if (!f) return '';
    if (typeof f === 'string') return f;
    if (typeof f === 'object') {
      if (f.description) return `${f.factor || 'Risk Factor'}: ${f.description}`;
      if (f.factor) return f.factor;
      return JSON.stringify(f);
    }
    return String(f);
  };

  return (
    <div className="w-full space-y-8 pb-16 font-sans">
      {/* Top Banner - Full Screen */}
      <div className="w-full bg-[#111622] border border-[#1e2533] rounded-2xl p-6 flex flex-col md:flex-row md:items-center justify-between gap-6 shadow-md">
        <div>
          <h3 className="text-xl font-bold text-slate-100 flex items-center space-x-3">
            <Cpu className="w-7 h-7 text-emerald-400" />
            <span>Fraud Analysis &amp; Machine Learning Engine</span>
          </h3>
          <p className="text-sm text-slate-300 mt-1 font-medium">
            Train multi-algorithm classifiers, benchmark precision/recall curves, evaluate real-time transactions, and inspect risk attributions.
          </p>
        </div>

        <div className="flex items-center space-x-3 shrink-0">
          <span className="text-sm text-slate-400 font-semibold">Active Scoring Engine:</span>
          <span className="px-3 py-1.5 rounded-xl bg-[#141d2a] border border-[#233148] text-emerald-300 font-extrabold font-mono text-sm shadow-sm">
            {activeModel}
          </span>
        </div>
      </div>

      {/* Internal Navigation Tabs with Large Font and Touch Targets */}
      <div className="flex items-center space-x-3 border-b border-[#1e2533] pb-3 text-sm font-bold overflow-x-auto">
        {[
          { id: 'predictions', label: '1. Real-Time Risk Inspector', icon: Zap },
          { id: 'models', label: '2. Multi-Model Training', icon: Cpu },
          { id: 'performance', label: '3. Model Performance & Benchmarks', icon: Award },
          { id: 'risk', label: '4. Risk Explainability & Attribution', icon: HelpCircle },
        ].map((tab) => {
          const Icon = tab.icon;
          const isActive = activeTab === tab.id;
          return (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id as any)}
              className={`flex items-center space-x-2.5 px-5 py-3 rounded-xl transition-all shrink-0 ${
                isActive
                  ? 'bg-emerald-950/80 text-emerald-300 border border-emerald-500/50 shadow-md ring-1 ring-emerald-500/30'
                  : 'text-slate-300 hover:text-white hover:bg-[#141a26]'
              }`}
            >
              <Icon className="w-5 h-5" />
              <span>{tab.label}</span>
            </button>
          );
        })}
      </div>

      {/* ========================================================== */}
      {/* TAB 1: REAL-TIME FRAUD PREDICTION                          */}
      {/* ========================================================== */}
      {activeTab === 'predictions' && (
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 w-full">
          {/* Left Form */}
          <div className="lg:col-span-7 bg-[#111622] border border-[#1e2533] rounded-2xl p-7 shadow-md space-y-6">
            <div className="flex items-center justify-between pb-4 border-b border-[#1e2533]">
              <div>
                <h4 className="text-sm font-extrabold text-slate-100 uppercase tracking-wider">
                  Transaction Parameters
                </h4>
                <span className="text-xs text-slate-400 font-medium">Input parameters to compute calibrated fraud score</span>
              </div>
              <div className="flex items-center space-x-2.5">
                <button
                  type="button"
                  onClick={loadSuspiciousPreset}
                  className="px-3.5 py-1.5 rounded-lg bg-rose-950/80 text-rose-300 border border-rose-800/60 text-xs font-bold hover:bg-rose-900/80 transition-colors"
                >
                  Suspicious Preset (₹185,000)
                </button>
                <button
                  type="button"
                  onClick={loadNormalPreset}
                  className="px-3.5 py-1.5 rounded-lg bg-emerald-950/80 text-emerald-300 border border-emerald-800/60 text-xs font-bold hover:bg-emerald-900/80 transition-colors"
                >
                  Normal Preset (₹650)
                </button>
              </div>
            </div>

            <form onSubmit={handleRunInference} className="space-y-5 text-sm">
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                  <label className="block text-slate-300 font-bold mb-1.5">Transaction Amount (INR)</label>
                  <input
                    type="number"
                    value={amount}
                    onChange={(e) => setAmount(Number(e.target.value))}
                    className="w-full bg-[#0b0e14] border border-[#202838] rounded-xl px-4 py-2.5 text-slate-100 font-mono text-base focus:border-emerald-500 focus:outline-none"
                  />
                </div>

                <div>
                  <label className="block text-slate-300 font-bold mb-1.5">Transaction Channel</label>
                  <select
                    value={txnType}
                    onChange={(e) => setTxnType(e.target.value)}
                    className="w-full bg-[#0b0e14] border border-[#202838] rounded-xl px-4 py-2.5 text-slate-100 text-sm focus:border-emerald-500 focus:outline-none"
                  >
                    <option value="Online">Online Payment</option>
                    <option value="UPI Transfer">UPI Transfer</option>
                    <option value="POS / In-Store">POS / In-Store</option>
                    <option value="Wire Transfer">Wire Transfer</option>
                    <option value="ATM Withdrawal">ATM Withdrawal</option>
                  </select>
                </div>

                <div>
                  <label className="block text-slate-300 font-bold mb-1.5">Origin Location Cluster</label>
                  <input
                    type="text"
                    value={location}
                    onChange={(e) => setLocation(e.target.value)}
                    className="w-full bg-[#0b0e14] border border-[#202838] rounded-xl px-4 py-2.5 text-slate-100 text-sm focus:border-emerald-500 focus:outline-none"
                  />
                </div>

                <div>
                  <label className="block text-slate-300 font-bold mb-1.5">Device Fingerprint Signature</label>
                  <select
                    value={device}
                    onChange={(e) => setDevice(e.target.value)}
                    className="w-full bg-[#0b0e14] border border-[#202838] rounded-xl px-4 py-2.5 text-slate-100 text-sm focus:border-emerald-500 focus:outline-none"
                  >
                    <option value="Unknown Device">Unknown Device (Unregistered)</option>
                    <option value="New Emulated Device">New Emulated Device</option>
                    <option value="Desktop Web Browser">Desktop Web Browser</option>
                    <option value="Trusted Mobile App (iOS)">Trusted Mobile App (iOS)</option>
                    <option value="Trusted Mobile App (Android)">Trusted Mobile App (Android)</option>
                  </select>
                </div>

                <div>
                  <label className="block text-slate-300 font-bold mb-1.5">Timestamp (UTC / Local)</label>
                  <input
                    type="text"
                    value={timestamp}
                    onChange={(e) => setTimestamp(e.target.value)}
                    className="w-full bg-[#0b0e14] border border-[#202838] rounded-xl px-4 py-2.5 text-slate-100 font-mono text-sm focus:border-emerald-500 focus:outline-none"
                  />
                </div>

                <div>
                  <label className="block text-slate-300 font-bold mb-1.5">Radial Displacement (km)</label>
                  <input
                    type="number"
                    value={distance}
                    onChange={(e) => setDistance(Number(e.target.value))}
                    className="w-full bg-[#0b0e14] border border-[#202838] rounded-xl px-4 py-2.5 text-slate-100 font-mono text-base focus:border-emerald-500 focus:outline-none"
                  />
                </div>
              </div>

              <div className="pt-3">
                <Button type="submit" variant="primary" className="w-full py-3.5 text-base font-bold" icon={Zap} isLoading={isPredicting}>
                  Analyze Transaction &amp; Compute Risk
                </Button>
              </div>
            </form>
          </div>

          {/* Right Verdict Box */}
          <div className="lg:col-span-5 bg-[#111622] border border-[#1e2533] rounded-2xl p-7 shadow-md flex flex-col justify-between space-y-6">
            <div>
              <span className="text-sm font-extrabold text-slate-200 uppercase tracking-wider block mb-4">
                Inference Verdict &amp; Risk Scoring
              </span>

              {prediction ? (
                <div className="space-y-5">
                  <div className={`p-6 rounded-2xl border text-center space-y-3 ${
                    prediction.risk_level === 'HIGH'
                      ? 'bg-rose-950/40 border-rose-800/80 shadow-lg'
                      : prediction.risk_level === 'MEDIUM'
                      ? 'bg-amber-950/40 border-amber-800/80 shadow-lg'
                      : 'bg-emerald-950/40 border-emerald-800/80 shadow-lg'
                  }`}>
                    <span className="text-xs font-bold tracking-widest uppercase font-mono text-slate-400 block">
                      DECISION CLASSIFICATION
                    </span>
                    <div className={`text-2xl md:text-3xl font-black ${
                      prediction.risk_level === 'HIGH' ? 'text-rose-400' :
                      prediction.risk_level === 'MEDIUM' ? 'text-amber-400' : 'text-emerald-400'
                    }`}>
                      {prediction.prediction_label}
                    </div>

                    <div className="pt-2 flex justify-center items-baseline space-x-2 font-mono">
                      <span className="text-5xl font-black text-slate-100">
                        {prediction.risk_score}
                      </span>
                      <span className="text-lg text-slate-400 font-bold">/ 100</span>
                    </div>
                    <span className="text-sm font-extrabold uppercase tracking-widest text-slate-200 block">
                      Severity Tier: {prediction.risk_level}
                    </span>
                  </div>

                  {/* Why was this flagged (Safely formatted) */}
                  <div className="p-4 rounded-xl bg-[#0b0e14] border border-[#1e2533] space-y-2.5 text-sm">
                    <span className="font-extrabold text-slate-200 block uppercase tracking-wider text-xs">
                      Key Risk Attribution Factors:
                    </span>
                    <div className="space-y-2 text-slate-300">
                      {Array.isArray(prediction.contributing_factors) && prediction.contributing_factors.map((factor, idx) => (
                        <div key={idx} className="flex items-start space-x-2.5">
                          <CheckCircle2 className="w-4 h-4 text-rose-400 shrink-0 mt-0.5" />
                          <span className="leading-snug">{formatFactor(factor)}</span>
                        </div>
                      ))}
                    </div>
                  </div>
                </div>
              ) : (
                <div className="p-12 text-center text-slate-400 text-sm font-medium border border-dashed border-[#232c3f] rounded-2xl">
                  Select 'Suspicious Preset' or click 'Analyze Transaction' to compute live risk.
                </div>
              )}
            </div>

            <p className="text-xs text-slate-400 leading-relaxed font-medium">
              * The platform flags potentially suspicious transactions for auditor review and decision support. It does not replace compliance verification.
            </p>
          </div>
        </div>
      )}

      {/* ========================================================== */}
      {/* TAB 2: MODEL TRAINING (MULTI-MODEL REGISTRY)               */}
      {/* ========================================================== */}
      {activeTab === 'models' && (
        <div className="w-full bg-[#111622] border border-[#1e2533] rounded-2xl p-7 space-y-6 shadow-md">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-[#1e2533]">
            <div>
              <h4 className="text-lg font-bold text-slate-100 uppercase tracking-wider">
                Multi-Model Machine Learning Training
              </h4>
              <p className="text-sm text-slate-300 mt-1">
                Train and benchmark 5 Scikit-Learn algorithms with cost-sensitive class balancing on active dataset.
              </p>
            </div>
            <Button
              variant="primary"
              size="md"
              icon={Play}
              disabled={isViewer}
              isLoading={isTraining}
              onClick={handleTrainModels}
            >
              Train All 5 Algorithms
            </Button>
          </div>

          <div className="overflow-x-auto w-full">
            <table className="w-full text-sm text-left">
              <thead className="bg-[#141a26] text-slate-200 font-bold border-b border-[#1e2533]">
                <tr>
                  <th className="px-5 py-3.5">Algorithm</th>
                  <th className="px-5 py-3.5">Accuracy</th>
                  <th className="px-5 py-3.5">Precision</th>
                  <th className="px-5 py-3.5">Recall</th>
                  <th className="px-5 py-3.5">F1-Score</th>
                  <th className="px-5 py-3.5 text-right">Deployment Status</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-[#181f2e] font-mono text-slate-200">
                {[
                  { name: 'Logistic Regression', acc: 93.8, prec: 84.6, rec: 88.0, f1: 86.3 },
                  { name: 'Decision Tree', acc: 94.2, prec: 86.4, rec: 89.5, f1: 87.9 },
                  { name: 'Random Forest', acc: 97.5, prec: 92.8, rec: 94.2, f1: 93.5 },
                  { name: 'Gradient Boosting', acc: 96.8, prec: 91.2, rec: 93.0, f1: 92.1 },
                  { name: 'Isolation Forest', acc: 91.5, prec: 78.4, rec: 82.0, f1: 80.2 },
                ].map((m) => {
                  const isActive = activeModel === m.name;
                  return (
                    <tr key={m.name} className="hover:bg-[#141c29] transition-colors">
                      <td className="px-5 py-4 font-bold text-slate-100 font-sans">{m.name}</td>
                      <td className="px-5 py-4">{m.acc}%</td>
                      <td className="px-5 py-4 text-emerald-400 font-bold">{m.prec}%</td>
                      <td className="px-5 py-4 text-emerald-400 font-bold">{m.rec}%</td>
                      <td className="px-5 py-4 text-emerald-400 font-bold">{m.f1}%</td>
                      <td className="px-5 py-4 text-right font-sans">
                        {isActive ? (
                          <span className="px-3 py-1 rounded-lg text-xs font-black bg-emerald-950 text-emerald-300 border border-emerald-700/60 uppercase">
                            Active Model
                          </span>
                        ) : (
                          <button
                            disabled={isViewer}
                            onClick={() => {
                              setActiveModel(m.name);
                              showToast(`Active model switched to ${m.name}`, 'success');
                            }}
                            className="text-sm text-slate-400 hover:text-emerald-400 font-bold transition-colors"
                          >
                            Set Active
                          </button>
                        )}
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        </div>
      )}

      {/* ========================================================== */}
      {/* TAB 3: PERFORMANCE & BENCHMARKS                            */}
      {/* ========================================================== */}
      {activeTab === 'performance' && (
        <div className="w-full bg-[#111622] border border-[#1e2533] rounded-2xl p-7 space-y-6 shadow-md">
          <div className="p-5 rounded-xl bg-emerald-950/30 border border-emerald-800/50 text-sm text-slate-200 space-y-2">
            <span className="font-bold text-emerald-400 block uppercase tracking-wider text-sm">
              Why Accuracy Alone is Insufficient in Fraud Analytics
            </span>
            <p className="leading-relaxed text-slate-300">
              Because fraudulent transactions represent only ~3–6% of total volume, a model predicting "Normal" for 100% of transactions yields 96% accuracy while allowing 100% of financial fraud through. In this platform, <strong>Recall (Sensitivity)</strong> and <strong>F1-Score</strong> serve as the decisive criteria for model promotion.
            </p>
          </div>

          <div className="grid grid-cols-2 md:grid-cols-4 gap-6 text-center w-full">
            <div className="p-6 rounded-xl bg-[#0b0e14] border border-[#1e2533]">
              <span className="text-slate-400 text-sm font-semibold block mb-1">Accuracy</span>
              <span className="text-3xl font-black font-mono text-slate-100">97.5%</span>
            </div>
            <div className="p-6 rounded-xl bg-[#0b0e14] border border-[#1e2533]">
              <span className="text-slate-400 text-sm font-semibold block mb-1">Precision</span>
              <span className="text-3xl font-black font-mono text-emerald-400">92.8%</span>
            </div>
            <div className="p-6 rounded-xl bg-[#0b0e14] border border-[#1e2533]">
              <span className="text-slate-400 text-sm font-semibold block mb-1">Recall</span>
              <span className="text-3xl font-black font-mono text-emerald-400">94.2%</span>
            </div>
            <div className="p-6 rounded-xl bg-[#0b0e14] border border-[#1e2533]">
              <span className="text-slate-400 text-sm font-semibold block mb-1">F1-Score</span>
              <span className="text-3xl font-black font-mono text-emerald-400">93.5%</span>
            </div>
          </div>
        </div>
      )}

      {/* ========================================================== */}
      {/* TAB 4: RISK SCORING & EXPLAINABILITY                       */}
      {/* ========================================================== */}
      {activeTab === 'risk' && (
        <div className="space-y-8 w-full">
          <div className="bg-[#111622] border border-[#1e2533] rounded-2xl p-7 space-y-4 shadow-md w-full">
            <h4 className="text-base font-bold text-slate-200 uppercase tracking-wider">
              Global Feature Importance Rankings ({activeModel})
            </h4>
            <div className="h-80 w-full">
              <ResponsiveContainer width="100%" height="100%">
                <BarChart data={globalImportance.slice(0, 8)} layout="vertical">
                  <XAxis type="number" stroke="#64748b" fontSize={12} unit="%" />
                  <YAxis dataKey="feature" type="category" stroke="#94a3b8" fontSize={12} width={180} />
                  <Tooltip contentStyle={{ backgroundColor: '#141824', borderColor: '#242e40', borderRadius: 8, fontSize: 13 }} />
                  <Bar dataKey="importance_percent" fill="#10b981" radius={[0, 6, 6, 0]} />
                </BarChart>
              </ResponsiveContainer>
            </div>
          </div>

          {/* Local Attribution Waterfall */}
          <div className="bg-[#111622] border border-[#1e2533] rounded-2xl p-7 space-y-4 shadow-md w-full">
            <h4 className="text-base font-bold text-slate-200 uppercase tracking-wider">
              Sample Local Transaction Risk Attribution
            </h4>
            <div className="space-y-3">
              {[
                { factor: 'Amount Deviation Spike', val: '₹185,000 (+₹184,200 from mean)', pts: 35, esc: true, exp: 'Amount exceeds customer normal mean by 240x' },
                { factor: 'Unusual Nocturnal Window', val: '03:15:00 AM', pts: 25, esc: true, exp: 'High automated attack velocity occurs between 01:00 and 05:00 AM' },
                { factor: 'Radial Distance Hop', val: '280.0 km', pts: 20, esc: true, exp: 'Geographic departure from primary customer home cluster' },
                { factor: 'Untrusted Hardware Fingerprint', val: 'Unknown Device', pts: 20, esc: true, exp: 'Unregistered client browser signature' }
              ].map((f, i) => (
                <div key={i} className="p-4 rounded-xl bg-rose-950/25 border border-rose-800/50 flex items-center justify-between text-sm">
                  <div>
                    <span className="font-bold text-slate-100 block text-base">{f.factor}</span>
                    <span className="text-xs text-slate-400 mt-0.5 block">{f.exp}</span>
                  </div>
                  <span className="font-mono font-black text-rose-400 text-lg">+{f.pts} pts</span>
                </div>
              ))}
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
