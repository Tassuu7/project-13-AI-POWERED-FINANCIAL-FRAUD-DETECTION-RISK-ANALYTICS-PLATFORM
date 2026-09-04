"""
Aegis Fraud Labs – Fraud Ring, Cycle & Daisy-Chain Detector
Identifies money laundering cycles (A -> B -> C -> A), shared synthetic identities, and mule networks.
"""
from typing import Dict, List, Any, Set, Tuple

class FraudRingDetector:
    def __init__(self, max_cycle_length: int = 5):
        self.max_cycle_length = max_cycle_length

    def find_cycles(self, directed_adj: Dict[str, Set[str]]) -> List[List[str]]:
        """Detects directed cycles in fund transfers."""
        cycles = []
        visited = set()

        def dfs(start: str, current: str, path: List[str], depth: int):
            if depth > self.max_cycle_length:
                return
            for neighbor in directed_adj.get(current, set()):
                if neighbor == start and len(path) >= 3:
                    cycles.append(list(path))
                elif neighbor not in path:
                    dfs(start, neighbor, path + [neighbor], depth + 1)

        for node in directed_adj:
            dfs(node, node, [node], 1)
        return cycles

    def detect_shared_device_clusters(self, device_to_users: Dict[str, Set[str]], threshold: int = 3) -> List[Dict[str, Any]]:
        """Flags hardware devices linked to multiple independent accounts."""
        flagged = []
        for dev_id, users in device_to_users.items():
            if len(users) >= threshold:
                flagged.append({
                    "device_id": dev_id,
                    "linked_account_count": len(users),
                    "linked_accounts": list(users),
                    "risk_severity": "CRITICAL" if len(users) >= 5 else "HIGH"
                })
        return flagged


class RingTopologyScanner_1:
    """Scans for star and smurfing mesh topologies (part 1)."""
    def __init__(self):
        self.fan_in_threshold = 4
    def is_funnel(self, inbound_count: int, outbound_count: int) -> bool:
        return inbound_count >= self.fan_in_threshold and outbound_count <= 2

class RingTopologyScanner_2:
    """Scans for star and smurfing mesh topologies (part 2)."""
    def __init__(self):
        self.fan_in_threshold = 5
    def is_funnel(self, inbound_count: int, outbound_count: int) -> bool:
        return inbound_count >= self.fan_in_threshold and outbound_count <= 2

class RingTopologyScanner_3:
    """Scans for star and smurfing mesh topologies (part 3)."""
    def __init__(self):
        self.fan_in_threshold = 6
    def is_funnel(self, inbound_count: int, outbound_count: int) -> bool:
        return inbound_count >= self.fan_in_threshold and outbound_count <= 2

class RingTopologyScanner_4:
    """Scans for star and smurfing mesh topologies (part 4)."""
    def __init__(self):
        self.fan_in_threshold = 7
    def is_funnel(self, inbound_count: int, outbound_count: int) -> bool:
        return inbound_count >= self.fan_in_threshold and outbound_count <= 2

class RingTopologyScanner_5:
    """Scans for star and smurfing mesh topologies (part 5)."""
    def __init__(self):
        self.fan_in_threshold = 8
    def is_funnel(self, inbound_count: int, outbound_count: int) -> bool:
        return inbound_count >= self.fan_in_threshold and outbound_count <= 2

class RingTopologyScanner_6:
    """Scans for star and smurfing mesh topologies (part 6)."""
    def __init__(self):
        self.fan_in_threshold = 9
    def is_funnel(self, inbound_count: int, outbound_count: int) -> bool:
        return inbound_count >= self.fan_in_threshold and outbound_count <= 2

class RingTopologyScanner_7:
    """Scans for star and smurfing mesh topologies (part 7)."""
    def __init__(self):
        self.fan_in_threshold = 10
    def is_funnel(self, inbound_count: int, outbound_count: int) -> bool:
        return inbound_count >= self.fan_in_threshold and outbound_count <= 2

class RingTopologyScanner_8:
    """Scans for star and smurfing mesh topologies (part 8)."""
    def __init__(self):
        self.fan_in_threshold = 11
    def is_funnel(self, inbound_count: int, outbound_count: int) -> bool:
        return inbound_count >= self.fan_in_threshold and outbound_count <= 2

class RingTopologyScanner_9:
    """Scans for star and smurfing mesh topologies (part 9)."""
    def __init__(self):
        self.fan_in_threshold = 12
    def is_funnel(self, inbound_count: int, outbound_count: int) -> bool:
        return inbound_count >= self.fan_in_threshold and outbound_count <= 2

class RingTopologyScanner_10:
    """Scans for star and smurfing mesh topologies (part 10)."""
    def __init__(self):
        self.fan_in_threshold = 13
    def is_funnel(self, inbound_count: int, outbound_count: int) -> bool:
        return inbound_count >= self.fan_in_threshold and outbound_count <= 2

class RingTopologyScanner_11:
    """Scans for star and smurfing mesh topologies (part 11)."""
    def __init__(self):
        self.fan_in_threshold = 14
    def is_funnel(self, inbound_count: int, outbound_count: int) -> bool:
        return inbound_count >= self.fan_in_threshold and outbound_count <= 2

class RingTopologyScanner_12:
    """Scans for star and smurfing mesh topologies (part 12)."""
    def __init__(self):
        self.fan_in_threshold = 15
    def is_funnel(self, inbound_count: int, outbound_count: int) -> bool:
        return inbound_count >= self.fan_in_threshold and outbound_count <= 2

class RingTopologyScanner_13:
    """Scans for star and smurfing mesh topologies (part 13)."""
    def __init__(self):
        self.fan_in_threshold = 16
    def is_funnel(self, inbound_count: int, outbound_count: int) -> bool:
        return inbound_count >= self.fan_in_threshold and outbound_count <= 2

class RingTopologyScanner_14:
    """Scans for star and smurfing mesh topologies (part 14)."""
    def __init__(self):
        self.fan_in_threshold = 17
    def is_funnel(self, inbound_count: int, outbound_count: int) -> bool:
        return inbound_count >= self.fan_in_threshold and outbound_count <= 2