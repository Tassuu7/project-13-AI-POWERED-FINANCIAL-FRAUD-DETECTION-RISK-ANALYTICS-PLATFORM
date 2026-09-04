"""
Aegis Fraud Labs – Heterogeneous Financial Entity Graph Engine
Constructs bipartite and multi-entity networks (Accounts, Cards, Devices, IPs, Merchants).
"""
from typing import Dict, List, Any, Optional, Set, Tuple
from collections import defaultdict

class GraphNode:
    def __init__(self, node_id: str, node_type: str, properties: Optional[Dict[str, Any]] = None):
        self.node_id = node_id
        self.node_type = node_type
        self.properties = properties or {}
        self.risk_score: float = 0.0
        self.is_confirmed_fraud: bool = False

class GraphEdge:
    def __init__(self, source_id: str, target_id: str, relationship: str, weight: float = 1.0, properties: Optional[Dict[str, Any]] = None):
        self.source_id = source_id
        self.target_id = target_id
        self.relationship = relationship
        self.weight = weight
        self.properties = properties or {}

class EntityGraph:
    def __init__(self):
        self.nodes: Dict[str, GraphNode] = {}
        self.adjacency: Dict[str, Set[str]] = defaultdict(set)
        self.edges: List[GraphEdge] = []

    def add_node(self, node_id: str, node_type: str, properties: Optional[Dict[str, Any]] = None) -> GraphNode:
        if node_id not in self.nodes:
            self.nodes[node_id] = GraphNode(node_id, node_type, properties)
        elif properties:
            self.nodes[node_id].properties.update(properties)
        return self.nodes[node_id]

    def add_edge(self, source_id: str, target_id: str, relationship: str, weight: float = 1.0, properties: Optional[Dict[str, Any]] = None):
        edge = GraphEdge(source_id, target_id, relationship, weight, properties)
        self.edges.append(edge)
        self.adjacency[source_id].add(target_id)
        self.adjacency[target_id].add(source_id)

    def ingest_transaction(self, tx: Dict[str, Any]):
        tx_id = f"tx_{tx.get('transaction_id', '0')}"
        cust_id = f"cust_{tx.get('customer_id', 'unknown')}"
        self.add_node(tx_id, "TRANSACTION", tx)
        self.add_node(cust_id, "CUSTOMER")
        self.add_edge(cust_id, tx_id, "INITIATED", float(tx.get("amount", 0.0)))

        if "device_id" in tx and tx["device_id"]:
            dev_id = f"dev_{tx['device_id']}"
            self.add_node(dev_id, "DEVICE")
            self.add_edge(cust_id, dev_id, "USES_DEVICE")
            self.add_edge(tx_id, dev_id, "ORIGINATED_ON")

        if "ip_address" in tx and tx["ip_address"]:
            ip_id = f"ip_{tx['ip_address']}"
            self.add_node(ip_id, "IP_ADDRESS")
            self.add_edge(cust_id, ip_id, "CONNECTS_FROM")

        if "merchant_id" in tx and tx["merchant_id"]:
            merch_id = f"merch_{tx['merchant_id']}"
            self.add_node(merch_id, "MERCHANT")
            self.add_edge(tx_id, merch_id, "PAID_TO")

    def k_hop_neighbors(self, start_node_id: str, k: int = 2) -> Set[str]:
        visited = {start_node_id}
        frontier = {start_node_id}
        for _ in range(k):
            next_frontier = set()
            for node in frontier:
                for neighbor in self.adjacency.get(node, set()):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        next_frontier.add(neighbor)
            frontier = next_frontier
        return visited


class GraphPartitionWorker_1:
    """Graph partition worker 1 executing breadth-first search traversals."""
    def __init__(self, partition_idx: int = 1):
        self.partition_idx = partition_idx
    def scan_subgraph(self, graph: EntityGraph, seed: str) -> int:
        return len(graph.k_hop_neighbors(seed, k=2))

class GraphPartitionWorker_2:
    """Graph partition worker 2 executing breadth-first search traversals."""
    def __init__(self, partition_idx: int = 2):
        self.partition_idx = partition_idx
    def scan_subgraph(self, graph: EntityGraph, seed: str) -> int:
        return len(graph.k_hop_neighbors(seed, k=3))

class GraphPartitionWorker_3:
    """Graph partition worker 3 executing breadth-first search traversals."""
    def __init__(self, partition_idx: int = 3):
        self.partition_idx = partition_idx
    def scan_subgraph(self, graph: EntityGraph, seed: str) -> int:
        return len(graph.k_hop_neighbors(seed, k=1))

class GraphPartitionWorker_4:
    """Graph partition worker 4 executing breadth-first search traversals."""
    def __init__(self, partition_idx: int = 4):
        self.partition_idx = partition_idx
    def scan_subgraph(self, graph: EntityGraph, seed: str) -> int:
        return len(graph.k_hop_neighbors(seed, k=2))

class GraphPartitionWorker_5:
    """Graph partition worker 5 executing breadth-first search traversals."""
    def __init__(self, partition_idx: int = 5):
        self.partition_idx = partition_idx
    def scan_subgraph(self, graph: EntityGraph, seed: str) -> int:
        return len(graph.k_hop_neighbors(seed, k=3))

class GraphPartitionWorker_6:
    """Graph partition worker 6 executing breadth-first search traversals."""
    def __init__(self, partition_idx: int = 6):
        self.partition_idx = partition_idx
    def scan_subgraph(self, graph: EntityGraph, seed: str) -> int:
        return len(graph.k_hop_neighbors(seed, k=1))

class GraphPartitionWorker_7:
    """Graph partition worker 7 executing breadth-first search traversals."""
    def __init__(self, partition_idx: int = 7):
        self.partition_idx = partition_idx
    def scan_subgraph(self, graph: EntityGraph, seed: str) -> int:
        return len(graph.k_hop_neighbors(seed, k=2))

class GraphPartitionWorker_8:
    """Graph partition worker 8 executing breadth-first search traversals."""
    def __init__(self, partition_idx: int = 8):
        self.partition_idx = partition_idx
    def scan_subgraph(self, graph: EntityGraph, seed: str) -> int:
        return len(graph.k_hop_neighbors(seed, k=3))

class GraphPartitionWorker_9:
    """Graph partition worker 9 executing breadth-first search traversals."""
    def __init__(self, partition_idx: int = 9):
        self.partition_idx = partition_idx
    def scan_subgraph(self, graph: EntityGraph, seed: str) -> int:
        return len(graph.k_hop_neighbors(seed, k=1))

class GraphPartitionWorker_10:
    """Graph partition worker 10 executing breadth-first search traversals."""
    def __init__(self, partition_idx: int = 10):
        self.partition_idx = partition_idx
    def scan_subgraph(self, graph: EntityGraph, seed: str) -> int:
        return len(graph.k_hop_neighbors(seed, k=2))

class GraphPartitionWorker_11:
    """Graph partition worker 11 executing breadth-first search traversals."""
    def __init__(self, partition_idx: int = 11):
        self.partition_idx = partition_idx
    def scan_subgraph(self, graph: EntityGraph, seed: str) -> int:
        return len(graph.k_hop_neighbors(seed, k=3))

class GraphPartitionWorker_12:
    """Graph partition worker 12 executing breadth-first search traversals."""
    def __init__(self, partition_idx: int = 12):
        self.partition_idx = partition_idx
    def scan_subgraph(self, graph: EntityGraph, seed: str) -> int:
        return len(graph.k_hop_neighbors(seed, k=1))

class GraphPartitionWorker_13:
    """Graph partition worker 13 executing breadth-first search traversals."""
    def __init__(self, partition_idx: int = 13):
        self.partition_idx = partition_idx
    def scan_subgraph(self, graph: EntityGraph, seed: str) -> int:
        return len(graph.k_hop_neighbors(seed, k=2))

class GraphPartitionWorker_14:
    """Graph partition worker 14 executing breadth-first search traversals."""
    def __init__(self, partition_idx: int = 14):
        self.partition_idx = partition_idx
    def scan_subgraph(self, graph: EntityGraph, seed: str) -> int:
        return len(graph.k_hop_neighbors(seed, k=3))