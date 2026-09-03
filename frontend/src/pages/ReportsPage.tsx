import React, { useState, useEffect } from 'react';
import {
  FileText,
  Download,
  Eye,
  Play,
  CheckCircle2,
  FileSpreadsheet,
  FileCode,
  RefreshCw
} from 'lucide-react';
import { useAppState } from '../context/AppStateContext';
import { useAuth } from '../context/AuthContext';
import { api } from '../services/api';
import { Button } from '../components/common/Button';

export const ReportsPage: React.FC = () => {
  const { showToast } = useAppState();
  const { user } = useAuth();

  const reportTypes = [
    { title: 'Executive Summary', desc: 'High-level synthesis of total transaction volume, intercepted fraud rate, and loss prevention exposure.' },
    { title: 'Fraud Analysis Report', desc: 'Deep dive into attack vectors, nocturnal transaction surges, and geographic anomalies.' },
    { title: 'Suspicious Transaction Report', desc: 'Detailed dossier of all triaged transactions, auditor clearance notes, and pending holds.' },
    { title: 'Model Performance Report', desc: 'Precision, Recall, F1-Score benchmarking curves, and Confusion Matrices for governance.' }
  ];

  const [selectedType, setSelectedType] = useState('Executive Summary');
  const [format, setFormat] = useState('html');
  const [isGenerating, setIsGenerating] = useState(false);
  const [activeReport, setActiveReport] = useState<any>(null);
  const [reportList, setReportList] = useState<any[]>([]);

  const loadReports = async () => {
    try {
      const list = await api.listReports();
      setReportList(list);
    } catch (e) {
      console.warn('Reports load error:', e);
    }
  };

  useEffect(() => {
    loadReports();
  }, []);

  const handleGenerate = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsGenerating(true);
    try {
      const res = await api.generateReport(selectedType, format);
      setActiveReport(res);
      showToast(`Generated: ${res.report_id} (${res.format.toUpperCase()})`, 'success');
      loadReports();
    } catch (err: any) {
      showToast(err.message || 'Report generation failed', 'error');
    } finally {
      setIsGenerating(false);
    }
  };

  const handleExportCSV = async () => {
    try {
      const res = await api.exportSuspicious();
      showToast(`Exported: ${res.filename}`, 'success');
      window.open(`http://localhost:8000/api/exports/download/${res.filename}`, '_blank');
    } catch (err: any) {
      showToast(err.message || 'CSV export failed', 'error');
    }
  };

  return (
    <div className="w-full space-y-8 pb-16 font-sans">
      {/* Top Banner - Full Screen */}
      <div className="w-full bg-[#111622] border border-[#1e2533] rounded-2xl p-6 flex flex-col sm:flex-row sm:items-center justify-between gap-6 shadow-md">
        <div>
          <h3 className="text-xl font-bold text-slate-100 flex items-center space-x-3">
            <FileText className="w-7 h-7 text-emerald-400" />
            <span>Compliance &amp; Risk Reporting Center</span>
          </h3>
          <p className="text-sm text-slate-300 mt-1 font-medium">
            Compile formatted audit dossiers, model governance packages, and executive loss mitigation assessments in HTML and PDF formats.
          </p>
        </div>

        <Button variant="secondary" size="md" icon={FileSpreadsheet} onClick={handleExportCSV}>
          Export Suspicious CSV
        </Button>
      </div>

      {/* Report Generator Controls */}
      <div className="bg-[#111622] border border-[#1e2533] rounded-2xl p-7 shadow-md w-full">
        <form onSubmit={handleGenerate} className="space-y-6 text-sm">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <label className="block text-slate-200 font-bold mb-2 uppercase tracking-wider text-xs">
                Select Report Scope
              </label>
              <select
                value={selectedType}
                onChange={(e) => setSelectedType(e.target.value)}
                className="w-full bg-[#0b0e14] border border-[#232a3b] rounded-xl px-4 py-3 text-slate-100 font-medium text-sm focus:border-emerald-500 focus:outline-none"
              >
                {reportTypes.map((r) => (
                  <option key={r.title} value={r.title}>
                    {r.title}
                  </option>
                ))}
              </select>
              <span className="text-xs text-slate-400 mt-2 block font-medium">
                {reportTypes.find((r) => r.title === selectedType)?.desc}
              </span>
            </div>

            <div>
              <label className="block text-slate-200 font-bold mb-2 uppercase tracking-wider text-xs">
                Render Format
              </label>
              <div className="grid grid-cols-2 gap-3">
                <button
                  type="button"
                  onClick={() => setFormat('html')}
                  className={`p-3 rounded-xl border text-sm font-bold flex items-center justify-center space-x-2 transition-all ${
                    format === 'html'
                      ? 'bg-emerald-950/80 border-emerald-500 text-emerald-300 shadow-sm'
                      : 'bg-[#0b0e14] border-[#232a3b] text-slate-400 hover:text-slate-200'
                  }`}
                >
                  <FileCode className="w-5 h-5 text-emerald-400" />
                  <span>Interactive HTML</span>
                </button>
                <button
                  type="button"
                  onClick={() => setFormat('pdf')}
                  className={`p-3 rounded-xl border text-sm font-bold flex items-center justify-center space-x-2 transition-all ${
                    format === 'pdf'
                      ? 'bg-emerald-950/80 border-emerald-500 text-emerald-300 shadow-sm'
                      : 'bg-[#0b0e14] border-[#232a3b] text-slate-400 hover:text-slate-200'
                  }`}
                >
                  <FileText className="w-5 h-5 text-emerald-400" />
                  <span>ReportLab PDF</span>
                </button>
              </div>
            </div>
          </div>

          <div className="flex justify-end pt-2">
            <Button
              type="submit"
              variant="primary"
              size="md"
              icon={Play}
              isLoading={isGenerating}
              className="py-3 px-6 text-sm font-bold shadow-lg"
            >
              Compile &amp; Generate Report
            </Button>
          </div>
        </form>
      </div>

      {/* Live Generated Report Viewer */}
      {activeReport && (
        <div className="bg-[#111622] border border-[#1e2533] rounded-2xl overflow-hidden shadow-lg w-full">
          <div className="p-5 bg-[#141a26] border-b border-[#1e2533] flex items-center justify-between">
            <div className="flex items-center space-x-3">
              <CheckCircle2 className="w-6 h-6 text-emerald-400" />
              <div>
                <h4 className="text-base font-bold text-slate-100 font-mono">
                  {activeReport.report_id}
                </h4>
                <span className="text-xs text-slate-400 font-sans">
                  Compiled at {activeReport.generated_at} &bull; Type: {activeReport.report_type}
                </span>
              </div>
            </div>

            <Button
              variant="primary"
              size="sm"
              icon={Download}
              onClick={() => window.open(`http://localhost:8000/api/reports/download/${activeReport.filename}`, '_blank')}
            >
              Download {activeReport.format.toUpperCase()}
            </Button>
          </div>

          <div className="p-4 bg-[#090c12]">
            <iframe
              src={`http://localhost:8000/api/reports/download/${activeReport.filename}`}
              title="Report Preview"
              className="w-full h-[550px] rounded-xl border border-[#202838] bg-white"
            />
          </div>
        </div>
      )}

      {/* Historical Generated Reports Table */}
      <div className="bg-[#111622] border border-[#1e2533] rounded-2xl overflow-hidden shadow-md w-full">
        <div className="p-5 bg-[#141a26] border-b border-[#1e2533] flex items-center justify-between">
          <h4 className="text-base font-bold text-slate-100">
            Historical Compliance Archives
          </h4>
          <Button variant="ghost" size="sm" icon={RefreshCw} onClick={loadReports}>
            Refresh
          </Button>
        </div>

        <div className="overflow-x-auto w-full">
          <table className="w-full text-sm text-left">
            <thead className="bg-[#0f131c] text-slate-300 font-bold border-b border-[#1e2533]">
              <tr>
                <th className="px-5 py-3.5">Filename</th>
                <th className="px-5 py-3.5">Report Type</th>
                <th className="px-5 py-3.5">Format</th>
                <th className="px-5 py-3.5">Generated Timestamp</th>
                <th className="px-5 py-3.5 text-right">Action</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-[#181f2e] font-mono text-slate-200">
              {reportList.map((r) => (
                <tr key={r.filename} className="hover:bg-[#141c29] transition-colors">
                  <td className="px-5 py-3.5 text-slate-100 font-bold">{r.filename}</td>
                  <td className="px-5 py-3.5 text-slate-300 font-sans">{r.report_type || 'Executive Summary'}</td>
                  <td className="px-5 py-3.5">
                    <span className="px-2.5 py-0.5 rounded-lg text-xs font-black bg-emerald-950 text-emerald-300 border border-emerald-700/60 uppercase">
                      {r.format}
                    </span>
                  </td>
                  <td className="px-5 py-3.5 text-xs text-slate-400">{r.created_at}</td>
                  <td className="px-5 py-3.5 text-right font-sans">
                    <a
                      href={`http://localhost:8000/api/reports/download/${r.filename}`}
                      target="_blank"
                      rel="noreferrer"
                      className="text-xs text-emerald-400 hover:text-emerald-300 font-bold inline-flex items-center space-x-1"
                    >
                      <Download className="w-4 h-4 mr-1" />
                      <span>Download</span>
                    </a>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};
