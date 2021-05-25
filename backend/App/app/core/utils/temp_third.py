import ccxt
import pandas as pd
import bt
from functools import reduce
from pypfopt import EfficientFrontier, discrete_allocation, objective_functions
from pypfopt import risk_models
from pypfopt import expected_returns
import numpy as np

kraken = getattr(ccxt, 'kraken')()
assets = ['ALGO/EUR', 'OXT/EUR', 'USDC/EUR']


def get_ohclh(asset, ticker="15m"):
    ohlcv = kraken.fetch_ohlcv(asset, ticker)
    columns = ['time', 'open', 'high', 'low', 'close', 'volume']
    df = pd.DataFrame(ohlcv, columns=columns)
    df = df.astype(float)
    df['time'] = pd.to_datetime(df['time'].astype(int), unit='ms')
    df = df.set_index('time')
    return df


def optimize(df: pd.DataFrame = None) -> []:
    avg_returns = expected_returns.mean_historical_return(df)
    cov_mat = risk_models.sample_cov(df)
    ef = EfficientFrontier(avg_returns, cov_mat)
    weights = ef.max_sharpe()
    cleaned_weights = ef.clean_weights()
    return cleaned_weights


dfs = []
for asset in assets:
    result = get_ohclh(asset)
    result['{}'.format(asset)] = result['close']
    dfs.append(result['{}'.format(asset)])
if len(dfs) > 0:
    dfs = reduce(lambda df1, df2: pd.merge(df1, df2, left_index=True, right_index=True), dfs)

weights = optimize(dfs)
