# Import necessary libraries
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load air quality data
air_quality = pd.read_csv('air_quality_data.csv')  # Replace with actual file path
weather = pd.read_csv('weather_data.csv')  # Replace with actual file path

# Handle missing values
air_quality.fillna(air_quality.median(), inplace=True)
weather.fillna(weather.median(), inplace=True)

# Merge datasets
air_quality['Date'] = pd.to_datetime(air_quality['Date'])
weather['Date'] = pd.to_datetime(weather['Date'])
data = pd.merge(air_quality, weather, on='Date')

# Normalize numerical features
scaler = MinMaxScaler()
columns_to_scale = ['PM2.5', 'PM10', 'NO₂', 'Temperature', 'Humidity', 'Wind Speed']
data[columns_to_scale] = scaler.fit_transform(data[columns_to_scale])

# Save preprocessed data
data.to_csv('preprocessed_data.csv', index=False)
print("Preprocessing completed. Data saved to 'preprocessed_data.csv'.")
