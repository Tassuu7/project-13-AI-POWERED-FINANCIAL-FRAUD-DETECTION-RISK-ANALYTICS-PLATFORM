import React, { createContext, useContext, useState, useEffect } from 'react';
import { DatasetInfo } from '../types';
import { api } from '../services/api';

interface AppStateContextType {
  selectedDataset: string;
  setSelectedDataset: (name: string) => void;
  datasets: DatasetInfo[];
  refreshDatasets: () => Promise<void>;
  activeModel: string;
  setActiveModel: (name: string) => void;
  toast: { message: string; type: 'success' | 'error' | 'info' } | null;
  showToast: (message: string, type?: 'success' | 'error' | 'info') => void;
  clearToast: () => void;
}

const AppStateContext = createContext<AppStateContextType | undefined>(undefined);

export const AppStateProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [selectedDataset, setSelectedDataset] = useState<string>('sample_synthetic_transactions.csv');
  const [datasets, setDatasets] = useState<DatasetInfo[]>([]);
  const [activeModel, setActiveModel] = useState<string>('Random Forest');
  const [toast, setToast] = useState<{ message: string; type: 'success' | 'error' | 'info' } | null>(null);

  const showToast = (message: string, type: 'success' | 'error' | 'info' = 'success') => {
    setToast({ message, type });
    setTimeout(() => {
      setToast(null);
    }, 4000);
  };

  const clearToast = () => setToast(null);

  const refreshDatasets = async () => {
    try {
      const list = await api.listDatasets();
      setDatasets(list);
      if (list.length > 0 && (!selectedDataset || !list.some(d => d.filename === selectedDataset))) {
        setSelectedDataset(list[0].filename);
      }
    } catch (e) {
      console.warn('Could not load datasets initially:', e);
    }
  };

  useEffect(() => {
    refreshDatasets();
  }, []);

  return (
    <AppStateContext.Provider
      value={{
        selectedDataset,
        setSelectedDataset,
        datasets,
        refreshDatasets,
        activeModel,
        setActiveModel,
        toast,
        showToast,
        clearToast,
      }}
    >
      {children}
    </AppStateContext.Provider>
  );
};

export const useAppState = () => {
  const ctx = useContext(AppStateContext);
  if (!ctx) throw new Error('useAppState must be used within AppStateProvider');
  return ctx;
};
