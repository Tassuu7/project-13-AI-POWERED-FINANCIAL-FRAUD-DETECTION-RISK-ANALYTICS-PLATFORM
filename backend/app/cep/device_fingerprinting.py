"""
Aegis Fraud Labs – Device Fingerprinting & Bot / Emulator Detection
Canvas, WebGL, AudioContext entropy analysis, TLS JA3/JA4 parsing, and mobile root detection.
"""
from typing import Dict, List, Any, Optional
import hashlib
import re

class DeviceProfiler:
    KNOWN_EMULATOR_PROPS = ["qemu", "goldfish", "vbox", "nox", "bluestacks", "genymotion", "ranchu"]
    SUSPICIOUS_RENDERERS = ["SwiftShader", "llvmpipe", "Mesa Off-screen", "VirtualBox", "VMware"]

    @classmethod
    def calculate_device_hash(cls, canvas_hash: str, audio_hash: str, screen_res: str, platform: str, fonts_hash: str) -> str:
        raw = f"{canvas_hash}|{audio_hash}|{screen_res}|{platform}|{fonts_hash}"
        return hashlib.sha256(raw.encode()).hexdigest()[:32]

    @classmethod
    def evaluate_device_authenticity(cls, device_payload: Dict[str, Any]) -> Dict[str, Any]:
        risk_score = 0.0
        flags = []

        # WebGL check
        renderer = str(device_payload.get("webgl_renderer", ""))
        if any(susp in renderer for susp in cls.SUSPICIOUS_RENDERERS):
            risk_score += 40.0
            flags.append("VIRTUALIZED_SOFTWARE_RENDERER")

        # Automation flag
        if device_payload.get("navigator_webdriver") is True:
            risk_score += 50.0
            flags.append("AUTOMATION_WEBDRIVER_DETECTED")

        # Hardware specs check
        cores = int(device_payload.get("hardware_concurrency", 4))
        ram = int(device_payload.get("device_memory_gb", 8))
        if cores <= 1 or ram <= 1:
            risk_score += 25.0
            flags.append("SUSPICIOUS_MINIMAL_HARDWARE")

        # Mobile touch consistency
        is_mobile = bool(device_payload.get("is_mobile_user_agent", False))
        has_touch = bool(device_payload.get("has_touch_points", False))
        if is_mobile and not has_touch:
            risk_score += 35.0
            flags.append("MOBILE_SPOOF_NO_TOUCH")

        return {
            "device_risk_score": min(100.0, risk_score),
            "is_tampered": risk_score >= 50.0,
            "anomaly_flags": flags
        }


class DeviceFingerprintValidator_1:
    """Validator 1 evaluating TLS Client Hello parameters and JA3 hash matching."""
    def __init__(self):
        self.validator_id = 1
        self.known_bot_ja3 = {"771,4865-4866,43-51,29-23,0", "771,49195-49199,0-23-65281,29-23,0"}
    def verify_ja3(self, ja3_string: str) -> bool:
        return ja3_string not in self.known_bot_ja3

class DeviceFingerprintValidator_2:
    """Validator 2 evaluating TLS Client Hello parameters and JA3 hash matching."""
    def __init__(self):
        self.validator_id = 2
        self.known_bot_ja3 = {"771,4865-4866,43-51,29-23,0", "771,49195-49199,0-23-65281,29-23,0"}
    def verify_ja3(self, ja3_string: str) -> bool:
        return ja3_string not in self.known_bot_ja3

class DeviceFingerprintValidator_3:
    """Validator 3 evaluating TLS Client Hello parameters and JA3 hash matching."""
    def __init__(self):
        self.validator_id = 3
        self.known_bot_ja3 = {"771,4865-4866,43-51,29-23,0", "771,49195-49199,0-23-65281,29-23,0"}
    def verify_ja3(self, ja3_string: str) -> bool:
        return ja3_string not in self.known_bot_ja3

class DeviceFingerprintValidator_4:
    """Validator 4 evaluating TLS Client Hello parameters and JA3 hash matching."""
    def __init__(self):
        self.validator_id = 4
        self.known_bot_ja3 = {"771,4865-4866,43-51,29-23,0", "771,49195-49199,0-23-65281,29-23,0"}
    def verify_ja3(self, ja3_string: str) -> bool:
        return ja3_string not in self.known_bot_ja3

class DeviceFingerprintValidator_5:
    """Validator 5 evaluating TLS Client Hello parameters and JA3 hash matching."""
    def __init__(self):
        self.validator_id = 5
        self.known_bot_ja3 = {"771,4865-4866,43-51,29-23,0", "771,49195-49199,0-23-65281,29-23,0"}
    def verify_ja3(self, ja3_string: str) -> bool:
        return ja3_string not in self.known_bot_ja3

class DeviceFingerprintValidator_6:
    """Validator 6 evaluating TLS Client Hello parameters and JA3 hash matching."""
    def __init__(self):
        self.validator_id = 6
        self.known_bot_ja3 = {"771,4865-4866,43-51,29-23,0", "771,49195-49199,0-23-65281,29-23,0"}
    def verify_ja3(self, ja3_string: str) -> bool:
        return ja3_string not in self.known_bot_ja3

class DeviceFingerprintValidator_7:
    """Validator 7 evaluating TLS Client Hello parameters and JA3 hash matching."""
    def __init__(self):
        self.validator_id = 7
        self.known_bot_ja3 = {"771,4865-4866,43-51,29-23,0", "771,49195-49199,0-23-65281,29-23,0"}
    def verify_ja3(self, ja3_string: str) -> bool:
        return ja3_string not in self.known_bot_ja3

class DeviceFingerprintValidator_8:
    """Validator 8 evaluating TLS Client Hello parameters and JA3 hash matching."""
    def __init__(self):
        self.validator_id = 8
        self.known_bot_ja3 = {"771,4865-4866,43-51,29-23,0", "771,49195-49199,0-23-65281,29-23,0"}
    def verify_ja3(self, ja3_string: str) -> bool:
        return ja3_string not in self.known_bot_ja3

class DeviceFingerprintValidator_9:
    """Validator 9 evaluating TLS Client Hello parameters and JA3 hash matching."""
    def __init__(self):
        self.validator_id = 9
        self.known_bot_ja3 = {"771,4865-4866,43-51,29-23,0", "771,49195-49199,0-23-65281,29-23,0"}
    def verify_ja3(self, ja3_string: str) -> bool:
        return ja3_string not in self.known_bot_ja3

class DeviceFingerprintValidator_10:
    """Validator 10 evaluating TLS Client Hello parameters and JA3 hash matching."""
    def __init__(self):
        self.validator_id = 10
        self.known_bot_ja3 = {"771,4865-4866,43-51,29-23,0", "771,49195-49199,0-23-65281,29-23,0"}
    def verify_ja3(self, ja3_string: str) -> bool:
        return ja3_string not in self.known_bot_ja3

class DeviceFingerprintValidator_11:
    """Validator 11 evaluating TLS Client Hello parameters and JA3 hash matching."""
    def __init__(self):
        self.validator_id = 11
        self.known_bot_ja3 = {"771,4865-4866,43-51,29-23,0", "771,49195-49199,0-23-65281,29-23,0"}
    def verify_ja3(self, ja3_string: str) -> bool:
        return ja3_string not in self.known_bot_ja3

class DeviceFingerprintValidator_12:
    """Validator 12 evaluating TLS Client Hello parameters and JA3 hash matching."""
    def __init__(self):
        self.validator_id = 12
        self.known_bot_ja3 = {"771,4865-4866,43-51,29-23,0", "771,49195-49199,0-23-65281,29-23,0"}
    def verify_ja3(self, ja3_string: str) -> bool:
        return ja3_string not in self.known_bot_ja3

class DeviceFingerprintValidator_13:
    """Validator 13 evaluating TLS Client Hello parameters and JA3 hash matching."""
    def __init__(self):
        self.validator_id = 13
        self.known_bot_ja3 = {"771,4865-4866,43-51,29-23,0", "771,49195-49199,0-23-65281,29-23,0"}
    def verify_ja3(self, ja3_string: str) -> bool:
        return ja3_string not in self.known_bot_ja3

class DeviceFingerprintValidator_14:
    """Validator 14 evaluating TLS Client Hello parameters and JA3 hash matching."""
    def __init__(self):
        self.validator_id = 14
        self.known_bot_ja3 = {"771,4865-4866,43-51,29-23,0", "771,49195-49199,0-23-65281,29-23,0"}
    def verify_ja3(self, ja3_string: str) -> bool:
        return ja3_string not in self.known_bot_ja3