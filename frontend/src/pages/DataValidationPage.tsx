import React, { useState, useEffect } from 'react';
import { CheckCircle2, AlertTriangle, XCircle, Info, RefreshCw, ArrowRight, ShieldCheck } from 'lucide-react';
import { useAppState } from '../context/AppStateContext';
import { api } from '../services/api';
import { ValidationReport, ValidationCheck } from '../types';
import { Button } from '../components/common/Button';

export const DataValidationPage: React.FC<{ onNavigateNext?: () => void }> = ({ onNavigateNext }) => {
  const { selectedDataset } = useAppState();
  const [report, setReport] = useState<ValidationReport | null>(null);
  const [isValidating, setIsValidating] = useState(false);

  const runValidation = async () => {
    if (!selectedDataset) return;
    setIsValidating(true);
    try {
      const rep = await api.validateDataset(selectedDataset);
      setReport(rep);
    } catch (err) {
      console.warn('Validation error:', err);
    } finally {
      setIsValidating(false);
    }
  };

  useEffect(() => {
    runValidation();
  }, [selectedDataset]);

  return (
    <div className="space-y-6 max-w-5xl mx-auto pb-12">
      {/* Top Header Card */}
      <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-5 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2">
            <ShieldCheck className="w-5 h-5 text-emerald-400" />
            <h3 className="text-base font-bold text-slate-100">
              Dataset Integrity &amp; Quality Validation Engine
            </h3>
          </div>
          <p className="text-xs text-slate-400 mt-1">
            Analyzing <span className="font-mono text-emerald-400 font-bold">{selectedDataset}</span> against enterprise financial schemas.
          </p>
        </div>
        <div className="flex items-center space-x-3">
          <Button variant="secondary" size="sm" icon={RefreshCw} onClick={runValidation} isLoading={isValidating}>
            Re-run Validation
          </Button>
          {report && report.valid && onNavigateNext && (
            <Button variant="primary" size="sm" icon={ArrowRight} onClick={onNavigateNext}>
              Proceed to Preprocessing
            </Button>
          )}
        </div>
      </div>

      {isValidating && (
        <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-8 text-center">
          <RefreshCw className="w-8 h-8 text-emerald-400 animate-spin mx-auto mb-2" />
          <p className="text-xs text-slate-400">Executing mathematical integrity verification rules...</p>
        </div>
      )}

      {report && !isValidating && (
        <>
          {/* Summary Strip */}
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
            <div className="bg-[#11141c] border border-[#1e2432] p-4 rounded-xl">
              <span className="text-xs text-slate-400 uppercase tracking-wider">Validation Status</span>
              <div className="flex items-center space-x-2 mt-1.5">
                {report.valid ? (
                  <>
                    <CheckCircle2 className="w-5 h-5 text-emerald-400" />
                    <span className="text-base font-bold text-emerald-400">PASSED</span>
                  </>
                ) : (
                  <>
                    <XCircle className="w-5 h-5 text-rose-400" />
                    <span className="text-base font-bold text-rose-400">CRITICAL ERROR</span>
                  </>
                )}
              </div>
            </div>

            <div className="bg-[#11141c] border border-[#1e2432] p-4 rounded-xl">
              <span className="text-xs text-slate-400 uppercase tracking-wider">Total Records</span>
              <div className="text-xl font-bold text-slate-100 font-mono mt-1.5">
                {report.total_records.toLocaleString()}
              </div>
            </div>

            <div className="bg-[#11141c] border border-[#1e2432] p-4 rounded-xl">
              <span className="text-xs text-slate-400 uppercase tracking-wider">Checks Passed</span>
              <div className="text-xl font-bold text-emerald-400 font-mono mt-1.5">
                {report.passed_checks} / {report.total_checks}
              </div>
            </div>

            <div className="bg-[#11141c] border border-[#1e2432] p-4 rounded-xl">
              <span className="text-xs text-slate-400 uppercase tracking-wider">Failed / Warnings</span>
              <div className={`text-xl font-bold font-mono mt-1.5 ${report.failed_checks > 0 ? 'text-amber-400' : 'text-slate-500'}`}>
                {report.failed_checks}
              </div>
            </div>
          </div>

          {/* Validation Checklist */}
          <div className="bg-[#11141c] border border-[#1e2432] rounded-xl overflow-hidden shadow-sm">
            <div className="px-5 py-3.5 bg-[#141822] border-b border-[#1e2432] text-xs font-bold text-slate-300 uppercase tracking-wider">
              Diagnostic Quality Checklist
            </div>
            <div className="divide-y divide-[#181d28]">
              {report.checks.map((c: ValidationCheck, idx: number) => {
                const isPassed = c.passed;
                const isError = !c.passed && c.severity === 'error';
                const isWarning = !c.passed && c.severity === 'warning';

                return (
                  <div key={idx} className="p-4 flex items-start space-x-3 hover:bg-[#131722] transition-colors">
                    <div className="pt-0.5 shrink-0">
                      {isPassed && <CheckCircle2 className="w-5 h-5 text-emerald-400" />}
                      {isError && <XCircle className="w-5 h-5 text-rose-400" />}
                      {isWarning && <AlertTriangle className="w-5 h-5 text-amber-400" />}
                    </div>
                    <div className="flex-1 min-w-0">
                      <div className="flex items-center space-x-2">
                        <span className="text-sm font-semibold text-slate-200">{c.name}</span>
                        <span className={`px-2 py-0.5 rounded text-[10px] font-bold uppercase ${
                          c.severity === 'error' ? 'bg-rose-950 text-rose-400 border border-rose-800/40' :
                          c.severity === 'warning' ? 'bg-amber-950 text-amber-400 border border-amber-800/40' :
                          'bg-emerald-950 text-emerald-400 border border-emerald-800/40'
                        }`}>
                          {c.severity}
                        </span>
                        {c.affected_count > 0 && (
                          <span className="text-[11px] text-slate-400 font-mono">
                            ({c.affected_count} affected)
                          </span>
                        )}
                      </div>
                      <p className="text-xs text-slate-400 mt-1 leading-relaxed">{c.details}</p>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>

          {/* Recommendations Box */}
          <div className="bg-[#11141c] border border-[#1e2432] rounded-xl p-5">
            <h4 className="text-xs font-bold text-slate-300 uppercase tracking-wider mb-2 flex items-center space-x-2">
              <Info className="w-4 h-4 text-emerald-400" />
              <span>Recommended Preprocessing Actions</span>
            </h4>
            <ul className="space-y-1.5 text-xs text-slate-300 list-disc list-inside">
              {report.recommended_actions.map((act, i) => (
                <li key={i}>{act}</li>
              ))}
            </ul>
          </div>
        </>
      )}
    </div>
  );
};
