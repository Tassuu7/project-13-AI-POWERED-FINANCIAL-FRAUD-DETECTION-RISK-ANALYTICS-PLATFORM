/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        dark: {
          950: '#07090c',
          900: '#0d1015',
          850: '#13171f',
          800: '#181d27',
          750: '#202633',
          700: '#2a3243',
          600: '#3e495f',
        },
        // Brand Emerald - Trust, Security, Normal operations
        brand: {
          DEFAULT: '#10b981',
          hover: '#059669',
          light: '#34d399',
          dark: '#047857',
          dim: 'rgba(16, 185, 129, 0.12)',
        },
        // Risk levels (strictly no blue)
        risk: {
          low: '#10b981',
          lowDim: 'rgba(16, 185, 129, 0.15)',
          medium: '#f59e0b',
          mediumDim: 'rgba(245, 158, 11, 0.15)',
          high: '#ef4444',
          highDim: 'rgba(239, 68, 68, 0.15)',
        }
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', '-apple-system', 'Segoe UI', 'sans-serif'],
        mono: ['JetBrains Mono', 'Fira Code', 'Courier New', 'monospace'],
      }
    },
  },
  plugins: [],
}
