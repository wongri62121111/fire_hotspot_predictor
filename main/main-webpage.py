import argparse
import threading
import signal
import sys
import time
import webbrowser
from sensor_logger import SensorLogger
from irregularity_detector import detect_irregularities
from sensor_visualize import SensorVisualizer
from flask import Flask, render_template, jsonify
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO

app = Flask(__name__)
data_file = 'data/wildfire_sensors.csv'

class WildfireMonitoringSystem:
    def __init__(self, log_interval=5, data_file='data/wildfire_sensors.csv'):
        self.data_file = data_file
        self.logger = SensorLogger(log_interval, data_file)
        self.visualizer = SensorVisualizer(data_file)
        self.running = True
        self.irregularities = []

    def start(self):
        signal.signal(signal.SIGINT, self.signal_handler)
        
        logger_thread = threading.Thread(target=self.logger.start_logging)
        logger_thread.daemon = True
        logger_thread.start()

        detector_thread = threading.Thread(target=self.run_detector)
        detector_thread.daemon = True
        detector_thread.start()

        # Open web browser
        webbrowser.open('http://localhost:5000')

        # Start Flask server
        app.run(host='0.0.0.0', port=5000)

    def run_detector(self):
        while self.running:
            self.irregularities = self.check_irregularities()
            time.sleep(5)

    def check_irregularities(self):
        thresholds = {
            'temperature': (20, 45),
            'humidity': (15, 85),
            'smoke_level': (0, 70),
            'windspeed': (0, 50),
            'precipitation': (0, 10),
            'soil_moisture': (10, 60)
        }
        
        irregularities = []
        try:
            df = pd.read_csv(self.data_file)
            latest = df.iloc[-1].to_dict()
            
            for key, (low, high) in thresholds.items():
                value = float(latest[key])
                if value < low or value > high:
                    irregularities.append({
                        'parameter': key,
                        'value': value,
                        'timestamp': latest['timestamp']
                    })
        except Exception as e:
            print(f"Error checking irregularities: {e}")
        
        return irregularities

    def signal_handler(self, signum, frame):
        print("\nShutting down monitoring system...")
        self.running = False
        sys.exit(0)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data')
def get_data():
    try:
        df = pd.read_csv(data_file)
        latest = df.iloc[-1].to_dict()
        history = df.tail(10).to_dict('records')  # Get last 10 records
        history.reverse()  # Show newest first
        

        
        return jsonify({
            'sensor_data': latest,
            'irregularities': system.irregularities,
            'history': history
        })
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/graph')
def plot_graph():
    try:
        df = pd.read_csv(data_file)
        fig, ax = plt.subplots(figsize=(10, 5))
        df.plot(x='timestamp', y=['temperature', 'humidity', 'smoke_level', 'windspeed', 'precipitation', 'soil_moisture'], ax=ax)
        plt.xticks(rotation=45)
        plt.tight_layout()

        buf = BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)
        return Response(buf, mimetype='image/png')
    except Exception as e:
        return jsonify({'error': str(e)})

def main():
    global system
    parser = argparse.ArgumentParser(description='Wildfire Monitoring System')
    parser.add_argument('--interval', type=int, default=5,
                      help='Logging interval in seconds')
    parser.add_argument('--data-file', type=str, default='data/wildfire_sensors.csv',
                      help='Path to data file')
    
    args = parser.parse_args()
    
    global data_file
    data_file = args.data_file
    
    system = WildfireMonitoringSystem(args.interval, args.data_file)
    system.start()

if __name__ == "__main__":
    main()