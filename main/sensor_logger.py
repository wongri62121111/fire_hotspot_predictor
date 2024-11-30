import os
import csv
import random
from datetime import datetime
import time


def generate_sensor_data():
    """
    Generate mock sensor data for temperature, humidity, and smoke levels.
    Returns:
        dict: A dictionary containing sensor data with a timestamp.
    """
    return {
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'temperature': round(random.uniform(20, 50), 2),
        'humidity': round(random.uniform(10, 90), 2),
        'smoke_level': round(random.uniform(0, 100), 2),
    }


def log_sensor_data(filename='data/wildfire_sensors.csv'):
    """
    Log generated sensor data into a CSV file.

    Args:
        filename (str): The file path where data will be logged.
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    data = generate_sensor_data()

    file_exists = os.path.isfile(filename)

    try:
        with open(filename, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data.keys())
            if not file_exists:
                writer.writeheader()  # Write header if the file is new
            writer.writerow(data)
    except PermissionError:
        print("Error: Cannot write to file. Check file permissions.")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")


class SensorLogger:
    def __init__(self, log_interval=5, log_file='main/data/wildfire_sensors.csv'):
        """
        Initialize the Sensor Logger.

        Args:
            log_interval (int): Logging interval in seconds.
            log_file (str): File path for logging sensor data.
        """
        self.log_interval = log_interval
        self.log_file = log_file

    def start_logging(self):
        """
        Start logging sensor data at regular intervals.
        """
        print("Starting sensor logging...")
        try:
            while True:
                log_sensor_data(self.log_file)
                print(f"Logged data to {self.log_file}")
                time.sleep(self.log_interval)
        except KeyboardInterrupt:
            print("\nLogging stopped by user.")


if __name__ == "__main__":
    logger = SensorLogger(log_interval=5)  # Log every 5 seconds
    logger.start_logging()
