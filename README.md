# Real-Time Sensor Anomaly Detection

## Overview
This project demonstrates a real-time anomaly detection system using sensor data and vector similarity.

It simulates sensor readings (temperature, humidity, vibration), stores normal patterns in a vector database, and detects anomalies based on similarity scores.

---

## Features
- Real-time sensor data simulation
- Vector-based anomaly detection using Qdrant
- Similarity score visualization
- Anomaly detection when similarity < 0.8
- Interactive dashboard using Streamlit

---

## Tech Stack
- Python
- Streamlit
- Qdrant Vector Database
- Plotly

---

## How It Works
1. Normal sensor data is stored as vectors in Qdrant
2. Incoming real-time data is generated using a smooth pattern (sine-based)
3. Each new data point is compared with stored vectors
4. A similarity score is calculated
5. If similarity < 0.8 → Anomaly is detected

---

## Installation

pip install -r requirements.txt

---

## Run the Project

streamlit run realtime_anomaly.py

---

## Output
- Live similarity score graph
- Red markers indicate anomalies
- Threshold line at 0.8

---

## Project Structure

sensor_anomaly_project/
│
├── realtime_anomaly.py
├── requirements.txt
├── README.md

---

