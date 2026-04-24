# 🏠 HouseIQ AI – Intelligent Real Estate Platform

HouseIQ AI is a **full-stack AI-powered real estate web application** that helps users make smarter property decisions using **machine learning + generative AI**.

It provides:

* 📊 Price prediction
* 🧠 Smart recommendations
* 🤖 AI chatbot (Gemini-powered)
* 📈 Market comparison analytics
* 💰 EMI calculation
* 📄 PDF report generation

---

## 🌐 Live Demo

* 🔗 Frontend: https://houseiq-7082e.web.app
* 🔗 Backend API: https://houseiq.onrender.com

---

## 🚀 Features

### 🔮 AI Price Prediction

Predict house prices based on:

* Area (sqft)
* Bedrooms (BHK)
* City & location
* Market price per sqft
* Income-based affordability analysis

---

### 📊 Market Comparison

Compare property prices across major Indian cities:

* Bangalore
* Mumbai
* Delhi
* Hyderabad
* Chennai
* Kolkata

---

### 🤖 AI Chatbot (Gemini)

* Ask real estate questions
* Get insights on pricing trends, investment, and legalities
* Powered by Google Gemini API

---

### 🧭 Smart Recommendation System

* Suggests best cities based on:

  * Budget
  * BHK preference
* Provides match % and insights

---

### 💰 EMI Calculator

* Calculates monthly EMI
* Shows:

  * Total interest
  * Principal breakdown

---

### 📄 PDF Report Generator

* Generates downloadable property reports
* Includes:

  * Price
  * Risk ratio
  * AI decision

---

### 🔐 Authentication System

* User Signup/Login
* Firebase Authentication
* User-specific:

  * History
  * Favorites

---

## 🏗️ Tech Stack

### 🌐 Frontend

* HTML, CSS, JavaScript
* Firebase Hosting
* Firebase Authentication
* Firestore Database

### ⚙️ Backend

* Python (Flask)
* REST API
* Hosted on Render

### 🤖 AI & ML

* Scikit-learn (ML model)
* Google Gemini API (Chatbot)

---

## 🔗 Architecture

```
User → Firebase Frontend → Flask API (Render)
            ↓
        Fetch API
            ↓
Backend (ML Model + Gemini AI)
            ↓
        JSON Response
            ↓
Frontend UI Update
```

---

## 📁 Project Structure

```
HouseIQ/
│
├── Frontend/
│   ├── index.html
│   ├── 404.html
│
├── Backend/
│   ├── app.py
│   ├── requirements.txt
│
├── firebase.json
├── .firebaserc
├── README.md
```

---

## ⚙️ Setup Instructions

### 🔹 1. Clone Repository

```bash
git clone https://github.com/your-username/HouseIQ.git
cd HouseIQ
```

---

### 🔹 2. Backend Setup

```bash
cd Backend
pip install -r requirements.txt
```

Create `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

Run backend:

```bash
python app.py
```

---

### 🔹 3. Frontend Setup

Open `Frontend/index.html`
Update:

```javascript
const API_BASE = "http://127.0.0.1:5000";
```

---

### 🔹 4. Firebase Deployment

```bash
firebase deploy
```

---

## 🌍 Deployment

### Frontend

* Hosted on Firebase Hosting

### Backend

* Hosted on Render

---

## ⚠️ Notes

* Free Render tier may sleep after inactivity
* First request may take ~30–60 seconds
* Large `.pkl` model files are excluded from GitHub

---

## 💡 Future Improvements

* Payment integration (Razorpay)
* Real-time property listings API
* User dashboards with analytics
* Mobile app version
* Advanced ML models

---

## 👨‍💻 Author

**Sai Pradeep**

* GitHub: https://github.com/Saipradeep-code

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it!

---

## 🧠 Interview Summary (Bonus)

> “I built a full-stack AI real estate platform using Firebase for frontend and Flask backend deployed on Render, integrating machine learning and Gemini API via REST APIs.”

---
