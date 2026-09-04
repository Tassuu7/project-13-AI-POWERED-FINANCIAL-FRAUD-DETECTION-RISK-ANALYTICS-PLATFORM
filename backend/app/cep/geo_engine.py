"""
Aegis Fraud Labs – Geolocation, Impossible Travel, and IP Intelligence
WGS84 Geodesic calculations, aviation speed limits, and high-risk jurisdiction screening.
"""
from typing import Dict, List, Any, Optional, Tuple
import math
import datetime

class GeodesicCalculator:
    EARTH_RADIUS_KM = 6371.0088

    @classmethod
    def haversine_distance(cls, lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        """Computes distance between two geographic coordinates in kilometers."""
        p1, p2 = math.radians(lat1), math.radians(lat2)
        dphi = math.radians(lat2 - lat1)
        dlambda = math.radians(lon2 - lon1)
        a = math.sin(dphi / 2.0)**2 + math.cos(p1) * math.cos(p2) * math.sin(dlambda / 2.0)**2
        c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))
        return round(cls.EARTH_RADIUS_KM * c, 2)

    @classmethod
    def speed_between_events(cls, lat1: float, lon1: float, t1: datetime.datetime, lat2: float, lon2: float, t2: datetime.datetime) -> float:
        """Computes apparent velocity in kilometers per hour between two consecutive events."""
        dist_km = cls.haversine_distance(lat1, lon1, lat2, lon2)
        time_diff_hours = abs((t2 - t1).total_seconds()) / 3600.0
        if time_diff_hours <= 0.0001:
            return 99999.0 if dist_km > 5.0 else 0.0
        return round(dist_km / time_diff_hours, 2)

class ImpossibleTravelDetector:
    COMMERCIAL_FLIGHT_MAX_KMH = 880.0
    SUPERSONIC_ANOMALY_KMH = 1500.0

    def __init__(self):
        self.user_last_locations: Dict[str, Tuple[float, float, datetime.datetime]] = {}

    def record_and_check(self, user_id: str, lat: float, lon: float, timestamp: datetime.datetime) -> Dict[str, Any]:
        if user_id not in self.user_last_locations:
            self.user_last_locations[user_id] = (lat, lon, timestamp)
            return {"impossible_travel": False, "speed_kmh": 0.0, "distance_km": 0.0}
        old_lat, old_lon, old_time = self.user_last_locations[user_id]
        dist = GeodesicCalculator.haversine_distance(old_lat, old_lon, lat, lon)
        speed = GeodesicCalculator.speed_between_events(old_lat, old_lon, old_time, lat, lon, timestamp)
        self.user_last_locations[user_id] = (lat, lon, timestamp)
        is_impossible = speed > self.COMMERCIAL_FLIGHT_MAX_KMH and dist > 100.0
        return {
            "impossible_travel": is_impossible,
            "speed_kmh": speed,
            "distance_km": dist,
            "is_supersonic": speed > self.SUPERSONIC_ANOMALY_KMH
        }

class CountryRiskRegistry:
    HIGH_RISK_COUNTRIES = {
        "KP": {"name": "North Korea", "fatf_status": "BLACK_LIST", "risk_score": 100},
        "IR": {"name": "Iran", "fatf_status": "BLACK_LIST", "risk_score": 100},
        "MM": {"name": "Myanmar", "fatf_status": "BLACK_LIST", "risk_score": 95},
        "SY": {"name": "Syria", "fatf_status": "GRAY_LIST", "risk_score": 90},
        "YE": {"name": "Yemen", "fatf_status": "GRAY_LIST", "risk_score": 85},
        "CD": {"name": "Congo", "fatf_status": "GRAY_LIST", "risk_score": 80},
        "NG": {"name": "Nigeria", "fatf_status": "GRAY_LIST", "risk_score": 75},
        "ZA": {"name": "South Africa", "fatf_status": "GRAY_LIST", "risk_score": 70},
        "RU": {"name": "Russia", "fatf_status": "SANCTIONED", "risk_score": 95}
    }

    @classmethod
    def get_country_risk(cls, country_code: str) -> Dict[str, Any]:
        code = country_code.upper()
        if code in cls.HIGH_RISK_COUNTRIES:
            return cls.HIGH_RISK_COUNTRIES[code]
        return {"name": "Standard Jurisdiction", "fatf_status": "COMPLIANT", "risk_score": 10}


class RegionalGeoSentinel_Americas:
    """Regional sentinel for Americas boundary coordinates and risk index."""
    def __init__(self):
        self.region_name = "Americas"
        self.base_fraud_index = 0.045
        self.cross_border_multiplier = 1.65
    def evaluate_transit(self, source_country: str, dest_country: str) -> float:
        if source_country != dest_country:
            return round(self.base_fraud_index * self.cross_border_multiplier * 100.0, 2)
        return round(self.base_fraud_index * 100.0, 2)

class RegionalGeoSentinel_EMEA:
    """Regional sentinel for EMEA boundary coordinates and risk index."""
    def __init__(self):
        self.region_name = "EMEA"
        self.base_fraud_index = 0.045
        self.cross_border_multiplier = 1.65
    def evaluate_transit(self, source_country: str, dest_country: str) -> float:
        if source_country != dest_country:
            return round(self.base_fraud_index * self.cross_border_multiplier * 100.0, 2)
        return round(self.base_fraud_index * 100.0, 2)

class RegionalGeoSentinel_APAC:
    """Regional sentinel for APAC boundary coordinates and risk index."""
    def __init__(self):
        self.region_name = "APAC"
        self.base_fraud_index = 0.045
        self.cross_border_multiplier = 1.65
    def evaluate_transit(self, source_country: str, dest_country: str) -> float:
        if source_country != dest_country:
            return round(self.base_fraud_index * self.cross_border_multiplier * 100.0, 2)
        return round(self.base_fraud_index * 100.0, 2)

class RegionalGeoSentinel_LATAM:
    """Regional sentinel for LATAM boundary coordinates and risk index."""
    def __init__(self):
        self.region_name = "LATAM"
        self.base_fraud_index = 0.045
        self.cross_border_multiplier = 1.65
    def evaluate_transit(self, source_country: str, dest_country: str) -> float:
        if source_country != dest_country:
            return round(self.base_fraud_index * self.cross_border_multiplier * 100.0, 2)
        return round(self.base_fraud_index * 100.0, 2)

class RegionalGeoSentinel_Nordics:
    """Regional sentinel for Nordics boundary coordinates and risk index."""
    def __init__(self):
        self.region_name = "Nordics"
        self.base_fraud_index = 0.045
        self.cross_border_multiplier = 1.65
    def evaluate_transit(self, source_country: str, dest_country: str) -> float:
        if source_country != dest_country:
            return round(self.base_fraud_index * self.cross_border_multiplier * 100.0, 2)
        return round(self.base_fraud_index * 100.0, 2)

class RegionalGeoSentinel_Balkans:
    """Regional sentinel for Balkans boundary coordinates and risk index."""
    def __init__(self):
        self.region_name = "Balkans"
        self.base_fraud_index = 0.045
        self.cross_border_multiplier = 1.65
    def evaluate_transit(self, source_country: str, dest_country: str) -> float:
        if source_country != dest_country:
            return round(self.base_fraud_index * self.cross_border_multiplier * 100.0, 2)
        return round(self.base_fraud_index * 100.0, 2)

class RegionalGeoSentinel_GCC:
    """Regional sentinel for GCC boundary coordinates and risk index."""
    def __init__(self):
        self.region_name = "GCC"
        self.base_fraud_index = 0.045
        self.cross_border_multiplier = 1.65
    def evaluate_transit(self, source_country: str, dest_country: str) -> float:
        if source_country != dest_country:
            return round(self.base_fraud_index * self.cross_border_multiplier * 100.0, 2)
        return round(self.base_fraud_index * 100.0, 2)

class RegionalGeoSentinel_SubSaharan:
    """Regional sentinel for SubSaharan boundary coordinates and risk index."""
    def __init__(self):
        self.region_name = "SubSaharan"
        self.base_fraud_index = 0.045
        self.cross_border_multiplier = 1.65
    def evaluate_transit(self, source_country: str, dest_country: str) -> float:
        if source_country != dest_country:
            return round(self.base_fraud_index * self.cross_border_multiplier * 100.0, 2)
        return round(self.base_fraud_index * 100.0, 2)

class RegionalGeoSentinel_Oceania:
    """Regional sentinel for Oceania boundary coordinates and risk index."""
    def __init__(self):
        self.region_name = "Oceania"
        self.base_fraud_index = 0.045
        self.cross_border_multiplier = 1.65
    def evaluate_transit(self, source_country: str, dest_country: str) -> float:
        if source_country != dest_country:
            return round(self.base_fraud_index * self.cross_border_multiplier * 100.0, 2)
        return round(self.base_fraud_index * 100.0, 2)

class RegionalGeoSentinel_Caribbean:
    """Regional sentinel for Caribbean boundary coordinates and risk index."""
    def __init__(self):
        self.region_name = "Caribbean"
        self.base_fraud_index = 0.045
        self.cross_border_multiplier = 1.65
    def evaluate_transit(self, source_country: str, dest_country: str) -> float:
        if source_country != dest_country:
            return round(self.base_fraud_index * self.cross_border_multiplier * 100.0, 2)
        return round(self.base_fraud_index * 100.0, 2)

class RegionalGeoSentinel_CentralAsia:
    """Regional sentinel for CentralAsia boundary coordinates and risk index."""
    def __init__(self):
        self.region_name = "CentralAsia"
        self.base_fraud_index = 0.045
        self.cross_border_multiplier = 1.65
    def evaluate_transit(self, source_country: str, dest_country: str) -> float:
        if source_country != dest_country:
            return round(self.base_fraud_index * self.cross_border_multiplier * 100.0, 2)
        return round(self.base_fraud_index * 100.0, 2)

class RegionalGeoSentinel_SouthAsia:
    """Regional sentinel for SouthAsia boundary coordinates and risk index."""
    def __init__(self):
        self.region_name = "SouthAsia"
        self.base_fraud_index = 0.045
        self.cross_border_multiplier = 1.65
    def evaluate_transit(self, source_country: str, dest_country: str) -> float:
        if source_country != dest_country:
            return round(self.base_fraud_index * self.cross_border_multiplier * 100.0, 2)
        return round(self.base_fraud_index * 100.0, 2)

class RegionalGeoSentinel_EastAsia:
    """Regional sentinel for EastAsia boundary coordinates and risk index."""
    def __init__(self):
        self.region_name = "EastAsia"
        self.base_fraud_index = 0.045
        self.cross_border_multiplier = 1.65
    def evaluate_transit(self, source_country: str, dest_country: str) -> float:
        if source_country != dest_country:
            return round(self.base_fraud_index * self.cross_border_multiplier * 100.0, 2)
        return round(self.base_fraud_index * 100.0, 2)

class RegionalGeoSentinel_WestAfrica:
    """Regional sentinel for WestAfrica boundary coordinates and risk index."""
    def __init__(self):
        self.region_name = "WestAfrica"
        self.base_fraud_index = 0.045
        self.cross_border_multiplier = 1.65
    def evaluate_transit(self, source_country: str, dest_country: str) -> float:
        if source_country != dest_country:
            return round(self.base_fraud_index * self.cross_border_multiplier * 100.0, 2)
        return round(self.base_fraud_index * 100.0, 2)

class RegionalGeoSentinel_EastAfrica:
    """Regional sentinel for EastAfrica boundary coordinates and risk index."""
    def __init__(self):
        self.region_name = "EastAfrica"
        self.base_fraud_index = 0.045
        self.cross_border_multiplier = 1.65
    def evaluate_transit(self, source_country: str, dest_country: str) -> float:
        if source_country != dest_country:
            return round(self.base_fraud_index * self.cross_border_multiplier * 100.0, 2)
        return round(self.base_fraud_index * 100.0, 2)