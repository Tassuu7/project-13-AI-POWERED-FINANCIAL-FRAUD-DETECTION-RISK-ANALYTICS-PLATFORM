import React from 'react';
import { CheckCircle2, AlertCircle, Info, X } from 'lucide-react';
import { useAppState } from '../../context/AppStateContext';

export const NotificationToast: React.FC = () => {
  const { toast, clearToast } = useAppState();

  if (!toast) return null;

  const isSuccess = toast.type === 'success';
  const isError = toast.type === 'error';

  return (
    <div className="fixed bottom-5 right-5 z-50 flex items-center space-x-3 px-4 py-3 rounded-lg shadow-xl border backdrop-blur-sm bg-[#10141d]/95 border-[#222938] text-sm animate-in fade-in slide-in-from-bottom-3 duration-200">
      {isSuccess && <CheckCircle2 className="w-5 h-5 text-emerald-400 shrink-0" />}
      {isError && <AlertCircle className="w-5 h-5 text-rose-400 shrink-0" />}
      {!isSuccess && !isError && <Info className="w-5 h-5 text-amber-400 shrink-0" />}

      <span className="text-slate-200 font-medium">{toast.message}</span>

      <button
        onClick={clearToast}
        className="text-slate-400 hover:text-slate-200 p-1 rounded transition-colors"
      >
        <X className="w-4 h-4" />
      </button>
    </div>
  );
};
