import React, { useState, useEffect } from 'react';
import { FileText, Download, Eye, Play, CheckCircle2, RefreshCw } from 'lucide-react';
import { useAppState } from '../context/AppStateContext';
import { useAuth } from '../context/AuthContext';
import { api } from '../services/api';
import { Button } from '../components/common/Button';

export const ReportGenerationPage: React.FC = () => {
  const { showToast } = useAppState();
  const { user } = useAuth();

  const reportTypes = [
    { type: 'Executive Risk Summary', desc: 'High-level synthesis of overall transaction volume, fraud rate, and loss prevention exposure.' },
    { type: 'Fraud Risk Analysis Report', desc: 'Deep dive into fraudulent vectors, channel incident rates, and time-of-day risks.' },
    { type: 'ML Model Evaluation Report', desc: 'Detailed benchmarking metrics: Accuracy, Precision, Recall, Confusion Matrix, and F1.' },
    { type: 'Suspicious Transaction Audit', desc: 'Auditor review logs, notes, and pending triaged transactions.' },
    { type: 'Dataset Overview Report', desc: 'Statistical summary, null value verification, and feature metadata.' }
  ];

  const [selectedType, setSelectedType] = useState('Executive Risk Summary');
  const [format, setFormat] = useState('html');
  const [author, setAuthor] = useState(user?.username || 'Fraud Analytics Operations');
  const [isGenerating, setIsGenerating] = useState(false);
  const [generatedReport, setGeneratedReport] = useState<any>(null);
  const [reportList, setReportList] = useState<any[]>([]);

  const loadReports = async () => {
    try {
      const list = await api.listReports();
      setReportList(list);
    } catch (err) {
      console.warn('Error loading reports list:', err);
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
      setGeneratedReport(res);
      showToast(`Generated ${res.report_type} (${res.format.toUpperCase()})`, 'success');
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

  return (
    <div className="space-y-6 max-w-6xl mx-auto pb-12">
      {/* Configuration Card */}
      <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-6 shadow-sm">
        <div className="flex items-center space-x-3 pb-4 border-b border-[#1e2432] mb-5">
          <div className="w-10 h-10 rounded-lg bg-emerald-950/80 border border-emerald-500/30 flex items-center justify-center text-emerald-400">
            <FileText className="w-5 h-5" />
          </div>
          <div>
            <h3 className="text-base font-bold text-slate-100">
              Enterprise Risk Report Generation Center
            </h3>
            <p className="text-xs text-slate-400">
              Compile formatted, regulatory-ready risk analytics and audit trails into standalone PDF or HTML documents.
            </p>
          </div>
        </div>

        <form onSubmit={handleGenerate} className="space-y-6 text-xs">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <label className="block font-semibold text-slate-300 mb-1.5 uppercase tracking-wider">
                Select Report Scope &amp; Type
              </label>
              <select
                value={selectedType}
                onChange={(e) => setSelectedType(e.target.value)}
                className="w-full bg-[#0b0e14] border border-[#232a3b] rounded-lg px-3 py-2 text-slate-100 focus:border-emerald-500 focus:outline-none"
              >
                {reportTypes.map((r) => (
                  <option key={r.type} value={r.type}>
                    {r.type}
                  </option>
                ))}
              </select>
            </div>

            <div>
              <label className="block font-semibold text-slate-300 mb-1.5 uppercase tracking-wider">
                Export File Format
              </label>
              <select
                value={format}
                onChange={(e) => setFormat(e.target.value)}
                className="w-full bg-[#0b0e14] border border-[#232a3b] rounded-lg px-3 py-2 text-slate-100 focus:border-emerald-500 focus:outline-none"
              >
                <option value="html">Interactive Standalone HTML Report</option>
                <option value="pdf">Formatted Portable Document Format (PDF via ReportLab)</option>
              </select>
            </div>

            <div className="md:col-span-2">
              <label className="block font-semibold text-slate-300 mb-1.5 uppercase tracking-wider">
                Author &amp; Operating Department
              </label>
              <input
                type="text"
                value={author}
                onChange={(e) => setAuthor(e.target.value)}
                className="w-full bg-[#0b0e14] border border-[#232a3b] rounded-lg px-3 py-2 text-slate-100 focus:border-emerald-500 focus:outline-none"
              />
            </div>
          </div>

          <div className="flex justify-end pt-2">
            <Button type="submit" variant="primary" icon={Play} isLoading={isGenerating}>
              Compile &amp; Generate Report
            </Button>
          </div>
        </form>
      </div>

      {/* In-App Report Live Preview */}
      {generatedReport && (
        <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-5 space-y-4 shadow-sm">
          <div className="flex items-center justify-between pb-3 border-b border-[#1e2432]">
            <div>
              <div className="flex items-center space-x-2 text-emerald-400 font-bold text-xs uppercase tracking-wider">
                <CheckCircle2 className="w-4 h-4" />
                <span>Report Generated Successfully</span>
              </div>
              <h4 className="text-sm font-bold text-slate-100 font-mono mt-0.5">
                {generatedReport.filename}
              </h4>
            </div>
            <Button
              variant="primary"
              size="sm"
              icon={Download}
              onClick={() => handleDownload(generatedReport.filename)}
            >
              Download {generatedReport.format.toUpperCase()}
            </Button>
          </div>

          {generatedReport.preview_html && (
            <div className="border border-[#1e2432] rounded-lg overflow-hidden bg-[#0d0f12] p-2">
              <iframe
                title="Report Live Preview"
                srcDoc={generatedReport.preview_html}
                className="w-full h-96 rounded bg-transparent"
              />
            </div>
          )}
        </div>
      )}

      {/* Generated Reports Archive */}
      <div className="bg-[#11141c] border border-[#1e2432] rounded-xl overflow-hidden shadow-sm">
        <div className="px-5 py-3.5 bg-[#141822] border-b border-[#1e2432] text-xs font-bold text-slate-300 uppercase tracking-wider">
          Previously Generated Report Documents Archive
        </div>
        <div className="divide-y divide-[#181d28] text-xs font-mono">
          {reportList.map((rep) => (
            <div key={rep.filename} className="p-4 flex items-center justify-between hover:bg-[#141822] transition-colors">
              <div className="flex items-center space-x-3">
                <FileText className="w-5 h-5 text-emerald-400 shrink-0" />
                <div>
                  <span className="font-bold text-slate-200 block truncate">{rep.filename}</span>
                  <span className="text-[11px] text-slate-500 font-sans">
                    Size: {(rep.size_bytes / 1024).toFixed(1)} KB &bull; Format: {rep.format}
                  </span>
                </div>
              </div>
              <Button size="sm" variant="secondary" icon={Download} onClick={() => handleDownload(rep.filename)}>
                Download
              </Button>
            </div>
          ))}

          {reportList.length === 0 && (
            <div className="p-8 text-center text-slate-500 font-sans">
              No reports generated in this workspace yet.
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
