from sklearn.preprocessing import StandardScaler, MinMaxScaler
from preprocessing_strategy import PreprocessingStrategy

class StandardScalingStrategy(PreprocessingStrategy):
    def __init__(self):
        self.scaler = StandardScaler()
    
    def preprocess(self, X):
        return self.scaler.fit_transform(X)

class MinMaxScalingStrategy(PreprocessingStrategy):
    def __init__(self):
        self.scaler = MinMaxScaler()
    
    def preprocess(self, X):
        return self.scaler.fit_transform(X)
