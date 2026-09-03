import React, { useState, useRef } from 'react';
import { UploadCloud, FileText, CheckCircle2, AlertTriangle, ArrowRight, Eye, Table } from 'lucide-react';
import { useAppState } from '../context/AppStateContext';
import { api } from '../services/api';
import { Button } from '../components/common/Button';

export const DataUploadPage: React.FC<{ onNavigateNext?: () => void }> = ({ onNavigateNext }) => {
  const { setSelectedDataset, refreshDatasets, showToast } = useAppState();
  const [file, setFile] = useState<File | null>(null);
  const [isUploading, setIsUploading] = useState(false);
  const [preview, setPreview] = useState<any>(null);
  const [dragActive, setDragActive] = useState(false);
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleDrag = (e: React.DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    if (e.type === 'dragenter' || e.type === 'dragover') {
      setDragActive(true);
    } else if (e.type === 'dragleave') {
      setDragActive(false);
    }
  };

  const handleDrop = (e: React.DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(false);
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      const droppedFile = e.dataTransfer.files[0];
      if (droppedFile.name.endsWith('.csv')) {
        setFile(droppedFile);
      } else {
        showToast('Only CSV files are accepted.', 'error');
      }
    }
  };

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      setFile(e.target.files[0]);
    }
  };

  const handleUpload = async () => {
    if (!file) return;
    setIsUploading(true);
    try {
      const res = await api.uploadDataset(file);
      showToast(`Uploaded ${res.filename} (${res.rows} records)`, 'success');
      await refreshDatasets();
      setSelectedDataset(res.filename);

      // Load preview
      const previewData = await api.previewDataset(res.filename, 10);
      setPreview(previewData);
    } catch (err: any) {
      showToast(err.message || 'Upload failed', 'error');
    } finally {
      setIsUploading(false);
    }
  };

  return (
    <div className="space-y-6 max-w-5xl mx-auto pb-12">
      {/* Upload Box */}
      <div
        onDragEnter={handleDrag}
        onDragOver={handleDrag}
        onDragLeave={handleDrag}
        onDrop={handleDrop}
        className={`bg-[#11141c] border-2 border-dashed rounded-xl p-8 text-center transition-all ${
          dragActive
            ? 'border-emerald-500 bg-emerald-950/20'
            : 'border-[#222938] hover:border-slate-600'
        }`}
      >
        <input
          ref={fileInputRef}
          type="file"
          accept=".csv"
          onChange={handleFileChange}
          className="hidden"
        />

        <div className="w-14 h-14 rounded-full bg-emerald-950/70 border border-emerald-500/30 flex items-center justify-center text-emerald-400 mx-auto mb-4">
          <UploadCloud className="w-7 h-7" />
        </div>

        <h3 className="text-base font-bold text-slate-100 mb-1">
          Upload Financial Transaction Dataset
        </h3>
        <p className="text-xs text-slate-400 max-w-md mx-auto mb-4">
          Drag and drop your transaction CSV file here, or browse local files. Maximum file limit is 50 MB.
        </p>

        <div className="flex items-center justify-center space-x-3">
          <Button
            type="button"
            variant="secondary"
            onClick={() => fileInputRef.current?.click()}
          >
            Select CSV File
          </Button>
          {file && (
            <Button
              type="button"
              variant="primary"
              onClick={handleUpload}
              isLoading={isUploading}
            >
              Upload &amp; Analyze
            </Button>
          )}
        </div>

        {file && (
          <div className="mt-4 inline-flex items-center space-x-2 bg-[#0d1016] border border-[#1f2535] px-3 py-1.5 rounded text-xs text-slate-300">
            <FileText className="w-4 h-4 text-emerald-400" />
            <span>{file.name}</span>
            <span className="text-slate-500 font-mono">({(file.size / 1024).toFixed(1)} KB)</span>
          </div>
        )}
      </div>

      {/* Dataset Preview Section */}
      {preview && (
        <div className="bg-[#11141c] border border-[#1d2330] rounded-xl p-5 space-y-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-2">
              <Table className="w-4 h-4 text-emerald-400" />
              <h4 className="text-sm font-bold text-slate-200 uppercase tracking-wider">
                Dataset Structure Preview: {preview.filename}
              </h4>
            </div>
            {onNavigateNext && (
              <Button variant="primary" size="sm" icon={ArrowRight} onClick={onNavigateNext}>
                Proceed to Data Validation
              </Button>
            )}
          </div>

          <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 text-xs">
            <div className="bg-[#0b0e14] p-3 rounded border border-[#1d2330]">
              <span className="text-slate-400">Total Rows</span>
              <div className="text-base font-bold text-slate-100 font-mono mt-1">
                {preview.total_rows.toLocaleString()}
              </div>
            </div>
            <div className="bg-[#0b0e14] p-3 rounded border border-[#1d2330]">
              <span className="text-slate-400">Columns Detected</span>
              <div className="text-base font-bold text-slate-100 font-mono mt-1">
                {preview.total_columns}
              </div>
            </div>
            <div className="bg-[#0b0e14] p-3 rounded border border-[#1d2330]">
              <span className="text-slate-400">Ground Truth Label</span>
              <div className="text-base font-bold text-emerald-400 font-mono mt-1">
                {preview.has_fraud_label ? 'Present (is_fraud)' : 'Unlabeled'}
              </div>
            </div>
            <div className="bg-[#0b0e14] p-3 rounded border border-[#1d2330]">
              <span className="text-slate-400">Fraud Cases</span>
              <div className="text-base font-bold text-rose-400 font-mono mt-1">
                {preview.fraud_count} ({preview.fraud_rate}%)
              </div>
            </div>
          </div>

          {/* Table Preview */}
          <div className="overflow-x-auto rounded border border-[#1d2330]">
            <table className="w-full text-xs text-left">
              <thead className="bg-[#171c26] text-slate-300 font-semibold border-b border-[#1d2330]">
                <tr>
                  {preview.columns.slice(0, 8).map((col: string) => (
                    <th key={col} className="px-3 py-2.5 whitespace-nowrap">
                      {col}
                    </th>
                  ))}
                </tr>
              </thead>
              <tbody className="divide-y divide-[#171c26] text-slate-300">
                {preview.data.map((row: any, idx: number) => (
                  <tr key={idx} className="hover:bg-[#151923]">
                    {preview.columns.slice(0, 8).map((col: string) => (
                      <td key={col} className="px-3 py-2 font-mono whitespace-nowrap">
                        {String(row[col] ?? '-')}
                      </td>
                    ))}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      )}
    </div>
  );
};
