from abc import ABC, abstractmethod

class EncodingStrategy(ABC):
    @abstractmethod
    def encode(self, X):
        pass
