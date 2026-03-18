import time
import math
import streamlit as st
import plotly.graph_objs as go
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

st.title("Real-Time Sensor Anomaly Detection")

client = QdrantClient(path="qdrant_storage")

if not client.collection_exists("sensor_collection"):
    client.create_collection(
        collection_name="sensor_collection",
        vectors_config=VectorParams(size=3, distance=Distance.COSINE),
    )

normal_data = [
    [25, 60, 0.02],
    [26, 58, 0.03],
    [24, 62, 0.01],
    [25, 59, 0.02]
]

points = [
    PointStruct(id=i, vector=normal_data[i], payload={"reading": normal_data[i]})
    for i in range(len(normal_data))
]

client.upsert(collection_name="sensor_collection", points=points)

chart = st.empty()
scores = []
anomaly_x = []
anomaly_y = []

t = 0

for i in range(100):

    t += 0.1

    temperature = 25 + 3 * math.sin(t)
    humidity = 60 + 8 * math.sin(t / 2)
    vibration = 0.02 + 0.02 * math.sin(t)

    if int(t * 10) % 50 == 0:
        temperature += 60
        humidity-= 40
        vibration += 5

    reading = [temperature, humidity, vibration]

    results = client.query_points(
        collection_name="sensor_collection",
        query=reading,
        limit=1
    )

    score = results.points[0].score
    scores.append(score)

    # anomaly detection
    if score < 0.8:
        anomaly_x.append(i)
        anomaly_y.append(score)
        st.error("Anomaly Detected!")

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        y=scores,
        mode='lines',
        name='Similarity Score'
    ))

    fig.add_trace(go.Scatter(
        x=anomaly_x,
        y=anomaly_y,
        mode='markers',
        marker=dict(color='red', size=10),
        name='Anomaly'
    ))

    # threshold
    fig.add_hline(y=0.8, line_dash="dash", line_color="red")

    fig.update_layout(
        title="Live Sensor Anomaly Detection",
        xaxis_title="Time",
        yaxis_title="Similarity Score"
    )

    chart.plotly_chart(fig, use_container_width=True)

    time.sleep(0.5)
