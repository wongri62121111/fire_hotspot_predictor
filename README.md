# Wildfire Prediction System  

This project aims to analyze historical wildfire data to predict potential future wildfire locations using **Python**. By leveraging data on past wildfire occurrences and environmental conditions, the system estimates fire risk across different regions.  

## Project Structure  

The project is divided into several modules for clarity and modularity:  

1. **Data Input Module**: Handles data collection and preprocessing from CSV files or other sources using libraries like `pandas`.  
2. **Feature Extraction Module**: Processes and extracts important features like temperature, humidity, wind speed, and vegetation type.  
3. **Prediction Algorithm Module**: Predicts future wildfire risks using machine learning models such as random forests or logistic regression.  
4. **Output Module**: Outputs predictions in a readable format and generates visualizations such as maps.  

---

## Prerequisites  

To run this project, you need:  
- Python 3.8 or higher.  
- Libraries: `pandas`, `numpy`, `scikit-learn`, `matplotlib`, and `folium`.  
- Basic understanding of Python programming and machine learning.  

---

## Data Collection  

Historical wildfire data is essential for this project. Suggested sources:  
- [NASA's Fire Information for Resource Management System (FIRMS)](https://firms.modaps.eosdis.nasa.gov/)  
- [US Forest Service - Fire Data](https://data.fs.usda.gov/geodata/)  
- National and regional meteorological services for climate data.  

---

## File Structure  

- **src/**: Contains all source code files.  
  - **data_input.py**: Functions for reading and preprocessing data from CSV files.  
  - **feature_extraction.py**: Functions to extract and analyze key features.  
  - **prediction.py**: Implements wildfire risk prediction using machine learning models.  
  - **output.py**: Handles result display and visualization.  
- **data/**: Sample datasets for testing (not included due to size, links provided in `resources.txt`).  
- **README.md**: Documentation for the project.  
- **requirements.txt**: Lists Python dependencies for easy installation.  

---

## Usage  

1. **Clone the Repository**:  
   ```bash  
   git clone https://github.com/yourusername/wildfire-prediction.git  
   cd wildfire-prediction  
   ```  

2. **Install Dependencies**:  
   ```bash  
   pip install -r requirements.txt  
   ```  

3. **Run the Project**:  
   ```bash  
   python src/main.py  
   ```  

4. **Provide Data**: Place your CSV files in the `data/` folder and update the file paths in the `data_input.py` script if necessary.  

---

## Sample Code Structure  

### **Data Input Module**  
Reads historical wildfire data from CSV files using `pandas` and handles missing values.  

### **Feature Extraction Module**  
Calculates averages, identifies high-risk areas, and other feature-based calculations.  

### **Prediction Algorithm Module**  
Uses machine learning models (e.g., random forests) to predict wildfire risk based on historical patterns.  

### **Output Module**  
Generates maps using `folium` and prints predictions to the console or saves them to a file.  

---

## Contributing  

Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request with your proposed changes.  

---

## License  

This project is open-source and available under the MIT License.  

---

## Resources and Additional Documentation  

See `resources.txt` for recommended datasets and additional reading material on fire risk prediction methods.  

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
1. **Python Libraries**:  
   - `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `folium`  
   - Description: For data preprocessing, analysis, machine learning, and visualization.  

2. **GIS Tools (for Visualization)**:  
   - `geopandas` (optional): Advanced mapping and geographic analysis.  

3. **APIs**:  
   - OpenWeatherMap API: Fetch real-time weather data for dynamic predictions.  

### Additional Reading  
1. **Fire Behavior and Prediction Models**:  
   - *Introduction to Wildland Fire Behavior (NWCG)* - Overview of how wildfires spread and conditions affecting fire behavior.  

2. **Statistical Analysis and Prediction**:  
   - *Statistical Methods for Fire Risk Prediction* - Guides on using regression, clustering, and other statistical models.  

3. **Machine Learning Techniques**:  
   - *Hands-On Machine Learning with Scikit-Learn* - For beginners looking to implement ML algorithms for fire prediction.  

4. **Weather and Climate Factors**:  
   - *Understanding Climate Data for Fire Risk Prediction* - Information on temperature, humidity, and other climate factors affecting fire risk.  
```  
