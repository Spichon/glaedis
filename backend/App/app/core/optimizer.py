import pandas as pd
from pypfopt import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns

def markov_optimize(df: pd.DataFrame = None) -> []:
    avg_returns = expected_returns.mean_historical_return(df)
    cov_mat = risk_models.sample_cov(df)
    ef = EfficientFrontier(avg_returns, cov_mat)
    weights = ef.max_sharpe()
    cleaned_weights = ef.clean_weights()
    return cleaned_weights
