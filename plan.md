Here's the implementation of the Wildfire Sensor Logger in Python based on your outlined plan:

1. Setting up the Python Script

File: sensor_logger.py

import os
import csv
import random
from datetime import datetime
import time

# Function to simulate sensor data
def generate_sensor_data():
    """
    Simulates sensor readings for temperature, humidity, and smoke level.
    Returns a dictionary with sensor data and timestamp.
    """
    data = {
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'temperature': round(random.uniform(20, 50), 2),  # in Celsius
        'humidity': round(random.uniform(10, 90), 2),     # in percentage
        'smoke_level': round(random.uniform(0, 100), 2)   # arbitrary scale
    }
    return data

# Function to log data into a CSV file
def log_sensor_data(filename='data/wildfire_sensors.csv'):
    """
    Logs generated sensor data into a CSV file.
    Creates the file and writes headers if it doesn't exist.
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)  # Ensure data directory exists
    data = generate_sensor_data()

    try:
        # Write data to CSV
        file_exists = os.path.isfile(filename)
        with open(filename, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data.keys())
            if not file_exists:  # Write header if file is new
                writer.writeheader()
            writer.writerow(data)
        print(f"Logged data: {data}")
    except Exception as e:
        print(f"Error logging data: {e}")

# Main function to simulate periodic logging
def start_logging(log_interval=5):
    """
    Starts the logging process with a specified interval (in seconds).
    """
    print("Starting Wildfire Sensor Logger...")
    print(f"Logging every {log_interval} seconds. Press Ctrl+C to stop.")
    try:
        while True:
            log_sensor_data()
            time.sleep(log_interval)
    except KeyboardInterrupt:
        print("\nLogging stopped. Goodbye!")

if __name__ == "__main__":
    # Configure log interval here (default 5 seconds)
    start_logging(log_interval=5)


---

2. Project Directory Setup

Create the following structure:

wildfire-sensor-logger/
│
├── sensor_logger.py         # Main script
├── README.md                # Documentation
├── data/                    # Directory for storing logged CSV files
└── requirements.txt         # (Empty for now, or specify dependencies if needed)


---

3. Usage

1. Run the Script:

python sensor_logger.py


2. Output Example:

Starting Wildfire Sensor Logger...
Logging every 5 seconds. Press Ctrl+C to stop.
Logged data: {'timestamp': '2024-11-28 12:34:56', 'temperature': 35.21, 'humidity': 48.65, 'smoke_level': 23.18}
Logged data: {'timestamp': '2024-11-28 12:35:01', 'temperature': 40.12, 'humidity': 30.45, 'smoke_level': 12.09}


3. Check the data/wildfire_sensors.csv file for the logged data.




---

4. Enhancements and Features

Logging Configuration: Add the ability to configure logging intervals or customize file paths.

Error Handling: Ensure robust handling for potential file or permission errors.

Future Extensions:

Real sensor integration using libraries like Adafruit for IoT sensors.

Data visualization using tools like matplotlib or pandas.




---

Example Logged Data in CSV

timestamp,temperature,humidity,smoke_level
2024-11-28 12:34:56,35.21,48.65,23.18
2024-11-28 12:35:01,40.12,30.45,12.09

This implementation sets a foundation for a wildfire monitoring tool while being simple enough to extend further. Let me know if you want to add more features!

