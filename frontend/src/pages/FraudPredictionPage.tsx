import React, { useState } from 'react';
import { Search, ShieldAlert, ShieldCheck, AlertTriangle, ArrowRight, Zap, Play, FileSpreadsheet } from 'lucide-react';
import { useAppState } from '../context/AppStateContext';
import { api } from '../services/api';
import { PredictionResult } from '../types';
import { Button } from '../components/common/Button';

export const FraudPredictionPage: React.FC<{ onNavigateNext?: () => void }> = ({ onNavigateNext }) => {
  const { selectedDataset, activeModel, showToast } = useAppState();

  const [activeTab, setActiveTab] = useState<'single' | 'batch'>('single');

  // Single form state
  const [amount, setAmount] = useState<number>(185000);
  const [txType, setTxType] = useState('Online');
  const [merchantCat, setMerchantCat] = useState('Crypto & Digital Assets');
  const [location, setLocation] = useState('Mumbai');
  const [deviceType, setDeviceType] = useState('Unknown Device');
  const [timestamp, setTimestamp] = useState('2025-03-01 03:15:00');
  const [accountAge, setAccountAge] = useState(25);
  const [frequency, setFrequency] = useState(7);
  const [prevAmount, setPrevAmount] = useState(1200);
  const [distance, setDistance] = useState(280);

  const [isPredicting, setIsPredicting] = useState(false);
  const [singleResult, setSingleResult] = useState<PredictionResult | null>(null);

  // Batch state
  const [batchResult, setBatchResult] = useState<any>(null);
  const [isBatchRunning, setIsBatchRunning] = useState(false);

  // Presets
  const loadSuspiciousPreset = () => {
    setAmount(185000);
    setTxType('Online');
    setMerchantCat('Crypto & Digital Assets');
    setLocation('Mumbai');
    setDeviceType('Unknown Device');
    setTimestamp('2025-03-01 03:15:00');
    setAccountAge(25);
    setFrequency(8);
    setPrevAmount(1200);
    setDistance(320);
    setSingleResult(null);
  };

  const loadNormalPreset = () => {
    setAmount(750);
    setTxType('POS / In-Store');
    setMerchantCat('Grocery & Supermarkets');
    setLocation('Hyderabad');
    setDeviceType('Trusted Mobile App (iOS)');
    setTimestamp('2025-03-01 14:30:00');
    setAccountAge(420);
    setFrequency(1);
    setPrevAmount(800);
    setDistance(4.2);
    setSingleResult(null);
  };

  const handleSinglePredict = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsPredicting(true);
    try {
      const payload = {
        amount: Number(amount),
        transaction_type: txType,
        merchant_category: merchantCat,
        location,
        device_type: deviceType,
        timestamp,
        account_age_days: Number(accountAge),
        transaction_frequency: Number(frequency),
        previous_transaction_amount: Number(prevAmount),
        distance_from_usual_location: Number(distance),
        customer_id: 'CUST-8821'
      };
      const res = await api.predictSingle(payload, activeModel);
      setSingleResult(res);
      showToast(`Evaluated: Risk Score ${res.risk_score}/100 (${res.risk_level})`, res.risk_level === 'HIGH' ? 'error' : 'success');
    } catch (err: any) {
      showToast(err.message || 'Prediction failed', 'error');
    } finally {
      setIsPredicting(false);
    }
  };

  const handleBatchPredict = async () => {
    if (!selectedDataset) return;
    setIsBatchRunning(true);
    try {
      const res = await api.predictBatch(selectedDataset, activeModel);
      setBatchResult(res);
      showToast(`Batch completed: ${res.high_risk_count} high-risk items routed to Investigation Desk!`, 'success');
    } catch (err: any) {
      showToast(err.message || 'Batch prediction failed', 'error');
    } finally {
      setIsBatchRunning(false);
    }
  };

  return (
    <div className="space-y-6 max-w-5xl mx-auto pb-12">
      {/* Tab Selector */}
      <div className="flex space-x-2 border-b border-[#1e2432] pb-2">
        <button
          onClick={() => setActiveTab('single')}
          className={`px-4 py-2 text-xs font-bold rounded-lg transition-colors ${
            activeTab === 'single'
              ? 'bg-emerald-950/60 text-emerald-400 border border-emerald-500/40'
              : 'text-slate-400 hover:text-slate-200'
          }`}
        >
          Single Transaction Inspector
        </button>
        <button
          onClick={() => setActiveTab('batch')}
          className={`px-4 py-2 text-xs font-bold rounded-lg transition-colors ${
            activeTab === 'batch'
              ? 'bg-emerald-950/60 text-emerald-400 border border-emerald-500/40'
              : 'text-slate-400 hover:text-slate-200'
          }`}
        >
          Batch Dataset Scoring
        </button>
      </div>

      {activeTab === 'single' && (
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
          {/* Left Form */}
          <div className="lg:col-span-7 bg-[#11141c] border border-[#1e2432] rounded-xl p-5 shadow-sm space-y-4">
            <div className="flex items-center justify-between pb-3 border-b border-[#1e2432]">
              <div>
                <h3 className="text-sm font-bold text-slate-100 uppercase tracking-wider">
                  Transaction Parameters
                </h3>
                <span className="text-xs text-slate-400">Model: {activeModel}</span>
              </div>
              <div className="flex items-center space-x-2">
                <Button type="button" variant="secondary" size="sm" onClick={loadSuspiciousPreset}>
                  Suspicious Preset
                </Button>
                <Button type="button" variant="secondary" size="sm" onClick={loadNormalPreset}>
                  Normal Preset
                </Button>
              </div>
            </div>

            <form onSubmit={handleSinglePredict} className="space-y-4 text-xs">
              <div className="grid grid-cols-2 gap-3">
                <div>
                  <label className="block font-semibold text-slate-300 mb-1">Amount (INR)</label>
                  <input
                    type="number"
                    value={amount}
                    onChange={(e) => setAmount(Number(e.target.value))}
                    required
                    className="w-full bg-[#0b0e14] border border-[#232a3b] rounded-lg px-3 py-2 text-slate-100 font-mono font-bold text-sm focus:border-emerald-500 focus:outline-none"
                  />
                </div>
                <div>
                  <label className="block font-semibold text-slate-300 mb-1">Previous Baseline (INR)</label>
                  <input
                    type="number"
                    value={prevAmount}
                    onChange={(e) => setPrevAmount(Number(e.target.value))}
                    required
                    className="w-full bg-[#0b0e14] border border-[#232a3b] rounded-lg px-3 py-2 text-slate-100 font-mono focus:border-emerald-500 focus:outline-none"
                  />
                </div>
              </div>

              <div className="grid grid-cols-2 gap-3">
                <div>
                  <label className="block font-semibold text-slate-300 mb-1">Channel / Type</label>
                  <select
                    value={txType}
                    onChange={(e) => setTxType(e.target.value)}
                    className="w-full bg-[#0b0e14] border border-[#232a3b] rounded-lg px-3 py-2 text-slate-100 focus:border-emerald-500 focus:outline-none"
                  >
                    <option value="Online">Online Payment</option>
                    <option value="POS / In-Store">POS / In-Store</option>
                    <option value="UPI Transfer">UPI Transfer</option>
                    <option value="ATM Withdrawal">ATM Withdrawal</option>
                    <option value="Wire Transfer">Wire Transfer</option>
                  </select>
                </div>
                <div>
                  <label className="block font-semibold text-slate-300 mb-1">Merchant Category</label>
                  <select
                    value={merchantCat}
                    onChange={(e) => setMerchantCat(e.target.value)}
                    className="w-full bg-[#0b0e14] border border-[#232a3b] rounded-lg px-3 py-2 text-slate-100 focus:border-emerald-500 focus:outline-none"
                  >
                    <option value="Crypto & Digital Assets">Crypto &amp; Digital Assets</option>
                    <option value="Luxury Goods & Jewelry">Luxury Goods &amp; Jewelry</option>
                    <option value="Electronics & Gadgets">Electronics &amp; Gadgets</option>
                    <option value="Grocery & Supermarkets">Grocery &amp; Supermarkets</option>
                    <option value="Dining & Food">Dining &amp; Food</option>
                  </select>
                </div>
              </div>

              <div className="grid grid-cols-2 gap-3">
                <div>
                  <label className="block font-semibold text-slate-300 mb-1">Device Fingerprint</label>
                  <select
                    value={deviceType}
                    onChange={(e) => setDeviceType(e.target.value)}
                    className="w-full bg-[#0b0e14] border border-[#232a3b] rounded-lg px-3 py-2 text-slate-100 focus:border-emerald-500 focus:outline-none"
                  >
                    <option value="Unknown Device">Unknown / Unregistered Device</option>
                    <option value="New Emulated Device">New Emulated Device</option>
                    <option value="Mobile Web Browser">Mobile Web Browser</option>
                    <option value="Trusted Mobile App (iOS)">Trusted Mobile App (iOS)</option>
                    <option value="Trusted Mobile App (Android)">Trusted Mobile App (Android)</option>
                    <option value="Desktop Web Browser">Desktop Web Browser</option>
                  </select>
                </div>
                <div>
                  <label className="block font-semibold text-slate-300 mb-1">Origination Location</label>
                  <input
                    type="text"
                    value={location}
                    onChange={(e) => setLocation(e.target.value)}
                    className="w-full bg-[#0b0e14] border border-[#232a3b] rounded-lg px-3 py-2 text-slate-100 focus:border-emerald-500 focus:outline-none"
                  />
                </div>
              </div>

              <div className="grid grid-cols-3 gap-3">
                <div>
                  <label className="block font-semibold text-slate-300 mb-1">Time of Day</label>
                  <input
                    type="text"
                    value={timestamp}
                    onChange={(e) => setTimestamp(e.target.value)}
                    className="w-full bg-[#0b0e14] border border-[#232a3b] rounded-lg px-3 py-2 text-slate-100 font-mono focus:border-emerald-500 focus:outline-none"
                  />
                </div>
                <div>
                  <label className="block font-semibold text-slate-300 mb-1">Frequency (Tx/hr)</label>
                  <input
                    type="number"
                    value={frequency}
                    onChange={(e) => setFrequency(Number(e.target.value))}
                    className="w-full bg-[#0b0e14] border border-[#232a3b] rounded-lg px-3 py-2 text-slate-100 font-mono focus:border-emerald-500 focus:outline-none"
                  />
                </div>
                <div>
                  <label className="block font-semibold text-slate-300 mb-1">Displacement (km)</label>
                  <input
                    type="number"
                    value={distance}
                    onChange={(e) => setDistance(Number(e.target.value))}
                    className="w-full bg-[#0b0e14] border border-[#232a3b] rounded-lg px-3 py-2 text-slate-100 font-mono focus:border-emerald-500 focus:outline-none"
                  />
                </div>
              </div>

              <div className="pt-2 flex justify-end">
                <Button type="submit" variant="primary" icon={Zap} isLoading={isPredicting}>
                  Run Real-Time Inference
                </Button>
              </div>
            </form>
          </div>

          {/* Right Result Card */}
          <div className="lg:col-span-5 flex flex-col justify-start">
            {singleResult ? (
              <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-5 space-y-5 shadow-lg">
                <div className="pb-3 border-b border-[#1e2432] flex items-center justify-between">
                  <span className="text-xs font-bold text-slate-400 uppercase tracking-wider">
                    Inference Verdict
                  </span>
                  <span className="text-[11px] font-mono text-slate-400">
                    Engine: {singleResult.model_used}
                  </span>
                </div>

                {/* Big Score Pill */}
                <div className={`p-4 rounded-xl border text-center ${
                  singleResult.risk_level === 'HIGH'
                    ? 'bg-rose-950/40 border-rose-600/60 text-rose-300'
                    : singleResult.risk_level === 'MEDIUM'
                    ? 'bg-amber-950/40 border-amber-600/60 text-amber-300'
                    : 'bg-emerald-950/40 border-emerald-600/60 text-emerald-300'
                }`}>
                  <div className="text-3xl font-black font-mono tracking-tight">
                    {singleResult.risk_score} <span className="text-sm font-normal text-slate-400">/ 100</span>
                  </div>
                  <div className="text-base font-bold uppercase tracking-wider mt-1">
                    {singleResult.prediction_label} ({singleResult.risk_level} RISK)
                  </div>
                  <div className="text-xs text-slate-400 mt-1">
                    Model Confidence: {(singleResult.confidence_probability * 100).toFixed(1)}%
                  </div>
                </div>

                {/* Recommended Action */}
                <div className="bg-[#0b0e14] border border-[#1e2432] p-3 rounded-lg text-xs">
                  <span className="text-slate-400 font-semibold block mb-0.5">Policy Recommendation:</span>
                  <span className="text-slate-200 font-bold">{singleResult.recommended_action}</span>
                </div>

                {/* Contributing Risk Factors */}
                <div className="space-y-2">
                  <span className="text-xs font-bold text-slate-300 uppercase tracking-wider block">
                    Contributing Risk Factors
                  </span>
                  <div className="space-y-1.5 text-xs">
                    {singleResult.contributing_factors.map((f, i) => (
                      <div key={i} className="p-2.5 bg-[#0b0e14] rounded border border-[#1a202c] flex items-start space-x-2">
                        <span className={`px-1.5 py-0.5 rounded text-[10px] font-bold shrink-0 ${
                          f.impact === 'HIGH' ? 'bg-rose-950 text-rose-400 border border-rose-800/40' :
                          f.impact === 'MEDIUM' ? 'bg-amber-950 text-amber-400 border border-amber-800/40' :
                          'bg-slate-800 text-slate-300'
                        }`}>
                          {f.impact}
                        </span>
                        <div className="min-w-0">
                          <span className="font-semibold text-slate-200 block">{f.factor}</span>
                          <span className="text-[11px] text-slate-400">{f.description}</span>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>

                {singleResult.risk_level === 'HIGH' && (
                  <div className="pt-2">
                    <span className="text-[11px] text-rose-400 font-semibold block text-center">
                      Auto-routed to Suspicious Transactions Investigation Desk
                    </span>
                  </div>
                )}
              </div>
            ) : (
              <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-8 text-center flex flex-col items-center justify-center h-full min-h-[350px]">
                <Search className="w-10 h-10 text-slate-600 mb-3" />
                <h4 className="text-sm font-bold text-slate-300">Awaiting Real-Time Transaction</h4>
                <p className="text-xs text-slate-500 max-w-xs mt-1">
                  Adjust transaction attributes or select a preset to evaluate risk probability and contributing factors.
                </p>
              </div>
            )}
          </div>
        </div>
      )}

      {activeTab === 'batch' && (
        <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-6 space-y-6">
          <div className="flex items-center space-x-3 pb-4 border-b border-[#1e2432]">
            <FileSpreadsheet className="w-6 h-6 text-emerald-400" />
            <div>
              <h3 className="text-base font-bold text-slate-100">Batch Fraud Prediction Pipeline</h3>
              <p className="text-xs text-slate-400">
                Score entire dataset <span className="font-mono text-emerald-400 font-bold">{selectedDataset}</span> with active model ({activeModel}).
              </p>
            </div>
          </div>

          <div className="flex justify-start">
            <Button variant="primary" icon={Play} onClick={handleBatchPredict} isLoading={isBatchRunning}>
              Execute Batch Inference on {selectedDataset}
            </Button>
          </div>

          {batchResult && (
            <div className="space-y-4 pt-4 border-t border-[#1e2432]">
              <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 text-xs font-mono">
                <div className="bg-[#0b0e14] p-4 rounded-lg border border-[#1e2432]">
                  <span className="text-slate-400 font-sans block">Total Processed</span>
                  <div className="text-xl font-bold text-slate-100 mt-1">{batchResult.total_processed}</div>
                </div>
                <div className="bg-[#0b0e14] p-4 rounded-lg border border-[#1e2432]">
                  <span className="text-slate-400 font-sans block">Low Risk (Approved)</span>
                  <div className="text-xl font-bold text-emerald-400 mt-1">{batchResult.low_risk_count}</div>
                </div>
                <div className="bg-[#0b0e14] p-4 rounded-lg border border-[#1e2432]">
                  <span className="text-slate-400 font-sans block">Medium Risk (Step-Up)</span>
                  <div className="text-xl font-bold text-amber-400 mt-1">{batchResult.medium_risk_count}</div>
                </div>
                <div className="bg-[#0b0e14] p-4 rounded-lg border border-[#1e2432]">
                  <span className="text-slate-400 font-sans block">High Risk (Investigate)</span>
                  <div className="text-xl font-bold text-rose-500 mt-1">{batchResult.high_risk_count}</div>
                </div>
              </div>

              {onNavigateNext && (
                <div className="flex justify-end pt-2">
                  <Button variant="primary" size="sm" icon={ArrowRight} onClick={onNavigateNext}>
                    View Suspicious Transactions Queue
                  </Button>
                </div>
              )}
            </div>
          )}
        </div>
      )}
    </div>
  );
};
