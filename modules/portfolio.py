from modules.broker import Oanda
from modules.alpha import AlphaModel
from modules.risk import RiskModel
from modules.cost import TransactionCostModel


class PortfolioConstructionModel(object):
    """ The alpha, risk, and transaction cost models then feed into a portfolio construction model, which balances the tradeoffs presented by the pursuit of profits, the limiting of risk, and the costs associated with both, thereby determining the best portfolio to hold. Having made this determination, the system can compare the current portfolio to the new target portfolio, with the differences between the current portfolio and the target portfolio representing the trades that need to be executed. """

    def __init__(self):
        pass
