from encoding_strategies import OneHotEncodingStrategy, LabelEncodingStrategy

class EncodingFactory:
    @staticmethod
    def create_encoding_strategy(strategy_type: str):
        if strategy_type == 'onehot_encoding':
            return OneHotEncodingStrategy()
        elif strategy_type == 'label_encoding':
            return LabelEncodingStrategy()
        else:
            raise ValueError(f"Unknown encoding strategy type: {strategy_type}")
