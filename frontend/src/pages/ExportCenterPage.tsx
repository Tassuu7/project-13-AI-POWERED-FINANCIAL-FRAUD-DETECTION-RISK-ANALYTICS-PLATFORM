import React, { useState, useEffect } from 'react';
import { Download, FileSpreadsheet, FileCode, Database, CheckCircle2, RefreshCw } from 'lucide-react';
import { useAppState } from '../context/AppStateContext';
import { api } from '../services/api';
import { Button } from '../components/common/Button';

export const ExportCenterPage: React.FC = () => {
  const { selectedDataset, showToast } = useAppState();
  const [exportFiles, setExportFiles] = useState<any[]>([]);
  const [isLoading, setIsLoading] = useState(false);

  const loadExports = async () => {
    try {
      const list = await api.listExportFiles();
      setExportFiles(list);
    } catch (err) {
      console.warn('Error loading export files:', err);
    }
  };

  useEffect(() => {
    loadExports();
  }, []);

  const handleExportSuspicious = async () => {
    setIsLoading(true);
    try {
      const res = await api.exportSuspicious();
      showToast(`Exported suspicious transactions to ${res.filename}`, 'success');
      loadExports();
    } catch (err: any) {
      showToast(err.message || 'Export failed', 'error');
    } finally {
      setIsLoading(false);
    }
  };

  const handleExportMetrics = async () => {
    setIsLoading(true);
    try {
      const res = await api.exportMetrics();
      showToast(`Exported model benchmarks to ${res.filename}`, 'success');
      loadExports();
    } catch (err: any) {
      showToast(err.message || 'Export failed', 'error');
    } finally {
      setIsLoading(false);
    }
  };

  const handleDownloadDataset = () => {
    if (!selectedDataset) return;
    window.open(`http://localhost:8000/api/datasets/${selectedDataset}/download`, '_blank');
  };

  const handleDownloadExport = (filename: string) => {
    window.open(`http://localhost:8000/api/exports/download/${filename}`, '_blank');
  };

  return (
    <div className="space-y-6 max-w-5xl mx-auto pb-12">
      {/* Header Banner */}
      <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-6 flex items-center space-x-3">
        <div className="w-10 h-10 rounded-lg bg-emerald-950/80 border border-emerald-500/30 flex items-center justify-center text-emerald-400 shrink-0">
          <Download className="w-5 h-5" />
        </div>
        <div>
          <h3 className="text-base font-bold text-slate-100">Local Artifact Export Center</h3>
          <p className="text-xs text-slate-400 mt-0.5">
            Export scored transactions, audit queue items, and machine learning performance matrices directly to local file storage.
          </p>
        </div>
      </div>

      {/* Quick Action Export Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
        <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-5 flex flex-col justify-between shadow-sm space-y-4">
          <div className="flex items-center space-x-3">
            <div className="p-2.5 rounded-lg bg-emerald-950 border border-emerald-500/30 text-emerald-400">
              <FileSpreadsheet className="w-5 h-5" />
            </div>
            <div>
              <h4 className="text-sm font-bold text-slate-100">Suspicious Transactions</h4>
              <span className="text-xs text-slate-400">Format: CSV</span>
            </div>
          </div>
          <p className="text-xs text-slate-400 leading-relaxed">
            Extract current investigation desk queue with auditor review statuses, notes, and anomaly indicators.
          </p>
          <Button variant="primary" size="sm" icon={Download} onClick={handleExportSuspicious} isLoading={isLoading}>
            Generate CSV Export
          </Button>
        </div>

        <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-5 flex flex-col justify-between shadow-sm space-y-4">
          <div className="flex items-center space-x-3">
            <div className="p-2.5 rounded-lg bg-amber-950 border border-amber-500/30 text-amber-400">
              <FileCode className="w-5 h-5" />
            </div>
            <div>
              <h4 className="text-sm font-bold text-slate-100">Model Evaluation Metrics</h4>
              <span className="text-xs text-slate-400">Format: JSON</span>
            </div>
          </div>
          <p className="text-xs text-slate-400 leading-relaxed">
            Export confusion matrices, ROC-AUC scores, training times, and hyperparameter metadata for model governance.
          </p>
          <Button variant="secondary" size="sm" icon={Download} onClick={handleExportMetrics} isLoading={isLoading}>
            Generate JSON Export
          </Button>
        </div>

        <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-5 flex flex-col justify-between shadow-sm space-y-4">
          <div className="flex items-center space-x-3">
            <div className="p-2.5 rounded-lg bg-slate-900 border border-slate-700 text-slate-300">
              <Database className="w-5 h-5" />
            </div>
            <div>
              <h4 className="text-sm font-bold text-slate-100">Active Dataset File</h4>
              <span className="text-xs text-slate-400">Format: Raw CSV</span>
            </div>
          </div>
          <p className="text-xs text-slate-400 leading-relaxed truncate">
            Download raw CSV file for active dataset: {selectedDataset}
          </p>
          <Button variant="secondary" size="sm" icon={Download} onClick={handleDownloadDataset}>
            Download CSV File
          </Button>
        </div>
      </div>

      {/* Export Directory Listing */}
      <div className="bg-[#11141c] border border-[#1e2432] rounded-xl overflow-hidden shadow-sm">
        <div className="px-5 py-3.5 bg-[#141822] border-b border-[#1e2432] flex items-center justify-between">
          <span className="text-xs font-bold text-slate-300 uppercase tracking-wider">
            Available Export Artifacts in Local Filesystem (`exports/`)
          </span>
          <Button variant="ghost" size="sm" icon={RefreshCw} onClick={loadExports}>
            Refresh Files
          </Button>
        </div>

        <div className="divide-y divide-[#181d28] text-xs font-mono">
          {exportFiles.map((f) => (
            <div key={f.filename} className="p-4 flex items-center justify-between hover:bg-[#141822] transition-colors">
              <div>
                <span className="font-bold text-slate-200 block truncate">{f.filename}</span>
                <span className="text-[11px] text-slate-500 font-sans">
                  Size: {(f.size_bytes / 1024).toFixed(1)} KB &bull; Type: {f.extension}
                </span>
              </div>
              <Button size="sm" variant="secondary" icon={Download} onClick={() => handleDownloadExport(f.filename)}>
                Download
              </Button>
            </div>
          ))}

          {exportFiles.length === 0 && (
            <div className="p-8 text-center text-slate-500 font-sans">
              No export packages generated yet. Click above to generate CSV or JSON packages.
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
