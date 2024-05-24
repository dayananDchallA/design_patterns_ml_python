from abc import ABC, abstractmethod

class PreprocessingStrategy(ABC):
    @abstractmethod
    def preprocess(self, X):
        pass
