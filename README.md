# Wildfire Sensor Logger

## Project Overview

The Wildfire Sensor Logger is a Python project designed to simulate and log sensor data related to wildfire detection. It includes a web-based dashboard that displays sensor data and highlights anomalies. The project generates mock sensor readings for temperature, humidity, and smoke levels, and provides an accessible framework for monitoring environmental data.

## Project Goals

- Simulate realistic sensor data for wildfire monitoring.
- Create a robust logging mechanism for sensor readings.
- Provide a web application to display sensor data and anomalies.
- Highlight anomalous readings with explanations on the dashboard.

## Prerequisites

- Python 3.8+
- Basic understanding of Python programming.
- Recommended: Virtual environment setup.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/wildfire-sensor-logger.git
   cd wildfire-sensor-logger
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Project Structure

```
wildfire-sensor-logger/
│
├── modules/                     # Core functionality modules
│   ├── sensor_logger.py         # Script for data generation and logging
│   ├── irregularity_detector.py # Script to detect anomalies
│   ├── notification_alert.py    # Script for email/SMS alerts
│
├── app/                         # Web application
│   ├── templates/               # HTML templates for the dashboard
│   │   └── index.html
│   ├── static/                  # Static files like CSS and JS
│   │   └── style.css
│   └── app.py                   # Flask application entry point
│
├── data/                        # Directory for storing logged CSV files
│   └── wildfire_sensors.csv
│
├── README.md                    # Project documentation
├── requirements.txt             # Python dependencies
└── setup.py                     # Script to automate installation
```

## Web Dashboard Features

- **Displays Sensor Data**:

  - Presents logged temperature, humidity, and smoke levels in a table.

- **Highlights Anomalies**:

  - Anomalous readings are highlighted directly in the table.
  - Includes a detailed explanation for each anomaly.

- **Human-Readable Anomaly Explanations**:

  - Lists anomalies and reasons (e.g., "Temperature exceeds the maximum threshold of 45°C").

## Setup Instructions

1. Run the setup script to install dependencies and set up the project structure:

   ```bash
   python setup.py
   ```

2. Start the Flask web application:

   ```bash
   python app/app.py
   ```

3. Open the dashboard in a browser:

   ```
   http://127.0.0.1:5000
   ```

## Requirements

The project uses the following Python libraries:

- `flask`: For the web application.
- `twilio`: For SMS notifications.
- `csv`: For handling sensor data files.
- `smtplib`: For email notifications.

## Usage

### 1. Logging Sensor Data

Run the logger script to generate and log sensor data:

```bash
python modules/sensor_logger.py
```

The data will be stored in `data/wildfire_sensors.csv`.

### 2. View Sensor Data and Anomalies

Start the web app and navigate to the dashboard to view data and anomalies:

```bash
python app/app.py
```

### 3. Customize Thresholds

Thresholds for anomalies can be adjusted in `app.py`:

```python
THRESHOLDS = {
    "temperature": (20, 45),
    "humidity": (15, 85),
    "smoke_level": (0, 70),
}
```

## Future Improvements

- Add real sensor integration.
- Enable real-time data visualization.
- Implement user authentication for restricted access.
- Add support for exporting data to other formats (e.g., JSON, Excel).

## Contributing

1. Fork the repository.
2. Create your feature branch.
3. Commit your changes.
4. Push to the branch.
5. Create a new Pull Request.

## License

[Choose an appropriate open-source license]

## Contact

[Your contact information]

Richard Wong @ Penn State University

Abdallah Salem @ Penn State University

