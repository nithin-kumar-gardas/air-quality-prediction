## Project Code Description

### Files Included:
1. **data_preprocessing.py**:
   - Handles data cleaning, normalization, and merging air quality and weather datasets.
   - Saves the preprocessed data to a CSV file.

2. **feature_engineering.py**:
   - Adds time-based features (day, month, year) and calculated variables (e.g., Heat Index).
   - Saves the engineered data to a CSV file.

3. **model_training.py**:
   - Implements a Random Forest model for predicting PM2.5 levels.
   - Evaluates the model using RMSE, MAE, and R² metrics.
   - Saves the trained model for future use.

### Instructions to Run:
1. Clone this repository:
   ```bash
   git clone https://github.com/nithin-kumar-gardas/air-quality-prediction.git
