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
    <div className="space-y-6 max-w-5xl mx-auto pb-12">
      {/* Header Banner */}
      <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-6 flex items-center space-x-3">
        <div className="w-10 h-10 rounded-lg bg-emerald-950/80 border border-emerald-500/30 flex items-center justify-center text-emerald-400 shrink-0">
          <BookOpen className="w-5 h-5" />
        </div>
        <div>
          <h3 className="text-base font-bold text-slate-100">Knowledge Base &amp; Data Dictionary</h3>
          <p className="text-xs text-slate-400 mt-0.5">
            Operational reference guide covering fraud risk mechanics, ML evaluation principles, and data attributes.
          </p>
        </div>
      </div>

      {/* Explanatory Sections */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {sections.map((sec, i) => {
          const Icon = sec.icon;
          return (
            <div key={i} className="bg-[#11141c] border border-[#1e2432] rounded-xl p-5 shadow-sm space-y-2">
              <div className="flex items-center space-x-2 text-emerald-400 font-bold text-xs">
                <Icon className="w-4 h-4" />
                <span>{sec.title}</span>
              </div>
              <p className="text-xs text-slate-400 leading-relaxed pt-1">
                {sec.content}
              </p>
            </div>
          );
        })}
      </div>

      {/* Data Dictionary Table */}
      <div className="bg-[#11141c] border border-[#1e2432] rounded-xl overflow-hidden shadow-sm">
        <div className="px-5 py-3.5 bg-[#141822] border-b border-[#1e2432] flex items-center space-x-2">
          <FileSpreadsheet className="w-4 h-4 text-emerald-400" />
          <span className="text-xs font-bold text-slate-300 uppercase tracking-wider">
            Canonical Dataset Schema &amp; Data Dictionary
          </span>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full text-xs text-left">
            <thead className="bg-[#161a24] text-slate-300 font-semibold border-b border-[#1e2432]">
              <tr>
                <th className="px-4 py-3">Column Attribute</th>
                <th className="px-4 py-3">Data Type</th>
                <th className="px-4 py-3">Operational Meaning &amp; Fraud Significance</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-[#181d28] text-slate-300">
              {dataDictionary.map((d) => (
                <tr key={d.col} className="hover:bg-[#141822] transition-colors">
                  <td className="px-4 py-3 font-mono font-bold text-emerald-400">{d.col}</td>
                  <td className="px-4 py-3 font-mono text-slate-400">{d.type}</td>
                  <td className="px-4 py-3 text-slate-300">{d.desc}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};
