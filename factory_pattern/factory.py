from regressor import LinearRegressor, DecisionTreeRegressorModel, RandomForestRegressorModel
class RegressorFactory:
    @staticmethod
    def create_regressor(regressor_type):
        if regressor_type == 'linear':
            return LinearRegressor()
        elif regressor_type == 'decision_tree':
            return DecisionTreeRegressorModel()
        elif regressor_type == 'random_forest':
            return RandomForestRegressorModel()
        else:
            raise ValueError("Invalid regressor type provided")
