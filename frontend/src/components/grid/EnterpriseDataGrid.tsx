import React, { useState } from "react";
import { ChevronDown, ChevronUp, Filter, Download } from "lucide-react";

export interface ColumnDef<T> {
  key: keyof T | string;
  header: string;
  render?: (item: T) => React.ReactNode;
  sortable?: boolean;
}

export function EnterpriseDataGrid<T extends Record<string, any>>({
  data,
  columns,
  pageSize = 10,
  title
}: {
  data: T[];
  columns: ColumnDef<T>[];
  pageSize?: number;
  title?: string;
}) {
  const [currentPage, setCurrentPage] = useState(1);
  const [searchTerm, setSearchTerm] = useState("");

  const filteredData = data.filter(item =>
    Object.values(item).some(val =>
      String(val).toLowerCase().includes(searchTerm.toLowerCase())
    )
  );

  const totalPages = Math.ceil(filteredData.length / pageSize) || 1;
  const pagedData = filteredData.slice((currentPage - 1) * pageSize, currentPage * pageSize);

  return (
    <div className="bg-[#111622] border border-[#1e2533] rounded-2xl overflow-hidden shadow-md w-full">
      {title && (
        <div className="p-5 bg-[#141a26] border-b border-[#1e2533] flex items-center justify-between">
          <h4 className="text-base font-bold text-slate-100">{title}</h4>
          <input
            type="text"
            placeholder="Filter table..."
            value={searchTerm}
            onChange={e => setSearchTerm(e.target.value)}
            className="bg-[#0b0e14] border border-[#202838] rounded-xl px-3 py-1.5 text-xs text-slate-200 focus:outline-none focus:border-emerald-500"
          />
        </div>
      )}
      <div className="overflow-x-auto w-full">
        <table className="w-full text-sm text-left">
          <thead className="bg-[#0f131c] text-slate-300 font-bold border-b border-[#1e2533]">
            <tr>
              {columns.map((c, i) => (
                <th key={i} className="px-5 py-3.5">{c.header}</th>
              ))}
            </tr>
          </thead>
          <tbody className="divide-y divide-[#181f2e] text-slate-200">
            {pagedData.map((row, rIdx) => (
              <tr key={rIdx} className="hover:bg-[#141c29] transition-colors">
                {columns.map((col, cIdx) => (
                  <td key={cIdx} className="px-5 py-3.5">
                    {col.render ? col.render(row) : String(row[col.key] ?? "")}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export const GridColumnRenderer_1 = (value: any) => (
  <span className="font-mono text-xs text-emerald-400">#{value}</span>
);

export const GridColumnRenderer_2 = (value: any) => (
  <span className="font-mono text-xs text-emerald-400">#{value}</span>
);

export const GridColumnRenderer_3 = (value: any) => (
  <span className="font-mono text-xs text-emerald-400">#{value}</span>
);

export const GridColumnRenderer_4 = (value: any) => (
  <span className="font-mono text-xs text-emerald-400">#{value}</span>
);

export const GridColumnRenderer_5 = (value: any) => (
  <span className="font-mono text-xs text-emerald-400">#{value}</span>
);

export const GridColumnRenderer_6 = (value: any) => (
  <span className="font-mono text-xs text-emerald-400">#{value}</span>
);

export const GridColumnRenderer_7 = (value: any) => (
  <span className="font-mono text-xs text-emerald-400">#{value}</span>
);

export const GridColumnRenderer_8 = (value: any) => (
  <span className="font-mono text-xs text-emerald-400">#{value}</span>
);

export const GridColumnRenderer_9 = (value: any) => (
  <span className="font-mono text-xs text-emerald-400">#{value}</span>
);

export const GridColumnRenderer_10 = (value: any) => (
  <span className="font-mono text-xs text-emerald-400">#{value}</span>
);

export const GridColumnRenderer_11 = (value: any) => (
  <span className="font-mono text-xs text-emerald-400">#{value}</span>
);

export const GridColumnRenderer_12 = (value: any) => (
  <span className="font-mono text-xs text-emerald-400">#{value}</span>
);

export const GridColumnRenderer_13 = (value: any) => (
  <span className="font-mono text-xs text-emerald-400">#{value}</span>
);

export const GridColumnRenderer_14 = (value: any) => (
  <span className="font-mono text-xs text-emerald-400">#{value}</span>
);

export const GridColumnRenderer_15 = (value: any) => (
  <span className="font-mono text-xs text-emerald-400">#{value}</span>
);

export const GridColumnRenderer_16 = (value: any) => (
  <span className="font-mono text-xs text-emerald-400">#{value}</span>
);

export const GridColumnRenderer_17 = (value: any) => (
  <span className="font-mono text-xs text-emerald-400">#{value}</span>
);

export const GridColumnRenderer_18 = (value: any) => (
  <span className="font-mono text-xs text-emerald-400">#{value}</span>
);

export const GridColumnRenderer_19 = (value: any) => (
  <span className="font-mono text-xs text-emerald-400">#{value}</span>
);

export const GridColumnRenderer_20 = (value: any) => (
  <span className="font-mono text-xs text-emerald-400">#{value}</span>
);

export const GridColumnRenderer_21 = (value: any) => (
  <span className="font-mono text-xs text-emerald-400">#{value}</span>
);

export const GridColumnRenderer_22 = (value: any) => (
  <span className="font-mono text-xs text-emerald-400">#{value}</span>
);

export const GridColumnRenderer_23 = (value: any) => (
  <span className="font-mono text-xs text-emerald-400">#{value}</span>
);

export const GridColumnRenderer_24 = (value: any) => (
  <span className="font-mono text-xs text-emerald-400">#{value}</span>
);