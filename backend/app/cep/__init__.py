"""CEP Package."""
from backend.app.cep.sliding_windows import window_registry, SlidingWindow, MultiTimeframeWindowBank
from backend.app.cep.velocity_metrics import VelocityAnalyzer
from backend.app.cep.geo_engine import GeodesicCalculator, ImpossibleTravelDetector, CountryRiskRegistry
from backend.app.cep.device_fingerprinting import DeviceProfiler
from backend.app.cep.biometrics_engine import BehavioralBiometricsEngine