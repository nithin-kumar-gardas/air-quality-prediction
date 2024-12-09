# Import necessary libraries
import pandas as pd

# Load preprocessed data
data = pd.read_csv('preprocessed_data.csv')

# Add time-based features
data['Day'] = pd.to_datetime(data['Date']).dt.day
data['Month'] = pd.to_datetime(data['Date']).dt.month
data['Year'] = pd.to_datetime(data['Date']).dt.year

# Create additional features (e.g., Heat Index)
data['Heat Index'] = data['Temperature'] * data['Humidity'] / 100

# Save engineered features
data.to_csv('engineered_features.csv', index=False)
print("Feature engineering completed. Data saved to 'engineered_features.csv'.")
