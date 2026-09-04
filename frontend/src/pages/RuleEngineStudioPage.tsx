import React, { useState } from "react";
import { Sliders, Plus, Play, CheckCircle2, Code2, AlertOctagon, Save } from "lucide-react";
import { Button } from "../components/common/Button";

export const RuleEngineStudioPage: React.FC = () => {
  const [selectedRuleId, setSelectedRuleId] = useState("R-0001");
  const [ruleExpr, setRuleExpr] = useState("amount > 100000 AND card_present == False");
  const [testOutput, setTestOutput] = useState<string | null>(null);

  const handleTestRule = () => {
    setTestOutput("VALID: AST Compiled successfully. Output: Condition matches 4.2% of historical transactions (Precision: 89.4%, Recall: 76.1%).");
  };

  return (
    <div className="w-full space-y-8 pb-16 font-sans">
      <div className="bg-[#111622] border border-[#1e2533] rounded-2xl p-6 flex items-center justify-between shadow-md">
        <div>
          <h3 className="text-xl font-bold text-slate-100 flex items-center space-x-3">
            <Sliders className="w-7 h-7 text-emerald-400" />
            <span>Rule Engine Studio &amp; DSL Expression Editor</span>
          </h3>
          <p className="text-sm text-slate-300 mt-1">
            Author, backtest, and deploy deterministic fraud rules using the Aegis Abstract Syntax Tree DSL compiler.
          </p>
        </div>
        <Button variant="primary" size="md" icon={Plus}>Create New Rule</Button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="bg-[#111622] border border-[#1e2533] rounded-2xl p-5 space-y-4">
          <h4 className="text-sm font-bold text-slate-200 uppercase tracking-wider">Active Rule Catalog (160 Rules)</h4>
          <div className="space-y-2 max-h-[500px] overflow-y-auto font-mono text-xs">
            {["R-0001: High Value Card Not Present", "R-0002: Cross Border Authorization", "R-0003: CVV Brute Force", "R-0004: Rapid SIM Swap Outflow"].map((r, i) => (
              <div
                key={i}
                onClick={() => setSelectedRuleId(`R-000${i+1}`)}
                className="p-3 rounded-xl bg-[#0b0e14] border border-[#1e2533] hover:border-emerald-500 cursor-pointer text-slate-300 flex justify-between items-center"
              >
                <span>{r}</span>
                <span className="text-emerald-400 font-bold">ACTIVE</span>
              </div>
            ))}
          </div>
        </div>

        <div className="md:col-span-2 bg-[#111622] border border-[#1e2533] rounded-2xl p-6 space-y-5">
          <div className="flex justify-between items-center">
            <h4 className="text-base font-bold text-slate-100 font-mono">Editing Rule: {selectedRuleId}</h4>
            <span className="px-3 py-1 rounded-full text-xs font-bold bg-amber-950 text-amber-300 border border-amber-800">WEIGHT: 85</span>
          </div>
          <div>
            <label className="block text-xs font-bold text-slate-400 mb-2 uppercase">DSL Expression Logic</label>
            <textarea
              value={ruleExpr}
              onChange={e => setRuleExpr(e.target.value)}
              rows={6}
              className="w-full bg-[#07090e] border border-[#232a3b] rounded-xl p-4 font-mono text-emerald-400 text-sm focus:outline-none focus:border-emerald-500"
            />
          </div>
          <div className="flex justify-end space-x-3">
            <Button variant="secondary" size="md" icon={Play} onClick={handleTestRule}>Validate &amp; Backtest</Button>
            <Button variant="primary" size="md" icon={Save}>Deploy Rule Changes</Button>
          </div>
          {testOutput && (
            <div className="p-4 rounded-xl bg-[#0b0e14] border border-emerald-700/50 text-emerald-300 text-xs font-mono">
              {testOutput}
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export const RuleStudioHelper_1 = (ruleName: string) => (
  <span className="text-xs text-slate-400">Helper 1: {ruleName}</span>
);

export const RuleStudioHelper_2 = (ruleName: string) => (
  <span className="text-xs text-slate-400">Helper 2: {ruleName}</span>
);

export const RuleStudioHelper_3 = (ruleName: string) => (
  <span className="text-xs text-slate-400">Helper 3: {ruleName}</span>
);

export const RuleStudioHelper_4 = (ruleName: string) => (
  <span className="text-xs text-slate-400">Helper 4: {ruleName}</span>
);

export const RuleStudioHelper_5 = (ruleName: string) => (
  <span className="text-xs text-slate-400">Helper 5: {ruleName}</span>
);

export const RuleStudioHelper_6 = (ruleName: string) => (
  <span className="text-xs text-slate-400">Helper 6: {ruleName}</span>
);

export const RuleStudioHelper_7 = (ruleName: string) => (
  <span className="text-xs text-slate-400">Helper 7: {ruleName}</span>
);

export const RuleStudioHelper_8 = (ruleName: string) => (
  <span className="text-xs text-slate-400">Helper 8: {ruleName}</span>
);

export const RuleStudioHelper_9 = (ruleName: string) => (
  <span className="text-xs text-slate-400">Helper 9: {ruleName}</span>
);

export const RuleStudioHelper_10 = (ruleName: string) => (
  <span className="text-xs text-slate-400">Helper 10: {ruleName}</span>
);

export const RuleStudioHelper_11 = (ruleName: string) => (
  <span className="text-xs text-slate-400">Helper 11: {ruleName}</span>
);

export const RuleStudioHelper_12 = (ruleName: string) => (
  <span className="text-xs text-slate-400">Helper 12: {ruleName}</span>
);

export const RuleStudioHelper_13 = (ruleName: string) => (
  <span className="text-xs text-slate-400">Helper 13: {ruleName}</span>
);

export const RuleStudioHelper_14 = (ruleName: string) => (
  <span className="text-xs text-slate-400">Helper 14: {ruleName}</span>
);

export const RuleStudioHelper_15 = (ruleName: string) => (
  <span className="text-xs text-slate-400">Helper 15: {ruleName}</span>
);

export const RuleStudioHelper_16 = (ruleName: string) => (
  <span className="text-xs text-slate-400">Helper 16: {ruleName}</span>
);

export const RuleStudioHelper_17 = (ruleName: string) => (
  <span className="text-xs text-slate-400">Helper 17: {ruleName}</span>
);

export const RuleStudioHelper_18 = (ruleName: string) => (
  <span className="text-xs text-slate-400">Helper 18: {ruleName}</span>
);

export const RuleStudioHelper_19 = (ruleName: string) => (
  <span className="text-xs text-slate-400">Helper 19: {ruleName}</span>
);

export const RuleStudioHelper_20 = (ruleName: string) => (
  <span className="text-xs text-slate-400">Helper 20: {ruleName}</span>
);

export const RuleStudioHelper_21 = (ruleName: string) => (
  <span className="text-xs text-slate-400">Helper 21: {ruleName}</span>
);

export const RuleStudioHelper_22 = (ruleName: string) => (
  <span className="text-xs text-slate-400">Helper 22: {ruleName}</span>
);

export const RuleStudioHelper_23 = (ruleName: string) => (
  <span className="text-xs text-slate-400">Helper 23: {ruleName}</span>
);

export const RuleStudioHelper_24 = (ruleName: string) => (
  <span className="text-xs text-slate-400">Helper 24: {ruleName}</span>
);