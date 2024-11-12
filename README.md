# Wildfire Prediction System

This project aims to analyze historical wildfire data to predict potential future wildfire locations using the C programming language. By leveraging data on past wildfire occurrences and environmental conditions, the system estimates fire risk across different regions. 

## Project Structure

The project is divided into several modules for clarity and modularity:

1. **Data Input Module**: Handles data collection and preprocessing from CSV files or other sources.
2. **Feature Extraction Module**: Processes and extracts important features like temperature, humidity, wind speed, and vegetation type.
3. **Prediction Algorithm Module**: Predicts future wildfire risks using thresholds or statistical analysis of historical data.
4. **Output Module**: Outputs predictions in a readable format or generates simple visualizations.

## Prerequisites

To compile and run this project, you need:
- GCC or another C compiler.
- Basic understanding of C programming, file handling, and basic statistical modeling.

## Data Collection

Historical wildfire data is essential for this project. Suggested sources:
- [NASA's Fire Information for Resource Management System (FIRMS)](https://firms.modaps.eosdis.nasa.gov/)
- [US Forest Service - Fire Data](https://data.fs.usda.gov/geodata/)
- National and regional meteorological services for climate data.

## File Structure

- **src/**: Contains all source code files.
  - **main.c**: Main entry point for the application.
  - **data_input.c**: Functions for reading and preprocessing data from CSV files.
  - **feature_extraction.c**: Functions to extract and analyze key features.
  - **prediction.c**: Implements the wildfire risk prediction logic.
  - **output.c**: Handles result display and storage.
- **include/**: Header files for modular design.
- **data/**: Sample datasets for testing (not included due to size, link provided in resources.txt).
- **README.md**: Documentation for the project.
- **resources.txt**: List of recommended resources and data sources.
- **Makefile**: To build the project easily.

## Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/wildfire-prediction.git
   cd wildfire-prediction

2. Compile the Project:

make


3. Run the Project:

./wildfire_prediction


4. Provide Data: Make sure to place your CSV files in the data/ folder and update the file path in the source code if necessary.



Sample Code Structure

Here is an overview of how each module works:

Data Input Module: Reads historical wildfire data from CSV files and stores it in a struct.

Feature Extraction Module: Calculates averages, identifies high-risk areas, and other feature-based calculations.

Prediction Algorithm Module: Uses predefined thresholds or statistical techniques to assess fire risk.

Output Module: Prints locations with high fire risk in a user-friendly format.


Contributing

Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request with your proposed changes.

License

This project is open-source and available under the MIT License.

Resources and Additional Documentation

See resources.txt for recommended datasets and additional reading material on fire risk prediction methods.

---

### resources.txt

```plaintext
# Wildfire Prediction Project Resources

### Recommended Datasets
1. **NASA FIRMS** - Fire Information for Resource Management System
   - Link: https://firms.modaps.eosdis.nasa.gov/
   - Description: Provides near-real-time active fire data from MODIS and VIIRS satellites.

2. **US Forest Service - Fire Data**
   - Link: https://data.fs.usda.gov/geodata/
   - Description: Fire occurrence data, including location, time, and environmental conditions.

3. **NOAA Climate Data** - National Oceanic and Atmospheric Administration
   - Link: https://www.ncdc.noaa.gov/cdo-web/
   - Description: Provides climate data that can be useful in understanding fire risk factors.

4. **Global Fire Emissions Database (GFED)**
   - Link: https://www.globalfiredata.org/
   - Description: Provides data on fire emissions, useful for analysis of fire causes and risk.

5. **National and Regional Weather Services**
   - Local sources like national weather bureaus for real-time climate information.

### Suggested Tools and Libraries
1. **GCC** - GNU Compiler Collection
   - Command-line C compiler.
   
2. **GNU Make**
   - Automates the build process for easier project compilation.

3. **CSV Libraries in C**:
   - `libcsv` (optional): A C library to facilitate CSV reading and parsing.

4. **libsvm** - Library for Support Vector Machines (Optional)
   - Link: https://www.csie.ntu.edu.tw/~cjlin/libsvm/
   - Description: A C-compatible library for basic machine learning models (SVMs).

5. **GIS Tools (for Visualization)**
   - `QGIS` (optional): Open-source tool for mapping and visualizing prediction data.
   - `Matplotlib (Python)` (optional): For generating simple maps if data is processed in Python and visualized outside of C.

### Additional Reading
1. **Fire Behavior and Prediction Models**:
   - *Introduction to Wildland Fire Behavior (NWCG)* - Overview of how wildfires spread and conditions affecting fire behavior.
   
2. **Statistical Analysis and Prediction**:
   - *Statistical Analysis in C* - Guides on using linear regression, clustering, and statistical models in C.
   
3. **Weather and Climate Factors**:
   - *Climate and Weather Data for Fire Prediction* - Information on temperature, humidity, and other climate factors affecting fire risk.

4. **Machine Learning in C (for Advanced Users)**:
   - *Machine Learning Algorithms in C* - Guide on implementing regression, clustering, and other ML techniques manually in C.
