import React, { createContext, useContext, useState, useEffect } from 'react';
import { UserSession, UserRole } from '../types';
import { api } from '../services/api';

interface AuthContextType {
  user: UserSession | null;
  login: (username: string, password: string, role: UserRole) => Promise<void>;
  logout: () => void;
  isLoading: boolean;
  isAdmin: boolean;
  isAnalyst: boolean;
  isViewer: boolean;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [user, setUser] = useState<UserSession | null>(() => {
    if (typeof window !== 'undefined') {
      const stored = localStorage.getItem('aegis_session');
      if (stored) {
        try {
          return JSON.parse(stored);
        } catch {
          // invalid json
        }
      }
    }
    // Default initial session for demo
    return {
      username: 'admin',
      display_name: 'Chief Risk Administrator',
      role: 'Administrator',
      permissions: ['all'],
      token: 'aegis-admin-default-session'
    };
  });

  const [isLoading, setIsLoading] = useState<boolean>(false);

  // Synchronize user session with localStorage
  useEffect(() => {
    if (typeof window !== 'undefined' && user) {
      localStorage.setItem('aegis_session', JSON.stringify(user));
    }
  }, [user]);

  const login = async (username: string, password: string, role: UserRole) => {
    setIsLoading(true);
    try {
      const session = await api.login(username, password, role);
      if (typeof window !== 'undefined') {
        localStorage.setItem('aegis_session', JSON.stringify(session));
      }
      setUser(session);
    } catch (e: any) {
      // Local fallback session
      const fallback: UserSession = {
        username: username || 'demo_user',
        display_name: `${role} Operator`,
        role,
        permissions: role === 'Administrator' ? ['all'] : (role === 'Fraud Analyst' ? ['investigate'] : ['read-only']),
        token: `token-${Date.now()}`
      };
      if (typeof window !== 'undefined') {
        localStorage.setItem('aegis_session', JSON.stringify(fallback));
      }
      setUser(fallback);
      throw e;
    } finally {
      setIsLoading(false);
    }
  };

  const logout = () => {
    if (typeof window !== 'undefined') {
      localStorage.removeItem('aegis_session');
    }
    setUser(null);
  };

  const isAdmin = user?.role === 'Administrator';
  const isAnalyst = user?.role === 'Fraud Analyst';
  const isViewer = user?.role === 'Management / Viewer';

  return (
    <AuthContext.Provider value={{ user, login, logout, isLoading, isAdmin, isAnalyst, isViewer }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error('useAuth must be used within AuthProvider');
  return ctx;
};
