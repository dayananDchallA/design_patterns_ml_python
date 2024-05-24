from scaling_strategies import StandardScalingStrategy, MinMaxScalingStrategy

class PreprocessingFactory:
    @staticmethod
    def create_preprocessing_strategy(strategy_type: str):
        if strategy_type == 'standard_scaling':
            return StandardScalingStrategy()
        elif strategy_type == 'minmax_scaling':
            return MinMaxScalingStrategy()
        else:
            raise ValueError(f"Unknown preprocessing strategy type: {strategy_type}")
