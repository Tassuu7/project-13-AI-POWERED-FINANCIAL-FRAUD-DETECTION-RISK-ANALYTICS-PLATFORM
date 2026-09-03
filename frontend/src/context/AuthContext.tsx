import React, { createContext, useContext, useState, useEffect } from 'react';
import { UserSession, UserRole } from '../types';
import { api } from '../services/api';

interface AuthContextType {
  user: UserSession | null;
  login: (username: string, role: UserRole) => Promise<void>;
  logout: () => void;
  isLoading: boolean;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [user, setUser] = useState<UserSession | null>({
    username: 'tasleema_analyst',
    role: 'Analyst',
    authenticated: true,
    permissions: ['all']
  });
  const [isLoading, setIsLoading] = useState<boolean>(false);

  const login = async (username: string, role: UserRole) => {
    setIsLoading(true);
    try {
      const session = await api.login(username, role);
      setUser(session);
    } catch (e) {
      // Fallback local session if server not reachable
      setUser({
        username: username || 'demo_analyst',
        role,
        authenticated: true,
        permissions: ['read', 'write']
      });
    } finally {
      setIsLoading(false);
    }
  };

  const logout = () => {
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, login, logout, isLoading }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error('useAuth must be used within AuthProvider');
  return ctx;
};
