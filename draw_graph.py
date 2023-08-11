import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QScrollArea
import numpy as np
import pandas as pd
import matplotlib as mlp
import matplotlib.pyplot as plt
import tensorflow as tf
from geopy.geocoders import Nominatim as Nom
import requests
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        

    

    def eightHourTemperatures(self,dates, temps):
        self.ax.plot(dates[0:7:1], temps[0:7:1])
        self.ax.set_xlabel('Dates')
        self.ax.set_ylabel('Temperatures (\u00b0C)')
        self.ax.set_title('Eight Hour Forecast')
        self.ax.grid(True)
        self.canvas.draw()

            

    def fiveDayTemperatures(self,dates,temps):
        self.ax.plot(dates[::8], temps[::8], color="green")
        self.ax.set_title("5 Days Weather Forecast")
        self.ax.set_xlabel("Dates")
        self.ax.set_ylabel("Temperatures (\u00b0C)")
        self.ax.grid(True)
        self.canvas.draw()
    

    def fiveDayTemps(self,dates,min_temps,temps,max_temps):
        self.ax.stackplot(dates[::8], min_temps[::8], temps[::8], max_temps[::8], labels=['Dataset 1', 'Dataset 2', 'Dataset 3'])
        ax.legend(loc='upper left')
        ax.xlabel('Temperatures (\u00b0C)')
        ax.ylabel('Y-axis Label')
        ax.title('5 Days Min-Actual-Max Tempertures')
        self.ax.grid(True)
        self.canvas.draw()

    def fiveDayArea(self,dataframe):
        dataframe.area(stacked=False)
        self.canvas.draw()

        

                     

    def oneDayForecast(self,dataframe):
        # Load your DataFrame
        df = dataframe

        # Extract features and target variable

        date_times = np.array([x for x in range(0,24*5,3)])
        X = date_times.reshape(-1,1)
        y = df['Temperature'].values

        # Scale features to the range [0, 1]
        scaler = MinMaxScaler()
        X_scaled = scaler.fit_transform(X)

        # Build the neural network model
        model = Sequential()
        model.add(Dense(64, activation='relu', input_dim=1))
        model.add(Dense(128, activation='relu'))
        model.add(Dense(1))  # 1 output neuron for temperature prediction

        # Compile the model
        model.compile(optimizer='adam', loss='mean_squared_error')

        # Train the model on the entire dataset
        model.fit(X_scaled, y, epochs=100, batch_size=8, verbose=1)

        # Generate time points for 24 hours
        time_points = np.linspace(0, 24, num=24)  # 24 intervals for each hour
        time_points = time_points.reshape(-1, 1)

        # Scale the time points
        scaled_time_points = scaler.transform(time_points)

        # Predict temperature values at the time points
        predicted_temperatures = model.predict(scaled_time_points)

        # Inverse transform the predicted temperatures to get them back to the original scale


        # Plotting
        self.ax.plot(time_points, predicted_temperatures, label='Predicted Temperature')
        self.ax.set_xlabel('Time (hours)')
        self.ax.set_ylabel('Temperature')
        self.ax.set_title('Predicted Temperature from 0 to 24 Hours')
        self.ax.grid(True)
        self.canvas.legend()
        
        
