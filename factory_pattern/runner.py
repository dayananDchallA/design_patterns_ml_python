from factory import RegressorFactory
# Example usage:
import numpy as np

# Create a sample dataset (X: features, y: target variable)
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
y = np.array([2.5, 3.5, 4.5, 5.5])

# Choose the regressor type: 'linear', 'decision_tree', or 'random_forest'
regressor_type = 'linear'

# Create the regressor using the factory
regressor = RegressorFactory.create_regressor(regressor_type)

# Fit the regressor to the data
regressor.fit(X, y)

# Make predictions
predictions = regressor.predict(X)
print(f"Predictions using {regressor_type} regressor: {predictions}")
