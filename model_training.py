# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Load engineered data
data = pd.read_csv('engineered_features.csv')

# Define features and target
X = data.drop(['Date', 'PM2.5'], axis=1)  # Replace 'PM2.5' with target column
y = data['PM2.5']

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
rmse = mean_squared_error(y_test, y_pred, squared=False)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Model Evaluation: RMSE={rmse}, MAE={mae}, R²={r2}")

# Save the model
import joblib
joblib.dump(model, 'random_forest_model.pkl')
print("Model saved as 'random_forest_model.pkl'.")
