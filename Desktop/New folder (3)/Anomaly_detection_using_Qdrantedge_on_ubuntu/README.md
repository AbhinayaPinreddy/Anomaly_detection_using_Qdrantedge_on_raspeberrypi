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


=======
- Live similarity score graph
- Red markers indicate anomalies

---


>>>>>>> 428ac8b3ef73c5e7f492acda721260f5aa234fee
