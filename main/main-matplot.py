import threading
import signal
import sys
from sensor_logger import SensorLogger
from irregularity_detector import detect_irregularities
from sensor_visualize import SensorVisualizer

class WildfireMonitoringSystem:
    def __init__(self, log_interval=5, data_file='data/wildfire_sensors.csv'):
        self.data_file = data_file
        self.logger = SensorLogger(log_interval, data_file)
        self.visualizer = SensorVisualizer(data_file)
        self.running = True

    def start(self):
        signal.signal(signal.SIGINT, self.signal_handler)
        
        logger_thread = threading.Thread(target=self.logger.start_logging)
        logger_thread.daemon = True
        logger_thread.start()

        detector_thread = threading.Thread(target=self.run_detector)
        detector_thread.daemon = True
        detector_thread.start()

        self.visualizer.start_visualization()

    def run_detector(self):
        while self.running:
            detect_irregularities(self.data_file)
            import time
            time.sleep(5)

    def signal_handler(self, signum, frame):
        print("\nShutting down monitoring system...")
        self.running = False
        sys.exit(0)

if __name__ == "__main__":
    system = WildfireMonitoringSystem()
    system.start()