# Wildfire Monitoring System

## Overview

A real-time monitoring system that collects and visualizes environmental data for wildfire detection, featuring sensor simulation, data logging, anomaly detection, and both matplotlib and web-based visualization interfaces.

## Features

- Real-time sensor data simulation (temperature, humidity, smoke levels)
- Automated data logging to CSV
- Anomaly detection with configurable thresholds
- Two visualization options:
  - Matplotlib-based real-time graphs
  - Web interface with live updates

## Prerequisites

- Python 3.8+
- pip

## Installation

```bash
git clone https://github.com/wongri62121111/wildfire-sensor-logger.git
cd wildfire-sensor-logger
pip install -r requirements.txt
```

## Usage

### Start with Matplotlib Visualization
```bash
python main-matplot.py
```

### Start with Web Interface
```bash
python main-webpage.py
```

Optional arguments:
- `--interval`: Logging interval in seconds (default: 5)
- `--data-file`: Custom data file path

## Project Structure

```
data/                          # Sensor data 
└── wildfire_sensors.csv
main/
├── irregularity_detector.py   # Anomaly detection logic
├── sensor_logger.py           # Sensor data generation and logging
├── sensor_visualize.py        # Matplotlib visualization
├── main-matplot.py            # Matplotlib interface launcher
├── main-webpage.py            # Web interface launcher
├── templates/                 # Web interface templates
        └── index.html
```

## Component Details

### Sensor Logger
- Generates mock sensor data
- Configurable logging intervals
- CSV storage with timestamps

### Irregularity Detector
Default thresholds:
- Temperature: 20-45°C
- Humidity: 15-85%
- Smoke Level: 0-70

### Visualizations
- Matplotlib: Real-time line graphs
- Web Interface: Live dashboard with current readings and alerts

## Configuration

Modify thresholds in `irregularity_detector.py`:
```python
thresholds = {
    'temperature': (20, 45),
    'humidity': (15, 85),
    'smoke_level': (0, 70)
}
```

## Contribution
1.Abdallah Salem
2.Richard Wong

