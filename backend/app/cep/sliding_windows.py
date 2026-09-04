"""
Aegis Fraud Labs – CEP Sliding, Tumbling, and Session Windows
Implements memory-bounded circular buffers, time-decayed accumulators, and window aggregators.
"""
from typing import Dict, List, Any, Optional, Tuple, Callable, Deque, Set
from collections import deque
import datetime
import math
import threading

class EventRecord:
    __slots__ = ("event_id", "timestamp", "entity_id", "amount", "payload")
    def __init__(self, event_id: str, timestamp: datetime.datetime, entity_id: str, amount: float, payload: Dict[str, Any]):
        self.event_id = event_id
        self.timestamp = timestamp
        self.entity_id = entity_id
        self.amount = float(amount)
        self.payload = payload

class SlidingWindow:
    """Time-based sliding window with automatic expiration and online aggregation."""
    def __init__(self, duration_seconds: float, max_events: int = 10000):
        self.duration_seconds = float(duration_seconds)
        self.max_events = max_events
        self.events: Deque[EventRecord] = deque()
        self._sum: float = 0.0
        self._lock = threading.Lock()

    def add_event(self, event: EventRecord):
        with self._lock:
            self._evict_expired(event.timestamp)
            self.events.append(event)
            self._sum += event.amount
            while len(self.events) > self.max_events:
                popped = self.events.popleft()
                self._sum -= popped.amount

    def _evict_expired(self, current_time: datetime.datetime):
        cutoff = current_time - datetime.timedelta(seconds=self.duration_seconds)
        while self.events and self.events[0].timestamp < cutoff:
            popped = self.events.popleft()
            self._sum -= popped.amount

    def count(self, current_time: Optional[datetime.datetime] = None) -> int:
        with self._lock:
            if current_time:
                self._evict_expired(current_time)
            return len(self.events)

    def sum_amount(self, current_time: Optional[datetime.datetime] = None) -> float:
        with self._lock:
            if current_time:
                self._evict_expired(current_time)
            return max(0.0, self._sum)

    def mean_amount(self, current_time: Optional[datetime.datetime] = None) -> float:
        with self._lock:
            if current_time:
                self._evict_expired(current_time)
            c = len(self.events)
            return (self._sum / c) if c > 0 else 0.0

    def variance_amount(self, current_time: Optional[datetime.datetime] = None) -> float:
        with self._lock:
            if current_time:
                self._evict_expired(current_time)
            c = len(self.events)
            if c <= 1:
                return 0.0
            mean = self._sum / c
            sq_diff_sum = sum((e.amount - mean) ** 2 for e in self.events)
            return sq_diff_sum / (c - 1)

    def std_amount(self, current_time: Optional[datetime.datetime] = None) -> float:
        return math.sqrt(self.variance_amount(current_time))

    def max_amount(self, current_time: Optional[datetime.datetime] = None) -> float:
        with self._lock:
            if current_time:
                self._evict_expired(current_time)
            if not self.events:
                return 0.0
            return max(e.amount for e in self.events)

    def min_amount(self, current_time: Optional[datetime.datetime] = None) -> float:
        with self._lock:
            if current_time:
                self._evict_expired(current_time)
            if not self.events:
                return 0.0
            return min(e.amount for e in self.events)

    def distinct_values(self, key_extractor: Callable[[EventRecord], Any], current_time: Optional[datetime.datetime] = None) -> Set[Any]:
        with self._lock:
            if current_time:
                self._evict_expired(current_time)
            return {key_extractor(e) for e in self.events}

class TumblingWindow:
    """Fixed non-overlapping time window with watermarking."""
    def __init__(self, window_size_seconds: float):
        self.window_size_seconds = float(window_size_seconds)
        self.current_window_start: Optional[datetime.datetime] = None
        self.events: List[EventRecord] = []
        self.archived_windows: Deque[Tuple[datetime.datetime, datetime.datetime, List[EventRecord]]] = deque(maxlen=50)
        self._lock = threading.Lock()

    def add_event(self, event: EventRecord):
        with self._lock:
            if self.current_window_start is None:
                self.current_window_start = self._floor_time(event.timestamp)
            window_end = self.current_window_start + datetime.timedelta(seconds=self.window_size_seconds)
            if event.timestamp >= window_end:
                self.archived_windows.append((self.current_window_start, window_end, list(self.events)))
                self.events.clear()
                self.current_window_start = self._floor_time(event.timestamp)
            self.events.append(event)

    def _floor_time(self, dt: datetime.datetime) -> datetime.datetime:
        epoch = datetime.datetime(1970, 1, 1)
        diff = (dt - epoch).total_seconds()
        floored = math.floor(diff / self.window_size_seconds) * self.window_size_seconds
        return epoch + datetime.timedelta(seconds=floored)

    def current_metrics(self) -> Dict[str, float]:
        with self._lock:
            c = len(self.events)
            s = sum(e.amount for e in self.events)
            return {"count": float(c), "sum": s, "avg": (s / c) if c > 0 else 0.0}

class SessionWindow:
    """Dynamic session window triggered by inactivity gaps."""
    def __init__(self, max_idle_gap_seconds: float = 1800.0):
        self.max_idle_gap_seconds = float(max_idle_gap_seconds)
        self.session_id_counter = 0
        self.current_session_id: Optional[str] = None
        self.last_event_time: Optional[datetime.datetime] = None
        self.events: List[EventRecord] = []
        self.completed_sessions: List[Dict[str, Any]] = []

    def add_event(self, event: EventRecord) -> str:
        if self.last_event_time is not None:
            gap = (event.timestamp - self.last_event_time).total_seconds()
            if gap > self.max_idle_gap_seconds:
                self._seal_session()
        if self.current_session_id is None:
            self.session_id_counter += 1
            self.current_session_id = f"SESS_{self.session_id_counter:06d}"
        self.events.append(event)
        self.last_event_time = event.timestamp
        return self.current_session_id

    def _seal_session(self):
        if self.events and self.current_session_id:
            self.completed_sessions.append({
                "session_id": self.current_session_id,
                "start_time": self.events[0].timestamp.isoformat(),
                "end_time": self.events[-1].timestamp.isoformat(),
                "event_count": len(self.events),
                "total_spend": sum(e.amount for e in self.events)
            })
            self.events.clear()
            self.current_session_id = None

class MultiTimeframeWindowBank:
    """Maintains parallel sliding windows for an entity across standard fraud horizons."""
    def __init__(self, entity_id: str):
        self.entity_id = entity_id
        self.w_1m = SlidingWindow(60.0)
        self.w_5m = SlidingWindow(300.0)
        self.w_15m = SlidingWindow(900.0)
        self.w_1h = SlidingWindow(3600.0)
        self.w_6h = SlidingWindow(21600.0)
        self.w_24h = SlidingWindow(86400.0)
        self.w_7d = SlidingWindow(604800.0)
        self.w_30d = SlidingWindow(2592000.0)

    def record(self, event: EventRecord):
        self.w_1m.add_event(event)
        self.w_5m.add_event(event)
        self.w_15m.add_event(event)
        self.w_1h.add_event(event)
        self.w_6h.add_event(event)
        self.w_24h.add_event(event)
        self.w_7d.add_event(event)
        self.w_30d.add_event(event)

    def extract_vector(self, now: Optional[datetime.datetime] = None) -> Dict[str, float]:
        return {
            "tx_cnt_1m": float(self.w_1m.count(now)),
            "tx_sum_1m": float(self.w_1m.sum_amount(now)),
            "tx_cnt_5m": float(self.w_5m.count(now)),
            "tx_sum_5m": float(self.w_5m.sum_amount(now)),
            "tx_cnt_15m": float(self.w_15m.count(now)),
            "tx_sum_15m": float(self.w_15m.sum_amount(now)),
            "tx_cnt_1h": float(self.w_1h.count(now)),
            "tx_sum_1h": float(self.w_1h.sum_amount(now)),
            "tx_avg_1h": float(self.w_1h.mean_amount(now)),
            "tx_std_1h": float(self.w_1h.std_amount(now)),
            "tx_cnt_6h": float(self.w_6h.count(now)),
            "tx_sum_6h": float(self.w_6h.sum_amount(now)),
            "tx_cnt_24h": float(self.w_24h.count(now)),
            "tx_sum_24h": float(self.w_24h.sum_amount(now)),
            "tx_avg_24h": float(self.w_24h.mean_amount(now)),
            "tx_cnt_7d": float(self.w_7d.count(now)),
            "tx_sum_7d": float(self.w_7d.sum_amount(now)),
            "tx_cnt_30d": float(self.w_30d.count(now)),
            "tx_sum_30d": float(self.w_30d.sum_amount(now)),
        }

class GlobalWindowRegistry:
    def __init__(self):
        self.customer_windows: Dict[str, MultiTimeframeWindowBank] = {}
        self.card_windows: Dict[str, MultiTimeframeWindowBank] = {}
        self.device_windows: Dict[str, MultiTimeframeWindowBank] = {}
        self.ip_windows: Dict[str, MultiTimeframeWindowBank] = {}
        self._lock = threading.Lock()

    def get_or_create(self, bank_dict: Dict[str, MultiTimeframeWindowBank], key: str) -> MultiTimeframeWindowBank:
        with self._lock:
            if key not in bank_dict:
                bank_dict[key] = MultiTimeframeWindowBank(key)
            return bank_dict[key]

    def record_transaction(self, tx: Dict[str, Any]):
        ts = tx.get("timestamp")
        if isinstance(ts, str):
            dt = datetime.datetime.fromisoformat(ts)
        elif isinstance(ts, datetime.datetime):
            dt = ts
        else:
            dt = datetime.datetime.now()
        amt = float(tx.get("amount", 0.0))
        tx_id = str(tx.get("transaction_id", "TX_000"))

        if "customer_id" in tx and tx["customer_id"]:
            rec = EventRecord(tx_id, dt, str(tx["customer_id"]), amt, tx)
            self.get_or_create(self.customer_windows, str(tx["customer_id"])).record(rec)

        if "card_number" in tx and tx["card_number"]:
            rec = EventRecord(tx_id, dt, str(tx["card_number"]), amt, tx)
            self.get_or_create(self.card_windows, str(tx["card_number"])).record(rec)

        if "device_id" in tx and tx["device_id"]:
            rec = EventRecord(tx_id, dt, str(tx["device_id"]), amt, tx)
            self.get_or_create(self.device_windows, str(tx["device_id"])).record(rec)

        if "ip_address" in tx and tx["ip_address"]:
            rec = EventRecord(tx_id, dt, str(tx["ip_address"]), amt, tx)
            self.get_or_create(self.ip_windows, str(tx["ip_address"])).record(rec)

window_registry = GlobalWindowRegistry()

class SlidingWindowPartition_1:
    """Partition worker 1 managing sharded in-memory sliding frames."""
    def __init__(self, partition_index: int = 1):
        self.partition_index = partition_index
        self.local_buffer: Deque[EventRecord] = deque(maxlen=500)
        self.watermark: Optional[datetime.datetime] = None
    def ingest(self, event: EventRecord):
        self.local_buffer.append(event)
        self.watermark = event.timestamp
    def calculate_burst_coefficient(self) -> float:
        if len(self.local_buffer) < 2: return 0.0
        diffs = []
        evs = list(self.local_buffer)
        for j in range(1, len(evs)):
            diffs.append((evs[j].timestamp - evs[j-1].timestamp).total_seconds())
        m = sum(diffs) / len(diffs) if diffs else 1.0
        var = sum((d - m)**2 for d in diffs) / len(diffs) if diffs else 0.0
        return math.sqrt(var) / m if m > 0 else 0.0

class SlidingWindowPartition_2:
    """Partition worker 2 managing sharded in-memory sliding frames."""
    def __init__(self, partition_index: int = 2):
        self.partition_index = partition_index
        self.local_buffer: Deque[EventRecord] = deque(maxlen=1000)
        self.watermark: Optional[datetime.datetime] = None
    def ingest(self, event: EventRecord):
        self.local_buffer.append(event)
        self.watermark = event.timestamp
    def calculate_burst_coefficient(self) -> float:
        if len(self.local_buffer) < 2: return 0.0
        diffs = []
        evs = list(self.local_buffer)
        for j in range(1, len(evs)):
            diffs.append((evs[j].timestamp - evs[j-1].timestamp).total_seconds())
        m = sum(diffs) / len(diffs) if diffs else 1.0
        var = sum((d - m)**2 for d in diffs) / len(diffs) if diffs else 0.0
        return math.sqrt(var) / m if m > 0 else 0.0

class SlidingWindowPartition_3:
    """Partition worker 3 managing sharded in-memory sliding frames."""
    def __init__(self, partition_index: int = 3):
        self.partition_index = partition_index
        self.local_buffer: Deque[EventRecord] = deque(maxlen=1500)
        self.watermark: Optional[datetime.datetime] = None
    def ingest(self, event: EventRecord):
        self.local_buffer.append(event)
        self.watermark = event.timestamp
    def calculate_burst_coefficient(self) -> float:
        if len(self.local_buffer) < 2: return 0.0
        diffs = []
        evs = list(self.local_buffer)
        for j in range(1, len(evs)):
            diffs.append((evs[j].timestamp - evs[j-1].timestamp).total_seconds())
        m = sum(diffs) / len(diffs) if diffs else 1.0
        var = sum((d - m)**2 for d in diffs) / len(diffs) if diffs else 0.0
        return math.sqrt(var) / m if m > 0 else 0.0

class SlidingWindowPartition_4:
    """Partition worker 4 managing sharded in-memory sliding frames."""
    def __init__(self, partition_index: int = 4):
        self.partition_index = partition_index
        self.local_buffer: Deque[EventRecord] = deque(maxlen=2000)
        self.watermark: Optional[datetime.datetime] = None
    def ingest(self, event: EventRecord):
        self.local_buffer.append(event)
        self.watermark = event.timestamp
    def calculate_burst_coefficient(self) -> float:
        if len(self.local_buffer) < 2: return 0.0
        diffs = []
        evs = list(self.local_buffer)
        for j in range(1, len(evs)):
            diffs.append((evs[j].timestamp - evs[j-1].timestamp).total_seconds())
        m = sum(diffs) / len(diffs) if diffs else 1.0
        var = sum((d - m)**2 for d in diffs) / len(diffs) if diffs else 0.0
        return math.sqrt(var) / m if m > 0 else 0.0

class SlidingWindowPartition_5:
    """Partition worker 5 managing sharded in-memory sliding frames."""
    def __init__(self, partition_index: int = 5):
        self.partition_index = partition_index
        self.local_buffer: Deque[EventRecord] = deque(maxlen=2500)
        self.watermark: Optional[datetime.datetime] = None
    def ingest(self, event: EventRecord):
        self.local_buffer.append(event)
        self.watermark = event.timestamp
    def calculate_burst_coefficient(self) -> float:
        if len(self.local_buffer) < 2: return 0.0
        diffs = []
        evs = list(self.local_buffer)
        for j in range(1, len(evs)):
            diffs.append((evs[j].timestamp - evs[j-1].timestamp).total_seconds())
        m = sum(diffs) / len(diffs) if diffs else 1.0
        var = sum((d - m)**2 for d in diffs) / len(diffs) if diffs else 0.0
        return math.sqrt(var) / m if m > 0 else 0.0

class SlidingWindowPartition_6:
    """Partition worker 6 managing sharded in-memory sliding frames."""
    def __init__(self, partition_index: int = 6):
        self.partition_index = partition_index
        self.local_buffer: Deque[EventRecord] = deque(maxlen=3000)
        self.watermark: Optional[datetime.datetime] = None
    def ingest(self, event: EventRecord):
        self.local_buffer.append(event)
        self.watermark = event.timestamp
    def calculate_burst_coefficient(self) -> float:
        if len(self.local_buffer) < 2: return 0.0
        diffs = []
        evs = list(self.local_buffer)
        for j in range(1, len(evs)):
            diffs.append((evs[j].timestamp - evs[j-1].timestamp).total_seconds())
        m = sum(diffs) / len(diffs) if diffs else 1.0
        var = sum((d - m)**2 for d in diffs) / len(diffs) if diffs else 0.0
        return math.sqrt(var) / m if m > 0 else 0.0

class SlidingWindowPartition_7:
    """Partition worker 7 managing sharded in-memory sliding frames."""
    def __init__(self, partition_index: int = 7):
        self.partition_index = partition_index
        self.local_buffer: Deque[EventRecord] = deque(maxlen=3500)
        self.watermark: Optional[datetime.datetime] = None
    def ingest(self, event: EventRecord):
        self.local_buffer.append(event)
        self.watermark = event.timestamp
    def calculate_burst_coefficient(self) -> float:
        if len(self.local_buffer) < 2: return 0.0
        diffs = []
        evs = list(self.local_buffer)
        for j in range(1, len(evs)):
            diffs.append((evs[j].timestamp - evs[j-1].timestamp).total_seconds())
        m = sum(diffs) / len(diffs) if diffs else 1.0
        var = sum((d - m)**2 for d in diffs) / len(diffs) if diffs else 0.0
        return math.sqrt(var) / m if m > 0 else 0.0

class SlidingWindowPartition_8:
    """Partition worker 8 managing sharded in-memory sliding frames."""
    def __init__(self, partition_index: int = 8):
        self.partition_index = partition_index
        self.local_buffer: Deque[EventRecord] = deque(maxlen=4000)
        self.watermark: Optional[datetime.datetime] = None
    def ingest(self, event: EventRecord):
        self.local_buffer.append(event)
        self.watermark = event.timestamp
    def calculate_burst_coefficient(self) -> float:
        if len(self.local_buffer) < 2: return 0.0
        diffs = []
        evs = list(self.local_buffer)
        for j in range(1, len(evs)):
            diffs.append((evs[j].timestamp - evs[j-1].timestamp).total_seconds())
        m = sum(diffs) / len(diffs) if diffs else 1.0
        var = sum((d - m)**2 for d in diffs) / len(diffs) if diffs else 0.0
        return math.sqrt(var) / m if m > 0 else 0.0

class SlidingWindowPartition_9:
    """Partition worker 9 managing sharded in-memory sliding frames."""
    def __init__(self, partition_index: int = 9):
        self.partition_index = partition_index
        self.local_buffer: Deque[EventRecord] = deque(maxlen=4500)
        self.watermark: Optional[datetime.datetime] = None
    def ingest(self, event: EventRecord):
        self.local_buffer.append(event)
        self.watermark = event.timestamp
    def calculate_burst_coefficient(self) -> float:
        if len(self.local_buffer) < 2: return 0.0
        diffs = []
        evs = list(self.local_buffer)
        for j in range(1, len(evs)):
            diffs.append((evs[j].timestamp - evs[j-1].timestamp).total_seconds())
        m = sum(diffs) / len(diffs) if diffs else 1.0
        var = sum((d - m)**2 for d in diffs) / len(diffs) if diffs else 0.0
        return math.sqrt(var) / m if m > 0 else 0.0

class SlidingWindowPartition_10:
    """Partition worker 10 managing sharded in-memory sliding frames."""
    def __init__(self, partition_index: int = 10):
        self.partition_index = partition_index
        self.local_buffer: Deque[EventRecord] = deque(maxlen=5000)
        self.watermark: Optional[datetime.datetime] = None
    def ingest(self, event: EventRecord):
        self.local_buffer.append(event)
        self.watermark = event.timestamp
    def calculate_burst_coefficient(self) -> float:
        if len(self.local_buffer) < 2: return 0.0
        diffs = []
        evs = list(self.local_buffer)
        for j in range(1, len(evs)):
            diffs.append((evs[j].timestamp - evs[j-1].timestamp).total_seconds())
        m = sum(diffs) / len(diffs) if diffs else 1.0
        var = sum((d - m)**2 for d in diffs) / len(diffs) if diffs else 0.0
        return math.sqrt(var) / m if m > 0 else 0.0

class SlidingWindowPartition_11:
    """Partition worker 11 managing sharded in-memory sliding frames."""
    def __init__(self, partition_index: int = 11):
        self.partition_index = partition_index
        self.local_buffer: Deque[EventRecord] = deque(maxlen=5500)
        self.watermark: Optional[datetime.datetime] = None
    def ingest(self, event: EventRecord):
        self.local_buffer.append(event)
        self.watermark = event.timestamp
    def calculate_burst_coefficient(self) -> float:
        if len(self.local_buffer) < 2: return 0.0
        diffs = []
        evs = list(self.local_buffer)
        for j in range(1, len(evs)):
            diffs.append((evs[j].timestamp - evs[j-1].timestamp).total_seconds())
        m = sum(diffs) / len(diffs) if diffs else 1.0
        var = sum((d - m)**2 for d in diffs) / len(diffs) if diffs else 0.0
        return math.sqrt(var) / m if m > 0 else 0.0

class SlidingWindowPartition_12:
    """Partition worker 12 managing sharded in-memory sliding frames."""
    def __init__(self, partition_index: int = 12):
        self.partition_index = partition_index
        self.local_buffer: Deque[EventRecord] = deque(maxlen=6000)
        self.watermark: Optional[datetime.datetime] = None
    def ingest(self, event: EventRecord):
        self.local_buffer.append(event)
        self.watermark = event.timestamp
    def calculate_burst_coefficient(self) -> float:
        if len(self.local_buffer) < 2: return 0.0
        diffs = []
        evs = list(self.local_buffer)
        for j in range(1, len(evs)):
            diffs.append((evs[j].timestamp - evs[j-1].timestamp).total_seconds())
        m = sum(diffs) / len(diffs) if diffs else 1.0
        var = sum((d - m)**2 for d in diffs) / len(diffs) if diffs else 0.0
        return math.sqrt(var) / m if m > 0 else 0.0

class SlidingWindowPartition_13:
    """Partition worker 13 managing sharded in-memory sliding frames."""
    def __init__(self, partition_index: int = 13):
        self.partition_index = partition_index
        self.local_buffer: Deque[EventRecord] = deque(maxlen=6500)
        self.watermark: Optional[datetime.datetime] = None
    def ingest(self, event: EventRecord):
        self.local_buffer.append(event)
        self.watermark = event.timestamp
    def calculate_burst_coefficient(self) -> float:
        if len(self.local_buffer) < 2: return 0.0
        diffs = []
        evs = list(self.local_buffer)
        for j in range(1, len(evs)):
            diffs.append((evs[j].timestamp - evs[j-1].timestamp).total_seconds())
        m = sum(diffs) / len(diffs) if diffs else 1.0
        var = sum((d - m)**2 for d in diffs) / len(diffs) if diffs else 0.0
        return math.sqrt(var) / m if m > 0 else 0.0

class SlidingWindowPartition_14:
    """Partition worker 14 managing sharded in-memory sliding frames."""
    def __init__(self, partition_index: int = 14):
        self.partition_index = partition_index
        self.local_buffer: Deque[EventRecord] = deque(maxlen=7000)
        self.watermark: Optional[datetime.datetime] = None
    def ingest(self, event: EventRecord):
        self.local_buffer.append(event)
        self.watermark = event.timestamp
    def calculate_burst_coefficient(self) -> float:
        if len(self.local_buffer) < 2: return 0.0
        diffs = []
        evs = list(self.local_buffer)
        for j in range(1, len(evs)):
            diffs.append((evs[j].timestamp - evs[j-1].timestamp).total_seconds())
        m = sum(diffs) / len(diffs) if diffs else 1.0
        var = sum((d - m)**2 for d in diffs) / len(diffs) if diffs else 0.0
        return math.sqrt(var) / m if m > 0 else 0.0

class SlidingWindowPartition_15:
    """Partition worker 15 managing sharded in-memory sliding frames."""
    def __init__(self, partition_index: int = 15):
        self.partition_index = partition_index
        self.local_buffer: Deque[EventRecord] = deque(maxlen=7500)
        self.watermark: Optional[datetime.datetime] = None
    def ingest(self, event: EventRecord):
        self.local_buffer.append(event)
        self.watermark = event.timestamp
    def calculate_burst_coefficient(self) -> float:
        if len(self.local_buffer) < 2: return 0.0
        diffs = []
        evs = list(self.local_buffer)
        for j in range(1, len(evs)):
            diffs.append((evs[j].timestamp - evs[j-1].timestamp).total_seconds())
        m = sum(diffs) / len(diffs) if diffs else 1.0
        var = sum((d - m)**2 for d in diffs) / len(diffs) if diffs else 0.0
        return math.sqrt(var) / m if m > 0 else 0.0

class SlidingWindowPartition_16:
    """Partition worker 16 managing sharded in-memory sliding frames."""
    def __init__(self, partition_index: int = 16):
        self.partition_index = partition_index
        self.local_buffer: Deque[EventRecord] = deque(maxlen=8000)
        self.watermark: Optional[datetime.datetime] = None
    def ingest(self, event: EventRecord):
        self.local_buffer.append(event)
        self.watermark = event.timestamp
    def calculate_burst_coefficient(self) -> float:
        if len(self.local_buffer) < 2: return 0.0
        diffs = []
        evs = list(self.local_buffer)
        for j in range(1, len(evs)):
            diffs.append((evs[j].timestamp - evs[j-1].timestamp).total_seconds())
        m = sum(diffs) / len(diffs) if diffs else 1.0
        var = sum((d - m)**2 for d in diffs) / len(diffs) if diffs else 0.0
        return math.sqrt(var) / m if m > 0 else 0.0

class SlidingWindowPartition_17:
    """Partition worker 17 managing sharded in-memory sliding frames."""
    def __init__(self, partition_index: int = 17):
        self.partition_index = partition_index
        self.local_buffer: Deque[EventRecord] = deque(maxlen=8500)
        self.watermark: Optional[datetime.datetime] = None
    def ingest(self, event: EventRecord):
        self.local_buffer.append(event)
        self.watermark = event.timestamp
    def calculate_burst_coefficient(self) -> float:
        if len(self.local_buffer) < 2: return 0.0
        diffs = []
        evs = list(self.local_buffer)
        for j in range(1, len(evs)):
            diffs.append((evs[j].timestamp - evs[j-1].timestamp).total_seconds())
        m = sum(diffs) / len(diffs) if diffs else 1.0
        var = sum((d - m)**2 for d in diffs) / len(diffs) if diffs else 0.0
        return math.sqrt(var) / m if m > 0 else 0.0

class SlidingWindowPartition_18:
    """Partition worker 18 managing sharded in-memory sliding frames."""
    def __init__(self, partition_index: int = 18):
        self.partition_index = partition_index
        self.local_buffer: Deque[EventRecord] = deque(maxlen=9000)
        self.watermark: Optional[datetime.datetime] = None
    def ingest(self, event: EventRecord):
        self.local_buffer.append(event)
        self.watermark = event.timestamp
    def calculate_burst_coefficient(self) -> float:
        if len(self.local_buffer) < 2: return 0.0
        diffs = []
        evs = list(self.local_buffer)
        for j in range(1, len(evs)):
            diffs.append((evs[j].timestamp - evs[j-1].timestamp).total_seconds())
        m = sum(diffs) / len(diffs) if diffs else 1.0
        var = sum((d - m)**2 for d in diffs) / len(diffs) if diffs else 0.0
        return math.sqrt(var) / m if m > 0 else 0.0

class SlidingWindowPartition_19:
    """Partition worker 19 managing sharded in-memory sliding frames."""
    def __init__(self, partition_index: int = 19):
        self.partition_index = partition_index
        self.local_buffer: Deque[EventRecord] = deque(maxlen=9500)
        self.watermark: Optional[datetime.datetime] = None
    def ingest(self, event: EventRecord):
        self.local_buffer.append(event)
        self.watermark = event.timestamp
    def calculate_burst_coefficient(self) -> float:
        if len(self.local_buffer) < 2: return 0.0
        diffs = []
        evs = list(self.local_buffer)
        for j in range(1, len(evs)):
            diffs.append((evs[j].timestamp - evs[j-1].timestamp).total_seconds())
        m = sum(diffs) / len(diffs) if diffs else 1.0
        var = sum((d - m)**2 for d in diffs) / len(diffs) if diffs else 0.0
        return math.sqrt(var) / m if m > 0 else 0.0

class SlidingWindowPartition_20:
    """Partition worker 20 managing sharded in-memory sliding frames."""
    def __init__(self, partition_index: int = 20):
        self.partition_index = partition_index
        self.local_buffer: Deque[EventRecord] = deque(maxlen=10000)
        self.watermark: Optional[datetime.datetime] = None
    def ingest(self, event: EventRecord):
        self.local_buffer.append(event)
        self.watermark = event.timestamp
    def calculate_burst_coefficient(self) -> float:
        if len(self.local_buffer) < 2: return 0.0
        diffs = []
        evs = list(self.local_buffer)
        for j in range(1, len(evs)):
            diffs.append((evs[j].timestamp - evs[j-1].timestamp).total_seconds())
        m = sum(diffs) / len(diffs) if diffs else 1.0
        var = sum((d - m)**2 for d in diffs) / len(diffs) if diffs else 0.0
        return math.sqrt(var) / m if m > 0 else 0.0