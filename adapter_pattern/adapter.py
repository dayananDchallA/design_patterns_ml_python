from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

# Existing code that expects a specific interface
class Model:
    def fit(self, X, y):
        raise NotImplementedError()

    def predict(self, X):
        raise NotImplementedError()

# Adapter for scikit-learn's LinearRegression
class SklearnAdapter(Model):
    def __init__(self, model):
        self.model = model

    def fit(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

# Adapter for statsmodels' OLS
class StatsmodelsAdapter(Model):
    def __init__(self, model):
        self.model = model

    def fit(self, X, y):
        self.model = self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

# Example usage
X = [[1], [2], [3]]
y = [1, 2, 3]

# Using sklearn's LinearRegression
sklearn_model = LinearRegression()
sklearn_adapter = SklearnAdapter(sklearn_model)
sklearn_adapter.fit(X, y)
print("Sklearn prediction:", sklearn_adapter.predict([[4]]))

# Using statsmodels' OLS
statsmodels_model = sm.OLS(y, sm.add_constant(X))
statsmodels_adapter = StatsmodelsAdapter(statsmodels_model)
statsmodels_adapter.fit(X, y)
print("Statsmodels prediction:", statsmodels_adapter.predict([[4, 1]]))
