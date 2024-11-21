from sklearn.ensemble import IsolationForest
import pandas as pd

# Load dataset
data = pd.read_csv("solar_data.csv")
features = data[["voltage", "current", "temperature"]]

# Train isolation forest
model = IsolationForest(contamination=0.1)
model.fit(features)

# Predict anomalies
data["anomaly"] = model.predict(features)
print(data[data["anomaly"] == -1])  # Anomalies
