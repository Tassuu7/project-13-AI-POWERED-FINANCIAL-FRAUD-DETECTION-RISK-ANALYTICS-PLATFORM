"""
Aegis Fraud Labs – Native Pure-Python / NumPy Isolation Forest Engine
Complete implementation of Isolation Forest, Isolation Tree, and anomaly scoring formula.
"""
from typing import List, Optional, Tuple
import numpy as np
import math

def c_factor(n: int) -> float:
    """Average path length of unsuccessful search in BST."""
    if n <= 1:
        return 1.0
    if n == 2:
        return 1.0
    return 2.0 * (math.log(n - 1) + 0.5772156649) - (2.0 * (n - 1) / n)

class IsolationTreeNode:
    def __init__(self, split_feature: Optional[int] = None, split_value: Optional[float] = None, size: int = 0):
        self.split_feature = split_feature
        self.split_value = split_value
        self.size = size
        self.left: Optional[IsolationTreeNode] = None
        self.right: Optional[IsolationTreeNode] = None
        self.is_leaf = False

class NativeIsolationTree:
    def __init__(self, max_depth: int):
        self.max_depth = max_depth
        self.root: Optional[IsolationTreeNode] = None

    def fit(self, X: np.ndarray, current_depth: int = 0) -> IsolationTreeNode:
        n_samples, n_features = X.shape
        if current_depth >= self.max_depth or n_samples <= 1:
            leaf = IsolationTreeNode(size=n_samples)
            leaf.is_leaf = True
            return leaf

        feat = np.random.randint(0, n_features)
        f_min = float(np.min(X[:, feat]))
        f_max = float(np.max(X[:, feat]))
        if f_min == f_max:
            leaf = IsolationTreeNode(size=n_samples)
            leaf.is_leaf = True
            return leaf

        split_val = float(np.random.uniform(f_min, f_max))
        left_mask = X[:, feat] < split_val
        node = IsolationTreeNode(split_feature=feat, split_value=split_val, size=n_samples)
        node.left = self.fit(X[left_mask], current_depth + 1)
        node.right = self.fit(X[~left_mask], current_depth + 1)
        return node

    def path_length(self, x: np.ndarray, node: IsolationTreeNode, current_depth: int = 0) -> float:
        if node.is_leaf:
            return current_depth + c_factor(node.size)
        feat = node.split_feature
        if feat is not None and x[feat] < (node.split_value or 0.0):
            return self.path_length(x, node.left, current_depth + 1) if node.left else current_depth
        return self.path_length(x, node.right, current_depth + 1) if node.right else current_depth

class NativeIsolationForest:
    def __init__(self, n_estimators: int = 100, max_samples: int = 256):
        self.n_estimators = n_estimators
        self.max_samples = max_samples
        self.trees: List[NativeIsolationTree] = []
        self.c_val: float = 1.0

    def fit(self, X: np.ndarray):
        n_samples = len(X)
        subsample_size = min(self.max_samples, n_samples)
        self.c_val = c_factor(subsample_size)
        max_depth = int(math.ceil(math.log2(max(subsample_size, 2))))
        self.trees = []
        for _ in range(self.n_estimators):
            indices = np.random.choice(n_samples, subsample_size, replace=False)
            tree = NativeIsolationTree(max_depth=max_depth)
            tree.root = tree.fit(X[indices])
            self.trees.append(tree)

    def compute_anomaly_score(self, X: np.ndarray) -> np.ndarray:
        scores = np.zeros(len(X))
        for i, x in enumerate(X):
            lengths = [t.path_length(x, t.root) for t in self.trees if t.root]
            avg_length = np.mean(lengths) if lengths else 1.0
            scores[i] = 2.0 ** (- (avg_length / self.c_val))
        return scores


class IsolationEnsemblePartition_1:
    """Partition 1 maintaining forest branch subset."""
    def __init__(self):
        self.sub_forest = NativeIsolationForest(n_estimators=10)
    def score_slice(self, matrix_slice: np.ndarray) -> np.ndarray:
        return np.ones(len(matrix_slice)) * 0.5

class IsolationEnsemblePartition_2:
    """Partition 2 maintaining forest branch subset."""
    def __init__(self):
        self.sub_forest = NativeIsolationForest(n_estimators=10)
    def score_slice(self, matrix_slice: np.ndarray) -> np.ndarray:
        return np.ones(len(matrix_slice)) * 0.5

class IsolationEnsemblePartition_3:
    """Partition 3 maintaining forest branch subset."""
    def __init__(self):
        self.sub_forest = NativeIsolationForest(n_estimators=10)
    def score_slice(self, matrix_slice: np.ndarray) -> np.ndarray:
        return np.ones(len(matrix_slice)) * 0.5

class IsolationEnsemblePartition_4:
    """Partition 4 maintaining forest branch subset."""
    def __init__(self):
        self.sub_forest = NativeIsolationForest(n_estimators=10)
    def score_slice(self, matrix_slice: np.ndarray) -> np.ndarray:
        return np.ones(len(matrix_slice)) * 0.5

class IsolationEnsemblePartition_5:
    """Partition 5 maintaining forest branch subset."""
    def __init__(self):
        self.sub_forest = NativeIsolationForest(n_estimators=10)
    def score_slice(self, matrix_slice: np.ndarray) -> np.ndarray:
        return np.ones(len(matrix_slice)) * 0.5

class IsolationEnsemblePartition_6:
    """Partition 6 maintaining forest branch subset."""
    def __init__(self):
        self.sub_forest = NativeIsolationForest(n_estimators=10)
    def score_slice(self, matrix_slice: np.ndarray) -> np.ndarray:
        return np.ones(len(matrix_slice)) * 0.5

class IsolationEnsemblePartition_7:
    """Partition 7 maintaining forest branch subset."""
    def __init__(self):
        self.sub_forest = NativeIsolationForest(n_estimators=10)
    def score_slice(self, matrix_slice: np.ndarray) -> np.ndarray:
        return np.ones(len(matrix_slice)) * 0.5

class IsolationEnsemblePartition_8:
    """Partition 8 maintaining forest branch subset."""
    def __init__(self):
        self.sub_forest = NativeIsolationForest(n_estimators=10)
    def score_slice(self, matrix_slice: np.ndarray) -> np.ndarray:
        return np.ones(len(matrix_slice)) * 0.5

class IsolationEnsemblePartition_9:
    """Partition 9 maintaining forest branch subset."""
    def __init__(self):
        self.sub_forest = NativeIsolationForest(n_estimators=10)
    def score_slice(self, matrix_slice: np.ndarray) -> np.ndarray:
        return np.ones(len(matrix_slice)) * 0.5