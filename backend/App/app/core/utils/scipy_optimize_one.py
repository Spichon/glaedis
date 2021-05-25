import scipy.optimize as sco
import ccxt
from functools import reduce
import pandas as pd
import numpy as np

kraken = getattr(ccxt, 'kraken')()
selected = ['ALGO/EUR', 'OXT/EUR', 'USDC/EUR', 'BTC/EUR', 'XRP/EUR', 'DOGE/EUR']

def get_ohclh(asset, ticker="1w"):
    ohlcv = kraken.fetch_ohlcv(asset, ticker)
    columns = ['time', 'open', 'high', 'low', 'close', 'volume']
    df = pd.DataFrame(ohlcv, columns=columns)
    df = df.astype(float)
    df['time'] = pd.to_datetime(df['time'].astype(int), unit='ms')
    df = df.set_index('time')
    return df

table = []
for asset in selected:
    result = get_ohclh(asset)
    result['{}'.format(asset)] = result['close']
    table.append(result['{}'.format(asset)])
if len(table) > 0:
    table = reduce(lambda df1, df2: pd.merge(df1, df2, left_index=True, right_index=True), table)

def calcPortfolioPerf(weights, meanReturns, covMatrix):
    '''
    Calculates the expected mean of returns and volatility for a portolio of
    assets, each carrying the weight specified by weights

    INPUT
    weights: array specifying the weight of each asset in the portfolio
    meanReturns: mean values of each asset's returns
    covMatrix: covariance of each asset in the portfolio

    OUTPUT
    tuple containing the portfolio return and volatility
    '''
    #Calculate return and variance
    portReturn = np.sum( meanReturns*weights )
    portStdDev = np.sqrt(np.dot(weights.T, np.dot(covMatrix, weights)))

    return portReturn, portStdDev

def negSharpeRatio(weights, meanReturns, covMatrix, riskFreeRate):
    '''
    Returns the negated Sharpe Ratio for the speicified portfolio of assets

    INPUT
    weights: array specifying the weight of each asset in the portfolio
    meanReturns: mean values of each asset's returns
    covMatrix: covariance of each asset in the portfolio
    riskFreeRate: time value of money
    '''
    p_ret, p_var = calcPortfolioPerf(weights, meanReturns, covMatrix)

    return -(p_ret - riskFreeRate) / p_var

def getPortfolioVol(weights, meanReturns, covMatrix):
    '''
    Returns the volatility of the specified portfolio of assets

    INPUT
    weights: array specifying the weight of each asset in the portfolio
    meanReturns: mean values of each asset's returns
    covMatrix: covariance of each asset in the portfolio

    OUTPUT
    The portfolio's volatility
    '''
    return calcPortfolioPerf(weights, meanReturns, covMatrix)[1]

def findMaxSharpeRatioPortfolio(meanReturns, covMatrix, riskFreeRate):
    '''
    Finds the portfolio of assets providing the maximum Sharpe Ratio

    INPUT
    meanReturns: mean values of each asset's returns
    covMatrix: covariance of each asset in the portfolio
    riskFreeRate: time value of money
    '''
    numAssets = len(meanReturns)
    args = (meanReturns, covMatrix, riskFreeRate)
    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    bounds = tuple( (0,1) for asset in range(numAssets))

    opts = sco.minimize(negSharpeRatio, numAssets*[1./numAssets,], args=args,
                        method='SLSQP', bounds=bounds, constraints=constraints)

    return opts

def findMinVariancePortfolio(meanReturns, covMatrix):
    '''
    Finds the portfolio of assets providing the lowest volatility

    INPUT
    meanReturns: mean values of each asset's returns
    covMatrix: covariance of each asset in the portfolio
    '''
    numAssets = len(meanReturns)
    args = (meanReturns, covMatrix)
    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    bounds = tuple( (0,1) for asset in range(numAssets))

    opts = sco.minimize(getPortfolioVol, numAssets*[1./numAssets,], args=args,
                        method='SLSQP', bounds=bounds, constraints=constraints)

    return opts


numAssets = len(selected)

#Calculate simple linear returns
returns = (table - table.shift(1)) / table.shift(1)

#Calculate individual mean returns and covariance between the stocks
meanDailyReturns = returns.mean()
covMatrix = returns.cov()
riskFreeRate=0.1

#Find portfolio with maximum Sharpe ratio
maxSharpe = findMaxSharpeRatioPortfolio(meanDailyReturns, covMatrix, riskFreeRate)
rp, sdp = calcPortfolioPerf(maxSharpe['x'], meanDailyReturns, covMatrix)

#Find portfolio with minimum variance
minVar = findMinVariancePortfolio(meanDailyReturns, covMatrix)
rp, sdp = calcPortfolioPerf(minVar['x'], meanDailyReturns, covMatrix)
