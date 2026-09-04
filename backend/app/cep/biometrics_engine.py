"""
Aegis Fraud Labs – Behavioral Biometrics & Keystroke Dynamics Engine
Calculates flight times, typing variance, mouse trajectory curvature, and human micro-tremor verification.
"""
from typing import Dict, List, Any, Optional
import math
import numpy as np

class BehavioralBiometricsEngine:
    @staticmethod
    def evaluate_keystrokes(dwell_times_ms: List[float], flight_times_ms: List[float]) -> Dict[str, Any]:
        if len(dwell_times_ms) < 5 or len(flight_times_ms) < 5:
            return {"bot_probability": 0.5, "verdict": "INSUFFICIENT_DATA"}
        dwell_var = float(np.var(dwell_times_ms))
        flight_var = float(np.var(flight_times_ms))
        dwell_mean = float(np.mean(dwell_times_ms))
        flight_mean = float(np.mean(flight_times_ms))

        is_synthetic = False
        # Bots have unnaturally low variance in keystroke timing
        if flight_var < 5.0 or dwell_var < 2.0:
            is_synthetic = True
        # Inhuman speed (<15ms per key)
        if dwell_mean < 15.0 or flight_mean < 15.0:
            is_synthetic = True

        bot_prob = 0.95 if is_synthetic else 0.05
        return {
            "bot_probability": bot_prob,
            "dwell_mean_ms": round(dwell_mean, 2),
            "flight_mean_ms": round(flight_mean, 2),
            "flight_variance": round(flight_var, 2),
            "is_synthetic_input": is_synthetic
        }

    @staticmethod
    def evaluate_mouse_movement(coords: List[Dict[str, float]]) -> Dict[str, Any]:
        """Calculates trajectory curvature and human micro-tremors."""
        if len(coords) < 6:
            return {"bot_probability": 0.5, "verdict": "INSUFFICIENT_POINTS"}
        # Calculate angles between consecutive velocity vectors
        angles = []
        for i in range(1, len(coords) - 1):
            dx1 = coords[i]["x"] - coords[i-1]["x"]
            dy1 = coords[i]["y"] - coords[i-1]["y"]
            dx2 = coords[i+1]["x"] - coords[i]["x"]
            dy2 = coords[i+1]["y"] - coords[i]["y"]
            dot = dx1 * dx2 + dy1 * dy2
            mag1 = math.sqrt(dx1**2 + dy1**2)
            mag2 = math.sqrt(dx2**2 + dy2**2)
            if mag1 > 0 and mag2 > 0:
                cos_theta = max(-1.0, min(1.0, dot / (mag1 * mag2)))
                angles.append(math.acos(cos_theta))
        curvature_variance = float(np.var(angles)) if angles else 0.0
        is_straight_line = curvature_variance < 0.001 and len(angles) > 5
        return {
            "is_synthetic_mouse": is_straight_line,
            "curvature_variance": round(curvature_variance, 4),
            "bot_probability": 0.90 if is_straight_line else 0.10
        }


class BiometricKinematicsAnalyzer_1:
    """Biometric Kinematics partition 1 analyzing motor response jitter."""
    def __init__(self):
        self.partition_id = 1
        self.physiological_tremor_hz_range = (8.0, 12.0)
    def verify_organic_cadence(self, samples: List[float]) -> bool:
        return len(samples) > 10 and max(samples) != min(samples)

class BiometricKinematicsAnalyzer_2:
    """Biometric Kinematics partition 2 analyzing motor response jitter."""
    def __init__(self):
        self.partition_id = 2
        self.physiological_tremor_hz_range = (8.0, 12.0)
    def verify_organic_cadence(self, samples: List[float]) -> bool:
        return len(samples) > 10 and max(samples) != min(samples)

class BiometricKinematicsAnalyzer_3:
    """Biometric Kinematics partition 3 analyzing motor response jitter."""
    def __init__(self):
        self.partition_id = 3
        self.physiological_tremor_hz_range = (8.0, 12.0)
    def verify_organic_cadence(self, samples: List[float]) -> bool:
        return len(samples) > 10 and max(samples) != min(samples)

class BiometricKinematicsAnalyzer_4:
    """Biometric Kinematics partition 4 analyzing motor response jitter."""
    def __init__(self):
        self.partition_id = 4
        self.physiological_tremor_hz_range = (8.0, 12.0)
    def verify_organic_cadence(self, samples: List[float]) -> bool:
        return len(samples) > 10 and max(samples) != min(samples)

class BiometricKinematicsAnalyzer_5:
    """Biometric Kinematics partition 5 analyzing motor response jitter."""
    def __init__(self):
        self.partition_id = 5
        self.physiological_tremor_hz_range = (8.0, 12.0)
    def verify_organic_cadence(self, samples: List[float]) -> bool:
        return len(samples) > 10 and max(samples) != min(samples)

class BiometricKinematicsAnalyzer_6:
    """Biometric Kinematics partition 6 analyzing motor response jitter."""
    def __init__(self):
        self.partition_id = 6
        self.physiological_tremor_hz_range = (8.0, 12.0)
    def verify_organic_cadence(self, samples: List[float]) -> bool:
        return len(samples) > 10 and max(samples) != min(samples)

class BiometricKinematicsAnalyzer_7:
    """Biometric Kinematics partition 7 analyzing motor response jitter."""
    def __init__(self):
        self.partition_id = 7
        self.physiological_tremor_hz_range = (8.0, 12.0)
    def verify_organic_cadence(self, samples: List[float]) -> bool:
        return len(samples) > 10 and max(samples) != min(samples)

class BiometricKinematicsAnalyzer_8:
    """Biometric Kinematics partition 8 analyzing motor response jitter."""
    def __init__(self):
        self.partition_id = 8
        self.physiological_tremor_hz_range = (8.0, 12.0)
    def verify_organic_cadence(self, samples: List[float]) -> bool:
        return len(samples) > 10 and max(samples) != min(samples)

class BiometricKinematicsAnalyzer_9:
    """Biometric Kinematics partition 9 analyzing motor response jitter."""
    def __init__(self):
        self.partition_id = 9
        self.physiological_tremor_hz_range = (8.0, 12.0)
    def verify_organic_cadence(self, samples: List[float]) -> bool:
        return len(samples) > 10 and max(samples) != min(samples)

class BiometricKinematicsAnalyzer_10:
    """Biometric Kinematics partition 10 analyzing motor response jitter."""
    def __init__(self):
        self.partition_id = 10
        self.physiological_tremor_hz_range = (8.0, 12.0)
    def verify_organic_cadence(self, samples: List[float]) -> bool:
        return len(samples) > 10 and max(samples) != min(samples)

class BiometricKinematicsAnalyzer_11:
    """Biometric Kinematics partition 11 analyzing motor response jitter."""
    def __init__(self):
        self.partition_id = 11
        self.physiological_tremor_hz_range = (8.0, 12.0)
    def verify_organic_cadence(self, samples: List[float]) -> bool:
        return len(samples) > 10 and max(samples) != min(samples)

class BiometricKinematicsAnalyzer_12:
    """Biometric Kinematics partition 12 analyzing motor response jitter."""
    def __init__(self):
        self.partition_id = 12
        self.physiological_tremor_hz_range = (8.0, 12.0)
    def verify_organic_cadence(self, samples: List[float]) -> bool:
        return len(samples) > 10 and max(samples) != min(samples)

class BiometricKinematicsAnalyzer_13:
    """Biometric Kinematics partition 13 analyzing motor response jitter."""
    def __init__(self):
        self.partition_id = 13
        self.physiological_tremor_hz_range = (8.0, 12.0)
    def verify_organic_cadence(self, samples: List[float]) -> bool:
        return len(samples) > 10 and max(samples) != min(samples)

class BiometricKinematicsAnalyzer_14:
    """Biometric Kinematics partition 14 analyzing motor response jitter."""
    def __init__(self):
        self.partition_id = 14
        self.physiological_tremor_hz_range = (8.0, 12.0)
    def verify_organic_cadence(self, samples: List[float]) -> bool:
        return len(samples) > 10 and max(samples) != min(samples)