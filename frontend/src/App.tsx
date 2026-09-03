import React, { useState } from 'react';
import { AuthProvider } from './context/AuthContext';
import { AppStateProvider, useAppState } from './context/AppStateContext';
import { Sidebar } from './components/layout/Sidebar';
import { Header } from './components/layout/Header';
import { NotificationToast } from './components/layout/NotificationToast';

// 20 Pages
import { LoginPage } from './pages/LoginPage';
import { DashboardPage } from './pages/DashboardPage';
import { DataUploadPage } from './pages/DataUploadPage';
import { SyntheticGeneratorPage } from './pages/SyntheticGeneratorPage';
import { DataValidationPage } from './pages/DataValidationPage';
import { PreprocessingPage } from './pages/PreprocessingPage';
import { FeatureEngineeringPage } from './pages/FeatureEngineeringPage';
import { EdaPage } from './pages/EdaPage';
import { ModelTrainingPage } from './pages/ModelTrainingPage';
import { ModelEvaluationPage } from './pages/ModelEvaluationPage';
import { FraudPredictionPage } from './pages/FraudPredictionPage';
import { RiskScoringPage } from './pages/RiskScoringPage';
import { TransactionExplorerPage } from './pages/TransactionExplorerPage';
import { SuspiciousTransactionsPage } from './pages/SuspiciousTransactionsPage';
import { ModelExplainabilityPage } from './pages/ModelExplainabilityPage';
import { ReportGenerationPage } from './pages/ReportGenerationPage';
import { ExportCenterPage } from './pages/ExportCenterPage';
import { ProcessingHistoryPage } from './pages/ProcessingHistoryPage';
import { SettingsPage } from './pages/SettingsPage';
import { HelpDocumentationPage } from './pages/HelpDocumentationPage';

const pageMetadata: Record<string, { title: string; subtitle: string }> = {
  dashboard: { title: 'Executive Fraud Analytics Dashboard', subtitle: 'Live transaction volume, risk tier distributions, and active model metrics' },
  login: { title: 'Application Access & Role Authorization', subtitle: 'Demo session management with Analyst, Reviewer, and Admin permissions' },
  upload: { title: 'Dataset Upload & Ingestion', subtitle: 'Drag-and-drop local CSV files for validation, profiling, and modeling' },
  generator: { title: 'Synthetic Financial Data Generator', subtitle: 'Deterministic, privacy-safe transaction generator with realistic fraud vectors' },
  validation: { title: 'Data Quality & Schema Validation Engine', subtitle: 'Integrity diagnostics, null detection, and schema verification' },
  preprocessing: { title: 'Data Preprocessing Pipeline', subtitle: 'Missing value imputation, categorical encoding, scaling, and train/test splits' },
  features: { title: 'Domain Fraud Feature Engineering', subtitle: 'Derive spend deviations, night-hour flags, and rapid velocity counters' },
  eda: { title: 'Exploratory Data Analysis (EDA)', subtitle: 'Statistical distributions, five-number summaries, and fraud correlations' },
  training: { title: 'Machine Learning Model Training', subtitle: 'Train Logistic Regression, Random Forest, Gradient Boosting, and Isolation Forest' },
  evaluation: { title: 'Model Evaluation & Benchmarks', subtitle: 'Compare algorithms on Precision, Recall, F1-Score, and Confusion Matrix' },
  prediction: { title: 'Real-Time Fraud Prediction', subtitle: 'Single transaction inference and batch dataset risk classification' },
  risk: { title: 'Transparent Risk Scoring Engine', subtitle: 'Calibrate 0–100 risk scores combining ML probability and verified heuristics' },
  explainability: { title: 'Model Interpretability & SHAP Waterfall', subtitle: 'Global feature importance rankings and local per-transaction factor attribution' },
  transactions: { title: 'Transaction Explorer & Ledger', subtitle: 'Search, multi-filter, sort, and paginate through transaction records' },
  suspicious: { title: 'Suspicious Transactions Investigation Desk', subtitle: 'Triage high-risk anomalies, append notes, and update audit statuses' },
  reports: { title: 'Report Generation Center', subtitle: 'Compile executive risk and evaluation reports in HTML and PDF formats' },
  exports: { title: 'Artifact Export Center', subtitle: 'Download predictions, suspicious transaction queues, and metrics locally' },
  history: { title: 'Processing History & Audit Trail', subtitle: 'Immutable JSON audit log tracking pipeline operations and model deployments' },
  settings: { title: 'System Settings & Thresholds', subtitle: 'Manage risk threshold bands, active model selector, and storage retention' },
  help: { title: 'Documentation & Data Dictionary', subtitle: 'Operating reference guide, fraud mechanics, and complete schema dictionary' },
};

const MainApp: React.FC = () => {
  const [activePage, setActivePage] = useState<string>('dashboard');
  const meta = pageMetadata[activePage] || { title: 'Financial Fraud Detection', subtitle: 'Risk Analytics Platform' };

  return (
    <div className="flex h-screen bg-[#080a0d] text-slate-100 overflow-hidden font-sans">
      {/* Sidebar Navigation */}
      <Sidebar activePage={activePage} setActivePage={setActivePage} />

      {/* Main Content Area */}
      <div className="flex-1 flex flex-col min-w-0 overflow-hidden">
        {/* Top Header */}
        <Header pageTitle={meta.title} pageSubtitle={meta.subtitle} />

        {/* Dynamic Page View */}
        <main className="flex-1 overflow-y-auto p-6">
          {activePage === 'dashboard' && <DashboardPage />}
          {activePage === 'login' && <LoginPage onComplete={() => setActivePage('dashboard')} />}
          {activePage === 'upload' && <DataUploadPage onNavigateNext={() => setActivePage('validation')} />}
          {activePage === 'generator' && <SyntheticGeneratorPage onNavigateNext={() => setActivePage('validation')} />}
          {activePage === 'validation' && <DataValidationPage onNavigateNext={() => setActivePage('preprocessing')} />}
          {activePage === 'preprocessing' && <PreprocessingPage onNavigateNext={() => setActivePage('features')} />}
          {activePage === 'features' && <FeatureEngineeringPage onNavigateNext={() => setActivePage('eda')} />}
          {activePage === 'eda' && <EdaPage onNavigateNext={() => setActivePage('training')} />}
          {activePage === 'training' && <ModelTrainingPage onNavigateNext={() => setActivePage('evaluation')} />}
          {activePage === 'evaluation' && <ModelEvaluationPage onNavigateNext={() => setActivePage('prediction')} />}
          {activePage === 'prediction' && <FraudPredictionPage onNavigateNext={() => setActivePage('suspicious')} />}
          {activePage === 'risk' && <RiskScoringPage />}
          {activePage === 'explainability' && <ModelExplainabilityPage />}
          {activePage === 'transactions' && <TransactionExplorerPage />}
          {activePage === 'suspicious' && <SuspiciousTransactionsPage />}
          {activePage === 'reports' && <ReportGenerationPage />}
          {activePage === 'exports' && <ExportCenterPage />}
          {activePage === 'history' && <ProcessingHistoryPage />}
          {activePage === 'settings' && <SettingsPage />}
          {activePage === 'help' && <HelpDocumentationPage />}
        </main>
      </div>

      {/* Global Notification Toast */}
      <NotificationToast />
    </div>
  );
};

export default function App() {
  return (
    <AuthProvider>
      <AppStateProvider>
        <MainApp />
      </AppStateProvider>
    </AuthProvider>
  );
}
