from flask import Flask, jsonify, request
from flask_cors import CORS
import random
import math

app = Flask(__name__)
CORS(app)  # 🔥 IMPORTANT: Enables frontend-backend connection


# -------------------------------
# ENVIRONMENT ANALYSIS ENGINE
# -------------------------------

class EnvironmentAnalyzer:
    def __init__(self, rain_mm, traffic_level, area_type):
        self.rain_mm = rain_mm
        self.traffic_level = traffic_level
        self.area_type = area_type

    def weather_score(self):
        return min(1, math.log(self.rain_mm + 1) / 3)

    def traffic_score(self):
        mapping = {
            "low": 0.35,
            "medium": 0.65,
            "high": 0.95
        }
        return mapping.get(self.traffic_level, 0.5)

    def location_score(self):
        mapping = {
            "safe": 0.3,
            "moderate": 0.6,
            "danger": 0.9
        }
        return mapping.get(self.area_type, 0.5)


# -------------------------------
# BEHAVIOR ENGINE
# -------------------------------

class BehaviorEngine:
    def __init__(self):
        self.sensor_variance = random.uniform(0.5, 1.0)
        self.route_stability = random.uniform(0.4, 1.0)
        self.micro_movements = random.uniform(0.3, 1.0)

    def behavior_score(self):
        return (
            self.sensor_variance * 0.4 +
            self.route_stability * 0.4 +
            self.micro_movements * 0.2
        )


# -------------------------------
# TRUST ENGINE
# -------------------------------

class TrustEngine:
    def __init__(self):
        self.network_stability = random.uniform(0.4, 1.0)
        self.crowd_match = random.uniform(0.3, 1.0)
        self.history_score = random.uniform(0.5, 1.0)

    def detect_spoof_pattern(self):
        return random.choice([True, False, False])

    def compute_trust(self, behavior_score):
        base_trust = (
            0.25 * behavior_score +
            0.25 * self.network_stability +
            0.25 * self.crowd_match +
            0.25 * self.history_score
        )

        if self.detect_spoof_pattern():
            base_trust *= 0.5

        return round(base_trust, 2)


# -------------------------------
# RISK ENGINE
# -------------------------------

class RiskEngine:
    def __init__(self, weather, traffic, location, behavior, history):
        self.weather = weather
        self.traffic = traffic
        self.location = location
        self.behavior = behavior
        self.history = history

    def compute_risk(self):
        risk = (
            0.3 * self.weather +
            0.25 * self.traffic +
            0.2 * self.location +
            0.15 * self.behavior +
            0.1 * self.history
        )

        noise = random.uniform(-0.05, 0.05)
        return round(min(max(risk + noise, 0), 1), 2)


# -------------------------------
# PRICING ENGINE
# -------------------------------

class PricingEngine:
    def __init__(self, base_price=30):
        self.base_price = base_price

    def surge_multiplier(self, risk):
        return 1 + (risk ** 2)

    def trust_discount(self, trust):
        return 1 - (trust * 0.4)

    def final_premium(self, risk, trust):
        premium = self.base_price * self.surge_multiplier(risk) * self.trust_discount(trust)
        return round(max(premium, 20), 2)


# -------------------------------
# API ROUTE
# -------------------------------

@app.route("/get_insurance_data", methods=["POST"])
def get_insurance_data():
    data = request.json

    rain = data.get("rain_mm", 5)
    traffic = data.get("traffic", "medium")
    area = data.get("area", "moderate")

    # Environment
    env = EnvironmentAnalyzer(rain, traffic, area)
    weather = env.weather_score()
    traffic_score = env.traffic_score()
    location = env.location_score()

    # Behavior
    behavior_engine = BehaviorEngine()
    behavior = behavior_engine.behavior_score()

    # Trust
    trust_engine = TrustEngine()
    trust = trust_engine.compute_trust(behavior)

    # Risk
    risk_engine = RiskEngine(weather, traffic_score, location, behavior, trust_engine.history_score)
    risk = risk_engine.compute_risk()

    # Pricing
    pricing = PricingEngine(base_price=30)
    premium = pricing.final_premium(risk, trust)

    # Decision
    status = "APPROVED" if trust > 0.6 else "FLAGGED"

    response = {
        "risk_score": risk,
        "trust_score": trust,
        "premium": premium,
        "status": status,
        "debug": {
            "weather": round(weather, 2),
            "traffic": traffic_score,
            "location": location,
            "behavior": round(behavior, 2)
        }
    }

    return jsonify(response)


# -------------------------------
# RUN SERVER
# -------------------------------

if __name__ == "__main__":
    app.run(debug=True)