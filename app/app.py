from flask import Flask, render_template, jsonify
import csv
import os
import smtplib

app = Flask(__name__)

# Filepath for sensor data
DATA_FILE = os.path.abspath("data/wildfire_sensors.csv")  # Adjust path as needed

# Thresholds for anomaly detection
THRESHOLDS = {
    "temperature": (20, 45),
    "humidity": (15, 85),
    "smoke_level": (0, 70),
}

def load_data():
    """
    Load sensor data from the CSV file.
    Returns:
        list: A list of dictionaries representing sensor data.
    """
    if not os.path.exists(DATA_FILE):
        print(f"Data file not found: {DATA_FILE}")
        return []
    
    try:
        with open(DATA_FILE, "r") as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
            print(f"Loaded data: {data}")  # Debugging
            return data
    except Exception as e:
        print(f"Error reading data file: {e}")
        return []

print(f"Looking for data file at: {DATA_FILE}")

def detect_anomalies(data):
    """
    Detect anomalies in sensor data based on predefined thresholds.
    Args:
        data (list): Sensor data records.
    Returns:
        list: A list of records with anomalies and explanations.
    """
    anomalies = []
    for row in data:
        anomaly = {}
        explanation = []
        for key, (low, high) in THRESHOLDS.items():
            try:
                value = float(row[key])
                if value < low or value > high:
                    anomaly[key] = value
                    if value < low:
                        explanation.append(f"{key.capitalize()} is below the minimum threshold of {low}.")
                    else:
                        explanation.append(f"{key.capitalize()} exceeds the maximum threshold of {high}.")
            except ValueError:
                print(f"Invalid value for {key}: {row[key]}")
        if anomaly:
            anomaly["timestamp"] = row["timestamp"]
            anomaly["explanation"] = " ".join(explanation)
            anomalies.append(anomaly)
    return anomalies


@app.route("/")
def index():
    """
    Render the dashboard with sensor data.
    """
    data = load_data()
    print(f"Data passed to template: {data}")  # Debugging
    anomalies = detect_anomalies(data)
    return render_template("index.html", data=data, anomalies=anomalies)

@app.route("/api/data")
def api_data():
    """
    API endpoint for fetching sensor data.
    """
    data = load_data()
    return jsonify(data)

@app.route("/api/anomalies")
def api_anomalies():
    """
    API endpoint for fetching anomalies.
    """
    data = load_data()
    anomalies = detect_anomalies(data)
    return jsonify(anomalies)



if __name__ == "__main__":
    app.run(debug=True)
