import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor, IsolationForest
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, classification_report
import matplotlib.pyplot as plt

data = pd.read_csv("solar_panel_data.csv")

X = data[["Voltage (V)", "Current (mA)"]]
y = data["Voltage (V)"]  #Using Voltage as both feature and target for anomaly detection and prediction

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model 1: Random Forest Regression for Performance Prediction
print("Training Random Forest Regressor...")
regressor = RandomForestRegressor(n_estimators=100, random_state=42)
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error (MSE): {mse}")

plt.scatter(y_test, y_pred, alpha=0.7)
plt.xlabel("Actual Voltage (V)")
plt.ylabel("Predicted Voltage (V)")
plt.title("Actual vs Predicted Voltage")
plt.show()

# Model 2: Isolation Forest for Anomaly Detection
print("Training Isolation Forest for Anomaly Detection...")
iso_forest = IsolationForest(contamination=0.1, random_state=42)
iso_forest.fit(X_train)

anomalies = iso_forest.predict(X_test)
X_test["Anomaly"] = anomalies

print("Anomaly Detection Results:")
print(X_test)

plt.scatter(X_test["Voltage (V)"], X_test["Current (mA)"], c=X_test["Anomaly"], cmap="coolwarm", alpha=0.7)
plt.xlabel("Voltage (V)")
plt.ylabel("Current (mA)")
plt.title("Anomaly Detection (Normal vs. Anomalous)")
plt.show()
