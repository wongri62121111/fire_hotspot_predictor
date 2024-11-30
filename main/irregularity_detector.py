import os
import csv


def detect_irregularities(file_path='main/data/wildfire_sensors.csv'):
    """
    Detect irregularities in sensor data based on predefined thresholds.

    Args:
        file_path (str): The path to the CSV file containing sensor data.
    """
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} does not exist.")
        return

    # Define thresholds for irregularities
    thresholds = {
        'temperature': (20, 45),  # Example: normal range is 20-45°C
        'humidity': (15, 85),    # Example: normal range is 15-85%
        'smoke_level': (0, 70),  # Example: normal range is 0-70 (arbitrary scale)
    }

    irregularities = []

    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Check each row for irregularities
                irregular_row = {}
                for key, (low, high) in thresholds.items():
                    value = float(row[key])
                    if value < low or value > high:
                        irregular_row[key] = value
                if irregular_row:
                    irregular_row['timestamp'] = row['timestamp']
                    irregularities.append(irregular_row)

    except Exception as e:
        print(f"Error reading file: {e}")
        return

    if irregularities:
        print("\nIrregularities detected:")
        for irregularity in irregularities:
            print(irregularity)
    else:
        print("\nNo irregularities detected.")


if __name__ == "__main__":
    # Specify the file path to the data
    file_path = 'main/data/wildfire_sensors.csv'
    detect_irregularities(file_path)
