from preprocessing_strategy import PreprocessingStrategy
from encoding_strategy import EncodingStrategy

class DataPreprocessingContext:
    def __init__(self, preprocessing_strategy: PreprocessingStrategy, encoding_strategy: EncodingStrategy):
        self.preprocessing_strategy = preprocessing_strategy
        self.encoding_strategy = encoding_strategy
    
    def set_preprocessing_strategy(self, strategy: PreprocessingStrategy):
        self.preprocessing_strategy = strategy
    
    def set_encoding_strategy(self, strategy: EncodingStrategy):
        self.encoding_strategy = strategy
    
    def preprocess(self, X):
        return self.preprocessing_strategy.preprocess(X)
    
    def encode(self, X):
        return self.encoding_strategy.encode(X)
