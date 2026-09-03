import React, { useState, useEffect } from 'react';
import { AuthProvider, useAuth } from './context/AuthContext';
import { AppStateProvider } from './context/AppStateContext';
import { Sidebar } from './components/layout/Sidebar';
import { Header } from './components/layout/Header';
import { NotificationToast } from './components/layout/NotificationToast';

// Pages
import { LoginPage } from './pages/LoginPage';
import { DashboardPage } from './pages/DashboardPage';
import { TransactionAnalysisPage } from './pages/TransactionAnalysisPage';
import { FraudAnalysisPage } from './pages/FraudAnalysisPage';
import { InvestigationsPage } from './pages/InvestigationsPage';
import { ReportsPage } from './pages/ReportsPage';
import { ModelManagementPage } from './pages/ModelManagementPage';
import { ProcessingHistoryPage } from './pages/ProcessingHistoryPage';
import { SettingsPage } from './pages/SettingsPage';
import { HelpDocumentationPage } from './pages/HelpDocumentationPage';

const pageMetadata: Record<string, { title: string; subtitle: string }> = {
  dashboard: { title: 'Risk Intelligence Dashboard', subtitle: 'Operational metrics, priority queues, and executive fraud exposure telemetry' },
  analyze: { title: 'Transaction Analysis & Ingestion Pipeline', subtitle: 'Dataset ingestion, structural validation, cleaning, and exploratory profiling' },
  'fraud-analysis': { title: 'Fraud Analysis & Machine Learning Engine', subtitle: 'Multi-model classifier training, precision/recall curves, and real-time inference' },
  investigations: { title: 'Fraud Investigation Desk & Case Management', subtitle: 'Prioritized queue of anomalous transactions requiring auditor action and notes' },
  reports: { title: 'Compliance & Risk Reporting Center', subtitle: 'Compile standalone audit dossiers and executive risk summaries in HTML and PDF' },
  models: { title: 'Model Registry & Lifecycle Administration', subtitle: 'Administer local Scikit-Learn .joblib binaries and production scoring engines' },
  history: { title: 'Processing History & Audit Trail', subtitle: 'Immutable local JSON audit log tracking pipeline operations and model runs' },
  settings: { title: 'System Settings & Thresholds', subtitle: 'Calibrate risk score boundaries (Low/Med/High) and local storage paths' },
  help: { title: 'Documentation & Data Dictionary', subtitle: 'Operational reference guide, fraud mechanics, and canonical schema definitions' },
};

const MainLayout: React.FC = () => {
  const { user, logout, isAdmin, isAnalyst, isViewer } = useAuth();
  const [activePage, setActivePage] = useState<string>('dashboard');

  // Role security guard: redirect unauthorized pages to dashboard
  useEffect(() => {
    if (isViewer && ['analyze', 'models', 'history', 'settings'].includes(activePage)) {
      setActivePage('dashboard');
    } else if (isAnalyst && ['models', 'history', 'settings'].includes(activePage)) {
      setActivePage('dashboard');
    }
  }, [activePage, user?.role]);

  // If not logged in, render single Login Page
  if (!user) {
    return <LoginPage onComplete={() => setActivePage('dashboard')} />;
  }

  const meta = pageMetadata[activePage] || {
    title: 'Financial Fraud Detection',
    subtitle: 'Risk Analytics Platform'
  };

  return (
    <div className="flex h-screen bg-[#080a0d] text-slate-100 overflow-hidden font-sans selection:bg-emerald-900 selection:text-emerald-100">
      {/* Role-Specific Consolidated Sidebar */}
      <Sidebar
        activePage={activePage}
        setActivePage={setActivePage}
        onLogout={logout}
      />

      {/* Main Content Area */}
      <div className="flex-1 flex flex-col min-w-0 overflow-hidden">
        {/* Header */}
        <Header pageTitle={meta.title} pageSubtitle={meta.subtitle} />

        {/* Dynamic View (Full Screen Responsive) */}
        <main className="flex-1 overflow-y-auto p-8 w-full">
          {activePage === 'dashboard' && <DashboardPage onNavigate={setActivePage} />}
          {activePage === 'analyze' && <TransactionAnalysisPage />}
          {activePage === 'fraud-analysis' && <FraudAnalysisPage />}
          {activePage === 'investigations' && <InvestigationsPage />}
          {activePage === 'reports' && <ReportsPage />}
          {activePage === 'models' && <ModelManagementPage />}
          {activePage === 'history' && <ProcessingHistoryPage />}
          {activePage === 'settings' && <SettingsPage />}
          {activePage === 'help' && <HelpDocumentationPage />}
        </main>
      </div>

      {/* Global Notifications */}
      <NotificationToast />
    </div>
  );
};

export default function App() {
  return (
    <AuthProvider>
      <AppStateProvider>
        <MainLayout />
      </AppStateProvider>
    </AuthProvider>
  );
}
