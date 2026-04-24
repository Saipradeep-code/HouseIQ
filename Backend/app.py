import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

print("App starting...")

app = Flask(__name__)
CORS(app)

chat_session = None
if GEMINI_API_KEY:
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        chatbot_model = genai.GenerativeModel(
            'gemini-2.5-flash',
            system_instruction="You are an expert Indian Real Estate AI Assistant. Help the user with property decisions, market trends, analyzing numbers, affordable cities in India, etc. Keep answers concise, factual, and use markdown formatting."
        )
        chat_session = chatbot_model.start_chat(history=[])
        print("Gemini Chatbot loaded ✅")
    except Exception as e:
        print("Failed to initialize Gemini:", e)

# CITY STATS DEFAULTS
CITY_STATS = {
    "Bangalore": {"population": 12327000, "literacy": 0.88},
    "Chennai": {"population": 10971000, "literacy": 0.90},
    "Delhi": {"population": 30290000, "literacy": 0.86},
    "Hyderabad": {"population": 10004000, "literacy": 0.83},
    "Kolkata": {"population": 14850000, "literacy": 0.87},
    "Mumbai": {"population": 20411000, "literacy": 0.90}
}

# --- LOAD ML MODEL safely ---
model = None
try:
    print("Loading model...")
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(current_dir, "model.pkl")

    if not os.path.exists(model_path):
        model_path = os.path.join(current_dir, "..", "Notebooks", "model.pkl")

    if not os.path.exists(model_path):
        model_path = "model.pkl"

    model = joblib.load(model_path)
    print("Model loaded ✅")
except Exception as e:
    print("Error loading model:", e)

@app.route("/")
def home():
    return jsonify({"status": "Server is running ✅"})

@app.route("/city-data/<city>", methods=["GET"])
def get_city_data(city):
    if city in CITY_STATS:
        return jsonify(CITY_STATS[city])
    return jsonify({"population": 5000000, "literacy": 0.85}), 404

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        area = float(data.get("area") or 1200)
        bedrooms = int(data.get("bedrooms") or 2)
        price_per_sqft = float(data.get("price_per_sqft") or 6500)
        city = data.get("city", "Bangalore")
        monthly_income = float(data.get("monthly_income") or 0)
        
        cstats = CITY_STATS.get(city, {"population": 5000000, "literacy": 0.85})
        population = cstats["population"]
        literacy = cstats["literacy"]

        literate = population * literacy
        power_parity = population * 0.002

        features = [0] * 12
        features[0] = area
        features[1] = bedrooms
        features[2] = population
        features[3] = literate
        features[4] = power_parity
        features[5] = literacy
        features[6] = price_per_sqft

        city_map = {"Chennai": 7, "Delhi": 8, "Hyderabad": 9, "Kolkata": 10, "Mumbai": 11}
        if city in city_map:
            features[city_map[city]] = 1

        if model:
            predicted_price = float(model.predict([features])[0])
        else:
            predicted_price = area * price_per_sqft * 1.1

        affordability_ratio = None
        decision_message = None

        if monthly_income > 0:
            annual_income = monthly_income * 12
            affordability_ratio = round(predicted_price / annual_income, 2)

            if affordability_ratio <= 3:
                decision_message = "💡 Smart Investment: This property is well within your budget."
            elif 3 < affordability_ratio <= 5:
                decision_message = "⚠️ Moderate Risk: This property may strain your finances."
            else:
                decision_message = "🚫 High Risk: This property is not financially safe right now."

        return jsonify({
            "price": predicted_price,
            "affordability_ratio": affordability_ratio,
            "decision_message": decision_message
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/compare", methods=["POST"])
def compare():
    try:
        data = request.json
        area = data.get("area", 1000)
        bedrooms = data.get("bedrooms", 2)
        pps = data.get("price_per_sqft", 5000)
        
        results = []
        for city, stats in CITY_STATS.items():
            f = [0] * 12
            f[0] = area
            f[1] = bedrooms
            f[2] = stats["population"]
            f[3] = stats["population"] * stats["literacy"]
            f[4] = stats["population"] * 0.002
            f[5] = stats["literacy"]
            f[6] = pps

            cm = {"Chennai": 7, "Delhi": 8, "Hyderabad": 9, "Kolkata": 10, "Mumbai": 11}
            if city in cm:
                f[cm[city]] = 1

            if model:
                p = float(model.predict([f])[0])
            else:
                p = area * pps

            results.append({"city": city, "avg_price": p})
            
        return jsonify(results)

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/recommend", methods=["POST"])
def recommend():
    try:
        data = request.json
        budget = float(data.get("budget", 5000000))
        bedrooms = int(data.get("bedrooms", 2))
        
        res = []
        for city, stats in CITY_STATS.items():
            pps = 5000
            if city == "Mumbai": pps = 15000
            elif city == "Delhi": pps = 9000
            elif city == "Bangalore": pps = 7500
            elif city == "Chennai": pps = 6500
            
            est_p = (bedrooms * 550) * pps

            if est_p <= budget * 0.8:
                match = 95
                tag = "Highly Affordable"
            elif est_p <= budget:
                match = 80
                tag = "Within Budget"
            elif est_p <= budget * 1.2:
                match = 50
                tag = "Slightly Over Budget"
            else:
                match = 20
                tag = "Not Recommended"
            
            res.append({"city": city, "est_price": est_p, "match": match, "tag": tag})
            
        res.sort(key=lambda x: x["match"], reverse=True)

        return jsonify({"recommendations": res})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/chatbot", methods=["POST"])
def chatbot():
    try:
        data = request.json
        msg = data.get("message", "")

        if not msg:
            return jsonify({"reply": "I didn't catch that."})

        if chat_session:
            r = chat_session.send_message(msg)
            return jsonify({"reply": r.text})

        return jsonify({"reply": "Gemini AI is currently offline."})

    except Exception:
        return jsonify({"reply": "AI Engine timeout."})

# ✅ IMPORTANT FIX FOR DEPLOYMENT
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)