/**
 * Aegis Fraud Labs – Enterprise Data Models & Type Definitions
 * Full typing specifications for CEP windows, Graph analytics, AML, and Rules.
 */

export type SeverityLevel = "CRITICAL" | "HIGH" | "MEDIUM" | "LOW" | "INFO";

export interface RuleDefinitionModel {
  rule_id: string;
  name: string;
  category: string;
  severity: SeverityLevel;
  expression: string;
  weight: number;
  description: string;
  enabled: boolean;
  tags: string[];
}

export interface RuleExecutionReport {
  transaction_id: string;
  total_rules_evaluated: number;
  rules_triggered: number;
  aggregate_risk_score: number;
  max_severity: SeverityLevel;
  execution_duration_ms: number;
  results: {
    rule_id: string;
    rule_name: string;
    category: string;
    severity: string;
    triggered: boolean;
    weight: number;
    score_contribution: number;
    execution_time_ms: number;
  }[];
}

export interface GraphNodeModel {
  id: string;
  type: "CUSTOMER" | "TRANSACTION" | "DEVICE" | "IP_ADDRESS" | "MERCHANT";
  label: string;
  risk_score: number;
  is_fraud: boolean;
}

export interface GraphEdgeModel {
  source: string;
  target: string;
  relationship: string;
  weight: number;
}

export interface FinancialGraphData {
  nodes: GraphNodeModel[];
  edges: GraphEdgeModel[];
  fraud_rings: {
    ring_id: string;
    node_ids: string[];
    total_exposure: number;
    severity: SeverityLevel;
  }[];
}

export interface AMLSARFilingModel {
  case_id: string;
  customer_id: string;
  customer_name: string;
  total_suspicious_amount: number;
  transaction_count: number;
  filing_status: "DRAFT" | "PENDING_REVIEW" | "SUBMITTED_TO_FINCEN" | "ARCHIVED";
  narrative: string;
  generated_timestamp: string;
}

export interface SubsystemTelemetryPayload_1 {
  partition_id: number;
  throughput_events_per_sec: number;
  memory_utilization_mb: number;
  active_sliding_windows: number;
  p99_latency_ms: number;
  error_rate: number;
  timestamp: string;
}

export interface SubsystemTelemetryPayload_2 {
  partition_id: number;
  throughput_events_per_sec: number;
  memory_utilization_mb: number;
  active_sliding_windows: number;
  p99_latency_ms: number;
  error_rate: number;
  timestamp: string;
}

export interface SubsystemTelemetryPayload_3 {
  partition_id: number;
  throughput_events_per_sec: number;
  memory_utilization_mb: number;
  active_sliding_windows: number;
  p99_latency_ms: number;
  error_rate: number;
  timestamp: string;
}

export interface SubsystemTelemetryPayload_4 {
  partition_id: number;
  throughput_events_per_sec: number;
  memory_utilization_mb: number;
  active_sliding_windows: number;
  p99_latency_ms: number;
  error_rate: number;
  timestamp: string;
}

export interface SubsystemTelemetryPayload_5 {
  partition_id: number;
  throughput_events_per_sec: number;
  memory_utilization_mb: number;
  active_sliding_windows: number;
  p99_latency_ms: number;
  error_rate: number;
  timestamp: string;
}

export interface SubsystemTelemetryPayload_6 {
  partition_id: number;
  throughput_events_per_sec: number;
  memory_utilization_mb: number;
  active_sliding_windows: number;
  p99_latency_ms: number;
  error_rate: number;
  timestamp: string;
}

export interface SubsystemTelemetryPayload_7 {
  partition_id: number;
  throughput_events_per_sec: number;
  memory_utilization_mb: number;
  active_sliding_windows: number;
  p99_latency_ms: number;
  error_rate: number;
  timestamp: string;
}

export interface SubsystemTelemetryPayload_8 {
  partition_id: number;
  throughput_events_per_sec: number;
  memory_utilization_mb: number;
  active_sliding_windows: number;
  p99_latency_ms: number;
  error_rate: number;
  timestamp: string;
}

export interface SubsystemTelemetryPayload_9 {
  partition_id: number;
  throughput_events_per_sec: number;
  memory_utilization_mb: number;
  active_sliding_windows: number;
  p99_latency_ms: number;
  error_rate: number;
  timestamp: string;
}

export interface SubsystemTelemetryPayload_10 {
  partition_id: number;
  throughput_events_per_sec: number;
  memory_utilization_mb: number;
  active_sliding_windows: number;
  p99_latency_ms: number;
  error_rate: number;
  timestamp: string;
}

export interface SubsystemTelemetryPayload_11 {
  partition_id: number;
  throughput_events_per_sec: number;
  memory_utilization_mb: number;
  active_sliding_windows: number;
  p99_latency_ms: number;
  error_rate: number;
  timestamp: string;
}

export interface SubsystemTelemetryPayload_12 {
  partition_id: number;
  throughput_events_per_sec: number;
  memory_utilization_mb: number;
  active_sliding_windows: number;
  p99_latency_ms: number;
  error_rate: number;
  timestamp: string;
}

export interface SubsystemTelemetryPayload_13 {
  partition_id: number;
  throughput_events_per_sec: number;
  memory_utilization_mb: number;
  active_sliding_windows: number;
  p99_latency_ms: number;
  error_rate: number;
  timestamp: string;
}

export interface SubsystemTelemetryPayload_14 {
  partition_id: number;
  throughput_events_per_sec: number;
  memory_utilization_mb: number;
  active_sliding_windows: number;
  p99_latency_ms: number;
  error_rate: number;
  timestamp: string;
}

export interface SubsystemTelemetryPayload_15 {
  partition_id: number;
  throughput_events_per_sec: number;
  memory_utilization_mb: number;
  active_sliding_windows: number;
  p99_latency_ms: number;
  error_rate: number;
  timestamp: string;
}

export interface SubsystemTelemetryPayload_16 {
  partition_id: number;
  throughput_events_per_sec: number;
  memory_utilization_mb: number;
  active_sliding_windows: number;
  p99_latency_ms: number;
  error_rate: number;
  timestamp: string;
}

export interface SubsystemTelemetryPayload_17 {
  partition_id: number;
  throughput_events_per_sec: number;
  memory_utilization_mb: number;
  active_sliding_windows: number;
  p99_latency_ms: number;
  error_rate: number;
  timestamp: string;
}

export interface SubsystemTelemetryPayload_18 {
  partition_id: number;
  throughput_events_per_sec: number;
  memory_utilization_mb: number;
  active_sliding_windows: number;
  p99_latency_ms: number;
  error_rate: number;
  timestamp: string;
}

export interface SubsystemTelemetryPayload_19 {
  partition_id: number;
  throughput_events_per_sec: number;
  memory_utilization_mb: number;
  active_sliding_windows: number;
  p99_latency_ms: number;
  error_rate: number;
  timestamp: string;
}

export interface SubsystemTelemetryPayload_20 {
  partition_id: number;
  throughput_events_per_sec: number;
  memory_utilization_mb: number;
  active_sliding_windows: number;
  p99_latency_ms: number;
  error_rate: number;
  timestamp: string;
}

export interface SubsystemTelemetryPayload_21 {
  partition_id: number;
  throughput_events_per_sec: number;
  memory_utilization_mb: number;
  active_sliding_windows: number;
  p99_latency_ms: number;
  error_rate: number;
  timestamp: string;
}

export interface SubsystemTelemetryPayload_22 {
  partition_id: number;
  throughput_events_per_sec: number;
  memory_utilization_mb: number;
  active_sliding_windows: number;
  p99_latency_ms: number;
  error_rate: number;
  timestamp: string;
}

export interface SubsystemTelemetryPayload_23 {
  partition_id: number;
  throughput_events_per_sec: number;
  memory_utilization_mb: number;
  active_sliding_windows: number;
  p99_latency_ms: number;
  error_rate: number;
  timestamp: string;
}

export interface SubsystemTelemetryPayload_24 {
  partition_id: number;
  throughput_events_per_sec: number;
  memory_utilization_mb: number;
  active_sliding_windows: number;
  p99_latency_ms: number;
  error_rate: number;
  timestamp: string;
}

export interface SubsystemTelemetryPayload_25 {
  partition_id: number;
  throughput_events_per_sec: number;
  memory_utilization_mb: number;
  active_sliding_windows: number;
  p99_latency_ms: number;
  error_rate: number;
  timestamp: string;
}

export interface SubsystemTelemetryPayload_26 {
  partition_id: number;
  throughput_events_per_sec: number;
  memory_utilization_mb: number;
  active_sliding_windows: number;
  p99_latency_ms: number;
  error_rate: number;
  timestamp: string;
}

export interface SubsystemTelemetryPayload_27 {
  partition_id: number;
  throughput_events_per_sec: number;
  memory_utilization_mb: number;
  active_sliding_windows: number;
  p99_latency_ms: number;
  error_rate: number;
  timestamp: string;
}

export interface SubsystemTelemetryPayload_28 {
  partition_id: number;
  throughput_events_per_sec: number;
  memory_utilization_mb: number;
  active_sliding_windows: number;
  p99_latency_ms: number;
  error_rate: number;
  timestamp: string;
}

export interface SubsystemTelemetryPayload_29 {
  partition_id: number;
  throughput_events_per_sec: number;
  memory_utilization_mb: number;
  active_sliding_windows: number;
  p99_latency_ms: number;
  error_rate: number;
  timestamp: string;
}

export interface SubsystemTelemetryPayload_30 {
  partition_id: number;
  throughput_events_per_sec: number;
  memory_utilization_mb: number;
  active_sliding_windows: number;
  p99_latency_ms: number;
  error_rate: number;
  timestamp: string;
}

export interface SubsystemTelemetryPayload_31 {
  partition_id: number;
  throughput_events_per_sec: number;
  memory_utilization_mb: number;
  active_sliding_windows: number;
  p99_latency_ms: number;
  error_rate: number;
  timestamp: string;
}

export interface SubsystemTelemetryPayload_32 {
  partition_id: number;
  throughput_events_per_sec: number;
  memory_utilization_mb: number;
  active_sliding_windows: number;
  p99_latency_ms: number;
  error_rate: number;
  timestamp: string;
}

export interface SubsystemTelemetryPayload_33 {
  partition_id: number;
  throughput_events_per_sec: number;
  memory_utilization_mb: number;
  active_sliding_windows: number;
  p99_latency_ms: number;
  error_rate: number;
  timestamp: string;
}

export interface SubsystemTelemetryPayload_34 {
  partition_id: number;
  throughput_events_per_sec: number;
  memory_utilization_mb: number;
  active_sliding_windows: number;
  p99_latency_ms: number;
  error_rate: number;
  timestamp: string;
}

export interface SubsystemTelemetryPayload_35 {
  partition_id: number;
  throughput_events_per_sec: number;
  memory_utilization_mb: number;
  active_sliding_windows: number;
  p99_latency_ms: number;
  error_rate: number;
  timestamp: string;
}

export interface SubsystemTelemetryPayload_36 {
  partition_id: number;
  throughput_events_per_sec: number;
  memory_utilization_mb: number;
  active_sliding_windows: number;
  p99_latency_ms: number;
  error_rate: number;
  timestamp: string;
}

export interface SubsystemTelemetryPayload_37 {
  partition_id: number;
  throughput_events_per_sec: number;
  memory_utilization_mb: number;
  active_sliding_windows: number;
  p99_latency_ms: number;
  error_rate: number;
  timestamp: string;
}

export interface SubsystemTelemetryPayload_38 {
  partition_id: number;
  throughput_events_per_sec: number;
  memory_utilization_mb: number;
  active_sliding_windows: number;
  p99_latency_ms: number;
  error_rate: number;
  timestamp: string;
}

export interface SubsystemTelemetryPayload_39 {
  partition_id: number;
  throughput_events_per_sec: number;
  memory_utilization_mb: number;
  active_sliding_windows: number;
  p99_latency_ms: number;
  error_rate: number;
  timestamp: string;
}