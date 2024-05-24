from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from encoding_strategy import EncodingStrategy

class OneHotEncodingStrategy(EncodingStrategy):
    def __init__(self):
        self.encoder = OneHotEncoder(sparse=False)
    
    def encode(self, X):
        return self.encoder.fit_transform(X)

class LabelEncodingStrategy(EncodingStrategy):
    def __init__(self):
        self.encoder = LabelEncoder()
    
    def encode(self, X):
        return self.encoder.fit_transform(X)
