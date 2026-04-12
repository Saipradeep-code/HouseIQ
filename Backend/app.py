print("App starting...")

from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

# create app
app = Flask(__name__)
CORS(app)

# load model
try:
    print("Loading model...")
    model = joblib.load("model.pkl")
    print("Model loaded ✅")
except Exception as e:
    print("Error loading model:", e)

# home route
@app.route("/")
def home():
    return "Server is running ✅"

# prediction route
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    # 🔥 get inputs from frontend
    area = float(data["area"])
    bedrooms = int(data["bedrooms"])
    population = float(data["population"])
    literacy = float(data["literacy"])
    price_per_sqft = float(data["price_per_sqft"])
    city = data["city"]

    # 🔥 derive missing features
    literate = population * literacy
    power_parity = population * 0.002

    # 🔥 exact 12 feature positions
    features = [0] * 12

    # base features
    features[0] = area
    features[1] = bedrooms
    features[2] = population
    features[3] = literate
    features[4] = power_parity
    features[5] = literacy
    features[6] = price_per_sqft

    # city encoding
    city_map = {
        "Chennai": 7,
        "Delhi": 8,
        "Hyderabad": 9,
        "Kolkata": 10,
        "Mumbai": 11
    }

    if city in city_map:
        features[city_map[city]] = 1

    # convert to numpy array
    input_array = np.array([features])

    # predict
    prediction = model.predict(input_array)[0]

    return jsonify({"price": int(prediction)})

# run server
if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True)