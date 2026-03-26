<<<<<<< HEAD
#  Real-Time Sensor Anomaly Detection (Qdrant Edge)

##  Overview
This project demonstrates a *real-time anomaly detection system* using vector similarity search and a local Qdrant Edge engine.

It simulates sensor data (temperature, humidity, vibration) and detects anomalies such as:
-  Spike  
-  Drift  
-  Drop  

---

##  How It Works

1. Sensor data is generated in real-time  
2. Converted into vectors  
3. Stored in a local Qdrant Edge database  
4. New data is compared using similarity search  
5. Low similarity → anomaly detected  

---

##  Tech Stack

- Python 3.12  
- Streamlit  
- NumPy  
- Plotly  
- Qdrant Edge (local vector database)  

---

##  Project Structure

qdrant_edge_project/
│── main.py
│── config.py
│── requirements.txt
│
├── core/
│   └── qdrant_engine.py
│
├── intelligence/
│   └── anomaly_engine.py

---

##  How to Run

### 1. Clone the repository
git clone <your-repo-link>
cd qdrant_edge_project

### 2. Create virtual environment
python -m venv venv
source venv/bin/activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run the application
streamlit run main.py
=======
# Real-Time Sensor Anomaly Detection on Raspberrypi OS

## Overview
This project demonstrates a real-time anomaly detection system using sensor data and vector similarity on raspberrypi.

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

## How It Works(on Raspberrypi OS)
1. Normal sensor data is stored as vectors in Qdrant
2. Incoming real-time data is generated using a smooth pattern (sine-based)
3. Each new data point is compared with stored vectors
4. A similarity score is calculated
5. If similarity < 0.8 → Anomaly is detected

---

## Installation

pip3 install -r requirements.txt

---

## Run the Project

python3 -m streamlit run realtime_anomaly.py
>>>>>>> 428ac8b3ef73c5e7f492acda721260f5aa234fee

---

## Output
<<<<<<< HEAD

- Live updating graph  
- Similarity score tracking  
- Red markers indicating anomalies  

---

## Important Notes


- If storage error occurs:
rm -rf qdrant_data
---

## Future Improvements

- Real sensor integration (Raspberry Pi)
- Alert system (email/SMS) 
- Cloud deployment 
- Advanced ML models

---
=======
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

>>>>>>> 428ac8b3ef73c5e7f492acda721260f5aa234fee
