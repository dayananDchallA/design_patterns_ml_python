'''
Explanation
1. preprocessing_strategy.py: Defines the PreprocessingStrategy interface.
2. encoding_strategy.py: Defines the EncodingStrategy interface.
3. scaling_strategies.py: Implements concrete strategies for scaling (standard scaling and min-max scaling).
4. encoding_strategies.py: Implements concrete strategies for encoding (one-hot encoding and label encoding).
5. data_preprocessing_context.py: Defines the DataPreprocessingContext class that uses preprocessing and encoding strategies.
6. main.py: Contains the main workflow, demonstrating how to use the context and strategies for data preprocessing and encoding in a machine learning pipeline.
These file names and structures will help keep the code organized and maintainable, making it easy to extend or modify individual components without affecting the entire system.
'''

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np
from data_preprocessing_context import DataPreprocessingContext
from scaling_strategies import StandardScalingStrategy, MinMaxScalingStrategy
from encoding_strategies import OneHotEncodingStrategy, LabelEncodingStrategy

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Example: Adding a categorical feature for demonstration
np.random.seed(42)
categorical_feature = np.random.choice(['A', 'B', 'C'], size=X.shape[0])
X = np.column_stack((X, categorical_feature))

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Separate numerical and categorical features
X_train_num = X_train[:, :-1]
X_train_cat = X_train[:, -1].reshape(-1, 1)
X_test_num = X_test[:, :-1]
X_test_cat = X_test[:, -1].reshape(-1, 1)

# Initialize context with Standard Scaling and OneHot Encoding strategies
context = DataPreprocessingContext(StandardScalingStrategy(), OneHotEncodingStrategy())
X_train_num_scaled = context.preprocess(X_train_num)
X_test_num_scaled = context.preprocess(X_test_num)
X_train_cat_encoded = context.encode(X_train_cat)
X_test_cat_encoded = context.encode(X_test_cat)

# Combine numerical and encoded categorical features
X_train_preprocessed = np.hstack((X_train_num_scaled, X_train_cat_encoded))
X_test_preprocessed = np.hstack((X_test_num_scaled, X_test_cat_encoded))

# Train and evaluate model
model = LogisticRegression()
model.fit(X_train_preprocessed, y_train)
predictions = model.predict(X_test_preprocessed)
print(f'Accuracy with Standard Scaling and OneHot Encoding: {accuracy_score(y_test, predictions)}')

# Change strategies to MinMax Scaling and Label Encoding
context.set_preprocessing_strategy(MinMaxScalingStrategy())
context.set_encoding_strategy(LabelEncodingStrategy())
X_train_num_scaled = context.preprocess(X_train_num)
X_test_num_scaled = context.preprocess(X_test_num)
X_train_cat_encoded = context.encode(X_train_cat.ravel()).reshape(-1, 1)
X_test_cat_encoded = context.encode(X_test_cat.ravel()).reshape(-1, 1)

# Combine numerical and encoded categorical features
X_train_preprocessed = np.hstack((X_train_num_scaled, X_train_cat_encoded))
X_test_preprocessed = np.hstack((X_test_num_scaled, X_test_cat_encoded))

# Retrain and evaluate model
model.fit(X_train_preprocessed, y_train)
predictions = model.predict(X_test_preprocessed)
print(f'Accuracy with MinMax Scaling and Label Encoding: {accuracy_score(y_test, predictions)}')
