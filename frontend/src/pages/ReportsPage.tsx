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
      showToast(`Generated: ${res.filename}`, 'success');
      loadReports();
    } catch (err: any) {
      showToast(err.message || 'Report generation failed', 'error');
    } finally {
      setIsGenerating(false);
    }
  };

  const handleDownload = (filename: string) => {
    window.open(`http://localhost:8000/api/reports/${filename}/download`, '_blank');
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
    <div className="space-y-6 max-w-6xl mx-auto pb-12 font-sans">
      {/* Top Banner */}
      <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-5 flex flex-col sm:flex-row sm:items-center justify-between gap-4 shadow-sm">
        <div>
          <h3 className="text-base font-bold text-slate-100 flex items-center space-x-2">
            <FileText className="w-5 h-5 text-emerald-400" />
            <span>Compliance &amp; Risk Reporting Center</span>
          </h3>
          <p className="text-xs text-slate-400 mt-0.5">
            Compile formatted audit dossiers, model governance packages, and executive loss mitigation assessments in HTML and PDF formats.
          </p>
        </div>

        <Button variant="secondary" size="sm" icon={FileSpreadsheet} onClick={handleExportCSV}>
          Export Suspicious CSV
        </Button>
      </div>

      {/* Report Generator Controls */}
      <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-6 shadow-sm">
        <form onSubmit={handleGenerate} className="space-y-4 text-xs">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <label className="block text-slate-300 font-semibold mb-1 uppercase tracking-wider">
                Select Report Scope
              </label>
              <select
                value={selectedType}
                onChange={(e) => setSelectedType(e.target.value)}
                className="w-full bg-[#0b0e14] border border-[#232a3b] rounded-lg px-3 py-2 text-slate-100 focus:border-emerald-500 focus:outline-none"
              >
                {reportTypes.map((r) => (
                  <option key={r.title} value={r.title}>
                    {r.title}
                  </option>
                ))}
              </select>
            </div>

            <div>
              <label className="block text-slate-300 font-semibold mb-1 uppercase tracking-wider">
                Output Format
              </label>
              <select
                value={format}
                onChange={(e) => setFormat(e.target.value)}
                className="w-full bg-[#0b0e14] border border-[#232a3b] rounded-lg px-3 py-2 text-slate-100 focus:border-emerald-500 focus:outline-none"
              >
                <option value="html">Interactive HTML Document (In-App Preview)</option>
                <option value="pdf">Print-Ready PDF Document (ReportLab Engine)</option>
              </select>
            </div>
          </div>

          <div className="flex justify-end pt-2">
            <Button type="submit" variant="primary" icon={Play} isLoading={isGenerating}>
              Generate Report
            </Button>
          </div>
        </form>
      </div>

      {/* Live In-App Preview Container matching Section 25 */}
      {activeReport && (
        <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-5 space-y-4 shadow-sm">
          <div className="flex items-center justify-between pb-3 border-b border-[#1e2432]">
            <div>
              <span className="text-emerald-400 font-bold text-xs uppercase tracking-wider flex items-center space-x-1.5">
                <CheckCircle2 className="w-4 h-4" />
                <span>Generated Successfully</span>
              </span>
              <h4 className="text-sm font-bold text-slate-100 font-mono mt-0.5">
                {activeReport.filename}
              </h4>
            </div>

            <Button
              variant="primary"
              size="sm"
              icon={Download}
              onClick={() => handleDownload(activeReport.filename)}
            >
              Download {activeReport.format.toUpperCase()}
            </Button>
          </div>

          {activeReport.preview_html && (
            <div className="border border-[#1e2432] rounded-lg overflow-hidden bg-[#0a0d13] p-1">
              <iframe
                title="Report Preview"
                srcDoc={activeReport.preview_html}
                className="w-full h-96 rounded bg-transparent"
              />
            </div>
          )}
        </div>
      )}

      {/* Report Archive List */}
      <div className="bg-[#11141c] border border-[#1e2432] rounded-xl overflow-hidden shadow-sm">
        <div className="p-4 bg-[#141822] border-b border-[#1e2432] flex items-center justify-between">
          <span className="text-xs font-bold text-slate-300 uppercase tracking-wider">
            Generated Reports Archive
          </span>
          <Button variant="ghost" size="sm" icon={RefreshCw} onClick={loadReports}>
            Refresh
          </Button>
        </div>

        <div className="divide-y divide-[#181d28] font-mono text-xs">
          {reportList.map((rep) => (
            <div key={rep.filename} className="p-4 flex items-center justify-between hover:bg-[#141822]">
              <div>
                <span className="font-bold text-slate-200 block truncate">{rep.filename}</span>
                <span className="text-[11px] text-slate-500 font-sans">
                  Size: {(rep.size_bytes / 1024).toFixed(1)} KB &bull; Type: {rep.format}
                </span>
              </div>
              <Button size="sm" variant="secondary" icon={Download} onClick={() => handleDownload(rep.filename)}>
                Download
              </Button>
            </div>
          ))}

          {reportList.length === 0 && (
            <div className="p-8 text-center text-slate-500 font-sans">
              No reports compiled yet. Click 'Generate Report' above.
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
