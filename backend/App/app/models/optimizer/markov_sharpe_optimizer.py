from app.models import Optimizer
from app.core.markov_optimizer import findMaxSharpeRatioPortfolio


class Markov_sharpe_optimizer(Optimizer):
    __tablename__ = None

    __mapper_args__ = {
        'polymorphic_identity': 'Max_profit'
    }

    def get_weights(self, portfolio, returns):
        meanDailyReturns = returns.mean()
        covMatrix = returns.cov()
        riskFreeRate = portfolio.risk_free
        maxSharpe = findMaxSharpeRatioPortfolio(meanDailyReturns, covMatrix, riskFreeRate)
        return maxSharpe['x']
