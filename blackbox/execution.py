from blackbox.portfolio import PortfolioConstructionModel


class ExecutionModel(object):
    """ The current portfolio reflects the positions the quant trader currently owns. After running the portfolio construction model, the quant trader generates the new target portfolio weights, shown in the New Target Portfolio column. The difference between the two indicates the trades that now need to be executed, which is the job of the execution algorithm. The execution algorithm takes the required trades and, using various other inputs such as the urgency with which the trades need to be executed and the dynamics of the liquidity in the markets, executes trades in an efficient and low-cost manner. """

    def __init__(self):
        pass
