import matplotlib.pyplot as plt

plt.plot(data["timestamp"], data["voltage"], label="Voltage")
plt.plot(data["timestamp"], data["current"], label="Current")
plt.scatter(data["timestamp"], data["anomaly"], label="Anomalies", color="red")
plt.legend()
plt.show()
