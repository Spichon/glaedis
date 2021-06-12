from app.models import Optimizer
from app.core.markov_optimizer import findMinVariancePortfolio

class Markov_volatility_optimizer(Optimizer):
    __tablename__ = None
    __mapper_args__ = {
        'polymorphic_identity': 'Min_risk'
    }

    def get_weights(self, portfolio, returns):
        meanDailyReturns = returns.mean()
        covMatrix = returns.cov()
        minVar = findMinVariancePortfolio(meanDailyReturns, covMatrix)
        return minVar['x']
