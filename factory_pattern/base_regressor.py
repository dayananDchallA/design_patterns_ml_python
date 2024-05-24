from abc import ABC, abstractmethod

class BaseRegressor(ABC):
    @abstractmethod
    def fit(self, X, y):
        pass

    @abstractmethod
    def predict(self, X):
        pass
