import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
import os

class SensorVisualizer:
    def __init__(self, data_file='data/wildfire_sensors.csv'):
        self.data_file = data_file
        self.fig, (self.ax1, self.ax2, self.ax3, self.ax4, self.ax5, self.ax6) = plt.subplots(6, 1, figsize=(10, 12))
        self.max_points = 50
        
        # Initialize empty data
        self.timestamps = []
        self.temps = []
        self.humidities = []
        self.smoke_levels = []
        self.windspeed = []
        self.precipitation = []
        self.soil_moisture = []
        
        # Set up plots
        self.temp_line, = self.ax1.plot([], [], 'r-', label='Temperature')
        self.humidity_line, = self.ax2.plot([], [], 'b-', label='Humidity')
        self.smoke_line, = self.ax3.plot([], [], 'k-', label='Smoke Level')
        self.windspeed_line, = self.ax4.plot([], [], 'm-', label='Windspeed')
        self.precipitation_line, = self.ax5.plot([], [], 'c-', label='Precipitation')
        self.soil_moisture_line, = self.ax6.plot([], [], 'y-', label='Soil Moisture')
        # Configure axes
        self.setup_axes()
        
    def setup_axes(self):
        self.ax1.set_ylabel('Temperature (°C)')
        self.ax2.set_ylabel('Humidity (%)')
        self.ax3.set_ylabel('Smoke Level')
        self.ax4.set_ylabel('Windspeed (m/s)')
        self.ax5.set_ylabel('Precipitation (mm/h)')
        self.ax6.set_ylabel('Soil Moisture (%)')
        
        for ax in [self.ax1, self.ax2, self.ax3, self.ax4, self.ax5, self.ax6]:
            ax.grid(True)
            ax.legend(loc='upper left')
        
        plt.tight_layout()
    
    def update(self, frame):
        if os.path.exists(self.data_file):
            try:
                df = pd.read_csv(self.data_file)
                latest_data = df.tail(self.max_points)
                
                self.timestamps = latest_data['timestamp'].tolist()
                self.temps = latest_data['temperature'].tolist()
                self.humidities = latest_data['humidity'].tolist()
                self.smoke_levels = latest_data['smoke_level'].tolist()
                self.windspeed = latest_data['windspeed'].tolist()
                self.precipitation = latest_data['precipitation'].tolist()
                self.soil_moisture = latest_data['soil_moisture'].tolist()
                
                # Update lines
                x_range = range(len(self.timestamps))
                self.temp_line.set_data(x_range, self.temps)
                self.humidity_line.set_data(x_range, self.humidities)
                self.smoke_line.set_data(x_range, self.smoke_levels)
                self.windspeed_line.set_data(x_range, self.windspeed)
                self.precipitation_line.set_data(x_range, self.precipitation)
                self.soil_moisture_line.set_data(x_range, self.soil_moisture)
                
                # Update axis limits
                for ax in [self.ax1, self.ax2, self.ax3, self.ax4, self.ax5, self.ax6]:
                    ax.relim()
                    ax.autoscale_view()
                    ax.set_xlim(0, len(self.timestamps))
                
            except pd.errors.EmptyDataError:
                pass
            
        return self.temp_line, self.humidity_line, self.smoke_line, self.windspeed_line, self.precipitation_line, self.soil_moisture_line

    def start_visualization(self):
        ani = FuncAnimation(self.fig, self.update, interval=1000)
        plt.show()