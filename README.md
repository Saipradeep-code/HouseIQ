# 🏠 HouseIQ — Smart Real Estate Price Prediction System

## 🚀 Overview

**HouseIQ** is an end-to-end Machine Learning web application that predicts house prices using real estate and socio-economic data.

It integrates **Data Warehousing, Data Mining, and Machine Learning** into a full-stack system with a Flask backend and interactive frontend.

---

## 🧠 Features

* 🔮 Accurate price prediction using **Random Forest (R² ≈ 0.96)**
* 🌆 City-based analysis (Mumbai, Chennai, Bangalore, etc.)
* 📊 Uses socio-economic factors:

  * Population
  * Literacy Rate
  * Power Parity
* ⚡ Real-time prediction via API
* 🌐 Full-stack web app (Frontend + Backend)

---

## 🏗️ System Architecture

```
Frontend (HTML/CSS/JS)
        ↓
Flask Backend API
        ↓
Machine Learning Model
        ↓
Dataset (Housing + Census Data)
```

---

## 🛠️ Tech Stack

* Python
* Flask
* Scikit-learn
* Pandas, NumPy
* HTML, CSS, JavaScript
* Git & GitHub

---

## 📂 Project Structure

```
HouseIQ/
│
├── Backend/
│   └── app.py
│
├── Frontend/
│   └── index.html
│
├── Data/
│   ├── Bangalore.csv
│   ├── Chennai.csv
│   ├── Delhi.csv
│   ├── Hyderabad.csv
│   ├── Kolkata.csv
│   ├── Mumbai.csv
│   └── india-districts-census-2011.csv
│
├── Notebooks/
│   ├── real_estate_project.ipynb
│   └── final_dataset.csv
│
└── README.md
```

---

## ⚙️ How to Run Locally

### 1️⃣ Clone the repository

```
git clone https://github.com/Saipradeep-code/HouseIQ.git
cd HouseIQ
```

### 2️⃣ Install dependencies

```
pip install flask flask-cors numpy pandas scikit-learn joblib
```

### 3️⃣ Run backend

```
cd Backend
python app.py
```

### 4️⃣ Open frontend

Open the file:

```
Frontend/index.html
```

---

## 📊 Model Details

* Algorithm: **Random Forest Regressor**
* R² Score: ~0.96
* Features:

  * Area
  * Bedrooms
  * Population
  * Literacy Rate
  * Power Parity
  * Price per Sqft
  * City (One-Hot Encoded)

---

## ⚠️ Note

> The trained model file (`model.pkl`) is not included due to GitHub file size limits.
> You can regenerate it by running the notebook in the `Notebooks` folder.

---

## 🚀 Future Enhancements

* 🔐 User authentication (Firebase)
* 📊 Interactive dashboards & charts
* 🗺️ Map-based visualization
* 🤖 AI recommendation system
* 🌐 Live deployment

---

## 👨‍💻 Author

**Sai Pradeep**
GitHub: https://github.com/Saipradeep-code

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
