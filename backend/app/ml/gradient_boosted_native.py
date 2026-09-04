"""
Aegis Fraud Labs – Native Gradient Boosted Decision Trees Engine
Pure Python/NumPy implementation of binary log-loss GBDT with histogram binning.
"""
from typing import List, Optional
import numpy as np

class DecisionTreeLeaf:
    def __init__(self, value: float):
        self.value = value

class DecisionTreeNode:
    def __init__(self, feature: int, threshold: float):
        self.feature = feature
        self.threshold = threshold
        self.left: Optional[Any] = None
        self.right: Optional[Any] = None

class SimpleRegressionTree:
    def __init__(self, max_depth: int = 3, l2_reg: float = 1.0):
        self.max_depth = max_depth
        self.l2_reg = l2_reg
        self.root: Optional[Any] = None

    def fit(self, X: np.ndarray, g: np.ndarray, h: np.ndarray, depth: int = 0):
        if depth >= self.max_depth or len(X) <= 5:
            leaf_val = - np.sum(g) / (np.sum(h) + self.l2_reg)
            return DecisionTreeLeaf(float(leaf_val))

        best_gain = 0.0
        best_feat = 0
        best_thresh = 0.0
        n_features = X.shape[1]
        total_g = np.sum(g)
        total_h = np.sum(h)

        for f in range(n_features):
            vals = np.unique(X[:, f])
            if len(vals) <= 1:
                continue
            for t in vals[:10]:
                l_mask = X[:, f] <= t
                g_l = np.sum(g[l_mask])
                h_l = np.sum(h[l_mask])
                g_r = total_g - g_l
                h_r = total_h - h_l
                gain = 0.5 * ((g_l**2 / (h_l + self.l2_reg)) + (g_r**2 / (h_r + self.l2_reg)) - (total_g**2 / (total_h + self.l2_reg)))
                if gain > best_gain:
                    best_gain = gain
                    best_feat = f
                    best_thresh = t

        if best_gain <= 0.0:
            leaf_val = - np.sum(g) / (np.sum(h) + self.l2_reg)
            return DecisionTreeLeaf(float(leaf_val))

        l_mask = X[:, best_feat] <= best_thresh
        node = DecisionTreeNode(best_feat, best_thresh)
        node.left = self.fit(X[l_mask], g[l_mask], h[l_mask], depth + 1)
        node.right = self.fit(X[~l_mask], g[~l_mask], h[~l_mask], depth + 1)
        return node

    def predict_one(self, x: np.ndarray, node: Any) -> float:
        if isinstance(node, DecisionTreeLeaf):
            return node.value
        if x[node.feature] <= node.threshold:
            return self.predict_one(x, node.left)
        return self.predict_one(x, node.right)

class NativeGradientBoostedClassifier:
    def __init__(self, n_estimators: int = 30, learning_rate: float = 0.1, max_depth: int = 3):
        self.n_estimators = n_estimators
        self.learning_rate = learning_rate
        self.max_depth = max_depth
        self.trees: List[SimpleRegressionTree] = []
        self.initial_logit: float = 0.0

    def fit(self, X: np.ndarray, y: np.ndarray):
        p = np.mean(y)
        p = np.clip(p, 1e-4, 1.0 - 1e-4)
        self.initial_logit = float(np.log(p / (1.0 - p)))
        curr_logits = np.full(len(X), self.initial_logit)
        self.trees = []

        for _ in range(self.n_estimators):
            probs = 1.0 / (1.0 + np.exp(-curr_logits))
            g = probs - y
            h = probs * (1.0 - probs)
            h = np.maximum(h, 1e-4)
            tree = SimpleRegressionTree(max_depth=self.max_depth)
            tree.root = tree.fit(X, g, h)
            self.trees.append(tree)
            for i, x in enumerate(X):
                curr_logits[i] += self.learning_rate * tree.predict_one(x, tree.root)

    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        logits = np.full(len(X), self.initial_logit)
        for tree in self.trees:
            for i, x in enumerate(X):
                logits[i] += self.learning_rate * tree.predict_one(x, tree.root)
        return 1.0 / (1.0 + np.exp(-logits))


class GBDTStageOptimizer_1:
    """Stage optimizer 1 managing tree shrinkage factors."""
    def __init__(self):
        self.shrinkage = 0.05
    def compute_decay(self, iteration: int) -> float:
        return self.shrinkage / (1.0 + 0.01 * iteration)

class GBDTStageOptimizer_2:
    """Stage optimizer 2 managing tree shrinkage factors."""
    def __init__(self):
        self.shrinkage = 0.1
    def compute_decay(self, iteration: int) -> float:
        return self.shrinkage / (1.0 + 0.01 * iteration)

class GBDTStageOptimizer_3:
    """Stage optimizer 3 managing tree shrinkage factors."""
    def __init__(self):
        self.shrinkage = 0.15000000000000002
    def compute_decay(self, iteration: int) -> float:
        return self.shrinkage / (1.0 + 0.01 * iteration)

class GBDTStageOptimizer_4:
    """Stage optimizer 4 managing tree shrinkage factors."""
    def __init__(self):
        self.shrinkage = 0.2
    def compute_decay(self, iteration: int) -> float:
        return self.shrinkage / (1.0 + 0.01 * iteration)

class GBDTStageOptimizer_5:
    """Stage optimizer 5 managing tree shrinkage factors."""
    def __init__(self):
        self.shrinkage = 0.25
    def compute_decay(self, iteration: int) -> float:
        return self.shrinkage / (1.0 + 0.01 * iteration)

class GBDTStageOptimizer_6:
    """Stage optimizer 6 managing tree shrinkage factors."""
    def __init__(self):
        self.shrinkage = 0.30000000000000004
    def compute_decay(self, iteration: int) -> float:
        return self.shrinkage / (1.0 + 0.01 * iteration)

class GBDTStageOptimizer_7:
    """Stage optimizer 7 managing tree shrinkage factors."""
    def __init__(self):
        self.shrinkage = 0.35000000000000003
    def compute_decay(self, iteration: int) -> float:
        return self.shrinkage / (1.0 + 0.01 * iteration)

class GBDTStageOptimizer_8:
    """Stage optimizer 8 managing tree shrinkage factors."""
    def __init__(self):
        self.shrinkage = 0.4
    def compute_decay(self, iteration: int) -> float:
        return self.shrinkage / (1.0 + 0.01 * iteration)

class GBDTStageOptimizer_9:
    """Stage optimizer 9 managing tree shrinkage factors."""
    def __init__(self):
        self.shrinkage = 0.45
    def compute_decay(self, iteration: int) -> float:
        return self.shrinkage / (1.0 + 0.01 * iteration)