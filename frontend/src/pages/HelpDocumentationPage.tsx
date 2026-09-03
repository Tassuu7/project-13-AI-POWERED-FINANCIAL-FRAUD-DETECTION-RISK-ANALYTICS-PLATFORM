import React from 'react';
import { BookOpen, ShieldCheck, Cpu, AlertTriangle, FileSpreadsheet, Lock } from 'lucide-react';

export const HelpDocumentationPage: React.FC = () => {
  const sections = [
    {
      title: '1. What is Financial Fraud Detection?',
      icon: ShieldCheck,
      content:
        'Financial transaction fraud detection acts like a real-time digital risk analyst. Rather than looking solely at the static price tag of a purchase, it monitors behavioural anomalies across multidimensional axes: geographic proximity, hour of day, device fingerprint authenticity, customer historical velocity, and transaction amount relative to average baseline spending.'
    },
    {
      title: '2. The End-to-End Machine Learning Pipeline',
      icon: Cpu,
      content:
        'The platform implements a complete 10-step lifecycle: Dataset Ingestion -> Schema Validation -> Preprocessing (missing values & scaling) -> Feature Engineering -> Exploratory Data Analysis -> Multi-Model Benchmark Training -> Precision/Recall Evaluation -> Single & Batch Inference -> Multi-Factor Risk Calibration -> Auditor Triage.'
    },
    {
      title: '3. Why Accuracy is Not Enough in Fraud Analytics',
      icon: AlertTriangle,
      content:
        'Because fraud comprises only 2–6% of actual transactions, a naive baseline predicting 100% legitimate transactions will score 96% accuracy while permitting millions in financial loss. In this platform, Recall (the % of actual fraud captured) and Precision (the % of flagged transactions that are genuine anomalies) serve as the primary metrics for deploying production classifiers.'
    },
    {
      title: '4. Synthetic Data Generation & Absolute Privacy',
      icon: Lock,
      content:
        'To strictly respect banking privacy regulations and project constraints, no real customer bank accounts, PAN numbers, or real card numbers are ever stored or processed. All datasets are generated using deterministic statistical distributions (Log-Normal amounts, Poisson transaction frequencies, and Haversine geographic displacement formulas).'
    }
  ];

  const dataDictionary = [
    { col: 'transaction_id', type: 'String', desc: 'Unique identifier for the financial transaction event.' },
    { col: 'customer_id', type: 'String', desc: 'Anonymized customer account identifier.' },
    { col: 'amount', type: 'Float (INR)', desc: 'Gross transaction exposure in Indian Rupees.' },
    { col: 'timestamp', type: 'Datetime', desc: 'Timestamp of transaction authorization (YYYY-MM-DD HH:MM:SS).' },
    { col: 'transaction_type', type: 'Categorical', desc: 'Channel: Online, POS / In-Store, UPI Transfer, ATM, Wire Transfer.' },
    { col: 'merchant_category', type: 'Categorical', desc: 'Retail segment: Grocery, Luxury Goods, Crypto, Tech, Dining.' },
    { col: 'location', type: 'Categorical', desc: 'Originating metropolitan cluster (e.g. Mumbai, Delhi, Bengaluru).' },
    { col: 'device_type', type: 'Categorical', desc: 'Hardware or client browser fingerprint.' },
    { col: 'distance_from_usual_location', type: 'Float (km)', desc: 'Radial displacement in kilometers from customer home cluster.' },
    { col: 'transaction_frequency', type: 'Integer', desc: 'Count of transactions initiated within monitoring window.' },
    { col: 'is_fraud', type: 'Binary (0/1)', desc: 'Ground truth classification label: 0 for Normal, 1 for Fraud.' }
  ];

  return (
    <div className="w-full space-y-8 pb-16 font-sans">
      {/* Header Banner - Full Screen */}
      <div className="w-full bg-[#111622] border border-[#1e2533] rounded-2xl p-6 flex items-center space-x-4 shadow-md">
        <div className="w-12 h-12 rounded-2xl bg-emerald-950/80 border border-emerald-500/40 flex items-center justify-center text-emerald-400 shrink-0 shadow-sm">
          <BookOpen className="w-7 h-7" />
        </div>
        <div>
          <h3 className="text-xl font-bold text-slate-100">Knowledge Base &amp; Data Dictionary</h3>
          <p className="text-sm text-slate-300 mt-1 font-medium">
            Operational reference guide covering fraud risk mechanics, ML evaluation principles, and data attributes.
          </p>
        </div>
      </div>

      {/* Educational Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 w-full">
        {sections.map((s, idx) => {
          const Icon = s.icon;
          return (
            <div key={idx} className="bg-[#111622] border border-[#1e2533] rounded-2xl p-6 space-y-3 shadow-md">
              <div className="flex items-center space-x-3">
                <Icon className="w-6 h-6 text-emerald-400" />
                <h4 className="text-base font-bold text-slate-100">{s.title}</h4>
              </div>
              <p className="text-sm text-slate-300 leading-relaxed font-medium">{s.content}</p>
            </div>
          );
        })}
      </div>

      {/* Canonical Schema Data Dictionary */}
      <div className="bg-[#111622] border border-[#1e2533] rounded-2xl overflow-hidden shadow-md w-full">
        <div className="p-5 bg-[#141a26] border-b border-[#1e2533]">
          <h4 className="text-base font-bold text-slate-100">
            Canonical Dataset Schema &amp; Feature Dictionary
          </h4>
          <span className="text-xs text-slate-400 mt-0.5 block">
            Standard 11-column data specification required for all ingested transaction ledgers
          </span>
        </div>

        <div className="overflow-x-auto w-full">
          <table className="w-full text-sm text-left">
            <thead className="bg-[#0f131c] text-slate-300 font-bold border-b border-[#1e2533]">
              <tr>
                <th className="px-5 py-3.5">Column Name</th>
                <th className="px-5 py-3.5">Data Type</th>
                <th className="px-5 py-3.5">Regulatory Description &amp; Analytical Purpose</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-[#181f2e] font-mono text-slate-200">
              {dataDictionary.map((item) => (
                <tr key={item.col} className="hover:bg-[#141c29] transition-colors">
                  <td className="px-5 py-3.5 text-emerald-400 font-bold">{item.col}</td>
                  <td className="px-5 py-3.5 text-slate-300 text-xs">{item.type}</td>
                  <td className="px-5 py-3.5 font-sans text-xs text-slate-300">{item.desc}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};
