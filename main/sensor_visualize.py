import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
import os

class SensorVisualizer:
    def __init__(self, data_file='data/wildfire_sensors.csv'):
        self.data_file = data_file
        self.fig, (self.ax1, self.ax2, self.ax3) = plt.subplots(3, 1, figsize=(10, 12))
        self.max_points = 50
        
        # Initialize empty data
        self.timestamps = []
        self.temps = []
        self.humidities = []
        self.smoke_levels = []
        
        # Set up plots
        self.temp_line, = self.ax1.plot([], [], 'r-', label='Temperature')
        self.humidity_line, = self.ax2.plot([], [], 'b-', label='Humidity')
        self.smoke_line, = self.ax3.plot([], [], 'g-', label='Smoke Level')
        
        # Configure axes
        self.setup_axes()
        
    def setup_axes(self):
        self.ax1.set_ylabel('Temperature (°C)')
        self.ax2.set_ylabel('Humidity (%)')
        self.ax3.set_ylabel('Smoke Level')
        
        for ax in [self.ax1, self.ax2, self.ax3]:
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
                
                # Update lines
                x_range = range(len(self.timestamps))
                self.temp_line.set_data(x_range, self.temps)
                self.humidity_line.set_data(x_range, self.humidities)
                self.smoke_line.set_data(x_range, self.smoke_levels)
                
                # Update axis limits
                for ax in [self.ax1, self.ax2, self.ax3]:
                    ax.relim()
                    ax.autoscale_view()
                    ax.set_xlim(0, len(self.timestamps))
                
            except pd.errors.EmptyDataError:
                pass
            
        return self.temp_line, self.humidity_line, self.smoke_line

    def start_visualization(self):
        ani = FuncAnimation(self.fig, self.update, interval=1000)
        plt.show()