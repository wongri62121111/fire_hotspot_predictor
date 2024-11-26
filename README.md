# Wildfire Sensor Logger

## Project Overview

The Wildfire Sensor Logger is a Python project designed to simulate and log sensor data related to wildfire detection. This project generates mock sensor readings for temperature, humidity, and smoke levels, providing a foundational tool for understanding environmental monitoring in wildfire-prone areas.

## Project Goals

- Simulate realistic sensor data for wildfire monitoring
- Create a robust logging mechanism for sensor readings
- Provide a simple, extensible framework for environmental data collection

## Prerequisites

- Python 3.8+
- Basic understanding of Python programming
- Recommended: Virtual environment setup

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

3. Install dependencies (if any are added later):
   ```bash
   pip install -r requirements.txt
   ```

## Project Structure

```
wildfire-sensor-logger/
│
├── sensor_logger.py         # Main script for data generation and logging
├── README.md                # Project documentation
├── data/                    # Directory for storing logged CSV files
└── requirements.txt         # Project dependencies
```

## Detailed Project Milestones and Implementation Guide

### Milestone 1: Project Setup and Basic Data Generation (Day 1)
**Objectives:**
- Set up Python development environment
- Create initial project structure
- Implement basic sensor data generation function

**Step-by-Step Implementation:**
1. Create project directory
2. Set up virtual environment
3. Create `sensor_logger.py`
4. Implement `generate_sensor_data()` function
5. Add basic error handling
6. Test data generation

**Code Checkpoint:**
```python
def generate_sensor_data():
    # Ensure random data generation works correctly
    data = {
        'timestamp': datetime.now(),
        'temperature': round(random.uniform(20, 50), 2),
        'humidity': round(random.uniform(10, 90), 2),
        'smoke_level': round(random.uniform(0, 100), 2)
    }
    print("Data generation test:", data)
```

### Milestone 2: CSV Logging Mechanism (Days 2-3)
**Objectives:**
- Implement robust CSV logging
- Handle file creation and appending
- Add data validation

**Step-by-Step Implementation:**
1. Create `log_sensor_data()` function
2. Implement file handling with `csv` module
3. Add error handling for file operations
4. Create `data/` directory for logs
5. Implement logging with timestamps

**Code Checkpoint:**
```python
def log_sensor_data(filename='data/wildfire_sensors.csv'):
    # Ensure proper file handling and logging
    os.makedirs('data', exist_ok=True)
    data = generate_sensor_data()
    
    # Implement file logging with comprehensive error handling
    try:
        with open(filename, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data.keys())
            writer.writerow(data)
    except PermissionError:
        print("Error: Cannot write to file. Check permissions.")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
```

### Milestone 3: Enhanced Functionality (Day 4)
**Objectives:**
- Add configuration options
- Implement logging intervals
- Create basic data validation

**Potential Enhancements:**
- Add configurable sensor ranges
- Implement logging frequency control
- Add basic data validation checks

**Code Checkpoint:**
```python
class SensorLogger:
    def __init__(self, 
                 log_interval=5,  # minutes
                 data_dir='data',
                 max_log_files=10):
        self.log_interval = log_interval
        self.data_dir = data_dir
        self.max_log_files = max_log_files
```

### Milestone 4: Testing and Documentation (Days 5-7)
**Objectives:**
- Write unit tests
- Create comprehensive documentation
- Prepare for potential extensions

**Tasks:**
1. Write unit tests for data generation
2. Create docstrings for all functions
3. Add logging configuration options
4. Prepare README with usage instructions
5. Consider potential future improvements

## Usage

Run the script directly:
```bash
python sensor_logger.py
```

## Future Improvements
- Add real sensor integration
- Implement advanced data validation
- Create data visualization tools
- Support multiple sensor types

## Contributing
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License
[Choose an appropriate open-source license]

## Contact
[Your contact information]
```

## Learning Outcomes

By completing this project, you will gain experience in:
- Python programming
- File I/O operations
- CSV handling
- Basic data simulation
- Project structure and documentation
- Error handling
- Configuration management

## Troubleshooting

- Ensure Python 3.8+ is installed
- Check file permissions when logging data
- Verify virtual environment activation
- Consult Python documentation for any module-specific issues