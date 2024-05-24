'''
Explanation
1. Strategy Interfaces:
PreprocessingStrategy and EncodingStrategy define the common interfaces for preprocessing and encoding strategies.

2. Concrete Strategies:
StandardScalingStrategy and MinMaxScalingStrategy implement PreprocessingStrategy.
OneHotEncodingStrategy and LabelEncodingStrategy implement EncodingStrategy.

3. Factory Classes:
PreprocessingFactory and EncodingFactory are responsible for creating instances of preprocessing and encoding strategies based on the provided type.

4. Context Class:
DataPreprocessingContext uses both a PreprocessingStrategy and an EncodingStrategy. It allows switching strategies at runtime using set_preprocessing_strategy and set_encoding_strategy.

5. Usage:
main.py demonstrates how to use the context and factories to dynamically create and switch between different preprocessing and encoding strategies during a machine learning workflow.

This approach allows for flexible and extensible code where both the preprocessing and encoding techniques can be changed dynamically without modifying the core logic of the data processing pipeline. 
The Factory Pattern is used to encapsulate the instantiation logic, while the Strategy Pattern is used to define and switch between different algorithms or behaviors at runtime.
'''

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np
from data_preprocessing_context import DataPreprocessingContext
from preprocessing_factory import PreprocessingFactory
from encoding_factory import EncodingFactory

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

# Create strategies using factories
preprocessing_strategy = PreprocessingFactory.create_preprocessing_strategy('standard_scaling')
encoding_strategy = EncodingFactory.create_encoding_strategy('onehot_encoding')

# Initialize context with created strategies
context = DataPreprocessingContext(preprocessing_strategy, encoding_strategy)
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

# Change strategies to MinMax Scaling and Label Encoding using factories
preprocessing_strategy = PreprocessingFactory.create_preprocessing_strategy('minmax_scaling')
encoding_strategy = EncodingFactory.create_encoding_strategy('label_encoding')

# Update context with new strategies
context.set_preprocessing_strategy(preprocessing_strategy)
context.set_encoding_strategy(encoding_strategy)
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
